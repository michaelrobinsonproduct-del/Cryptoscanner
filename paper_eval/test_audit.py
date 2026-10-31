"""Synthetic-only adversarial tests; none of these fixtures are real market results."""
import copy
import unittest

from paper_eval.audit import evaluate
from paper_pov import ledger
from paper_pov.test_ledger import synthetic

SHA = "a" * 40


def scenario(*, offsets=(0, 30, 60, 90, 120), gain=True):
    state = ledger.empty()
    first_watch = None
    missed = None
    for offset in offsets:
        report = synthetic(offset)
        if first_watch is None:
            first_watch = [p["pair"] for p in report["watch"][:2]]
            missed = next(o["pair"] for o in report["observations"]
                          if o["pair"] not in {p["pair"] for p in report["watch"]})
        for p in report["watch"]:
            p["baseline_score"] = 100 if p["pair"] == first_watch[0] else 10
            p["challenger_score"] = 100 if p["pair"] == first_watch[1] else 10
        if gain and offset:
            for o in report["observations"]:
                if o["pair"] in (first_watch[0], missed):
                    o["price"] = 1.40
        state = ledger.advance(state, report, SHA)
    return state


class AuditTests(unittest.TestCase):
    def test_forward_sampled_comparison_and_observed_miss(self):
        state = scenario()
        out = evaluate(state, horizon_hours=1, top_k=1)
        self.assertEqual(out["actual_scans"], 5)
        self.assertEqual(out["mature_enough_runs"], 1)
        self.assertEqual(out["comparable_runs"], 1)
        self.assertEqual(out["comparison_samples_per_arm"], 1)
        self.assertEqual(out["baseline_observed_hits"], 1)
        self.assertEqual(out["challenger_observed_hits"], 0)
        self.assertEqual(out["observed_nonwatch_30pct_movers"], 1)
        self.assertGreater(out["continuously_sampled_nonwatch_pairs"], 0)
        self.assertIsNone(out["independent_held_out_lift"])
        self.assertIs(out["production_applied"], False)
        self.assertIn("not all-market recall", out["limitations"])

    def test_gap_abstains_not_false_negative(self):
        out = evaluate(scenario(offsets=(0, 120)), horizon_hours=1, top_k=1)
        self.assertEqual(out["mature_enough_runs"], 1)
        self.assertEqual(out["comparable_runs"], 0)
        self.assertEqual(out["excluded_incomplete_or_gap"], 1)
        self.assertIsNone(out["baseline_observed_hit_rate"])

    def test_immature_never_scored(self):
        out = evaluate(scenario(offsets=(0, 30)), horizon_hours=1, top_k=1)
        self.assertEqual(out["comparable_runs"], 0)
        self.assertEqual(out["excluded_immature"], 2)

    def test_mutated_return_rejected_even_with_valid_checksum(self):
        state = scenario()
        state["outcomes"][0]["return_pct"] = 999
        ledger.seal(state)
        with self.assertRaisesRegex(ValueError, "return disagrees"):
            evaluate(state, 1, 1)

    def test_mutated_hit_rejected_even_with_valid_checksum(self):
        state = scenario()
        state["outcomes"][0]["observed_30pct_hit"] = False
        ledger.seal(state)
        with self.assertRaisesRegex(ValueError, "hit label disagrees"):
            evaluate(state, 1, 1)

    def test_mutated_gap_rejected_even_with_valid_checksum(self):
        state = scenario()
        state["outcomes"][0]["status"] = "ABSTAIN_GAP"
        for field in ("observed_at", "return_pct", "observed_peak_pct", "observed_30pct_hit"):
            state["outcomes"][0].pop(field, None)
        ledger.seal(state)
        with self.assertRaisesRegex(ValueError, "contradicts"):
            evaluate(state, 1, 1)

    def test_orphan_prediction_rejected(self):
        state = scenario()
        state["predictions"][0]["run_id"] = "f" * 64
        ledger.seal(state)
        with self.assertRaisesRegex(ValueError, "Orphan"):
            evaluate(state, 1, 1)

    def test_outcome_before_maturity_rejected(self):
        state = scenario()
        state["runs"] = state["runs"][:2]
        state["observations"] = [o for o in state["observations"]
                                 if o["run_id"] in {r["id"] for r in state["runs"]}]
        state["predictions"] = [p for p in state["predictions"]
                               if p["run_id"] in {r["id"] for r in state["runs"]}]
        ledger.seal(state)
        with self.assertRaisesRegex(ValueError, "maturity"):
            evaluate(state, 1, 1)

    def test_tampered_market_price_rejected(self):
        state = scenario()
        for o in state["observations"]:
            if o["at"] != state["runs"][0]["as_of"]:
                o["price"] *= 1.05
                break
        ledger.seal(state)
        with self.assertRaisesRegex(ValueError, "(return|peak) disagrees"):
            evaluate(state, 1, 1)

    def test_invalid_horizon_and_k_fail_closed(self):
        state = scenario(offsets=(0,))
        for h, k in ((0, 1), (2, 1), (1, 0), (1, 13), (True, 1), (1, True)):
            with self.assertRaises(ValueError):
                evaluate(state, h, k)

    def test_duplicate_observation_rejected(self):
        state = scenario(offsets=(0,))
        state["observations"].append(copy.deepcopy(state["observations"][0]))
        state["runs"][0]["observation_count"] += 1
        ledger.seal(state)
        with self.assertRaisesRegex(ValueError, "Duplicate observation"):
            evaluate(state, 1, 1)

    def test_checksum_rejected_before_evaluation(self):
        state = scenario(offsets=(0,))
        state["predictions"][0]["price"] = 999
        with self.assertRaisesRegex(ValueError, "checksum"):
            evaluate(state, 1, 1)


if __name__ == "__main__":
    unittest.main()
