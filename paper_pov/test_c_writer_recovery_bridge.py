"""Focused C/D read-only recovered writer bridge acceptance."""
import copy
import unittest
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

    def test_independently_authenticated_writer_is_separate_from_a2(self):
        verified = {**readback(), "status": "VERIFIED_REMOTE_READBACK",
                    "independently_authenticated": True}
        result = bridge(integration(), verified)
        self.assertTrue(result["writer_recovery"]["independently_authenticated"])
        self.assertFalse(result["same_run_or_candidate_parity_claimed"])


if __name__ == "__main__":
    unittest.main()
