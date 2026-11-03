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
        with self.assertRaisesRegex(ValueError, "conflicting"):
            persist_report(self.latest, {**self.report, "watch": []})
        self.assertEqual(json.loads(receipt.read_text()), self.report)
        self.assertEqual(json.loads(self.latest.read_text()), self.report)

    def test_exact_retry_is_idempotent_and_does_not_rewrite_latest(self):
        receipt = persist_report(self.latest, self.report)
        original = self.latest.read_bytes()
        with patch("paper_pov.scanner.atomic_json", side_effect=AssertionError("unexpected rewrite")):
            self.assertEqual(persist_report(self.latest, self.report), receipt)
        self.assertEqual(self.latest.read_bytes(), original)
        self.assertEqual(len(list((self.latest.parent / "receipts").glob("*.json"))), 1)

    def test_missing_receipt_same_timestamp_rejected(self):
        receipt = persist_report(self.latest, self.report)
        receipt.unlink()
        with self.assertRaisesRegex(ValueError, "incomplete"):
            persist_report(self.latest, self.report)

    def test_tampered_receipt_same_timestamp_rejected(self):
        receipt = persist_report(self.latest, self.report)
        receipt.write_text("{}")
        with self.assertRaisesRegex(ValueError, "readback mismatch"):
            persist_report(self.latest, self.report)

    def test_latest_failure_preserves_sealed_receipt_and_retry_recovers(self):
        with patch("paper_pov.scanner.atomic_json", side_effect=OSError("disk full")):
            with self.assertRaisesRegex(OSError, "disk full"):
                persist_report(self.latest, self.report)
        self.assertFalse(self.latest.exists())
        receipts = list((self.latest.parent / "receipts").glob("*.json"))
        self.assertEqual(len(receipts), 1)
        self.assertEqual(json.loads(receipts[0].read_text()), self.report)
        recovered = persist_report(self.latest, self.report)
        self.assertEqual(recovered, receipts[0])
        self.assertEqual(json.loads(self.latest.read_text()), self.report)
        self.assertEqual(len(list((self.latest.parent / "receipts").glob("*.json"))), 1)

    def test_orphan_receipt_recovers_missing_latest_without_duplication(self):
        receipt = persist_report(self.latest, self.report)
        self.latest.unlink()
        with patch("paper_pov.scanner.os.open", wraps=__import__("os").open) as open_mock:
            self.assertEqual(persist_report(self.latest, self.report), receipt)
            self.assertFalse(any(call.args and call.args[0] == receipt
                                 for call in open_mock.call_args_list))
        self.assertEqual(json.loads(self.latest.read_text()), self.report)
        self.assertEqual(len(list((self.latest.parent / "receipts").glob("*.json"))), 1)

    def test_orphan_receipt_recovers_after_older_latest(self):
        older = {**self.report, "as_of": "2026-11-03T01:59:59+00:00"}
        persist_report(self.latest, older)
        receipt = persist_report(self.latest, self.report)
        self.latest.write_text(json.dumps(older))
        self.assertEqual(persist_report(self.latest, self.report), receipt)
        self.assertEqual(json.loads(self.latest.read_text()), self.report)

    def test_conflicting_orphan_never_overwrites(self):
        receipt = persist_report(self.latest, self.report)
        self.latest.unlink()
        receipt.write_text("{}")
        with self.assertRaisesRegex(ValueError, "conflicting orphan"):
            persist_report(self.latest, self.report)
        self.assertFalse(self.latest.exists())
        self.assertEqual(receipt.read_text(), "{}")

    def test_corrupt_latest_without_matching_receipt_fails_closed(self):
        self.latest.write_text("{}")
        with self.assertRaisesRegex(ValueError, "invalid latest without matching sealed receipt"):
            persist_report(self.latest, self.report)
        self.assertEqual(self.latest.read_text(), "{}")
        self.assertEqual(list((self.latest.parent / "receipts").glob("*.json")), [])

    def test_receipt_and_latest_directories_are_synced(self):
        with patch("paper_pov.scanner.sync_directory", wraps=__import__(
                "paper_pov.scanner", fromlist=["sync_directory"]).sync_directory) as sync:
            receipt = persist_report(self.latest, self.report)
        self.assertEqual([call.args[0] for call in sync.call_args_list],
                         [receipt.parent, self.latest.parent])
        self.assertEqual(json.loads(self.latest.read_text()), self.report)

    def test_latest_directory_sync_failure_recovers_without_duplicate_receipt(self):
        real_sync = __import__("paper_pov.scanner", fromlist=["sync_directory"]).sync_directory
        calls = 0
        def fail_second(path):
            nonlocal calls
            calls += 1
            if calls == 2:
                raise OSError("directory sync failed")
            real_sync(path)
        with patch("paper_pov.scanner.sync_directory", side_effect=fail_second):
            with self.assertRaisesRegex(OSError, "directory sync failed"):
                persist_report(self.latest, self.report)
        receipts = list((self.latest.parent / "receipts").glob("*.json"))
        self.assertEqual(len(receipts), 1)
        self.assertEqual(json.loads(receipts[0].read_text()), self.report)
        with patch("paper_pov.scanner.sync_directory", wraps=real_sync) as sync_retry:
            self.assertEqual(persist_report(self.latest, self.report), receipts[0])
        self.assertEqual([call.args[0] for call in sync_retry.call_args_list],
                         [receipts[0].parent, self.latest.parent])
        self.assertEqual(len(list((self.latest.parent / "receipts").glob("*.json"))), 1)

    def test_orphan_recovery_syncs_receipt_before_publishing_latest(self):
        receipt = persist_report(self.latest, self.report)
        self.latest.unlink()
        real_sync = __import__("paper_pov.scanner", fromlist=["sync_directory"]).sync_directory
        with patch("paper_pov.scanner.sync_directory", wraps=real_sync) as sync:
            with patch("paper_pov.scanner.atomic_json", wraps=__import__(
                    "paper_pov.scanner", fromlist=["atomic_json"]).atomic_json) as publish:
                self.assertEqual(persist_report(self.latest, self.report), receipt)
        self.assertGreaterEqual(sync.call_count, 2)
        self.assertEqual(sync.call_args_list[0].args[0], receipt.parent)
        self.assertEqual(publish.call_count, 1)
        self.assertEqual(json.loads(self.latest.read_text()), self.report)

    def test_orphan_sync_failure_never_publishes_latest(self):
        receipt = persist_report(self.latest, self.report)
        self.latest.unlink()
        with patch("paper_pov.scanner.sync_directory", side_effect=OSError("fsync interrupted")):
            with self.assertRaisesRegex(OSError, "fsync interrupted"):
                persist_report(self.latest, self.report)
        self.assertFalse(self.latest.exists())
        self.assertEqual(json.loads(receipt.read_text()), self.report)
        self.assertEqual(persist_report(self.latest, self.report), receipt)
        self.assertEqual(json.loads(self.latest.read_text()), self.report)

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

    def test_latest_readback_failure_preserves_sealed_receipt(self):
        with patch("paper_pov.scanner.atomic_json", side_effect=lambda path, report: Path(path).write_text("{}")):
            with self.assertRaisesRegex(IOError, "latest report readback mismatch"):
                persist_report(self.latest, self.report)
        receipts = list((self.latest.parent / "receipts").glob("*.json"))
        self.assertEqual(len(receipts), 1)
        self.assertEqual(json.loads(receipts[0].read_text()), self.report)
        self.assertEqual(persist_report(self.latest, self.report), receipts[0])
        self.assertEqual(json.loads(self.latest.read_text()), self.report)

if __name__ == "__main__":
    unittest.main()
