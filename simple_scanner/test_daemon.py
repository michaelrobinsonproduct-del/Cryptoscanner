"""Offline acceptance tests for the single-writer daemon (no live network)."""
import datetime as dt
import os
import tempfile
import unittest
from unittest.mock import patch
from simple_scanner.daemon import quarter_hour_bucket, due_manual, serve

UTC = dt.timezone.utc
class StopLoop(Exception): pass

class DaemonTests(unittest.TestCase):
    def test_quarter_hour_boundaries(self):
        a=dt.datetime(2026,10,17,20,14,59,tzinfo=UTC)
        b=dt.datetime(2026,10,17,20,15,0,tzinfo=UTC)
        self.assertEqual(quarter_hour_bucket(b),quarter_hour_bucket(a)+1)

    def test_missing_token_never_fetches(self):
        with tempfile.TemporaryDirectory() as folder, patch.dict(os.environ,{},clear=True), \
             patch("simple_scanner.daemon.fetch_requests") as fetch:
            self.assertFalse(due_manual(folder,dt.datetime.now(UTC)))
            fetch.assert_not_called()

    def test_pending_request_detected(self):
        now=dt.datetime.now(UTC)
        with tempfile.TemporaryDirectory() as folder, \
             patch.dict(os.environ,{"SIMPLE_SCANNER_GITHUB_TOKEN":"synthetic"},clear=True), \
             patch("simple_scanner.daemon.fetch_requests",return_value=[{"issue_number":42,"created_at":now.isoformat()}]):
            self.assertTrue(due_manual(folder,now))

    def test_corrupt_ledger_blocks_request(self):
        now=dt.datetime.now(UTC)
        with tempfile.TemporaryDirectory() as folder, \
             patch.dict(os.environ,{"SIMPLE_SCANNER_GITHUB_TOKEN":"synthetic"},clear=True), \
             patch("simple_scanner.daemon.fetch_requests") as fetch:
            from pathlib import Path
            Path(folder,"manual_request_ledger.json").write_text("{broken")
            self.assertFalse(due_manual(folder,now))
            fetch.assert_not_called()

    def test_scheduled_and_manual_run_in_one_process(self):
        base=dt.datetime(2026,10,17,20,14,59,tzinfo=UTC)
        moments=iter([base,base,base+dt.timedelta(seconds=1),base+dt.timedelta(seconds=2)])
        calls=[]
        def clock(): return next(moments)
        def sleep(_): 
            if len(calls)>=2: raise StopLoop()
        def run(origin):
            calls.append(origin)
            return 0
        with tempfile.TemporaryDirectory() as folder, \
             patch.dict(os.environ,{"SIMPLE_SCANNER_DATA_DIR":folder},clear=True), \
             patch("simple_scanner.daemon.signal.signal"), \
             patch("simple_scanner.daemon.due_manual",side_effect=[True,False]):
            with self.assertRaises(StopLoop):
                serve(sleep=sleep,clock=clock,run=run)
        self.assertEqual(calls,["manual","cron"])

    def test_no_unrequested_manual_scan(self):
        base=dt.datetime(2026,10,17,20,14,0,tzinfo=UTC)
        moments=iter([base,base,base])
        calls=[]
        with tempfile.TemporaryDirectory() as folder, \
             patch.dict(os.environ,{"SIMPLE_SCANNER_DATA_DIR":folder},clear=True), \
             patch("simple_scanner.daemon.signal.signal"), \
             patch("simple_scanner.daemon.due_manual",return_value=False):
            def stop_after_one(_): raise StopLoop()
            with self.assertRaises(StopLoop):
                serve(sleep=stop_after_one,clock=lambda:next(moments),run=lambda x:calls.append(x))
        self.assertEqual(calls,[])

if __name__=="__main__":
    unittest.main()
