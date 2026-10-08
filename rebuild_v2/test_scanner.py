import unittest
from scanner import rank, confirm_watch, confirm_twice
import time

class ShadowScannerTests(unittest.TestCase):
    def test_valid_quote(self):
        t={"c":["10"],"o":"10","v":["0","10000"],"t":[0,500],"b":["9.99"],"a":["10.01"]}
        self.assertGreater(rank(t)["score"],0)
    def test_crossed_quote_rejected(self):
        t={"c":["10"],"o":"10","v":["0","10000"],"t":[0,500],"b":["10.02"],"a":["10.01"]}
        with self.assertRaises(ValueError):
            rank(t)
    def test_zero_open_rejected(self):
        t={"c":["10"],"o":"0","v":["0","10000"],"t":[0,500],"b":["9.99"],"a":["10.01"]}
        with self.assertRaises(ValueError):
            rank(t)

    def test_confirmation_stays_watch_only(self):
        now=time.time()
        def fake(endpoint):
            if endpoint.startswith("Depth?"):
                return {"XXBTZUSD":{"bids":[["100","1","1"]],"asks":[["100.1","1","1"]]}}
            return {"XXBTZUSD":[["100","1",now-10,"b","l",""]]}
        result=confirm_watch("XXBTZUSD",{},fake)
        self.assertFalse(result["entry_approved"])
        self.assertEqual(result["status"],"WATCH_CONFIRMED")
    def test_stale_trade_rejected(self):
        def fake(endpoint):
            if endpoint.startswith("Depth?"):
                return {"XXBTZUSD":{"bids":[["100","1","1"]],"asks":[["100.1","1","1"]]}}
            return {"XXBTZUSD":[["100","1",time.time()-600,"b","l",""]]}
        with self.assertRaises(ValueError):
            confirm_watch("XXBTZUSD",{},fake)

    def test_double_confirmation_never_authorizes_entry(self):
        def fake(endpoint):
            if endpoint.startswith("Depth?"):
                return {"XXBTZUSD":{"bids":[["100","1","1"]],"asks":[["100.1","1","1"]]}}
            return {"XXBTZUSD":[["100","1",time.time()-5,"b","l",""]]}
        # A deterministic time advance is needed for strictly ordered timestamps.
        result=confirm_twice("XXBTZUSD",{},fake,lambda _: time.sleep(0.01))
        self.assertEqual(result["status"],"DOUBLE_CONFIRMED_WATCH")
        self.assertFalse(result["entry_approved"])

if __name__=="__main__": unittest.main()
