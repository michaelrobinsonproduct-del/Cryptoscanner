"""Offline failure-injection contracts for the independent paper-only monitor."""
import datetime as dt
import hashlib
import unittest
from pathlib import Path

from paper_pov.ledger import empty, seal
from paper_pov.monitor import UTC, evaluate, scheduled_slots

SHA = "a" * 40
ASOF = "2026-10-31T20:11:00+00:00"
PAIR = "XXBTZUSD"


def run(run_id, when, conclusion="success", event="schedule", status="completed"):
    return {"id": run_id, "event": event, "status": status,
            "conclusion": conclusion, "created_at": when, "head_sha": SHA}


def fixture():
    rid = "b" * 64
    pid = hashlib.sha256(("paper-v1|" + ASOF + "|" + PAIR).encode()).hexdigest()
    return seal({"schema": 1, "generation": 1,
        "runs": [{"id": rid, "as_of": ASOF, "source_sha": SHA,
                  "report_sha256": "c" * 64, "watch_count": 1, "observation_count": 1}],
        "predictions": [{"run_id": rid, "prediction_id": pid, "pair": PAIR,
                         "as_of": ASOF, "price": 100.0, "rank": 1,
                         "baseline_score": 1.0, "challenger_score": 2.0}],
        "observations": [{"run_id": rid, "pair": PAIR,
                          "at": "2026-10-31T20:10:50+00:00", "price": 100.0}],
        "outcomes": []})


def payload(*runs):
    return {"workflow_runs": list(runs)}


