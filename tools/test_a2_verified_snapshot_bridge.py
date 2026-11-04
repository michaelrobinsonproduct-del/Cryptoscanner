import unittest
from tools.a2_verified_snapshot_bridge import assess_verified_a2


def snapshot():
    return {"receipt_sha256": "a" * 64, "scan_status": "WATCH",
            "snapshot_age_seconds": 8.3,
            "quote_age_seconds": {"XBTUSD": 7.2},
            "watch": [{"pair": "XBTUSD", "rank": 1, "status": "PAPER_WATCH",
                       "buy_approved": False,
                       "quote_timestamp_semantics": "client_observed_not_exchange_event_time"}]}


class A2BridgeTests(unittest.TestCase):
    def test_paper_watch_not_live_certified(self):
        verdict = assess_verified_a2(snapshot())
        self.assertTrue(verdict["accepted"])
        self.assertEqual(verdict["paper_watch_count"], 1)
        self.assertFalse(verdict["live_watch_certified"])

    def test_stablecoin_rejected(self):
        s = snapshot()
        s["watch"][0]["pair"] = "USDTUSD"
        s["quote_age_seconds"] = {"USDTUSD": 7.2}
        self.assertIn("stablecoin_pair", assess_verified_a2(s)["errors"])

    def test_expired_quote(self):
        s = snapshot()
        s["quote_age_seconds"]["XBTUSD"] = 601
        self.assertIn("quote_expired", assess_verified_a2(s)["errors"])

    def test_quote_semantics_not_promoted(self):
        s = snapshot()
        s["watch"][0]["quote_timestamp_semantics"] = "exchange_event_time"
        self.assertIn("unexpected_quote_semantics", assess_verified_a2(s)["errors"])

    def test_abstain(self):
        s = snapshot()
        s.update(scan_status="ABSTAIN_NO_QUALIFIED_OHLC", watch=[], quote_age_seconds={})
        self.assertEqual(assess_verified_a2(s)["status"], "PAPER_ABSTAIN")

    def test_missing_quote_coverage(self):
        s = snapshot()
        s["quote_age_seconds"] = {}
        self.assertIn("invalid_quote_age_coverage", assess_verified_a2(s)["errors"])


if __name__ == "__main__":
    unittest.main()
