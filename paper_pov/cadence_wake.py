"""Independent owner-comment cadence gate for the EXISTING GitHub PAPER writer.

No market request, ledger mutation, or workflow dispatch happens in this module.
The workflow must recheck run/ledger/main state before and after its attempt marker.
"""
import argparse
import datetime as dt
import hashlib
import json
import re
from pathlib import Path

from .external_heartbeat_guard import (
    REPOSITORY, OWNER, OWNER_ID, ISSUE_NUMBER, REF, UTC,
    MAX_EVENT_AGE, CLOCK_SKEW, _owner_identity, _utc_timestamp,
)
from .ledger import verify
from .monitor import instant
from .recovery import MESSAGE, SHA, ACTIVE, RECOVERY_MARKER
from .segmented_storage import MAX_RAW_BYTES

COMMAND = "/paper-cadence-heartbeat"
WORKFLOW = "paper-pipeline.yml"
MARKER = "PAPER_CADENCE_ATTEMPT:"
MIN_SCAN_SPACING = dt.timedelta(minutes=25)
CADENCE = dt.timedelta(minutes=30)
MAX_SLOT_LATENESS = dt.timedelta(minutes=29)
RETRY_INTERVAL = dt.timedelta(minutes=45)
RECOVERY_RETRY_INTERVAL = dt.timedelta(minutes=90)
BOT = {"login": "github-actions[bot]", "id": 41898282}


def authorize(event, *, repository, actor, ref, event_name, now=None):
    """Require the immutable owner, exact issue, command, and recent event."""
    if not isinstance(event, dict):
        raise ValueError("Malformed issue_comment event")
    if (repository != REPOSITORY or actor != OWNER or
            ref != "refs/heads/main" or event_name != "issue_comment" or
            event.get("action") != "created"):
        raise ValueError("Untrusted GitHub event context")
    repo, issue, comment = (event.get(k) for k in ("repository", "issue", "comment"))
    if (not isinstance(repo, dict) or repo.get("full_name") != REPOSITORY or
            repo.get("default_branch") != REF or
            not _owner_identity(repo.get("owner")) or
            not isinstance(issue, dict) or type(issue.get("number")) is not int or
            issue["number"] != ISSUE_NUMBER or issue.get("pull_request") is not None or
            issue.get("state") != "open" or not isinstance(comment, dict) or
            type(comment.get("id")) is not int or comment["id"] <= 0 or
            comment.get("body") != COMMAND or
            comment.get("author_association") != "OWNER" or
            not _owner_identity(comment.get("user")) or
            not _owner_identity(event.get("sender"))):
        raise ValueError("Untrusted owner command or issue")
    current = dt.datetime.now(UTC) if now is None else now
    if not isinstance(current, dt.datetime) or current.tzinfo is None:
        raise ValueError("Naive authorization clock")
    timestamp = _utc_timestamp(comment.get("created_at"))
    if timestamp > current.astimezone(UTC) + CLOCK_SKEW or current.astimezone(UTC) - timestamp > MAX_EVENT_AGE:
        raise ValueError("Stale or future-dated command")
    return {"schema": 1, "paper_only": True, "action": "REQUEST_EXISTING_PAPER_WRITER_ONLY",
            "workflow": WORKFLOW, "ref": REF, "issue": ISSUE_NUMBER,
            "comment_id": comment["id"], "comment_created_at": timestamp.isoformat()}


def slot_at(now):
    now = now.astimezone(UTC)
    return now.replace(minute=30 if now.minute >= 30 else 0, second=0, microsecond=0)


