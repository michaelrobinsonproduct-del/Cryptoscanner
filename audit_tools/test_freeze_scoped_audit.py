"""No-network, fail-closed finite audit decision tests."""
import copy
import unittest
from audit_tools.freeze_scoped_audit import freeze

A = "a" * 40
B = "b" * 40
C = "c" * 40

def fixtures():
    live = [{"number": n, "head_sha": chr(96+n)*40} for n in (4, 7)]
    review = [{"number": p["number"], "head_sha": p["head_sha"], "classification": "conflicting",
               "review_valid": True, "reason": "verified source", "source_path": "x.py",
               "source_blob_sha": C} for p in live]
    cases = [{"pr": n, "path": "x"+str(n)+".py",
              "source": {"status": "VERIFIED_EXACT_HEAD_SOURCE"}} for n in (4, 7, 33, 40)]
    return (
        {"main_sha": A, "ledger_sha": B, "checkout_sha": C, "open_prs": live},
        {"main_sha": A, "open_pr_count": 2, "prs": review},
        {"main_sha": A, "ledger_sha_read_only": B, "audit_checkout_sha": C,
         "source_cases": cases, "main_legacy_writer": {"main_sha": A,
             "path": ".github/workflows/kraken-recovery-schedule.yml",
             "source": {"status": "VERIFIED_EXACT_HEAD_SOURCE"}}},
        {"main_sha": A, "ledger_sha_read_only": B, "status": "NOT_CERTIFIED",
         "unresolved_pr_count": 0, "unknown_consumer_count": 2,
         "unknown_write_destination_count": 1,
         "cleanup_authorized": False, "production_mutation_authorized": False},
        {"remote_main_sha": A, "audit_checkout_sha": C, "unknowns": ["ios", "supabase"]},
        {"main_sha": A, "unknown_write_destinations": ["unknown.yml"]},
        {"runtime_coverage_certified": False, "cleanup_authorized": False},
    )

class FreezeScopeTests(unittest.TestCase):
    def test_scope_is_not_promoted_by_verified_sources(self):
        result = freeze(*fixtures())
        self.assertEqual(result["full_audit"], "NOT_CERTIFIED")
        self.assertEqual(result["scope_decisions"]["isolated_read_only_integration"],
                         "CONDITIONAL_PREPARE_TEST_ONLY")
        self.assertEqual(result["scope_decisions"]["legacy_deletion"], "BLOCKED")
        self.assertEqual(result["unknown_consumer_count"], 2)
        self.assertEqual(result["unknown_write_destinations"], ["unknown.yml"])
        self.assertFalse(result["cleanup_authorized"])
        self.assertEqual(len(result["prs"]), 2)

    def test_stale_review_is_unknown_and_gate_must_agree(self):
        data = list(fixtures())
        data[1]["prs"][0]["review_valid"] = False
        data[3]["unresolved_pr_count"] = 1
        result = freeze(*data)
        self.assertEqual(result["unresolved_semantic_prs"], [4])
        self.assertEqual(result["prs"][0]["disposition"], "unknown")
        data[3]["unresolved_pr_count"] = 0
        with self.assertRaisesRegex(ValueError, "unresolved counts"):
            freeze(*data)

    def test_head_mismatch_and_duplicate_pr_fail(self):
        data = list(fixtures())
        data[1]["prs"][0]["head_sha"] = "d" * 40
        with self.assertRaisesRegex(ValueError, "different PR head"):
            freeze(*data)
        data = list(fixtures())
        data[0]["open_prs"].append(copy.deepcopy(data[0]["open_prs"][0]))
        with self.assertRaisesRegex(ValueError, "duplicate"):
            freeze(*data)

    def test_main_ledger_checkout_identity_fail_closed(self):
        for index, key in ((1, "main_sha"), (2, "ledger_sha_read_only"),
                           (4, "audit_checkout_sha"), (5, "main_sha")):
            data = list(fixtures())
            data[index][key] = "f" * 40
            with self.subTest(index=index, key=key):
                with self.assertRaisesRegex(ValueError, "identity mismatch"):
                    freeze(*data)

    def test_missing_source_case_and_legacy_writer_fail_closed(self):
        data = list(fixtures())
        data[2]["source_cases"].pop()
        with self.assertRaisesRegex(ValueError, "risk source cases"):
            freeze(*data)
        data = list(fixtures())
        data[2]["main_legacy_writer"]["main_sha"] = "f" * 40
        with self.assertRaisesRegex(ValueError, "legacy writer"):
            freeze(*data)

    def test_unverified_source_remains_blocked_but_isolated_tests_possible(self):
        data = list(fixtures())
        data[2]["source_cases"][0]["source"]["status"] = "PR_HEAD_DRIFT"
        result = freeze(*data)
        self.assertEqual(result["unverified_source_cases"], ["4:x4.py"])
        self.assertEqual(result["scope_decisions"]["isolated_read_only_integration"],
                         "CONDITIONAL_PREPARE_TEST_ONLY")
        self.assertEqual(result["scope_decisions"]["production_activation"], "BLOCKED")

    def test_no_external_snapshot_or_false_gate_approval(self):
        data = list(fixtures())
        data[6]["runtime_coverage_certified"] = True
        with self.assertRaisesRegex(ValueError, "External snapshot"):
            freeze(*data)
        data = list(fixtures())
        data[3]["status"] = "CERTIFIED"
        with self.assertRaisesRegex(ValueError, "authorization"):
            freeze(*data)

    def test_ledger_or_runtime_count_disagreement_abstains(self):
        data = list(fixtures())
        data[3]["unknown_consumer_count"] = 1
        with self.assertRaisesRegex(ValueError, "consumer counts"):
            freeze(*data)
        data = list(fixtures())
        data[3]["unknown_write_destination_count"] = 0
        with self.assertRaisesRegex(ValueError, "write destination counts"):
            freeze(*data)

if __name__ == "__main__":
    unittest.main()
