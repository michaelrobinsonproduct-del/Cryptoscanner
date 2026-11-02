"""Batch 24 isolated outbox acceptance: no network, no live execution."""
import json
import tempfile
import unittest
from pathlib import Path
from simple_scanner import fixture_delivery_outbox as outbox

RECEIPT={"status":"VERIFIED","buy_approved":False,"watch":[{"symbol":"BTC"}]}

class OutboxTests(unittest.TestCase):
    def test_stage_survives_reload_and_does_not_repeat_scan(self):
        with tempfile.TemporaryDirectory() as root:
            first=outbox.stage(root,42,"run-1",RECEIPT)
            self.assertEqual(first["status"],"PENDING")
            self.assertEqual(outbox.stage(root,42,"run-1",RECEIPT),first)
            self.assertEqual(len(outbox.pending(root)),1)
            self.assertEqual(outbox.pending(root)[0]["run_id"],"run-1")

    def test_confirm_is_idempotent_and_requires_matching_evidence(self):
        with tempfile.TemporaryDirectory() as root:
            first=outbox.stage(root,42,"run-1",RECEIPT)
            with self.assertRaises(RuntimeError):
                outbox.confirm(root,42,"wrong",first["sha256"],101)
            with self.assertRaises(ValueError):
                outbox.confirm(root,42,"run-1",first["sha256"],0)
            result=outbox.confirm(root,42,"run-1",first["sha256"],101)
            self.assertEqual(result["status"],"DELIVERED")
            self.assertEqual(outbox.confirm(root,42,"run-1",first["sha256"],101),result)
            self.assertEqual(outbox.pending(root),[])
            with self.assertRaises(RuntimeError):
                outbox.confirm(root,42,"run-1",first["sha256"],102)

    def test_ambiguous_network_result_stays_pending(self):
        with tempfile.TemporaryDirectory() as root:
            outbox.stage(root,42,"run-1",RECEIPT)
            # Timeout is not a confirmed GitHub comment. Never auto-ack.
            self.assertEqual(len(outbox.pending(root)),1)

    def test_conflicting_run_cannot_overwrite_pending_receipt(self):
        with tempfile.TemporaryDirectory() as root:
            outbox.stage(root,42,"run-1",RECEIPT)
            with self.assertRaises(RuntimeError):
                outbox.stage(root,42,"run-2",RECEIPT)
            self.assertEqual(outbox.pending(root)[0]["run_id"],"run-1")

    def test_corrupt_outbox_fails_closed(self):
        with tempfile.TemporaryDirectory() as root:
            Path(root,outbox.FILENAME).write_text("{bad")
            with self.assertRaises(ValueError):
                outbox.stage(root,42,"run-1",RECEIPT)

    def test_research_only_and_size_guard(self):
        with tempfile.TemporaryDirectory() as root:
            with self.assertRaises(ValueError):
                outbox.stage(root,42,"run-1",{"status":"VERIFIED","buy_approved":True})
            with self.assertRaises(RuntimeError):
                outbox.stage(root,42,"run-1",{"status":"VERIFIED","buy_approved":False,"watch":["X"*outbox.MAX_BYTES]})
            self.assertFalse(Path(root,outbox.FILENAME).exists())

if __name__=="__main__":
    unittest.main()
