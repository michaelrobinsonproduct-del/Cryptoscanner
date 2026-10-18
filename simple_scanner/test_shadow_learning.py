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

 def test_market_miss_model_requires_mature_outcomes(self):
  import datetime as dt
  with tempfile.TemporaryDirectory() as d:
   p=Path(d)/"history.sqlite3";c=sqlite3.connect(p)
   c.execute("CREATE TABLE candidate_features(run_at TEXT,pair TEXT,move_15m_pct REAL,volume_accel REAL,base_score REAL)")
   c.execute("CREATE TABLE outcomes(run_at TEXT,pair TEXT,horizon_hours INTEGER,return_pct REAL)")
   c.execute("CREATE TABLE snapshots(run_at TEXT,pair TEXT)")
   c.execute("CREATE TABLE market_observations(run_at TEXT,pair TEXT,price REAL)")
   c.execute("CREATE TABLE market_signals(run_at TEXT,pair TEXT,move24_pct REAL,spread_bps REAL,notional_24h_usd REAL)")
   now=dt.datetime.now(dt.timezone.utc)
   for j in range(5):
    t=(now-dt.timedelta(hours=4,minutes=j)).isoformat()
    c.execute("INSERT INTO market_signals VALUES (?,?,?,?,?)",(t,f"C{j}",.5,20,200000))
    c.execute("INSERT INTO market_observations VALUES (?,?,?)",(t,f"C{j}",1.0))
    c.execute("INSERT INTO market_observations VALUES (?,?,?)",((now-dt.timedelta(hours=3,minutes=j)).isoformat(),f"C{j}",1.2))
   c.commit();c.close()
   r=evaluate(p)
   self.assertEqual(r["market_miss_model"]["samples"],5)
   self.assertEqual(r["market_miss_model"]["breakouts"],5)
   self.assertEqual(r["market_miss_model"]["status"],"INSUFFICIENT_MARKET_OUTCOMES")

 def test_shadow_main_current_scan_evidence_states(self):
  import json,os
  from unittest.mock import patch
  from simple_scanner.shadow_learning import main
  for evidence,expected in (
      ({"status":"VERIFIED"},"INSUFFICIENT_DATA"),
      ({"status":"UNVERIFIED","archive_status":"UNVERIFIED_NOT_RECORDED"},"CURRENT_SCAN_EVIDENCE_UNVERIFIED"),
      ({"status":"UNVERIFIED","sqlite_status":"MISMATCH"},"CURRENT_SCAN_EVIDENCE_UNVERIFIED")):
   with self.subTest(evidence=evidence),tempfile.TemporaryDirectory() as d:
    sqlite3.connect(Path(d)/"history.sqlite3").close()
    baseline={"mode":"SHADOW_ONLY","status":"INSUFFICIENT_DATA",
              "buy_approved":False,"live_weights_modified":False,
              "challenger_promotion_gate":{"status":"BLOCKED"}}
    with patch.dict(os.environ,{"SIMPLE_SCANNER_DATA_DIR":d}),\
         patch("simple_scanner.shadow_learning.evaluate",return_value=baseline),\
         patch("simple_scanner.scan_output.verify_scan_history_evidence",return_value=evidence):
     main()
    saved=json.loads((Path(d)/"shadow_learning.json").read_text())
    self.assertEqual(saved["status"],expected)
    self.assertFalse(saved["buy_approved"])
    self.assertFalse(saved["live_weights_modified"])
    if evidence["status"]!="VERIFIED":
     self.assertFalse(saved["promotion_eligible"])
     self.assertEqual(saved["challenger_promotion_gate"]["status"],"BLOCKED_UNVERIFIED_CURRENT_SCAN")