def decide(runs_payload, comments, ledger, ledger_commit, ledger_message, main_sha, intent, now):
    """Fail closed on uncertain run/ledger identity, writer, timing or duplicate."""
    result = {"schema": 1, "paper_only": True, "action": "BLOCKED",
              "reason": "UNVALIDATED", "checked_at": None, "ledger_commit": ledger_commit}
    def abstain(reason, blocked=False):
        result.update(action="BLOCKED" if blocked else "NO_DISPATCH", reason=reason)
        return result
    if not isinstance(now, dt.datetime) or now.tzinfo is None:
        return abstain("NAIVE_CLOCK", True)
    now = now.astimezone(UTC)
    result["checked_at"] = now.isoformat()
    if (not isinstance(intent, dict) or intent.get("action") != "REQUEST_EXISTING_PAPER_WRITER_ONLY"
            or intent.get("workflow") != WORKFLOW or intent.get("ref") != REF or
            intent.get("paper_only") is not True or intent.get("issue") != ISSUE_NUMBER or
            type(intent.get("comment_id")) is not int or intent["comment_id"] <= 0):
        return abstain("UNAUTHORIZED_INTENT", True)
    if (not isinstance(runs_payload, dict) or
            not isinstance(runs_payload.get("workflow_runs"), list) or
            not isinstance(comments, list)):
        return abstain("API_EVIDENCE_UNAVAILABLE", True)
    if not SHA.fullmatch(ledger_commit or "") or not SHA.fullmatch(main_sha or ""):
        return abstain("SOURCE_OR_LEDGER_SHA_INVALID", True)
    try:
        state = verify(ledger, MAX_RAW_BYTES)
        if state["generation"] < 1 or not state["runs"]:
            return abstain("LEDGER_EMPTY", True)
        last = state["runs"][-1]
        last_at = instant(last["as_of"])
        match = MESSAGE.fullmatch(ledger_message or "")
        if not match or match.group(2) != last["source_sha"]:
            return abstain("LEDGER_PROVENANCE_MISMATCH", True)
        anchor_id = int(match.group(1))
        if last_at > now + CLOCK_SKEW:
            return abstain("LEDGER_FUTURE_ASOF", True)
        result.update(ledger_generation=state["generation"], ledger_as_of=last["as_of"],
                      anchor_run_id=anchor_id, source_sha=main_sha)
    except (ValueError, TypeError, KeyError, AttributeError, OverflowError) as exc:
        result["error"] = str(exc)[:180]
        return abstain("LEDGER_INVALID", True)
    runs = runs_payload["workflow_runs"]
    if not runs:
        return abstain("NO_RUN_HISTORY", True)
    clean = []
    try:
        for run in runs:
            if not isinstance(run, dict):
                return abstain("RUN_METADATA_INVALID", True)
            created = instant(run["created_at"])
            if created > now + CLOCK_SKEW:
                return abstain("FUTURE_RUN_TIMESTAMP", True)
            if run.get("event") not in ("schedule", "workflow_dispatch"):
                if (run.get("event") == "push" and
                        isinstance(run.get("head_branch"), str) and run["head_branch"].strip() and
                        type(run.get("id")) is int and run["id"] > 0 and
                        SHA.fullmatch(run.get("head_sha") or "") and
                        run.get("status") == "completed" and
                        run.get("conclusion") in ("success", "failure", "cancelled") and
                        created < last_at - CLOCK_SKEW):
                    continue
                return abstain("RUN_EVENT_INVALID", True)
            if run.get("head_branch") != REF:
                return abstain("RUN_BRANCH_INVALID", True)
            if run.get("status") not in ACTIVE and run.get("status") != "completed":
                return abstain("RUN_STATUS_INVALID", True)
            clean.append((created, run))
    except (KeyError, ValueError, TypeError, OverflowError):
        return abstain("RUN_METADATA_INVALID", True)
    if any(run.get("status") in ACTIVE for _, run in clean):
        return abstain("SCANNER_ACTIVE_OR_QUEUED")
    anchors = [(at, run) for at, run in clean if run.get("status") == "completed" and
               type(run.get("id")) is int and run["id"] == anchor_id]
    if len(anchors) != 1:
        return abstain("LEDGER_ANCHOR_MISSING_OR_DUPLICATE", True)
    anchor_at, anchor = anchors[0]
    if (anchor.get("head_sha") != last["source_sha"] or
            anchor.get("conclusion") not in ("success", "failure") or
            last_at < anchor_at - CLOCK_SKEW):
        return abstain("LEDGER_ANCHOR_INVALID", True)
    newest = max(anchor_at, last_at)
    for created, run in clean:
        if run is anchor or run.get("status") != "completed":
            continue
        if created == anchor_at:
            return abstain("RUN_CREATED_AT_TIE_AMBIGUOUS", True)
        if created > anchor_at:
            if (run.get("conclusion") != "failure" or
                    type(run.get("id")) is not int or run["id"] <= 0 or
                    not SHA.fullmatch(run.get("head_sha") or "")):
                return abstain("NEWER_RUN_NOT_DURABLY_RECONCILED", True)
            newest = max(newest, created)
        elif run.get("conclusion") not in ("success", "failure", "cancelled"):
            return abstain("RUN_CONCLUSION_INVALID", True)
    slot = slot_at(now)
    result["target_slot"] = slot.isoformat()
    if now - slot > MAX_SLOT_LATENESS:
        return abstain("CADENCE_SLOT_TOO_LATE")
    if last_at >= slot:
        return abstain("CADENCE_SLOT_ALREADY_DURABLE")
    if now - newest < MIN_SCAN_SPACING:
        return abstain("RECENT_SCAN_OR_ATTEMPT")
    for comment in comments:
        if not isinstance(comment, dict) or not isinstance(comment.get("body"), str):
            return abstain("ISSUE_COMMENT_INVALID", True)
        if comment.get("user") != BOT:
            continue
        marker, interval = None, None
        if MARKER + ledger_commit in comment["body"]:
            marker, interval = "CADENCE_ALREADY_ATTEMPTED", RETRY_INTERVAL
        elif RECOVERY_MARKER + ledger_commit in comment["body"]:
            marker, interval = "RECOVERY_ALREADY_ATTEMPTED", RECOVERY_RETRY_INTERVAL
        if marker:
            try:
                at = instant(comment["created_at"])
            except (ValueError, TypeError, KeyError):
                return abstain("ATTEMPT_MARKER_TIMESTAMP_INVALID", True)
            if at > now + CLOCK_SKEW:
                return abstain("ATTEMPT_MARKER_IN_FUTURE", True)
            if now - at < interval:
                return abstain(marker)
    result.update(action="DISPATCH_EXISTING_WORKFLOW", reason="INDEPENDENT_CADENCE_DUE",
                  attempt_marker=MARKER + ledger_commit,
                  decision_sha256=hashlib.sha256((ledger_commit + "|" + str(anchor_id) +
                  "|" + slot.isoformat() + "|" + main_sha).encode()).hexdigest())
    return result


