"""Offline receipt delivery tests; never send real GitHub requests."""
import io
import json
import os
import unittest
from unittest.mock import patch
from urllib.error import URLError
from simple_scanner.manual_requests import publish_results, sanitize_watch

class FakeResponse:
    status = 201
    def __enter__(self): return self
    def __exit__(self, *args): return False

class ReceiptTests(unittest.TestCase):
    def setUp(self):
        self.items = [{"issue_number": 123, "created_at": "2026-10-16T19:59:00+00:00"}]
        self.run = {"completed_at": "2026-10-16T20:00:00+00:00"}

    def test_nonfinite_scores_never_published(self):
        self.assertNotIn("score", sanitize_watch([{"symbol": "TEST/USD", "score": float("nan")}])[0])

    def test_no_token_never_calls_network(self):
        with patch.dict(os.environ, {}, clear=True), patch("urllib.request.urlopen") as send:
            self.assertEqual(publish_results(self.items, self.run, [{"symbol": "TAO/USD", "score": 73.5, "move_15m_pct": 2.1, "volume_accel": 1.7, "risk": "HIGH", "private": "must-not-leak"}], "FRESH"), [])
            send.assert_not_called()

    def test_receipt_is_bounded_and_research_only(self):
        with patch.dict(os.environ, {"SIMPLE_SCANNER_GITHUB_TOKEN": "synthetic"}), patch("urllib.request.urlopen", return_value=FakeResponse()) as send:
            self.assertEqual(publish_results(self.items, self.run, [{"symbol": "TAO/USD", "score": 73.5, "move_15m_pct": 2.1, "volume_accel": 1.7, "risk": "HIGH", "private": "must-not-leak"}], "FRESH"), self.items)
            request = send.call_args.args[0]
            body = json.loads(request.data)["body"]
            self.assertIn('"buy_approved": false', body)
            self.assertIn("MANUAL_SCAN_RESULT", body)
            self.assertIn("TAO/USD", body)
            self.assertIn('"dex_status": "FRESH"', body)
            self.assertNotIn("must-not-leak", body)
            self.assertNotIn("synthetic", body)

    def test_delivery_failure_never_acknowledged(self):
        with patch.dict(os.environ, {"SIMPLE_SCANNER_GITHUB_TOKEN": "synthetic"}), patch("urllib.request.urlopen", side_effect=URLError("offline")):
            self.assertEqual(publish_results(self.items, self.run, [{"symbol": "TAO/USD", "score": 73.5, "move_15m_pct": 2.1, "volume_accel": 1.7, "risk": "HIGH", "private": "must-not-leak"}], "FRESH"), [])

if __name__ == "__main__":
    unittest.main()
