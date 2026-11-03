"""Focused deterministic manual/scheduled scanner output acceptance."""
import copy
import unittest
from paper_pov.manual_scheduled_parity import compare


def report():
    return {"schema": 1, "mode": "PAPER_ONLY", "buy_approved": False,
            "source": "Kraken public REST", "started_at": "2026-11-03T00:00:00+00:00",
            "as_of": "2026-11-03T00:00:10+00:00", "eligible_pairs": 20,
            "matched_tickers": 20, "observed_markets": 20, "ohlc_screened": 1,
            "watch": [{"pair": "XXBTZUSD", "prediction_id": "p1", "status": "PAPER_WATCH"}],
            "observations": [{"pair": "XXBTZUSD", "price": 100}],
            "abstentions": [], "forward_labels": 0, "held_out_lift": None,
            "production_applied": False}


class ParityTests(unittest.TestCase):
    def test_equal_fixture(self):
        self.assertEqual(len(compare(report(), copy.deepcopy(report()))), 64)

    def test_ranked_candidate_divergence(self):
        other = report()
        other["watch"][0]["pair"] = "XETHZUSD"
        with self.assertRaisesRegex(ValueError, "watch"):
            compare(report(), other)

    def test_observation_divergence(self):
        other = report()
        other["observations"][0]["price"] = 101
        with self.assertRaisesRegex(ValueError, "observations"):
            compare(report(), other)

    def test_missing_field_fails(self):
        other = report()
        del other["matched_tickers"]
        with self.assertRaisesRegex(ValueError, "missing"):
            compare(report(), other)

    def test_empty_watch_fails(self):
        other = report()
        other["watch"] = []
        with self.assertRaisesRegex(ValueError, "no WATCH"):
            compare(other, other)

    def test_unsafe_mode_fails(self):
        other = report()
        other["buy_approved"] = True
        with self.assertRaisesRegex(ValueError, "unsafe"):
            compare(other, other)

    def test_duplicate_predictions_fail(self):
        other = report()
        other["watch"].append(dict(other["watch"][0]))
        with self.assertRaisesRegex(ValueError, "duplicate"):
            compare(other, other)


if __name__ == "__main__":
    unittest.main()
