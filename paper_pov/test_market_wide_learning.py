import unittest
from datetime import datetime, timedelta, timezone
from .market_wide_learning import build_market_cohort

class MarketWideLearningTest(unittest.TestCase):
    def test_unselected_market_and_negative_control(self):
        start = datetime(2026, 1, 1, tzinfo=timezone.utc)
        candles = []
        for pair in ("GAINUSD", "FLATUSD", "EXCLUDED"):
            for i in range(601):
                close = 100 if pair != "GAINUSD" or i < 24 else 135
                candles.append(dict(pair=pair, timestamp_utc=(start+timedelta(minutes=5*i)).isoformat(), close=close, high=close))
        result = build_market_cohort(candles, eligible_pairs=["GAINUSD","FLATUSD"], evaluation_asof_utc=(start+timedelta(hours=50)).isoformat())
        self.assertEqual(result["observed_pairs"], ["FLATUSD","GAINUSD"])
        outcomes = result["outcomes"]
        self.assertTrue(any(x["pair"]=="GAINUSD" and x["hit"] is True for x in outcomes))
        self.assertTrue(any(x["pair"]=="FLATUSD" and x["hit"] is False for x in outcomes))
        self.assertFalse(result["production_applied"])
        self.assertFalse(result["source_authenticated"])

    def test_recent_short_horizon_and_unobserved_pair(self):
        start = datetime(2026, 1, 1, tzinfo=timezone.utc)
        candles = []
        for i in range(25):
            close = 100 if i < 24 else 135
            candles.append(dict(pair="GAINUSD", timestamp_utc=(start+timedelta(minutes=5*i)).isoformat(), close=close, high=close))
        result = build_market_cohort(candles, eligible_pairs=["GAINUSD", "MISSINGUSD"], evaluation_asof_utc=(start+timedelta(hours=2)).isoformat())
        self.assertEqual(result["missing_eligible_pairs"], ["MISSINGUSD"])
        self.assertEqual(result["per_horizon"]["1"]["hits"], 1)
        for h in ("6", "24", "48"):
            self.assertEqual(result["per_horizon"][h]["immature"], 1)
            self.assertEqual(result["per_horizon"][h]["hits"], 0)

    def test_features_reuse_existing_contract_without_future_leakage(self):
        from .frozen_historical_shadow import NAMES
        start = datetime(2026, 1, 1, tzinfo=timezone.utc)
        rows = [dict(pair="GAINUSD", timestamp_utc=(start+timedelta(minutes=5*i)).isoformat(),
                     close=100 if i < 24 else 135, high=100 if i < 24 else 135,
                     volume=10+i, trades=5+i) for i in range(25)]
        kwargs = dict(eligible_pairs=["GAINUSD"], evaluation_asof_utc=(start+timedelta(hours=2)).isoformat())
        result = build_market_cohort(rows, **kwargs)
        self.assertEqual(result["feature_complete_anchors"], 1)
        self.assertEqual(set(result["anchors"][0]["features"]), set(NAMES))
        rows[-1]["close"] = rows[-1]["high"] = 150
        later = build_market_cohort(rows, **kwargs)
        self.assertEqual(result["anchors"][0]["features"], later["anchors"][0]["features"])

    def test_real_source_adapter_rotates_without_watchs_and_checks_asof_eligibility(self):
        from .market_wide_learning import run_observed_market_batch, select_market_batch
        start = datetime(2026, 1, 1, tzinfo=timezone.utc)
        at = lambda minutes: (start+timedelta(minutes=minutes)).isoformat()
        ledger = {"generation": 2, "runs": [{"id": "latest", "as_of": at(120), "observation_count": 2}],
                  "observations": [{"run_id": "older", "pair": "GAINUSD", "at": at(59)},
                                   {"run_id": "latest", "pair": "GAINUSD", "at": at(120)},
                                   {"run_id": "latest", "pair": "FLATUSD", "at": at(120)}],
                  "predictions": []}
        self.assertEqual(select_market_batch(ledger, batch_size=1)[1], ["GAINUSD"])
        def fetch(pair):
            return {"pair": pair, "source": "kraken_public_ohlc_rest", "response_sha256": "a"*64,
                    "candles": [dict(pair=pair, timestamp_utc=at(i*5), close=100 if i<24 else 135,
                                    high=100 if i<24 else 135, volume=10+i, trades=5+i)
                                for i in range(25)]}
        report = run_observed_market_batch(ledger, fetch=fetch, batch_size=1)
        self.assertEqual(report["per_horizon"]["1"]["hits"], 1)
        self.assertEqual(report["missing_eligible_pairs"], ["FLATUSD"])
        self.assertEqual(report["outcomes"][0]["source_sha256"], "a"*64)
        self.assertFalse(report["source_authenticated"])
        self.assertFalse(report["production_applied"])
        ledger["observations"].pop(0)
        report = run_observed_market_batch(ledger, fetch=fetch, batch_size=1)
        self.assertEqual(report["eligibility_abstentions"], 1)
        self.assertEqual(report["per_horizon"]["1"]["hits"], 0)

if __name__ == "__main__":
    unittest.main()
