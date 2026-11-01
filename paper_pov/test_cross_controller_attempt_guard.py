"""Cross-controller dedup: never race a cadence dispatch still becoming visible.

These are offline decision tests. No workflow dispatch, ledger write, or
external network request occurs here.
"""
import datetime as dt
import unittest

from paper_pov.recovery import CADENCE_MARKER, CADENCE_RETRY_INTERVAL, RECOVERY_MARKER
from paper_pov.test_recovery import BOT, COMMIT, decision, scan

UTC = dt.timezone.utc
NOW = dt.datetime(2026, 10, 31, 23, 27, tzinfo=UTC)


def bot_attempt(at="2026-10-31T23:15:00Z", *, commit=COMMIT, actor=None):
    return {
        "body": "### Independent PAPER cadence ATTEMPT\n<!-- " +
                CADENCE_MARKER + commit + " -->",
        "created_at": at,
        "user": BOT if actor is None else actor,
    }


class CrossControllerAttemptGuardTests(unittest.TestCase):
    def test_recovery_dispatch_still_writes_original_recovery_marker(self):
        d = decision()
        self.assertEqual(d["action"], "DISPATCH_EXISTING_WORKFLOW")
        self.assertEqual(d["attempt_marker"], RECOVERY_MARKER + COMMIT)

    def test_recent_cadence_bot_attempt_blocks_recovery_for_same_ledger(self):
        d = decision(comments=[bot_attempt()])
        self.assertEqual((d["action"], d["reason"]),
                         ("NO_DISPATCH", "CADENCE_ALREADY_ATTEMPTED"))

    def test_failed_after_ledger_push_still_obeys_cadence_dedup(self):
        d = decision(runs=[scan(conclusion="failure")],
                     comments=[bot_attempt()])
        self.assertEqual((d["action"], d["reason"]),
                         ("NO_DISPATCH", "CADENCE_ALREADY_ATTEMPTED"))

    def test_cadence_retry_boundary_is_45_minutes_not_25(self):
        self.assertEqual(CADENCE_RETRY_INTERVAL, dt.timedelta(minutes=45))
        recent = decision(comments=[bot_attempt("2026-10-31T22:42:01Z")])
        self.assertEqual((recent["action"], recent["reason"]),
                         ("NO_DISPATCH", "CADENCE_ALREADY_ATTEMPTED"))
        boundary = decision(comments=[bot_attempt("2026-10-31T22:42:00Z")])
        self.assertEqual((boundary["action"], boundary["reason"]),
                         ("DISPATCH_EXISTING_WORKFLOW", "MATURED_SLOT_MISSED"))

    def test_untrusted_user_cannot_suppress_recovery(self):
        for actor in (
            {"login": "michaelrobinsonproduct-del", "id": 336805669},
            {"login": "github-actions[bot]", "id": 123},
            {"login": "attacker", "id": 41898282},
        ):
            with self.subTest(actor=actor):
                d = decision(comments=[bot_attempt(actor=actor)])
                self.assertEqual(d["action"], "DISPATCH_EXISTING_WORKFLOW")

    def test_marker_on_different_ledger_commit_does_not_block(self):
        d = decision(comments=[bot_attempt(commit="a" * 40)])
        self.assertEqual(d["action"], "DISPATCH_EXISTING_WORKFLOW")

    def test_malformed_trusted_marker_timestamp_fails_closed(self):
        d = decision(comments=[bot_attempt("not-a-date")])
        self.assertEqual((d["action"], d["reason"]),
                         ("BLOCKED", "CADENCE_MARKER_TIMESTAMP_INVALID"))

    def test_future_trusted_marker_timestamp_fails_closed(self):
        d = decision(comments=[bot_attempt("2026-10-31T23:30:00Z")])
        self.assertEqual((d["action"], d["reason"]),
                         ("BLOCKED", "CADENCE_MARKER_IN_FUTURE"))

    def test_recovery_marker_still_has_original_90_minute_cooldown(self):
        d = decision(comments=[{"body": "<!-- " + RECOVERY_MARKER + COMMIT + " -->",
                                "created_at": "2026-10-31T22:10:00Z",
                                "user": BOT}])
        self.assertEqual((d["action"], d["reason"]),
                         ("NO_DISPATCH", "RECOVERY_ALREADY_ATTEMPTED"))

    def test_active_writer_precedes_marker_eligibility(self):
        d = decision(
            runs=[scan(), scan(124, "2026-10-31T23:20:00Z",
                               status="in_progress", conclusion=None)],
            comments=[bot_attempt("2026-10-31T22:00:00Z")])
        self.assertEqual((d["action"], d["reason"]),
                         ("NO_DISPATCH", "SCANNER_ACTIVE_OR_QUEUED"))


if __name__ == "__main__":
    unittest.main()
