import sqlite3
import unittest
from simple_scanner.offline_replay import cohort_split, replay_feasibility

class OfflineReplayTests(unittest.TestCase):
    def test_cohorts_do_not_leak_and_embargo(self):
        rows=[(f'2026-10-{day:02d}', pair, day) for day in range(1,11) for pair in ('BTC','ETH','SOL')]
        result=cohort_split(list(reversed(rows)))
        train={r[0] for r in result['train']}
        holdout={r[0] for r in result['holdout']}
        self.assertTrue(max(train)<min(holdout))
        self.assertFalse(train & holdout)
        self.assertEqual(len(result['train']) % 3,0)
        self.assertEqual(len(result['holdout']) % 3,0)
        self.assertEqual(len(result['embargoed_timestamps']),1)
        self.assertFalse(result['promotion_eligible'])

    def test_full_archive_counts_not_last_6000_rows(self):
        with sqlite3.connect(':memory:') as db:
            db.execute('CREATE TABLE market_signals(run_at TEXT,pair TEXT)')
            db.execute('CREATE TABLE market_observations(run_at TEXT,pair TEXT,price REAL)')
            db.executemany('INSERT INTO market_signals VALUES(?,?)',
                           [(str(i//100),str(i)) for i in range(6101)])
            db.executemany('INSERT INTO market_observations VALUES(?,?,?)',
                           [(str(i//100),str(i),1.) for i in range(6101)])
            report=replay_feasibility(db)
        self.assertEqual(report['signal_rows'],6101)
        self.assertEqual(report['signal_timestamps'],62)
        self.assertFalse(report['full_replay_verified'])
        self.assertFalse(report['promotion_eligible'])

    def test_missing_archive_fails_closed(self):
        with sqlite3.connect(':memory:') as db:
            self.assertEqual(replay_feasibility(db)['status'],'MISSING_TABLES')
        with self.assertRaises(ValueError):
            cohort_split([('t1','BTC')])

if __name__=='__main__':
    unittest.main()
