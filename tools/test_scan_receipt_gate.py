import datetime as dt
import unittest

from tools.scan_receipt_gate import validate_receipt

NOW = dt.datetime(2026, 11, 3, 23, 0, tzinfo=dt.timezone.utc)


def valid():
    return {
        "source": "kraken", "status": "WATCH", "source_authenticated": True,
        "exchange_event_freshness_verified": True,
        "observed_at": "2026-11-03T22:59:00Z",
        "source_as_of": "2026-11-03T22:58:00Z",
        "candidates": [{"pair": "XBTUSD", "price": 70000,
                        "quote_at": "2026-11-03T22:58:00Z",
                        "stablecoin_excluded": True}],
    }


class GateTests(unittest.TestCase):
    def test_valid_watch_and_abstention(self):
        self.assertEqual(validate_receipt(valid(), now=NOW), [])
        r = valid()
        r.update(status="ABSTAIN", candidates=[])
        self.assertEqual(validate_receipt(r, now=NOW), [])

    def test_authentication_and_freshness_evidence(self):
        r = valid()
        r["source_authenticated"] = False
        self.assertIn("watch_without_source_authentication", validate_receipt(r, now=NOW))
        r = valid()
        r["exchange_event_freshness_verified"] = False
        self.assertIn("watch_without_exchange_freshness_evidence", validate_receipt(r, now=NOW))

    def test_quote_stale_or_future(self):
        for stamp in ("2026-11-03T22:49:00Z", "2026-11-03T23:01:00Z"):
            r = valid()
            r["candidates"][0]["quote_at"] = stamp
            self.assertIn("candidate_0_quote_not_fresh", validate_receipt(r, now=NOW))

    def test_stale_source_and_naive_observation(self):
        r = valid()
        r["source_as_of"] = "2026-11-03T22:40:00Z"
        self.assertIn("source_as_of_stale", validate_receipt(r, now=NOW))
        r = valid()
        r["observed_at"] = "2026-11-03T22:59:00"
        self.assertIn("observed_at_invalid", validate_receipt(r, now=NOW))

    def test_duplicate_and_invalid_price(self):
        r = valid()
        r["candidates"].append(dict(r["candidates"][0]))
        self.assertIn("candidate_1_duplicate_pair", validate_receipt(r, now=NOW))
        for price in (0, -1, float("nan"), float("inf"), True, "100"):
            with self.subTest(price=price):
                r = valid()
                r["candidates"][0]["price"] = price
                self.assertIn("candidate_0_invalid_price", validate_receipt(r, now=NOW))

    def test_stablecoin_and_status_contract(self):
        r = valid()
        r["candidates"][0].pop("stablecoin_excluded")
        self.assertIn("candidate_0_stablecoin_filter_unverified", validate_receipt(r, now=NOW))
        r = valid()
        r["candidates"] = []
        self.assertIn("watch_without_candidates", validate_receipt(r, now=NOW))
        r = valid()
        r["status"] = "ABSTAIN"
        self.assertIn("abstain_with_candidates", validate_receipt(r, now=NOW))

    def test_malformed(self):
        self.assertEqual(validate_receipt(None, now=NOW), ["receipt_not_object"])
        self.assertIn("candidates_not_array", validate_receipt({**valid(), "candidates": None}, now=NOW))


if __name__ == "__main__":
    unittest.main()
