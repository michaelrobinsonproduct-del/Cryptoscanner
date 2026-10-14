"""Deterministic offline tests for read-only shadow evaluation."""
import sqlite3
import tempfile
import unittest
from pathlib import Path
from simple_scanner.research_risk_shadow import evaluate

class RiskShadowTests(unittest.TestCase):
    def test_partial_signals_do_not_become_risk_labels(self):
        with tempfile.TemporaryDirectory() as tmp:
            path=Path(tmp)/"history.sqlite3"
            con=sqlite3.connect(path)
            con.executescript("""CREATE TABLE candidate_features(run_at TEXT,pair TEXT,move_15m_pct REAL,volume_accel REAL);
            CREATE TABLE outcomes(run_at TEXT,pair TEXT,horizon_hours INTEGER,return_pct REAL);
            INSERT INTO candidate_features VALUES('2026-10-01','X',-1,5);
            INSERT INTO outcomes VALUES('2026-10-01','X',1,-2);
            INSERT INTO outcomes VALUES('2026-10-01','X',24,100);""")
            con.commit()
            con.close()
            before=path.read_bytes()
            result=evaluate(path)
            self.assertEqual(result["observations"],1)
            self.assertFalse(result["full_risk_validation_possible"])
            self.assertFalse(result["buy_approved"])
            self.assertEqual(result["partial_signal_outcomes"]["NEGATIVE_15M_MOMENTUM"]["average_return_pct"],-2)
            self.assertEqual(result["partial_signal_outcomes"]["VOLUME_SPIKE_REVIEW"]["samples"],1)
            self.assertEqual(before,path.read_bytes())

    def test_missing_db_not_created(self):
        with tempfile.TemporaryDirectory() as tmp:
            path=Path(tmp)/"missing.sqlite3"
            with self.assertRaises(sqlite3.OperationalError):
                evaluate(path)
            self.assertFalse(path.exists())
