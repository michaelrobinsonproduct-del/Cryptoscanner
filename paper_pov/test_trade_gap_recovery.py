"""Adversarial Kraken trade gap recovery acceptance tests; no live writes."""
import copy
import datetime as dt
import hashlib
import unittest

from paper_pov.trade_gap_recovery import (
    REVISION, SOURCE_URL, canonical, verify_captured_bucket)

UTC = dt.timezone.utc
START = dt.datetime(2026, 11, 1, 12, 0, tzinfo=UTC)
NOW = START + dt.timedelta(minutes=10)


def captured():
    raw = {
        "pair": "TESTUSD",
        "candle": [int(START.timestamp()), "2", "3", "2", "3", "2.5", "4", 2],
        "trades": [
            {"id": "t1", "at": (START + dt.timedelta(seconds=30)).isoformat(),
             "price": "2", "volume": "2"},
            {"id": "t2", "at": (START + dt.timedelta(seconds=90)).isoformat(),
             "price": "3", "volume": "2"}]}
    return {"revision": REVISION, "source_url": SOURCE_URL,
            "retrieved_at": (START + dt.timedelta(minutes=6)).isoformat(),
            "raw_response": raw, "raw_sha256": hashlib.sha256(canonical(raw)).hexdigest()}


def reseal(x):
    x["raw_sha256"] = hashlib.sha256(canonical(x["raw_response"])).hexdigest()
    return x


class TradeBucketRecoveryTests(unittest.TestCase):
    def test_complete_two_trade_bucket_accepted_without_imputation(self):
        s = captured()
        result = verify_captured_bucket(s, "TESTUSD", START, NOW)
        self.assertEqual(result["trade_count"], 2)
        self.assertEqual(result["source_sha256"], s["raw_sha256"])
        self.assertEqual(len(result["observations"]), 2)
        self.assertFalse(result["ledger_modified"])
        self.assertFalse(result["exchange_signed"])

    def test_checksum_and_pair_mismatch_fail_closed(self):
        s = captured()
        s["raw_response"]["pair"] = "OTHERUSD"
        with self.assertRaisesRegex(ValueError, "checksum"):
            verify_captured_bucket(s, "TESTUSD", START, NOW)
        reseal(s)
        with self.assertRaisesRegex(ValueError, "pair"):
            verify_captured_bucket(s, "TESTUSD", START, NOW)

    def test_missing_trade_never_fills_ohlc(self):
        s = captured()
        s["raw_response"]["trades"].pop()
        reseal(s)
        with self.assertRaisesRegex(ValueError, "count"):
            verify_captured_bucket(s, "TESTUSD", START, NOW)

    def test_duplicate_trade_id_and_out_of_bucket_fail(self):
        s = captured()
        s["raw_response"]["trades"][1]["id"] = "t1"
        reseal(s)
        with self.assertRaisesRegex(ValueError, "duplicate"):
            verify_captured_bucket(s, "TESTUSD", START, NOW)
        s = captured()
        s["raw_response"]["trades"][1]["at"] = (START + dt.timedelta(minutes=6)).isoformat()
        reseal(s)
        with self.assertRaisesRegex(ValueError, "Out-of-bucket"):
            verify_captured_bucket(s, "TESTUSD", START, NOW)

    def test_fabricated_high_or_volume_cannot_be_recovered(self):
        for idx, value in ((2, "9"), (6, "99"), (5, "2.4")):
            s = captured()
            s["raw_response"]["candle"][idx] = value
            reseal(s)
            with self.assertRaisesRegex(ValueError, "reconstruct"):
                verify_captured_bucket(s, "TESTUSD", START, NOW)

    def test_unclosed_future_and_revision_fail(self):
        s = captured()
        s["retrieved_at"] = (START + dt.timedelta(minutes=4)).isoformat()
        with self.assertRaisesRegex(ValueError, "Incomplete"):
            verify_captured_bucket(s, "TESTUSD", START, NOW)
        s = captured()
        with self.assertRaises(ValueError):
            verify_captured_bucket(s, "TESTUSD", START, START + dt.timedelta(minutes=5))
        s = captured()
        s["revision"] = "unverified-archive"
        with self.assertRaisesRegex(ValueError, "revision"):
            verify_captured_bucket(s, "TESTUSD", START, NOW)

    def test_nonmonotonic_and_naive_trade_time_fail(self):
        s = captured()
        s["raw_response"]["trades"][1]["at"] = (START + dt.timedelta(seconds=20)).isoformat()
        reseal(s)
        with self.assertRaisesRegex(ValueError, "nonmonotonic"):
            verify_captured_bucket(s, "TESTUSD", START, NOW)
        s = captured()
        s["raw_response"]["trades"][0]["at"] = "2026-11-01T12:00:30"
        reseal(s)
        with self.assertRaisesRegex(ValueError, "naive"):
            verify_captured_bucket(s, "TESTUSD", START, NOW)


if __name__ == "__main__":
    unittest.main()
