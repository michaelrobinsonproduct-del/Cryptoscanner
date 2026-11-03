"""Focused deterministic tests for PAPER WATCH contract (no network or credentials)."""
import datetime as dt
import unittest
from paper_pov.scanner import UTC, watch_contract

class WatchContractTests(unittest.TestCase):
    def setUp(self):
        self.quote = dt.datetime(2026, 11, 3, 1, 0, tzinfo=UTC)
        self.row = {"spread_bps": 12, "volume_accel": 1.5, "move15_pct": 1.8}

    def test_fresh_watch_contract(self):
        x = watch_contract(self.row, self.quote, self.quote + dt.timedelta(seconds=180))
        self.assertEqual(x["status"], "PAPER_WATCH")
        self.assertEqual(x["risk"], "ELEVATED")
        self.assertEqual(x["quote_age_seconds"], 180)
        self.assertFalse(x["buy_approved"])
        self.assertEqual(x["quote_timestamp_semantics"], "client_observed_not_exchange_event_time")

    def test_ten_minute_boundary(self):
        self.assertEqual(watch_contract(self.row, self.quote, self.quote + dt.timedelta(seconds=600))["quote_age_seconds"], 600)
        with self.assertRaisesRegex(ValueError, "freshness"):
            watch_contract(self.row, self.quote, self.quote + dt.timedelta(seconds=601))

    def test_future_quote_rejected(self):
        with self.assertRaises(ValueError):
            watch_contract(self.row, self.quote, self.quote - dt.timedelta(seconds=1))

    def test_risk_escalates(self):
        for change in ({"spread_bps": 35}, {"volume_accel": 0.5}, {"move15_pct": 9}):
            self.assertEqual(watch_contract({**self.row, **change}, self.quote, self.quote)["risk"], "HIGH")

    def test_invalid_liquidity_rejected(self):
        for change in ({"spread_bps": -1}, {"volume_accel": 0}, {"move15_pct": float("nan")}):
            with self.assertRaises(ValueError):
                watch_contract({**self.row, **change}, self.quote, self.quote)

if __name__ == "__main__":
    unittest.main()
