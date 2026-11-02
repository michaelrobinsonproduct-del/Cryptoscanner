"""Bounded, read-only GitHub Actions evidence acquisition for PAPER cadence.

This is a reusable audit job, NOT a scheduler, recovery controller or writer.
Every HTTP request is GET. Missing or truncated evidence fails closed.
"""
import argparse
import datetime as dt
import hashlib
import json
import os
import re
from pathlib import Path
from urllib.parse import urlencode, urlsplit
from urllib.request import Request, urlopen, HTTPRedirectHandler, build_opener

from paper_pov.cadence_provenance import audit, timestamp

WORKFLOW = "paper-pipeline.yml"
MAX_PAGE = 100
MAX_LOG_BYTES = 4 * 1024 * 1024


# Log markers are writer claims, not independent remote-storage verification.
READBACK_MARKER = re.compile(
    r"^(\d{4}-\d{2}-\d{2}T[^ ]+Z) PAPER_LEDGER_REMOTE_READBACK_VERIFIED ([0-9a-f]{40})$")
RESULTS_MARKER = re.compile(
    r"^(\d{4}-\d{2}-\d{2}T[^ ]+Z) PAPER_RESULTS_VERIFIED (\d+) (\d+) (\d+)$")


def delivery_log_claim(log, run_id, started, finished):
    """Bound results/readback log claims to the authentic writer job.

    Test output can contain PAPER_RESULTS_VERIFIED for *other* run IDs.
    Such fixture claims are ignored. Duplicate current-run claims abstain.
    No result here verifies remote bytes, artifacts, or user delivery.
    """
    readbacks, results = [], []
    for line_index, line in enumerate(log.splitlines()):
        match = READBACK_MARKER.fullmatch(line)
        if match:
            readbacks.append((line_index, *match.groups()))
        match = RESULTS_MARKER.fullmatch(line)
        if match and match.group(2) == str(run_id):
            results.append((line_index, *match.groups()))
    if len(readbacks) != 1 or len(results) != 1:
        return {"delivery_log_claim_status": "UNVERIFIED"}
    # A log whose results marker physically precedes the readback marker
    # cannot prove results were published after remote persistence, even if
    # the embedded timestamps claim otherwise.
    if readbacks[0][0] >= results[0][0]:
        return {"delivery_log_claim_status": "UNVERIFIED"}
    try:
        _, rt, commit = readbacks[0]
        _, st, _, generation, watch = results[0]
        rt, st = timestamp(rt), timestamp(st)
        if not started <= rt <= st <= finished or int(generation) < 1 or int(watch) < 0:
            raise ValueError("incoherent delivery log claim")
    except (ValueError, TypeError, OverflowError):
        return {"delivery_log_claim_status": "UNVERIFIED"}
    return {"delivery_log_claim_status": "MATCHED_LOG_MARKERS_NOT_REMOTE_BYTES",
            "claimed_ledger_commit": commit, "claimed_generation": int(generation),
            "claimed_watch_count": int(watch),
            "remote_ledger_bytes_verified": False,
            "results_artifact_sha256_verified": False,
            "results_delivery_verified": False}


def artifact_metadata_claim(artifacts, run):
    """Verify GitHub artifact *metadata* identity, never archive contents.

    A matching digest is a GitHub assertion until ZIP bytes are downloaded,
    independently SHA256-hashed and ledger continuity is checked.
    """
    rid = run["id"]
    expected = {"public-paper-ledger-" + str(rid),
                "public-paper-results-" + str(rid)}
    if not isinstance(artifacts, list) or len(artifacts) != 2:
        return {"artifact_metadata_status": "UNVERIFIED"}
    names, ids, digests = set(), set(), {}
    for artifact in artifacts:
        if not isinstance(artifact, dict):
            return {"artifact_metadata_status": "UNVERIFIED"}
        name = artifact.get("name")
        source = artifact.get("workflow_run")
        digest = artifact.get("digest")
        if (name not in expected or name in names or
                (type(artifact.get("id")) is int and artifact["id"] in ids) or
                artifact.get("expired") is not False or
                type(artifact.get("id")) is not int or artifact["id"] <= 0 or
                type(artifact.get("size_in_bytes")) is not int or
                artifact["size_in_bytes"] <= 0 or
                not isinstance(source, dict) or
                type(source.get("id")) is not int or source["id"] != rid or
                source.get("head_sha") != run.get("head_sha") or
                source.get("head_branch") != "main" or
                not isinstance(digest, str) or
                not re.fullmatch(r"sha256:[0-9a-f]{64}", digest)):
            return {"artifact_metadata_status": "UNVERIFIED"}
        names.add(name)
        ids.add(artifact["id"])
        digests[name] = digest
    if names != expected:
        return {"artifact_metadata_status": "UNVERIFIED"}
    return {"artifact_metadata_status": "GITHUB_METADATA_MATCHED_NOT_BYTES",
            "github_reported_artifact_digests": digests,
            "artifact_zip_bytes_independently_verified": False}


