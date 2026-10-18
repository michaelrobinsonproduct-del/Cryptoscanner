"""Regression evidence from actual Railway SHADOW_LEARNING log (2026-10-18).

The reported ranked candidates are real production outputs, NOT raw SQLite
observations or an authoritative Kraken AssetPairs identity ledger.
This verifies exclusion only; it must never satisfy the release replay gate.
"""
import unittest
from simple_scanner.historical_precursor import crypto_pair
from simple_scanner.shadow_learning import early_accumulation_rank

# Railway kraken-simple-validation deploy logs, observed 2026-10-18T16:30:16Z.
# Each tuple is (pair, logged score, logged recent move %, spread bps, notional USD).
PRODUCTION_LOG_CANDIDATES = (
    ("ZGBPZUSD",67.071,0.0128,0.900,3092706.04),
    ("ZEURZUSD",66.899,-0.0053,0.267,8540105.30),
)

class ProductionLogRegressionTests(unittest.TestCase):
    def test_actual_fiat_pairs_excluded_by_canonical_identity(self):
        # Independent metadata is required for real-history release evidence.
        # Here the canonical base names are known fiat symbols, solely to
        # verify the regression without claiming archival provenance.
        identity = {"ZGBPZUSD":{"base":"ZGBP"},
                    "ZEURZUSD":{"base":"ZEUR"}}
        for pair,score,recent,spread,notional in PRODUCTION_LOG_CANDIDATES:
            with self.subTest(pair=pair):
                self.assertFalse(crypto_pair(pair,identity))
                current=100*(1+recent/100)
                rows=[(pair,0.0,spread,notional,100.0,current)]
                self.assertEqual(early_accumulation_rank(rows,asset_pairs=identity),[])
        self.assertEqual(len(PRODUCTION_LOG_CANDIDATES),2)

if __name__=="__main__":
    unittest.main()
