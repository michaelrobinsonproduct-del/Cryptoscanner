"""Offline failure-injection tests for the independent learning watchdog."""
import datetime as dt
import unittest

from watchdog_learning import assess, alert_issue, latest_due, lease_state, run_state, load_evidence_artifacts, UTC


NOW = dt.datetime(2026, 10, 31, 2, 0, tzinfo=UTC)
CREATED = dt.datetime(2026, 10, 31, 1, 0, tzinfo=UTC)


def iso(t):
    return t.isoformat().replace("+00:00", "Z")


def run(identifier=1, *, status="completed", conclusion="success", age=5,
        event="push"):
    return {"id": identifier, "status": status, "conclusion": conclusion,
            "created_at": iso(NOW - dt.timedelta(minutes=age)), "event": event}


def jobs(*, verified="success", cache="success"):
    return [{"steps": [
        {"name": "Check cooperative research lease, active runs, and cached source evidence",
         "conclusion": cache},
        {"name": "Verify and summarize retained evidence without labels",
         "conclusion": verified}]}]


def artifact(expiry_days=25, name="kraken-reusable-ohlc-evidence"):
    return {"name": name, "expired": False,
            "expires_at": iso(NOW + dt.timedelta(days=expiry_days))}


def assess_case(runs=None, jobs_by_id=None, artifacts=None, lease=None,
                now=NOW, created=CREATED):
    return assess(now, created, runs if runs is not None else [run()],
                  jobs_by_id if jobs_by_id is not None else {1: jobs()},
                  artifacts if artifacts is not None else [artifact(), artifact(name="kraken-bounded-independent-trade-members")],
                  {"concurrency": lease if lease is not None else {"owner": None}})


