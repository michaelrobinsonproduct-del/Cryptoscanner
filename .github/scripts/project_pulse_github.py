#!/usr/bin/env python3
"""Read-only GitHub project status supplement for Project Pulse."""
import json
import os
from pathlib import Path
import time
import urllib.request
import urllib.error

out = Path("project-pulse-output")
out.mkdir(exist_ok=True)
repo = os.environ.get("GITHUB_REPOSITORY", "")
token = os.environ.get("GH_TOKEN", "")
budget = min(10, max(1, int(os.environ.get("ANALYSIS_MINUTES", "3"))))
deadline = time.monotonic() + budget * 60
errors = []

def fetch(endpoint):
    if not repo or not token or deadline - time.monotonic() < 15:
        errors.append({"endpoint": endpoint, "error": "Missing credentials or insufficient time"})
        return None
    req = urllib.request.Request("https://api.github.com/repos/" + repo + endpoint,
        headers={"Authorization": "Bearer " + token, "Accept": "application/vnd.github+json",
                 "X-GitHub-Api-Version": "2022-11-28", "User-Agent": "project-pulse"})
    try:
        with urllib.request.urlopen(req, timeout=12) as response:
            return json.load(response)
    except (urllib.error.URLError, ValueError, TimeoutError) as exc:
        errors.append({"endpoint": endpoint, "error": str(exc)[:200]})
        return None

runs_response = fetch("/actions/runs?per_page=50")
runs = runs_response.get("workflow_runs", []) if isinstance(runs_response, dict) else []
runs = [r for r in runs if r.get("name") != "Project Pulse - one-run project briefing"]
failures = [r for r in runs if r.get("conclusion") in ("failure", "timed_out")]
issues_response = fetch("/issues?state=open&per_page=100")
issues = [i for i in (issues_response or []) if "pull_request" not in i]
prs = fetch("/pulls?state=open&per_page=100") or []
report = {
    "schema": 1, "sampled_workflow_runs": len(runs),
    "failed_runs": [{"name": r.get("name"), "conclusion": r.get("conclusion"),
                     "url": r.get("html_url"), "sha": r.get("head_sha")} for r in failures],
    "open_issues": [{"number": i.get("number"), "title": i.get("title"),
                     "url": i.get("html_url")} for i in issues],
    "open_prs": [{"number": p.get("number"), "title": p.get("title"),
                 "url": p.get("html_url")} for p in prs],
    "api_errors": errors, "limits": "First 50 runs, first 100 issues and PRs; not exhaustive"
}
(out / "github-status.json").write_text(json.dumps(report, indent=2) + "\n")
lines = ["# Project Pulse: Live GitHub Status", "",
         f"- Recent runs examined: {len(runs)}",
         f"- Failed or timed-out runs: {len(failures)}",
         f"- Open issues sampled: {len(issues)}",
         f"- Open PRs sampled: {len(prs)}", "",
         "## Priority 1: Investigate recent workflow failures", ""]
for r in failures[:15]:
    lines.append(f"- **{r.get('name')}** ({r.get('conclusion')}): {r.get('html_url')}")
lines += ["", "## Priority 2: Open pull requests", ""]
for p in prs[:30]:
    lines.append(f"- #{p.get('number')} {p.get('title')}: {p.get('html_url')}")
lines += ["", "## Open issues", ""]
for i in issues[:30]:
    lines.append(f"- #{i.get('number')} {i.get('title')}: {i.get('html_url')}")
if errors:
    lines += ["", "## API errors (report may be incomplete)", ""]
    lines += [f"- {e['endpoint']}: {e['error']}" for e in errors]
lines += ["", report["limits"], ""]
(out / "github-status.md").write_text("\n".join(lines))
print(json.dumps({"runs": len(runs), "failed": len(failures),
                  "issues": len(issues), "prs": len(prs), "errors": errors}))
