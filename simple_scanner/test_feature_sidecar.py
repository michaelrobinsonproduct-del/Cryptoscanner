import sqlite3
import tempfile
import unittest
from pathlib import Path
from simple_scanner.feature_sidecar import persist_features

def capture(stamp,pair="A"):
    return {"status":"DIAGNOSTIC_ONLY","records":[{"pair":pair,"observed_at":stamp,
        "price":100,"spread_bps":2,"notional_24h_usd":100000,"move_24h_pct":1}]}

class SidecarTests(unittest.TestCase):
    def test_store_and_bounded_retention(self):
        with tempfile.TemporaryDirectory() as d:
            p=Path(d)/"research.sqlite3"
            for h in (0,1,2):
                stamp=f"2026-10-15T{h:02d}:00:00+00:00"
                result=persist_features(p,capture(stamp),observed_at=stamp,keep_runs=2)
                self.assertFalse(result["production_modified"])
            con=sqlite3.connect(p)
            self.assertEqual(con.execute("SELECT COUNT(*) FROM market_features").fetchone()[0],2)
            self.assertEqual(con.execute("SELECT MIN(observed_at) FROM market_features").fetchone()[0],"2026-10-15T01:00:00+00:00")
            con.close()
    def test_duplicate_rejected(self):
        with tempfile.TemporaryDirectory() as d:
            p=Path(d)/"research.sqlite3";stamp="2026-10-15T00:00:00+00:00"
            persist_features(p,capture(stamp),observed_at=stamp)
            with self.assertRaises(ValueError):
                persist_features(p,capture(stamp),observed_at=stamp)
    def test_protected_path_rejected(self):
        stamp="2026-10-15T00:00:00+00:00"
        with self.assertRaises(ValueError):
            persist_features("/data/history.sqlite3",capture(stamp),observed_at=stamp)
    def test_bad_record_rejected_without_creating_db(self):
        with tempfile.TemporaryDirectory() as d:
            p=Path(d)/"research.sqlite3";stamp="2026-10-15T00:00:00+00:00"
            bad=capture(stamp);bad["records"][0]["price"]=-1
            with self.assertRaises(ValueError):
                persist_features(p,bad,observed_at=stamp)
            self.assertFalse(p.exists())
    def test_duplicate_pairs_rejected(self):
        with tempfile.TemporaryDirectory() as d:
            stamp="2026-10-15T00:00:00+00:00";bad=capture(stamp)
            bad["records"].append(dict(bad["records"][0]))
            with self.assertRaises(ValueError):
                persist_features(Path(d)/"research.sqlite3",bad,observed_at=stamp)
