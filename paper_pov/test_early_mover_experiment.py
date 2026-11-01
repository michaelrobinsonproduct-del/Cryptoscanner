"""Adversarial tests for frozen, read-only momentum shadow research."""
import datetime as dt
import unittest

from paper_pov.early_mover_experiment import (
    trailing_sampled_return, _top, _metrics, evaluate)

UTC = dt.timezone.utc
T = dt.datetime(2026, 11, 1, 12, tzinfo=UTC)


class MomentumShadowTests(unittest.TestCase):
    def test_asof_anchor_never_uses_quote_within_last_30_minutes(self):
        timeline = [(T - dt.timedelta(minutes=100), 1.0),
                    (T - dt.timedelta(minutes=70), 2.0),
                    (T - dt.timedelta(minutes=29), 100.0),
                    (T + dt.timedelta(minutes=1), 1000.0)]
        self.assertAlmostEqual(trailing_sampled_return(timeline, T, 3.0), 0.5)

    def test_missing_past_anchor_abstains(self):
        self.assertIsNone(trailing_sampled_return(
            [(T - dt.timedelta(minutes=91), 1.0),
             (T - dt.timedelta(minutes=29), 2.0)], T, 3.0))

    def test_boundary_and_zero_or_nonfinite_quote_fail_closed(self):
        self.assertEqual(trailing_sampled_return(
            [(T - dt.timedelta(minutes=90), 2.0)], T, 2.0), 0.0)
        for price in (0, -1, float("nan"), float("inf")):
            with self.assertRaises(ValueError):
                trailing_sampled_return([(T - dt.timedelta(minutes=60), 2.0)], T, price)
        with self.assertRaises(ValueError):
            trailing_sampled_return([(T - dt.timedelta(minutes=60), 0.0)], T, 2.0)

    def test_ranking_tie_is_deterministic_and_invalid_scores_rejected(self):
        rows = [{"pair": "BUSD", "momentum": 0.2},
                {"pair": "AUSD", "momentum": 0.2},
                {"pair": "CUSD", "momentum": 0.1}]
        self.assertEqual([x["pair"] for x in _top(rows, "momentum", 2)],
                         ["AUSD", "BUSD"])
        with self.assertRaises(ValueError):
            _top([{"pair": "XUSD", "momentum": float("nan")}], "momentum")

    def test_unknown_outcome_is_not_false_positive(self):
        selected = [{"pair": "AUSD"}, {"pair": "BUSD"}, {"pair": "CUSD"}]
        outcomes = {"AUSD": {"status": "MATURED_OBSERVED", "observed_peak_pct": 22},
                    "BUSD": {"status": "ABSTAIN_GAP"}}
        got = _metrics(selected, outcomes, 20)
        self.assertEqual((got["selected"], got["known"], got["unknown_gap"],
                          got["hits"], got["false_positives"]), (3, 1, 2, 1, 0))

    def test_zero_known_outcomes_does_not_claim_precision(self):
        got = _metrics([{"pair": "AUSD"}], {}, 30)
        self.assertIsNone(got["precision_known_only"])
        self.assertEqual(got["unknown_gap"], 1)

    def test_parameters_are_frozen(self):
        with self.assertRaisesRegex(ValueError, "Frozen"):
            evaluate({}, T, horizons=(1,), thresholds=(5, 20, 30))
        with self.assertRaisesRegex(ValueError, "Frozen"):
            evaluate({}, T, thresholds=(2, 20, 30))


if __name__ == "__main__":
    unittest.main()
