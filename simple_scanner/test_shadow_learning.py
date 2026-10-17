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

 def test_adaptive_weights_fit_training_not_live_model(self):
  with tempfile.TemporaryDirectory() as d:
   p=Path(d)/"history.sqlite3";c=sqlite3.connect(p)
   c.execute("CREATE TABLE candidate_features(run_at TEXT,pair TEXT,move_15m_pct REAL,volume_accel REAL,base_score REAL)")
   c.execute("CREATE TABLE outcomes(run_at TEXT,pair TEXT,horizon_hours INTEGER,return_pct REAL)")
   for t in range(30):
    for j in range(8):
     # Baseline ranks a loser highest; intrahour momentum identifies the winner.
     c.execute("INSERT INTO candidate_features VALUES (?,?,?,?,?)",(f"2026-10-{t+1:02d}",f"C{j}",4.0 if j==7 else 0.0,1.0,80.0 if j==0 else 60.0))
     c.execute("INSERT INTO outcomes VALUES (?,?,?,?)",(f"2026-10-{t+1:02d}",f"C{j}",1,8.0 if j==7 else -3.0))
   c.commit();c.close()
   r=evaluate(p)
   self.assertEqual(r["status"],"ADAPTIVE_SHADOW_EVALUATED")
   self.assertGreater(r["learned_weights"]["momentum"],0)
   self.assertGreater(r["holdout"]["delta_pct"],0)
   self.assertFalse(r["promotion_eligible"])
   self.assertFalse(r["live_weights_modified"])

 def test_unselected_breakout_audit(self):
  import datetime as dt
  with tempfile.TemporaryDirectory() as d:
   p=Path(d)/"history.sqlite3";c=sqlite3.connect(p)
   c.execute("CREATE TABLE candidate_features(run_at TEXT,pair TEXT,move_15m_pct REAL,volume_accel REAL,base_score REAL)")
   c.execute("CREATE TABLE outcomes(run_at TEXT,pair TEXT,horizon_hours INTEGER,return_pct REAL)")
   c.execute("CREATE TABLE snapshots(run_at TEXT,pair TEXT)")
   c.execute("CREATE TABLE market_observations(run_at TEXT,pair TEXT,price REAL)")
   t=dt.datetime.now(dt.timezone.utc)-dt.timedelta(minutes=35)
   c.execute("INSERT INTO market_observations VALUES (?,?,?)",(t.isoformat(),"MISS",1.0))
   c.execute("INSERT INTO market_observations VALUES (?,?,?)",((t+dt.timedelta(minutes=15)).isoformat(),"MISS",1.2))
   c.commit();c.close()
   r=evaluate(p)
   self.assertEqual(r["missed_breakout_examples"][0]["pair"],"MISS")
   self.assertFalse(r["misses_included_in_weight_training"])
