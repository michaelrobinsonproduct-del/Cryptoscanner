"""Independent, read-only GitHub paper scanner monitor.

This never executes a scanner, updates the ledger, or treats sampled paper
outcomes as exchange-complete or predictive lift.
"""
import argparse
import datetime as dt
import hashlib
import json
import re
from pathlib import Path

from .ledger import verify

UTC = dt.timezone.utc
GRACE = dt.timedelta(minutes=35)
RUN_WINDOW = dt.timedelta(minutes=55)
STUCK = dt.timedelta(minutes=45)
SHA40 = re.compile(r"[0-9a-f]{40}")
COMMIT_MESSAGE = re.compile(r"paper: immutable scan ([0-9]+) source ([0-9a-f]{40})")


def instant(value):
    if not isinstance(value, str):
        raise ValueError("Missing GitHub timestamp")
    parsed = dt.datetime.fromisoformat(value.replace("Z", "+00:00"))
    if parsed.tzinfo is None:
        raise ValueError("Naive GitHub timestamp")
    return parsed.astimezone(UTC)


def scheduled_slots(now, minute):
    current = now.astimezone(UTC).replace(minute=minute, second=0, microsecond=0)
    return [current - dt.timedelta(hours=i) for i in range(6)
            if current - dt.timedelta(hours=i) + GRACE <= now]


def assess_runs(payload, now, minute, prefix, alerts):
    if not isinstance(payload, dict) or not isinstance(payload.get("workflow_runs"), list):
        alerts.append(prefix + "_RUNS_UNAVAILABLE")
        return []
    runs = payload["workflow_runs"]
    scheduled = []
    for run in runs:
        try:
            if run.get("event") == "schedule":
                instant(run["created_at"])
                scheduled.append(run)
        except (KeyError, ValueError, TypeError):
            alerts.append(prefix + "_RUN_METADATA_INVALID")
    scheduled.sort(key=lambda x: instant(x["created_at"]), reverse=True)
    successes = [x for x in scheduled if x.get("status") == "completed"
                 and x.get("conclusion") == "success"]
    latest_success_at = instant(successes[0]["created_at"]) if successes else None
    if scheduled and scheduled[0].get("status") == "completed" and scheduled[0].get("conclusion") != "success":
        alerts.append(prefix + "_LATEST_SCHEDULED_FAILED")
    for run in scheduled:
        if run.get("status") in ("queued", "in_progress", "waiting") and now - instant(run["created_at"]) > STUCK:
            alerts.append(prefix + "_SCHEDULED_STUCK")
            break
    mature_slots = scheduled_slots(now, minute)
    if len(mature_slots) >= 2:
        last_two = mature_slots[:2]
        def successful_in(slot):
            return any(slot - dt.timedelta(minutes=5) <= instant(x["created_at"]) <= slot + RUN_WINDOW
                       for x in successes)
        if all(not successful_in(slot) for slot in last_two):
            alerts.append(prefix + "_TWO_MISSED_SLOTS")
    if not scheduled:
        alerts.append(prefix + "_NO_SCHEDULED_HISTORY")
    return runs


