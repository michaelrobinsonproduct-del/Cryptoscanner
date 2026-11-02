"""Bounded, read-only GitHub Actions evidence acquisition for PAPER cadence.

This is a reusable audit job, NOT a scheduler, recovery controller or writer.
Every HTTP request is GET. Missing or truncated evidence fails closed.
"""
import argparse
import datetime as dt
import hashlib
import json
import os
from pathlib import Path
from urllib.parse import urlencode
from urllib.request import Request, urlopen

from paper_pov.cadence_provenance import audit, timestamp

WORKFLOW = "paper-pipeline.yml"
MAX_PAGE = 100
MAX_LOG_BYTES = 4 * 1024 * 1024


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
        return body.decode("utf-8", errors="replace") if text else json.loads(body)

    return get


def collect(get, repo, checked_at, lookback_hours=24, max_runs=80):
    """Return a reproducible audit plus SHA256 evidence index; no writes."""
    if not isinstance(repo, str) or len(repo.split("/")) != 2 or any(
            not part or not all(c.isalnum() or c in "-_." for c in part)
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
        if not isinstance(rows, list) or len(rows) >= MAX_PAGE:
            raise ValueError("truncated or malformed workflow run page")
        for row in rows:
            if not isinstance(row, dict) or type(row.get("id")) is not int:
                raise ValueError("invalid run row")
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
        if not isinstance(job_rows, list) or len(job_rows) >= MAX_PAGE:
            raise ValueError("truncated or malformed job page")
        jobs[str(rid)] = job_rows
        matching = [j for j in job_rows if isinstance(j, dict)
                    and j.get("name") == "public-paper"
                    and type(j.get("run_id")) is int and j["run_id"] == rid
                    and type(j.get("id")) is int and j["id"] > 0]
        if len(matching) != 1:
            continue  # Audit abstains without a unique writer job.
        raw = get(base + "/jobs/" + str(matching[0]["id"]) + "/logs", text=True)
        logs[str(rid)] = raw
        evidence.append({"run_id": rid, "job_id": matching[0]["id"],
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
