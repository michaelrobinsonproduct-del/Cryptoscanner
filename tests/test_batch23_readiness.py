"""Batch 23: read-only fixture readiness and report parity, not production replay."""
import datetime as dt
import json
import sqlite3
import tempfile
import unittest
from pathlib import Path
from simple_scanner.offline_replay import replay_feasibility,cohort_split
from simple_scanner.offline_scoring_comparison import compare_cohorts
from simple_scanner.shadow_learning import score

class ReadinessAcceptance(unittest.TestCase):
    def test_missing_archive_fails_closed(self):
        with sqlite3.connect(':memory:') as db:
            result=replay_feasibility(db)
        self.assertEqual(result['status'],'MISSING_TABLES')
        self.assertFalse(result['promotion_eligible'])

    def test_full_fixture_inventory_does_not_claim_replay(self):
        with sqlite3.connect(':memory:') as db:
            db.execute('CREATE TABLE market_signals (run_at TEXT, pair TEXT)')
            db.execute('CREATE TABLE market_observations (run_at TEXT, pair TEXT)')
            db.executemany('INSERT INTO market_signals VALUES(?,?)',
                           [(f't{i}',pair) for i in range(12) for pair in ('BTC','ETH')])
            db.executemany('INSERT INTO market_observations VALUES(?,?)',
                           [(f't{i}','BTC') for i in range(12)])
            result=replay_feasibility(db)
        self.assertEqual(result['signal_rows'],24)
        self.assertEqual(result['signal_timestamps'],12)
        self.assertEqual(result['observation_rows'],12)
        self.assertFalse(result['full_replay_verified'])
        self.assertFalse(result['promotion_eligible'])

    def test_holdout_equal_budget_and_no_promotion(self):
        rows=[(f't{i}',pair,momentum,volume,base,ret)
              for i in range(12) for pair,momentum,volume,base,ret in
              (('BTC',1.,1.,50.,2.),('ETH',3.,2.,45.,8.))]
        split=cohort_split(rows)
        old=compare_cohorts(split['holdout'],lambda r:score(r,0,0))
        challenger=compare_cohorts(split['holdout'],lambda r:score(r,3,4))
        self.assertEqual(old['delta_pct'],0)
        self.assertEqual(challenger['selection_budget_per_cohort'],1)
        self.assertFalse(challenger['production_scoring_parity_verified'])
        self.assertFalse(challenger['promotion_eligible'])
        self.assertTrue(all(p['timestamp'] not in split['embargoed_timestamps']
                            for p in challenger['picks']))

    def test_manual_and_scheduled_report_contract(self):
        from simple_scanner.execute_once import MODULES,REQUIRED
        self.assertEqual(MODULES[0],'simple_scanner.scan')
        self.assertIn('WATCH_SUMMARY',REQUIRED)
        self.assertIn('HISTORY_PERSISTED',REQUIRED)
        self.assertNotIn('simple_scanner.offline_scoring_comparison',MODULES)

if __name__=='__main__':
    unittest.main()
