import unittest
import json
from paper_pov.historical_trade_recovery import recover,ns


class HistoricalTradeRecoveryTests(unittest.TestCase):
    def test_resume_cursor_and_only_completed_observed_bars(self):
        start="2026-10-01T00:00:00Z"
        end="2026-10-01T02:00:00Z"
        base=ns(start)//10**9
        p1=json.dumps({"error":[],"result":{"TESTUSD":[["1","2",base+i*300+1,"b","m","",i] for i in range(13)],
                        "last":str(ns(start)+3601*10**9)}}).encode()
        p2=json.dumps({"error":[],"result":{"TESTUSD":[["1.35","2",base+i*300+1,"b","m","",i] for i in range(13,25)],
                        "last":str(ns(start)+7201*10**9)}}).encode()
        seen=[]
        def a(pair,cursor):
            seen.append(cursor)
            return p1
        state,_,summary=recover("TESTUSD",start,end,max_pages=1,fetch_page=a,pause=lambda _:None)
        self.assertFalse(summary["cursor_window_reached"])
        self.assertEqual(summary["completed_candles"],12)
        def b(pair,cursor):
            seen.append(cursor)
            return p2
        state2,cohort,summary=recover("TESTUSD",start,end,max_pages=1,previous=state,fetch_page=b,pause=lambda _:None)
        self.assertEqual(seen,[ns(start)-1,ns(start)+3601*10**9])
        self.assertTrue(summary["cursor_window_reached"])
        self.assertEqual(summary["completed_candles"],24)
        self.assertEqual(summary["per_horizon"]["1"]["hits"],1)
        self.assertFalse(summary["source_authenticated"])
        self.assertEqual(len(state2["pages"]),2)
        state2["pages"][0]["last"]+=1
        with self.assertRaisesRegex(ValueError,"checksum"):
            recover("TESTUSD",start,end,previous=state2)

if __name__=="__main__":
    unittest.main()
