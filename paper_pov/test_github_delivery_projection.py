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
