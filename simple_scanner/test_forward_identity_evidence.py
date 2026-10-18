"""Offline tests for same-scan identity evidence."""
import unittest
import tempfile
import json
from pathlib import Path
from unittest.mock import patch
from simple_scanner.historical_precursor import load_same_run_asset_pairs
from simple_scanner.historical_precursor import crypto_pair

class ForwardIdentityEvidenceTests(unittest.TestCase):
    def test_fiat_and_stablecoin_excluded_with_canonical_base(self):
        pairs={"ZGBPZUSD":{"base":"ZGBP"},"ZEURZUSD":{"base":"ZEUR"},
               "USDSUSD":{"base":"USDS"},"SOLUSD":{"base":"SOL"}}
        self.assertEqual([p for p in pairs if crypto_pair(p,pairs)],["SOLUSD"])

    def test_metadata_only_matches_exact_run(self):
        with tempfile.TemporaryDirectory() as directory:
            Path(directory, "latest.json").write_text(json.dumps({
                "completed_at": "2026-10-18T16:00:00+00:00",
                "asset_pairs": {"SOLUSD": {"base": "SOL"}}}))
            with patch.dict("os.environ", {"SIMPLE_SCANNER_DATA_DIR": directory}):
                self.assertIsNone(load_same_run_asset_pairs("2026-10-18T15:59:59+00:00"))
                self.assertEqual(load_same_run_asset_pairs("2026-10-18T16:00:00+00:00")["SOLUSD"]["base"], "SOL")

if __name__=="__main__":
    unittest.main()
