"""Regression checks for atomic scanner publication."""
import json
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch
from simple_scanner.scan_output import publish_latest_atomic, verify_market_evidence

class AtomicOutputTests(unittest.TestCase):
    def test_market_evidence_audit_complete(self):
        report={"started_at":"2026-10-18T16:00:00+00:00",
                "completed_at":"2026-10-18T16:00:10+00:00",
                "market_prices":{"SOLUSD":100},
                "market_signals":{"SOLUSD":{"move24_pct":2}},
                "asset_pairs":{"SOLUSD":{"base":"SOL"}}}
        result=verify_market_evidence(report)
        self.assertEqual(result["status"],"COMPLETE")
        self.assertEqual(result["scan_duration_seconds"],10)

    def test_market_evidence_audit_fails_closed(self):
        report={"started_at":"2026-10-18T16:00:10+00:00",
                "completed_at":"2026-10-18T16:00:00+00:00",
                "market_prices":{},
                "market_signals":{"SOLUSD":{"move24_pct":2}},
                "asset_pairs":{}}
        result=verify_market_evidence(report)
        self.assertEqual(result["status"],"INCOMPLETE")
        self.assertEqual(result["missing_pairs"],["SOLUSD"])

    def test_complete_output_and_no_temporary_file(self):
        with tempfile.TemporaryDirectory() as d:
            target=Path(d)/"latest.json"
            publish_latest_atomic(target, {"completed_at":"t1","watch":[{"pair":"SOLUSD"}]})
            self.assertEqual(json.loads(target.read_text())["watch"][0]["pair"],"SOLUSD")
            self.assertEqual([p.name for p in Path(d).iterdir()],["latest.json"])

    def test_serialization_failure_preserves_previous_scan(self):
        with tempfile.TemporaryDirectory() as d:
            target=Path(d)/"latest.json"
            target.write_text('{"last_good":true}')
            with self.assertRaises(TypeError):
                publish_latest_atomic(target, {"bad":object()})
            self.assertEqual(json.loads(target.read_text()),{"last_good":True})
            self.assertEqual([p.name for p in Path(d).iterdir()],["latest.json"])

    def test_directory_sync_failure_is_reported(self):
        with tempfile.TemporaryDirectory() as d:
            target=Path(d)/"latest.json"
            with patch("simple_scanner.scan_output.os.fsync",side_effect=[None,OSError("directory sync failed")]):
                with self.assertRaisesRegex(OSError,"directory sync failed"):
                    publish_latest_atomic(target, {"completed_at":"t2"})
            self.assertEqual(json.loads(target.read_text()),{"completed_at":"t2"})
            self.assertEqual([p.name for p in Path(d).iterdir()],["latest.json"])

    def test_replace_failure_preserves_previous_scan(self):
        with tempfile.TemporaryDirectory() as d:
            target=Path(d)/"latest.json"
            target.write_text('{"last_good":true}')
            with patch("simple_scanner.scan_output.os.replace",side_effect=OSError("disk error")):
                with self.assertRaises(OSError):
                    publish_latest_atomic(target, {"completed_at":"t2"})
            self.assertEqual(json.loads(target.read_text()),{"last_good":True})
            self.assertEqual([p.name for p in Path(d).iterdir()],["latest.json"])
