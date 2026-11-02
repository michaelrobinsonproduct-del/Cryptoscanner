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
from urllib.parse import urlencode
from urllib.request import Request, urlopen

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
    for line in log.splitlines():
        match = READBACK_MARKER.fullmatch(line)
        if match:
            readbacks.append(match.groups())
        match = RESULTS_MARKER.fullmatch(line)
        if match and match.group(2) == str(run_id):
            results.append(match.groups())
    if len(readbacks) != 1 or len(results) != 1:
        return {"delivery_log_claim_status": "UNVERIFIED"}
    try:
        rt, commit = readbacks[0]
        st, _, generation, watch = results[0]
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
        with urlopen(req, timeout=20) as response:
            body = response.read(MAX_LOG_BYTES + 1)
        if len(body) > MAX_LOG_BYTES:
            raise ValueError("GitHub response exceeds bounded size")
        # Lossy replacement would make a digest of modified log evidence.
        # Malformed UTF-8 must abstain, never masquerade as authenticated text.
        return body.decode("utf-8", errors="strict") if text else json.loads(body)

    return get


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
        if run.get("status") != "completed" or run.get("run_attempt") != 1:
            continue
        response = get(base + "/runs/" + str(rid) + "/jobs?per_page=100")
        job_rows = response.get("jobs") if isinstance(response, dict) else None
        job_total = response.get("total_count") if isinstance(response, dict) else None
        if (not isinstance(job_rows, list) or len(job_rows) >= MAX_PAGE or
                type(job_total) is not int or job_total != len(job_rows)):
            raise ValueError("truncated or malformed job page")
        jobs[str(rid)] = job_rows
        matching = [j for j in job_rows if isinstance(j, dict)
                    and j.get("name") == "public-paper"
                    and type(j.get("run_id")) is int and j["run_id"] == rid
                    and type(j.get("id")) is int and j["id"] > 0]
        if len(matching) != 1:
            continue  # Audit abstains without a unique writer job.
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
        logs[str(rid)] = raw
        evidence.append({"run_id": rid, "job_id": matching[0]["id"],
                         **delivery_log_claim(raw, rid, started, finished),
                         # The API client decodes text with replacement. This
                         # digest is of the audited decoded log, NOT original
                         # transport bytes or a GitHub-attested log digest.
                         "decoded_log_sha256": hashlib.sha256(raw.encode("utf-8")).hexdigest(),
                         "raw_log_sha256_verified": False})
    result = audit(runs, logs, checked_at, lookback_hours, jobs=jobs)
    return {"report": result, "evidence": evidence,
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


if __name__ == "__main__":
    main()