class PaperMonitorTests(unittest.TestCase):
    def check(self, now="2026-10-31T20:27:00+00:00", scans=None, audits=None,
              ledger=None, previous=None, message=None, errors=()):
        if scans is None:
            scans = payload(run(123, "2026-10-31T20:10:00Z"))
        if audits is None:
            audits = payload(run(456, "2026-10-31T20:22:00Z"))
        if ledger is None:
            ledger = fixture()
        if previous is None:
            previous = empty()
        if message is None:
            message = "paper: immutable scan 123 source " + SHA
        return evaluate(scans, audits, ledger, previous, "d" * 40, message,
                        dt.datetime.fromisoformat(now), errors)

    def test_healthy_realistic_schedule_and_sealed_ledger(self):
        result = self.check()
        self.assertEqual(result["status"], "HEALTHY")
        self.assertEqual(result["metrics"]["scans_persisted"], 1)
        self.assertEqual(result["metrics"]["matured_labels"], 0)
        self.assertIsNone(result["metrics"]["held_out_lift"])
        self.assertFalse(result["metrics"]["exchange_event_freshness_verified"])

    def test_one_missed_slot_not_two(self):
        result = self.check(now="2026-10-31T21:27:00+00:00",
                            audits=payload(run(456, "2026-10-31T21:22:00Z")))
        self.assertNotIn("PAPER_SCAN_TWO_MISSED_SLOTS", result["alerts"])

    def test_two_missed_scheduled_slots_alert(self):
        result = self.check(now="2026-10-31T23:27:00+00:00",
                            audits=payload(run(456, "2026-10-31T23:22:00Z")))
        self.assertIn("PAPER_SCAN_TWO_MISSED_SLOTS", result["alerts"])

    def test_manual_success_cannot_hide_two_missed_schedules(self):
        scans = payload(run(123, "2026-10-31T20:10:00Z"),
                        run(888, "2026-10-31T21:10:00Z", event="workflow_dispatch"))
        result = self.check(now="2026-10-31T23:27:00+00:00", scans=scans,
                            audits=payload(run(456, "2026-10-31T23:22:00Z")))
        self.assertIn("PAPER_SCAN_TWO_MISSED_SLOTS", result["alerts"])

    def test_latest_scheduled_failure_alerts(self):
        scans = payload(run(123, "2026-10-31T20:10:00Z"),
                        run(124, "2026-10-31T21:10:00Z", conclusion="failure"))
        result = self.check(now="2026-10-31T21:27:00+00:00", scans=scans,
                            audits=payload(run(456, "2026-10-31T21:22:00Z")))
        self.assertIn("PAPER_SCAN_LATEST_SCHEDULED_FAILED", result["alerts"])

    def test_queued_retry_cannot_hide_completed_failure(self):
        scans = payload(run(123, "2026-10-31T20:10:00Z"),
                        run(124, "2026-10-31T21:10:00Z", conclusion="failure"),
                        run(125, "2026-10-31T21:20:00Z", status="queued", conclusion=None))
        result = self.check(now="2026-10-31T21:27:00+00:00", scans=scans,
                            audits=payload(run(456, "2026-10-31T21:22:00Z")))
        self.assertIn("PAPER_SCAN_LATEST_SCHEDULED_FAILED", result["alerts"])

    def test_stuck_scheduled_job_alerts(self):
        scans = payload(run(123, "2026-10-31T20:10:00Z"),
                        run(124, "2026-10-31T19:10:00Z", status="in_progress", conclusion=None))
        self.assertIn("PAPER_SCAN_SCHEDULED_STUCK", self.check(scans=scans)["alerts"])

    def test_two_active_writers_detected(self):
        scans = payload(run(123, "2026-10-31T20:10:00Z"),
                        run(124, "2026-10-31T20:20:00Z", status="in_progress", conclusion=None),
                        run(125, "2026-10-31T20:21:00Z", status="in_progress", conclusion=None))
        self.assertIn("PAPER_MULTIPLE_ACTIVE_EXECUTIONS", self.check(scans=scans)["alerts"])

    def test_queued_scan_is_not_a_second_active_writer(self):
        scans = payload(run(123, "2026-10-31T20:10:00Z"),
                        run(124, "2026-10-31T20:20:00Z", status="in_progress", conclusion=None),
                        run(125, "2026-10-31T20:21:00Z", status="queued", conclusion=None))
        self.assertNotIn("PAPER_MULTIPLE_ACTIVE_EXECUTIONS", self.check(scans=scans)["alerts"])

    def test_issue_write_token_only_in_scheduled_alert_job(self):
        workflow = Path(".github/workflows/paper-monitor.yml").read_text()
        monitor, alert = workflow.split("\n  alert:\n")
        self.assertNotIn("issues: write", monitor)
        self.assertIn("issues: write", alert)
        self.assertIn("github.event_name == 'schedule'", alert)
        self.assertIn("sha256sum -c SHA256SUMS", alert)

    def test_corrupted_resealed_ledger_fails_closed(self):
        state = fixture()
        state["predictions"][0]["price"] = 200
        seal(state)
        self.assertIn("PAPER_LEDGER_INVALID", self.check(ledger=state)["alerts"])

    def test_missing_parent_ledger_fails_closed(self):
        self.assertIn("PAPER_PREVIOUS_LEDGER_UNAVAILABLE",
                      evaluate(payload(run(123, "2026-10-31T20:10:00Z")),
                               payload(run(456, "2026-10-31T20:22:00Z")),
                               fixture(), None, "d" * 40,
                               "paper: immutable scan 123 source " + SHA,
                               dt.datetime(2026, 10, 31, 20, 27, tzinfo=UTC))["alerts"])

    def test_generation_regression_detected(self):
        self.assertIn("PAPER_LEDGER_GENERATION_NONCONTIGUOUS",
                      self.check(previous=fixture())["alerts"])

    def test_mismatched_run_source_detected(self):
        self.assertIn("PAPER_LEDGER_RUN_UNLINKED",
                      self.check(message="paper: immutable scan 999 source " + SHA)["alerts"])

    def test_malformed_git_history_metadata_detected(self):
        self.assertIn("PAPER_LEDGER_SOURCE_UNLINKED",
                      self.check(message="untrusted commit")["alerts"])

    def test_audit_failure_is_independent(self):
        audits = payload(run(456, "2026-10-31T20:22:00Z", conclusion="failure"))
        self.assertIn("PAPER_AUDIT_LATEST_SCHEDULED_FAILED",
                      self.check(audits=audits)["alerts"])

    def test_missing_api_fails_closed(self):
        self.assertIn("PAPER_SCAN_RUNS_UNAVAILABLE",
                      self.check(scans={"error": "rate limited"})["alerts"])

    def test_collection_error_not_silently_green(self):
        self.assertIn("PAPER_EVIDENCE_SCAN_API_UNAVAILABLE",
                      self.check(errors=["SCAN_API_UNAVAILABLE"])["alerts"])

    def test_no_research_monitor_conflation(self):
        self.assertNotIn("RESEARCH", " ".join(self.check()["alerts"]))
        self.assertEqual(self.check()["metrics"]["dex_status"], "NOT_USED_NO_FRESHNESS_GATE")

    def test_schedule_grace_is_explicit(self):
        now = dt.datetime(2026, 10, 31, 21, 27, tzinfo=UTC)
        slots = scheduled_slots(now, 9)
        self.assertEqual(slots[0].hour, 20)

    def test_workflow_is_readonly_and_alerts_only(self):
        workflow = Path(".github/workflows/paper-monitor.yml").read_text()
        self.assertIn("cron: '27 * * * *'", workflow)
        self.assertIn("issues: write", workflow)
        self.assertIn("contents: read", workflow)
        self.assertIn("persist-credentials: false", workflow)
        self.assertNotIn("git push", workflow)
        self.assertNotIn("railway", workflow.lower())
        self.assertNotIn("paper-proof-ledger-single-writer", workflow)
        self.assertIn("PAPER_MONITOR_ISSUE_READBACK_VERIFIED", workflow)


if __name__ == "__main__":
    unittest.main()
