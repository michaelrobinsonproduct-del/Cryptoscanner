"""Offline contracts for frozen read-only Q3 challenger prospective integration."""
import copy
import datetime as dt
import json
import unittest
from pathlib import Path

from paper_pov.frozen_historical_shadow import (
    frozen_model, features_at_entry, observed_close_label,
    prospectively_evaluate,
)

UTC=dt.timezone.utc
START=dt.datetime(2026,11,1,tzinfo=UTC)


def observations(n=650):
    rows=[]
    for i in range(n):
        t=START+dt.timedelta(minutes=5*i)
        rows.append((t, {"pair":"AAAUSD","timestamp_utc":t.isoformat(),
                         "close":10., "high":10., "volume":2000.,
                         "trades":20}))
    return rows


class FrozenHistoricalShadowTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.model=json.loads(Path("historical/evidence/q3_2026_frozen_shadow_v1.json").read_text())

    def test_real_historical_model_digest_and_read_only(self):
        model=frozen_model(self.model)
        self.assertEqual(model["train_complete"],5273)
        self.assertEqual(model["train_positive"],67)
        broken=copy.deepcopy(self.model)
        broken["training"]["weights"]["volatility_60m"]+=1
        with self.assertRaisesRegex(ValueError,"digest"):
            frozen_model(broken)
        unauthorized=copy.deepcopy(self.model)
        unauthorized["promotion_authorized"]=True
        with self.assertRaises(ValueError):
            frozen_model(unauthorized)

    def test_asof_cannot_include_future_candles(self):
        rows=observations(40)
        entry=rows[20][0]+dt.timedelta(seconds=10)
        before=features_at_entry(rows,entry)
        self.assertIsNotNone(before)
        changed=copy.deepcopy(rows)
        changed[25][1]["close"]=120
        self.assertEqual(before,features_at_entry(changed,entry))
        self.assertIsNone(features_at_entry(rows,START+dt.timedelta(minutes=5)))

    def test_real_48h_close_target_only_on_complete_forward_intervals(self):
        rows=observations(650)
        entry=rows[25][0]
        self.assertEqual(observed_close_label(rows,entry,10.,48,
             entry+dt.timedelta(hours=49)),0.)
        future=copy.deepcopy(rows)
        future[600][1]["close"]=13.5
        self.assertGreaterEqual(observed_close_label(future,entry,10.,48,
             entry+dt.timedelta(hours=49)),.30)
        broken=future[:40]+future[41:]
        self.assertIsNone(observed_close_label(broken,entry,10.,48,
             entry+dt.timedelta(hours=49)))
        self.assertIsNone(observed_close_label(future,entry,10.,48,
             entry+dt.timedelta(hours=24)))

    def test_prospective_score_is_not_promoted_and_uses_same_matured_scan(self):
        rows=observations(650)
        data={"schema":"kraken_ohlc_observations_v1",
              "results":[{"pair":"AAAUSD","candles":[c for _,c in rows]}]}
        entry=rows[25][0]
        ledger={"predictions":[{"prediction_id":"one","run_id":"run1",
              "pair":"AAAUSD","as_of":entry.isoformat(),"price":10.,
              "baseline_score":75.}]}
        x=prospectively_evaluate(ledger,data,self.model,
                    evaluated_at_utc=(entry+dt.timedelta(hours=49)).isoformat())
        self.assertEqual(x["eligible_scored_watchs"],1)
        self.assertEqual(x["paired_complete_scan_count"],1)
        self.assertEqual(x["baseline_hits30"],0)
        self.assertFalse(x["production_applied"])
        self.assertFalse(x["measured_lift_verified"])
        self.assertFalse(x["source_authenticated"])


if __name__=="__main__":
    unittest.main()
