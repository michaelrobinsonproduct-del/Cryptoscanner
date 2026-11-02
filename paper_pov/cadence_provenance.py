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
EXECUTED = re.compile(r"(?:^|\n)(\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}(?:\.\d+)?Z) (PAPER_VERIFIED_GITHUB_EVENT|PAPER_VERIFIED_ORIGINATING_CRON|PAPER_PIPELINE_SOURCE_SHA)=([^\r\n]+)")


def timestamp(value):
    if not isinstance(value, str):
        raise ValueError("missing timestamp")
    result = dt.datetime.fromisoformat(value.replace("Z", "+00:00"))
    if result.tzinfo is None:
        raise ValueError("naive timestamp")
    return result.astimezone(UTC)


def provenance(log, earliest=None, latest=None):
    """Only unambiguous executed provenance lines are accepted.

    Optional bounds tie markers to the independently fetched GitHub writer
    job's start and the observation time; no bounds are invented if absent.
    """
    if not isinstance(log, str):
        return None
    found = {}
    marker_times = []
    marker_order = []
    for raw_time, key, value in EXECUTED.findall(log):
        if key in found:  # Never silently select one of two contradictory markers.
            return None
        try:
            marker_times.append(timestamp(raw_time))
        except (ValueError, TypeError, OverflowError):
            return None
        found[key] = value.strip()
        marker_order.append(key)
    if marker_order != ["PAPER_VERIFIED_GITHUB_EVENT",
                        "PAPER_VERIFIED_ORIGINATING_CRON",
                        "PAPER_PIPELINE_SOURCE_SHA"]:
        return None
    # Executed GitHub log markers should be chronological and close together.
    # Reject pasted/reordered historical fragments rather than joining them.
    if marker_times and (marker_times != sorted(marker_times) or
                         (marker_times[-1] - marker_times[0]).total_seconds() > 300):
        return None
    if marker_times and ((earliest is not None and marker_times[0] < earliest) or
                         (latest is not None and marker_times[-1] > latest)):
        return None
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
                and type(job.get("run_id")) is int and job["run_id"] == run_id
                and job.get("name") == "public-paper"]
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
            # A GitHub rerun keeps the original run ID/event/created_at but
            # is manually initiated later. It cannot certify an unattended slot.
            if type(run.get("run_attempt")) is not int or run["run_attempt"] != 1:
                evidence.append({"run_id": rid,
                                 "classification": "MISSING_OR_RERUN_ATTEMPT_PROVENANCE"})
                continue
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
            queue_seconds = writer_job_queue_seconds(jobs, rid, created, now)
            # If authentic job metadata is present, a log marker from before
            # the writer job began (or from the future) cannot certify this run.
            job_start = (created + dt.timedelta(seconds=queue_seconds)
                         if queue_seconds is not None else None)
            job_end = now
            # When GitHub supplies a canonical writer completion timestamp,
            # executed markers after that job ended cannot authenticate it.
            # Invalid supplied completion evidence abstains rather than
            # silently falling back to the wall-clock audit timestamp.
            if job_start is not None and isinstance(jobs, dict):
                matching_jobs = [j for j in jobs.get(str(rid), [])
                                 if isinstance(j, dict) and j.get("name") == "public-paper"
                                 and type(j.get("run_id")) is int and j["run_id"] == rid]
                if len(matching_jobs) == 1 and "completed_at" in matching_jobs[0]:
                    try:
                        job_end = timestamp(matching_jobs[0]["completed_at"])
                        if not job_start <= job_end <= now:
                            raise ValueError("incoherent writer completion")
                    except (ValueError, TypeError, OverflowError):
                        evidence.append({"run_id": rid,
                                         "classification": "INVALID_WRITER_JOB_COMPLETION"})
                        continue
            p = provenance(logs.get(str(rid)), earliest=job_start,
                           latest=job_end if job_start is not None else None)
            row = {"run_id": rid, "event": event, "created_at": created.isoformat(),
                   "conclusion": run.get("conclusion"), "classification": "UNVERIFIED_PROVENANCE"}
            if (p is None or p["PAPER_VERIFIED_GITHUB_EVENT"] != event
                    or p["PAPER_PIPELINE_SOURCE_SHA"] != run.get("head_sha")):
                evidence.append(row)
                continue
            if queue_seconds is not None:
                row["writer_job_queue_seconds"] = queue_seconds
                row["provenance_bound_to_writer_job_start"] = True
            row["verified_source_sha"] = p["PAPER_PIPELINE_SOURCE_SHA"]
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
    dispatched.sort(key=lambda r: r["created_at"])
    # This is only GitHub run-creation coverage, NOT proof of successful
    # persistence, quote freshness, delivery, or expected cron-slot identity.
    successful = sorted(native + dispatched, key=lambda r: r["created_at"])
    creation_times = [timestamp(r["created_at"]) for r in successful]
    latest_native = native[-1] if native else None
    latest_dispatch = dispatched[-1] if dispatched else None
    # Source equality is a necessary but NOT sufficient manual/schedule parity gate.
    source_match = (latest_native["verified_source_sha"] == latest_dispatch["verified_source_sha"]
                    if latest_native and latest_dispatch else None)
    # Same source code hours apart is not a meaningful paired-run comparison.
    # This is a time-comparability check only; it does not establish manual
    # origin, identical inputs, outcomes, or a successful persisted ledger.
    # Preserve subsecond precision at the 30-minute comparability boundary.
    cross_event_gap = (round(abs((timestamp(latest_native["created_at"]) -
                                  timestamp(latest_dispatch["created_at"])).total_seconds()), 3)
                       if latest_native and latest_dispatch else None)
    cross_event_comparable = (cross_event_gap <= 1800
                              if cross_event_gap is not None else None)
    max_creation_gap = max((round((b - a).total_seconds(), 3) for a, b in
                            zip(creation_times, creation_times[1:])), default=None)
    latest_age = int((now - creation_times[-1]).total_seconds()) if creation_times else None
    # Distinguish absence of any authenticated attempt from an attempted scan
    # that failed after starting. Neither is proof of durable persistence.
    attempts = sorted(native + dispatched + native_failed + dispatch_failed,
                      key=lambda r: r["created_at"])
    attempt_times = [timestamp(r["created_at"]) for r in attempts]
    latest_attempt_age = (int((now - attempt_times[-1]).total_seconds())
                          if attempt_times else None)
    max_attempt_gap = max((round((b - a).total_seconds(), 3) for a, b in
                           zip(attempt_times, attempt_times[1:])), default=None)
    # Find the most recent actual close-time, same-source native/dispatch
    # candidate, rather than pairing two unrelated latest executions.
    # This is NOT manual-origin or results-parity certification.
    candidate_pairs = []
    for n in native:
        for d in dispatched:
            gap = round(abs((timestamp(n["created_at"]) -
                             timestamp(d["created_at"])).total_seconds()), 3)
            if gap <= 1800 and n["verified_source_sha"] == d["verified_source_sha"]:
                candidate_pairs.append((
                    max(timestamp(n["created_at"]), timestamp(d["created_at"])),
                    -gap, n["run_id"], d["run_id"], gap, n["verified_source_sha"]))
    candidate_pairs.sort(reverse=True)
    latest_pair = ({"native_run_id": candidate_pairs[0][2],
                    "dispatch_run_id": candidate_pairs[0][3],
                    "creation_gap_seconds": candidate_pairs[0][4],
                    "verified_source_sha": candidate_pairs[0][5],
                    "manual_origin_verified": False,
                    "results_parity_verified": False}
                   if candidate_pairs else None)
    # Count nominal opportunities without inferring missed slots: GitHub does
    # not expose the originating hour for delayed schedule events.
    scheduled_opportunities = 0
    hour = cutoff.replace(minute=0, second=0, microsecond=0)
    while hour <= now:
        for minute in CRONS.values():
            slot = hour.replace(minute=minute)
            scheduled_opportunities += int(cutoff <= slot <= now)
        hour += dt.timedelta(hours=1)
    queue_samples = [r["writer_job_queue_seconds"] for r in successful
                     if "writer_job_queue_seconds" in r]
    evidence.sort(key=lambda r: (r.get("created_at", ""), str(r.get("run_id"))))
    return {"schema": 1, "checked_at": now.isoformat(), "lookback_hours": lookback_hours,
            "verified_native_count": len(native), "verified_dispatch_count": len(dispatched),
            "latest_native_source_sha": latest_native["verified_source_sha"] if latest_native else None,
            "latest_dispatch_source_sha": latest_dispatch["verified_source_sha"] if latest_dispatch else None,
            "latest_cross_event_source_sha_equal": source_match,
            "latest_cross_event_creation_gap_seconds": cross_event_gap,
            "latest_cross_event_within_30m": cross_event_comparable,
            "latest_time_comparable_same_source_pair": latest_pair,
            "time_comparable_same_source_pair_count": len(candidate_pairs),
            "scheduled_slot_opportunities_in_window": scheduled_opportunities,
            "verified_successful_writer_run_creation_count": len(successful),
            "last_verified_successful_run_created_at": successful[-1]["created_at"] if successful else None,
            "seconds_since_last_verified_successful_run_creation": latest_age,
            "max_verified_successful_run_creation_gap_seconds": max_creation_gap,
            "verified_attempt_run_creation_count": len(attempts),
            "last_verified_attempt_created_at": attempts[-1]["created_at"] if attempts else None,
            "seconds_since_last_verified_attempt_creation": latest_attempt_age,
            "max_verified_attempt_run_creation_gap_seconds": max_attempt_gap,
            "over_45m_since_verified_attempt_creation": (latest_attempt_age > 2700
                                                          if latest_attempt_age is not None else None),
            "writer_job_queue_sample_count": len(queue_samples),
            "max_verified_writer_job_queue_seconds": max(queue_samples, default=None),
            "over_45m_since_verified_successful_run_creation": latest_age > 2700 if latest_age is not None else None,
            "verified_native_unsuccessful_count": len(native_failed),
            "verified_dispatch_unsuccessful_count": len(dispatch_failed),
            "unverified_or_ambiguous_count": len(evidence) - len(native) - len(dispatched) - len(native_failed) - len(dispatch_failed),
            "native_minimum_lateness_seconds": [r["minimum_lateness_seconds"] for r in native],
            "runs": evidence,
            "limitations": ["Only the canonical main-branch PAPER writer workflow is counted; foreign workflow markers abstain",
                            "GitHub reruns preserve event=schedule but are not original unattended cron executions",
                            "Missing or noninitial run_attempt metadata abstains rather than certifying native cadence",
                            "A completed failed workflow is an attempt, not a successful scan",
                            "Attempt cadence includes authenticated failed executions but is not persisted scan cadence",
                            "A cron expression identifies a minute, not an hour; reported lateness is only a lower bound",
                            "Creation gaps are observational and cannot certify missed cron slots or persisted ledger generations",
                            "Created-at is not the job's completion time",
                            "Writer job queue delay is measured only from matching GitHub public-paper job started_at; missing metadata abstains",
                            "Job queue delay is separate from the native cron creation lateness lower bound",
                            "When authentic writer-job metadata exists, executed log markers must fall after its start and before audit time",
                            "Without writer-job metadata, executed log markers are not independently job-time-bound",
                            "A successful workflow is not durable ledger or remote SHA256 readback proof",
                            "workflow_dispatch alone does not distinguish owner manual from external recovery",
                            "Cross-event source SHA equality is necessary but never proves manual/unattended result parity",
                            "A cross-event pair more than 30 minutes apart is not time-comparable even if source SHAs match",
                            "Close-time same-source pairs are candidates only; dispatch origin and results parity remain unverified",
                            "Nominal slot opportunities are not a count of proven missed GitHub cron events"]}


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--runs", required=True)
    parser.add_argument("--logs", required=True, help="JSON object: run ID -> decoded job log")
    parser.add_argument("--jobs", help="Optional JSON object: run ID -> GitHub Actions job metadata list")
    parser.add_argument("--checked-at", required=True)
    parser.add_argument("--lookback-hours", type=int, default=24)
    parser.add_argument("--output", required=True)
    args = parser.parse_args()
    payload = json.loads(Path(args.runs).read_text())
    jobs = json.loads(Path(args.jobs).read_text()) if args.jobs else None
    report = audit(payload["workflow_runs"], json.loads(Path(args.logs).read_text()),
                   args.checked_at, args.lookback_hours, jobs=jobs)
    Path(args.output).write_text(json.dumps(report, sort_keys=True, indent=2) + "\n")
    print("PAPER_CADENCE_PROVENANCE " + json.dumps({k: v for k, v in report.items() if k != "runs"}, sort_keys=True))


if __name__ == "__main__":
    main()
