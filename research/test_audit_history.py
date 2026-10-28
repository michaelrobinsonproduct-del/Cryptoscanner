import sqlite3
import tempfile
import unittest
from pathlib import Path
from audit_history import audit
class AuditTests(unittest.TestCase):
    def test_read_only_duplicates_gaps(self):
        with tempfile.TemporaryDirectory() as d:
            db=Path(d)/'fixture.sqlite3'
            with sqlite3.connect(db) as con:
                con.execute('CREATE TABLE market_observations (run_at TEXT,pair TEXT,price REAL)')
                con.executemany('INSERT INTO market_observations VALUES (?,?,?)',[('2026-01-01T00:00:00+00:00','ABCUSD',1),('2026-01-01T00:00:00+00:00','ABCUSD',1),('2026-01-01T02:00:00+00:00','ABCUSD',2)])
            before=db.read_bytes();r=audit(db)
            self.assertEqual(db.read_bytes(),before)
            self.assertEqual(r['tables']['market_observations']['duplicate_pair_timestamps'],1)
            self.assertEqual(len(r['tables']['market_observations']['timestamp_gaps_over_90m']),1)
            self.assertEqual(r['tables']['outcomes']['status'],'MISSING')
    def test_label_mismatch(self):
        with tempfile.TemporaryDirectory() as d:
            db=Path(d)/'fixture.sqlite3'
            with sqlite3.connect(db) as con:
                con.execute('CREATE TABLE snapshots (run_at TEXT,pair TEXT,price REAL)')
                con.execute('CREATE TABLE market_observations (run_at TEXT,pair TEXT,price REAL)')
                con.execute('CREATE TABLE outcomes (run_at TEXT,pair TEXT,horizon_hours INTEGER,evaluated_at TEXT,return_pct REAL)')
                con.execute("INSERT INTO snapshots VALUES ('2026-01-01T00:00:00+00:00','ABCUSD',10)")
                con.execute("INSERT INTO market_observations VALUES ('2026-01-01T01:00:00+00:00','ABCUSD',12)")
                con.execute("INSERT INTO outcomes VALUES ('2026-01-01T00:00:00+00:00','ABCUSD',1,'2026-01-01T01:00:00+00:00',10)")
            self.assertEqual(audit(db)['tables']['outcomes']['label_checks']['return_mismatch_gt_0_02pp'],1)
if __name__=='__main__':unittest.main()
