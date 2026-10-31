"""Independent, read-only GitHub research health assessment and issue alerting.

No Railway access, no source downloads, no research checkpoint writes.
The issue is an alert *record*, not proof of user push/email delivery.
"""
import argparse
import base64
import datetime as dt
import json
import os
import urllib.request

UTC = dt.timezone.utc
RESEARCH_WORKFLOW = "research-reusable-evidence.yml"
ALERT_TITLE = "[Learning Watchdog] Research attention required"
EVIDENCE_ARTIFACT = "kraken-reusable-ohlc-evidence"
TRADE_EVIDENCE_ARTIFACT = "kraken-bounded-independent-trade-members"


def timestamp(value):
    if not isinstance(value, str):
        raise ValueError("timestamp missing")
    parsed = dt.datetime.fromisoformat(value.replace("Z", "+00:00"))
    if parsed.tzinfo is None:
        raise ValueError("timezone missing")
    return parsed.astimezone(UTC)


def lease_state(concurrency, now):
    owner = concurrency.get("owner")
    if not owner:
        return "clear"
    expiry = concurrency.get("lease_expires_at")
    if not expiry:
        return "unknown_active"
    try:
        return "active" if timestamp(expiry) > now else "expired"
    except (ValueError, TypeError):
        return "unknown_active"


def run_state(run, jobs):
    if run.get("status") != "completed":
        return "running"
    if run.get("conclusion") != "success":
        return "failed"
    steps = [s for job in jobs for s in job.get("steps", [])]
    verified = next((s for s in steps if s.get("name") ==
                     "Verify and summarize retained evidence without labels"), None)
    cache = next((s for s in steps if s.get("name", "").startswith(
                 "Check cooperative research lease")), None)
    if verified and verified.get("conclusion") == "success":
        return "evidence_run"
    if verified and verified.get("conclusion") == "skipped" and cache and cache.get("conclusion") == "success":
        return "skipped_no_work"
    return "unverified_green"


def latest_due(now, hour=3, minute=13, grace_minutes=120):
    boundary = now.replace(hour=hour, minute=minute, second=0, microsecond=0)
    if now < boundary + dt.timedelta(minutes=grace_minutes):
        boundary -= dt.timedelta(days=1)
    return boundary


def assess(now, workflow_created, runs, jobs_by_id, artifacts, checkpoint):
    """Evaluate only evidence-backed failures; don't mistake a daily cadence for a 90m stall."""
    alerts = []
    state = lease_state(checkpoint.get("concurrency", {}), now)
    if state == "expired":
        alerts.append("EXPIRED_RESEARCH_LEASE")
    if state == "unknown_active":
        alerts.append("UNVERIFIABLE_LEASE_EXPIRY")
    runs = sorted(runs, key=lambda r: timestamp(r["created_at"]), reverse=True)
    statuses = [(r, run_state(r, jobs_by_id.get(r["id"], []))) for r in runs]
    if not statuses and now - workflow_created > dt.timedelta(hours=2):
        alerts.append("NO_RESEARCH_RUNS")
    # A queued/running retry must not hide the latest completed failure.
    # Clear the alert only after a newer completed run has recovered.
    completed = [(r, s) for r, s in statuses if s != "running"]
    if completed and completed[0][1] == "failed":
        alerts.append("LATEST_RESEARCH_RUN_FAILED")
    if statuses and statuses[0][1] == "unverified_green":
        alerts.append("LATEST_GREEN_RUN_UNVERIFIED")
    for r, status in statuses:
        if status == "running" and now - timestamp(r["created_at"]) > dt.timedelta(minutes=120):
            alerts.append("RESEARCH_RUN_STALLED")
            break
    if len(statuses) >= 2 and all(s == "skipped_no_work" for _, s in statuses[:2]):
        alerts.append("REPEATED_GREEN_NO_WORK")
    due = latest_due(now)
    if due >= workflow_created:
        scheduled = [r for r in runs if r.get("event") == "schedule" and
                     due <= timestamp(r["created_at"]) < due + dt.timedelta(days=1)]
        if not scheduled:
            alerts.append("MISSED_DAILY_RESEARCH_SCHEDULE")
        elif all(run_state(r, jobs_by_id.get(r["id"], [])) == "failed" for r in scheduled):
            alerts.append("FAILED_DAILY_RESEARCH_SCHEDULE")
    def retained_expiries(name):
        expiries = []
        for artifact in artifacts:
            if artifact.get("name") != name:
                continue
            try:
                expiry = timestamp(artifact.get("expires_at"))
            except (ValueError, TypeError, OverflowError):
                alerts.append("MALFORMED_RESEARCH_ARTIFACT_METADATA")
                continue
            if not artifact.get("expired") and expiry > now:
                expiries.append(expiry)
        return expiries

    for name, missing, expiring in (
        (EVIDENCE_ARTIFACT, "NO_RETAINED_RESEARCH_EVIDENCE", "RESEARCH_ARTIFACT_EXPIRING"),
        (TRADE_EVIDENCE_ARTIFACT, "NO_RETAINED_TRADE_EVIDENCE", "TRADE_ARTIFACT_EXPIRING"),
    ):
        expiries = retained_expiries(name)
        if not expiries:
            alerts.append(missing)
        elif max(expiries) - now < dt.timedelta(hours=72):
            alerts.append(expiring)
    return {
        "status": "ALERT" if alerts else "HEALTHY",
        "alerts": sorted(set(alerts)),
        "lease": state,
        "latest_run": statuses[0][0]["id"] if statuses else None,
        "latest_run_class": statuses[0][1] if statuses else "none",
        "recent_evidence_runs": sum(s == "evidence_run" for _, s in statuses),
        "real_predictive_labels_verified": False,
        "production_modified": False,
    }


