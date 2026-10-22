"""Offline failure/recovery contracts for Kraken and DEX; never call live APIs."""
import datetime as dt
import io
import json
import tempfile
import unittest
from contextlib import redirect_stdout
from pathlib import Path
from unittest.mock import patch
from simple_scanner import dex, dex_guard, scan

class SourceRecoveryAcceptance(unittest.TestCase):
    def test_kraken_transient_failure_recovers_without_live_network(self):
        calls=[]
        def fake_open(req, timeout):
            calls.append(req.full_url)
            if len(calls)<3: raise TimeoutError('fixture timeout')
            class Response:
                def __enter__(self): return self
                def __exit__(self,*args): return False
                def read(self,*args): return b'{"error":[],"result":{"XXBTZUSD":{"status":"online"}}}'
            return Response()
        with patch.object(scan.urllib.request,'urlopen',side_effect=fake_open),patch.object(scan.time,'sleep') as wait:
            result=scan.get('AssetPairs')
        self.assertIn('XXBTZUSD',result)
        self.assertEqual(len(calls),3)
        self.assertEqual(wait.call_count,2)

    def test_kraken_exhausted_retries_fail_closed(self):
        with patch.object(scan.urllib.request,'urlopen',side_effect=TimeoutError('offline')),patch.object(scan.time,'sleep'):
            with self.assertRaises(TimeoutError):
                scan.get('AssetPairs')

    def test_dex_stale_cache_cannot_be_approved_on_outage(self):
        with tempfile.TemporaryDirectory() as root,patch.dict('os.environ',{'SIMPLE_SCANNER_DATA_DIR':root}):
            path=Path(root)/'dex_latest.json'
            path.write_text(json.dumps({'observed_at':(dt.datetime.now(dt.timezone.utc)-dt.timedelta(minutes=62)).isoformat(),'candidates':[{'symbol':'OLD'}]}))
            out=io.StringIO()
            with patch.object(dex,'fetch',side_effect=TimeoutError('offline')),redirect_stdout(out):
                dex.main()
            self.assertIn('DEX_STALE_CACHE',out.getvalue())
            self.assertIn('"usable_for_current_research": false',out.getvalue())
            self.assertIn('"buy_approved": false',out.getvalue())

    def test_dex_circuit_recovery_preserves_research_only(self):
        with tempfile.TemporaryDirectory() as root,patch.dict('os.environ',{'SIMPLE_SCANNER_DATA_DIR':root}):
            state=Path(root)/'dex_circuit.json'
            state.write_text(json.dumps({'blocked_at':(dt.datetime.now(dt.timezone.utc)-dt.timedelta(hours=4)).isoformat()}))
            out=io.StringIO()
            with patch.object(dex,'fetch',return_value={'pairs':[]}),redirect_stdout(out):
                dex_guard.run()
            self.assertFalse(state.exists())
            self.assertIn('DEX_SUMMARY',out.getvalue())
            self.assertIn('"buy_approved": false',out.getvalue())

if __name__=='__main__':
    unittest.main()
