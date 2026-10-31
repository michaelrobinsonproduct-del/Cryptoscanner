"""Adversarial, synthetic-only paper ledger relationship checks."""
import copy
import unittest
from paper_pov import ledger
from paper_pov.test_ledger import synthetic, SHA


class LedgerIntegrityTests(unittest.TestCase):
    def setUp(self):
        self.state = ledger.advance(ledger.empty(), synthetic(0), SHA)

    def corrupt(self, mutation, pattern):
        state = copy.deepcopy(self.state)
        mutation(state)
        ledger.seal(state)  # Attacker or partial writer can recompute SHA.
        with self.assertRaisesRegex(ValueError, pattern):
            ledger.verify(state)

    def test_orphan_prediction(self):
        self.corrupt(lambda s: s["predictions"][0].update(run_id="f" * 64), "Orphan paper prediction")

    def test_orphan_observation(self):
        self.corrupt(lambda s: s["observations"][0].update(run_id="f" * 64), "Orphan market observation")

    def test_missing_observation(self):
        self.corrupt(lambda s: s["observations"].pop(), "Observation count mismatch")

    def test_missing_prediction(self):
        self.corrupt(lambda s: s["predictions"].pop(), "Prediction count/rank mismatch")

    def test_rewritten_as_of(self):
        self.corrupt(lambda s: s["predictions"][0].update(as_of="2026-01-01T00:00:00+00:00"), "Prediction as-of mismatch")

    def test_duplicate_market_quote(self):
        self.corrupt(lambda s: s["observations"][1].update(pair=s["observations"][0]["pair"]), "duplicate observation market")

    def test_future_quote(self):
        self.corrupt(lambda s: s["observations"][0].update(at="2099-01-01T00:00:00+00:00"), "Observation timestamp")

    def test_bad_price(self):
        self.corrupt(lambda s: s["predictions"][0].update(price=-1), "Invalid prediction price")

    def test_bad_rank(self):
        self.corrupt(lambda s: s["predictions"][0].update(rank=99), "Invalid prediction rank")

    def test_unobserved_watch_market(self):
        self.corrupt(lambda s: s["observations"][0].update(pair="SYNTHETIC/UNKNOWN"), "Prediction market lacks observed quote")

    def test_invalid_run_source(self):
        self.corrupt(lambda s: s["runs"][0].update(source_sha="main"), "Invalid run source SHA")

    def test_orphan_outcome(self):
        self.corrupt(lambda s: s["outcomes"].append({"prediction_id":"f"*64,"horizon_hours":1,"status":"ABSTAIN_GAP"}), "Orphan or invalid paper outcome")

    def test_legitimate_matured_and_compacted_states(self):
        state = ledger.empty()
        for minute in (0, 30, 60, 90, 120, 51*60):
            state = ledger.advance(state, synthetic(minute), SHA)
            ledger.verify(state)
        self.assertGreater(state["archived"]["scans"], 0)
        self.assertGreater(state["archived"]["gap_abstentions"], 0)


if __name__ == "__main__":
    unittest.main()
