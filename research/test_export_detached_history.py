import json
import sqlite3
import tempfile
import unittest
from pathlib import Path
from export_detached_history import export
from audit_history import audit

class ExportTests(unittest.TestCase):
    def make_db(self, folder):
        db = Path(folder) / 'detached.sqlite3'
        with sqlite3.connect(db) as conn:
            conn.execute('CREATE TABLE market_observations (run_at TEXT, pair TEXT, price REAL)')
            conn.executemany('INSERT INTO market_observations VALUES (?,?,?)', [
                ('2026-01-01T00:00:00+00:00','AUSD',1.0),
                ('2026-01-01T00:00:00+00:00','AUSD',1.0),
                ('2026-01-01T03:00:00+00:00','AUSD',1.5)])
        return db

    def test_export_and_preserve_source(self):
        with tempfile.TemporaryDirectory() as d:
            db=self.make_db(d)
            original=db.read_bytes()
            target=Path(d)/'audit.json'
            export(db,target)
            self.assertEqual(db.read_bytes(),original)
            payload=json.loads(target.read_text())
            self.assertEqual(payload['audit']['tables']['market_observations']['duplicate_pair_timestamps'],1)
            self.assertEqual(len(payload['audit']['tables']['market_observations']['timestamp_gaps_over_90m']),1)
            self.assertEqual(payload['audit']['tables']['outcomes']['status'],'MISSING')
            self.assertEqual(payload['format'],'cryptoscanner-detached-history-audit-v1')

    def test_no_overwrite_existing_export(self):
        with tempfile.TemporaryDirectory() as d:
            db=self.make_db(d)
            target=Path(d)/'audit.json'
            target.write_text('preserve')
            with self.assertRaises(FileExistsError): export(db,target)
            self.assertEqual(target.read_text(),'preserve')

    def test_cannot_export_onto_source(self):
        with tempfile.TemporaryDirectory() as d:
            db=self.make_db(d)
            with self.assertRaises(ValueError): export(db,db)

    def test_corrupt_database_rejected(self):
        with tempfile.TemporaryDirectory() as d:
            db=Path(d)/'corrupt.sqlite3'
            db.write_bytes(b'not a sqlite database')
            target=Path(d)/'audit.json'
            with self.assertRaises(sqlite3.DatabaseError): export(db,target)
            self.assertFalse(target.exists())

    def test_missing_evaluation_observation_and_bad_label(self):
        with tempfile.TemporaryDirectory() as d:
            db=Path(d)/'detached.sqlite3'
            with sqlite3.connect(db) as conn:
                conn.execute('CREATE TABLE snapshots (run_at TEXT,pair TEXT,price REAL)')
                conn.execute('CREATE TABLE market_observations (run_at TEXT,pair TEXT,price REAL)')
                conn.execute('CREATE TABLE outcomes (run_at TEXT,pair TEXT,horizon_hours INTEGER,evaluated_at TEXT,return_pct REAL)')
                conn.execute("INSERT INTO snapshots VALUES ('2026-01-01T00:00:00+00:00','AUSD',10)")
                conn.execute("INSERT INTO market_observations VALUES ('2026-01-01T01:00:00+00:00','AUSD',12)")
                conn.execute("INSERT INTO outcomes VALUES ('2026-01-01T00:00:00+00:00','AUSD',1,'2026-01-01T01:00:00+00:00',10)")
                conn.execute("INSERT INTO outcomes VALUES ('2026-01-01T00:00:00+00:00','AUSD',3,'2026-01-01T03:00:00+00:00',15)")
            labels=audit(db)['tables']['outcomes']['label_checks']
            self.assertEqual(labels['return_mismatch_gt_0_02pp'],1)
            self.assertEqual(labels['missing_evaluation_observation'],1)

if __name__=='__main__': unittest.main()
