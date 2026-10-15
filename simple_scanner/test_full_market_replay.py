import sqlite3
import tempfile
import unittest
from pathlib import Path
from simple_scanner.full_market_replay import replay

class ReplayTests(unittest.TestCase):
    def test_point_in_time_and_no_mutation(self):
        with tempfile.TemporaryDirectory() as d:
            p=Path(d)/"history.sqlite3"
            c=sqlite3.connect(p)
            c.execute("CREATE TABLE market_observations(run_at TEXT,pair TEXT,price REAL)")
            c.execute("CREATE TABLE snapshots(run_at TEXT,pair TEXT)")
            for t,price in (("00:00",100),("00:15",102),("00:30",110)):
                c.execute("INSERT INTO market_observations VALUES(?,?,?)",
                          (f"2026-10-01T{t}:00+00:00","A",price))
            c.execute("INSERT INTO snapshots VALUES(?,?)",("2026-10-01T00:15:00+00:00","A"))
            c.commit();c.close()
            before=p.read_bytes()
            result=replay(p)
            self.assertEqual(before,p.read_bytes())
            self.assertEqual(len(result["events"]),1)
            event=result["events"][0]
            self.assertAlmostEqual(event["prior_momentum_pct"],2)
            self.assertTrue(event["breakout"])
            self.assertTrue(event["baseline_selected"])
            self.assertFalse(result["promotion_eligible"])
            self.assertFalse(result["feature_parity_verified"])
    def test_empty_market(self):
        with tempfile.TemporaryDirectory() as d:
            p=Path(d)/"history.sqlite3";c=sqlite3.connect(p)
            c.execute("CREATE TABLE market_observations(run_at TEXT,pair TEXT,price REAL)")
            c.execute("CREATE TABLE snapshots(run_at TEXT,pair TEXT)")
            c.commit();c.close()
            self.assertEqual(replay(p)["events"],[])
