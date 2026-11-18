import json
import unittest
from paper_pov.historical_coarse_discovery import inspect, discover, START, STEP, prioritized_windows
class CoarseDiscoveryTest(unittest.TestCase):
    def test_completed_future_bar_only_and_reuse(self):
        def row(t,high,close):
            return [int(t.timestamp()),"100",str(high),"90",str(close),"100","1",1]
        raw=json.dumps({"error":[],"result":{"TESTUSD":[row(START,100,100),
          row(START+STEP,135,110),row(START+2*STEP,300,100)],"last":1}}).encode()
        x=inspect("TESTUSD",raw)
        self.assertEqual(x["observed_bars_in_window"],2)
        self.assertEqual(len(x["events"]),1)
        self.assertAlmostEqual(x["events"][0]["observed_coarse_excursion"],.35)
        a=discover(["TESTUSD"],budget=1,fetch_page=lambda p:raw,pause=lambda _:None)
        b=discover(["TESTUSD"],prior=a,budget=1,fetch_page=lambda p:self.fail("Refetched completed discovery"),pause=lambda _:None)
        self.assertEqual(prioritized_windows(a),prioritized_windows(b))
        self.assertFalse(b["production_applied"])
    def test_current_uncommitted_bar_not_discovered(self):
        raw=json.dumps({"error":[],"result":{"TESTUSD":[[int(START.timestamp()),"100","100","90","100","100","1",1],
              [int((START+STEP).timestamp()),"100","1000","90","100","100","1",1]],"last":1}}).encode()
        self.assertEqual(inspect("TESTUSD",raw)["events"],[])
