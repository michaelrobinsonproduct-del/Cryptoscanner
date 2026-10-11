"""Mocked Kraken regression: ranking and early discovery must not regress."""
import datetime as dt
import json
import os
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch
from simple_scanner import scan

class ScanTests(unittest.TestCase):
    def test_32_screened_12_selected_and_outside_top12_promoted(self):
        now=int(dt.datetime.now(dt.timezone.utc).timestamp())
        pairs={f"COIN{i}USD":{"status":"online","wsname":f"COIN{i}/USD","base":f"COIN{i}"} for i in range(60)}
        ticker={p:{"c":["1"],"b":["0.999"],"a":["1.001"],"o":str(1/(1+(60-i)*.001)),"v":["1000000","1000000"]} for i,p in enumerate(pairs)}
        def fake_get(path):
            if path=="AssetPairs":return pairs
            if path.startswith("Ticker"):return ticker
            if path.startswith("OHLC"):
                pair=path.split("pair=")[1].split("&")[0]
                i=int(pair.removeprefix("COIN").removesuffix("USD"))
                values=[1.0]*14
                if i==15:values[-2]=1.2
                bars=[[now-70*60+j*300,"1","1","1",str(values[j]),"1","100"] for j in range(14)]
                return {pair:bars,"last":now}
            raise AssertionError(path)
        with tempfile.TemporaryDirectory() as tmp:
            cwd=os.getcwd()
            try:
                os.chdir(tmp)
                with patch.object(scan,"get",side_effect=fake_get),patch.object(scan.time,"sleep",return_value=None):
                    scan.main()
                result=json.loads(Path("simple_scanner/output/latest.json").read_text())
                self.assertEqual(result["ohlc_screened"],32)
                self.assertEqual(len(result["watch"]),12)
                self.assertEqual(result["validated_watch"],12)
                self.assertEqual(len({x["pair"] for x in result["watch"]}),12)
                self.assertTrue(all(x["early_signal_score"] is not None for x in result["watch"]))
                self.assertTrue(all(x["research_rank"]==j for j,x in enumerate(result["watch"],1)))
                self.assertIn("COIN15USD",[x["pair"] for x in result["watch"]])
                self.assertFalse(result["buy_approved"])
            finally:
                os.chdir(cwd)
