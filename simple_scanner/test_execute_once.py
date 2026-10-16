"""Offline tests for the isolated executor; never call Kraken or Railway."""
import contextlib
import io
import json
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

if __name__ == "__main__":
    unittest.main()
