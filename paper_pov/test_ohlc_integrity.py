"""Adversarial offline OHLC source-integrity tests; never use live Kraken or orders."""
import datetime as dt
import unittest

from paper_pov import scanner
from paper_pov.test_scanner import NOW, fixture


def report_with(mutate):
    """Mutate one selected market so failures remain visible as abstentions."""
    def api(path):
        response = fixture()(path)
        if path.startswith("OHLC?") and "pair=C0USD&" in path:
            return mutate(response, "C0USD")
        return response
    return scanner.scan(api=api, clock=lambda: NOW, sleep=lambda _: None)


def change_candle(index, field, value):
    def change(response, pair):
        response[pair][index][field] = value
        return response
    return change


class CompletedOHLCIntegrityTests(unittest.TestCase):
    def assert_abstains(self, mutate, reason):
        report = report_with(mutate)
        self.assertNotIn("C0USD", {p["pair"] for p in report["watch"]})
        errors = [a["reason"] for a in report["abstentions"] if a["pair"] == "C0USD"]
        self.assertEqual(len(errors), 1)
        self.assertIn(reason, errors[0])
        self.assertIs(report["production_applied"], False)
        self.assertEqual(report["forward_labels"], 0)

    def test_valid_kraken_shape_keeps_candidate(self):
        report = report_with(lambda response, pair: response)
        self.assertIn("C0USD", {p["pair"] for p in report["watch"]})
        self.assertEqual(report["forward_labels"], 0)

    def test_wrong_market_response_rejected(self):
        def change(response, pair):
            response["WRONGUSD"] = response.pop(pair)
            return response
        self.assert_abstains(change, "pair mismatch")

    def test_extra_market_response_rejected(self):
        def change(response, pair):
            response["WRONGUSD"] = response[pair]
            return response
        self.assert_abstains(change, "pair mismatch")

    def test_missing_last_cursor_rejected(self):
        def change(response, pair):
            del response["last"]
            return response
        self.assert_abstains(change, "pair mismatch")

    def test_one_second_timestamp_misalignment_rejected(self):
        def change(response, pair):
            for candle in response[pair]:
                candle[0] += 1
            return response
        self.assert_abstains(change, "unaligned OHLC timestamp")

    def test_fractional_timestamp_not_silently_truncated(self):
        def change(response, pair):
            for candle in response[pair]:
                candle[0] += 0.5
            return response
        self.assert_abstains(change, "unaligned OHLC timestamp")

    def test_duplicate_uncommitted_tail_rejected(self):
        def change(response, pair):
            response[pair][-1][0] = response[pair][-2][0]
            return response
        self.assert_abstains(change, "uncommitted OHLC tail")

    def test_high_below_close_rejected(self):
        self.assert_abstains(change_candle(0, 2, "0.5"), "invalid or no-trade")

    def test_low_above_open_rejected(self):
        self.assert_abstains(change_candle(0, 3, "1.005"), "invalid or no-trade")

    def test_vwap_outside_candle_rejected(self):
        self.assert_abstains(change_candle(0, 5, "2"), "invalid or no-trade")

    def test_zero_trade_count_is_no_trade_abstention(self):
        self.assert_abstains(change_candle(0, 7, "0"), "invalid or no-trade")

    def test_fractional_trade_count_rejected(self):
        self.assert_abstains(change_candle(0, 7, "1.5"), "invalid or no-trade")

    def test_nonfinite_high_rejected(self):
        self.assert_abstains(change_candle(0, 2, "nan"), "nonfinite")

    def test_short_ohlc_row_rejected(self):
        def change(response, pair):
            response[pair][0].pop()
            return response
        self.assert_abstains(change, "row schema")

    def test_negative_open_rejected(self):
        self.assert_abstains(change_candle(0, 1, "-1"), "invalid or no-trade")

    def test_ticker_clock_regression_fails_closed(self):
        calls = [0]
        def clock():
            calls[0] += 1
            return NOW - dt.timedelta(seconds=1) if calls[0] == 2 else NOW
        with self.assertRaisesRegex(RuntimeError, "Ticker request stale"):
            scanner.scan(api=fixture(), clock=clock, sleep=lambda _: None)

    def test_completion_clock_regression_fails_closed(self):
        calls = [0]
        def clock():
            calls[0] += 1
            return NOW - dt.timedelta(seconds=1) if calls[0] == 4 else NOW
        with self.assertRaisesRegex(RuntimeError, "Quote observations expired"):
            scanner.scan(api=fixture(), clock=clock, sleep=lambda _: None,
                         max_ohlc=1)


if __name__ == "__main__":
    unittest.main()
