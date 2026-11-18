import json
import tempfile
import unittest
from pathlib import Path
from paper_pov.historical_trade_batch import run_batch,window_keys

class HistoricalTradeBatchTest(unittest.TestCase):
    def test_completed_window_not_refetched(self):
        calls=[]
        def fetch(pair,cursor):
            calls.append((pair,cursor))
            start=(cursor+1)//10**9
            end=start+3*86400+60
            return json.dumps({"error":[],"result":{pair:[["1","1",start+1,"b","m","",1],
                ["1","1",end,"b","m","",2]],"last":str(end*10**9)}}).encode()
        with tempfile.TemporaryDirectory() as tmp:
            a,b=Path(tmp)/"a",Path(tmp)/"b"
            first=run_batch(["ACTUSD"],a,batch_size=1,fetch_page=fetch,pause=lambda _:None)
            second=run_batch(["ACTUSD"],b,prior=a,batch_size=1,fetch_page=fetch,pause=lambda _:None)
            self.assertEqual(first["completed_windows"],1)
            self.assertEqual(second["completed_windows"],2)
            self.assertEqual(len(calls),2)
            self.assertNotEqual(calls[0],calls[1])
            self.assertEqual(len(window_keys(["ACTUSD"])),12)
            self.assertFalse(second["source_authenticated"])

if __name__=="__main__":
    unittest.main()