class SafeLogRedirect(HTTPRedirectHandler):
    """Allow signed GitHub log-storage redirects without forwarding API tokens."""

    def redirect_request(self, req, fp, code, msg, headers, newurl):
        origin, target = urlsplit(req.full_url), urlsplit(newurl)
        host = (target.hostname or "").lower()
        if (target.scheme != "https" or
                not (host.endswith(".githubusercontent.com") or
                     host.endswith(".blob.core.windows.net"))):
            raise ValueError("untrusted GitHub log redirect target")
        redirected = super().redirect_request(req, fp, code, msg, headers, newurl)
        if redirected is None:
            raise ValueError("GitHub log redirect rejected")
        if target.netloc != origin.netloc:
            redirected.remove_header("Authorization")
        return redirected


class RejectApiRedirect(HTTPRedirectHandler):
    """Authenticated JSON API reads must never redirect to another origin."""

    def redirect_request(self, req, fp, code, msg, headers, newurl):
        raise ValueError("unexpected authenticated GitHub JSON API redirect")


def github_reader(token, api_url="https://api.github.com"):
    if not token:
        raise ValueError("read-only GitHub token required")

    def get(path, text=False):
        if not path.startswith("/repos/") or "://" in path:
            raise ValueError("unexpected GitHub API path")
        req = Request(api_url.rstrip("/") + path, headers={
            "Authorization": "Bearer " + token,
            "Accept": "application/vnd.github+json",
            "X-GitHub-Api-Version": "2022-11-28",
            "User-Agent": "Cryptoscanner-readonly-cadence"})
        if req.get_method() != "GET":
            raise ValueError("read-only GET required")
        # Job logs redirect to signed storage. Never forward the GitHub API
        # bearer token to a different host; JSON API reads stay direct.
        if text:
            with build_opener(SafeLogRedirect()).open(req, timeout=20) as response:
                body = response.read(MAX_LOG_BYTES + 1)
        else:
            with build_opener(RejectApiRedirect()).open(req, timeout=20) as response:
                body = response.read(MAX_LOG_BYTES + 1)
        if len(body) > MAX_LOG_BYTES:
            raise ValueError("GitHub response exceeds bounded size")
        # Lossy replacement would make a digest of modified log evidence.
        # Malformed UTF-8 must abstain, never masquerade as authenticated text.
        return body.decode("utf-8", errors="strict") if text else json.loads(body)

    return get


