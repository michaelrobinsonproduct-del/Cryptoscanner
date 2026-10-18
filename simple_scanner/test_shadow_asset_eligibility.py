"""Regression tests for isolated shadow precursor eligibility; no network calls."""
import unittest
from simple_scanner.historical_precursor import crypto_pair, rank_precursors, precursor_feature_audit

class ShadowEligibilityTests(unittest.TestCase):
    def test_stablecoin_aliases_excluded(self):
        for symbol in ("USDT", "USDC", "DAI", "PYUSD", "EURC", "RLUSD",
                       "TUSD", "FDUSD", "USDD", "USDE", "USDG", "USDS",
                       "UST", "USTC"):
            with self.subTest(symbol=symbol):
                self.assertFalse(crypto_pair(symbol + "USD"))

    def test_legitimate_volatile_symbols_remain(self):
        for symbol in ("BTC", "XXBT", "ETH", "XETH", "SOL", "SUI", "STBL", "US"):
            with self.subTest(symbol=symbol):
                self.assertTrue(crypto_pair(symbol + "USD"))

    def test_canonical_kraken_base_overrides_misleading_pair(self):
        meta = {"MYSTERYUSD": {"base": "USDS"}, "USDSUSD": {"base": "SOL"},
                "XXBTZUSD": {"base": "XXBT"}}
        self.assertFalse(crypto_pair("MYSTERYUSD", meta))
        self.assertTrue(crypto_pair("USDSUSD", meta))
        self.assertTrue(crypto_pair("XXBTZUSD", meta))
        self.assertFalse(crypto_pair("UNKNOWNUSD", meta))

    def test_scoring_unchanged_for_eligible_asset(self):
        row = ("SOLUSD", 2.0, 10.0, 250000.0, 100.0, 101.0, 100.0)
        result = rank_precursors([row])
        self.assertEqual(len(result), 1)
        self.assertEqual(result[0]["pair"], "SOLUSD")
        self.assertEqual(result[0]["recent_change_pct"], 1.0)

    def test_stablecoin_never_ranked(self):
        rows = [(s + "USD", 2.0, 10.0, 250000.0, 100.0, 101.0, 100.0)
                for s in ("USDG", "USDS", "UST", "USTC")]
        self.assertEqual(rank_precursors(rows), [])

    def test_audit_is_observe_only_and_does_not_change_ranking(self):
        rows = [("SOLUSD", 2.0, 10.0, 250000.0, 100.0, 101.0, 100.0),
                ("USDSUSD", 2.0, 10.0, 250000.0, 100.0, 101.0, 100.0)]
        before = rank_precursors(rows)
        audit = precursor_feature_audit(rows)
        after = rank_precursors(rows)
        self.assertEqual(before, after)
        self.assertEqual(audit["mode"], "OBSERVE_ONLY")
        self.assertEqual(audit["score_adjustment"], 0)
        self.assertFalse(audit["promotion_eligible"])
        self.assertEqual(audit["counts"]["rows"], 2)
        self.assertEqual(audit["counts"]["eligible_identity"], 1)

    def test_audit_handles_invalid_history(self):
        rows = [("SOLUSD", 2.0, 10.0, 250000.0, None, 101.0, 100.0)]
        self.assertEqual(precursor_feature_audit(rows)["counts"]["valid_numeric"], 0)

if __name__ == "__main__":
    unittest.main()