class GitHub:
    def __init__(self, repository, token):
        if not repository or not token:
            raise ValueError("GitHub repository and token required")
        self.base = "https://api.github.com/repos/" + repository
        self.headers = {"Authorization": "Bearer " + token,
                        "Accept": "application/vnd.github+json",
                        "X-GitHub-Api-Version": "2022-11-28"}

    def call(self, path, *, method="GET", data=None):
        payload = None if data is None else json.dumps(data).encode("utf-8")
        req = urllib.request.Request(self.base + path, data=payload, method=method,
                                     headers=self.headers)
        with urllib.request.urlopen(req, timeout=20) as response:
            raw = response.read()
        return json.loads(raw) if raw else {}


def alert_issue(api, report, *, dry_run=False):
    """Deduplicated issue delivery; verifies remote state after each write."""
    if dry_run:
        return "DRY_RUN"
    existing = None
    # Fail closed rather than creating duplicate alerts when the issue list is paginated.
    for page in range(1, 6):
        issues = api.call("/issues?state=open&per_page=100&page=" + str(page))
        existing = next((x for x in issues if x.get("title") == ALERT_TITLE and
                         "pull_request" not in x), None)
        if existing or len(issues) < 100:
            break
    else:
        raise RuntimeError("open issue pagination exceeded safe bound")
    if report["status"] != "ALERT":
        if existing:
            api.call("/issues/" + str(existing["number"]), method="PATCH",
                     data={"state": "closed", "body": "Recovered: latest watchdog assessment HEALTHY."})
            verify = api.call("/issues/" + str(existing["number"]))
            if verify.get("state") != "closed":
                raise RuntimeError("alert issue recovery was not persisted")
            return "RECOVERED_CLOSED"
        return "NO_ALERT"
    body = ("Independent research watchdog found actionable issues.\n\n" +
            "\n".join("- " + a for a in report["alerts"]) +
            "\n\nLatest workflow run: " + str(report["latest_run"]) +
            "\nThis issue does not guarantee a push notification or email.")
    if existing:
        number = existing["number"]
        if existing.get("body") != body:
            api.call("/issues/" + str(number), method="PATCH", data={"body": body})
    else:
        created = api.call("/issues", method="POST", data={"title": ALERT_TITLE, "body": body})
        number = created["number"]
    verify = api.call("/issues/" + str(number))
    if verify.get("body") != body or verify.get("state") != "open":
        raise RuntimeError("alert issue write not verified")
    return "ISSUE_VERIFIED_" + str(number)


def load_evidence_artifacts(api):
    """Fetch both source families independently; an OHLC-only query is incomplete."""
    artifacts = []
    for name in (EVIDENCE_ARTIFACT, TRADE_EVIDENCE_ARTIFACT):
        response = api.call("/actions/artifacts?name=" + name + "&per_page=50")
        if not isinstance(response.get("artifacts"), list):
            raise RuntimeError("missing evidence artifact response for " + name)
        artifacts.extend(response["artifacts"])
    return artifacts


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args()
    api = GitHub(os.environ.get("GITHUB_REPOSITORY"),
                 os.environ.get("GH_TOKEN"))
    workflow = api.call("/actions/workflows/" + RESEARCH_WORKFLOW)
    runs = api.call("/actions/workflows/" + RESEARCH_WORKFLOW + "/runs?per_page=40")["workflow_runs"]
    jobs = {}
    for r in runs[:8]:
        if r.get("status") == "completed":
            jobs[r["id"]] = api.call("/actions/runs/" + str(r["id"]) + "/jobs?per_page=30")["jobs"]
    artifacts = load_evidence_artifacts(api)
    state = api.call("/contents/research/learning_progress.json?ref=research-learning-program-20261027")
    checkpoint = json.loads(base64.b64decode(state["content"]))
    report = assess(dt.datetime.now(UTC), timestamp(workflow["created_at"]),
                    runs, jobs, artifacts, checkpoint)
    report["delivery"] = alert_issue(api, report, dry_run=args.dry_run)
    print(json.dumps(report, sort_keys=True))
    if report["status"] == "ALERT":
        raise SystemExit(1)


if __name__ == "__main__":
    main()