def main():
    parser = argparse.ArgumentParser()
    for name in ("event", "repository", "actor", "ref", "event-name", "runs",
                 "comments", "ledger", "ledger-commit", "ledger-message",
                 "main-sha", "output"):
        parser.add_argument("--" + name, required=True)
    args = parser.parse_args()
    output = Path(args.output)
    output.unlink(missing_ok=True)
    now = dt.datetime.now(UTC)
    try:
        intent = authorize(json.loads(Path(args.event).read_text()),
                           repository=args.repository, actor=args.actor,
                           ref=args.ref, event_name=args.event_name, now=now)
        result = decide(json.loads(Path(args.runs).read_text()),
                        [json.loads(line) for line in Path(args.comments).read_text().splitlines() if line.strip()],
                        json.loads(Path(args.ledger).read_text()),
                        Path(args.ledger_commit).read_text().strip(),
                        Path(args.ledger_message).read_text().strip(),
                        Path(args.main_sha).read_text().strip(), intent, now)
    except (OSError, ValueError, TypeError, KeyError) as exc:
        result = {"schema": 1, "paper_only": True, "action": "BLOCKED",
                  "reason": "EVIDENCE_READ_OR_AUTH_FAILURE", "error": str(exc)[:180],
                  "checked_at": now.isoformat()}
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(json.dumps(result, sort_keys=True, separators=(",", ":"), allow_nan=False) + "\n")
    print("PAPER_CADENCE_DECISION " + json.dumps(result, sort_keys=True))
    if result["action"] == "BLOCKED":
        raise SystemExit(2)


if __name__ == "__main__":
    main()