def current_remote_ref_evidence(get, repo, evidence, runs, report=None):
    """One authenticated GET checks the current Git ref against the newest log claim.

    A matching ref SHA proves only GitHub's current branch pointer, NOT
    independently rehashed ledger bytes or the writer's historical readback.
    A differing ref can mean another legitimate writer advanced the branch.
    """
    created = {r["id"]: r.get("created_at", "") for r in runs}
    # A well-formed readback line can occur in a job whose event/source
    # provenance failed verification. It must not authenticate the remote ref.
    verified_ids = {
        row["run_id"] for row in (report or {}).get("runs", [])
        if row.get("classification") in (
            "VERIFIED_NATIVE_SCHEDULE", "VERIFIED_WORKFLOW_DISPATCH_NOT_NATIVE")
    }
    complete_claims = [e for e in evidence
                       if e.get("delivery_log_claim_status") ==
                       "MATCHED_LOG_MARKERS_NOT_REMOTE_BYTES"]
    claims = [e for e in complete_claims if e.get("run_id") in verified_ids]
    if not claims:
        return {"status": ("UNVERIFIED_NO_SOURCE_AUTHENTICATED_LOG_CLAIM"
                           if complete_claims else "UNVERIFIED_NO_COMPLETE_LOG_CLAIM")}
    latest = max(claims, key=lambda e: (created.get(e["run_id"], ""), e["run_id"]))
    expected = latest["claimed_ledger_commit"]
    # A later unauthenticated or failed writer may have changed the ledger.
    # Matching the old trusted claim to today's ref cannot prove that the
    # latest observed writer attempt was safe or idempotent.
    verified = {"VERIFIED_NATIVE_SCHEDULE", "VERIFIED_WORKFLOW_DISPATCH_NOT_NATIVE"}
    newer_unknown = []
    for row in (report or {}).get("runs", []):
        if not isinstance(row, dict) or row.get("classification") in verified:
            continue
        # A rerun preserves the original created_at even though its writer
        # attempt may have executed *after* the latest trusted writer. Its
        # attempt time is not authenticated here, so creation order cannot
        # rule it out as a newer writer. Abstain even when the ref still
        # matches the trusted claim.
        if row.get("classification") == "MISSING_OR_RERUN_ATTEMPT_PROVENANCE":
            newer_unknown.append(row.get("run_id"))
            continue
        try:
            if timestamp(row["created_at"]) <= timestamp(created[latest["run_id"]]):
                continue
        except (KeyError, TypeError, ValueError, OverflowError):
            pass  # Missing time is not evidence that the attempt was earlier.
        newer_unknown.append(row.get("run_id"))
    try:
        response = get("/repos/" + repo + "/git/ref/heads/paper-proof-ledger")
        observed = response["object"]["sha"]
        if (response.get("ref") != "refs/heads/paper-proof-ledger" or
                response["object"].get("type") != "commit" or
                not isinstance(observed, str) or
                not re.fullmatch(r"[0-9a-f]{40}", observed)):
            raise ValueError("invalid remote ref metadata")
    except (OSError, ValueError, KeyError, TypeError):
        return {"status": "UNVERIFIED_REMOTE_REF_UNAVAILABLE",
                "claimed_run_id": latest["run_id"], "claimed_commit": expected}
    return {"status": ("UNVERIFIED_NEWER_WRITER_ORIGIN" if newer_unknown
                       else "MATCHED_CURRENT_REF_SHA_NOT_LEDGER_BYTES"
                       if observed == expected else
                       "UNVERIFIED_REF_DIFFERENT_OR_ADVANCED"),
            "claimed_run_id": latest["run_id"], "claimed_commit": expected,
            "newer_unattested_run_ids": newer_unknown,
            "current_ref_sha": observed, "remote_ledger_bytes_verified": False}


