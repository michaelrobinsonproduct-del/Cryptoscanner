"""Offline-only release acceptance for manual request delivery and recovery."""
import datetime as dt
import io
import json
import os
import tempfile
import unittest
import urllib.error
from pathlib import Path
from unittest.mock import patch
from simple_scanner.manual_requests import (
    acknowledge_requests, parse_requests, plan_requests, publish_results, read_ledger
)

class FakeResponse:
    status=201
    def __enter__(self): return self
    def __exit__(self,*args): return False

class DeliveryRecoveryTests(unittest.TestCase):
    def setUp(self):
        self.now=dt.datetime.now(dt.timezone.utc)
        self.issue={'number':81,'title':'MANUAL_SCAN_REQUEST','state':'open',
                    'created_at':self.now.isoformat(),
                    'labels':[{'name':'manual-scan-request'}]}
        self.requests=[{'issue_number':81,'created_at':self.now.isoformat()}]
        self.run={'completed_at':self.now.isoformat()}

    def test_request_filters_and_duplicate_prevention(self):
        invalid=dict(self.issue,number=82,labels=[])
        pull=dict(self.issue,number=83,pull_request={})
        found=parse_requests([self.issue,self.issue,invalid,pull],now=self.now)
        self.assertEqual(found,self.requests)
        self.assertEqual(plan_requests(found,{'completed_issue_numbers':[81]},self.now),[])
        self.assertEqual(plan_requests(found,{'completed_issue_numbers':[]},self.now),found)

    def test_successful_receipt_is_bounded_research_only(self):
        captured=[]
        def send(request,timeout):
            payload=json.loads(request.data.decode())
            receipt=json.loads(payload['body'].split('\\x60\\x60\\x60json\\n',1)[1].split('\\n\\x60\\x60\\x60',1)[0])
            captured.append(receipt)
            return FakeResponse()
        with patch.dict(os.environ,{'SIMPLE_SCANNER_GITHUB_TOKEN':'fixture'},clear=True),patch('simple_scanner.manual_requests.urllib.request.urlopen',side_effect=send):
            delivered=publish_results(self.requests,self.run,[{'symbol':'BTC','score':50,'secret':'never'}],'FRESH',origin='manual')
        self.assertEqual(delivered,self.requests)
        self.assertEqual(captured[0]['status'],'VERIFIED')
        self.assertFalse(captured[0]['buy_approved'])
        self.assertEqual(captured[0]['learning'],'SHADOW_ONLY')
        self.assertNotIn('secret',captured[0]['watch'][0])

    def test_permission_failure_does_not_mark_delivered(self):
        error=urllib.error.HTTPError('https://example.invalid',403,'forbidden',{},io.BytesIO(b'{"message":"Forbidden"}'))
        with patch.dict(os.environ,{'SIMPLE_SCANNER_GITHUB_TOKEN':'fixture'},clear=True),patch('simple_scanner.manual_requests.urllib.request.urlopen',side_effect=error):
            self.assertEqual(publish_results(self.requests,self.run,[],'FRESH'),[])

    def test_acknowledgement_recovery_is_idempotent(self):
        with tempfile.TemporaryDirectory() as root:
            acknowledge_requests(root,self.requests,'run-1')
            acknowledge_requests(root,self.requests,'run-1')
            self.assertEqual(read_ledger(root)['completed_issue_numbers'],[81])
            self.assertEqual(plan_requests(self.requests,read_ledger(root),self.now),[])
            self.assertEqual(list(Path(root).glob('.manual_ledger_*')),[])

    def test_stale_request_rejected(self):
        old=dict(self.issue,created_at=(self.now-dt.timedelta(minutes=61)).isoformat())
        self.assertEqual(parse_requests([old],now=self.now),[])

if __name__=='__main__':
    unittest.main()
