"""Read-only, source-authenticated PAPER cron-vs-dispatch cadence evidence.

GitHub Actions API created_at alone does NOT identify the originating cron.
The workflow's executed provenance step must be present in the job log;
otherwise this audit abstains. No scanner dispatches or repository writes.
"""
import argparse
import datetime as dt
import json
import re
from pathlib import Path

UTC = dt.timezone.utc
CRONS = {"9 * * * *": 9, "39 * * * *": 39}
SHA = re.compile(r"[0-9a-f]{40}\Z")
# Match executed log output, not the shell's echoed source commands.
EXECUTED = re.compile(r"(?:^|\n)[^\n]*?Z (PAPER_VERIFIED_GITHUB_EVENT|PAPER_VERIFIED_ORIGINATING_CRON|PAPER_PIPELINE_SOURCE_SHA)=([^\r\n]+)")


def timestamp(value):
    if not isinstance(value, str):
        raise ValueError("missing timestamp")
    result = dt.datetime.fromisoformat(value.replace("Z", "+00:00"))
    if result.tzinfo is None:
        raise ValueError("naive timestamp")
    return result.astimezone(UTC)


def provenance(log):
    """Only unambiguous executed provenance lines are accepted."""
    if not isinstance(log, str):
        return None
    found = {}
    for key, value in EXECUTED.findall(log):
        if key in found:  # Never silently select one of two contradictory markers.
            return None
        found[key] = value.strip()
    if set(found) != {"PAPER_VERIFIED_GITHUB_EVENT", "PAPER_VERIFIED_ORIGINATING_CRON", "PAPER_PIPELINE_SOURCE_SHA"}:
        return None
    if not SHA.fullmatch(found["PAPER_PIPELINE_SOURCE_SHA"]):
        return None
    return found


def last_nominal_slot(created, minute):
    slot = created.replace(minute=minute, second=0, microsecond=0)
    if slot > created:
        slot -= dt.timedelta(hours=1)
    return slot


def audit(runs, logs, checked_at, lookback_hours=24):
    """Report provable per-run minimum lateness; never assume cron hour.

    logs maps run ID (as string) to raw GitHub job log. The report does not
    assume a completed job is a persisted ledger generation; that requires
    separate sealed ledger and remote readback verification.
    """
    now = timestamp(checked_at)
    if not 1 <= lookback_hours <= 168:
        raise ValueError("bounded lookback required")
    if not isinstance(runs, list) or not isinstance(logs, dict):
        raise ValueError("runs and logs must be structured inputs")
    cutoff = now - dt.timedelta(hours=lookback_hours)
    evidence = []
    ids = set()
    for run in runs:
        try:
            rid = run["id"]
            if type(rid) is not int or rid <= 0 or rid in ids:
                raise ValueError("duplicate/invalid run id")
            ids.add(rid)
            created = timestamp(run["created_at"])
            if created > now + dt.timedelta(minutes=2):
                raise ValueError("future run")
            if created < cutoff or created > now:
                continue
            event = run["event"]
            if event not in ("schedule", "workflow_dispatch"):
                continue
            p = provenance(logs.get(str(rid)))
            row = {"run_id": rid, "event": event, "created_at": created.isoformat(),
                   "conclusion": run.get("conclusion"), "classification": "UNVERIFIED_PROVENANCE"}
            if (p is None or p["PAPER_VERIFIED_GITHUB_EVENT"] != event
                    or p["PAPER_PIPELINE_SOURCE_SHA"] != run.get("head_sha")):
                evidence.append(row)
                continue
            cron = p["PAPER_VERIFIED_ORIGINATING_CRON"]
            if event == "workflow_dispatch":
                if cron == "MANUAL_DISPATCH":
                    row["classification"] = "VERIFIED_WORKFLOW_DISPATCH_NOT_NATIVE"
                evidence.append(row)
                continue
            if cron not in CRONS:
                evidence.append(row)
                continue
            nominal = last_nominal_slot(created, CRONS[cron])
            lower_bound = round((created - nominal).total_seconds(), 3)
            row.update(originating_cron=cron, minimum_lateness_seconds=lower_bound)
            # GitHub does not expose the scheduled hour. This is the *latest*
            # possible matching cron slot, never a proven originating slot.
            row.update(classification="VERIFIED_NATIVE_SCHEDULE",
                       latest_possible_nominal_slot=nominal.isoformat(),
                       originating_hour_verified=False)
            evidence.append(row)
        except (ValueError, TypeError, KeyError, AttributeError):
            evidence.append({"run_id": run.get("id") if isinstance(run, dict) else None,
                             "classification": "INVALID_RUN_METADATA"})
    native = [r for r in evidence if r["classification"] == "VERIFIED_NATIVE_SCHEDULE"]
    dispatched = [r for r in evidence if r["classification"] == "VERIFIED_WORKFLOW_DISPATCH_NOT_NATIVE"]
    native.sort(key=lambda r: r["created_at"])
    evidence.sort(key=lambda r: (r.get("created_at", ""), str(r.get("run_id"))))
    return {"schema": 1, "checked_at": now.isoformat(), "lookback_hours": lookback_hours,
            "verified_native_count": len(native), "verified_dispatch_count": len(dispatched),
            "unverified_or_ambiguous_count": len(evidence) - len(native) - len(dispatched),
            "native_minimum_lateness_seconds": [r["minimum_lateness_seconds"] for r in native],
            "runs": evidence,
            "limitations": ["A cron expression identifies a minute, not an hour; reported lateness is only a lower bound",
                            "Created-at is not the job's completion time",
                            "A successful workflow is not durable ledger or remote SHA256 readback proof",
                            "workflow_dispatch alone does not distinguish owner manual from external recovery"]}


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--runs", required=True)
    parser.add_argument("--logs", required=True, help="JSON object: run ID -> decoded job log")
    parser.add_argument("--checked-at", required=True)
    parser.add_argument("--lookback-hours", type=int, default=24)
    parser.add_argument("--output", required=True)
    args = parser.parse_args()
    payload = json.loads(Path(args.runs).read_text())
    report = audit(payload["workflow_runs"], json.loads(Path(args.logs).read_text()),
                   args.checked_at, args.lookback_hours)
    Path(args.output).write_text(json.dumps(report, sort_keys=True, indent=2) + "\n")
    print("PAPER_CADENCE_PROVENANCE " + json.dumps({k: v for k, v in report.items() if k != "runs"}, sort_keys=True))


if __name__ == "__main__":
    main()
