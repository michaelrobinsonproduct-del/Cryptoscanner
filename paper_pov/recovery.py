"""Fail-closed decision for requesting the EXISTING single-writer paper workflow.

Never scans, trades, changes the ledger or claims a dispatch was executed.
"""
import argparse
import datetime as dt
import hashlib
import json
import re
from pathlib import Path

from .ledger import verify
from .monitor import UTC, instant, matched_scheduled_slots, scheduled_slots
from .segmented_storage import MAX_RAW_BYTES

MESSAGE = re.compile(r"paper: (?:immutable|atomic packed) scan ([1-9][0-9]*) source ([0-9a-f]{40})")
SHA = re.compile(r"[0-9a-f]{40}")
ACTIVE = frozenset(("queued", "in_progress", "waiting", "requested", "pending"))
RECOVERY_MARKER = "PAPER_RECOVERY_ATTEMPT:"
MIN_SUCCESS_AGE = dt.timedelta(minutes=45)
RETRY_INTERVAL = dt.timedelta(minutes=90)


def decide(runs_payload, comments, ledger, ledger_commit, ledger_message, now):
    """Only verified missed-slot and durable-ledger evidence authorize a request."""
    result = {"schema": 1, "paper_only": True, "action": "BLOCKED",
              "reason": "UNVALIDATED", "checked_at": now.astimezone(UTC).isoformat(),
              "ledger_commit": ledger_commit, "latest_run_id": None,
              "missed_matured_slots": [], "source_sha": None}

    def abstain(reason, blocked=False):
        result.update(action="BLOCKED" if blocked else "NO_DISPATCH", reason=reason)
        return result

    if now.tzinfo is None:
        return abstain("NAIVE_CLOCK", True)
    now = now.astimezone(UTC)
    if not isinstance(runs_payload, dict) or not isinstance(runs_payload.get("workflow_runs"), list):
        return abstain("RUN_API_INVALID", True)
    if not SHA.fullmatch(ledger_commit or ""):
        return abstain("LEDGER_COMMIT_INVALID", True)
    if not isinstance(comments, list):
        return abstain("ISSUE_COMMENTS_UNAVAILABLE", True)
    try:
        state = verify(ledger, MAX_RAW_BYTES)
        if state["generation"] < 1 or not state["runs"]:
            return abstain("LEDGER_EMPTY_OR_UNVERIFIED", True)
        latest_record = state["runs"][-1]
        latest_asof = instant(latest_record["as_of"])
        if latest_asof > now + dt.timedelta(minutes=2):
            return abstain("LEDGER_FUTURE_ASOF", True)
        match = MESSAGE.fullmatch(ledger_message or "")
        if not match or match.group(2) != latest_record["source_sha"]:
            return abstain("LEDGER_COMMIT_PROVENANCE_MISMATCH", True)
        latest_id = int(match.group(1))
        result.update(latest_run_id=latest_id, source_sha=latest_record["source_sha"],
                      ledger_generation=state["generation"], ledger_as_of=latest_record["as_of"])
    except (ValueError, KeyError, TypeError, AttributeError, OverflowError) as exc:
        result["validation_error"] = str(exc)[:180]
        return abstain("LEDGER_INVALID", True)

    runs = runs_payload["workflow_runs"]
    if not runs:
        return abstain("NO_RUN_HISTORY", True)
    clean = []
    ignored_legacy_push = []
    try:
        for item in runs:
            if not isinstance(item, dict):
                return abstain("RUN_METADATA_INVALID", True)
            at = instant(item["created_at"])
            if at > now + dt.timedelta(minutes=2):
                return abstain("FUTURE_RUN_TIMESTAMP", True)
            event = item.get("event")
            if event not in ("schedule", "workflow_dispatch"):
                # The public workflow previously ran on push. Those historical
                # completed runs are NOT scanner writers, and must not disable
                # missed-slot recovery forever. Ignore ONLY an unambiguously
                # old, completed, identified-branch push predating the sealed ledger.
                # Unknown, active, newer or missing-branch events fail closed.
                if (event == "push" and isinstance(item.get("head_branch"), str)
                        and bool(item["head_branch"].strip())
                        and type(item.get("id")) is int and item["id"] > 0
                        and isinstance(item.get("head_sha"), str)
                        and SHA.fullmatch(item["head_sha"])
                        and item.get("status") == "completed"
                        and item.get("conclusion") in ("success", "failure", "cancelled")
                        and at < latest_asof - dt.timedelta(minutes=2)):
                    ignored_legacy_push.append(item.get("id"))
                    continue
                result["invalid_run_id"] = item.get("id")
                result["invalid_run_event"] = event
                return abstain("RUN_EVENT_INVALID", True)
            if item.get("head_branch") != "main":
                return abstain("RUN_BRANCH_NOT_MAIN", True)
            if item.get("status") not in ACTIVE and item.get("status") != "completed":
                return abstain("RUN_STATUS_INVALID", True)
            clean.append((at, item))
    except (ValueError, TypeError, KeyError, OverflowError):
        return abstain("RUN_METADATA_INVALID", True)
    result["ignored_historical_push_run_ids"] = ignored_legacy_push
    clean.sort(key=lambda pair: pair[0], reverse=True)
    if any(x.get("status") in ACTIVE for _, x in clean):
        return abstain("SCANNER_ACTIVE_OR_QUEUED")
    completed = [(t, x) for t, x in clean if x.get("status") == "completed"]
    if not completed:
        return abstain("NO_COMPLETED_SCANNER_RUN", True)
    newest_at, newest = completed[0]
    # The sealed ledger identifies the durable writer. A later failed run may
    # have stopped before its push; a failure after its push is itself sealed.
    # Neither situation justifies a permanent retry dead end.
    anchors = [(at, item) for at, item in completed if type(item.get("id")) is int
               and item["id"] == latest_id]
    if len(anchors) != 1:
        return abstain("LEDGER_RUN_NOT_FOUND_OR_DUPLICATE", True)
    anchor_at, anchor = anchors[0]
    if anchor.get("head_sha") != latest_record["source_sha"]:
        return abstain("LEDGER_NOT_LINKED_TO_RUN_SOURCE", True)
    if anchor.get("conclusion") not in ("success", "failure"):
        return abstain("LEDGER_ANCHOR_CONCLUSION_INVALID", True)
    if latest_asof < anchor_at - dt.timedelta(minutes=2):
        return abstain("LEDGER_ASOF_BEFORE_RUN", True)
    for at, item in completed:
        if item is anchor:
            continue
        if item.get("conclusion") not in ("success", "failure", "cancelled"):
            return abstain("RUN_CONCLUSION_INVALID", True)
        # GitHub timestamps have second resolution. Distinct runs created in
        # the same second cannot be ordered against the durable ledger anchor.
        # Never infer that an unlinked success/failure/cancellation is older.
        if at == anchor_at:
            return abstain("RUN_CREATED_AT_TIE_AMBIGUOUS", True)
        if at > anchor_at:
            # Only completed failed attempts may follow a durable anchor.
            # A newer unlinked success or ambiguous cancellation must block.
            if (item.get("conclusion") != "failure" or
                    type(item.get("id")) is not int or item["id"] <= 0 or
                    not isinstance(item.get("head_sha"), str) or
                    not SHA.fullmatch(item["head_sha"])):
                return abstain("NEWER_RUN_NOT_DURABLY_RECONCILED", True)
    result["latest_completed_run_id"] = newest.get("id")
    result["latest_completed_conclusion"] = newest.get("conclusion")
    result["durable_anchor_conclusion"] = anchor.get("conclusion")
    # Bounded retries: the latest failed attempt must also age >=45 minutes.
    if now - max(newest_at, latest_asof) < MIN_SUCCESS_AGE:
        return abstain("RECENT_ATTEMPT")

    matured = scheduled_slots(now, 9, 30)
    if not matured:
        return abstain("INSUFFICIENT_MATURED_SLOTS")
    scheduled_successes = [x for _, x in clean if x.get("event") == "schedule"
                           and x.get("status") == "completed" and x.get("conclusion") == "success"]
    matched = matched_scheduled_slots(scheduled_successes, now, 9, 30)
    if matured[0] in matched:
        return abstain("MATURED_SLOT_COVERED")
    # A successful scheduled OR recovery-dispatched scan after the missing
    # slot means we already have a newer durable scan; never double-dispatch.
    if max(anchor_at, latest_asof) >= matured[0]:
        return abstain("DURABLE_SCAN_AFTER_MATURED_SLOT")
    result["missed_matured_slots"] = [matured[0].isoformat()]

    marker = RECOVERY_MARKER + ledger_commit
    for item in comments:
        if not isinstance(item, dict) or not isinstance(item.get("body"), str):
            return abstain("ISSUE_COMMENT_INVALID", True)
        if marker in item["body"]:
            actor = item.get("user")
            # Public issue comments are untrusted; only the Actions bot can deduplicate.
            if not isinstance(actor, dict) or actor.get("login") != "github-actions[bot]" or actor.get("id") != 41898282:
                continue
            try:
                at = instant(item["created_at"])
            except (ValueError, TypeError, KeyError):
                return abstain("RECOVERY_MARKER_TIMESTAMP_INVALID", True)
            if at > now + dt.timedelta(minutes=2):
                return abstain("RECOVERY_MARKER_IN_FUTURE", True)
            if now - at < RETRY_INTERVAL:
                return abstain("RECOVERY_ALREADY_ATTEMPTED")
    result.update(action="DISPATCH_EXISTING_WORKFLOW", reason="MATURED_SLOT_MISSED",
                  attempt_marker=marker,
                  decision_sha256=hashlib.sha256((ledger_commit + "|" + str(latest_id) + "|" +
                  "|".join(result["missed_matured_slots"])).encode()).hexdigest())
    return result


def main():
    p = argparse.ArgumentParser()
    for name in ("runs", "comments", "ledger", "ledger-commit", "ledger-message", "output"):
        p.add_argument("--" + name, required=True)
    args = p.parse_args()
    try:
        data = decide(json.loads(Path(args.runs).read_text()),
                      [json.loads(line) for line in Path(args.comments).read_text().splitlines() if line.strip()],
                      json.loads(Path(args.ledger).read_text()),
                      Path(args.ledger_commit).read_text().strip(),
                      Path(args.ledger_message).read_text().strip(), dt.datetime.now(UTC))
    except (OSError, ValueError, TypeError) as exc:
        data = {"schema": 1, "paper_only": True, "action": "BLOCKED",
                "reason": "EVIDENCE_READ_FAILURE", "error": str(exc)[:180],
                "checked_at": dt.datetime.now(UTC).isoformat()}
    path = Path(args.output)
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(data, sort_keys=True, separators=(",", ":"), allow_nan=False) + "\n")
    print("PAPER_RECOVERY_DECISION " + json.dumps(data, sort_keys=True))
    if data["action"] == "BLOCKED":
        raise SystemExit(2)


if __name__ == "__main__":
    main()
