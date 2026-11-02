"""Offline authentication tests for disabled manual HTTP trigger."""
import http.client
import threading
import unittest
from http.server import ThreadingHTTPServer
from unittest.mock import patch
from simple_scanner.manual_trigger import Handler

class TriggerTests(unittest.TestCase):
    def setUp(self):
        self.server = ThreadingHTTPServer(("127.0.0.1", 0), Handler)
        self.thread = threading.Thread(target=self.server.serve_forever, daemon=True)
        self.thread.start()

    def tearDown(self):
        self.server.shutdown()
        self.server.server_close()
        self.thread.join(timeout=2)

    def request(self, token=None, body=None):
        connection = http.client.HTTPConnection("127.0.0.1", self.server.server_port, timeout=2)
        headers = {"Content-Length": "0" if body is None else str(len(body))}
        if token:
            headers["Authorization"] = token
        connection.request("POST", "/internal/manual-scan", body=body, headers=headers)
        response = connection.getresponse()
        status = response.status
        response.read()
        connection.close()
        return status

    def test_missing_secret_fails_closed(self):
        with patch.dict("os.environ", {}, clear=True), patch("simple_scanner.manual_trigger.execute") as run:
            self.assertEqual(self.request("Bearer example"), 401)
            run.assert_not_called()

    def test_bad_token_cannot_run(self):
        with patch.dict("os.environ", {"SIMPLE_SCANNER_TRIGGER_TOKEN": "correct"}), patch("simple_scanner.manual_trigger.execute") as run:
            self.assertEqual(self.request("Bearer wrong"), 401)
            run.assert_not_called()

    def test_valid_token_runs_same_executor(self):
        with patch.dict("os.environ", {"SIMPLE_SCANNER_TRIGGER_TOKEN": "correct"}), patch("simple_scanner.manual_trigger.execute", return_value=0) as run:
            self.assertEqual(self.request("Bearer correct"), 200)
            run.assert_called_once_with("manual")

    def test_busy_does_not_retry(self):
        with patch.dict("os.environ", {"SIMPLE_SCANNER_TRIGGER_TOKEN": "correct"}), patch("simple_scanner.manual_trigger.execute", return_value=75) as run:
            self.assertEqual(self.request("Bearer correct"), 409)
            run.assert_called_once()

    def test_rejects_request_body(self):
        with patch.dict("os.environ", {"SIMPLE_SCANNER_TRIGGER_TOKEN": "correct"}), patch("simple_scanner.manual_trigger.execute") as run:
            self.assertEqual(self.request("Bearer correct", b"extra"), 400)
            run.assert_not_called()

if __name__ == "__main__":
    unittest.main()
