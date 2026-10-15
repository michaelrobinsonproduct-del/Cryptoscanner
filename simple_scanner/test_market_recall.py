import sqlite3
import tempfile
import unittest
from pathlib import Path
from simple_scanner.market_recall import baseline_recall

class MarketRecallTests(unittest.TestCase):
    def make_db(self, p):
        c=sqlite3.connect(p)
        c.execute("CREATE TABLE market_observations(run_at TEXT,pair TEXT,price REAL)")
        c.execute("CREATE TABLE snapshots(run_at TEXT,pair TEXT,price REAL,score REAL)")
        for pair in ("A","B","C"):
            c.execute("INSERT INTO market_observations VALUES(?,?,?)",("2026-10-01T00:00:00+00:00",pair,100))
            c.execute("INSERT INTO market_observations VALUES(?,?,?)",("2026-10-01T00:15:00+00:00",pair,110 if pair!="C" else 102))
        c.execute("INSERT INTO snapshots VALUES(?,?,?,?)",("2026-10-01T00:00:00+00:00","A",100,50))
        c.commit();c.close()
    def test_recall_and_read_only(self):
        with tempfile.TemporaryDirectory() as d:
            p=Path(d)/"h.sqlite3";self.make_db(p)
            before=p.read_bytes()
            r=baseline_recall(p)
            self.assertEqual((r["breakouts"],r["caught"],r["missed"]),(2,1,1))
            self.assertEqual(r["recall"],0.5)
            self.assertFalse(r["promotion_eligible"])
            self.assertEqual(before,p.read_bytes())
    def test_strict_gap(self):
        with tempfile.TemporaryDirectory() as d:
            p=Path(d)/"h.sqlite3";self.make_db(p)
            self.assertEqual(baseline_recall(p,max_gap_minutes=5)["breakouts"],0)
    def test_missing_history_fails(self):
        with tempfile.TemporaryDirectory() as d:
            with self.assertRaises(sqlite3.OperationalError):
                baseline_recall(Path(d)/"missing.sqlite3")
