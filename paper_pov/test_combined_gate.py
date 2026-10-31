"""Independent combined-gate regression: synthetic fixtures are never market evidence."""
import datetime as dt
import unittest
from paper_pov import ledger
from paper_pov.test_ledger import synthetic, SHA, NOW


class CombinedGateTests(unittest.TestCase):
    def test_retained_run_owns_quote_even_when_quote_precedes_compaction_cutoff(self):
        state = ledger.advance(ledger.empty(), synthetic(0), SHA)
        second = synthetic(50 * 60 + 1)
        quote_at = (NOW + dt.timedelta(minutes=50 * 60 - 1)).isoformat()
        second["started_at"] = (NOW + dt.timedelta(minutes=50 * 60 - 2)).isoformat()
        for p in second["watch"]:
            p["quote_observed_at"] = quote_at
        for o in second["observations"]:
            o["observed_at"] = quote_at
        state = ledger.advance(state, second, SHA)
        retained_id = state["runs"][-1]["id"]
        state = ledger.advance(state, synthetic(100 * 60 + 1), SHA)
        self.assertEqual(sum(o["run_id"] == retained_id for o in state["observations"]), 25)
        self.assertEqual(state["archived"]["observations"], 25)
        self.assertEqual(ledger.scoreboard(state)["market_observations"], 75)
        ledger.verify(state)

    def test_hourly_sampling_is_not_continuous_under_45_minute_gate(self):
        state = ledger.empty()
        for minute in (0, 60, 120):
            state = ledger.advance(state, synthetic(minute), SHA)
        first = state["predictions"][0]["prediction_id"]
        outcome = [o for o in state["outcomes"] if o["prediction_id"] == first and o["horizon_hours"] == 1]
        self.assertEqual(len(outcome), 1)
        self.assertEqual(outcome[0]["status"], "ABSTAIN_GAP")
        self.assertNotIn("observed_30pct_hit", outcome[0])
        ledger.verify(state)

    def test_49_minute_unobserved_gap_abstains(self):
        state = ledger.empty()
        for minute in (0, 49, 110):
            state = ledger.advance(state, synthetic(minute), SHA)
        first = state["predictions"][0]["prediction_id"]
        outcome = [o for o in state["outcomes"] if o["prediction_id"] == first and o["horizon_hours"] == 1]
        self.assertEqual(len(outcome), 1)
        self.assertEqual(outcome[0]["status"], "ABSTAIN_GAP")
        ledger.verify(state)
