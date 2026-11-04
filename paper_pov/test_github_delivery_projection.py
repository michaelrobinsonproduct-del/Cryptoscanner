import unittest
from paper_pov.github_delivery_projection import project_delivery

SHA = "a" * 40
BASE = {"source_run_id": 123, "source_sha": SHA,
        "watch_delivery_authorized": False, "publisher_authenticated": False}


class DeliveryProjectionTests(unittest.TestCase):
    def test_sealed_historical_readback_never_becomes_live_watch(self):
        report = {"watch": [{"pair": "TAOUSD", "rank": 1}], "eligible_pairs": 605,
                  "matched_tickers": 605, "observed_markets": 602, "ohlc_screened": 600}
        transport = {**BASE, "sealed": True,
                     "bundle": {"schema": "paper_sealed_bundle_v1",
                                "receipt_json": __import__("json").dumps(report),
                                "candidate_snapshot": {"watch": report["watch"]}}}
        projected = project_delivery(transport)
        self.assertEqual(projected["historical_watch_count"], 1)
        self.assertEqual(projected["historical_coverage"]["observed_markets"], 602)
        self.assertEqual(projected["live_watch"], [])
        self.assertFalse(projected["live_watch_authorized"])
        self.assertTrue(projected["single_writer_read_only"])

    def test_checksum_only_legacy_exposes_no_unverified_watch(self):
        result = project_delivery({**BASE, "sealed": False,
                                   "artifact_status": "CHECKSUM_VERIFIED_LEGACY_NO_RECEIPT",
                                   "scoreboard": {"watch_count": 12}})
        self.assertEqual(result["status"], "LEGACY_CHECKSUM_ONLY")
        self.assertIsNone(result["historical_watch_count"])
        self.assertEqual(result["live_watch"], [])

    def test_inconsistent_sealed_candidate_projection_rejected(self):
        import json
        transport = {**BASE, "sealed": True,
                     "bundle": {"schema": "paper_sealed_bundle_v1",
                                "receipt_json": json.dumps({"watch": [{"pair": "TAOUSD"}]}),
                                "candidate_snapshot": {"watch": []}}}
        with self.assertRaisesRegex(ValueError, "inconsistent"):
            project_delivery(transport)

    def test_d_writer_recovery_reconciliation_is_separate_historical_cohort(self):
        base = {**BASE, "sealed": False, "artifact_status": "CHECKSUM_VERIFIED_LEGACY_NO_RECEIPT", "scoreboard": {}}
        recovery = {"status": "WRITER_CHECKSUM_ONLY", "remote_downloaded": True,
                    "ledger_writer_invoked": False, "production_applied": False,
                    "independently_authenticated": False, "run_id": "456", "source_sha": "b"*40,
                    "persisted_paper": {"ledger_generation": 7, "scan_status": "ABSTAIN_STALE",
                                        "live_replay_performed": False},
                    "remote_ledger_reconciliation": {"status": "UNAVAILABLE",
                        "reason": "REMOTE_LEDGER_QUERY_FAILED",
                        "independently_authenticated": False, "production_applied": False}}
        result = project_delivery(base, recovery)
        self.assertEqual(result["writer_reconciliation_status"], "UNAVAILABLE")
        self.assertEqual(result["writer_recovery"]["ledger_generation"], 7)
        self.assertEqual(result["writer_recovery"]["source_run_id"], 456)
        self.assertFalse(result["writer_recovery"]["same_scan_as_delivery"])
        self.assertEqual(result["live_watch"], [])
        for status, remote in (("MATCH", "c"*64), ("DIVERGED", "d"*64)):
            with self.subTest(status=status):
                recovery["remote_ledger_reconciliation"] = {
                    "status": status, "recovered_sha256": "c"*64, "remote_sha256": remote,
                    "independently_authenticated": False, "production_applied": False}
                self.assertEqual(project_delivery(base, recovery)["writer_reconciliation_status"], status)
        recovery["remote_ledger_reconciliation"]["status"] = "MATCH"
        with self.assertRaisesRegex(ValueError, "digest contradiction"):
            project_delivery(base, recovery)
        recovery["remote_ledger_reconciliation"] = None
        recovery["production_applied"] = True
        with self.assertRaisesRegex(ValueError, "not read-only"):
            project_delivery(base, recovery)

    def test_existing_c_handoff_in_shared_delivery_schema(self):
        base = {**BASE, "sealed": False, "artifact_status": "CHECKSUM_VERIFIED_LEGACY_NO_RECEIPT", "scoreboard": {}}
        replay = {"schema": "c_a2_read_only_candidates_v1", "production_applied": False,
                  "trading_approved": False, "live_watch_certified": False,
                  "status": "ABSTAIN_LEGACY_QUOTE_EVIDENCE",
                  "freshness_status": "HISTORICAL_ARTIFACT_NOT_LIVE",
                  "quote_timestamp_semantics": "client_observed_not_exchange_event_time",
                  "receipt_sha256": "a"*64, "watch_count": 1,
                  "watch": [{"pair": "TAOUSD", "rank": 1, "status": "PAPER_WATCH"}],
                  "eligible_pairs": 10, "observed_markets": 8,
                  "source_as_of": "2026-10-01T00:00:00Z",
                  "source_cohort": "authenticated_snapshot_distinct_from_historical_manual_scheduled"}
        result = project_delivery(base, historical_a2=replay)
        self.assertEqual(result["historical_a2"]["watch_count"], 1)
        self.assertFalse(result["historical_a2"]["live_watch_certified"])
        self.assertEqual(result["live_watch"], [])
        replay["live_watch_certified"] = True
        with self.assertRaises(ValueError):
            project_delivery(base, historical_a2=replay)

    def test_untrusted_promotion_and_run_provenance_rejected(self):
        valid = {**BASE, "sealed": False,
                 "artifact_status": "CHECKSUM_VERIFIED_LEGACY_NO_RECEIPT", "scoreboard": {}}
        for update in ({"watch_delivery_authorized": True},
                       {"publisher_authenticated": True},
                       {"source_sha": "bad"},
                       {"source_run_id": "123"}):
            with self.subTest(update=update), self.assertRaises(ValueError):
                project_delivery({**valid, **update})


if __name__ == "__main__":
    unittest.main()
