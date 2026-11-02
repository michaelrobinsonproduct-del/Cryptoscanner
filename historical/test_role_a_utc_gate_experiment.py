"""Adversarial research-only tests: no network, scanner or ledger writes."""
import io
import sys
import unittest
import zipfile
from pathlib import Path
import numpy as np
import pandas as pd

sys.path.insert(0, str(Path(__file__).parent))
from role_a_utc_gate_experiment import attach_midnight_proxy, load, metrics, scores, select


class ResearchTests(unittest.TestCase):
    def fixture(self):
        return pd.DataFrame([{
            "pair": p, "at": "2026-05-10T01:00:00+00:00",
            "date": "2026-05-10", "split": "test",
            "gate_status": "PASS_PRICE_PROXY",
            "pre_return_5m_pct": i / 10, "pre_return_15m_pct": i / 2,
            "pre_return_60m_pct": float(i), "volume_accel": float(i),
            "trade_accel": float(i), "volatility_pct": float(i) / 2,
            "max_forward_return_pct": float(i) * 10,
            "hit20": i >= 2, "hit30": i >= 3,
        } for i, p in enumerate(["AAAUSD", "BBBUSD", "CCCUSD", "DDDUSD"])])

    def test_future_labels_do_not_affect_any_ranking_feature(self):
        a = self.fixture()
        b = a.copy()
        b["max_forward_return_pct"] = [10000, 0, 0, 0]
        b["hit30"] = [True, False, False, False]
        for key in scores(a):
            np.testing.assert_array_equal(scores(a)[key], scores(b)[key])

    def test_priority_fills_same_budget_and_stable_ties(self):
        d = self.fixture()
        self.assertEqual(len(select(d, scores(d)["quiet_high_activity"], 3)), 3)
        self.assertEqual(list(select(d, np.zeros(4), 2).pair),
                         ["AAAUSD", "BBBUSD"])

    def test_signed_utc_gate_proxy_missing_midnight_abstains(self):
        d = pd.DataFrame([
            {"pair": "AAAUSD", "at": "2026-05-10T00:00:00+00:00", "price": 100},
            {"pair": "AAAUSD", "at": "2026-05-10T01:00:00+00:00", "price": 100.2},
            {"pair": "AAAUSD", "at": "2026-05-10T02:00:00+00:00", "price": 100.3},
            {"pair": "AAAUSD", "at": "2026-05-10T03:00:00+00:00", "price": 112.01},
            {"pair": "BBBUSD", "at": "2026-05-10T03:00:00+00:00", "price": 100},
            {"pair": "AAAUSD", "at": "2026-05-11T00:30:00+00:00", "price": 100},
        ])
        self.assertEqual(list(attach_midnight_proxy(d).gate_status),
                         ["BELOW_0_25", "BELOW_0_25", "PASS_PRICE_PROXY",
                          "ABOVE_12", "NO_UTC_MIDNIGHT_CLOSE",
                          "NO_UTC_MIDNIGHT_CLOSE"])

    def test_no_future_midnight_backfill(self):
        d = pd.DataFrame([
            {"pair": "AAAUSD", "at": "2026-05-10T23:45:00+00:00", "price": 100},
            {"pair": "AAAUSD", "at": "2026-05-11T00:00:00+00:00", "price": 120},
        ])
        self.assertEqual(attach_midnight_proxy(d).gate_status.iloc[0],
                         "NO_UTC_MIDNIGHT_CLOSE")

    def test_tampered_strict_archive_rejected(self):
        with io.BytesIO() as f:
            with zipfile.ZipFile(f, "w") as z:
                for name in ("research.ndjson", "research_training.ndjson",
                             "research_training_manifest.json", "moves.ndjson",
                             "summary.json"):
                    z.writestr(name, b"{}\n")
            f.seek(0)
            with self.assertRaisesRegex(ValueError, "source SHA mismatch"):
                load(f)

    def test_false_positives_and_recall_are_explicit(self):
        d = self.fixture()
        p = select(d, scores(d)["momentum_abs60_proxy"], 2)
        m = metrics(d, p, 2)["test"]
        self.assertEqual((m["hits30"], m["false_positives30"],
                          m["missed_observed_windows30"]), (1, 1, 0))


if __name__ == "__main__":
    unittest.main()
