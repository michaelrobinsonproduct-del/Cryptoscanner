"""Offline adversarial tests for prospective Kraken receipt and event provenance."""
import json
import unittest
from research.kraken_prospective_provenance import capture


class CaptureTests(unittest.TestCase):
    def make(self, *, bid_time=1700000000, ask_time=1700000000,
             trade_time=1700000000, ask_price="101", bid_price="100", pair="XXBTZUSD"):
        depth = {"error": [], "result": {pair: {"bids": [[bid_price, "2", bid_time]],
                                                  "asks": [[ask_price, "3", ask_time]]}}}
        trades = {"error": [], "result": {pair: [["100", "0.5", trade_time, "b", "l", ""]], "last": "42"}}
        responses = [json.dumps(depth).encode(), json.dumps(trades).encode()]
        clock = iter([1700000010.0, 1700000010.1, 1700000011.0, 1700000011.1])
        return lambda _: responses.pop(0), lambda: next(clock)

    def test_valid_point_in_time_capture(self):
        transport, clock = self.make()
        r = capture(transport=transport, clock=clock)
        self.assertTrue(r["eligible_point_in_time_snapshot"])
        self.assertEqual(r["spread"], "1")
        self.assertEqual(r["authenticated_first_entry_episodes"], 0)
        self.assertFalse(r["historical_first_observed_recovered"])
        self.assertIsNone(r["held_out_lift"])
        self.assertEqual(len(r["depth_receipt"]["sha256"]), 64)

    def test_stale_bid_fails_closed(self):
        transport, clock = self.make(bid_time=1699999000)
        self.assertFalse(capture(transport=transport, clock=clock)["eligible_point_in_time_snapshot"])

    def test_stale_trade_fails_closed(self):
        transport, clock = self.make(trade_time=1699999000)
        self.assertFalse(capture(transport=transport, clock=clock)["eligible_point_in_time_snapshot"])

    def test_future_event_rejected(self):
        transport, clock = self.make(ask_time=1700000020)
        with self.assertRaisesRegex(ValueError, "future event"):
            capture(transport=transport, clock=clock)

    def test_crossed_book_rejected(self):
        transport, clock = self.make(ask_price="99")
        with self.assertRaisesRegex(ValueError, "crossed"):
            capture(transport=transport, clock=clock)

    def test_market_mismatch_rejected(self):
        responses = [json.dumps({"error": [], "result": {"A": {"bids": [["1", "1", 1]], "asks": [["2", "1", 1]]}}}).encode(),
                     json.dumps({"error": [], "result": {"B": [["1", "1", 1]], "last": "1"}}).encode()]
        clock = iter([10, 10.1, 11, 11.1])
        with self.assertRaisesRegex(ValueError, "market mismatch"):
            capture(transport=lambda _: responses.pop(0), clock=lambda: next(clock))

    def test_untrusted_pair_rejected_before_network(self):
        with self.assertRaisesRegex(ValueError, "invalid pair"):
            capture("XBTUSD&foo=1", transport=lambda _: self.fail("network called"))

    def test_latency_above_ten_seconds_rejected(self):
        transport, _ = self.make()
        clock = iter([1700000000, 1700000011])
        with self.assertRaisesRegex(ValueError, "latency"):
            capture(transport=transport, clock=lambda: next(clock))

    def test_api_error_rejected(self):
        with self.assertRaisesRegex(ValueError, "API error"):
            capture(transport=lambda _: b'{"error":["EQuery:Unknown asset pair"],"result":{}}', clock=lambda: 10)

    def test_missing_book_timestamp_rejected(self):
        _, clock = self.make()
        bad = {"error": [], "result": {"XXBTZUSD": {"bids": [["100", "2"]], "asks": [["101", "3", 1700000000]]}}}
        responses = [json.dumps(bad).encode(), json.dumps({"error": [], "result": {"XXBTZUSD": [["100", "1", 1700000000]], "last": "1"}}).encode()]
        with self.assertRaisesRegex(ValueError, "lacks exchange level timestamps"):
            capture(transport=lambda _: responses.pop(0), clock=clock)


if __name__ == "__main__":
    unittest.main()
