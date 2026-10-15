"""Isolated end-to-end smoke test: synthetic Kraken responses, temporary history, cached DEX."""
import contextlib
import datetime as dt
import io
import json
import os
from pathlib import Path
import tempfile
import unittest
from unittest.mock import patch

from simple_scanner import scan, history, shadow_learning, dex_guard

class ScannerIntegration(unittest.TestCase):
    def test_scan_history_shadow_and_dex_without_network_or_production_storage(self):
        now=dt.datetime.now(dt.timezone.utc)
        pairs={f"P{i}":{"status":"online","wsname":f"C{i}/USD","base":f"C{i}"} for i in range(60)}
        tickers={}
        for i in range(60):
            price=1.02 if i==0 else 1.0
            tickers[f"P{i}"]={"c":[str(price)],"b":[str(price)],"a":[str(price*1.001)],"o":["1"],"v":["0","1000000"]}
        # 14 bars; last is unfinished and is excluded by the scanner.
        candles=[]
        for j in range(14):
            t=(now-dt.timedelta(minutes=65-5*j)).timestamp()
            close=1.0+0.002*j
            candles.append([t,"0","0","0",str(close),"0","100","0"])
        def fake_get(path):
            if path=="AssetPairs": return pairs
            if path=="Ticker" or path.startswith("Ticker?pair="): return tickers
            if path.startswith("OHLC?"): return {"P0":candles,"last":int(now.timestamp())}
            raise AssertionError("Unexpected API path "+path)
        with tempfile.TemporaryDirectory() as folder:
            output=Path(folder)
            # Fresh DEX cache avoids external network requests.
            (output/"dex_latest.json").write_text(json.dumps({"observed_at":now.isoformat(),"candidates":[]}))
            with patch.dict(os.environ,{"SIMPLE_SCANNER_DATA_DIR":folder}),patch.object(scan,"get",side_effect=fake_get),patch.object(scan.time,"sleep",return_value=None),patch.object(history,"DATA_DIR",output),patch.object(history,"DB",output/"history.sqlite3"),patch.object(history,"LATEST",output/"latest.json"),contextlib.redirect_stdout(io.StringIO()) as captured:
                scan.main()
                report=json.loads((output/"latest.json").read_text())
                self.assertFalse(report["buy_approved"])
                self.assertEqual(report["status"],"RESEARCH_ONLY")
                self.assertTrue(report["watch"])
                self.assertTrue(all(item["risk"] in ("LOW","MEDIUM","HIGH","EXTREME") for item in report["watch"]))
                self.assertEqual([item["research_rank"] for item in report["watch"]],list(range(1,len(report["watch"])+1)))
                history.persist()
                self.assertTrue((output/"history.sqlite3").exists())
                self.assertEqual(json.loads((output/"learning.json").read_text())["history_db_integrity"],"ok")
                shadow_learning.main()
                self.assertFalse(json.loads((output/"shadow_learning.json").read_text())["buy_approved"])
                dex_guard.run()
                self.assertIn("DEX_CACHE_REUSED",captured.getvalue())
                self.assertIn("WATCH_SUMMARY",captured.getvalue())
                self.assertIn('"risk":',captured.getvalue())
if __name__=="__main__": unittest.main()
