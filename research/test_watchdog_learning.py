"""Offline failure-injection tests for the independent learning watchdog."""
import datetime as dt
import unittest

from watchdog_learning import assess, alert_issue, latest_due, lease_state, run_state, load_evidence_artifacts, GAP_WORKFLOW_NAME, UTC


NOW = dt.datetime(2026, 10, 31, 2, 0, tzinfo=UTC)
CREATED = dt.datetime(2026, 10, 31, 1, 0, tzinfo=UTC)


def iso(t):
    return t.isoformat().replace("+00:00", "Z")


def run(identifier=1, *, status="completed", conclusion="success", age=5,
        event="push"):
    return {"id": identifier, "status": status, "conclusion": conclusion,
            "created_at": iso(NOW - dt.timedelta(minutes=age)), "event": event}


def jobs(*, verified="success", cache="success",
         reconcile="success", observed="success", upload="success"):
    return [{"steps": [
        {"name": "Check cooperative research lease, active runs, and cached source evidence",
         "conclusion": cache},
        {"name": "Verify and summarize retained evidence without labels",
         "conclusion": verified},
        {"name": "Reconcile retained trades and audit closed-candle early-mover candidates (no labels)",
         "conclusion": reconcile},
        {"name": "Independently corroborate contiguous observed 1h trade buckets (no labels)",
         "conclusion": observed},
        {"name": "Upload bounded independent observed-window corroboration",
         "conclusion": upload}]}]


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
    def test_green_primary_with_failed_job_is_unverified(self):
        broken = {**jobs()[0], "status": "completed", "conclusion": "failure"}
        self.assertEqual(run_state(run(), [broken]), "unverified_green")

    def test_green_primary_with_unfinished_job_is_unverified(self):
        broken = {**jobs()[0], "status": "in_progress"}
        self.assertEqual(run_state(run(), [broken]), "unverified_green")

    def test_green_source_with_failed_job_is_unverified(self):
        broken = {**gap_jobs()[0], "status": "completed", "conclusion": "failure"}
        self.assertEqual(run_state(gap_run(), [broken]), "unverified_green")

    def test_green_source_with_cancelled_job_is_unverified(self):
        broken = {**gap_jobs()[0], "status": "completed", "conclusion": "cancelled"}
        self.assertEqual(run_state(gap_run(), [broken]), "unverified_green")

    def test_completed_successful_job_still_counts(self):
        good = {**jobs()[0], "status": "completed", "conclusion": "success"}
        self.assertEqual(run_state(run(), [good]), "evidence_run")

    def test_primary_two_skips_not_masked_by_source_success(self):
        result = assess(NOW, CREATED,
                        [run(1, age=20), run(2, age=10)],
                        {1: jobs(verified="skipped"), 2: jobs(upload="skipped")},
                        [artifact(), artifact(name="kraken-bounded-independent-trade-members")],
                        {"concurrency": {"owner": None}},
                        [gap_run(10, age=5)], {10: gap_jobs()})
        self.assertIn("REPEATED_GREEN_NO_WORK", result["alerts"])

    def test_source_two_skips_not_masked_by_primary_success(self):
        result = assess(NOW, CREATED, [run(1, age=5)], {1: jobs()},
                        [artifact(), artifact(name="kraken-bounded-independent-trade-members")],
                        {"concurrency": {"owner": None}},
                        [gap_run(10, age=20), gap_run(11, age=10)],
                        {10: gap_jobs(inspect="skipped"), 11: gap_jobs(upload="skipped")})
        self.assertIn("REPEATED_GREEN_NO_WORK", result["alerts"])

    def test_blank_conflicting_lease_owner_fails_closed(self):
        self.assertIn("UNVERIFIABLE_LEASE_EXPIRY",
            assess_case(lease={"owner": "  ", "lease_expires_at":
                iso(NOW + dt.timedelta(minutes=10))})["alerts"])

    def test_orphaned_lease_expiry_is_not_a_free_lease(self):
        self.assertIn("UNVERIFIABLE_LEASE_EXPIRY",
            assess_case(lease={"owner": None, "lease_expires_at":
                iso(NOW + dt.timedelta(minutes=10))})["alerts"])

    def test_foreign_live_owner_is_preserved_not_expired(self):
        result = assess_case(lease={"owner": "different-live-worker",
            "lease_expires_at": iso(NOW + dt.timedelta(minutes=10))})
        self.assertEqual(result["lease"], "active")
        self.assertNotIn("EXPIRED_RESEARCH_LEASE", result["alerts"])

    def test_late_failing_older_dispatch_cannot_hide_behind_newer_green(self):
        failed = run(1, age=30, conclusion="failure")
        failed["updated_at"] = iso(NOW - dt.timedelta(minutes=1))
        success = run(2, age=10)
        success["updated_at"] = iso(NOW - dt.timedelta(minutes=5))
        result = assess_case(runs=[success, failed],
                             jobs_by_id={1: jobs(), 2: jobs()})
        self.assertIn("LATEST_RESEARCH_RUN_FAILED", result["alerts"])

    def test_completion_order_detects_two_late_skipped_batches(self):
        skipped1, skipped2, green = run(1, age=30), run(2, age=20), run(3, age=10)
        skipped1["updated_at"] = iso(NOW - dt.timedelta(minutes=1))
        skipped2["updated_at"] = iso(NOW - dt.timedelta(minutes=2))
        green["updated_at"] = iso(NOW - dt.timedelta(minutes=5))
        result = assess_case(runs=[green, skipped2, skipped1],
            jobs_by_id={1: jobs(verified="skipped"),
                        2: jobs(upload="skipped"), 3: jobs()})
        self.assertIn("REPEATED_GREEN_NO_WORK", result["alerts"])

    def test_long_running_recently_completed_evidence_is_fresh(self):
        completed = run(1, age=110)
        completed["updated_at"] = iso(NOW - dt.timedelta(minutes=2))
        result = assess_case(runs=[completed], jobs_by_id={1: jobs()},
                             created=NOW - dt.timedelta(hours=4))
        self.assertNotIn("NO_SUBSTANTIVE_RESEARCH_90M", result["alerts"])

    def test_healthy_evidence_run(self):
        result = assess_case()
        self.assertEqual(result["status"], "HEALTHY")
        self.assertEqual(result["latest_run_class"], "evidence_run")
        self.assertFalse(result["real_predictive_labels_verified"])

    def test_green_skip_is_not_evidence(self):
        self.assertEqual(run_state(run(), jobs(verified="skipped")), "skipped_no_work")

    def test_green_without_step_logs_is_unverified(self):
        self.assertEqual(run_state(run(), []), "unverified_green")

    def test_green_verify_but_skipped_reconciliation_is_no_work(self):
        self.assertEqual(run_state(run(), jobs(reconcile="skipped")), "skipped_no_work")

    def test_green_verify_but_skipped_independent_corroboration_is_no_work(self):
        self.assertEqual(run_state(run(), jobs(observed="skipped")), "skipped_no_work")

    def test_green_verify_but_skipped_report_upload_is_no_work(self):
        self.assertEqual(run_state(run(), jobs(upload="skipped")), "skipped_no_work")

    def test_green_verify_without_downstream_step_logs_is_unverified(self):
        partial = jobs()
        partial[0]["steps"] = partial[0]["steps"][:2]
        self.assertEqual(run_state(run(), partial), "unverified_green")

    def test_two_green_partial_batches_cannot_hide_no_progress(self):
        result = assess_case(runs=[run(1, age=5), run(2, age=15), run(3, age=25)],
                             jobs_by_id={1: jobs(observed="skipped"),
                                         2: jobs(upload="skipped"),
                                         3: jobs()})
        self.assertIn("REPEATED_GREEN_NO_WORK", result["alerts"])

    def test_failed_latest_run_alerts(self):
        result = assess_case(runs=[run(conclusion="failure")])
        self.assertIn("LATEST_RESEARCH_RUN_FAILED", result["alerts"])

    def test_active_retry_does_not_hide_latest_completed_failure(self):
        result = assess_case(runs=[run(1, status="in_progress", conclusion=None, age=2),
                                   run(2, conclusion="failure", age=10)],
                             jobs_by_id={2: jobs()})
        self.assertIn("LATEST_RESEARCH_RUN_FAILED", result["alerts"])

    def test_active_retry_after_completed_success_is_not_false_failure(self):
        result = assess_case(runs=[run(1, status="queued", conclusion=None, age=2),
                                   run(2, age=10),
                                   run(3, conclusion="failure", age=20)],
                             jobs_by_id={2: jobs()})
        self.assertNotIn("LATEST_RESEARCH_RUN_FAILED", result["alerts"])
        self.assertEqual(result["status"], "HEALTHY")

    def test_recovered_old_failure_does_not_alert(self):
        result = assess_case(runs=[run(1), run(2, conclusion="failure", age=10)])
        self.assertEqual(result["status"], "HEALTHY")

    def test_no_substantive_learning_after_ninety_minutes(self):
        result = assess_case(now=NOW + dt.timedelta(minutes=91),
                             runs=[run(1, age=5)], jobs_by_id={1: jobs()})
        self.assertIn("NO_SUBSTANTIVE_RESEARCH_90M", result["alerts"])

    def test_recent_evidence_does_not_trigger_ninety_minute_alert(self):
        result = assess_case(now=NOW + dt.timedelta(minutes=80),
                             runs=[run(1, age=5)], jobs_by_id={1: jobs()})
        self.assertNotIn("NO_SUBSTANTIVE_RESEARCH_90M", result["alerts"])

    def test_running_retry_cannot_hide_ninety_minute_evidence_gap(self):
        result = assess_case(now=NOW + dt.timedelta(minutes=95),
                             runs=[run(1, status="in_progress", conclusion=None, age=2),
                                   run(2, age=20)],
                             jobs_by_id={2: jobs()})
        self.assertIn("NO_SUBSTANTIVE_RESEARCH_90M", result["alerts"])

    def test_running_retry_cannot_hide_two_completed_no_work_runs(self):
        result = assess_case(runs=[run(1, status="queued", conclusion=None, age=1),
                                   run(2, age=5), run(3, age=20)],
                             jobs_by_id={2: jobs(verified="skipped"),
                                         3: jobs(verified="skipped")})
        self.assertIn("REPEATED_GREEN_NO_WORK", result["alerts"])

    def test_running_retry_cannot_hide_unverified_completed_green(self):
        result = assess_case(runs=[run(1, status="in_progress", conclusion=None, age=1),
                                   run(2, age=5)],
                             jobs_by_id={2: []})
        self.assertIn("LATEST_GREEN_RUN_UNVERIFIED", result["alerts"])

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
        recent = run(2, age=5)
        recent["created_at"] = iso(now - dt.timedelta(minutes=5))
        result = assess_case(now=now, runs=[recent, scheduled],
                             jobs_by_id={1: jobs(), 2: jobs()})
        self.assertEqual(result["status"], "HEALTHY")



