"""Adversarial synthetic chain-audit contracts; not real Kraken evidence."""
import copy
import unittest

from paper_eval.chain import verify_chain
from paper_pov import ledger
from paper_pov.test_ledger import SHA, synthetic


def sequence(minutes):
    states = [ledger.empty()]
    for m in minutes:
        states.append(ledger.advance(states[-1], synthetic(m), SHA))
    entries = [{"commit": format(i + 1, "040x"), "state": state}
               for i, state in enumerate(states)]
    return entries[::-1]


class ChainTests(unittest.TestCase):
    def test_genesis_to_three_appends(self):
        entries = sequence((0, 30, 60))
        report = verify_chain(entries, entries[0]["commit"])
        self.assertEqual(report["transitions_checked"], 3)
        self.assertEqual(report["tip_generation"], 3)
        self.assertTrue(report["verified_to_genesis"])
        self.assertFalse(report["bounded_history_only"])
        self.assertFalse(report["production_applied"])

    def test_one_scan_and_empty_genesis(self):
        entries = sequence((0,))
        self.assertEqual(verify_chain(entries, entries[0]["commit"])["snapshots_checked"], 2)
        zero = sequence(())
        self.assertEqual(verify_chain(zero, zero[0]["commit"])["transitions_checked"], 0)

    def test_detect_missing_middle_generation(self):
        entries = sequence((0, 30, 60))
        with self.assertRaisesRegex(ValueError, "exactly one new ledger generation"):
            verify_chain([entries[0], entries[2], entries[3]], entries[0]["commit"])

    def test_resealed_prior_prediction_mutation_rejected(self):
        entries = sequence((0, 30, 60))
        changed = copy.deepcopy(entries)
        changed[1]["state"]["predictions"][0]["baseline_score"] += 1
        ledger.seal(changed[1]["state"])
        with self.assertRaises(ValueError):
            verify_chain(changed, changed[0]["commit"])

    def test_resealed_prior_quote_mutation_rejected(self):
        entries = sequence((0, 30, 60))
        changed = copy.deepcopy(entries)
        first = changed[1]["state"]["runs"][0]["id"]
        watched = {p["pair"] for p in changed[1]["state"]["predictions"]
                   if p["run_id"] == first}
        quote = next(o for o in changed[1]["state"]["observations"]
                     if o["run_id"] == first and o["pair"] not in watched)
        quote["price"] *= 1.1
        ledger.seal(changed[1]["state"])
        with self.assertRaisesRegex(ValueError, "quote history"):
            verify_chain(changed, changed[0]["commit"])

    def test_tip_identity_mismatch_and_duplicate_commits(self):
        entries = sequence((0, 30))
        with self.assertRaisesRegex(ValueError, "tip mismatch"):
            verify_chain(entries, "f" * 40)
        entries[1]["commit"] = entries[0]["commit"]
        with self.assertRaisesRegex(ValueError, "Duplicate commit"):
            verify_chain(entries, entries[0]["commit"])

    def test_short_history_without_genesis_fails_closed(self):
        entries = sequence((0, 30, 60))
        with self.assertRaisesRegex(ValueError, "History truncated"):
            verify_chain(entries[:2], entries[0]["commit"])

    def test_full_bound_is_explicitly_partial(self):
        entries = sequence((0, 30, 60, 90))
        report = verify_chain(entries[:3], entries[0]["commit"], max_transitions=2)
        self.assertTrue(report["bounded_history_only"])
        self.assertFalse(report["verified_to_genesis"])
        self.assertEqual(report["transitions_checked"], 2)

    def test_oversized_manifest_and_invalid_limit(self):
        entries = sequence((0, 30, 60))
        with self.assertRaisesRegex(ValueError, "Unbounded"):
            verify_chain(entries, entries[0]["commit"], max_transitions=2)
        with self.assertRaisesRegex(ValueError, "limit"):
            verify_chain(entries, entries[0]["commit"], max_transitions=0)

    def test_resealed_compaction_tamper_fails(self):
        entries = sequence((0, 51 * 60))
        altered = copy.deepcopy(entries)
        altered[0]["state"]["archived"]["observed_30pct_hits"] += 1
        ledger.seal(altered[0]["state"])
        with self.assertRaisesRegex(ValueError, "sampled-hit totals"):
            verify_chain(altered, altered[0]["commit"])


if __name__ == "__main__":
    unittest.main()
