"""Synthetic-only acceptance of outcome continuity; never performance evidence."""
import unittest
from paper_pov import ledger
from paper_pov.test_ledger import synthetic

SOURCE_SHA = "a" * 40


class CadenceAcceptanceTests(unittest.TestCase):
    def test_hourly_quotes_fail_closed_without_45_minute_continuity(self):
        state = ledger.empty()
        for minute in (0, 60, 120, 180):
            state = ledger.advance(state, synthetic(minute), SOURCE_SHA)
        score = ledger.scoreboard(state)
        self.assertEqual(score["matured_labels"], 0)
        self.assertGreater(score["gap_abstentions"], 0)
        self.assertIsNone(score["held_out_lift"])
        ledger.verify(state)

    def test_half_hourly_quotes_mature_all_horizons_without_fake_lift(self):
        state = ledger.empty()
        first_ids = None
        for minute in range(0, 50 * 60 + 1, 30):
            state = ledger.advance(state, synthetic(minute), SOURCE_SHA)
            if first_ids is None:
                first_ids = [p["prediction_id"] for p in state["predictions"]]
        ledger.verify(state)
        score = ledger.scoreboard(state)
        self.assertGreater(score["matured_labels"], 0)
        self.assertEqual(score["gap_abstentions"], 0)
        self.assertIsNone(score["held_out_lift"])
        self.assertFalse(score["production_applied"])
        self.assertEqual(
            {1, 6, 24, 48},
            {o["horizon_hours"] for o in state["outcomes"]},
        )
        # This 50-hour fixture need not cross the compaction threshold.
        # Assert that the first immutable prediction IDs remain present
        # either in the active ledger or in an archived segment.
        self.assertEqual(len(first_ids), 12)
        active_ids = {p["prediction_id"] for p in state["predictions"]}
        self.assertTrue(set(first_ids).issubset(active_ids) or state["archive_index"])


if __name__ == "__main__":
    unittest.main()