class AssessmentTests(unittest.TestCase):
    def test_healthy_evidence_run(self):
        result = assess_case()
        self.assertEqual(result["status"], "HEALTHY")
        self.assertEqual(result["latest_run_class"], "evidence_run")
        self.assertFalse(result["real_predictive_labels_verified"])

    def test_green_skip_is_not_evidence(self):
        self.assertEqual(run_state(run(), jobs(verified="skipped")), "skipped_no_work")

    def test_green_without_step_logs_is_unverified(self):
        self.assertEqual(run_state(run(), []), "unverified_green")

    def test_failed_latest_run_alerts(self):
        result = assess_case(runs=[run(conclusion="failure")])
        self.assertIn("LATEST_RESEARCH_RUN_FAILED", result["alerts"])

    def test_recovered_old_failure_does_not_alert(self):
        result = assess_case(runs=[run(1), run(2, conclusion="failure", age=10)])
        self.assertEqual(result["status"], "HEALTHY")

    def test_expired_lease_alerts(self):
        result = assess_case(lease={"owner": "other", "lease_expires_at":
                                    iso(NOW - dt.timedelta(minutes=1))})
        self.assertIn("EXPIRED_RESEARCH_LEASE", result["alerts"])

    def test_live_lease_not_alerted(self):
        result = assess_case(lease={"owner": "other", "lease_expires_at":
                                    iso(NOW + dt.timedelta(minutes=10))})
        self.assertEqual(result["status"], "HEALTHY")

    def test_malformed_lease_fails_closed(self):
        result = assess_case(lease={"owner": "other", "lease_expires_at": "broken"})
        self.assertIn("UNVERIFIABLE_LEASE_EXPIRY", result["alerts"])

    def test_stuck_run_alerts(self):
        result = assess_case(runs=[run(status="in_progress", conclusion=None, age=130)],
                             jobs_by_id={})
        self.assertIn("RESEARCH_RUN_STALLED", result["alerts"])

    def test_short_active_run_is_not_failure(self):
        result = assess_case(runs=[run(status="in_progress", conclusion=None, age=15)],
                             jobs_by_id={})
        self.assertEqual(result["status"], "HEALTHY")

    def test_repeated_green_skips_without_recent_evidence(self):
        r1, r2 = run(1, age=5), run(2, age=20)
        result = assess_case(runs=[r1, r2], jobs_by_id={
            1: jobs(verified="skipped"), 2: jobs(verified="skipped")})
        self.assertIn("REPEATED_GREEN_NO_WORK", result["alerts"])

    def test_two_consecutive_skips_alert_even_if_prior_work_recent(self):
        result = assess_case(runs=[run(1, age=5), run(2, age=20), run(3, age=30)],
                             jobs_by_id={1: jobs(verified="skipped"),
                                         2: jobs(verified="skipped"), 3: jobs()})
        self.assertIn("REPEATED_GREEN_NO_WORK", result["alerts"])

    def test_expired_artifact_alerts(self):
        result = assess_case(artifacts=[artifact(expiry_days=-1), artifact(name="kraken-bounded-independent-trade-members")])
        self.assertIn("NO_RETAINED_RESEARCH_EVIDENCE", result["alerts"])

    def test_artifact_near_expiry_alerts(self):
        result = assess_case(artifacts=[artifact(expiry_days=2), artifact(name="kraken-bounded-independent-trade-members")])
        self.assertIn("RESEARCH_ARTIFACT_EXPIRING", result["alerts"])

    def test_missing_trade_artifact_alerts(self):
        result = assess_case(artifacts=[artifact()])
        self.assertIn("NO_RETAINED_TRADE_EVIDENCE", result["alerts"])

    def test_expiring_trade_artifact_alerts(self):
        result = assess_case(artifacts=[artifact(),
            artifact(expiry_days=1, name="kraken-bounded-independent-trade-members")])
        self.assertIn("TRADE_ARTIFACT_EXPIRING", result["alerts"])

    def test_malformed_artifact_metadata_alerts_instead_of_crashing(self):
        broken = artifact()
        broken["expires_at"] = "not-a-date"
        result = assess_case(artifacts=[broken,
            artifact(name="kraken-bounded-independent-trade-members")])
        self.assertIn("MALFORMED_RESEARCH_ARTIFACT_METADATA", result["alerts"])
        self.assertIn("NO_RETAINED_RESEARCH_EVIDENCE", result["alerts"])

    def test_no_research_runs_after_activation_alerts(self):
        result = assess_case(runs=[], jobs_by_id={},
            now=CREATED + dt.timedelta(hours=3))
        self.assertIn("NO_RESEARCH_RUNS", result["alerts"])

    def test_unverified_green_latest_alerts(self):
        result = assess_case(jobs_by_id={1: []})
        self.assertIn("LATEST_GREEN_RUN_UNVERIFIED", result["alerts"])

    def test_missing_daily_schedule_after_grace(self):
        now = dt.datetime(2026, 11, 1, 6, 0, tzinfo=UTC)
        result = assess_case(now=now, runs=[run(age=5)])
        self.assertIn("MISSED_DAILY_RESEARCH_SCHEDULE", result["alerts"])

    def test_schedule_grace_and_first_activation(self):
        self.assertEqual(latest_due(NOW), dt.datetime(2026, 10, 30, 3, 13, tzinfo=UTC))
        self.assertEqual(assess_case()["status"], "HEALTHY")

    def test_successful_scheduled_run_satisfies_due(self):
        now = dt.datetime(2026, 11, 1, 6, 0, tzinfo=UTC)
        scheduled = run(1, age=5, event="schedule")
        scheduled["created_at"] = iso(dt.datetime(2026, 11, 1, 3, 14, tzinfo=UTC))
        result = assess_case(now=now, runs=[scheduled])
        self.assertEqual(result["status"], "HEALTHY")


class FakeAPI:
    def __init__(self):
        self.issues = {}
        self.next_number = 11
        self.writes = 0

    def call(self, path, *, method="GET", data=None):
        if path.startswith("/issues?state=open&per_page=100&page="):
            page = int(path.rsplit("=", 1)[-1])
            open_issues = [v.copy() for v in self.issues.values() if v["state"] == "open"]
            return open_issues[(page - 1) * 100:page * 100]
        if path == "/issues" and method == "POST":
            n = self.next_number
            self.next_number += 1
            self.issues[n] = {"number": n, "title": data["title"],
                              "body": data["body"], "state": "open"}
            self.writes += 1
            return self.issues[n].copy()
        if path.startswith("/issues/"):
            n = int(path.split("/")[-1])
            if method == "PATCH":
                self.issues[n].update(data)
                self.writes += 1
            return self.issues[n].copy()
        raise AssertionError((path, method))


