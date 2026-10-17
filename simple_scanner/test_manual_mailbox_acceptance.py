"""End-to-end offline manual mailbox acceptance tests. No network or live scans."""
import contextlib
import datetime as dt
import io
import json
import os
from pathlib import Path
import tempfile
import unittest
from unittest.mock import patch

from simple_scanner.execute_once import execute
from simple_scanner.manual_requests import read_ledger

class Result:
    returncode = 0
    stderr = ""
    def __init__(self, stdout):
        self.stdout = stdout

class ManualMailboxAcceptance(unittest.TestCase):
    def run_case(self, *, shadow_valid=True, dex_age_minutes=1, publish_ok=True, scan_valid=True):
        with tempfile.TemporaryDirectory() as folder:
            now = dt.datetime.now(dt.timezone.utc)
            stamp = now.isoformat()
            summary = {"started_at":stamp, "completed_at":stamp, "buy_approved":False, "status":"RESEARCH_ONLY"}
            if not scan_valid:
                summary["buy_approved"] = True
            Path(folder, "latest.json").write_text(json.dumps(summary))
            watch = [{"symbol":"TAO/USD", "score":50.0, "move_15m_pct":0.1, "volume_accel":1.1, "risk":"MEDIUM"}]
            history = {"history_db_integrity":"ok", "buy_approved":False, "model_updates":"DISABLED_PENDING_UNBIASED_FORWARD_VALIDATION"}
            shadow = {"mode":"SHADOW_ONLY", "live_weights_modified":not shadow_valid}
            dex = {"observed_at":(now-dt.timedelta(minutes=dex_age_minutes)).isoformat(), "buy_approved":False, "candidates":0}
            records = [
                Result("SCAN_SUMMARY "+json.dumps(summary)+"\nWATCH_SUMMARY "+json.dumps(watch)),
                Result("HISTORY_PERSISTED "+json.dumps(history)),
                Result("SHADOW_LEARNING "+json.dumps(shadow)),
                Result("DEX_CACHE_REUSED "+json.dumps(dex)),
            ]
            request = {"issue_number":123, "created_at":(now-dt.timedelta(minutes=1)).isoformat()}
            env = {"SIMPLE_SCANNER_DATA_DIR":folder, "SIMPLE_SCANNER_GITHUB_TOKEN":"synthetic"}
            with patch.dict(os.environ,env,clear=True), \
                 patch("simple_scanner.manual_requests.fetch_requests", return_value=[request]) as fetch, \
                 patch("simple_scanner.manual_requests.publish_results", return_value=[request] if publish_ok else []) as publish, \
                 patch("simple_scanner.execute_once.subprocess.run",side_effect=records) as stages:
                output = io.StringIO()
                with contextlib.redirect_stdout(output):
                    exit_code=execute("cron")
                state=read_ledger(folder)
                self.assertEqual(stages.call_count,4)
                self.assertEqual(fetch.call_count,1)
                if scan_valid and shadow_valid and dex_age_minutes<=61:
                    publish.assert_called_once()
                    self.assertEqual(state["completed_issue_numbers"],[123] if publish_ok else [])
                    self.assertEqual(exit_code,0)
                    self.assertIn('"status": "VERIFIED"',output.getvalue())
                else:
                    publish.assert_not_called()
                    self.assertEqual(state["completed_issue_numbers"],[])
                    if scan_valid:
                        self.assertIn('"status": "PARTIAL"',output.getvalue())
                    else:
                        self.assertNotEqual(exit_code,0)
                return output.getvalue()

    def test_verified_delivery_acknowledged(self):
        self.run_case()
    def test_failed_delivery_not_acknowledged(self):
        self.run_case(publish_ok=False)
    def test_expired_dex_never_satisfies_request(self):
        self.run_case(dex_age_minutes=62)
    def test_shadow_model_modification_never_satisfies_request(self):
        self.run_case(shadow_valid=False)
    def test_buy_approval_never_satisfies_request(self):
        self.run_case(scan_valid=False)

if __name__ == "__main__":
    unittest.main()
