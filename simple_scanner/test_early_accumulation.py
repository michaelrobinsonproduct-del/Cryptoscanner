"""Early accumulation shadow research tests; no production scoring changes."""
import sqlite3
import unittest
import tempfile
import os
import json
from pathlib import Path
from unittest.mock import patch
from simple_scanner.shadow_learning import early_accumulation_rank, evaluate_early_accumulation

class AccumulationTests(unittest.TestCase):
    def test_ranks_early_not_extended(self):
        rows=[("EARLY",1,10,250000,100,101),
              ("EXTENDED",35,10,500000,100,101),
              ("ILLQ",1,10,2000,100,101),
              ("WIDE",1,300,500000,100,101)]
        ranked=early_accumulation_rank(rows)
        self.assertEqual([r["pair"] for r in ranked],["EARLY"])

    def test_rejects_missing_invalid_prices(self):
        self.assertEqual(early_accumulation_rank([("BAD",1,10,100000,0,10)]),[])

    def test_missing_history_fails_closed(self):
        con=sqlite3.connect(":memory:")
        try:
            result=evaluate_early_accumulation(con)
            self.assertEqual(result["status"],"AWAITING_MARKET_HISTORY")
            self.assertIs(result["buy_approved"],False)
        finally:
            con.close()

    def test_only_prior_observations(self):
        con=sqlite3.connect(":memory:")
        try:
            con.execute("CREATE TABLE market_signals(run_at TEXT,pair TEXT,move24_pct REAL,spread_bps REAL,notional_24h_usd REAL)")
            con.execute("CREATE TABLE market_observations(run_at TEXT,pair TEXT,price REAL)")
            con.executemany("INSERT INTO market_signals VALUES(?,?,?,?,?)",[("2026-10-17T00:15:00+00:00","ABC",1,10,250000)])
            con.executemany("INSERT INTO market_observations VALUES(?,?,?)",[
                ("2026-10-17T00:00:00+00:00","ABC",100),
                ("2026-10-17T00:15:00+00:00","ABC",101)])
            with tempfile.TemporaryDirectory() as folder:
                Path(folder, "latest.json").write_text(json.dumps({
                    "completed_at": "2026-10-17T00:15:00+00:00",
                    "asset_pairs": {"ABC": {"base": "ABC"}}}))
                with patch.dict(os.environ, {"SIMPLE_SCANNER_DATA_DIR": folder}):
                    result=evaluate_early_accumulation(con)
            self.assertEqual(result["status"],"SHADOW_CANDIDATES")
            self.assertEqual(result["history_eligible"],1)
            self.assertEqual(result["candidates"][0]["pair"],"ABC")
            self.assertIs(result["buy_approved"],False)
        finally:
            con.close()

if __name__=="__main__":
    unittest.main()
