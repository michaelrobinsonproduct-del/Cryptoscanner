"""Offline integration tests: optional mailbox cannot interfere with scan stages."""
import os
import tempfile
import unittest
from unittest.mock import patch
from simple_scanner.execute_once import execute

class MailboxIntegrationTests(unittest.TestCase):
    def test_cron_without_token_never_checks_github(self):
        with tempfile.TemporaryDirectory() as folder:
            with patch.dict(os.environ, {"SIMPLE_SCANNER_DATA_DIR": folder}, clear=True), \
                 patch("simple_scanner.manual_requests.fetch_requests") as fetch, \
                 patch("simple_scanner.execute_once.subprocess.run") as run:
                run.return_value.returncode = 1
                run.return_value.stdout = ""
                run.return_value.stderr = "synthetic failure"
                self.assertEqual(execute("cron"), 1)
                fetch.assert_not_called()

    def test_manual_checks_github_with_token(self):
        with tempfile.TemporaryDirectory() as folder:
            with patch.dict(os.environ, {"SIMPLE_SCANNER_DATA_DIR": folder, "SIMPLE_SCANNER_GITHUB_TOKEN": "synthetic"}, clear=True), \
                 patch("simple_scanner.manual_requests.fetch_requests") as fetch, \
                 patch("simple_scanner.execute_once.subprocess.run") as run:
                run.return_value.returncode = 1
                run.return_value.stdout = ""
                run.return_value.stderr = "synthetic failure"
                self.assertEqual(execute("manual"), 1)
                fetch.assert_called_once()

    def test_github_failure_does_not_block_scan(self):
        with tempfile.TemporaryDirectory() as folder:
            with patch.dict(os.environ, {"SIMPLE_SCANNER_DATA_DIR": folder, "SIMPLE_SCANNER_GITHUB_TOKEN": "synthetic"}, clear=True), \
                 patch("simple_scanner.manual_requests.fetch_requests", side_effect=RuntimeError("offline")), \
                 patch("simple_scanner.execute_once.subprocess.run") as run:
                run.return_value.returncode = 1
                run.return_value.stdout = ""
                run.return_value.stderr = "synthetic failure"
                self.assertEqual(execute("cron"), 1)
                run.assert_called_once()

if __name__ == "__main__":
    unittest.main()
