import json
from datetime import datetime,timedelta,timezone
from pathlib import Path
import tempfile
import unittest
from paper_pov.post_q3_observed_recovery import recover_snapshots


class PostQ3RecoveryTest(unittest.TestCase):
    def test_duplicate_snapshots_deduplicate_without_inventing_market_coverage(self):
        start=datetime(2026,10,2,tzinfo=timezone.utc)
        rows=[dict(pair="TESTUSD",timestamp_utc=(start+timedelta(minutes=5*i)).isoformat(),
                   close=100,high=135 if i==24 else 100,volume=10,trades=5)
              for i in range(25)]
        payload=dict(schema="kraken_ohlc_observations_v1",source_authenticated=False,
                     results=[dict(pair="TESTUSD",response_sha256="a"*64,candles=rows)])
        with tempfile.TemporaryDirectory() as tmp:
            root=Path(tmp)
            paths=[]
            for run in ("1","2"):
                path=root/run/"kraken-candles.json"
                path.parent.mkdir()
                path.write_text(json.dumps(payload))
                paths.append(path)
            result=recover_snapshots(paths,end_utc=(start+timedelta(hours=2)).isoformat(),
                                     cohort_path=root/"cohorts.gz")
            self.assertEqual(result["observed_candles"],25)
            self.assertEqual(result["per_horizon"]["1"]["hits"],1)
            self.assertEqual(result["coverage_scope"],"PARTIAL_PREDICTION_SELECTED_NOT_MARKET_WIDE")
            self.assertFalse(result["source_authenticated"])
            payload["results"][0]["candles"][0]["close"]=99
            paths[1].write_text(json.dumps(payload))
            with self.assertRaisesRegex(ValueError,"rewritten"):
                recover_snapshots(paths,end_utc=(start+timedelta(hours=2)).isoformat(),
                                  cohort_path=root/"cohorts.gz")


if __name__=="__main__":
    unittest.main()
