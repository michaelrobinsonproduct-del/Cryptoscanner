"""Offline tests for the isolated executor; never call Kraken or Railway."""
import contextlib
import io
import json
import datetime as dt
import subprocess
import os
from pathlib import Path
import tempfile
import unittest
from unittest.mock import patch
from simple_scanner.execute_once import execute

class Result:
    def __init__(self, out="", code=0):
        self.stdout = out
        self.stderr = "synthetic failure" if code else ""
        self.returncode = code

class ExecuteTests(unittest.TestCase):
    def test_reject_invalid_origin(self):
        with self.assertRaises(ValueError):
            execute("invalid")

    def test_fails_closed_on_scan_error(self):
        with tempfile.TemporaryDirectory() as folder:
            with patch.dict(os.environ, {"SIMPLE_SCANNER_DATA_DIR": folder}):
                with patch("simple_scanner.execute_once.subprocess.run", return_value=Result(code=1)):
                    self.assertEqual(execute(), 1)

    def test_rejects_missing_records(self):
        with tempfile.TemporaryDirectory() as folder:
            with patch.dict(os.environ, {"SIMPLE_SCANNER_DATA_DIR": folder}):
                with patch("simple_scanner.execute_once.subprocess.run", return_value=Result()):
                    self.assertEqual(execute(), 1)

    def test_lock_rejects_concurrent_execution(self):
        import fcntl
        with tempfile.TemporaryDirectory() as folder:
            with patch.dict(os.environ, {"SIMPLE_SCANNER_DATA_DIR": folder}):
                with (Path(folder) / "scan_execution.lock").open("a+") as lock:
                    fcntl.flock(lock.fileno(), fcntl.LOCK_EX | fcntl.LOCK_NB)
                    with patch("simple_scanner.execute_once.subprocess.run") as run:
                        self.assertEqual(execute(), 75)
                        run.assert_not_called()


    def test_timeout(self):
        with tempfile.TemporaryDirectory() as folder:
            with patch.dict(os.environ, {"SIMPLE_SCANNER_DATA_DIR": folder}):
                with patch("simple_scanner.execute_once.subprocess.run", side_effect=subprocess.TimeoutExpired("scan", 240)):
                    self.assertEqual(execute(), 124)

    def test_success_and_stale_rejection(self):
        with tempfile.TemporaryDirectory() as folder:
            with patch.dict(os.environ, {"SIMPLE_SCANNER_DATA_DIR": folder}):
                now = dt.datetime.now(dt.timezone.utc).isoformat()
                summary = {"started_at": now, "completed_at": now, "buy_approved": False, "status": "RESEARCH_ONLY"}
                (Path(folder) / "latest.json").write_text(json.dumps(summary))
                records = [Result("SCAN_SUMMARY " + json.dumps(summary) + "\nWATCH_SUMMARY []"),
                           Result("HISTORY_PERSISTED {}"), Result("SHADOW_LEARNING {}"), Result("DEX_CACHE_REUSED {}")]
                with patch("simple_scanner.execute_once.subprocess.run", side_effect=records):
                    self.assertEqual(execute(), 0)
                old = (dt.datetime.now(dt.timezone.utc) - dt.timedelta(minutes=20)).isoformat()
                summary["started_at"] = old
                (Path(folder) / "latest.json").write_text(json.dumps(summary))
                records[0] = Result("SCAN_SUMMARY " + json.dumps(summary) + "\nWATCH_SUMMARY []")
                with patch("simple_scanner.execute_once.subprocess.run", side_effect=records):
                    self.assertEqual(execute(), 1)
    def test_shadow_failure_does_not_block_dex(self):
        with tempfile.TemporaryDirectory() as folder:
            with patch.dict(os.environ, {"SIMPLE_SCANNER_DATA_DIR": folder}):
                now = dt.datetime.now(dt.timezone.utc).isoformat()
                summary = {"started_at": now, "completed_at": now, "buy_approved": False, "status": "RESEARCH_ONLY"}
                (Path(folder) / "latest.json").write_text(json.dumps(summary))
                records = [Result("SCAN_SUMMARY " + json.dumps(summary) + "\nWATCH_SUMMARY []"),
                           Result("HISTORY_PERSISTED {}"), Result(code=1), Result("DEX_CACHE_REUSED {}")]
                with patch("simple_scanner.execute_once.subprocess.run", side_effect=records) as run:
                    self.assertEqual(execute(), 0)
                    self.assertEqual(run.call_count, 4)

    def test_rejects_missing_and_naive_timestamps(self):
        with tempfile.TemporaryDirectory() as folder:
            with patch.dict(os.environ, {"SIMPLE_SCANNER_DATA_DIR": folder}):
                now = dt.datetime.now(dt.timezone.utc).isoformat()
                summary = {"started_at": now, "completed_at": now, "buy_approved": False, "status": "RESEARCH_ONLY"}
                outputs = [Result("SCAN_SUMMARY " + json.dumps(summary) + "\nWATCH_SUMMARY []"),
                           Result("HISTORY_PERSISTED {}"), Result("SHADOW_LEARNING {}"), Result("DEX_CACHE_REUSED {}")]
                for invalid in ("not-a-date", dt.datetime.now().isoformat()):
                    summary["started_at"] = invalid
                    (Path(folder) / "latest.json").write_text(json.dumps(summary))
                    outputs[0] = Result("SCAN_SUMMARY " + json.dumps(summary) + "\nWATCH_SUMMARY []")
                    with patch("simple_scanner.execute_once.subprocess.run", side_effect=outputs):
                        self.assertEqual(execute(), 1)

    def test_missing_latest_json_fails_closed(self):
        with tempfile.TemporaryDirectory() as folder:
            with patch.dict(os.environ, {"SIMPLE_SCANNER_DATA_DIR": folder}):
                now = dt.datetime.now(dt.timezone.utc).isoformat()
                summary = {"started_at": now, "completed_at": now, "buy_approved": False, "status": "RESEARCH_ONLY"}
                records = [Result("SCAN_SUMMARY " + json.dumps(summary) + "\nWATCH_SUMMARY []"),
                           Result("HISTORY_PERSISTED {}"), Result("SHADOW_LEARNING {}"), Result("DEX_CACHE_REUSED {}")]
                with patch("simple_scanner.execute_once.subprocess.run", side_effect=records):
                    self.assertEqual(execute(), 1)

    def test_rejects_future_completion(self):
        with tempfile.TemporaryDirectory() as folder:
            with patch.dict(os.environ, {"SIMPLE_SCANNER_DATA_DIR": folder}):
                now = dt.datetime.now(dt.timezone.utc)
                summary = {"started_at": now.isoformat(),
                           "completed_at": (now + dt.timedelta(hours=1)).isoformat(),
                           "buy_approved": False, "status": "RESEARCH_ONLY"}
                (Path(folder) / "latest.json").write_text(json.dumps(summary))
                records = [Result("SCAN_SUMMARY " + json.dumps(summary) + "\nWATCH_SUMMARY []"),
                           Result("HISTORY_PERSISTED {}"), Result("SHADOW_LEARNING {}"), Result("DEX_CACHE_REUSED {}")]
                with patch("simple_scanner.execute_once.subprocess.run", side_effect=records):
                    self.assertEqual(execute(), 1)

    def test_rejects_persisted_buy_approval(self):
        with tempfile.TemporaryDirectory() as folder:
            with patch.dict(os.environ, {"SIMPLE_SCANNER_DATA_DIR": folder}):
                now = dt.datetime.now(dt.timezone.utc).isoformat()
                summary = {"started_at": now, "completed_at": now, "buy_approved": False, "status": "RESEARCH_ONLY"}
                latest = dict(summary, buy_approved=True)
                (Path(folder) / "latest.json").write_text(json.dumps(latest))
                records = [Result("SCAN_SUMMARY " + json.dumps(summary) + "\nWATCH_SUMMARY []"),
                           Result("HISTORY_PERSISTED {}"), Result("SHADOW_LEARNING {}"), Result("DEX_CACHE_REUSED {}")]
                with patch("simple_scanner.execute_once.subprocess.run", side_effect=records):
                    self.assertEqual(execute(), 1)

    def test_rejects_non_object_summary(self):
        with tempfile.TemporaryDirectory() as folder:
            with patch.dict(os.environ, {"SIMPLE_SCANNER_DATA_DIR": folder}):
                (Path(folder) / "latest.json").write_text("{}")
                records = [Result("SCAN_SUMMARY []\nWATCH_SUMMARY []"),
                           Result("HISTORY_PERSISTED {}"), Result("SHADOW_LEARNING {}"), Result("DEX_CACHE_REUSED {}")]
                with patch("simple_scanner.execute_once.subprocess.run", side_effect=records):
                    self.assertEqual(execute(), 1)

if __name__ == "__main__":
    unittest.main()
