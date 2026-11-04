"""Bounded, fail-closed recovery decision for missed GitHub paper scan slots.

This module never trades or writes a ledger. Its CLI may dispatch the
EXISTING single-writer paper-pipeline workflow after bounded eligibility checks.
"""
import datetime as dt

UTC = dt.timezone.utc
SLOT_MINUTES = (9, 39)
GRACE = dt.timedelta(minutes=14)
MAX_AGE = dt.timedelta(minutes=40)
ACTIVE = {"queued", "in_progress", "waiting", "pending", "requested"}


def utc(value):
    parsed = dt.datetime.fromisoformat(value.replace("Z", "+00:00"))
    if parsed.tzinfo is None or parsed.utcoffset() is None:
        raise ValueError("Naive run timestamp")
    return parsed.astimezone(UTC)


def decision(now, runs):
    """Decide only the latest eligible :09/:39 UTC slot, never backfill prices.

    A completed failure counts as attempted; retrying after a partial ledger
    commit requires human inspection. Unknown/malformed API data aborts.
    """
    now = utc(now) if isinstance(now, str) else now
    if now.tzinfo is None or now.utcoffset() is None:
        raise ValueError("Naive current timestamp")
    now = now.astimezone(UTC)
    if not isinstance(runs, list):
        raise ValueError("Incomplete GitHub workflow runs")
    hour = now.replace(minute=0, second=0, microsecond=0)
    slots = [hour + dt.timedelta(minutes=m) for m in SLOT_MINUTES]
    slots += [hour - dt.timedelta(hours=1) + dt.timedelta(minutes=m) for m in SLOT_MINUTES]
    eligible = [s for s in slots if GRACE <= now - s <= MAX_AGE]
    if not eligible:
        return {"action": "WAIT", "reason": "No eligible bounded recovery slot"}
    slot = max(eligible)
    if len(runs) >= 100:
        raise ValueError("GitHub workflow run history may be truncated")
    checked = []
    for run in runs:
        if not isinstance(run, dict) or run.get("event") not in ("schedule", "workflow_dispatch"):
            raise ValueError("Unrecognized paper run evidence")
        if run.get("status") not in ACTIVE | {"completed"}:
            raise ValueError("Unrecognized paper run status")
        started = utc(run["created_at"])
        if started > now + dt.timedelta(minutes=1):
            raise ValueError("Future paper run timestamp")
        checked.append((started, run))
    if any(run["status"] in ACTIVE for _, run in checked):
        return {"action": "WAIT", "reason": "Single writer already queued or active"}
    # An attempted run after the slot is enough to prevent a second attempt,
    # even if the workflow failed after committing the ledger.
    if any(started >= slot for started, _ in checked):
        return {"action": "WAIT", "reason": "Slot already attempted"}
    return {"action": "DISPATCH", "slot_utc": slot.isoformat(),
            "reason": "No workflow run since eligible scheduled slot"}


def validate_recovery_slot(slot, event, now=None):
    """Validate explicit recovery provenance; never treat it as historic prices."""
    if not slot:
        return "NORMAL_SCAN"
    if event != "workflow_dispatch":
        raise ValueError("Recovery slot only allowed for manual dispatch event")
    stamp = utc(slot)
    if stamp.second or stamp.microsecond or stamp.minute not in SLOT_MINUTES:
        raise ValueError("Invalid scheduled slot identity")
    now = dt.datetime.now(UTC) if now is None else (utc(now) if isinstance(now, str) else now)
    age = now.astimezone(UTC) - stamp
    if not GRACE <= age <= MAX_AGE:
        raise ValueError("Recovery slot outside bounded freshness window")
    return stamp.isoformat()


