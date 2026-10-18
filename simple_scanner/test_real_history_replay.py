"""Offline replay fixtures never access production history."""
import json
from pathlib import Path
import sqlite3
import tempfile
import unittest
from simple_scanner.real_history_replay import replay

class RealHistoryReplayTests(unittest.TestCase):
    def test_missing_identity_blocks_and_verified_replay_preserves_scores(self):
        with tempfile.TemporaryDirectory() as folder:
            db=Path(folder)/"history.sqlite3"
            identities=Path(folder)/"identities.json"
            with sqlite3.connect(db) as con:
                con.execute("CREATE TABLE market_signals(run_at TEXT,pair TEXT,move24_pct REAL,spread_bps REAL,notional_24h_usd REAL)")
                con.execute("CREATE TABLE market_observations(run_at TEXT,pair TEXT,price REAL)")
                for pair in ("SOLUSD","ZEURZUSD"):
                    for minute,price in ((0,100),(15,100.5),(30,101)):
                        run=f"2026-10-18T00:{minute:02d}:00+00:00"
                        con.execute("INSERT INTO market_signals VALUES (?,?,?,?,?)",(run,pair,2,10,250000))
                        con.execute("INSERT INTO market_observations VALUES (?,?,?)",(run,pair,price))
            identities.write_text(json.dumps({"SOLUSD":{"base":"SOL"}}))
            blocked=replay(db,identities)
            self.assertEqual(blocked["status"],"BLOCKED_UNVERIFIED_IDENTITIES")
            self.assertEqual(blocked["missing_examples"],["ZEURZUSD"])
            identities.write_text(json.dumps({"SOLUSD":{"base":"SOL"},"ZEURZUSD":{"base":"ZEUR"}}))
            self.assertEqual(replay(db,identities)["status"],"BLOCKED_UNVERIFIED_IDENTITIES")
            def verified(base):
                return {"base":base,"source":"kraken_assetpairs",
                        "observed_at":"2026-10-18T00:00:00+00:00",
                        "evidence_ref":"archive/kraken-assetpairs-20261018.json"}
            identities.write_text(json.dumps({"SOLUSD":verified("SOL"),"ZEURZUSD":verified("ZEUR")}))
            result=replay(db,identities)
            self.assertTrue(result["passed"])
            self.assertEqual(result["rows"],6)
            self.assertEqual(result["excluded_fiat_stable_rows"],3)

if __name__=="__main__":
    unittest.main()
