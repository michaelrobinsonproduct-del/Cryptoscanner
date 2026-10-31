"""Adversarial synthetic tests for paper entry-price and as-of quote attribution.

No live market claims, production changes, credentials, or trading.
"""
import copy
import datetime as dt
import unittest

from paper_pov import ledger
from paper_pov.test_ledger import SHA, NOW, synthetic


def quote_for(report, pair):
    return next(o for o in report["observations"] if o["pair"] == pair)


class QuoteAttributionTests(unittest.TestCase):
    def setUp(self):
        self.report = synthetic(0)
        self.pair = self.report["watch"][0]["pair"]

    def test_unmodified_source_snapshot_is_accepted(self):
        state = ledger.advance(ledger.empty(), self.report, SHA)
        ledger.verify(state)
        watch = state["predictions"][0]
        quote = next(o for o in state["observations"]
                     if o["run_id"] == watch["run_id"] and o["pair"] == watch["pair"])
        self.assertEqual(watch["price"], quote["price"])

    def test_watch_price_disagrees_with_same_run_quote(self):
        self.report["watch"][0]["price"] *= 1.3
        with self.assertRaisesRegex(ValueError, "Prediction price differs"):
            ledger.advance(ledger.empty(), self.report, SHA)

    def test_observation_price_disagrees_with_same_run_watch(self):
        quote_for(self.report, self.pair)["price"] *= 1.3
        with self.assertRaisesRegex(ValueError, "Prediction price differs"):
            ledger.advance(ledger.empty(), self.report, SHA)

    def test_watch_quote_time_disagrees_with_same_run_observation(self):
        self.report["watch"][0]["quote_observed_at"] = (
            NOW - dt.timedelta(seconds=2)).isoformat()
        with self.assertRaisesRegex(ValueError, "Prediction quote timestamp differs"):
            ledger.advance(ledger.empty(), self.report, SHA)

    def test_equivalent_timezone_offset_is_accepted(self):
        # Same instant, different representation; compare instants not strings.
        self.report["watch"][0]["quote_observed_at"] = (
            NOW.astimezone(dt.timezone(dt.timedelta(hours=-4)))).isoformat()
        state = ledger.advance(ledger.empty(), self.report, SHA)
        self.assertEqual(state["generation"], 1)

    def test_watch_market_missing_from_observations(self):
        quote = quote_for(self.report, self.pair)
        self.report["observations"].remove(quote)
        self.report["observed_markets"] -= 1
        with self.assertRaisesRegex(ValueError, "Prediction market lacks observed quote"):
            ledger.advance(ledger.empty(), self.report, SHA)

    def test_resealed_prediction_entry_price_rejected(self):
        state = ledger.advance(ledger.empty(), self.report, SHA)
        state["predictions"][0]["price"] *= 1.3
        ledger.seal(state)
        with self.assertRaisesRegex(ValueError, "Prediction price differs"):
            ledger.verify(state)

    def test_resealed_observation_entry_price_rejected(self):
        state = ledger.advance(ledger.empty(), self.report, SHA)
        watch = state["predictions"][0]
        quote = next(o for o in state["observations"]
                     if o["run_id"] == watch["run_id"] and o["pair"] == watch["pair"])
        quote["price"] *= 1.3
        ledger.seal(state)
        with self.assertRaisesRegex(ValueError, "Prediction price differs"):
            ledger.verify(state)

    def test_different_prices_in_different_runs_are_valid(self):
        state = ledger.advance(ledger.empty(), self.report, SHA)
        later = synthetic(30, price=1.25)
        for watch in later["watch"]:
            watch["price"] = 1.25
        state = ledger.advance(state, later, SHA)
        ledger.verify(state)
        self.assertEqual(state["generation"], 2)
        self.assertEqual(state["predictions"][0]["price"], 1.01)
        self.assertEqual(state["predictions"][12]["price"], 1.25)

    def test_nonwatch_market_price_is_independent(self):
        watched = {p["pair"] for p in self.report["watch"]}
        other = next(o for o in self.report["observations"] if o["pair"] not in watched)
        other["price"] = 99
        state = ledger.advance(ledger.empty(), self.report, SHA)
        ledger.verify(state)

    def test_rejected_report_does_not_mutate_existing_history(self):
        before = ledger.advance(ledger.empty(), self.report, SHA)
        snapshot = copy.deepcopy(before)
        later = synthetic(30)
        later["watch"][0]["price"] *= 1.3
        with self.assertRaisesRegex(ValueError, "Prediction price differs"):
            ledger.advance(before, later, SHA)
        self.assertEqual(before, snapshot)


if __name__ == "__main__":
    unittest.main()