def evaluate(scan_payload, audit_payload, ledger, previous, ledger_commit,
             ledger_message, now, collection_errors=()):
    if now.tzinfo is None:
        raise ValueError("Monitor clock must be timezone aware")
    now = now.astimezone(UTC)
    alerts = ["PAPER_EVIDENCE_" + str(x) for x in collection_errors]
    scan_runs = assess_runs(scan_payload, now, 9, "PAPER_SCAN", alerts)
    assess_runs(audit_payload, now, 21, "PAPER_AUDIT", alerts)
    active = [x for x in scan_runs if x.get("status") in ("queued", "in_progress", "waiting")]
    if len(active) > 1:
        alerts.append("PAPER_MULTIPLE_ACTIVE_EXECUTIONS")
    metrics = {
        "scans_persisted": None, "predictions": None, "matured_labels": None,
        "gap_abstentions": None, "latest_scan_as_of": None,
        "max_client_quote_age_seconds": None, "client_quote_freshness_limit_seconds": 600,
        "exchange_event_freshness_verified": False, "ledger_commit": ledger_commit,
        "held_out_lift": None, "production_applied": False,
        "dex_status": "NOT_USED_NO_FRESHNESS_GATE",
        "paper_status": "PAPER_ONLY_NO_TRADES",
    }
    try:
        if not isinstance(ledger_commit, str) or not SHA40.fullmatch(ledger_commit):
            raise ValueError("Missing immutable ledger commit SHA")
        state = verify(ledger)
        if state["generation"] < 1 or not state["runs"]:
            raise ValueError("Missing persisted scans")
        last = state["runs"][-1]
        as_of = instant(last["as_of"])
        if as_of > now + dt.timedelta(minutes=2):
            raise ValueError("Future-dated paper run")
        obs = [o for o in state["observations"] if o["run_id"] == last["id"]]
        if not obs:
            raise ValueError("Missing latest run observations")
        ages = [(as_of - instant(o["at"])).total_seconds() for o in obs]
        if min(ages) < 0 or max(ages) > 600:
            raise ValueError("Client-observed quotes older than ten minutes")
        metrics.update({
            "scans_persisted": state["generation"],
            "predictions": state.get("archived", {}).get("predictions", 0) + len(state["predictions"]),
            "matured_labels": state.get("archived", {}).get("matured_labels", 0) +
                sum(x.get("status") == "MATURED_OBSERVED" for x in state["outcomes"]),
            "gap_abstentions": state.get("archived", {}).get("gap_abstentions", 0) +
                sum(x.get("status") == "ABSTAIN_GAP" for x in state["outcomes"]),
            "latest_scan_as_of": last["as_of"],
            "max_client_quote_age_seconds": round(max(ages), 3),
        })
        if previous is None:
            alerts.append("PAPER_PREVIOUS_LEDGER_UNAVAILABLE")
        else:
            old = verify(previous)
            if state["generation"] != old["generation"] + 1:
                alerts.append("PAPER_LEDGER_GENERATION_NONCONTIGUOUS")
            if old["runs"] and (len(state["runs"]) < 2 or state["runs"][-2] != old["runs"][-1]):
                alerts.append("PAPER_LEDGER_LAST_RUN_REWRITTEN")
        match = COMMIT_MESSAGE.fullmatch(ledger_message or "")
        if not match or match.group(2) != last["source_sha"]:
            alerts.append("PAPER_LEDGER_SOURCE_UNLINKED")
        else:
            source_run = next((x for x in scan_runs if str(x.get("id")) == match.group(1)), None)
            if source_run is None or source_run.get("head_sha") != last["source_sha"]:
                alerts.append("PAPER_LEDGER_RUN_UNLINKED")
            elif instant(source_run["created_at"]) > as_of + dt.timedelta(minutes=2):
                alerts.append("PAPER_LEDGER_ASOF_PRECEDES_RUN")
            newest_success = [x for x in scan_runs if x.get("status") == "completed"
                              and x.get("conclusion") == "success"]
            if newest_success and max(instant(x["created_at"]) for x in newest_success) > instant(source_run["created_at"]):
                alerts.append("PAPER_LEDGER_LAGGING_SUCCESSFUL_RUN")
    except (ValueError, TypeError, KeyError, IndexError, AttributeError, OverflowError) as exc:
        alerts.append("PAPER_LEDGER_INVALID")
        metrics["ledger_validation_error"] = str(exc)[:180]
    alerts = sorted(set(alerts))
    fingerprint = hashlib.sha256("|".join(alerts).encode()).hexdigest()[:16] if alerts else None
    return {
        "schema": 1, "monitor": "INDEPENDENT_GITHUB_PAPER_ONLY",
        "checked_at": now.isoformat(), "status": "ALERT" if alerts else "HEALTHY",
        "alerts": alerts, "alert_fingerprint": fingerprint, "metrics": metrics,
        "limitations": ["Client-observed ticker timestamps are not exchange trade-event timestamps",
                        "Hourly paper scans ordinarily abstain under the unchanged 45-minute gap gate",
                        "No unbiased held-out predictive improvement is established",
                        "GitHub issue delivery/readback does not prove email or push delivery"],
    }


def load_json(path):
    if not path:
        return None
    return json.loads(Path(path).read_text())


def main():
    parser = argparse.ArgumentParser()
    for name in ("scan-runs", "audit-runs", "ledger", "previous", "ledger-commit",
                 "ledger-message", "errors", "output"):
        parser.add_argument("--" + name, required=name not in ("previous", "errors"))
    args = parser.parse_args()
    errors = Path(args.errors).read_text().splitlines() if args.errors else []
    def safe_load(path, label):
        try:
            return load_json(path)
        except (OSError, ValueError) as exc:
            errors.append(label + "_UNAVAILABLE")
            return None
    result = evaluate(safe_load(args.scan_runs, "SCAN_API"),
                      safe_load(args.audit_runs, "AUDIT_API"),
                      safe_load(args.ledger, "LEDGER"),
                      safe_load(args.previous, "PREVIOUS") if args.previous else None,
                      Path(args.ledger_commit).read_text().strip() if Path(args.ledger_commit).exists() else "",
                      Path(args.ledger_message).read_text().strip() if Path(args.ledger_message).exists() else "",
                      dt.datetime.now(UTC), errors)
    output = Path(args.output)
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(json.dumps(result, sort_keys=True, separators=(",", ":"), allow_nan=False) + "\n")
    print("PAPER_INDEPENDENT_MONITOR " + json.dumps(result, sort_keys=True))


if __name__ == "__main__":
    main()
