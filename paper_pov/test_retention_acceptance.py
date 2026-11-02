"""Adversarial synthetic tests for real-ledger retention acceptance."""
import copy
import unittest
from paper_pov import ledger
from paper_pov.retention_acceptance import verify_transition
from paper_pov.test_ledger import synthetic, SHA


class RetentionAcceptanceTests(unittest.TestCase):
    def transition(self, minutes):
        before = ledger.advance(ledger.empty(), synthetic(0), SHA)
        report = synthetic(minutes)
        after = ledger.advance(before, report, SHA)
        # ledger.advance reuses nested immutable record dictionaries; isolate\n        # the before snapshot so adversarial mutations only affect after.\n        return copy.deepcopy(before), copy.deepcopy(after), report

    def check(self, before, after, report):
        return verify_transition(before, after, report, SHA)

    def test_no_rollover_retains_all_original_identifiers(self):
        b, a, r = self.transition(30)
        result = self.check(b, a, r)
        self.assertEqual(result["archived_predictions"], 0)
        self.assertEqual(result["cumulative_predictions"], 24)

    def test_fifty_hour_rollover_preserves_cumulative_identity_accounting(self):
        b, a, r = self.transition(51 * 60)
        result = self.check(b, a, r)
        self.assertEqual(result["archived_runs"], 1)
        self.assertEqual(result["archived_predictions"], 12)
        self.assertEqual(result["archived_observations"], 25)
        self.assertEqual(len(a["predictions"]), 12)
        self.assertEqual(result["cumulative_predictions"], 24)

    def test_missing_archive_prediction_count_rejected_even_if_sealed(self):
        b, a, r = self.transition(51 * 60)
        a["archived"]["predictions"] -= 1
        ledger.seal(a)
        with self.assertRaisesRegex(ValueError, "ARCHIVE_COUNTER_PREDICTIONS"):
            self.check(b, a, r)

    def test_missing_archive_observation_count_rejected_even_if_sealed(self):
        b, a, r = self.transition(51 * 60)
        a["archived"]["observations"] -= 1
        ledger.seal(a)
        with self.assertRaisesRegex(ValueError, "ARCHIVE_COUNTER_OBSERVATIONS"):
            self.check(b, a, r)

    def test_removed_archive_index_identity_rejected(self):
        b, a, r = self.transition(51 * 60)
        a["archive_index"] = []
        ledger.seal(a)
        with self.assertRaisesRegex(ValueError, "ARCHIVE_INDEX_IDENTITY"):
            self.check(b, a, r)

    def test_changed_retained_prediction_score_rejected(self):
        b, a, r = self.transition(30)
        a["predictions"][0]["challenger_score"] += 0.1
        ledger.seal(a)
        with self.assertRaisesRegex(ValueError, "MUTATED_OLD_PREDICTION"):
            self.check(b, a, r)

    def test_changed_retained_nonwatch_observation_rejected(self):
        b, a, r = self.transition(30)
        a["observations"][20]["price"] += 0.1
        ledger.seal(a)
        with self.assertRaisesRegex(ValueError, "MUTATED_OLD_OBSERVATION"):
            self.check(b, a, r)

    def test_mutated_existing_outcome_rejected(self):
        b = ledger.advance(ledger.empty(), synthetic(0), SHA)
        b = ledger.advance(b, synthetic(120), SHA)
        r = synthetic(150)
        a = ledger.advance(b, r, SHA)
        b = copy.deepcopy(b)
        a["outcomes"][0]["target_at"] = "2020-01-01T00:00:00+00:00"
        ledger.seal(a)
        with self.assertRaisesRegex(ValueError, "MUTATED_OLD_OUTCOME"):
            self.check(b, a, r)

    def test_forged_new_source_provenance_rejected(self):
        b, a, r = self.transition(30)
        with self.assertRaisesRegex(ValueError, "NEW_RUN_PROVENANCE"):
            verify_transition(b, a, r, "b" * 40)

    def test_generation_skip_rejected(self):
        b, a, r = self.transition(30)
        a["generation"] += 1
        ledger.seal(a)
        with self.assertRaises(ValueError):
            self.check(b, a, r)


if __name__ == "__main__":
    unittest.main()
