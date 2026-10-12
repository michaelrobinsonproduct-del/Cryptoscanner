"""Regression tests for scanner coverage and safe failure behavior."""
import datetime as dt
import json
import os
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch
from simple_scanner import scan

class CoverageTests(unittest.TestCase):
    def test_rejects_partial_ticker_coverage(self):
        pairs={f"C{i}USD":{"status":"online","wsname":f"C{i}/USD","base":f"C{i}"} for i in range(100)}
        ticker={p:{"c":["1"],"b":["0.99"],"a":["1.01"],"o":"0.99","v":["1000000","1000000"]} for p in list(pairs)[:20]}
        def fake_get(path):
            if path=="AssetPairs":return pairs
            if path.startswith("Ticker"):return ticker
            raise AssertionError("OHLC must not be requested with inadequate ticker coverage")
        with tempfile.TemporaryDirectory() as tmp:
            previous=os.getcwd()
            try:
                os.chdir(tmp)
                with patch.object(scan,"get",side_effect=fake_get):
                    with self.assertRaisesRegex(RuntimeError,"Insufficient eligible-pair ticker coverage"):
                        scan.main()
            finally:
                os.chdir(previous)

    def test_never_approves_buy_from_research_scan(self):
        pairs={f"C{i}USD":{"status":"online","wsname":f"C{i}/USD","base":f"C{i}"} for i in range(60)}
        ticker={p:{"c":["1"],"b":["0.999"],"a":["1.001"],"o":"0.99","v":["1000000","1000000"]} for p in pairs}
        now=int(dt.datetime.now(dt.timezone.utc).timestamp())
        def fake_get(path):
            if path=="AssetPairs":return pairs
            if path.startswith("Ticker"):return ticker
            if path.startswith("OHLC"):
                p=path.split("pair=")[1].split("&")[0]
                return {p:[[now-70*60+i*300,"1","1","1","1","1","100"] for i in range(14)],"last":now}
            raise AssertionError(path)
        with tempfile.TemporaryDirectory() as tmp:
            previous=os.getcwd()
            try:
                os.chdir(tmp)
                with patch.object(scan,"get",side_effect=fake_get),patch.object(scan.time,"sleep",return_value=None):
                    scan.main()
                report=json.loads(Path("simple_scanner/output/latest.json").read_text())
                self.assertFalse(report["buy_approved"])
                self.assertEqual(report["status"],"RESEARCH_ONLY")
                self.assertEqual(report["matched_tickers"],60)
            finally:
                os.chdir(previous)
