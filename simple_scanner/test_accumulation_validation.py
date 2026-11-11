"""Fail-closed tests for historical accumulation validation."""
import sqlite3
import unittest
from simple_scanner.shadow_learning import validate_accumulation_history

class HistoricalValidationTests(unittest.TestCase):
    def test_missing_tables(self):
        con=sqlite3.connect(":memory:")
        try:
            result=validate_accumulation_history(con)
            self.assertEqual(result["status"],"AWAITING_HISTORY")
            self.assertIs(result["promotion_eligible"],False)
        finally:
            con.close()

    def test_insufficient_matured_data(self):
        con=sqlite3.connect(":memory:")
        try:
            con.execute("CREATE TABLE market_signals(run_at TEXT,pair TEXT,move24_pct REAL,spread_bps REAL,notional_24h_usd REAL)")
            con.execute("CREATE TABLE market_observations(run_at TEXT,pair TEXT,price REAL)")
            result=validate_accumulation_history(con)
            self.assertEqual(result["status"],"INSUFFICIENT_MATURED_HISTORY")
            self.assertEqual(result["samples"],0)
            self.assertIs(result["promotion_eligible"],False)
        finally:
            con.close()

if __name__=="__main__":
    unittest.main()
