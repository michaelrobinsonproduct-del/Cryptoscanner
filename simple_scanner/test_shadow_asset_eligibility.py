"""Regression tests for isolated shadow precursor eligibility; no network calls."""
import unittest
import sqlite3
import json
import tempfile
import os
from pathlib import Path
from unittest.mock import patch
from simple_scanner.historical_precursor import crypto_pair, rank_precursors, precursor_feature_audit, evaluate_precursor, load_same_run_asset_pairs
from simple_scanner.shadow_learning import early_accumulation_rank, evaluate_early_accumulation, validate_accumulation_history

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

    def test_canonical_rank_excludes_stable_without_changing_sol_score(self):
        rows = [("SOLUSD", 2.0, 10.0, 250000.0, 100.0, 101.0, 100.0),
                ("MYSTERYUSD", 2.0, 10.0, 250000.0, 100.0, 101.0, 100.0)]
        meta = {"SOLUSD": {"base": "SOL"}, "MYSTERYUSD": {"base": "USDS"}}
        self.assertEqual(rank_precursors(rows, asset_pairs=meta), rank_precursors(rows[:1]))

    def test_evaluation_fails_closed_without_same_run_metadata(self):
        with tempfile.TemporaryDirectory() as folder:
            con = sqlite3.connect(":memory:")
            con.execute("CREATE TABLE market_signals (run_at TEXT, pair TEXT, move24_pct REAL, spread_bps REAL, notional_24h_usd REAL)")
            con.execute("CREATE TABLE market_observations (run_at TEXT, pair TEXT, price REAL)")
            con.execute("INSERT INTO market_signals VALUES ('2026-10-18T00:00:00+00:00','SOLUSD',2,10,250000)")
            con.execute("INSERT INTO market_observations VALUES ('2026-10-18T00:00:00+00:00','SOLUSD',101)")
            with patch.dict(os.environ, {"SIMPLE_SCANNER_DATA_DIR": folder}):
                result = evaluate_precursor(con)
            self.assertEqual(result["status"], "AWAITING_CANONICAL_ASSET_METADATA")
            self.assertEqual(result["candidates"], [])
            self.assertFalse(result["promotion_eligible"])
            con.close()

    def test_both_shadow_rankers_exclude_fiat_and_stable(self):
        meta = {"ZGBPZUSD": {"base": "ZGBP"}, "ZEURZUSD": {"base": "ZEUR"},
                "USDSUSD": {"base": "USDS"}, "SOLUSD": {"base": "SOL"}}
        six = [(p, 2.0, 10.0, 250000.0, 100.0, 101.0) for p in meta]
        seven = [(*row, 100.0) for row in six]
        self.assertEqual([r["pair"] for r in early_accumulation_rank(six, meta)], ["SOLUSD"])
        self.assertEqual([r["pair"] for r in rank_precursors(seven, asset_pairs=meta)], ["SOLUSD"])

    def test_metadata_loader_rejects_wrong_timestamp(self):
        with tempfile.TemporaryDirectory() as folder:
            path = Path(folder) / "latest.json"
            path.write_text(json.dumps({"completed_at": "wrong", "asset_pairs": {"SOLUSD": {"base": "SOL"}}}))
            with patch.dict(os.environ, {"SIMPLE_SCANNER_DATA_DIR": folder}):
                self.assertIsNone(load_same_run_asset_pairs("expected"))
                self.assertEqual(load_same_run_asset_pairs("wrong")["SOLUSD"]["base"], "SOL")

    def test_historical_holdout_cannot_claim_identity_coverage(self):
        con = sqlite3.connect(":memory:")
        try:
            con.execute("CREATE TABLE market_signals (run_at TEXT, pair TEXT, move24_pct REAL, spread_bps REAL, notional_24h_usd REAL)")
            con.execute("CREATE TABLE market_observations (run_at TEXT, pair TEXT, price REAL)")
            con.execute("INSERT INTO market_signals VALUES ('2026-10-01T00:00:00+00:00','ZEURZUSD',1,2,100000)")
            con.execute("INSERT INTO market_observations VALUES ('2026-10-01T00:00:00+00:00','ZEURZUSD',1)")
            result = validate_accumulation_history(con)
            self.assertEqual(result["status"], "AWAITING_HISTORICAL_CANONICAL_IDENTITIES")
            self.assertEqual(result["identity_coverage"]["historical_rows_verified"], 0)
            self.assertFalse(result["promotion_eligible"])
            self.assertFalse(result["live_weights_modified"])
            self.assertNotIn("metrics", result)
        finally:
            con.close()

    def test_historical_replay_preserves_unaffected_rank_scores(self):
        # Deterministic 48-snapshot replay: original eligibility vs canonical
        # identity, with fiat and stablecoin identities removed.
        import math
        for step in range(48):
            rows = []
            metadata = {}
            for i in range(18):
                pair = "COIN" + str(i) + "USD"
                older = 100.0 + i
                previous = older * (1 + ((step + i) % 5) / 1000)
                current = previous * (1 + ((step * 3 + i) % 20) / 1000)
                rows.append((pair, 1.0 + (i % 6), 8.0 + i,
                             100000.0 + 1000 * i, previous, current, older))
                metadata[pair] = {"base": "COIN" + str(i)}
            rows.extend([
                ("ZEURZUSD", 0.1, 2.0, 300000, 100, 100.2, 100),
                ("USDSUSD", 0.1, 2.0, 300000, 100, 100.2, 100),
            ])
            metadata.update({"ZEURZUSD": {"base": "ZEUR"},
                             "USDSUSD": {"base": "USDS"}})
            baseline = rank_precursors(rows, limit=100)
            candidate = rank_precursors(rows, limit=100, asset_pairs=metadata)
            baseline_by_pair = {item["pair"]: item for item in baseline}
            self.assertEqual(len(candidate), 18)
            for item in candidate:
                self.assertEqual(item, baseline_by_pair[item["pair"]])
            self.assertNotIn("ZEURZUSD", {item["pair"] for item in candidate})
            self.assertNotIn("USDSUSD", {item["pair"] for item in candidate})

if __name__ == "__main__":
    unittest.main()
