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
MIN_SUCCESS_AGE = dt.timedelta(minutes=70)
RETRY_INTERVAL = dt.timedelta(minutes=90)


def decide(runs_payload, comments, ledger, ledger_commit, ledger_message, now):
    """Only verified two-missed-slot evidence can authorize a request."""
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
    try:
        for item in runs:
            if not isinstance(item, dict) or item.get("event") not in ("schedule", "workflow_dispatch"):
                return abstain("RUN_EVENT_INVALID", True)
            if item.get("head_branch") != "main":
                return abstain("RUN_BRANCH_NOT_MAIN", True)
            if item.get("status") not in ACTIVE and item.get("status") != "completed":
                return abstain("RUN_STATUS_INVALID", True)
            at = instant(item["created_at"])
            if at > now + dt.timedelta(minutes=2):
                return abstain("FUTURE_RUN_TIMESTAMP", True)
            clean.append((at, item))
    except (ValueError, TypeError, KeyError, OverflowError):
        return abstain("RUN_METADATA_INVALID", True)
    clean.sort(key=lambda pair: pair[0], reverse=True)
    if any(x.get("status") in ACTIVE for _, x in clean):
        return abstain("SCANNER_ACTIVE_OR_QUEUED")
    completed = [(t, x) for t, x in clean if x.get("status") == "completed"]
    if not completed:
        return abstain("NO_COMPLETED_SCANNER_RUN", True)
    newest_at, newest = completed[0]
    if newest.get("conclusion") != "success":
        return abstain("LATEST_SCANNER_RUN_FAILED", True)
    if str(newest.get("id")) != str(latest_id) or newest.get("head_sha") != latest_record["source_sha"]:
        return abstain("LEDGER_NOT_LINKED_TO_NEWEST_SUCCESS", True)
    if latest_asof < newest_at - dt.timedelta(minutes=2):
        return abstain("LEDGER_ASOF_BEFORE_RUN", True)
    if now - newest_at < MIN_SUCCESS_AGE:
        return abstain("RECENT_SUCCESS")

    matured = scheduled_slots(now, 9, 30)
    if len(matured) < 2:
        return abstain("INSUFFICIENT_MATURED_SLOTS")
    scheduled_successes = [x for _, x in clean if x.get("event") == "schedule"
                           and x.get("status") == "completed" and x.get("conclusion") == "success"]
    matched = matched_scheduled_slots(scheduled_successes, now, 9, 30)
    if matured[0] in matched or matured[1] in matched:
        return abstain("MATURED_SLOT_COVERED")
    if newest_at >= matured[1]:
        return abstain("SUCCESS_AFTER_OLDER_MATURED_SLOT")
    result["missed_matured_slots"] = [x.isoformat() for x in matured[:2]]

    marker = RECOVERY_MARKER + ledger_commit
    for item in comments:
        if not isinstance(item, dict) or not isinstance(item.get("body"), str):
            return abstain("ISSUE_COMMENT_INVALID", True)
        if marker in item["body"]:
            try:
                at = instant(item["created_at"])
            except (ValueError, TypeError, KeyError):
                return abstain("RECOVERY_MARKER_TIMESTAMP_INVALID", True)
            if at > now + dt.timedelta(minutes=2):
                return abstain("RECOVERY_MARKER_IN_FUTURE", True)
            if now - at < RETRY_INTERVAL:
                return abstain("RECOVERY_ALREADY_ATTEMPTED")
    result.update(action="DISPATCH_EXISTING_WORKFLOW", reason="TWO_MATURED_SLOTS_MISSED",
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
