"""Focused synthetic contracts for independent paper-learning health."""
import datetime as dt
import unittest
from paper_pov.learning_health import assess

NOW = dt.datetime(2026, 11, 10, 3, 0, tzinfo=dt.timezone.utc)


def run(id, minute, conclusion="success", status="completed"):
    return {"id": id, "status": status, "conclusion": conclusion,
            "updated_at": (NOW - dt.timedelta(minutes=minute)).isoformat()}


def jobs(id, *, acquisition=True):
    return {id: [{"conclusion": "success", "steps": [
        {"name": "Read existing paper ledger artifact", "conclusion": "success"},
        {"name": "Carry forward observed Kraken candles from existing learning artifact",
         "conclusion": "success" if acquisition else "skipped"},
        {"name": "Reconstruct only authentic completed Kraken outcomes and shadow evidence",
         "conclusion": "success" if acquisition else "skipped"},
        {"name": "Retain read-only learning evidence", "conclusion": "success"},
    ]}]}


def artifacts(id):
    return {id: [{"name": "public-paper-learning-" + str(id),
                   "expired": False, "size_in_bytes": 2304}]}


class HealthTests(unittest.TestCase):
    def test_verified_fresh_success(self):
        state = assess(NOW, [run(41, 10)], jobs(41), artifacts(41))
        self.assertEqual(state["status"], "HEALTHY")
        self.assertFalse(state["predictive_lift_verified"])
        self.assertFalse(state["production_applied"])

    def test_old_success_does_not_mask_staleness(self):
        state = assess(NOW, [run(41, 95)], jobs(41), artifacts(41))
        self.assertIn("NO_VERIFIED_READ_ONLY_LEARNING_90M", state["alerts"])

    def test_missing_artifact_is_not_learning(self):
        state = assess(NOW, [run(41, 10)], jobs(41), {})
        self.assertEqual(state["status"], "ALERT")

    def test_skipped_acquisition_not_learning(self):
        state = assess(NOW, [run(41, 10)], jobs(41, acquisition=False), artifacts(41))
        self.assertEqual(state["status"], "ALERT")

    def test_latest_failed_run_not_masked_by_older_success(self):
        rows = [run(42, 5, conclusion="failure"), run(41, 20)]
        state = assess(NOW, rows, jobs(41), artifacts(41))
        self.assertIn("LATEST_READ_ONLY_LEARNING_FAILED", state["alerts"])
        self.assertEqual(state["latest_verified_evidence_run"], 41)

    def test_in_progress_is_not_falsely_completed(self):
        rows = [run(42, 2, conclusion=None, status="in_progress"),
                run(41, 20)]
        state = assess(NOW, rows, jobs(41), artifacts(41))
        self.assertEqual(state["status"], "HEALTHY")

    def test_never_run_alerts(self):
        state = assess(NOW, [], {}, {})
        self.assertIn("NO_READ_ONLY_LEARNING_RUNS", state["alerts"])

if __name__ == "__main__":
    unittest.main()
