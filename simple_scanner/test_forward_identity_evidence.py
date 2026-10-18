"""Offline tests for same-scan identity evidence."""
import unittest
from simple_scanner.historical_precursor import crypto_pair

class ForwardIdentityEvidenceTests(unittest.TestCase):
    def test_fiat_and_stablecoin_excluded_with_canonical_base(self):
        pairs={"ZGBPZUSD":{"base":"ZGBP"},"ZEURZUSD":{"base":"ZEUR"},
               "USDSUSD":{"base":"USDS"},"SOLUSD":{"base":"SOL"}}
        self.assertEqual([p for p in pairs if crypto_pair(p,pairs)],["SOLUSD"])

if __name__=="__main__":
    unittest.main()