def canonical_writer_overlap_evidence(report, jobs):
    """Bound authenticated canonical job overlap without assuming complete coverage.

    A missing/failed/ambiguous adjacent writer attempt prevents a clean
    no-overlap claim. Reused GitHub job IDs invalidate independent identity.
    Even complete bounded coverage never proves external writer isolation.
    """
    verified = {"VERIFIED_NATIVE_SCHEDULE",
                "VERIFIED_WORKFLOW_DISPATCH_NOT_NATIVE"}
    rows = report.get("runs", [])
    if not isinstance(rows, list) or not isinstance(jobs, dict):
        return {"status": "UNVERIFIED_INVALID_JOB_COVERAGE",
                "global_exclusivity_verified": False}
    incomplete_rows = [r for r in rows
                       if not isinstance(r, dict) or
                       r.get("classification") not in verified]
    incomplete = sorted({r["run_id"] for r in incomplete_rows
                         if isinstance(r, dict) and type(r.get("run_id")) is int})
    intervals, seen_job_ids = [], set()
    for row in rows:
        if not isinstance(row, dict) or row.get("classification") not in verified:
            continue
        rid = row["run_id"]
        canonical = [j for j in jobs.get(str(rid), [])
                     if isinstance(j, dict) and j.get("name") == "public-paper"]
        matching = [j for j in canonical
                    if type(j.get("run_id")) is int and j["run_id"] == rid]
        if (len(canonical) != 1 or len(matching) != 1 or
                matching[0].get("conclusion") != "success"):
            return {"status": "UNVERIFIED_INCONSISTENT_WRITER_JOB",
                    "global_exclusivity_verified": False}
        writer = matching[0]
        job_id = writer.get("id")
        if type(job_id) is not int or job_id <= 0:
            return {"status": "UNVERIFIED_INVALID_WRITER_JOB_ID",
                    "global_exclusivity_verified": False}
        if job_id in seen_job_ids:
            return {"status": "UNVERIFIED_REUSED_WRITER_JOB_ID",
                    "global_exclusivity_verified": False}
        seen_job_ids.add(job_id)
        try:
            start = timestamp(writer["started_at"])
            end = timestamp(writer["completed_at"])
            created = timestamp(row["created_at"])
            if writer.get("status") != "completed" or not created <= start < end:
                raise ValueError("incoherent writer interval")
        except (KeyError, TypeError, ValueError, OverflowError):
            return {"status": "UNVERIFIED_INVALID_WRITER_INTERVAL",
                    "global_exclusivity_verified": False}
        intervals.append((start, end, rid))
    intervals.sort()
    overlaps = []
    for i, (start, end, rid) in enumerate(intervals):
        for next_start, next_end, next_rid in intervals[i + 1:]:
            if next_start >= end:
                break
            if max(start, next_start) < min(end, next_end):
                overlaps.append({"first_run_id": rid, "second_run_id": next_rid,
                                 "overlap_seconds": round(
                                     (min(end, next_end) -
                                      max(start, next_start)).total_seconds(), 3)})
    return {"status": ("FAILED_OVERLAPPING_CANONICAL_WRITER_JOBS" if overlaps
                       else "UNVERIFIED_INCOMPLETE_WRITER_COVERAGE" if incomplete_rows
                       else "NO_OVERLAP_OBSERVED_BOUNDED_SAMPLE" if len(intervals) >= 2
                       else "UNVERIFIED_INSUFFICIENT_AUTHENTICATED_JOBS"),
            "authenticated_writer_job_count": len(intervals),
            "incomplete_writer_run_count": len(incomplete_rows),
            "incomplete_writer_run_ids": incomplete,
            "overlap_pair_count": len(overlaps),
            "overlaps": overlaps,
            "global_exclusivity_verified": False}



def canonical_writer_attempt_intervals(report, jobs):
    """Detect overlapping GitHub canonical job *attempts*, even failed ones.

    GitHub job intervals are independently returned metadata, not proof that
    a scanner process wrote anything. Incomplete or unauthenticated intervals
    can never establish single-writer safety.
    """
    rows = report.get("runs", [])
    if not isinstance(rows, list) or not isinstance(jobs, dict):
        return {"status": "UNVERIFIED_INVALID_JOB_COVERAGE",
                "actual_ledger_write_overlap_verified": False}
    verified = {"VERIFIED_NATIVE_SCHEDULE",
                "VERIFIED_WORKFLOW_DISPATCH_NOT_NATIVE"}
    intervals, unknown, unverified_source = [], [], []
    seen_job_ids = set()
    try:
        audit_time = timestamp(report["checked_at"]) if report.get("checked_at") else None
    except (ValueError, TypeError, OverflowError):
        return {"status": "UNVERIFIED_INVALID_AUDIT_TIME",
                "actual_ledger_write_overlap_verified": False}
    for row in rows:
        rid = row.get("run_id") if isinstance(row, dict) else None
        if type(rid) is not int or rid <= 0:
            unknown.append(None)
            continue
        if row.get("classification") not in verified:
            unverified_source.append(rid)
        canonical = [j for j in jobs.get(str(rid), [])
                     if isinstance(j, dict) and j.get("name") == "public-paper"]
        if len(canonical) != 1:
            unknown.append(rid)
            continue
        writer = canonical[0]
        if (type(writer.get("id")) is not int or writer["id"] <= 0 or
                type(writer.get("run_id")) is not int or writer["run_id"] != rid or
                writer.get("status") != "completed" or
                writer["id"] in seen_job_ids):
            unknown.append(rid)
            continue
        seen_job_ids.add(writer["id"])
        try:
            start = timestamp(writer["started_at"])
            end = timestamp(writer["completed_at"])
            created = timestamp(row["created_at"])
            if not created <= start < end or (audit_time is not None and end > audit_time):
                raise ValueError("incoherent or future job interval")
        except (KeyError, TypeError, ValueError, OverflowError):
            unknown.append(rid)
            continue
        intervals.append((start, end, rid))
    intervals.sort()
    overlaps = []
    for i, (start, end, rid) in enumerate(intervals):
        for next_start, next_end, next_rid in intervals[i + 1:]:
            if next_start >= end:
                break
            duration = (min(end, next_end) - max(start, next_start)).total_seconds()
            if duration > 0:
                overlaps.append({"first_run_id": rid, "second_run_id": next_rid,
                                 "overlap_seconds": round(duration, 3)})
    return {
        "status": ("FAILED_OVERLAPPING_GITHUB_CANONICAL_JOB_INTERVALS" if overlaps
                   else "UNVERIFIED_INCOMPLETE_JOB_INTERVALS" if unknown
                   else "UNVERIFIED_SOURCE_PROVENANCE_FOR_JOB_INTERVALS" if unverified_source
                   else "NO_OVERLAP_OBSERVED_BOUNDED_JOB_INTERVALS" if len(intervals) >= 2
                   else "UNVERIFIED_INSUFFICIENT_JOB_INTERVALS"),
        "observed_job_interval_count": len(intervals),
        "unverified_source_run_ids": sorted(set(unverified_source)),
        "unknown_interval_run_ids": unknown,
        "overlap_pair_count": len(overlaps),
        "overlaps": overlaps,
        "actual_ledger_write_overlap_verified": False,
        "global_exclusivity_verified": False,
    }



