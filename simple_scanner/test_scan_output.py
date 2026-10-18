"""Regression checks for atomic scanner publication."""
import json
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch
from simple_scanner.scan_output import publish_latest_atomic

class AtomicOutputTests(unittest.TestCase):
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

    def test_replace_failure_preserves_previous_scan(self):
        with tempfile.TemporaryDirectory() as d:
            target=Path(d)/"latest.json"
            target.write_text('{"last_good":true}')
            with patch("simple_scanner.scan_output.os.replace",side_effect=OSError("disk error")):
                with self.assertRaises(OSError):
                    publish_latest_atomic(target, {"completed_at":"t2"})
            self.assertEqual(json.loads(target.read_text()),{"last_good":True})
            self.assertEqual([p.name for p in Path(d).iterdir()],["latest.json"])
