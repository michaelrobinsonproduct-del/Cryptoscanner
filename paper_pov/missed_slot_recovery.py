"""Bounded, fail-closed recovery decision for missed GitHub paper scan slots.

This module never trades, writes a ledger, or dispatches a workflow. Its caller
may dispatch the EXISTING single-writer paper-pipeline workflow only when a
scheduled slot has no matching run and no paper workflow is already active.
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


def main():
    import json
    import os
    import subprocess
    repo = os.environ["GITHUB_REPOSITORY"]
    # Fail closed if GitHub cannot return a complete authoritative response.
    def fetch_runs():
        raw = subprocess.check_output([
        "gh", "api", "-X", "GET", f"repos/{repo}/actions/workflows/paper-pipeline.yml/runs",
        "-f", "branch=main", "-f", "per_page=100",
    ], timeout=30)
        payload = json.loads(raw)
        if not isinstance(payload, dict) or not isinstance(payload.get("workflow_runs"), list):
            raise ValueError("Missing GitHub workflow run list")
        if payload.get("total_count", 0) > len(payload["workflow_runs"]) and len(payload["workflow_runs"]) >= 100:
            raise ValueError("GitHub workflow history truncated")
        return [{k: run[k] for k in ("event", "status", "created_at")}
                for run in payload["workflow_runs"]]

    first = decision(dt.datetime.now(UTC), fetch_runs())
    print(json.dumps({"phase": "initial", **first}, sort_keys=True), flush=True)
    if first["action"] != "DISPATCH":
        return
    # Re-query immediately before dispatch. An already queued scheduled run,
    # manual dispatch or another recovery attempt must suppress this one.
    second = decision(dt.datetime.now(UTC), fetch_runs())
    print(json.dumps({"phase": "pre_dispatch", **second}, sort_keys=True), flush=True)
    if second["action"] != "DISPATCH" or second["slot_utc"] != first["slot_utc"]:
        return
    subprocess.run(["gh", "workflow", "run", "paper-pipeline.yml",
                    "--ref", "main"], check=True, timeout=30)


if __name__ == "__main__":
    main()
