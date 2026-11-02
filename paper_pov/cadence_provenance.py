"""Read-only, source-authenticated PAPER cron-vs-dispatch cadence evidence.

GitHub Actions API created_at alone does NOT identify the originating cron.
The workflow's executed provenance step must be present in the job log;
otherwise this audit abstains. No scanner dispatches or repository writes.
"""
import argparse
from collections import Counter
import datetime as dt
import json
import re
from pathlib import Path

UTC = dt.timezone.utc
CRONS = {"9 * * * *": 9, "39 * * * *": 39}
WRITER_WORKFLOW = ".github/workflows/paper-pipeline.yml"
WRITER_BRANCH = "main"
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


def writer_job_queue_seconds(jobs, run_id, created, checked_at):
    """Bound queue delay to one authentic canonical writer job; otherwise abstain.

    GitHub run_started_at is not a substitute for the job's started_at.
    This does not establish nominal cron delivery or successful persistence.
    """
    if not isinstance(jobs, dict):
        return None
    candidates = jobs.get(str(run_id))
    if not isinstance(candidates, list):
        return None
    matching = [job for job in candidates if isinstance(job, dict)
                and job.get("run_id") == run_id and job.get("name") == "public-paper"]
    if len(matching) != 1:
        return None
    try:
        started = timestamp(matching[0]["started_at"])
        if started < created or started > checked_at:
            return None
        return round((started - created).total_seconds(), 3)
    except (ValueError, TypeError, KeyError, AttributeError):
        return None


