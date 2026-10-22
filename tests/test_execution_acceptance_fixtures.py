"""Fixture-based shared execution and delivery acceptance, never live endpoints."""
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
from simple_scanner.manual_requests import acknowledge_requests, read_ledger, sanitize_watch

class AcceptanceTests(unittest.TestCase):
    def fixture(self, root):
        now=dt.datetime.now(dt.timezone.utc)
        stamp=now.isoformat()
        summary={'started_at':stamp,'completed_at':stamp,'status':'RESEARCH_ONLY','buy_approved':False}
        (Path(root)/'latest.json').write_text(json.dumps(summary))
        outputs={
            'simple_scanner.scan':'SCAN_SUMMARY '+json.dumps(summary)+'\nWATCH_SUMMARY '+json.dumps([{'symbol':'BTC/USD','score':55,'risk':'HIGH'}]),
            'simple_scanner.history':'HISTORY_PERSISTED '+json.dumps({'history_db_integrity':'ok','buy_approved':False,'model_updates':'DISABLED_PENDING_UNBIASED_FORWARD_VALIDATION'}),
            'simple_scanner.shadow_learning':'SHADOW_LEARNING '+json.dumps({'mode':'SHADOW_ONLY','live_weights_modified':False}),
            'simple_scanner.dex_guard':'DEX_SUMMARY '+json.dumps({'observed_at':stamp,'errors':0,'buy_approved':False}),
        }
        return outputs

    def run_fixture(self, origin, broken=None, manual=False):
        with tempfile.TemporaryDirectory() as root:
            outputs=self.fixture(root)
            if broken:
                outputs.update(broken)
            def invoke(args, **kwargs):
                module=args[-1]
                if module == 'simple_scanner.shadow_learning' and broken and module in broken:
                    return subprocess.CompletedProcess(args,1,outputs[module],'shadow failure')
                return subprocess.CompletedProcess(args,0,outputs[module],'')
            buf=io.StringIO()
            env={'SIMPLE_SCANNER_DATA_DIR':root}
            if manual: env['SIMPLE_SCANNER_GITHUB_TOKEN']='fixture-only'
            requests=[{'issue_number':42,'created_at':dt.datetime.now(dt.timezone.utc).isoformat()}]
            with patch.dict(os.environ,env,clear=True), patch.object(execute_once.subprocess,'run',side_effect=invoke), patch('simple_scanner.manual_requests.fetch_requests',return_value=requests), patch('simple_scanner.manual_requests.publish_results',return_value=requests), contextlib.redirect_stdout(buf):
                status=execute_once.execute(origin)
            return status,buf.getvalue()

    def test_manual_and_cron_verified_same_pipeline(self):
        for origin in ('manual','cron'):
            status,output=self.run_fixture(origin)
            self.assertEqual(status,0,output)
            self.assertIn('SCAN_EXECUTION_VERIFIED',output)
            self.assertIn('"status": "VERIFIED"',output)

    def test_manual_acknowledgement_after_delivery(self):
        status,output=self.run_fixture('manual',manual=True)
        self.assertEqual(status,0,output)
        self.assertIn('MANUAL_REQUESTS_SATISFIED',output)
        self.assertIn('"delivery_status": "DELIVERED"',output)

    def test_shadow_failure_degrades_without_approval(self):
        status,output=self.run_fixture('cron',broken={'simple_scanner.shadow_learning':''})
        self.assertEqual(status,0,output)
        self.assertIn('SHADOW_LEARNING_PARTIAL_FAILURE',output)
        self.assertIn('"status": "PARTIAL"',output)

    def test_dex_failure_degrades_without_approval(self):
        status,output=self.run_fixture('cron',broken={'simple_scanner.dex_guard':'DEX_CIRCUIT_OPEN {}'})
        self.assertEqual(status,0,output)
        self.assertIn('"status": "PARTIAL"',output)

    def test_missing_scan_output_fails_closed(self):
        status,output=self.run_fixture('cron',broken={'simple_scanner.scan':'WATCH_SUMMARY []'})
        self.assertNotEqual(status,0)
        self.assertIn('SCAN_INCOMPLETE',output)

    def test_corrupt_ledger_cannot_acknowledge(self):
        with tempfile.TemporaryDirectory() as root:
            path=Path(root)/'manual_request_ledger.json'
            path.write_text('{corrupt')
            self.assertFalse(read_ledger(root)['ledger_valid'])
            with self.assertRaises(RuntimeError):
                acknowledge_requests(root,[{'issue_number':42}],'run')

    def test_delivery_sanitizes_untrusted_values(self):
        watch=sanitize_watch([{'symbol':'BTC','score':float('nan'),'risk':'H'*100,'secret':'should-not-publish'}])
        self.assertNotIn('score',watch[0])
        self.assertNotIn('secret',watch[0])
        self.assertEqual(len(watch[0]['risk']),32)

if __name__=='__main__':
    unittest.main()
