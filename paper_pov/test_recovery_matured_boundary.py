"""Live-time recovery boundary regression; no workflow dispatch or ledger writes."""
import datetime as dt
import hashlib
import unittest

from paper_pov.ledger import seal
from paper_pov.monitor import UTC
from paper_pov.recovery import RECOVERY_MARKER
from paper_pov.test_monitor import fixture
from paper_pov.test_recovery import COMMIT, BOT, decision, scan


def durable_at_1012():
    state = fixture()
    asof = "2026-11-01T10:12:59+00:00"
    state["runs"][0]["as_of"] = asof
    state["predictions"][0]["as_of"] = asof
    state["predictions"][0]["prediction_id"] = hashlib.sha256(
        ("paper-v1|" + asof + "|" + state["predictions"][0]["pair"]).encode()
    ).hexdigest()
    state["observations"][0]["at"] = "2026-11-01T10:12:50+00:00"
    return seal(state)


class RecoveryLiveBoundaryTests(unittest.TestCase):
    def setUp(self):
        self.ledger = durable_at_1012()
        self.anchor = scan(123, "2026-11-01T10:11:01Z",
                           event="workflow_dispatch")

    def at(self, hour, minute, second=0, runs=None, comments=None):
        return decision(
            runs=[self.anchor] if runs is None else runs,
            ledger=self.ledger,
            comments=[] if comments is None else comments,
            now=dt.datetime(2026, 11, 1, hour, minute, second, tzinfo=UTC),
        )

    def test_real_1111_abstention_then_1039_slot_matures_at_1114(self):
        # A 10:12 durable scan covers the last mature 10:09 slot at 11:11.
        before = self.at(11, 11, 53)
        self.assertEqual((before["action"], before["reason"]),
                         ("NO_DISPATCH", "DURABLE_SCAN_AFTER_MATURED_SLOT"))
        self.assertEqual(before["missed_matured_slots"], [])
        # The 10:39 slot becomes mature exactly 35 minutes later, at 11:14.
        still_early = self.at(11, 13, 59)
        self.assertEqual(still_early["action"], "NO_DISPATCH")
        due = self.at(11, 14)
        self.assertEqual((due["action"], due["reason"]),
                         ("DISPATCH_EXISTING_WORKFLOW", "MATURED_SLOT_MISSED"))
        self.assertEqual(due["missed_matured_slots"],
                         ["2026-11-01T10:39:00+00:00"])

    def test_active_writer_blocks_newly_matured_slot(self):
        active = scan(124, "2026-11-01T11:35:00Z",
                      status="in_progress", conclusion=None,
                      event="workflow_dispatch")
        due = self.at(11, 36, runs=[self.anchor, active])
        self.assertEqual((due["action"], due["reason"]),
                         ("NO_DISPATCH", "SCANNER_ACTIVE_OR_QUEUED"))

    def test_verified_bot_attempt_still_enforces_ninety_minute_dedup(self):
        marker = {"body": "<!-- " + RECOVERY_MARKER + COMMIT + " -->",
                  "created_at": "2026-11-01T11:20:00Z", "user": BOT}
        due = self.at(11, 36, comments=[marker])
        self.assertEqual((due["action"], due["reason"]),
                         ("NO_DISPATCH", "RECOVERY_ALREADY_ATTEMPTED"))


if __name__ == "__main__":
    unittest.main()
