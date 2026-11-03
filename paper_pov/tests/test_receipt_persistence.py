"""Focused A2 receipt persistence tests: no live data or production writes."""
import datetime as dt
import json
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

from paper_pov.scanner import UTC, persist_report

class ReceiptTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.latest = Path(self.temp.name) / "latest.json"
        self.report = {"as_of": "2026-11-03T02:00:00+00:00", "mode": "PAPER_ONLY",
                       "watch": [{"pair": "TESTUSD", "status": "PAPER_WATCH", "buy_approved": False}]}

    def test_immutable_receipt_and_latest_readback(self):
        receipt = persist_report(self.latest, self.report)
        self.assertEqual(json.loads(receipt.read_text()), self.report)
        self.assertEqual(json.loads(self.latest.read_text()), self.report)
        self.assertEqual(len(list((self.latest.parent / "receipts").glob("*.json"))), 1)

    def test_duplicate_scan_does_not_replace_latest(self):
        receipt = persist_report(self.latest, self.report)
        with self.assertRaises(FileExistsError):
            persist_report(self.latest, {**self.report, "watch": []})
        self.assertEqual(json.loads(receipt.read_text()), self.report)
        self.assertEqual(json.loads(self.latest.read_text()), self.report)

    def test_latest_failure_removes_new_receipt(self):
        with patch("paper_pov.scanner.atomic_json", side_effect=OSError("disk full")):
            with self.assertRaisesRegex(OSError, "disk full"):
                persist_report(self.latest, self.report)
        self.assertFalse(self.latest.exists())
        self.assertEqual(list((self.latest.parent / "receipts").glob("*.json")), [])

    def test_invalid_report_never_writes(self):
        with self.assertRaises(ValueError):
            persist_report(self.latest, {**self.report, "bad": float("nan")})
        self.assertFalse(self.latest.exists())

    def test_older_scan_does_not_regress_latest(self):
        persist_report(self.latest, self.report)
        older = dict(self.report, as_of="2026-11-03T01:59:59+00:00")
        with self.assertRaisesRegex(ValueError, "out-of-order"):
            persist_report(self.latest, older)
        self.assertEqual(json.loads(self.latest.read_text()), self.report)

    def test_latest_readback_failure(self):
        with patch("paper_pov.scanner.atomic_json", side_effect=lambda path, report: Path(path).write_text("{}")):
            with self.assertRaisesRegex(IOError, "latest report readback mismatch"):
                persist_report(self.latest, self.report)
        self.assertEqual(list((self.latest.parent / "receipts").glob("*.json")), [])

if __name__ == "__main__":
    unittest.main()
