import sqlite3
import tempfile
import unittest
from pathlib import Path
from simple_scanner.research_feature_pipeline import capture_to_sidecar

STAMP="2026-10-15T12:00:00+00:00"
def valid():
    return {"c":["102"],"b":["101"],"a":["102"],"o":"100","v":["0","2000"]}

class ResearchPipelineTests(unittest.TestCase):
    def test_end_to_end_offline(self):
        with tempfile.TemporaryDirectory() as d:
            p=Path(d)/"features.sqlite3"
            result=capture_to_sidecar({"A":{},"B":{}},{"A":valid(),"B":valid()},
                                      observed_at=STAMP,path=p)
            self.assertTrue(result["stored"])
            self.assertFalse(result["production_modified"])
            self.assertFalse(result["buy_approved"])
            with sqlite3.connect(p) as con:
                self.assertEqual(con.execute("SELECT COUNT(*) FROM market_features").fetchone()[0],2)
    def test_missing_market_rejected_without_db(self):
        with tempfile.TemporaryDirectory() as d:
            p=Path(d)/"features.sqlite3"
            result=capture_to_sidecar({"A":{},"B":{}},{"A":valid()},
                                      observed_at=STAMP,path=p)
            self.assertFalse(result["stored"])
            self.assertFalse(p.exists())
    def test_no_eligible_pairs(self):
        with tempfile.TemporaryDirectory() as d:
            p=Path(d)/"features.sqlite3"
            self.assertFalse(capture_to_sidecar({}, {},observed_at=STAMP,path=p)["stored"])
            self.assertFalse(p.exists())
    def test_production_storage_rejected(self):
        with self.assertRaises(ValueError):
            capture_to_sidecar({"A":{}},{"A":valid()},observed_at=STAMP,
                               path="/data/research.sqlite3")
    def test_invalid_coverage_threshold(self):
        with self.assertRaises(ValueError):
            capture_to_sidecar({"A":{}},{"A":valid()},observed_at=STAMP,
                               path="unused.sqlite3",minimum_coverage_pct=0)
