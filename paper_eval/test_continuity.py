"""Synthetic transition and archive tamper tests, never real market evidence."""
import copy
import unittest

from paper_eval.continuity import verify_transition
from paper_pov import ledger
from paper_pov.test_ledger import SHA, synthetic


class ContinuityTests(unittest.TestCase):
    def test_simple_append_retains_every_previous_record(self):
        before = ledger.advance(ledger.empty(), synthetic(0), SHA)
        after = ledger.advance(before, synthetic(30), SHA)
        out = verify_transition(before, after)
        self.assertEqual((out["from_generation"], out["to_generation"]), (1, 2))
        self.assertEqual(out["new_predictions"], 12)
        self.assertEqual(out["new_observations"], 25)
        self.assertEqual(out["compacted_runs"], 0)
        self.assertTrue(out["prior_records_immutable"])
        self.assertFalse(out["production_applied"])

    def test_50_hour_compaction_is_reconstructed_from_prior_quotes(self):
        before = ledger.advance(ledger.empty(), synthetic(0), SHA)
        after = ledger.advance(before, synthetic(51 * 60), SHA)
        out = verify_transition(before, after)
        self.assertEqual(out["compacted_runs"], 1)
        self.assertEqual(out["compacted_predictions"], 12)
        self.assertEqual(out["compacted_observations"], 25)
        self.assertEqual(out["reconstructed_compacted_gaps"], 48)
        self.assertEqual(out["reconstructed_compacted_matured"], 0)

    def test_resealed_mutation_of_retained_prediction_fails(self):
        before = ledger.advance(ledger.empty(), synthetic(0), SHA)
        after = ledger.advance(before, synthetic(30), SHA)
        after["predictions"][0]["baseline_score"] += 5
        ledger.seal(after)
        with self.assertRaisesRegex(ValueError, "Immutable prediction history"):
            verify_transition(before, after)

    def test_resealed_mutation_of_retained_quote_fails(self):
        before = ledger.advance(ledger.empty(), synthetic(0), SHA)
        after = ledger.advance(before, synthetic(30), SHA)
        after["observations"][0]["price"] *= 1.01
        ledger.seal(after)
        with self.assertRaisesRegex(ValueError, "quote history"):
            verify_transition(before, after)

    def test_resealed_archive_gap_to_fake_matured_fails(self):
        before = ledger.advance(ledger.empty(), synthetic(0), SHA)
        after = ledger.advance(before, synthetic(51 * 60), SHA)
        after["archived"]["gap_abstentions"] -= 1
        after["archived"]["matured_labels"] += 1
        ledger.seal(after)
        with self.assertRaisesRegex(ValueError, "matured-label totals"):
            verify_transition(before, after)

    def test_resealed_archive_fake_hit_fails(self):
        before = ledger.advance(ledger.empty(), synthetic(0), SHA)
        after = ledger.advance(before, synthetic(51 * 60), SHA)
        after["archived"]["observed_30pct_hits"] += 1
        ledger.seal(after)
        with self.assertRaisesRegex(ValueError, "sampled-hit totals"):
            verify_transition(before, after)

    def test_resealed_archive_provenance_index_loss_fails(self):
        before = ledger.advance(ledger.empty(), synthetic(0), SHA)
        after = ledger.advance(before, synthetic(51 * 60), SHA)
        after["archive_index"] = []
        ledger.seal(after)
        with self.assertRaisesRegex(ValueError, "provenance index"):
            verify_transition(before, after)

    def test_resealed_old_outcome_rewrite_fails(self):
        before = ledger.empty()
        for minute in (0, 30, 60, 90, 120):
            before = ledger.advance(before, synthetic(minute), SHA)
        after = ledger.advance(before, synthetic(150), SHA)
        altered = copy.deepcopy(after)
        altered["outcomes"][0]["return_pct"] += 0.01
        ledger.seal(altered)
        with self.assertRaisesRegex(ValueError, "(return disagrees|Previously recorded outcome)"):
            verify_transition(before, altered)

    def test_replay_and_skipped_generation_fail(self):
        before = ledger.advance(ledger.empty(), synthetic(0), SHA)
        after = ledger.advance(before, synthetic(30), SHA)
        altered = copy.deepcopy(after)
        altered["generation"] = 3
        ledger.seal(altered)
        with self.assertRaisesRegex(ValueError, "(generation|Expected exactly)"):
            verify_transition(before, altered)

    def test_archive_summary_must_match_owning_run(self):
        before = ledger.advance(ledger.empty(), synthetic(0), SHA)
        after = ledger.advance(before, synthetic(51 * 60), SHA)
        altered = copy.deepcopy(after)
        altered["archived"]["observations"] += 1
        ledger.seal(altered)
        with self.assertRaisesRegex(ValueError, "Archived observation count"):
            verify_transition(before, altered)


if __name__ == "__main__":
    unittest.main()
