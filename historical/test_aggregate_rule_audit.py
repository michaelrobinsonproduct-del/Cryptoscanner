"""Exact-source regression tests for the October historical aggregate audit."""
import copy
import hashlib
import json
import unittest
from pathlib import Path

from historical.aggregate_rule_audit import analyze


SOURCE = Path(__file__).parent / "evidence/kraken_20261010_historical_model.json"


class AggregateRuleAuditTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.model = json.loads(SOURCE.read_text())
        cls.report = analyze(cls.model)

    def test_source_blob_is_exact_archived_model(self):
        data = SOURCE.read_bytes()
        git_sha = hashlib.sha1(b"blob " + str(len(data)).encode() + b"\\0" + data).hexdigest()
        self.assertEqual(git_sha, "7a082fdf394e06b5de6ceee50e09ade8c97b2b97")

    def test_holdout_stratification_and_missed_movers(self):
        g = self.report["results"]["holdout"]["groups"]
        self.assertEqual((g["baseline"]["rows"], g["baseline"]["hits"]), (4995, 182))
        self.assertEqual((g["abs60_gt3"]["rows"], g["abs60_gt3"]["hits"]), (298, 83))
        self.assertEqual((g["quiet_or_early_abs60_le3"]["rows"], g["quiet_or_early_abs60_le3"]["hits"]), (4697, 99))
        self.assertEqual((g["early_and_trades_2x"]["rows"], g["early_and_trades_2x"]["hits"]), (272, 6))
        self.assertEqual((g["abs60_gt3_and_trades_2x"]["rows"], g["abs60_gt3_and_trades_2x"]["hits"]), (55, 15))
        self.assertGreater(self.report["results"]["holdout"]["abs60_gt3_vs_early_lift"], 10)
        self.assertLess(self.report["results"]["holdout"]["abs60_gt3_vs_early_fisher_one_sided_p"], 1e-40)

    def test_trade_acceleration_apparent_lift_disappears_within_holdout_strata(self):
        h = self.report["results"]["holdout"]
        self.assertGreater(h["raw_trade2_vs_baseline_lift"], 1.7)
        self.assertLess(h["trade2_within_early_lift"], 1.15)
        self.assertLess(h["trade2_within_abs60_gt3_lift"], 1.15)
        self.assertEqual(h["groups"]["volume_and_trades_2x"]["hits"], 17)
        self.assertEqual(h["groups"]["trades_only_2x"]["hits"], 4)

    def test_training_replication_and_nonstationary_trade_signal(self):
        t = self.report["results"]["train"]
        self.assertEqual((t["groups"]["abs60_gt3"]["rows"], t["groups"]["abs60_gt3"]["hits"]), (495, 179))
        self.assertEqual((t["groups"]["abs60_gt3_and_trades_2x"]["rows"], t["groups"]["abs60_gt3_and_trades_2x"]["hits"]), (89, 30))
        self.assertGreater(t["trade2_within_early_lift"], 1.5)
        self.assertLess(self.report["results"]["holdout"]["trade2_within_early_lift"], 1.15)

    def test_invalid_overlap_abstains(self):
        bad = copy.deepcopy(self.model)
        bad["rules"]["early_trades"]["holdout"]["rows"] = 400
        with self.assertRaises(ValueError):
            analyze(bad)
        bad = copy.deepcopy(self.model)
        bad["rules"]["volume_trades"]["train"]["major_movers"] = 999
        with self.assertRaises(ValueError):
            analyze(bad)


if __name__ == "__main__":
    unittest.main()
