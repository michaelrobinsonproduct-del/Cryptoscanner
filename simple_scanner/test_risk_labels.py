"""Risk label regression checks. Run: python -m unittest simple_scanner.test_risk_labels"""
import unittest
from simple_scanner.risk_labels import assess_risk

BASE = {"status": "WATCH_RESEARCH_ONLY", "spread_bps": 5,
        "notional_24h_usd": 50000000, "move_15m_pct": 0.1,
        "move_60m_pct": 0.5, "volume_accel": 1.2}

class RiskTests(unittest.TestCase):
    def test_low(self):
        self.assertEqual(assess_risk(BASE)["risk"], "LOW")
    def test_medium(self):
        self.assertEqual(assess_risk({**BASE, "spread_bps": 30})["risk"], "MEDIUM")
    def test_high(self):
        self.assertEqual(assess_risk({**BASE, "move_15m_pct": -6})["risk"], "HIGH")
    def test_extreme(self):
        self.assertEqual(assess_risk({**BASE, "notional_24h_usd": 120000})["risk"], "EXTREME")
    def test_missing(self):
        candidate = dict(BASE)
        del candidate["spread_bps"]
        self.assertEqual(assess_risk(candidate)["risk"], "UNASSESSED")
    def test_unverified(self):
        self.assertEqual(assess_risk({**BASE, "status": "UNVERIFIED"})["risk"], "UNASSESSED")
    def test_nonfinite(self):
        self.assertEqual(assess_risk({**BASE, "volume_accel": float("inf")})["risk"], "UNASSESSED")
    def test_immutable(self):
        candidate = dict(BASE)
        assess_risk(candidate)
        self.assertEqual(candidate, BASE)

if __name__ == "__main__":
    unittest.main()
