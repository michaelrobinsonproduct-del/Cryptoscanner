"""Focused decision tests: never fabricate a historical market scan."""
import unittest
from paper_pov.missed_slot_recovery import decision, validate_recovery_slot

NOW = "2026-11-03T23:24:30Z"


def run(created, status="completed", event="schedule"):
    return {"created_at": created, "status": status, "event": event}


class MissedSlotRecoveryTests(unittest.TestCase):
    def test_recovery_slot_provenance_and_bounded_age(self):
        self.assertEqual(validate_recovery_slot("", "workflow_dispatch"), "NORMAL_SCAN")
        self.assertEqual(validate_recovery_slot("2026-11-03T23:09:00+00:00",
                         "workflow_dispatch", NOW), "2026-11-03T23:09:00+00:00")
        with self.assertRaisesRegex(ValueError, "only allowed"):
            validate_recovery_slot("2026-11-03T23:09:00Z", "schedule", NOW)
        with self.assertRaisesRegex(ValueError, "Invalid scheduled"):
            validate_recovery_slot("2026-11-03T23:10:00Z", "workflow_dispatch", NOW)
        with self.assertRaisesRegex(ValueError, "outside bounded"):
            validate_recovery_slot("2026-11-03T22:39:00Z", "workflow_dispatch", NOW)

    def test_missing_slot_dispatches_existing_writer(self):
        result = decision(NOW, [run("2026-11-03T22:39:03Z")])
        self.assertEqual(result["action"], "DISPATCH")
        self.assertEqual(result["slot_utc"], "2026-11-03T23:09:00+00:00")

    def test_existing_attempt_suppresses_recovery_even_if_failed(self):
        self.assertEqual(decision(NOW, [
            run("2026-11-03T23:10:00Z")])["action"], "WAIT")

    def test_active_writer_suppresses_recovery(self):
        self.assertEqual(decision(NOW, [
            run("2026-11-03T22:39:00Z", "in_progress")])["action"], "WAIT")

    def test_before_grace_does_not_dispatch(self):
        self.assertEqual(decision("2026-11-03T23:12:00Z", [])["action"], "WAIT")

    def test_old_slots_not_backfilled(self):
        self.assertEqual(decision("2026-11-03T23:55:00Z", [])["slot_utc"],
                         "2026-11-03T23:39:00+00:00")

    def test_truncated_or_untrusted_history_fails_closed(self):
        with self.assertRaisesRegex(ValueError, "truncated"):
            decision(NOW, [run("2026-11-03T22:00:00Z")] * 100)
        with self.assertRaisesRegex(ValueError, "Unrecognized"):
            decision(NOW, [{"created_at": NOW, "event": "unknown", "status": "completed"}])

    def test_manual_run_suppresses_duplicate(self):
        self.assertEqual(decision(NOW, [
            run("2026-11-03T23:15:00Z", event="workflow_dispatch")])["action"], "WAIT")


if __name__ == "__main__":
    unittest.main()
