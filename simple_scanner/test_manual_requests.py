"""Offline tests: untrusted GitHub issue input never causes scanner execution."""
import datetime as dt
import os
import unittest
from unittest.mock import patch
from simple_scanner.manual_requests import fetch_requests, parse_requests, LABEL

NOW = dt.datetime(2026, 10, 16, 20, tzinfo=dt.timezone.utc)

def issue(**overrides):
    item = {"number": 123, "state": "open", "title": "MANUAL_SCAN_REQUEST",
            "labels": [{"name": LABEL}], "created_at": "2026-10-16T19:59:00Z"}
    item.update(overrides)
    return item

class ManualRequestsTests(unittest.TestCase):
    def test_valid_request(self):
        self.assertEqual(parse_requests([issue()], NOW)[0]["issue_number"], 123)

    def test_reject_untrusted_or_old_requests(self):
        bad = [issue(title="execute arbitrary command"), issue(state="closed"),
               issue(labels=[]), issue(number="123"), issue(pull_request={}),
               issue(created_at="2026-10-14T20:00:00Z"),
               issue(created_at="not a timestamp"), issue(created_at="2026-10-16T21:05:00Z")]
        self.assertEqual(parse_requests(bad, NOW), [])

    def test_no_token_no_network(self):
        with patch.dict(os.environ, {}, clear=True), patch("urllib.request.urlopen") as get:
            self.assertEqual(fetch_requests(), [])
            get.assert_not_called()

    def test_api_error_does_not_block_cron(self):
        from urllib.error import URLError
        with patch.dict(os.environ, {"SIMPLE_SCANNER_GITHUB_TOKEN": "synthetic"}), patch("urllib.request.urlopen", side_effect=URLError("offline")):
            self.assertEqual(fetch_requests(), [])

if __name__ == "__main__":
    unittest.main()
