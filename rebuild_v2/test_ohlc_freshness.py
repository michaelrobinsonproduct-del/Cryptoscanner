"""Stale OHLC research data must never silently boost live rankings."""
import datetime as dt
import unittest

from scanner import historical_live_features


class CandleFreshnessTests(unittest.TestCase):
    def candles(self, age):
        now=dt.datetime.now(dt.timezone.utc).timestamp()
        # Keep the fixture on a valid five-minute boundary. An age of 360
        # means the last completed candle opened 360s ago; the incomplete
        # candle opens 300s later. Avoid clock-phase-dependent test failures.
        last_open=int(now//300)*300 + 300 - (int(age//300)*300)
        bars=[]
        for i in range(14):
            ts=last_open-(13-i)*300
            bars.append([ts,"1","1","1","1","1","100","10"])
        return {"PAIR":bars,"last":last_open}

    def test_stale_completed_candle_rejected(self):
        with self.assertRaisesRegex(ValueError,"stale or future"):
            historical_live_features("PAIR",fetch=lambda _:self.candles(1800))

    def test_current_completed_candle_accepted(self):
        features=historical_live_features("PAIR",fetch=lambda _:self.candles(300))
        self.assertEqual(features["pre_return_60m_pct"],0)

    def test_just_closed_bar_accepted(self):
        features=historical_live_features("PAIR",fetch=lambda _:self.candles(60))
        self.assertEqual(features["pre_return_60m_pct"],0)

    def test_future_candle_rejected(self):
        with self.assertRaisesRegex(ValueError,"stale or future"):
            historical_live_features("PAIR",fetch=lambda _:self.candles(-1200))


if __name__=="__main__":
    unittest.main()
