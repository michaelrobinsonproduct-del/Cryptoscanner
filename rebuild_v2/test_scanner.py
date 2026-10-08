import unittest
import os
import tempfile
import pathlib
import history
import datetime as dt
from scanner import rank, confirm_watch, confirm_twice
import time

class ScannerTests(unittest.TestCase):
    def test_quote(self):
        t={"c":["10"],"o":"10","v":["0","10000"],"t":[0,500],"b":["9.99"],"a":["10.01"]}
        self.assertGreater(rank(t)["score"],0)
    def test_crossed(self):
        t={"c":["10"],"o":"10","v":["0","10000"],"t":[0,500],"b":["10.02"],"a":["10.01"]}
        with self.assertRaises(ValueError): rank(t)
    def test_zero_open(self):
        t={"c":["10"],"o":"0","v":["0","10000"],"t":[0,500],"b":["9.99"],"a":["10.01"]}
        with self.assertRaises(ValueError): rank(t)
    def test_fresh_trade(self):
        def fake(endpoint):
            if endpoint.startswith("Depth?"):
                return {"XXBTZUSD":{"bids":[["100","1","1"]],"asks":[["100.1","1","1"]]}}
            return {"XXBTZUSD":[["100","1",time.time()-5,"b","l",""]]}
        self.assertFalse(confirm_watch("XXBTZUSD",{},fake)["entry_approved"])
        self.assertFalse(confirm_twice("XXBTZUSD",{},fake,lambda _:time.sleep(.01))["entry_approved"])
    def test_stale_trade(self):
        def fake(endpoint):
            if endpoint.startswith("Depth?"):
                return {"XXBTZUSD":{"bids":[["100","1","1"]],"asks":[["100.1","1","1"]]}}
            return {"XXBTZUSD":[["100","1",time.time()-500,"b","l",""]]}
        with self.assertRaises(ValueError): confirm_watch("XXBTZUSD",{},fake)
    def test_idempotent_history(self):
        with tempfile.TemporaryDirectory() as folder:
            original=history.DB
            history.DB=pathlib.Path(folder)/"history.db"
            try:
                sample={"started_at":"2026-10-08T00:00:00+00:00","completed_at":"2026-10-08T00:00:01+00:00","health":"COMPLETE","watch":[{"pair":"ABCUSD","score":70,"status":"WATCH"}]}
                history.store_run(sample)
                history.store_run(sample)
                with history.connect() as db:
                    self.assertEqual(db.execute("SELECT count(*) FROM runs").fetchone()[0],1)
                    self.assertEqual(db.execute("SELECT count(*) FROM observations").fetchone()[0],1)
            finally: history.DB=original
    def test_prospective_outcome_uses_bid(self):
        with tempfile.TemporaryDirectory() as folder:
            original=history.DB
            history.DB=pathlib.Path(folder)/"history.db"
            try:
                t0=dt.datetime.now(dt.timezone.utc)-dt.timedelta(hours=1,minutes=5)
                run={"started_at":t0.isoformat(),"completed_at":t0.isoformat(),"health":"COMPLETE","watch":[{"pair":"ABCUSD","price":100,"score":80,"status":"WATCH"}]}
                history.store_run(run)
                current={"completed_at":dt.datetime.now(dt.timezone.utc).isoformat(),"market_quotes":[{"pair":"ABCUSD","bid":110}]}
                history.evaluate_outcomes(current)
                with history.connect() as db:
                    row=db.execute("SELECT horizon_hours,return_pct FROM outcomes").fetchone()
                    self.assertEqual(row[0],1)
                    self.assertAlmostEqual(row[1],10)
            finally:
                history.DB=original

if __name__=="__main__": unittest.main()
