import unittest
import os
import tempfile
import pathlib
import history
import datetime as dt
from scanner import rank, confirm_watch, confirm_twice, eligible_crypto_pair, eligible_watch
import time

class ScannerTests(unittest.TestCase):
    def test_exclude_fiat_and_stablecoins(self):
        for base in ("ZEUR", "ZGBP", "USD", "USDT", "USDC", "DAI", "PYUSD"):
            self.assertFalse(eligible_crypto_pair({"base":base}))
        for base in ("XXBT", "XETH", "SOL", "AKE", "HYPE"):
            self.assertTrue(eligible_crypto_pair({"base":base}))
    def test_positive_momentum_gate(self):
        self.assertFalse(eligible_watch({"score":99,"move24_pct":-0.01}))
        self.assertFalse(eligible_watch({"score":99,"move24_pct":0}))
        self.assertFalse(eligible_watch({"score":59,"move24_pct":2}))
        self.assertTrue(eligible_watch({"score":60,"move24_pct":0.01}))
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
    def test_reliability_scorecard_requires_full_window(self):
        with tempfile.TemporaryDirectory() as folder:
            original=history.DB
            history.DB=pathlib.Path(folder)/"history.db"
            try:
                now=dt.datetime.now(dt.timezone.utc)
                run={"started_at":now.isoformat(),"completed_at":now.isoformat(),"health":"COMPLETE","watch":[]}
                history.store_run(run)
                score=history.reliability_scorecard(now=now)
                self.assertEqual(score["24h"]["status"],"INSUFFICIENT_HISTORY")
                self.assertIsNone(score["24h"]["coverage_pct"])
                self.assertEqual(score["168h"]["status"],"INSUFFICIENT_HISTORY")
            finally:
                history.DB=original
    def test_history_diagnostics_before_and_after_outcome(self):
        with tempfile.TemporaryDirectory() as folder:
            original=history.DB
            history.DB=pathlib.Path(folder)/"history.db"
            try:
                first=history.history_diagnostics()
                self.assertEqual(first["runs"],0)
                self.assertFalse(first["history_available"])
                t0=dt.datetime.now(dt.timezone.utc)-dt.timedelta(hours=1,minutes=5)
                run={"started_at":t0.isoformat(),"completed_at":t0.isoformat(),"health":"COMPLETE","watch":[{"pair":"ABCUSD","price":100,"score":80,"status":"WATCH"}]}
                history.store_run(run)
                before=history.history_diagnostics()
                self.assertEqual(before["observations"],1)
                self.assertEqual(before["outcomes"],0)
                history.evaluate_outcomes({"completed_at":dt.datetime.now(dt.timezone.utc).isoformat(),"market_quotes":[{"pair":"ABCUSD","bid":110}]})
                after=history.history_diagnostics()
                self.assertEqual(after["outcomes"],1)
                self.assertEqual(after["unlabeled_observations"],0)
                self.assertEqual(after["learning_status"],"OUTCOMES_AVAILABLE")
            finally:
                history.DB=original
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
