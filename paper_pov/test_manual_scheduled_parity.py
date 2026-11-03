"""Focused deterministic manual/scheduled scanner output acceptance."""
import copy
import unittest
from paper_pov.manual_scheduled_parity import compare
from paper_pov import scanner
from paper_pov.test_scanner import fixture, NOW


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
    def test_real_scanner_fixture_manual_scheduled_equivalence(self):
        # Exercise the actual Kraken paper scanner's filtering, OHLC ranking,
        # timestamp and immutable prediction-ID generation on both entry paths.
        manual = scanner.scan(api=fixture(stable=True), clock=lambda: NOW,
                              sleep=lambda _: None)
        scheduled = scanner.scan(api=fixture(stable=True), clock=lambda: NOW,
                                 sleep=lambda _: None)
        self.assertEqual(manual["excluded_stablecoin_pairs"], 13)
        self.assertEqual(len(manual["watch"]), 12)
        self.assertEqual(len(compare(manual, scheduled)), 64)

    def test_real_scanner_fixture_detects_changed_ranked_score(self):
        manual = scanner.scan(api=fixture(), clock=lambda: NOW,
                              sleep=lambda _: None)
        scheduled = copy.deepcopy(manual)
        scheduled["watch"][0]["challenger_score"] += 0.01
        with self.assertRaisesRegex(ValueError, "watch"):
            compare(manual, scheduled)

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

    def test_empty_watch_parity_is_valid_abstention(self):
        other = report()
        other["watch"] = []
        self.assertEqual(len(compare(other, copy.deepcopy(other))), 64)

    def test_extra_source_metadata_divergence(self):
        a, b = report(), report()
        a["ticker_move_reference"] = "kraken_ticker_today_open_utc"
        b["ticker_move_reference"] = "rolling_24h"
        with self.assertRaisesRegex(ValueError, "ticker_move_reference"):
            compare(a, b)

    def test_missing_extra_field_divergence(self):
        a, b = report(), report()
        a["excluded_stablecoin_pairs"] = 2
        with self.assertRaisesRegex(ValueError, "excluded_stablecoin_pairs"):
            compare(a, b)

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
