"""DEX source isolation and minimum-liquidity regression checks."""
import json
import os
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch
from simple_scanner import dex

class DexTests(unittest.TestCase):
    def test_partial_source_failure_preserves_verified_research(self):
        sample={"pairs":[{"chainId":"solana","pairAddress":"valid","baseToken":{"symbol":"ABC"},"liquidity":{"usd":50000},"volume":{"h24":200000},"priceChange":{"h1":3}},{"chainId":"base","pairAddress":"illiquid","liquidity":{"usd":100},"volume":{"h24":200000}}]}
        with tempfile.TemporaryDirectory() as tmp:
            def source(query):
                if query=="base":raise TimeoutError("provider timeout")
                return sample
            with patch.object(dex,"fetch",side_effect=source),patch.dict(os.environ,{"SIMPLE_SCANNER_DATA_DIR":tmp}):
                dex.main()
            report=json.loads((Path(tmp)/"dex_latest.json").read_text())
            self.assertFalse(report["buy_approved"])
            self.assertEqual(len(report["candidates"]),1)
            self.assertEqual(len(report["errors"]),1)
            self.assertEqual(report["scope"],"sampled_search_not_full_dex_universe")
    def test_total_failure_does_not_publish(self):
        with tempfile.TemporaryDirectory() as tmp:
            with patch.object(dex,"fetch",side_effect=TimeoutError("offline")),patch.dict(os.environ,{"SIMPLE_SCANNER_DATA_DIR":tmp}):
                with self.assertRaisesRegex(RuntimeError,"All DEX discovery sources failed"):dex.main()
            self.assertFalse((Path(tmp)/"dex_latest.json").exists())
