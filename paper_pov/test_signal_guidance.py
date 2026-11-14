"""Focused signal guidance contracts: no fabricated 30% odds or trades."""
import math
import unittest

from paper_pov.signal_guidance import assess, action_text


class SignalGuidanceTests(unittest.TestCase):
    def setUp(self):
        self.strong = {
            "price_usd": 1.50, "challenger_score": 95.0,
            "move15_pct": 0.8, "volume_accel": 3.1, "spread_bps": 6.0,
        }

    def test_strong_signal_can_suggest_small_research_entry_but_not_odds(self):
        out = assess(self.strong)
        self.assertEqual(out["signal_confidence"], "STRONG")
        self.assertGreaterEqual(out["signal_confidence_score"], 75)
        self.assertEqual(out["risk"], "HIGH")
        self.assertEqual(out["recommendation"], "CONSIDER_SMALL_ENTRY")
        self.assertIsNone(out["gain_probability_pct"])
        self.assertEqual(out["target_gain_pct"], 30)
        self.assertEqual(out["horizon_hours"], 48)
        self.assertFalse(out["signal_confidence_is_probability"])
        self.assertFalse(out["recommendation_is_trade_authorization"])
        self.assertEqual(action_text(out["recommendation"]), "Consider small entry")

    def test_weak_negative_low_volume_signal_is_no_action(self):
        row = {**self.strong, "challenger_score": 18.0,
               "move15_pct": -1.7, "volume_accel": 0.15, "spread_bps": 48.0}
        out = assess(row)
        self.assertEqual(out["risk"], "EXTREME")
        self.assertEqual(out["recommendation"], "DO_NOTHING")
        self.assertIsNone(out["gain_probability_pct"])

    def test_independent_legacy_uses_own_score_and_missing_spread_is_risky(self):
        legacy = {**self.strong, "legacy_score": 45.0}
        legacy.pop("spread_bps")
        out = assess(legacy, score_field="legacy_score", overlap=True)
        self.assertEqual(out["risk"], "VERY_HIGH")
        self.assertTrue(out["independent_legacy_overlap_verified"])
        self.assertEqual(out["recommendation"], "WATCH")
        self.assertIn("spread unavailable", " ".join(out["risk_reasons"]))

    def test_substantial_entry_requires_verified_holdout_not_just_high_score(self):
        out = assess(self.strong, overlap=True)
        self.assertEqual(out["recommendation"], "CONSIDER_SMALL_ENTRY")
        untrusted = {
            "source_authenticated": False, "independent_held_out": True,
            "qualified_48h_samples": 999, "calibration_verified": True,
            "probability_pct": 99.0,
        }
        self.assertIsNone(assess(self.strong, overlap=True,
                                 validated_calibration=untrusted)["gain_probability_pct"])
        qualified = {**untrusted, "source_authenticated": True}
        proven = assess(self.strong, overlap=True, validated_calibration=qualified)
        self.assertEqual(proven["gain_probability_pct"], 99.0)
        self.assertEqual(proven["recommendation"], "CONSIDER_MORE_SUBSTANTIAL_ENTRY")

    def test_thin_liquidity_increases_risk_without_changing_signal_rank(self):
        liquid = assess({**self.strong, "notional_24h_usd": 6000000})
        thin = assess({**self.strong, "notional_24h_usd": 120000})
        self.assertGreater(thin["risk_score"], liquid["risk_score"])
        self.assertEqual(liquid["signal_confidence_score"],
                         thin["signal_confidence_score"])
        self.assertIn("Thin reported 24h USD turnover", " ".join(thin["risk_reasons"]))

    def test_reject_nonfinite_and_malformed_features(self):
        for field, value in (("volume_accel", -1), ("price_usd", 0),
                             ("move15_pct", math.nan),
                             ("challenger_score", float("inf")),
                             ("spread_bps", -1), ("volume_accel", True)):
            with self.subTest(field=field, value=value), self.assertRaises(ValueError):
                assess({**self.strong, field: value})
        with self.assertRaises(ValueError):
            assess(self.strong, score_field="legacy_score")


if __name__ == "__main__":
    unittest.main()
