#!/usr/bin/env python3
"""Project Pulse v3: bounded read-only diagnosis and actionable planning."""
import json
import os
from pathlib import Path
import re
import time
import urllib.error
import urllib.request

OUT = Path("project-pulse-output")
OUT.mkdir(exist_ok=True)
REPO = os.environ.get("GITHUB_REPOSITORY", "")
TOKEN = os.environ.get("GH_TOKEN", "")
BUDGET = min(10, max(1, int(os.environ.get("ANALYSIS_MINUTES", "3"))))
DEADLINE = time.monotonic() + BUDGET * 60
ERRORS = []
HEADERS = {"Authorization": "Bearer " + TOKEN,
           "Accept": "application/vnd.github+json",
           "X-GitHub-Api-Version": "2022-11-28",
           "User-Agent": "project-pulse"}
PATTERNS = [
    ("missing-input", r"no such file|file not found|not found:|missing required|ENOENT"),
    ("dependency", r"ModuleNotFoundError|ImportError|no module named|cannot import"),
    ("assertion", r"AssertionError|FAILED |assert .*=="),
    ("timeout", r"timed out|timeout|exceeded the maximum"),
    ("permission", r"permission denied|403 Forbidden|resource not accessible"),
    ("syntax", r"SyntaxError|IndentationError"),
    ("network", r"connection refused|connection reset|temporary failure|HTTP 5\\d\\d"),
]
def request(path, accept=None):
    if not REPO or not TOKEN or time.monotonic() > DEADLINE - 12:
        ERRORS.append({"path": path, "error": "Credentials missing or time budget nearly exhausted"})
        return None
    req = urllib.request.Request("https://api.github.com/repos/" + REPO + path,
        headers={**HEADERS, **({"Accept": accept} if accept else {})})
    try:
        with urllib.request.urlopen(req, timeout=min(10, max(2, int(DEADLINE-time.monotonic()-8)))) as response:
            raw = response.read(2_000_000)
            if accept == "application/vnd.github+json":
                return json.loads(raw)
            return raw.decode("utf-8", errors="replace")
    except (urllib.error.URLError, ValueError, TimeoutError) as exc:
        ERRORS.append({"path": path, "error": str(exc)[:180]})
        return None

runs_data = request("/actions/runs?per_page=50", "application/vnd.github+json") or {}
runs = runs_data.get("workflow_runs", []) if isinstance(runs_data, dict) else []
# Latest failed run per workflow, excluding Project Pulse itself.
latest = {}
for run in runs:
    if run.get("conclusion") not in ("failure", "timed_out"):
        continue
    name = run.get("name") or "Unknown"
    if name.startswith("Project Pulse") or name in latest:
        continue
    latest[name] = run
    if len(latest) >= 8:
        break

diagnoses = []
for name, run in latest.items():
    if time.monotonic() > DEADLINE - 20:
        break
    run_id = run.get("id")
    jobs = request("/actions/runs/" + str(run_id) + "/jobs?per_page=30",
                   "application/vnd.github+json") or {}
    failed_jobs = [j for j in jobs.get("jobs", []) if j.get("conclusion") in ("failure", "timed_out")]
    entries = []
    for job in failed_jobs[:2]:
        if time.monotonic() > DEADLINE - 18:
            break
        logs = request("/actions/jobs/" + str(job["id"]) + "/logs")
        if logs is None:
            entries.append({"job": job.get("name"), "classification": "unavailable",
                            "evidence": "Job log unavailable; do not infer cause"})
            continue
        matches = []
        for line in logs.splitlines():
            if any(re.search(pattern, line, re.I) for _, pattern in PATTERNS):
                matches.append(line.strip()[-260:])
        category = "unclassified"
        for label, pattern in PATTERNS:
            if re.search(pattern, logs, re.I):
                category = label
                break
        entries.append({"job": job.get("name"), "classification": category,
                        "evidence": matches[-3:]})
    diagnoses.append({"workflow": name, "run_id": run_id, "url": run.get("html_url"),
                      "sha": run.get("head_sha"), "jobs": entries})

issues = request("/issues?state=open&per_page=50", "application/vnd.github+json") or []
issues = [i for i in issues if "pull_request" not in i]
prs = request("/pulls?state=open&per_page=50", "application/vnd.github+json") or []
queue = []
for d in diagnoses:
    for j in d["jobs"]:
        queue.append({"priority": "P1", "kind": "investigate-failed-job",
                      "workflow": d["workflow"], "job": j["job"],
                      "classification": j["classification"], "evidence": j["evidence"],
                      "source_url": d["url"], "source_sha": d["sha"],
                      "status": "proposed", "execution": "manual-review-required"})
for i in issues:
    title = i.get("title", "")
    priority = "P1" if re.search(r"block|fail|broken|finish|integration", title, re.I) else "P2"
    queue.append({"priority": priority, "kind": "review-open-issue",
                  "issue": i.get("number"), "title": title,
                  "source_url": i.get("html_url"), "status": "proposed",
                  "execution": "manual-review-required"})
queue.sort(key=lambda x: (x["priority"], x["kind"]))
report = {"schema": 1, "run_sample": len(runs), "diagnosed_workflows": len(diagnoses),
          "diagnoses": diagnoses, "open_issue_count": len(issues),
          "open_pr_count": len(prs),
          "open_prs": [{"number": p.get("number"), "title": p.get("title"),
                        "url": p.get("html_url")} for p in prs],
          "proposed_work_queue": queue, "api_errors": ERRORS,
          "limitations": "Recent 50 runs; up to 8 distinct failing workflows; 2 failed jobs each; first 50 issues/PRs. Keyword-based triage is advisory, not a verified root cause. No source changes."}
(OUT / "project-plan.json").write_text(json.dumps(report, indent=2) + "\n")
lines = ["# Project Pulse v3 — Investigation and Next Actions", "",
         f"**Recent runs sampled:** {len(runs)}",
         f"**Failing workflows investigated:** {len(diagnoses)}",
         f"**Open issues:** {len(issues)} | **Open PRs:** {len(prs)}", "",
         "## Diagnosed failing workflows", ""]
for d in diagnoses:
    lines += [f"### {d['workflow']}", d["url"] or "", ""]
    for j in d["jobs"]:
        lines.append(f"- **{j['job']}**: {j['classification']}")
        for evidence in j["evidence"][:2]:
            lines.append(f"  - Evidence: `{evidence.replace(chr(96), chr(39))}`")
lines += ["", "## Prioritized proposed work queue", ""]
for q in queue[:35]:
    label = q.get("title") or (q.get("workflow", "") + " / " + q.get("job", ""))
    lines.append(f"- **{q['priority']}** {q['kind']}: {label} — {q['source_url']}")
lines += ["", "## Open PRs (sample)", ""]
for p in prs[:25]:
    lines.append(f"- #{p.get('number')} {p.get('title')}: {p.get('html_url')}")
if ERRORS:
    lines += ["", "## Missing evidence / API errors", ""]
    lines += [f"- {e['path']}: {e['error']}" for e in ERRORS]
lines += ["", report["limitations"], "",
          "**No changes were made to production, scoring, workflows, or repository source.**", ""]
(OUT / "project-plan.md").write_text("\n".join(lines))
if not runs and ERRORS:\n    raise SystemExit("INCOMPLETE_PROJECT_PULSE: GitHub run retrieval failed; inspect project-plan.json errors")\nprint(json.dumps({"runs": len(runs), "diagnosed_workflows": len(diagnoses),
                  "queue_items": len(queue), "api_errors": len(ERRORS)}))
