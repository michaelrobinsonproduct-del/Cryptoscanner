"""Offline receipt delivery tests; never send real GitHub requests."""
import io
import json
import os
import unittest
from unittest.mock import patch
from urllib.error import URLError
from simple_scanner.manual_requests import publish_results

class FakeResponse:
    status = 201
    def __enter__(self): return self
    def __exit__(self, *args): return False

class ReceiptTests(unittest.TestCase):
    def setUp(self):
        self.items = [{"issue_number": 123, "created_at": "2026-10-16T19:59:00+00:00"}]
        self.run = {"completed_at": "2026-10-16T20:00:00+00:00"}

    def test_no_token_never_calls_network(self):
        with patch.dict(os.environ, {}, clear=True), patch("urllib.request.urlopen") as send:
            self.assertEqual(publish_results(self.items, self.run), [])
            send.assert_not_called()

    def test_receipt_is_bounded_and_research_only(self):
        with patch.dict(os.environ, {"SIMPLE_SCANNER_GITHUB_TOKEN": "synthetic"}), patch("urllib.request.urlopen", return_value=FakeResponse()) as send:
            self.assertEqual(publish_results(self.items, self.run), self.items)
            request = send.call_args.args[0]
            body = json.loads(request.data)["body"]
            self.assertIn('"buy_approved": false', body)
            self.assertIn("MANUAL_SCAN_RESULT", body)
            self.assertNotIn("synthetic", body)

    def test_delivery_failure_never_acknowledged(self):
        with patch.dict(os.environ, {"SIMPLE_SCANNER_GITHUB_TOKEN": "synthetic"}), patch("urllib.request.urlopen", side_effect=URLError("offline")):
            self.assertEqual(publish_results(self.items, self.run), [])

if __name__ == "__main__":
    unittest.main()