def authenticated_ledger_claim_continuity(report, evidence):
    """Check monotonicity of source-authenticated log claims, NOT ledger bytes.

    A duplicate generation can be an idempotent no-write retry, not a proven
    duplicate persisted scan. Missing runs or generation gaps must abstain.
    """
    verified = {"VERIFIED_NATIVE_SCHEDULE",
                "VERIFIED_WORKFLOW_DISPATCH_NOT_NATIVE"}
    rows = report.get("runs", [])
    if not isinstance(rows, list) or not isinstance(evidence, list):
        return {"status": "UNVERIFIED_INVALID_CLAIM_COVERAGE",
                "remote_ledger_bytes_verified": False}
    candidates = []
    for row in rows:
        if not isinstance(row, dict) or row.get("classification") not in verified:
            continue
        rid = row.get("run_id")
        matches = [e for e in evidence if isinstance(e, dict) and
                   type(e.get("run_id")) is int and e["run_id"] == rid and
                   e.get("delivery_log_claim_status") ==
                   "MATCHED_LOG_MARKERS_NOT_REMOTE_BYTES"]
        if len(matches) != 1 or type(matches[0].get("claimed_generation")) is not int:
            return {"status": "UNVERIFIED_INCOMPLETE_AUTHENTICATED_CLAIMS",
                    "missing_run_id": rid, "remote_ledger_bytes_verified": False}
        try:
            created = timestamp(row["created_at"])
        except (KeyError, ValueError, TypeError, OverflowError):
            return {"status": "UNVERIFIED_INVALID_CLAIM_TIMESTAMPS",
                    "remote_ledger_bytes_verified": False}
        e = matches[0]
        generation, commit = e["claimed_generation"], e.get("claimed_ledger_commit")
        if generation <= 0 or not isinstance(commit, str) or not re.fullmatch(
                r"[0-9a-f]{40}", commit):
            return {"status": "UNVERIFIED_INVALID_LEDGER_CLAIM",
                    "remote_ledger_bytes_verified": False}
        candidates.append((created, rid, generation, commit))
    candidates.sort()
    if len(candidates) < 2:
        return {"status": "UNVERIFIED_INSUFFICIENT_LEDGER_CLAIMS",
                "authenticated_claim_count": len(candidates),
                "remote_ledger_bytes_verified": False}
    gaps, repeated = [], []
    for previous, current in zip(candidates, candidates[1:]):
        prev_time, prev_id, prev_gen, prev_commit = previous
        curr_time, curr_id, curr_gen, curr_commit = current
        if curr_time == prev_time:
            return {"status": "UNVERIFIED_AMBIGUOUS_RUN_ORDER",
                    "remote_ledger_bytes_verified": False}
        if curr_gen < prev_gen or (curr_gen == prev_gen and curr_commit != prev_commit):
            return {"status": "FAILED_CONFLICTING_AUTHENTICATED_LEDGER_CLAIMS",
                    "first_run_id": prev_id, "second_run_id": curr_id,
                    "first_generation": prev_gen, "second_generation": curr_gen,
                    "remote_ledger_bytes_verified": False}
        if curr_gen == prev_gen:
            repeated.append({"first_run_id": prev_id, "second_run_id": curr_id,
                             "generation": curr_gen})
        elif curr_gen > prev_gen + 1:
            gaps.append({"first_run_id": prev_id, "second_run_id": curr_id,
                         "missing_generation_count": curr_gen - prev_gen - 1})
    # A failed, rerun or unauthenticated writer in this bounded sample may
    # have attempted a ledger mutation without producing a trusted claim.
    # Never describe authenticated endpoints as a continuous ledger sequence
    # while another observed writer's persistence outcome is unknown.
    uncertain = sorted({r.get("run_id") for r in rows
                        if isinstance(r, dict) and
                        type(r.get("run_id")) is int and
                        r.get("classification") not in verified})
    return {
        "status": ("UNVERIFIED_UNATTESTED_WRITER_BETWEEN_CLAIMS" if uncertain
                   else "UNVERIFIED_REPEATED_LEDGER_GENERATION" if repeated
                   else "UNVERIFIED_GENERATION_GAPS" if gaps
                   else "MONOTONIC_AUTHENTICATED_LOG_CLAIMS_NOT_REMOTE_BYTES"),
        "unattested_writer_run_ids": uncertain,
        "authenticated_claim_count": len(candidates),
        "first_generation": candidates[0][2],
        "last_generation": candidates[-1][2],
        "repeated_generations": repeated,
        "generation_gaps": gaps,
        "remote_ledger_bytes_verified": False,
        "duplicate_persisted_scan_verified": False,
    }


