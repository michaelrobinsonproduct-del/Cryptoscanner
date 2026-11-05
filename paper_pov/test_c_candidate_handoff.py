"""C -> B/D executable candidate handoff acceptance."""
import copy
import json
import subprocess
import sys
import unittest
from pathlib import Path
from tempfile import TemporaryDirectory
from paper_pov.c_candidate_handoff import consume, from_integration


def fixture():
    return {
        "schema": "c_a2_read_only_candidates_v1",
        "receipt_sha256": "a" * 64,
        "source_as_of": "2026-11-03T00:00:00Z",
        "source_cohort": "authenticated_snapshot_distinct_from_historical_manual_scheduled",
        "eligible_pairs": 605,
        "observed_markets": 602,
        "watch_count": 2,
        "watch": [{"pair": "XXBTZUSD", "rank": 1, "status": "PAPER_WATCH"}, {"pair": "XETHZUSD", "rank": 2, "status": "PAPER_WATCH"}],
        "status": "ABSTAIN_LEGACY_QUOTE_EVIDENCE",
        "freshness_status": "HISTORICAL_ARTIFACT_NOT_LIVE",
        "quote_timestamp_semantics": "client_observed_not_exchange_event_time",
        "live_watch_certified": False,
        "production_applied": False,
        "trading_approved": False,
    }


class HandoffTests(unittest.TestCase):
    def test_preserves_ranked_candidates_and_provenance_without_live_certification(self):
        src = fixture()
        out = consume(src)
        self.assertEqual(out["watch"], src["watch"])
        self.assertEqual(out["receipt_sha256"], src["receipt_sha256"])
        self.assertEqual(out["status"], "WATCH_REPLAY_ONLY_NOT_LIVE")
        self.assertFalse(out["live_watch_certified"])
        self.assertFalse(out["production_applied"])

    def test_integration_to_bd_roundtrip(self):
        src = fixture()
        integration = {
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
        handoff = from_integration(integration)
        self.assertEqual(handoff, src)
        handoff["watch"][0]["pair"] = "MUTATED"
        self.assertEqual(integration["a2_watch_candidates"][0]["pair"], src["watch"][0]["pair"])
        for key, bad in (("historical_artifact_parity", False),
                         ("manual_run", ""),
                         ("scheduled_run", "41636714169"),
                         ("recovery_verified", False),
                         ("a2_snapshot_attached", False),
                         ("exchange_event_freshness_verified", True),
                         ("a2_receipt_sha256", "bad"),
                         ("a2_watch_count", 3),
                         ("production_applied", True)):
            with self.subTest(key=key):
                mutated = copy.deepcopy(integration)
                mutated[key] = bad
                with self.assertRaises(ValueError):
                    from_integration(mutated)

    def test_single_invocation_writes_both_authenticated_artifacts(self):
        src = fixture()
        integration = {
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
        with TemporaryDirectory() as temp:
            root = Path(temp)
            source = root / "integration.json"
            candidates = root / "nested" / "c" / "candidates.json"
            bd = root / "nested" / "b" / "bd.json"
            source.write_text(json.dumps(integration))
            result = subprocess.run(
                [sys.executable, "-m", "paper_pov.c_candidate_handoff",
                 str(source), "--from-integration", "--output", str(candidates),
                 "--bd-output", str(bd)],
                capture_output=True, text=True, check=True)
            self.assertEqual(json.loads(candidates.read_text()), src)
            self.assertEqual(json.loads(bd.read_text()), consume(src))
            self.assertIn("WATCH_REPLAY_ONLY_NOT_LIVE", result.stdout)
            bd.unlink()
            source.write_text(json.dumps({**integration, "recovery_verified": False}))
            failed = subprocess.run(
                [sys.executable, "-m", "paper_pov.c_candidate_handoff",
                 str(source), "--from-integration", "--output", str(candidates),
                 "--bd-output", str(bd)],
                capture_output=True, text=True)
            self.assertNotEqual(failed.returncode, 0)
            self.assertFalse(bd.exists())

    def test_fail_closed_on_bad_contract(self):
        changes = [("watch_count", 3), ("observed_markets", 1),
                   ("live_watch_certified", True), ("production_applied", True),
                   ("trading_approved", True), ("freshness_status", "LIVE"),
                   ("receipt_sha256", "fake"), ("watch", []),
                   ("quote_timestamp_semantics", "exchange_event_time"),
                   ("watch", [{"pair": "XXBTZUSD", "rank": 1, "status": "PAPER_WATCH"}, {"pair": "XXBTZUSD", "rank": 2, "status": "PAPER_WATCH"}]),
                   ("watch", [{"pair": "XXBTZUSD", "rank": 1, "status": "PAPER_WATCH"}, {"pair": "XETHZUSD", "rank": 4, "status": "PAPER_WATCH"}]),
                   ("watch", [{"pair": "XXBTZUSD", "rank": 1}])]
        for key, value in changes:
            with self.subTest(key=key):
                src = copy.deepcopy(fixture())
                src[key] = value
                with self.assertRaises(ValueError):
                    consume(src)


if __name__ == "__main__":
    unittest.main()
