import os
import sqlite3
import tempfile
import unittest
from research.export_candidate_cohorts import export_candidate_cohorts
from research.equal_budget_forward import compare

RUN="2026-10-01T00:00:00+00:00"

class PersistedCohortTests(unittest.TestCase):
    def setUp(self):
        self.temp=tempfile.TemporaryDirectory()
        self.path=os.path.join(self.temp.name,"history.sqlite3")
        con=sqlite3.connect(self.path)
        con.executescript("""
        CREATE TABLE candidate_features(run_at TEXT,pair TEXT,base_score REAL,early_signal_score REAL);
        CREATE TABLE snapshots(run_at TEXT,pair TEXT,price REAL);
        CREATE TABLE market_signals(run_at TEXT,pair TEXT,spread_bps REAL,notional_24h_usd REAL);
        CREATE TABLE outcomes(run_at TEXT,pair TEXT,horizon_hours INTEGER,evaluated_at TEXT,return_pct REAL);
        """)
        for pair,base,challenger,ret in (("AAA",10,1,25),("BBB",1,10,-2),("NOLIQ",5,5,30)):
            con.execute("INSERT INTO candidate_features VALUES(?,?,?,?)",(RUN,pair,base,challenger))
            con.execute("INSERT INTO snapshots VALUES(?,?,?)",(RUN,pair,1))
            if pair!="NOLIQ":
                con.execute("INSERT INTO market_signals VALUES(?,?,?,?)",(RUN,pair,10,200000))
            con.execute("INSERT INTO outcomes VALUES(?,?,?,?,?)",(RUN,pair,1,"2026-10-01T01:05:00+00:00",ret))
        con.commit()
        con.close()
    def tearDown(self):
        self.temp.cleanup()
    def test_real_schema_export_and_comparison(self):
        rows=export_candidate_cohorts(self.path)
        self.assertEqual({r["pair"] for r in rows},{"AAA","BBB"})
        result=compare(rows,budget=1)
        self.assertEqual(result["horizons"][1]["baseline"]["hits20"],1)
        self.assertEqual(result["horizons"][1]["challenger"]["false_positives"],1)
        self.assertEqual(result["horizons"][24]["baseline"]["matured"],0)
        self.assertFalse(result["promotion_eligible"])
    def test_missing_database_does_not_create_it(self):
        absent=os.path.join(self.temp.name,"absent.sqlite3")
        with self.assertRaises(sqlite3.OperationalError):
            export_candidate_cohorts(absent)
        self.assertFalse(os.path.exists(absent))
    def test_readonly_source(self):
        con=sqlite3.connect(self.path)
        before=con.execute("SELECT COUNT(*) FROM snapshots").fetchone()[0]
        con.close()
        export_candidate_cohorts(self.path)
        con=sqlite3.connect(self.path)
        after=con.execute("SELECT COUNT(*) FROM snapshots").fetchone()[0]
        con.close()
        self.assertEqual(before,after)

if __name__=="__main__":
    unittest.main()
