"""Adversarial, offline, no-network tests for independent shadow overlap."""
import copy
import datetime as dt
import hashlib
import json
import unittest

from paper_pov.learning_overlap import compare


SHA40 = "a" * 40
SHA64 = "b" * 64


def current():
    return {"schema": 1, "status": "SUCCESS_PAPER_ONLY", "run_id": "1234",
            "source_sha": SHA40, "ledger_commit": SHA40, "ledger_sha256": SHA64,
            "remote_readback_verified": True, "production_applied": False,
            "buy_approved": False, "as_of": "2026-11-01T16:00:00+00:00",
            "candidates": [
                {"symbol": "TRX/USD", "rank": 1, "status": "WATCH_PAPER_ONLY",
                 "price_usd": 0.31, "challenger_score": 77.2,
                 "quote_observed_at": "2026-11-01T15:59:55+00:00"},
                {"symbol": "UNI/USD", "rank": 2, "status": "WATCH_PAPER_ONLY",
                 "price_usd": 7.31, "challenger_score": 66.1,
                 "quote_observed_at": "2026-11-01T15:59:54+00:00"}]}


def shadow():
    return {"schema": 1, "mode": "LEGACY_INSPIRED_SHADOW",
            "independent_execution": True, "run_id": "5678",
            "source_sha": "c" * 40, "strategy_name": "legacy-inspired-separate-v1",
            "production_applied": False, "buy_approved": False,
            "as_of": "2026-11-01T16:00:15Z",
            "feature_cutoff_utc": "2026-11-01T16:00:00Z",
            "candidates": [
                {"symbol": "UNI/USD", "rank": 1, "status": "WATCH_PAPER_ONLY",
                 "price_usd": 7.32, "legacy_score": 52.0,
                 "quote_observed_at": "2026-11-01T16:00:10Z"},
                {"symbol": "AVAX/USD", "rank": 2, "status": "WATCH_PAPER_ONLY",
                 "price_usd": 8.74, "legacy_score": 48.0,
                 "quote_observed_at": "2026-11-01T16:00:11Z"}]}


def execute(main=None, other=None, *, digest=None, run_id="5678"):
    main = current() if main is None else main
    other = shadow() if other is None else other
    data = json.dumps(other, sort_keys=True).encode()
    current_data = json.dumps(main, sort_keys=True).encode()
    return compare(current_data, data, expected_current_sha256=hashlib.sha256(current_data).hexdigest(),
                   expected_current_run_id="1234", expected_ledger_sha256=SHA64,
                   expected_legacy_sha256=digest or hashlib.sha256(data).hexdigest(),
                   expected_legacy_run_id=run_id)


class OverlapTests(unittest.TestCase):
    def test_real_independent_overlap(self):
        result = execute()
        self.assertEqual(result["overlap_count"], 1)
        self.assertEqual(result["both_identified"][0]["symbol"], "UNI/USD")
        self.assertEqual((result["both_identified"][0]["current_rank"],
                          result["both_identified"][0]["legacy_rank"]), (2, 1))
        self.assertIsNone(result["performance_lift"])
        self.assertFalse(result["trading_authorized"])

    def test_no_overlap_is_honest(self):
        a = shadow()
        a["candidates"][0]["symbol"] = "ETH/USD"
        self.assertEqual(execute(other=a)["overlap_count"], 0)

    def test_digest_mismatch(self):
        with self.assertRaisesRegex(ValueError, "digest"):
            execute(digest="0" * 64)

    def test_current_digest_mismatch(self):
        a = current()
        data = json.dumps(a, sort_keys=True).encode()
        b = json.dumps(shadow(), sort_keys=True).encode()
        with self.assertRaisesRegex(ValueError, "Current artifact digest"):
            compare(data, b, expected_current_sha256="0" * 64,
                    expected_current_run_id="1234", expected_ledger_sha256=SHA64,
                    expected_legacy_sha256=hashlib.sha256(b).hexdigest(),
                    expected_legacy_run_id="5678")

    def test_unsealed_current(self):
        a = current()
        a["remote_readback_verified"] = False
        with self.assertRaisesRegex(ValueError, "anchored"):
            execute(main=a)

    def test_wrong_ledger(self):
        a = current()
        a["ledger_sha256"] = "0" * 64
        with self.assertRaisesRegex(ValueError, "anchored"):
            execute(main=a)

    def test_forged_independence(self):
        a = shadow()
        a["independent_execution"] = False
        with self.assertRaisesRegex(ValueError, "strategy"):
            execute(other=a)

    def test_same_run_not_independent(self):
        a = shadow()
        a["run_id"] = "1234"
        with self.assertRaisesRegex(ValueError, "execution"):
            execute(other=a, run_id="1234")

    def test_future_features_rejected(self):
        a = shadow()
        a["feature_cutoff_utc"] = "2026-11-01T16:00:16Z"
        with self.assertRaisesRegex(ValueError, "future"):
            execute(other=a)

    def test_time_misalignment_rejected(self):
        a = shadow()
        a["as_of"] = "2026-11-01T16:03:00Z"
        with self.assertRaisesRegex(ValueError, "time-aligned"):
            execute(other=a)

    def test_future_quote_rejected(self):
        a = shadow()
        a["candidates"][0]["quote_observed_at"] = "2026-11-01T16:00:16Z"
        with self.assertRaisesRegex(ValueError, "quote"):
            execute(other=a)

    def test_stale_quote_rejected(self):
        a = shadow()
        a["candidates"][0]["quote_observed_at"] = "2026-11-01T15:40:00Z"
        with self.assertRaisesRegex(ValueError, "quote"):
            execute(other=a)

    def test_baseline_relabel_rejected(self):
        a = shadow()
        a["candidates"][0]["baseline_score"] = 52
        with self.assertRaisesRegex(ValueError, "relabel"):
            execute(other=a)

    def test_duplicate_pair_rejected(self):
        a = shadow()
        a["candidates"][1]["symbol"] = "UNI/USD"
        with self.assertRaisesRegex(ValueError, "duplicate"):
            execute(other=a)

    def test_stablecoin_base_rejected(self):
        a = shadow()
        a["candidates"][0]["symbol"] = "USDT/USD"
        with self.assertRaisesRegex(ValueError, "canonical"):
            execute(other=a)

    def test_noncanonical_alias_rejected(self):
        a = shadow()
        a["candidates"][0]["symbol"] = "uni/usd"
        with self.assertRaisesRegex(ValueError, "canonical"):
            execute(other=a)

    def test_nonfinite_score_rejected(self):
        a = shadow()
        a["candidates"][0]["legacy_score"] = float("nan")
        with self.assertRaisesRegex(ValueError, "Nonfinite"):
            execute(other=a)

    def test_naive_timestamp_rejected(self):
        a = shadow()
        a["as_of"] = "2026-11-01T16:00:15"
        with self.assertRaisesRegex(ValueError, "Naive"):
            execute(other=a)

    def test_rank_tampering_rejected(self):
        a = shadow()
        a["candidates"][0]["rank"] = 2
        with self.assertRaisesRegex(ValueError, "ranking"):
            execute(other=a)

    def test_no_trading_claim(self):
        a = shadow()
        a["buy_approved"] = True
        with self.assertRaisesRegex(ValueError, "strategy"):
            execute(other=a)


if __name__ == "__main__":
    unittest.main()
