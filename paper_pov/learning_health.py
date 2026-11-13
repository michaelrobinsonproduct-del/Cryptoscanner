"""Independent health assessment of the CURRENT read-only paper learning workflow.

No scanner dispatch, production ledger writes, trades, score promotion, or research
lease manipulation. A green workflow without a retained artifact is not proof.
"""
import datetime as dt
import json
import os
import sys
import urllib.request

UTC = dt.timezone.utc
WORKFLOW = "paper-ledger-learning.yml"
REQUIRED = ("Read existing paper ledger artifact",
            "Carry forward observed Kraken candles from existing learning artifact",
            "Reconstruct only authentic completed Kraken outcomes and shadow evidence",
            "Retain read-only learning evidence")


def parsed(ts):
    if not isinstance(ts, str):
        raise ValueError("Missing GitHub timestamp")
    d = dt.datetime.fromisoformat(ts.replace("Z", "+00:00"))
    if d.tzinfo is None:
        raise ValueError("Timezone required")
    return d.astimezone(UTC)


def assess(now, runs, jobs_by_run, artifacts_by_run, *, maximum_age_minutes=90):
    """A real retained learning artifact and successful acquisition are required."""
    completed = sorted((r for r in runs if r.get("status") == "completed"),
                       key=lambda r: parsed(r["updated_at"]), reverse=True)
    latest = completed[0] if completed else None
    evidence = []
    for run in completed:
        if run.get("conclusion") != "success":
            continue
        jobs = jobs_by_run.get(run["id"], [])
        steps = {s.get("name"): s.get("conclusion")
                 for job in jobs for s in job.get("steps", [])}
        valid_jobs = bool(jobs) and all(j.get("conclusion") == "success"
                                        for j in jobs)
        valid_steps = all(steps.get(name) == "success" for name in REQUIRED)
        valid_artifact = any(a.get("name") == "public-paper-learning-" + str(run["id"])
                             and not a.get("expired", True)
                             and a.get("size_in_bytes", 0) > 0
                             for a in artifacts_by_run.get(run["id"], []))
        if valid_jobs and valid_steps and valid_artifact:
            evidence.append(run)
    cutoff = now - dt.timedelta(minutes=maximum_age_minutes)
    recent = [r for r in evidence if parsed(r["updated_at"]) >= cutoff]
    alerts = []
    if not runs:
        alerts.append("NO_READ_ONLY_LEARNING_RUNS")
    if latest and latest.get("conclusion") != "success":
        alerts.append("LATEST_READ_ONLY_LEARNING_FAILED")
    if not recent:
        alerts.append("NO_VERIFIED_READ_ONLY_LEARNING_90M")
    return {
        "status": "ALERT" if alerts else "HEALTHY",
        "alerts": alerts,
        "latest_completed_run": latest["id"] if latest else None,
        "latest_verified_evidence_run": evidence[0]["id"] if evidence else None,
        "fresh_verified_runs": len(recent),
        "workflow": WORKFLOW,
        "evidence": "completed Kraken outcome acquisition + SHA256-checked retained learning artifact",
        "predictive_lift_verified": False,
        "production_applied": False,
    }


class GitHub:
    def __init__(self, repo, token):
        if not repo or not token:
            raise ValueError("Repository and GitHub token required")
        self.url = "https://api.github.com/repos/" + repo
        self.headers = {
            "Authorization": "Bearer " + token,
            "Accept": "application/vnd.github+json",
            "X-GitHub-Api-Version": "2022-11-28",
        }

    def get(self, path):
        req = urllib.request.Request(self.url + path, headers=self.headers)
        with urllib.request.urlopen(req, timeout=25) as response:
            return json.load(response)


def main():
    api = GitHub(os.environ.get("GITHUB_REPOSITORY"), os.environ.get("GH_TOKEN"))
    runs = api.get("/actions/workflows/" + WORKFLOW + "/runs?per_page=20")["workflow_runs"]
    jobs, artifacts = {}, {}
    # Completed jobs only: never let an unfinished run count as progress.
    for run in runs:
        if run.get("status") != "completed":
            continue
        rid = run["id"]
        jobs[rid] = api.get("/actions/runs/" + str(rid) + "/jobs?per_page=50")["jobs"]
        artifacts[rid] = api.get("/actions/runs/" + str(rid) + "/artifacts?per_page=50")["artifacts"]
    result = assess(dt.datetime.now(UTC), runs, jobs, artifacts)
    print(json.dumps(result, sort_keys=True))
    if os.environ.get("GITHUB_STEP_SUMMARY"):
        with open(os.environ["GITHUB_STEP_SUMMARY"], "a") as f:
            f.write("## Independent paper-learning health\n\n```json\n"
                    + json.dumps(result, indent=2, sort_keys=True) + "\n```\n")
    if result["status"] != "HEALTHY":
        sys.exit(1)


if __name__ == "__main__":
    main()
