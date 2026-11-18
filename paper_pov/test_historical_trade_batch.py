import json
import gzip
import tempfile
import unittest
from pathlib import Path
from paper_pov.historical_trade_batch import run_batch,window_keys,verified_trade_cohorts

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
            replayed=list(verified_trade_cohorts(b))
            self.assertEqual(len(replayed),2)
            self.assertEqual(len(calls),2)
            self.assertEqual(replayed[0][1]["sampling_scope"],"EVENT_PRIORITIZED_AND_BACKGROUND_NOT_UNBIASED")
            p=b/second["records"][0]["key"]/"cursor-state.json.gz"
            p.write_bytes(p.read_bytes()+b"tampered")
            with self.assertRaisesRegex(ValueError,"checksum"):
                list(verified_trade_cohorts(b))

    def test_failed_window_has_bounded_retry_without_replacing_background(self):
        calls=[]
        def fetch(pair,cursor):
            calls.append(pair)
            start=(cursor+1)//10**9
            end=start+3*86400+60
            if pair=="AUSD" and calls.count(pair)==1:
                raise ValueError("Previously observed API error")
            return json.dumps({"error":[],"result":{pair:[["1","1",start+1,"b","m","",1],
                ["1","1",end,"b","m","",2]],"last":str(end*10**9)}}).encode()
        with tempfile.TemporaryDirectory() as tmp:
            root=Path(tmp)
            first=run_batch(["AUSD","BUSD","CUSD","DUSD","EUSD","FUSD"],root/"first",
                batch_size=1,fetch_page=fetch,pause=lambda _:None)
            self.assertEqual(len(first["failures"]),1)
            second=run_batch(["AUSD","BUSD","CUSD","DUSD","EUSD","FUSD"],root/"second",
                prior=root/"first",batch_size=4,fetch_page=fetch,pause=lambda _:None)
            self.assertEqual(second["completed_windows"],4)
            self.assertFalse(second["failures"])
            self.assertIn("BUSD",calls)
            self.assertEqual(calls.count("AUSD"),2)

if __name__=="__main__":
    unittest.main()