class ArtifactDiscoveryTests(unittest.TestCase):
    def test_both_evidence_families_queried_independently(self):
        class API:
            def __init__(self):
                self.paths = []
            def call(self, path):
                self.paths.append(path)
                return {"artifacts": [{"name": path.split("name=")[1].split("&")[0]}]}
        api = API()
        found = load_evidence_artifacts(api)
        self.assertEqual({x["name"] for x in found}, {
            "kraken-reusable-ohlc-evidence",
            "kraken-bounded-independent-trade-members"})
        self.assertEqual(len(api.paths), 2)

    def test_missing_artifact_response_fails_closed(self):
        class API:
            def call(self, path):
                return {"artifacts": []} if "kraken-reusable-ohlc-evidence" in path else {}
        with self.assertRaisesRegex(RuntimeError, "missing evidence artifact"):
            load_evidence_artifacts(API())


class AlertTests(unittest.TestCase):
    def test_dry_run_never_writes(self):
        api = FakeAPI()
        self.assertEqual(alert_issue(api, {"status": "ALERT"}, dry_run=True), "DRY_RUN")
        self.assertEqual(api.writes, 0)

    def test_alert_create_readback_and_idempotency(self):
        api = FakeAPI()
        report = {"status": "ALERT", "alerts": ["EXPIRED_RESEARCH_LEASE"],
                  "latest_run": 1}
        self.assertEqual(alert_issue(api, report), "ISSUE_VERIFIED_11")
        self.assertEqual(alert_issue(api, report), "ISSUE_VERIFIED_11")
        self.assertEqual(api.writes, 1)

    def test_alert_body_contains_actual_newlines(self):
        api = FakeAPI()
        report = {"status": "ALERT", "alerts": ["EXPIRED_RESEARCH_LEASE"],
                  "latest_run": 7}
        alert_issue(api, report)
        body = api.issues[11]["body"]
        self.assertIn("\n- EXPIRED_RESEARCH_LEASE", body)
        self.assertNotIn("\\n", body)

    def test_existing_alert_on_second_page_is_reused(self):
        api = FakeAPI()
        for n in range(100):
            api.issues[n] = {"number": n, "title": "Unrelated", "body": "",
                             "state": "open"}
        api.issues[101] = {"number": 101, "title": "[Learning Watchdog] Research attention required",
                           "body": "old", "state": "open"}
        report = {"status": "ALERT", "alerts": ["EXPIRED_RESEARCH_LEASE"],
                  "latest_run": 7}
        self.assertEqual(alert_issue(api, report), "ISSUE_VERIFIED_101")
        self.assertEqual(len(api.issues), 101)

    def test_oversized_issue_listing_fails_closed(self):
        api = FakeAPI()
        for n in range(500):
            api.issues[n] = {"number": n, "title": "Unrelated", "body": "",
                             "state": "open"}
        report = {"status": "ALERT", "alerts": ["EXPIRED_RESEARCH_LEASE"],
                  "latest_run": 7}
        with self.assertRaisesRegex(RuntimeError, "pagination"):
            alert_issue(api, report)
        self.assertEqual(api.writes, 0)

    def test_recovery_closes_verified_alert(self):
        api = FakeAPI()
        report = {"status": "ALERT", "alerts": ["LATEST_RESEARCH_RUN_FAILED"],
                  "latest_run": 1}
        alert_issue(api, report)
        self.assertEqual(alert_issue(api, {"status": "HEALTHY"}), "RECOVERED_CLOSED")
        self.assertEqual(api.issues[11]["state"], "closed")


if __name__ == "__main__":
    unittest.main()
