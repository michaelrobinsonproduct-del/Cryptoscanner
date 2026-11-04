"""Focused C/D read-only recovered writer bridge acceptance."""
import copy
import unittest
import json
import subprocess
import sys
import tempfile
from pathlib import Path
from paper_pov.c_writer_recovery_bridge import bridge
from paper_pov.test_c_candidate_handoff import fixture


def integration():
    src = fixture()
    return {
        "schema": "c_read_only_integration_v1",
        "status": "ABSTAIN_LEGACY_QUOTE_EVIDENCE",
        "recovery_verified": True,
        "historical_artifact_parity": True,
        "manual_run": "41636714169",
        "scheduled_run": "41626400391",
        "a2_snapshot_attached": True,
        "exchange_event_freshness_verified": False,
        "production_applied": False,
        "trading_approved": False,
        "a2_receipt_sha256": src["receipt_sha256"],
        "a2_as_of": src["source_as_of"],
        "a2_source_cohort": src["source_cohort"],
        "a2_eligible_pairs": src["eligible_pairs"],
        "a2_observed_markets": src["observed_markets"],
        "a2_watch_count": src["watch_count"],
        "a2_watch_candidates": src["watch"],
    }


def readback():
    return {
        "status": "WRITER_CHECKSUM_ONLY",
        "remote_downloaded": True,
        "ledger_writer_invoked": False,
        "production_applied": False,
        "independently_authenticated": False,
        "run_id": "41636714169",
        "source_sha": "94929a544899ddec63c676b6d4d52539da8e3837",
        "artifact_id": 13231431070,
    }