def audit(runs, logs, checked_at, lookback_hours=24, jobs=None):
    """Report provable per-run minimum lateness; never assume cron hour.

    logs maps run ID (as string) to raw GitHub job log. Optional jobs maps
    run ID to GitHub job metadata for separately measured writer queue delay.
    The report does not
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
    # Duplicate run IDs invalidate every occurrence, not just the later one.
    # Otherwise a valid first occurrence could be counted despite conflicting input.
    id_counts = Counter(row.get("id") for row in runs if isinstance(row, dict)
                        and type(row.get("id")) is int)
    for run in runs:
        try:
            rid = run["id"]
            if type(rid) is not int or rid <= 0 or id_counts[rid] != 1:
                raise ValueError("duplicate/invalid run id")
            created = timestamp(run["created_at"])
            if created > now:
                raise ValueError("future run")
            if created < cutoff:
                continue
            event = run["event"]
            if event not in ("schedule", "workflow_dispatch"):
                continue
            # Printed provenance markers alone cannot authenticate a foreign
            # workflow or PR branch that happens to emit identical strings.
            if run.get("path") != WRITER_WORKFLOW or run.get("head_branch") != WRITER_BRANCH:
                evidence.append({"run_id": rid, "created_at": created.isoformat(),
                                 "classification": "WRONG_WORKFLOW_OR_REF"})
                continue
            if run.get("status") != "completed":
                evidence.append({"run_id": rid, "created_at": created.isoformat(),
                                 "classification": "INCOMPLETE_WORKFLOW"})
                continue
            if run.get("conclusion") not in ("success", "failure", "cancelled", "timed_out"):
                evidence.append({"run_id": rid, "created_at": created.isoformat(),
                                 "classification": "UNKNOWN_WORKFLOW_CONCLUSION"})
                continue
            successful = run["conclusion"] == "success"
            p = provenance(logs.get(str(rid)))
            row = {"run_id": rid, "event": event, "created_at": created.isoformat(),
                   "conclusion": run.get("conclusion"), "classification": "UNVERIFIED_PROVENANCE"}
            if (p is None or p["PAPER_VERIFIED_GITHUB_EVENT"] != event
                    or p["PAPER_PIPELINE_SOURCE_SHA"] != run.get("head_sha")):
                evidence.append(row)
                continue
            queue_seconds = writer_job_queue_seconds(jobs, rid, created, now)
            if queue_seconds is not None:
                row["writer_job_queue_seconds"] = queue_seconds
            cron = p["PAPER_VERIFIED_ORIGINATING_CRON"]
            if event == "workflow_dispatch":
                if cron == "MANUAL_DISPATCH":
                    row["classification"] = ("VERIFIED_WORKFLOW_DISPATCH_NOT_NATIVE"
                                             if successful else "VERIFIED_WORKFLOW_DISPATCH_UNSUCCESSFUL")
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
            row.update(classification=("VERIFIED_NATIVE_SCHEDULE" if successful
                                       else "VERIFIED_NATIVE_SCHEDULE_UNSUCCESSFUL"),
                       latest_possible_nominal_slot=nominal.isoformat(),
                       originating_hour_verified=False,
                       durable_ledger_verified=False)
            evidence.append(row)
        except (ValueError, TypeError, KeyError, AttributeError):
            evidence.append({"run_id": run.get("id") if isinstance(run, dict) else None,
                             "classification": "INVALID_RUN_METADATA"})
    native = [r for r in evidence if r["classification"] == "VERIFIED_NATIVE_SCHEDULE"]
    dispatched = [r for r in evidence if r["classification"] == "VERIFIED_WORKFLOW_DISPATCH_NOT_NATIVE"]
    native_failed = [r for r in evidence if r["classification"] == "VERIFIED_NATIVE_SCHEDULE_UNSUCCESSFUL"]
    dispatch_failed = [r for r in evidence if r["classification"] == "VERIFIED_WORKFLOW_DISPATCH_UNSUCCESSFUL"]
    native.sort(key=lambda r: r["created_at"])
    # This is only GitHub run-creation coverage, NOT proof of successful
    # persistence, quote freshness, delivery, or expected cron-slot identity.
    successful = sorted(native + dispatched, key=lambda r: r["created_at"])
    creation_times = [timestamp(r["created_at"]) for r in successful]
    max_creation_gap = max((int((b - a).total_seconds()) for a, b in
                            zip(creation_times, creation_times[1:])), default=None)
    latest_age = int((now - creation_times[-1]).total_seconds()) if creation_times else None
    queue_samples = [r["writer_job_queue_seconds"] for r in successful
                     if "writer_job_queue_seconds" in r]
    evidence.sort(key=lambda r: (r.get("created_at", ""), str(r.get("run_id"))))
    return {"schema": 1, "checked_at": now.isoformat(), "lookback_hours": lookback_hours,
            "verified_native_count": len(native), "verified_dispatch_count": len(dispatched),
            "verified_successful_writer_run_creation_count": len(successful),
            "last_verified_successful_run_created_at": successful[-1]["created_at"] if successful else None,
            "seconds_since_last_verified_successful_run_creation": latest_age,
            "max_verified_successful_run_creation_gap_seconds": max_creation_gap,
            "writer_job_queue_sample_count": len(queue_samples),
            "max_verified_writer_job_queue_seconds": max(queue_samples, default=None),
            "over_45m_since_verified_successful_run_creation": latest_age > 2700 if latest_age is not None else None,
            "verified_native_unsuccessful_count": len(native_failed),
            "verified_dispatch_unsuccessful_count": len(dispatch_failed),
            "unverified_or_ambiguous_count": len(evidence) - len(native) - len(dispatched) - len(native_failed) - len(dispatch_failed),
            "native_minimum_lateness_seconds": [r["minimum_lateness_seconds"] for r in native],
            "runs": evidence,
            "limitations": ["Only the canonical main-branch PAPER writer workflow is counted; foreign workflow markers abstain",
                            "A completed failed workflow is an attempt, not a successful scan",
                            "A cron expression identifies a minute, not an hour; reported lateness is only a lower bound",
                            "Creation gaps are observational and cannot certify missed cron slots or persisted ledger generations",
                            "Created-at is not the job's completion time",
                            "Writer job queue delay is measured only from matching GitHub public-paper job started_at; missing metadata abstains",
                            "Job queue delay is separate from the native cron creation lateness lower bound",
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
