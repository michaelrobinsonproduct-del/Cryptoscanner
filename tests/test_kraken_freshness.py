import datetime as dt
import math
import unittest
from simple_scanner.scan import ohlc_is_fresh

class KrakenFreshnessTests(unittest.TestCase):
    def test_ohlc_boundaries_and_invalid(self):
        now = dt.datetime.fromtimestamp(2000000000, tz=dt.timezone.utc)
        for age, valid in [(0, True), (899, True), (900, True), (901, False), (-1, False)]:
            with self.subTest(age=age):
                self.assertEqual(ohlc_is_fresh(now.timestamp()-age, now), valid)
        for value in ('nan', 'inf', '-inf', 'not-a-number', None):
            with self.subTest(value=value):
                self.assertFalse(ohlc_is_fresh(value, now))

if __name__ == '__main__':
    unittest.main()