def resolve_writer_slot(event, cron="", recovery_slot="", now=None):
    """Resolve a single ledger-serialized slot or refuse ambiguous late runs.

    GitHub does not supply the original scheduled fire timestamp. We therefore
    refuse delayed scheduled jobs rather than misattribute their live quotes.
    """
    now = dt.datetime.now(UTC) if now is None else (utc(now) if isinstance(now, str) else now)
    now = now.astimezone(UTC)
    if event == "workflow_dispatch":
        if cron:
            raise ValueError("Manual dispatch cannot assert originating cron")
        if recovery_slot:
            return validate_recovery_slot(recovery_slot, event, now)
        return None
    if event != "schedule" or recovery_slot:
        raise ValueError("Unrecognized or mixed slot provenance")
    minute = {"9 * * * *": 9, "39 * * * *": 39}.get(cron)
    if minute is None:
        raise ValueError("Unknown originating cron")
    candidate = now.replace(minute=minute, second=0, microsecond=0)
    if candidate > now:
        candidate -= dt.timedelta(hours=1)
    # A scheduled invocation that is substantially late must abstain rather
    # than claim a different slot or silently duplicate recovered evidence.
    if not dt.timedelta(0) <= now - candidate < dt.timedelta(minutes=25):
        raise ValueError("Delayed scheduled slot cannot be identified safely")
    return candidate.isoformat()


def inspect_slot(now, runs):
    """Read-only, bounded slot diagnosis. Never claims historical prices."""
    verdict = decision(now, runs)
    if verdict["action"] == "DISPATCH":
        return {"status": "MISSED_SLOT_RECOVERY_REQUIRED",
                "slot_utc": verdict["slot_utc"],
                "writer_dispatched": False, "ledger_persisted": False,
                "reason": "Main writer has no authorized recovery_slot_utc input"}
    return {"status": "NO_RECOVERY_DISPATCH", "reason": verdict["reason"],
            "writer_dispatched": False, "ledger_persisted": False}


def fetch_recent_runs(repo, *, now=None, command=None):
    """Fetch authenticated, complete workflow history with no mutation."""
    import json
    import subprocess
    now = dt.datetime.now(UTC) if now is None else now
    cutoff = (now - dt.timedelta(hours=2)).strftime("%Y-%m-%dT%H:%M:%SZ")
    args = ["gh", "api", "-X", "GET",
            f"repos/{repo}/actions/workflows/paper-pipeline.yml/runs",
            "-f", "branch=main", "-f", "per_page=100", "-f", "created=>=" + cutoff]
    raw = (command or subprocess.check_output)(args, timeout=30)
    payload = json.loads(raw)
    if (not isinstance(payload, dict) or not isinstance(payload.get("workflow_runs"), list)
            or not isinstance(payload.get("total_count"), int)
            or payload["total_count"] != len(payload["workflow_runs"])):
        raise ValueError("GitHub workflow history incomplete or truncated")
    return [{k: run[k] for k in ("event", "status", "created_at")}
            for run in payload["workflow_runs"]]


def main():
    """Operator visibility only; dispatch is deliberately not enabled.

    Main paper-pipeline.yml does not declare a recovery_slot_utc input.
    Sending an undeclared input would fail and cannot recover missed slots.
    """
    import json
    import os
    now = dt.datetime.now(UTC)
    try:
        runs = fetch_recent_runs(os.environ["GITHUB_REPOSITORY"], now=now)
        report = inspect_slot(now, runs)
    except (ValueError, KeyError, OSError, TimeoutError) as exc:
        report = {"status": "RECOVERY_EVIDENCE_UNAVAILABLE",
                  "error_type": type(exc).__name__, "writer_dispatched": False,
                  "ledger_persisted": False}
    report.update(schema="paper_missed_slot_observer_v1", observed_at=now.isoformat(),
                  production_applied=False)
    print(json.dumps(report, sort_keys=True), flush=True)
    if "GITHUB_OUTPUT" in os.environ:
        from pathlib import Path
        with Path(os.environ["GITHUB_OUTPUT"]).open("a") as out:
            out.write("recovery_status=" + report["status"] + "\\n")
    return report


if __name__ == "__main__":
    main()
