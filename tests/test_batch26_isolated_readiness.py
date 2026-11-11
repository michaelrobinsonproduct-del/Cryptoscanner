"""Batch 26 isolated cross-gate reliability checks, no production endpoints."""
import json
import sqlite3
import tempfile
import unittest
from pathlib import Path
from simple_scanner import fixture_delivery_outbox as outbox
from simple_scanner import fixture_receipt_reconciliation as recon
from simple_scanner.offline_replay import replay_feasibility,cohort_split
from simple_scanner.offline_scoring_comparison import compare_cohorts
from simple_scanner.shadow_learning import score
from simple_scanner.execute_once import MODULES,REQUIRED

R={"status":"VERIFIED","buy_approved":False,"watch":[{"symbol":"BTC/USD","risk":"HIGH"}]}

class Batch26Safety(unittest.TestCase):
    def test_manual_and_cron_share_one_execution_contract(self):
        self.assertEqual(MODULES,("simple_scanner.scan","simple_scanner.history","simple_scanner.shadow_learning","simple_scanner.dex_guard"))
        self.assertEqual(REQUIRED,("SCAN_SUMMARY","WATCH_SUMMARY","HISTORY_PERSISTED"))

    def test_outbox_timeout_restart_and_reconciliation_without_new_scan(self):
        with tempfile.TemporaryDirectory() as root:
            first=outbox.stage(root,22,"run-22",R)
            self.assertEqual(recon.reconcile(root,22,[]),"UNRESOLVED_NO_REPOST")
            self.assertEqual(outbox.stage(root,22,"run-22",R),first)
            marker=recon.marker(22,"run-22",first["sha256"])
            self.assertEqual(recon.reconcile(root,22,[{"id":400,"body":marker}]),"DELIVERED")
            self.assertEqual(outbox.pending(root),[])

    def test_outbox_invalid_file_fails_closed_without_history_mutation(self):
        with tempfile.TemporaryDirectory() as root:
            db=Path(root,"history.sqlite")
            with sqlite3.connect(db) as con:
                con.execute("CREATE TABLE market_signals (run_at TEXT)")
                con.execute("INSERT INTO market_signals VALUES ('t0')")
            before=db.read_bytes()
            Path(root,outbox.FILENAME).write_text('{"entries":null}')
            with self.assertRaises(RuntimeError):
                outbox.pending(root)
            self.assertEqual(db.read_bytes(),before)

    def test_history_missing_tables_cannot_be_called_replay(self):
        with sqlite3.connect(":memory:") as con:
            con.execute("CREATE TABLE market_signals (run_at TEXT)")
            result=replay_feasibility(con)
        self.assertEqual(result["status"],"MISSING_TABLES")
        self.assertFalse(result["promotion_eligible"])

    def test_synthetic_scoring_cannot_approve_production(self):
        rows=[(f"t{i}",pair,m,v,b,r) for i in range(12)
              for pair,m,v,b,r in (("BTC",1.,1.,50.,2.),("ETH",3.,2.,45.,8.))]
        split=cohort_split(rows)
        result=compare_cohorts(split["holdout"],lambda row:score(row,3,4))
        self.assertFalse(result["promotion_eligible"])
        self.assertFalse(result["production_scoring_parity_verified"])
        self.assertEqual(result["selection_budget_per_cohort"],1)

if __name__=="__main__":
    unittest.main()
