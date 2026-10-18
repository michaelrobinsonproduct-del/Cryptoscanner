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
    def test_wrapper_preserves_production_stage_order(self):
        from simple_scanner.execute_once import MODULES
        self.assertEqual(MODULES, (
            "simple_scanner.scan",
            "simple_scanner.history",
            "simple_scanner.shadow_learning",
            "simple_scanner.dex_guard",
        ))

    def test_docker_default_uses_locked_cron_wrapper(self):
        dockerfile = (Path(__file__).parent / "Dockerfile").read_text()
        self.assertIn('CMD ["python","-m","simple_scanner.execute_once","cron"]', dockerfile)

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


    def test_cron_and_manual_share_same_lock(self):
        import fcntl
        with tempfile.TemporaryDirectory() as folder:
            with patch.dict(os.environ, {"SIMPLE_SCANNER_DATA_DIR": folder}):
                with (Path(folder) / "scan_execution.lock").open("a+") as lock:
                    fcntl.flock(lock.fileno(), fcntl.LOCK_EX | fcntl.LOCK_NB)
                    with patch("simple_scanner.execute_once.subprocess.run") as run:
                        for origin in ("cron", "manual"):
                            with self.subTest(origin=origin):
                                output = io.StringIO()
                                with contextlib.redirect_stdout(output):
                                    self.assertEqual(execute(origin), 75)
                                self.assertIn("SCAN_BUSY", output.getvalue())
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
                           Result('HISTORY_SAME_RUN_AUDIT {"status":"MATCHED"}\nHISTORY_PERSISTED {"history_db_integrity":"ok","buy_approved":false,"model_updates":"DISABLED_PENDING_UNBIASED_FORWARD_VALIDATION"}'), Result('SHADOW_LEARNING {"mode":"SHADOW_ONLY","live_weights_modified":false}'), Result("DEX_CACHE_REUSED {}")]
                with patch("simple_scanner.execute_once.subprocess.run", side_effect=records):
                    output = io.StringIO()
                    with contextlib.redirect_stdout(output):
                        self.assertEqual(execute(), 0)
                    self.assertIn('"shadow_present": true', output.getvalue())
                old = (dt.datetime.now(dt.timezone.utc) - dt.timedelta(minutes=20)).isoformat()
                summary["started_at"] = old
                (Path(folder) / "latest.json").write_text(json.dumps(summary))
                records[0] = Result("SCAN_SUMMARY " + json.dumps(summary) + "\nWATCH_SUMMARY []")
                with patch("simple_scanner.execute_once.subprocess.run", side_effect=records):
                    self.assertEqual(execute(), 1)
    def test_invalid_shadow_record_is_partial_not_verified(self):
        with tempfile.TemporaryDirectory() as folder:
            with patch.dict(os.environ, {"SIMPLE_SCANNER_DATA_DIR": folder}):
                now = dt.datetime.now(dt.timezone.utc).isoformat()
                summary = {"started_at": now, "completed_at": now, "buy_approved": False, "status": "RESEARCH_ONLY"}
                (Path(folder) / "latest.json").write_text(json.dumps(summary))
                records = [Result("SCAN_SUMMARY " + json.dumps(summary) + "\nWATCH_SUMMARY []"),
                           Result('HISTORY_PERSISTED {"history_db_integrity":"ok","buy_approved":false,"model_updates":"DISABLED_PENDING_UNBIASED_FORWARD_VALIDATION"}'),
                           Result('SHADOW_LEARNING {"mode":"SHADOW_ONLY","live_weights_modified":true}'),
                           Result("DEX_CACHE_REUSED {}")]
                with patch("simple_scanner.execute_once.subprocess.run", side_effect=records):
                    output = io.StringIO()
                    with contextlib.redirect_stdout(output):
                        self.assertEqual(execute(), 0)
                    self.assertIn('"status": "PARTIAL"', output.getvalue())
                    self.assertIn('"shadow_present": false', output.getvalue())

    def test_shadow_failure_does_not_block_dex(self):
        with tempfile.TemporaryDirectory() as folder:
            with patch.dict(os.environ, {"SIMPLE_SCANNER_DATA_DIR": folder}):
                now = dt.datetime.now(dt.timezone.utc).isoformat()
                summary = {"started_at": now, "completed_at": now, "buy_approved": False, "status": "RESEARCH_ONLY"}
                (Path(folder) / "latest.json").write_text(json.dumps(summary))
                records = [Result("SCAN_SUMMARY " + json.dumps(summary) + "\nWATCH_SUMMARY []"),
                           Result('HISTORY_PERSISTED {"history_db_integrity":"ok","buy_approved":false,"model_updates":"DISABLED_PENDING_UNBIASED_FORWARD_VALIDATION"}'), Result(code=1), Result("DEX_CACHE_REUSED {}")]
                with patch("simple_scanner.execute_once.subprocess.run", side_effect=records) as run:
                    self.assertEqual(execute(), 0)
                    self.assertEqual(run.call_count, 4)

    def test_failed_shadow_with_emitted_record_remains_partial(self):
        with tempfile.TemporaryDirectory() as folder:
            with patch.dict(os.environ, {"SIMPLE_SCANNER_DATA_DIR": folder}):
                now = dt.datetime.now(dt.timezone.utc).isoformat()
                summary = {"started_at": now, "completed_at": now, "buy_approved": False, "status": "RESEARCH_ONLY"}
                (Path(folder) / "latest.json").write_text(json.dumps(summary))
                records = [Result("SCAN_SUMMARY " + json.dumps(summary) + "\nWATCH_SUMMARY []"),
                           Result('HISTORY_PERSISTED {"history_db_integrity":"ok","buy_approved":false,"model_updates":"DISABLED_PENDING_UNBIASED_FORWARD_VALIDATION"}'),
                           Result('SHADOW_LEARNING {"mode":"SHADOW_ONLY","live_weights_modified":false}', code=1),
                           Result("DEX_CACHE_REUSED {}")]
                with patch("simple_scanner.execute_once.subprocess.run", side_effect=records):
                    output = io.StringIO()
                    with contextlib.redirect_stdout(output):
                        self.assertEqual(execute(), 0)
                    self.assertIn('"status": "PARTIAL"', output.getvalue())
                    self.assertIn('"shadow_present": false', output.getvalue())

    def test_dex_freshness_gate(self):
        for age_minutes, expected in ((1, "VERIFIED"), (62, "PARTIAL")):
            with self.subTest(age_minutes=age_minutes), tempfile.TemporaryDirectory() as folder:
                with patch.dict(os.environ, {"SIMPLE_SCANNER_DATA_DIR": folder}):
                    now = dt.datetime.now(dt.timezone.utc).isoformat()
                    summary = {"started_at": now, "completed_at": now, "buy_approved": False, "status": "RESEARCH_ONLY"}
                    (Path(folder) / "latest.json").write_text(json.dumps(summary))
                    observed = (dt.datetime.now(dt.timezone.utc) - dt.timedelta(minutes=age_minutes)).isoformat()
                    dex = {"observed_at": observed, "buy_approved": False, "candidates": 0}
                    records = [Result("SCAN_SUMMARY " + json.dumps(summary) + "\nWATCH_SUMMARY []"),
                               Result('HISTORY_SAME_RUN_AUDIT {"status":"MATCHED"}\nHISTORY_PERSISTED {"history_db_integrity":"ok","buy_approved":false,"model_updates":"DISABLED_PENDING_UNBIASED_FORWARD_VALIDATION"}'),
                               Result('SHADOW_LEARNING {"mode":"SHADOW_ONLY","live_weights_modified":false}'),
                               Result("DEX_CACHE_REUSED " + json.dumps(dex))]
                    with patch("simple_scanner.execute_once.subprocess.run", side_effect=records):
                        output = io.StringIO()
                        with contextlib.redirect_stdout(output):
                            self.assertEqual(execute(), 0)
                        self.assertIn('"status": "' + expected + '"', output.getvalue())

    def test_rejects_unsafe_history_record(self):
        for unsafe in (
            {"history_db_integrity": "corrupt", "buy_approved": False, "model_updates": "DISABLED_PENDING_UNBIASED_FORWARD_VALIDATION"},
            {"history_db_integrity": "ok", "buy_approved": True, "model_updates": "DISABLED_PENDING_UNBIASED_FORWARD_VALIDATION"},
            {"history_db_integrity": "ok", "buy_approved": False, "model_updates": "ENABLED"},
        ):
            with self.subTest(unsafe=unsafe), tempfile.TemporaryDirectory() as folder:
                with patch.dict(os.environ, {"SIMPLE_SCANNER_DATA_DIR": folder}):
                    now = dt.datetime.now(dt.timezone.utc).isoformat()
                    summary = {"started_at": now, "completed_at": now, "buy_approved": False, "status": "RESEARCH_ONLY"}
                    (Path(folder) / "latest.json").write_text(json.dumps(summary))
                    dex = {"observed_at": now, "buy_approved": False}
                    records = [Result("SCAN_SUMMARY " + json.dumps(summary) + "\nWATCH_SUMMARY []"),
                               Result("HISTORY_PERSISTED " + json.dumps(unsafe)),
                               Result('SHADOW_LEARNING {"mode":"SHADOW_ONLY","live_weights_modified":false}'),
                               Result("DEX_CACHE_REUSED " + json.dumps(dex))]
                    with patch("simple_scanner.execute_once.subprocess.run", side_effect=records):
                        output = io.StringIO()
                        with contextlib.redirect_stdout(output):
                            self.assertEqual(execute(), 1)
                        self.assertIn("SCAN_HISTORY_SAFETY_FAILED", output.getvalue())

    def test_rejects_missing_and_naive_timestamps(self):
        with tempfile.TemporaryDirectory() as folder:
            with patch.dict(os.environ, {"SIMPLE_SCANNER_DATA_DIR": folder}):
                now = dt.datetime.now(dt.timezone.utc).isoformat()
                summary = {"started_at": now, "completed_at": now, "buy_approved": False, "status": "RESEARCH_ONLY"}
                outputs = [Result("SCAN_SUMMARY " + json.dumps(summary) + "\nWATCH_SUMMARY []"),
                           Result('HISTORY_PERSISTED {"history_db_integrity":"ok","buy_approved":false,"model_updates":"DISABLED_PENDING_UNBIASED_FORWARD_VALIDATION"}'), Result('SHADOW_LEARNING {"mode":"SHADOW_ONLY","live_weights_modified":false}'), Result("DEX_CACHE_REUSED {}")]
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
                           Result('HISTORY_PERSISTED {"history_db_integrity":"ok","buy_approved":false,"model_updates":"DISABLED_PENDING_UNBIASED_FORWARD_VALIDATION"}'), Result('SHADOW_LEARNING {"mode":"SHADOW_ONLY","live_weights_modified":false}'), Result("DEX_CACHE_REUSED {}")]
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
                           Result('HISTORY_PERSISTED {"history_db_integrity":"ok","buy_approved":false,"model_updates":"DISABLED_PENDING_UNBIASED_FORWARD_VALIDATION"}'), Result('SHADOW_LEARNING {"mode":"SHADOW_ONLY","live_weights_modified":false}'), Result("DEX_CACHE_REUSED {}")]
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
                           Result('HISTORY_PERSISTED {"history_db_integrity":"ok","buy_approved":false,"model_updates":"DISABLED_PENDING_UNBIASED_FORWARD_VALIDATION"}'), Result('SHADOW_LEARNING {"mode":"SHADOW_ONLY","live_weights_modified":false}'), Result("DEX_CACHE_REUSED {}")]
                with patch("simple_scanner.execute_once.subprocess.run", side_effect=records):
                    self.assertEqual(execute(), 1)

    def test_rejects_non_object_summary(self):
        with tempfile.TemporaryDirectory() as folder:
            with patch.dict(os.environ, {"SIMPLE_SCANNER_DATA_DIR": folder}):
                (Path(folder) / "latest.json").write_text("{}")
                records = [Result("SCAN_SUMMARY []\nWATCH_SUMMARY []"),
                           Result('HISTORY_PERSISTED {"history_db_integrity":"ok","buy_approved":false,"model_updates":"DISABLED_PENDING_UNBIASED_FORWARD_VALIDATION"}'), Result('SHADOW_LEARNING {"mode":"SHADOW_ONLY","live_weights_modified":false}'), Result("DEX_CACHE_REUSED {}")]
                with patch("simple_scanner.execute_once.subprocess.run", side_effect=records):
                    self.assertEqual(execute(), 1)

if __name__ == "__main__":
    unittest.main()