def gap_run(identifier=10, *, age=5, status="completed", conclusion="success",
            event="push"):
    value = run(identifier, age=age, status=status, conclusion=conclusion,
                event=event)
    value["name"] = GAP_WORKFLOW_NAME
    return value


def gap_jobs(*, verify="success", reuse="success", inspect="success",
             upload="success"):
    return [{"steps": [
        {"name": "Verify exact pinned code and fail-closed offline tests",
         "conclusion": verify},
        {"name": "Reuse bounded retained artifacts only when cooperative lease clear",
         "conclusion": reuse},
        {"name": "Independently inspect one retained gap against bounded REST (not a complete label)",
         "conclusion": inspect},
        {"name": "Retain bounded gap evidence for 30 days",
         "conclusion": upload},
    ]}]


class BoundedSourceWatchdogTests(unittest.TestCase):
    def test_complete_source_work_counts_as_evidence_not_labels(self):
        self.assertEqual(run_state(gap_run(), gap_jobs()), "evidence_run")
        self.assertFalse(assess_case()["real_predictive_labels_verified"])

    def test_skipped_source_inspection_never_counts(self):
        self.assertEqual(run_state(gap_run(), gap_jobs(inspect="skipped")),
                         "skipped_no_work")

    def test_skipped_source_upload_never_counts(self):
        self.assertEqual(run_state(gap_run(), gap_jobs(upload="skipped")),
                         "skipped_no_work")

    def test_missing_source_step_logs_fail_closed(self):
        self.assertEqual(run_state(gap_run(), []), "unverified_green")

    def test_recent_bounded_source_prevents_false_ninety_minute_alert(self):
        old = run(1, age=110)
        result = assess(NOW, NOW - dt.timedelta(hours=3), [old],
                        {1: jobs()}, [artifact(), artifact(name="kraken-bounded-independent-trade-members")],
                        {"concurrency": {"owner": None}},
                        [gap_run(10, age=5)], {10: gap_jobs()})
        self.assertNotIn("NO_SUBSTANTIVE_RESEARCH_90M", result["alerts"])
        self.assertEqual(result["latest_run"], 10)

    def test_failed_bounded_source_run_alerts(self):
        result = assess(NOW, CREATED, [run(1, age=30)], {1: jobs()},
                        [artifact(), artifact(name="kraken-bounded-independent-trade-members")],
                        {"concurrency": {"owner": None}},
                        [gap_run(10, age=5, conclusion="failure")], {10: gap_jobs()})
        self.assertIn("LATEST_RESEARCH_RUN_FAILED", result["alerts"])

    def test_two_skipped_source_runs_trigger_no_progress(self):
        result = assess(NOW, CREATED, [run(1, age=40)], {1: jobs()},
                        [artifact(), artifact(name="kraken-bounded-independent-trade-members")],
                        {"concurrency": {"owner": None}},
                        [gap_run(10, age=5), gap_run(11, age=15)],
                        {10: gap_jobs(inspect="skipped"), 11: gap_jobs(upload="skipped")})
        self.assertIn("REPEATED_GREEN_NO_WORK", result["alerts"])

    def test_source_schedule_cannot_satisfy_primary_daily_schedule(self):
        now = dt.datetime(2026, 11, 1, 6, 0, tzinfo=UTC)
        source = gap_run(10, event="schedule")
        source["created_at"] = iso(dt.datetime(2026, 11, 1, 3, 14, tzinfo=UTC))
        result = assess(now, CREATED, [], {},
                        [artifact(), artifact(name="kraken-bounded-independent-trade-members")],
                        {"concurrency": {"owner": None}},
                        [source], {10: gap_jobs()})
        self.assertIn("MISSED_DAILY_RESEARCH_SCHEDULE", result["alerts"])

    def test_running_source_retry_cannot_hide_primary_failure(self):
        result = assess(NOW, CREATED, [run(1, age=15, conclusion="failure")],
                        {1: jobs()}, [artifact(), artifact(name="kraken-bounded-independent-trade-members")],
                        {"concurrency": {"owner": None}},
                        [gap_run(10, age=5, status="in_progress", conclusion=None)], {})
        self.assertIn("LATEST_RESEARCH_RUN_FAILED", result["alerts"])


    def test_newer_source_success_cannot_hide_primary_failure(self):
        result = assess(NOW, CREATED, [run(1, age=20, conclusion="failure")],
                        {1: jobs()}, [artifact(), artifact(name="kraken-bounded-independent-trade-members")],
                        {"concurrency": {"owner": None}},
                        [gap_run(10, age=5)], {10: gap_jobs()})
        self.assertIn("LATEST_RESEARCH_RUN_FAILED", result["alerts"])

    def test_newer_primary_success_cannot_hide_source_failure(self):
        result = assess(NOW, CREATED, [run(1, age=5)], {1: jobs()},
                        [artifact(), artifact(name="kraken-bounded-independent-trade-members")],
                        {"concurrency": {"owner": None}},
                        [gap_run(10, age=20, conclusion="failure")], {10: gap_jobs()})
        self.assertIn("LATEST_RESEARCH_RUN_FAILED", result["alerts"])

    def test_newer_source_success_cannot_hide_primary_unverified_green(self):
        result = assess(NOW, CREATED, [run(1, age=20)], {1: []},
                        [artifact(), artifact(name="kraken-bounded-independent-trade-members")],
                        {"concurrency": {"owner": None}},
                        [gap_run(10, age=5)], {10: gap_jobs()})
        self.assertIn("LATEST_GREEN_RUN_UNVERIFIED", result["alerts"])

    def test_newer_primary_success_cannot_hide_source_unverified_green(self):
        result = assess(NOW, CREATED, [run(1, age=5)], {1: jobs()},
                        [artifact(), artifact(name="kraken-bounded-independent-trade-members")],
                        {"concurrency": {"owner": None}},
                        [gap_run(10, age=20)], {10: []})
        self.assertIn("LATEST_GREEN_RUN_UNVERIFIED", result["alerts"])

    def test_same_stream_recovery_clears_old_failure_despite_other_stream(self):
        result = assess(NOW, CREATED,
                        [run(1, age=20, conclusion="failure"), run(2, age=10)],
                        {1: jobs(), 2: jobs()},
                        [artifact(), artifact(name="kraken-bounded-independent-trade-members")],
                        {"concurrency": {"owner": None}},
                        [gap_run(10, age=5)], {10: gap_jobs()})
        self.assertNotIn("LATEST_RESEARCH_RUN_FAILED", result["alerts"])


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
    def test_alert_readback_wrong_title_fails_delivery(self):
        class WrongTitle(FakeAPI):
            def call(self, path, *, method="GET", data=None):
                result = super().call(path, method=method, data=data)
                if path.startswith("/issues/") and method == "GET":
                    return {**result, "title": "unexpected"}
                return result
        with self.assertRaisesRegex(RuntimeError, "write not verified"):
            alert_issue(WrongTitle(), {"status": "ALERT",
                "alerts": ["EXPIRED_RESEARCH_LEASE"], "latest_run": 1})

    def test_recovery_readback_wrong_body_fails_delivery(self):
        class WrongRecovery(FakeAPI):
            def call(self, path, *, method="GET", data=None):
                result = super().call(path, method=method, data=data)
                if path.startswith("/issues/") and method == "GET" and result.get("state") == "closed":
                    return {**result, "body": "not persisted"}
                return result
        api = WrongRecovery()
        alert_issue(api, {"status": "ALERT",
            "alerts": ["LATEST_RESEARCH_RUN_FAILED"], "latest_run": 1})
        with self.assertRaisesRegex(RuntimeError, "recovery was not persisted"):
            alert_issue(api, {"status": "HEALTHY"})

    def test_alert_transport_failure_is_not_reported_as_delivered(self):
        class FailingAPI(FakeAPI):
            def call(self, path, *, method="GET", data=None):
                if path == "/issues" and method == "POST":
                    raise RuntimeError("issue delivery unavailable")
                return super().call(path, method=method, data=data)
        with self.assertRaisesRegex(RuntimeError, "issue delivery unavailable"):
            alert_issue(FailingAPI(), {"status": "ALERT",
                "alerts": ["NO_SUBSTANTIVE_RESEARCH_90M"], "latest_run": 1})

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
