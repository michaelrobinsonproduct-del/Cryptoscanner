import os
import sqlite3
import tempfile
import unittest
from research.export_candidate_cohorts import export_candidate_cohorts
from research.equal_budget_forward import compare

RUN="2026-10-01T00:00:00+00:00"
LATE="2026-10-01T00:01:00+00:00"
DUE="2026-10-01T01:05:00+00:00"

class ProvenanceFixtureTests(unittest.TestCase):
    def setUp(self):
        self.temp=tempfile.TemporaryDirectory()
        self.db=os.path.join(self.temp.name,"fixture.sqlite")
        with sqlite3.connect(self.db) as con:
            con.executescript("""
            CREATE TABLE candidate_features(run_at TEXT,pair TEXT,base_score REAL,early_signal_score REAL,features_observed_at TEXT);
            CREATE TABLE snapshots(run_at TEXT,pair TEXT,price REAL,observed_at TEXT);
            CREATE TABLE market_signals(run_at TEXT,pair TEXT,spread_bps REAL,notional_24h_usd REAL,observed_at TEXT);
            CREATE TABLE outcomes(run_at TEXT,pair TEXT,horizon_hours INTEGER,evaluated_at TEXT,return_pct REAL);
            """)
            for pair,base,challenger,ret in (("AAA",10,1,25),("BBB",1,10,-2)):
                con.execute("INSERT INTO candidate_features VALUES(?,?,?,?,?)",(RUN,pair,base,challenger,RUN))
                con.execute("INSERT INTO snapshots VALUES(?,?,?,?)",(RUN,pair,1,RUN))
                con.execute("INSERT INTO market_signals VALUES(?,?,?,?,?)",(RUN,pair,10,200000,RUN))
                con.execute("INSERT INTO outcomes VALUES(?,?,?,?,?)",(RUN,pair,1,DUE,ret))
    def tearDown(self):
        self.temp.cleanup()
    def test_valid_timestamped_cohort_and_immature_horizons(self):
        rows=export_candidate_cohorts(self.db)
        self.assertEqual(len(rows),2)
        result=compare(rows,budget=1)
        self.assertEqual(result["horizons"][1]["baseline"]["hits20"],1)
        self.assertEqual(result["horizons"][1]["challenger"]["false_positives"],1)
        self.assertEqual(result["horizons"][24]["baseline"]["matured"],0)
    def test_duplicate_outcome_fails_closed(self):
        with sqlite3.connect(self.db) as con:
            con.execute("INSERT INTO outcomes VALUES(?,?,?,?,?)",(RUN,"AAA",1,DUE,99))
        with self.assertRaisesRegex(ValueError,"duplicate outcomes"):
            export_candidate_cohorts(self.db)
    def test_future_liquidity_observation_fails_closed(self):
        with sqlite3.connect(self.db) as con:
            con.execute("UPDATE market_signals SET observed_at=? WHERE pair='AAA'",(LATE,))
        with self.assertRaisesRegex(ValueError,"future feature"):
            export_candidate_cohorts(self.db)
    def test_duplicate_features_fails_closed(self):
        with sqlite3.connect(self.db) as con:
            con.execute("INSERT INTO candidate_features VALUES(?,?,?,?,?)",(RUN,"AAA",9,9,RUN))
        with self.assertRaisesRegex(ValueError,"duplicate candidate_features"):
            export_candidate_cohorts(self.db)

if __name__=="__main__":
    unittest.main()
