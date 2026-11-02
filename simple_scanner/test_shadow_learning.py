"""Shadow learner safety tests."""
import sqlite3,tempfile,unittest
from pathlib import Path
from simple_scanner.shadow_learning import evaluate
class ShadowTests(unittest.TestCase):
 def test_empty_history_cannot_promote(self):
  with tempfile.TemporaryDirectory() as d:
   p=Path(d)/"history.sqlite3"; c=sqlite3.connect(p)
   c.execute("CREATE TABLE candidate_features(run_at TEXT,pair TEXT,move_15m_pct REAL,volume_accel REAL,base_score REAL)")
   c.execute("CREATE TABLE outcomes(run_at TEXT,pair TEXT,horizon_hours INTEGER,return_pct REAL)")
   c.commit();c.close()
   r=evaluate(p)
   self.assertEqual(r["status"],"INSUFFICIENT_DATA")
   self.assertFalse(r["buy_approved"])
   self.assertFalse(r["live_weights_modified"])
 def test_no_mutation_of_existing_database(self):
  with tempfile.TemporaryDirectory() as d:
   p=Path(d)/"history.sqlite3";c=sqlite3.connect(p)
   c.execute("CREATE TABLE candidate_features(run_at TEXT,pair TEXT,move_15m_pct REAL,volume_accel REAL,base_score REAL)")
   c.execute("CREATE TABLE outcomes(run_at TEXT,pair TEXT,horizon_hours INTEGER,return_pct REAL)")
   c.commit();c.close()
   before=p.read_bytes();evaluate(p);self.assertEqual(before,p.read_bytes())
