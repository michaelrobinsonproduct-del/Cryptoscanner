"""Adversarial as-of, leakage, missing-peer and equal-budget tests."""
import unittest
import numpy as np
import pandas as pd
from cross_sectional_regime_discovery import attach_peer_context, hypothesis_scores, evaluate

def fixture():
    rows = []
    for at, split in (("2026-02-01T00:00:00+00:00", "train"), ("2026-03-02T00:00:00+00:00", "validation"), ("2026-05-02T00:00:00+00:00", "test")):
        for i in range(8):
            rows.append(dict(at=at, date=at[:10], split=split, pair=f"T{i}USD",
                             pre_return_60m_pct=float(i - 3), pre_return_15m_pct=float(i - 2),
                             pre_return_5m_pct=float(i) / 10, trade_accel=2.,
                             volume_accel=2., volatility_pct=1., hit20=i == 7,
                             hit30=i == 7, gate_status="PASS_PRICE_PROXY"))
    return pd.DataFrame(rows)

class CrossSectionalResearchTests(unittest.TestCase):
    def test_leave_one_out_excludes_focal_asset(self):
        d = attach_peer_context(fixture())
        row = d[(d["at"].str.startswith("2026-05")) & (d.pair == "T7USD")].iloc[0]
        self.assertAlmostEqual(row.peer_60m, np.mean(np.arange(7) - 3))
        self.assertEqual(row.peer_count, 7)
        self.assertAlmostEqual(row.peer_breadth15, 4 / 7)

    def test_future_outcomes_never_enter_features(self):
        d = attach_peer_context(fixture())
        before = hypothesis_scores(d)
        d["hit30"] = ~d["hit30"]
        after = hypothesis_scores(d)
        for key in before:
            np.testing.assert_array_equal(before[key], after[key])

    def test_peer_context_never_uses_future_timestamp(self):
        d = fixture()
        d.loc[d.split == "test", "pre_return_60m_pct"] += 200
        out = attach_peer_context(d)
        base = attach_peer_context(fixture())
        np.testing.assert_array_equal(out[out.split == "train"].peer_60m.to_numpy(),
                                      base[base.split == "train"].peer_60m.to_numpy())

    def test_insufficient_peer_population_abstains(self):
        d = fixture().iloc[:4]
        out = attach_peer_context(d)
        self.assertTrue(out.peer_60m.isna().all())
        self.assertFalse(out.peer_eligible.any())
        with self.assertRaisesRegex(ValueError, "at least five peers"):
            evaluate(d)

    def test_equal_top12_top3_budget(self):
        report = evaluate(fixture())
        for v in report["top3_diagnostic"].values():
            self.assertEqual(v["test"]["picks"], 3)
        for v in report["top12"].values():
            self.assertEqual(v["test"]["picks"], 8)
            self.assertEqual(v["test"]["unfilled_budget"], 4)

    def test_validation_selection_invariant_to_test_labels(self):
        d = fixture()
        before = evaluate(d)
        d.loc[d.split == "test", "hit30"] = False
        after = evaluate(d)
        self.assertEqual(before["validation_selected_top3"], after["validation_selected_top3"])
        self.assertEqual(before["validation_selected_top12"], after["validation_selected_top12"])

    def test_adding_future_anchors_does_not_change_prior_peers(self):
        d = fixture()
        before = attach_peer_context(d)
        future = d[d.split == "test"].copy()
        future["at"] = "2026-06-01T00:00:00+00:00"
        after = attach_peer_context(pd.concat([d, future], ignore_index=True))
        np.testing.assert_array_equal(before.peer_60m.to_numpy(),
                                      after.iloc[:len(d)].peer_60m.to_numpy())

if __name__ == "__main__":
    unittest.main()
