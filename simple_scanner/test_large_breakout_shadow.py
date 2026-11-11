"""Regression tests for market-wide large-breakout shadow metrics."""
import sqlite3
import unittest
from unittest.mock import patch
from simple_scanner.shadow_learning import evaluate_market_misses

class LargeBreakoutShadowTests(unittest.TestCase):
    def test_insufficient_history_is_safe(self):
        con=sqlite3.connect(":memory:")
        try:
            con.execute("CREATE TABLE market_signals(run_at TEXT,pair TEXT,move24_pct REAL,spread_bps REAL,notional_24h_usd REAL)")
            con.execute("CREATE TABLE market_observations(run_at TEXT,pair TEXT,price REAL)")
            con.execute("CREATE TABLE snapshots(run_at TEXT,pair TEXT)")
            result=evaluate_market_misses(con)
            self.assertEqual(result["status"],"INSUFFICIENT_MARKET_OUTCOMES")
            self.assertEqual(result["samples"],0)
        finally:
            con.close()

if __name__=="__main__":
    unittest.main()
