import unittest

from tools.c_integration_receipt_bridge import assess_c_integration


def report():
    return {
        "schema": "c_read_only_integration_v1",
        "production_applied": False,
        "trading_approved": False,
        "exchange_event_freshness_verified": False,
        "status": "ABSTAIN_LEGACY_QUOTE_EVIDENCE",
        "historical_artifact_parity": True,
        "recovery_verified": True,
        "a2_snapshot_attached": True,
        "a2_receipt_sha256": "a" * 64,
        "a2_watch_count": 12,
        "a2_source_cohort": "authenticated_snapshot_distinct_from_historical_manual_scheduled",
    }


class BridgeTests(unittest.TestCase):
    def test_real_schema_remains_abstention(self):
        result = assess_c_integration(report())
        self.assertTrue(result["accepted"])
        self.assertFalse(result["live_watch_certified"])
        self.assertEqual(result["status"], "ABSTAIN_LEGACY_QUOTE_EVIDENCE")

    def test_freshness_claim_does_not_promote(self):
        r = report()
        r["exchange_event_freshness_verified"] = True
        self.assertFalse(assess_c_integration(r)["accepted"])

    def test_bad_digest_and_count(self):
        r = report()
        r["a2_receipt_sha256"] = "not-a-digest"
        r["a2_watch_count"] = True
        verdict = assess_c_integration(r)
        self.assertIn("invalid_a2_receipt_digest", verdict["errors"])
        self.assertIn("invalid_a2_watch_count", verdict["errors"])

    def test_unrecovered_and_production(self):
        r = report()
        r["recovery_verified"] = False
        r["production_applied"] = True
        self.assertFalse(assess_c_integration(r)["accepted"])

    def test_wrong_schema(self):
        self.assertEqual(assess_c_integration({})["status"], "INVALID_REPORT")


if __name__ == "__main__":
    unittest.main()
