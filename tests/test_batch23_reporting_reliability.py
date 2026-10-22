"""Batch 23 offline reporting, locking and fail-closed delivery contracts."""
import contextlib
import datetime as dt
import io
import json
import os
import subprocess
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch
from simple_scanner import execute_once

class ReportingReliabilityTests(unittest.TestCase):
    def run_case(self, origin='manual', overrides=None, pending=False, delivery=None, busy=False):
        with tempfile.TemporaryDirectory() as root:
            stamp=dt.datetime.now(dt.timezone.utc).isoformat()
            summary={'started_at':stamp,'completed_at':stamp,'status':'RESEARCH_ONLY','buy_approved':False}
            Path(root,'latest.json').write_text(json.dumps(summary))
            outputs={
                'simple_scanner.scan':'SCAN_SUMMARY '+json.dumps(summary)+'\nWATCH_SUMMARY '+json.dumps([{'symbol':'BTC/USD','score':50}]),
                'simple_scanner.history':'HISTORY_PERSISTED '+json.dumps({'history_db_integrity':'ok','buy_approved':False,'model_updates':'DISABLED_PENDING_UNBIASED_FORWARD_VALIDATION'}),
                'simple_scanner.shadow_learning':'SHADOW_LEARNING '+json.dumps({'mode':'SHADOW_ONLY','live_weights_modified':False}),
                'simple_scanner.dex_guard':'DEX_SUMMARY '+json.dumps({'observed_at':stamp,'errors':0,'buy_approved':False}),
            }
            outputs.update(overrides or {})
            calls=[]
            def invoke(args,**kwargs):
                calls.append(args[-1])
                return subprocess.CompletedProcess(args,0,outputs[args[-1]],'')
            requests=[{'issue_number':91,'created_at':stamp}] if pending else []
            buf=io.StringIO()
            with patch.dict(os.environ,{'SIMPLE_SCANNER_DATA_DIR':root,'SIMPLE_SCANNER_GITHUB_TOKEN':'fixture'} if pending else {'SIMPLE_SCANNER_DATA_DIR':root},clear=True),patch.object(execute_once.subprocess,'run',side_effect=invoke),patch('simple_scanner.manual_requests.fetch_requests',return_value=requests),patch('simple_scanner.manual_requests.publish_results',return_value=delivery if delivery is not None else requests),contextlib.redirect_stdout(buf):
                if busy:
                    with patch.object(execute_once.fcntl,'flock',side_effect=BlockingIOError):
                        status=execute_once.execute(origin)
                else:
                    status=execute_once.execute(origin)
                ledger=Path(root,'manual_request_ledger.json')
                state=json.loads(ledger.read_text()) if ledger.exists() else None
            return status,buf.getvalue(),calls,state

    def test_manual_and_cron_same_verified_reporting_and_order(self):
        for origin in ('manual','cron'):
            status,log,calls,_=self.run_case(origin)
            self.assertEqual(status,0,log)
            self.assertEqual(calls,list(execute_once.MODULES))
            record=json.loads(next(x.split(' ',1)[1] for x in log.splitlines() if x.startswith('SCAN_EXECUTION_VERIFIED ')))
            self.assertEqual(record['origin'],origin)
            self.assertEqual(record['status'],'VERIFIED')
            self.assertFalse(record['buy_approved'])

    def test_concurrent_scan_returns_busy_without_subprocess(self):
        status,log,calls,_=self.run_case(busy=True)
        self.assertEqual(status,75)
        self.assertEqual(calls,[])
        self.assertIn('SCAN_BUSY',log)

    def test_invalid_history_rejected_before_delivery(self):
        status,log,_,_=self.run_case(overrides={'simple_scanner.history':'HISTORY_PERSISTED '+json.dumps({'history_db_integrity':'failed','buy_approved':False,'model_updates':'DISABLED_PENDING_UNBIASED_FORWARD_VALIDATION'})},pending=True)
        self.assertNotEqual(status,0)
        self.assertIn('SCAN_HISTORY_SAFETY_FAILED',log)
        self.assertNotIn('MANUAL_REQUESTS_SATISFIED',log)

    def test_dex_degraded_does_not_deliver_pending_request(self):
        status,log,_,state=self.run_case(overrides={'simple_scanner.dex_guard':'DEX_STALE_CACHE {}'},pending=True)
        self.assertEqual(status,0)
        self.assertIn('"status": "PARTIAL"',log)
        self.assertNotIn('MANUAL_REQUESTS_SATISFIED',log)
        self.assertIsNone(state)

    def test_failed_delivery_is_explicitly_blocked(self):
        status,log,_,state=self.run_case(pending=True,delivery=[])
        self.assertEqual(status,0)
        self.assertIn('MANUAL_RESULT_DELIVERY_PENDING',log)
        self.assertIn('"delivery_status": "BLOCKED"',log)
        self.assertIsNotNone(state)

if __name__=='__main__':
    unittest.main()
