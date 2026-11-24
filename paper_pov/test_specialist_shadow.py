import unittest
from paper_pov.specialist_shadow import compare_specialists, specialist_scores


class SpecialistShadowTests(unittest.TestCase):
    def test_accumulation_penalizes_already_rallied_coin(self):
        f = dict(momentum_5m=.01, momentum_15m=.02, momentum_60m=.01,
                 volume_accel=3., trade_accel=2., volatility_60m=.005)
        self.assertGreater(specialist_scores(f)["accumulation"],
                           specialist_scores(dict(f, momentum_60m=.25))["accumulation"])
        self.assertIsNone(specialist_scores(dict(f, volume_accel=float("nan"))))

    def test_equal_budget_and_unknowns_preserved(self):
        f = dict(momentum_5m=.01, momentum_15m=.02, momentum_60m=.01,
                 volume_accel=3., trade_accel=2., volatility_60m=.005)
        rows = [dict(prediction_id="a", features=f),
                dict(prediction_id="b", features=dict(f, momentum_60m=.25)),
                dict(prediction_id="c", features=dict(f, volume_accel=10.))]
        labels = {"a": {"hit": False, "coverage_complete": True},
                  "c": {"hit": True, "coverage_complete": True,
                        "observed_lead_hours_upper_bound": 6.}}
        report = compare_specialists([(rows, ["b"], ["a"])], labels, scope="TEST")
        self.assertEqual(report["common_complete_batches"], 0)
        self.assertEqual(report["metrics"]["baseline"]["unknown"], 1)
        self.assertEqual(report["metrics"]["baseline"]["complete_misses"], 0)
        self.assertEqual(report["metrics"]["accumulation"]["early_known_hits"], 1)
        self.assertEqual(report["metrics"]["accumulation"]["known_positive_anchor_recall"], 1)
        self.assertTrue(all(m["selected"] == 1 for m in report["metrics"].values()))
        labels["b"] = {"hit": False, "coverage_complete": True}
        paired = compare_specialists([(rows, ["b"], ["a"])], labels, scope="TEST")
        self.assertEqual(paired["common_complete_batches"], 1)
        self.assertEqual(paired["metrics"]["accumulation"]["paired_precision"], 1)
        self.assertFalse(paired["promotion_authorized"])
