"""DEX discovery contracts: no fake coverage, no stale/illiquid promotion."""
import datetime as dt
import unittest
from dex_discovery import discover


class DexDiscoveryTests(unittest.TestCase):
    def setUp(self):
        self.now=dt.datetime(2026,10,10,18,0,tzinfo=dt.timezone.utc)
        self.profile={"chainId":"solana","tokenAddress":"TOKEN"}
        self.pair={"chainId":"solana","pairAddress":"POOL","baseToken":{"address":"TOKEN","symbol":"TEST"},
                   "quoteToken":{"address":"USDC"},"liquidity":{"usd":50000},
                   "volume":{"h24":25000},"priceChange":{"h1":5},
                   "pairCreatedAt":int(self.now.timestamp()*1000)-3600000}
    def test_eligible_pair_research_only(self):
        def fetch(path):
            return [self.profile] if path=="/token-profiles/latest/v1" else [self.pair]
        r=discover(fetch=fetch,now=self.now)
        self.assertEqual(r["status"],"COMPLETE")
        self.assertEqual(r["eligible_pairs"],1)\n        self.assertEqual(r["candidate_count_total"],1)\n        self.assertEqual(r["rejection_counts"],{})
        self.assertEqual(r["profiles_checked"],1)
        self.assertFalse(r["entry_approved"])
        self.assertFalse(r["candidates"][0]["entry_approved"])
        self.assertEqual(r["coverage"],"SAMPLED_NEW_PROFILES_NOT_FULL_DEX")
    def test_stale_illiquid_and_wrong_chain_rejected(self):
        for changes in ({"pairCreatedAt":int(self.now.timestamp()*1000)-86400*40*1000},
                        {"liquidity":{"usd":100}},{"chainId":"ethereum"},
                        {"baseToken":{"address":"DIFFERENT"}}):
            pair={**self.pair,**changes}
            def fetch(path):
                return [self.profile] if path=="/token-profiles/latest/v1" else [pair]
            result=discover(fetch=fetch,now=self.now)\n            self.assertEqual(result["eligible_pairs"],0)\n            self.assertEqual(sum(result["rejection_counts"].values()),1)
    def test_source_failure_is_visible_and_isolated(self):
        def broken(path):raise RuntimeError("provider offline")
        r=discover(fetch=broken,now=self.now)
        self.assertEqual(r["status"],"FAILED")
        self.assertEqual(r["eligible_pairs"],0)
        self.assertFalse(r["entry_approved"])
    def test_dedupes_profiles_and_limits_requests(self):
        calls=[]
        def fetch(path):
            calls.append(path)
            return [self.profile,self.profile,self.profile] if path=="/token-profiles/latest/v1" else [self.pair]
        r=discover(fetch=fetch,now=self.now,max_tokens=1)
        self.assertEqual(r["profiles_checked"],1)
        self.assertEqual(len(calls),2)


if __name__=="__main__":
    unittest.main()
