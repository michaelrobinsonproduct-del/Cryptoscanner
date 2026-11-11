"""Focused contracts for leak-free Kraken historical research."""
import unittest

from historical.kraken_q3_48h_shadow import (
    START, FIVE_MIN, parse_bar, parse_market, candidate_rows,
    outcomes_for_anchor, frozen_asof_universe, freeze_challenger, compare,
    split_for_stamp
)


def bars(price=10.0, *, start=START, length=680, volume=5000):
    return [(start + 300*i, price, float(volume), 100.)
            for i in range(length)]


class KrakenQ3ShadowTests(unittest.TestCase):
    def test_source_csv_contract_and_stablecoin_exclusion(self):
        self.assertEqual(parse_market("XBTUSD_5.csv"), "XBTUSD")
        self.assertIsNone(parse_market("USDTUSD_5.csv"))
        self.assertIsNone(parse_market("XBTUSD_60.csv"))
        self.assertEqual(parse_bar(["300", "3", "4", "2", "3.5", "2", "5"]),
                         (300, 3.5, 2.0, 5.0))
        self.assertIsNone(parse_bar(["301", "3", "4", "2", "3.5", "2", "5"]))
        self.assertIsNone(parse_bar(["300", "3", "4", "2", "5", "2", "5"]))

    def test_48h_complete_and_unfilled_gap_abstentions(self):
        b = bars()
        candidates = list(candidate_rows("XBTUSD", b))
        self.assertTrue(candidates)
        first = candidates[0]
        self.assertEqual(first["at"] % 3600, 0)
        self.assertTrue(all(first["outcomes"][str(h)] == 0 for h in (1,6,24,48)))
        missing = b[:53] + b[54:]
        rows = list(candidate_rows("XBTUSD", missing))
        first2 = rows[0]
        self.assertIsNotNone(first2["outcomes"]["1"])
        self.assertIsNone(first2["outcomes"]["6"])
        self.assertIsNone(first2["outcomes"]["48"])

    def test_future_prices_never_determine_asof_selection(self):
        a = bars(price=10, volume=30000)
        b = bars(price=20, volume=9000)
        before = frozen_asof_universe([("AAAUSD", a), ("BBBUSD", b)], top_n=1)
        changed = a[:60] + [(ts, 1000, v, tr) for ts, _, v, tr in a[60:]]
        after = frozen_asof_universe([("AAAUSD", changed), ("BBBUSD", b)], top_n=1)
        self.assertEqual(before[0]["at"], after[0]["at"])
        self.assertEqual(before[0]["pair"], after[0]["pair"])
        self.assertEqual(before[0]["features"], after[0]["features"])
        self.assertNotEqual(before[0]["outcomes"]["48"], after[0]["outcomes"]["48"])

    def test_model_fit_only_older_training_labels(self):
        from copy import deepcopy
        sample = []
        for i in range(40):
            hit = i % 2 == 0
            feat = {k: (5 if hit else -5) + i/100 for k in
                    ("momentum_5m", "momentum_15m", "momentum_60m",
                     "volume_accel", "trade_accel", "volatility_60m")}
            sample.append({"pair": str(i), "at": START + i*3600, "split": "train",
                           "features": feat, "outcomes": {"48": .31 if hit else .01}})
        model = freeze_challenger(sample)
        self.assertEqual(model["status"], "SHADOW_ONLY")
        later = deepcopy(sample)
        later.extend({"pair": "ZZZ", "at": START+50*3600, "split": "test",
                      "features": {f: 9999 for f in model["feature_names"]},
                      "outcomes": {"48": .99}} for _ in range(2))
        self.assertEqual(model, freeze_challenger(later))

    def test_identical_baseline_challenger_holdout_and_abstention(self):
        f = {k: 1.0 for k in ("momentum_5m", "momentum_15m",
             "momentum_60m", "volume_accel", "trade_accel", "volatility_60m")}
        rows = [
            {"pair": "AAAUSD", "at": START, "split": "test", "features": f,
             "outcomes": {"1":0,"6":0,"24":0,"48":None}},
            {"pair": "BBBUSD", "at": START+3600, "split": "test", "features": f,
             "outcomes": {"1":0,"6":0,"24":0,"48":.31}},
        ]
        model = {"status":"SHADOW_ONLY", "feature_names":list(f),
                 "means":{k:0 for k in f}, "scales":{k:1 for k in f},
                 "weights":{k:1 for k in f}}
        result = compare(rows,model,"test")
        for strategy in result.values():
            self.assertEqual(strategy["timestamps"],2)
            self.assertEqual(strategy["48h_abstentions"],1)
            self.assertEqual(strategy["hits30"],1)
            self.assertEqual(strategy["complete_48h"],1)

    def test_forty_eight_hour_split_embargo(self):
        import datetime as dt
        stamp = lambda day: int(dt.datetime(2026, 8, day, tzinfo=dt.timezone.utc).timestamp())
        self.assertEqual(split_for_stamp(stamp(13)), "train")
        self.assertEqual(split_for_stamp(stamp(16)), "embargo")
        self.assertEqual(split_for_stamp(stamp(18)), "validation")


if __name__ == "__main__":
    unittest.main()