def collect(get, repo, checked_at, lookback_hours=24, max_runs=80):
    """Return a reproducible audit plus SHA256 evidence index; no writes."""
    if not isinstance(repo, str) or len(repo.split("/")) != 2 or any(
            not part or part in (".", "..") or
            not all(c.isalnum() or c in "-_." for c in part)
            for part in repo.split("/")):
        raise ValueError("invalid repository name")
    now = timestamp(checked_at)
    if type(lookback_hours) is not int or not 1 <= lookback_hours <= 168:
        raise ValueError("bounded lookback required")
    if type(max_runs) is not int or not 1 <= max_runs <= 100:
        raise ValueError("bounded run count required")
    cutoff = now - dt.timedelta(hours=lookback_hours)
    base = "/repos/" + repo + "/actions"
    runs = []
    seen = set()
    for event in ("schedule", "workflow_dispatch"):
        # Server-side time filtering avoids hitting the first full page of
        # all-time history and falsely treating it as the 24h sample.
        path = base + "/workflows/" + WORKFLOW + "/runs?" + urlencode(
            {"event": event, "created": ">=" + cutoff.strftime("%Y-%m-%dT%H:%M:%SZ"),
             "per_page": MAX_PAGE})
        response = get(path)
        rows = response.get("workflow_runs") if isinstance(response, dict) else None
        total = response.get("total_count") if isinstance(response, dict) else None
        if (not isinstance(rows, list) or len(rows) >= MAX_PAGE or
                type(total) is not int or total != len(rows)):
            raise ValueError("truncated or malformed workflow run page")
        for row in rows:
            if not isinstance(row, dict) or type(row.get("id")) is not int:
                raise ValueError("invalid run row")
            if row.get("event") != event:
                raise ValueError("workflow run event query mismatch")
            if row["id"] in seen:
                raise ValueError("duplicate run across event queries")
            seen.add(row["id"])
            if timestamp(row["created_at"]) >= cutoff:
                runs.append(row)
    if len(runs) > max_runs:
        raise ValueError("bounded run budget exceeded; no partial report")
    logs, jobs, evidence = {}, {}, []
    for run in runs:
        rid = run["id"]
        # Even failed/in-progress runs may contain concurrent canonical jobs.
        # Read their job metadata, but never read/publish a success log for them.
        # A rerun retains its original event/created_at, but its latest
        # canonical job attempt can overlap a different writer. Collect job
        # metadata for reruns without accepting their logs as native proof.
        response = get(base + "/runs/" + str(rid) + "/jobs?per_page=100")
        job_rows = response.get("jobs") if isinstance(response, dict) else None
        job_total = response.get("total_count") if isinstance(response, dict) else None
        if (not isinstance(job_rows, list) or len(job_rows) >= MAX_PAGE or
                type(job_total) is not int or job_total != len(job_rows)):
            raise ValueError("truncated or malformed job page")
        jobs[str(rid)] = job_rows
        if run.get("run_attempt") != 1:
            continue  # Job interval only; never certify a rerun's source/log.
        if run.get("status") != "completed":
            continue
        canonical = [j for j in job_rows if isinstance(j, dict)
                     and j.get("name") == "public-paper"]
        matching = [j for j in canonical
                    if type(j.get("run_id")) is int and j["run_id"] == rid
                    and type(j.get("id")) is int and j["id"] > 0]
        if len(canonical) != 1 or len(matching) != 1:
            continue  # Any competing canonical writer job invalidates proof.
        # A green workflow is not evidence that its canonical writer job ran.
        # Bind log acquisition to a completed successful writer job with
        # coherent start/end timestamps, not a skipped or failed job.
        writer = matching[0]
        try:
            started = timestamp(writer["started_at"])
            finished = timestamp(writer["completed_at"])
            created = timestamp(run["created_at"])
        except (KeyError, ValueError, TypeError, OverflowError):
            continue
        if (writer.get("status") != "completed" or
                writer.get("conclusion") != "success" or
                not created <= started <= finished <= now):
            continue
        raw = get(base + "/jobs/" + str(writer["id"]) + "/logs", text=True)
        artifact_response = get(base + "/runs/" + str(rid) + "/artifacts?per_page=100")
        artifact_rows = (artifact_response.get("artifacts")
                         if isinstance(artifact_response, dict) else None)
        artifact_total = (artifact_response.get("total_count")
                          if isinstance(artifact_response, dict) else None)
        if (not isinstance(artifact_rows, list) or len(artifact_rows) >= MAX_PAGE or
                type(artifact_total) is not int or artifact_total != len(artifact_rows)):
            raise ValueError("truncated or malformed artifact metadata page")
        logs[str(rid)] = raw
        evidence.append({"run_id": rid, "job_id": matching[0]["id"],
                         **artifact_metadata_claim(artifact_rows, run),
                         **delivery_log_claim(raw, rid, started, finished),
                         # The API client decodes text with replacement. This
                         # digest is of the audited decoded log, NOT original
                         # transport bytes or a GitHub-attested log digest.
                         "decoded_log_sha256": hashlib.sha256(raw.encode("utf-8")).hexdigest(),
                         "raw_log_sha256_verified": False})
    result = audit(runs, logs, checked_at, lookback_hours, jobs=jobs)
    remote_ref = current_remote_ref_evidence(get, repo, evidence, runs, report=result)
    overlap = canonical_writer_overlap_evidence(result, jobs)
    attempts = canonical_writer_attempt_intervals(result, jobs)
    continuity = authenticated_ledger_claim_continuity(result, evidence)
    return {"report": result, "evidence": evidence,
            "ledger_log_claim_continuity": continuity,
            "writer_attempt_interval_evidence": attempts,
            "current_remote_ref_evidence": remote_ref,
            "writer_overlap_evidence": overlap,
            "raw_log_content_persisted": False,
            "read_only": True, "workflow": WORKFLOW}


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--repo", required=True)
    parser.add_argument("--checked-at", default=dt.datetime.now(dt.timezone.utc).isoformat())
    parser.add_argument("--lookback-hours", type=int, default=24)
    parser.add_argument("--max-runs", type=int, default=80)
    parser.add_argument("--output", required=True)
    args = parser.parse_args()
    result = collect(github_reader(os.environ.get("GITHUB_TOKEN")), args.repo,
                     args.checked_at, args.lookback_hours, args.max_runs)
    Path(args.output).write_text(json.dumps(result, sort_keys=True, indent=2) + "\n")
    print("PAPER_CADENCE_READONLY " + json.dumps({
        k: v for k, v in result["report"].items() if k != "runs"}, sort_keys=True))
    # Surface bounded job-attempt and ledger-claim failures in CI logs, so
    # reviewers need not download an artifact merely to see a critical FAIL.
    print("PAPER_RELIABILITY_READONLY " + json.dumps({
        "writer_attempt_intervals": result["writer_attempt_interval_evidence"],
        "ledger_claim_continuity": result["ledger_log_claim_continuity"],
        "canonical_writer_overlap": result["writer_overlap_evidence"],
        "current_remote_ref": result["current_remote_ref_evidence"],
    }, sort_keys=True))


if __name__ == "__main__":
    main()
