"""Focused C2 acceptance regressions for contradictory A2 metadata."""
import unittest
from paper_pov.c_read_only_integration import combine


def evidence():
    parity = {
        "status": "FIXTURE_OR_ARTIFACT_CONTRACT_VERIFIED_NOT_LIVE_PARITY",
        "candidate_schema_parity": True, "same_source_sha": True,
        "manual_run": "1", "scheduled_run": "2",
        "manual_generation": 3, "scheduled_generation": 3,
        "manual_watch_count": 1, "scheduled_watch_count": 1,
    }
    recovery = {
        "schema": "paper_recovery_v1", "production_applied": False,
        "all_recovered": True,
        "runs": {
            name: {"run_id": run, "generation": 3, "watch": 1,
                   "certified": False, "status": "ABSTAIN_LEGACY_QUOTE_EVIDENCE"}
            for name, run in (("manual", "1"), ("scheduled", "2"))
        },
    }
    snapshot = {
        "receipt_sha256": "a" * 64, "watch": [{"pair": "BTCUSD", "rank": 1, "status": "PAPER_WATCH"}],
        "scan_status": "WATCH", "as_of": "2026-11-03T00:00:00Z",
        "eligible_pairs": 4, "observed_markets": 3,
        "abstention_counts": {"missing": 1},
    }
    return parity, recovery, snapshot


class C2CoverageContract(unittest.TestCase):
    def test_valid_coverage_is_read_only(self):
        result = combine(*evidence())
        self.assertTrue(result["a2_snapshot_attached"])
        self.assertEqual(result["a2_watch_candidates"], [{"pair": "BTCUSD", "rank": 1, "status": "PAPER_WATCH"}])
        self.assertEqual(result["a2_watch_count"], len(result["a2_watch_candidates"]))
        self.assertEqual(result["status"], "ABSTAIN_LEGACY_QUOTE_EVIDENCE")
        self.assertFalse(result["production_applied"])
        self.assertFalse(result["trading_approved"])

    def test_malformed_watch_payload_abstains(self):
        for watch in ([None], ["BTCUSD"], [[]], [{}], [42]):
            with self.subTest(watch=watch):
                p, r, s = evidence()
                s["watch"] = watch
                with self.assertRaises(ValueError):
                    combine(p, r, s)

    def test_downstream_candidate_contract_rejected_early(self):
        for watch in ([{"pair": "BTCUSD", "rank": 1, "status": "BUY"}],
                      [{"pair": "BTCUSD", "rank": True, "status": "PAPER_WATCH"}],
                      [{"pair": "BTCUSD", "rank": 2, "status": "PAPER_WATCH"}],
                      [{"pair": "", "rank": 1, "status": "PAPER_WATCH"}],
                      [{"pair": "BTCUSD", "rank": 1, "status": "PAPER_WATCH"}] * 2):
            with self.subTest(watch=watch):
                p, r, s = evidence()
                s["watch"] = watch
                with self.assertRaises(ValueError):
                    combine(p, r, s)

    def test_invalid_coverage_abstains(self):
        for key, value in (("eligible_pairs", True), ("eligible_pairs", -1),
                           ("observed_markets", 5), ("observed_markets", 0),
                           ("abstention_counts", {"missing": -1}),
                           ("abstention_counts", {"missing": True}),
                           ("abstention_counts", None), ("as_of", "")):
            with self.subTest(key=key, value=value):
                p, r, s = evidence()
                s[key] = value
                with self.assertRaises(ValueError):
                    combine(p, r, s)


if __name__ == "__main__":
    unittest.main()