class BridgeTests(unittest.TestCase):
    def test_real_writer_provenance_and_historical_candidates_remain_distinct(self):
        result = bridge(integration(), readback(), restored_latest={"mode": "PAPER_ONLY"})
        self.assertEqual(result["historical_a2"]["watch_count"], 2)
        self.assertEqual(result["writer_recovery"]["artifact_id"], 13231431070)
        self.assertFalse(result["writer_recovery"]["independently_authenticated"])
        self.assertFalse(result["same_run_or_candidate_parity_claimed"])
        self.assertFalse(result["live_watch_certified"])
        self.assertFalse(result["production_applied"])

    def test_rejects_failed_or_falsely_authenticated_writer(self):
        for key, value in (("status", "REMOTE_READBACK_FAILED"),
                           ("independently_authenticated", True),
                           ("remote_downloaded", False),
                           ("ledger_writer_invoked", True),
                           ("production_applied", True),
                           ("source_sha", "bad")):
            with self.subTest(key=key):
                bad = copy.deepcopy(readback())
                bad[key] = value
                with self.assertRaises(ValueError):
                    bridge(integration(), bad)
        with self.assertRaises(ValueError):
            bridge(integration(), readback(), restored_latest={"trading_approved": True})

    def test_real_persisted_writer_status_and_remote_divergence(self):
        actual = {**readback(), "status": "VERIFIED_REMOTE_READBACK", "independently_authenticated": True,
                  "persisted_paper": {"ledger_generation": 70, "scan_status": "ABSTAIN_STALE_QUOTE",
                                      "quote_evidence_certified": False, "live_replay_performed": False},
                  "remote_ledger_reconciliation": {"status": "DIVERGED", "independently_authenticated": False}}
        output = bridge(integration(), actual)
        self.assertEqual(output["writer_recovery"]["persisted_paper"]["ledger_generation"], 70)
        self.assertEqual(output["writer_recovery"]["remote_ledger_reconciliation"]["status"], "DIVERGED")
        self.assertFalse(output["live_watch_certified"])
        self.assertFalse(output["writer_recovery"]["delivery_projection_ready"])
        self.assertEqual(output["writer_recovery"]["delivery_blocker"], "D_REMOTE_LEDGER_RECONCILIATION_NOT_MATCH")
        with self.assertRaises(ValueError):
            bridge(integration(), {**actual, "remote_ledger_reconciliation": {"status": "MATCH", "independently_authenticated": True}})

    def test_missing_remote_branch_preserves_historical_recovery(self):
        d = {**readback(), "remote_ledger_reconciliation": {"status": "UNAVAILABLE", "reason": "REMOTE_LEDGER_QUERY_FAILED", "independently_authenticated": False}}
        result = bridge(integration(), d)
        self.assertEqual(result["writer_recovery"]["remote_ledger_reconciliation"]["status"], "UNAVAILABLE")
        self.assertFalse(result["live_watch_certified"])

    def test_cli_emits_recovered_provenance_and_replay_as_separate_artifacts(self):
        with tempfile.TemporaryDirectory() as d:
            root = Path(d)
            (root / "integration.json").write_text(json.dumps(integration()))
            (root / "readback.json").write_text(json.dumps(readback()))
            result = subprocess.run([
                sys.executable, "-m", "paper_pov.c_writer_recovery_bridge",
                "--integration", str(root / "integration.json"),
                "--readback", str(root / "readback.json"),
                "--output", str(root / "combined.json"),
                "--bd-output", str(root / "bd.json"),
                "--writer-readback-output", str(root / "writer.json"),
            ], capture_output=True, text=True)
            self.assertEqual(result.returncode, 0, result.stderr)
            combined = json.loads((root / "combined.json").read_text())
            bd = json.loads((root / "bd.json").read_text())
            self.assertFalse((root / "writer.json").exists())
            self.assertEqual(combined["writer_recovery"]["delivery_blocker"], "D_REMOTE_READBACK_NOT_INDEPENDENTLY_AUTHENTICATED")
            self.assertEqual(bd, combined["historical_a2"])
            self.assertFalse(combined["same_run_or_candidate_parity_claimed"])
            self.assertEqual(bd["status"], "WATCH_REPLAY_ONLY_NOT_LIVE")

    def test_writer_delivery_export_requires_real_persisted_paper(self):
        actual = {**readback(), "status": "VERIFIED_REMOTE_READBACK", "independently_authenticated": True, "persisted_paper": {"ledger_generation": 70, "scan_status": "ABSTAIN_STALE_QUOTE", "live_replay_performed": False}, "remote_ledger_reconciliation": {"status": "MATCH", "independently_authenticated": False}}
        with tempfile.TemporaryDirectory() as d:
            root = Path(d)
            (root / "integration.json").write_text(json.dumps(integration()))
            (root / "readback.json").write_text(json.dumps(actual))
            proc = subprocess.run([sys.executable, "-m", "paper_pov.c_writer_recovery_bridge",
                "--integration", str(root / "integration.json"), "--readback", str(root / "readback.json"),
                "--output", str(root / "combined.json"), "--writer-readback-output", str(root / "writer.json")],
                capture_output=True, text=True)
            self.assertEqual(proc.returncode, 0, proc.stderr)
            self.assertEqual(json.loads((root / "writer.json").read_text()), actual)
            self.assertTrue(json.loads((root / "combined.json").read_text())["writer_recovery"]["delivery_projection_ready"])

    def test_writer_export_rejects_diverged_and_unavailable_remote_ledger(self):
        actual = {**readback(), "status": "VERIFIED_REMOTE_READBACK", "independently_authenticated": True, "persisted_paper": {"ledger_generation": 70, "scan_status": "WATCH", "live_replay_performed": False},
                  "remote_ledger_reconciliation": {"status": "MATCH", "independently_authenticated": False}}
        with tempfile.TemporaryDirectory() as d:
            root = Path(d)
            (root / "integration.json").write_text(json.dumps(integration()))
            (root / "readback.json").write_text(json.dumps(actual))
            for status in ("MATCH", "DIVERGED", "UNAVAILABLE"):
                actual["remote_ledger_reconciliation"]["status"] = status
                (root / "readback.json").write_text(json.dumps(actual))
                result = subprocess.run([sys.executable, "-m", "paper_pov.c_writer_recovery_bridge",
                    "--integration", str(root / "integration.json"), "--readback", str(root / "readback.json"),
                    "--output", str(root / "combined.json"), "--writer-readback-output", str(root / "writer.json")],
                    capture_output=True, text=True)
                self.assertEqual(result.returncode, 0, result.stderr)
                self.assertEqual((root / "writer.json").exists(), status == "MATCH")
                self.assertEqual(json.loads((root / "combined.json").read_text())["writer_recovery"]["delivery_projection_ready"], status == "MATCH")

    def test_checksum_only_match_never_exports_delivery_receipt(self):
        # A checksum-matched artifact is not independent remote ledger proof.
        actual = {**readback(), "persisted_paper": {"ledger_generation": 70, "scan_status": "WATCH", "live_replay_performed": False},
                  "remote_ledger_reconciliation": {"status": "MATCH", "independently_authenticated": False}}
        result = bridge(integration(), actual)
        self.assertFalse(result["writer_recovery"]["delivery_projection_ready"])
        self.assertEqual(result["writer_recovery"]["delivery_blocker"], "D_REMOTE_READBACK_NOT_INDEPENDENTLY_AUTHENTICATED")

    def test_independently_authenticated_writer_is_separate_from_a2(self):
        verified = {**readback(), "status": "VERIFIED_REMOTE_READBACK",
                    "independently_authenticated": True}
        result = bridge(integration(), verified)
        self.assertTrue(result["writer_recovery"]["independently_authenticated"])
        self.assertFalse(result["same_run_or_candidate_parity_claimed"])


if __name__ == "__main__":
    unittest.main()
