"""No-network, fail-closed finite audit decision tests."""
import copy
import unittest
from audit_tools.freeze_scoped_audit import freeze

A = "a" * 40
B = "b" * 40
C = "c" * 40

def fixtures():
    heads = {4: "d" * 40, 7: "e" * 40, 33: "f" * 40, 40: "1" * 40}
    live = [{"number": n, "head_sha": heads[n],
             "file_blob_comparisons": [{"path": "x.py", "pr_blob_sha": C}]}
            for n in (4, 7, 33, 40)]
    review = [{"number": p["number"], "head_sha": p["head_sha"], "classification": "conflicting",
               "review_valid": True, "reason": "verified source", "source_path": "x.py",
               "source_blob_sha": C} for p in live]
    cases = [{"pr": n, "path": path, "head_sha": heads[n], "expected_head_sha": heads[n],
              "expected_blob_sha": C,
              "source": {"status": "VERIFIED_EXACT_HEAD_SOURCE",
                         "calculated_sha": C, "github_contents_sha": C,
                         "pr_files_api_sha": C, "pr_files_api_discrepancy": False}}
             for n, path in ((4, "evaluation/measure-forward.ts"),
                             (4, "evaluation/shadow-cycle.ts"),
                             (7, "simple_scanner/scan.py"),
                             (33, ".github/workflows/kraken-simple.yml"),
                             (40, ".github/workflows/paper-forward-audit.yml"))]
    for case in cases:
        next(p for p in live if p["number"] == case["pr"])["file_blob_comparisons"].append(
            {"path": case["path"], "pr_blob_sha": C})
    return (
        {"main_sha": A, "ledger_sha": B, "checkout_sha": C, "open_prs": live,
         "main_blob_shas": {".github/workflows/kraken-recovery-schedule.yml": C}},
        {"main_sha": A, "open_pr_count": 4, "prs": review},
        {"main_sha": A, "ledger_sha_read_only": B, "audit_checkout_sha": C,
         "source_cases": cases, "main_legacy_writer": {"main_sha": A,
             "path": ".github/workflows/kraken-recovery-schedule.yml",
             "expected_blob_sha": C,
             "source": {"status": "VERIFIED_EXACT_HEAD_SOURCE",
                        "calculated_sha": C, "github_contents_sha": C}}},
        {"main_sha": A, "ledger_sha_read_only": B, "status": "NOT_CERTIFIED", "blockers": [],
         "unresolved_pr_count": 0, "unknown_consumer_count": 2,
         "unknown_write_destination_count": 1,
         "cleanup_authorized": False, "production_mutation_authorized": False},
        {"remote_main_sha": A, "audit_checkout_sha": C, "unknowns": ["ios", "supabase"]},
        {"remote_main_sha": A, "unknown_write_destinations": ["unknown.yml"]},
        {"current_main_sha": A, "runtime_coverage_certified": False, "cleanup_authorized": False},
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
        self.assertEqual(len(result["prs"]), 4)

    def test_review_valid_cannot_hide_wrong_or_missing_source_blob(self):
        for mutation in ("wrong_blob", "missing_path", "duplicate_path", "wrong_claim"):
            data = list(fixtures())
            if mutation == "wrong_blob":
                data[0]["open_prs"][0]["file_blob_comparisons"][0]["pr_blob_sha"] = "9" * 40
            elif mutation == "missing_path":
                data[0]["open_prs"][0]["file_blob_comparisons"] = [
                    x for x in data[0]["open_prs"][0]["file_blob_comparisons"] if x["path"] != "x.py"]
            elif mutation == "duplicate_path":
                data[0]["open_prs"][0]["file_blob_comparisons"].append(
                    copy.deepcopy(data[0]["open_prs"][0]["file_blob_comparisons"][0]))
            else:
                data[1]["prs"][0]["source_blob_sha"] = "9" * 40
            with self.subTest(mutation=mutation):
                with self.assertRaisesRegex(ValueError, "semantic source blob mismatch"):
                    freeze(*data)

    def test_unreviewed_pr_is_unknown_without_source_claim(self):
        data = list(fixtures())
        data[1]["prs"][0]["review_valid"] = False
        data[0]["open_prs"][0]["file_blob_comparisons"] = [
                    x for x in data[0]["open_prs"][0]["file_blob_comparisons"] if x["path"] != "x.py"]
        data[3]["unresolved_pr_count"] = 1
        result = freeze(*data)
        self.assertEqual(result["prs"][0]["disposition"], "unknown")
        self.assertFalse(result["cleanup_authorized"])

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
        data[1]["prs"][0]["head_sha"] = "f" * 40
        with self.assertRaisesRegex(ValueError, "different PR head"):
            freeze(*data)
        data = list(fixtures())
        data[0]["open_prs"].append(copy.deepcopy(data[0]["open_prs"][0]))
        with self.assertRaisesRegex(ValueError, "duplicate"):
            freeze(*data)

    def test_main_ledger_checkout_identity_fail_closed(self):
        for index, key in ((1, "main_sha"), (2, "ledger_sha_read_only"),
                           (4, "audit_checkout_sha"), (5, "remote_main_sha")):
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
        self.assertEqual(result["unverified_source_cases"], ["4:evaluation/measure-forward.ts"])
        self.assertEqual(result["scope_decisions"]["isolated_read_only_integration"],
                         "CONDITIONAL_PREPARE_TEST_ONLY")
        self.assertEqual(result["scope_decisions"]["production_activation"], "BLOCKED")

    def test_forged_verified_status_cannot_hide_head_drift(self):
        data = list(fixtures())
        data[2]["source_cases"][0]["head_sha"] = "9" * 40
        result = freeze(*data)
        self.assertIn("4:evaluation/measure-forward.ts", result["unverified_source_cases"])
        self.assertFalse(result["prs"][0]["source_evidence_current"])
        self.assertEqual(result["scope_decisions"]["production_activation"], "BLOCKED")

    def test_forged_verified_source_blob_rejected(self):
        data = list(fixtures())
        data[2]["source_cases"][0]["source"]["calculated_sha"] = "9" * 40
        with self.assertRaisesRegex(ValueError, "Source evidence identity mismatch"):
            freeze(*data)
        data = list(fixtures())
        data[2]["main_legacy_writer"]["source"]["github_contents_sha"] = "9" * 40
        with self.assertRaisesRegex(ValueError, "Main legacy writer blob identity mismatch"):
            freeze(*data)

    def test_duplicate_risk_case_is_not_silently_accepted(self):
        data = list(fixtures())
        data[2]["source_cases"].append(copy.deepcopy(data[2]["source_cases"][0]))
        with self.assertRaisesRegex(ValueError, "duplicated"):
            freeze(*data)

    def test_pr_files_api_discrepancy_is_preserved_without_faking_source_drift(self):
        data = list(fixtures())
        case = data[2]["source_cases"][2]  # PR 7: exact Contents blob remains valid
        case["source"]["pr_files_api_discrepancy"] = True
        case["source"]["pr_files_api_sha"] = "9" * 40
        next(p for p in data[0]["open_prs"] if p["number"] == 7)["file_blob_comparisons"][1]["pr_blob_sha"] = "9" * 40
        result = freeze(*data)
        self.assertEqual(result["pr_files_api_discrepancies"], [7])
        row = next(x for x in result["source_evidence_matrix"] if x["pr"] == 7)
        self.assertEqual(row["source_status"], "VERIFIED_EXACT_HEAD_SOURCE")
        self.assertEqual(row["pr_files_api_blob_sha"], "9" * 40)
        self.assertFalse(row["blocks"]["isolated_read_only_integration"])
        self.assertTrue(row["blocks"]["legacy_deletion"])

    def test_risk_case_api_sha_and_discrepancy_must_match_inventory(self):
        for mutation in ("forged_api_sha", "hidden_discrepancy", "duplicate_case_path"):
            data = list(fixtures())
            case = data[2]["source_cases"][0]
            if mutation == "forged_api_sha":
                case["source"]["pr_files_api_sha"] = "9" * 40
                case["source"]["pr_files_api_discrepancy"] = True
                expected = "Risk source PR-files evidence mismatch"
            elif mutation == "hidden_discrepancy":
                case["source"]["pr_files_api_sha"] = "9" * 40
                next(p for p in data[0]["open_prs"] if p["number"] == 4)["file_blob_comparisons"][1]["pr_blob_sha"] = "9" * 40
                expected = "Risk source discrepancy flag mismatch"
            else:
                next(p for p in data[0]["open_prs"] if p["number"] == 4)["file_blob_comparisons"].append(
                    {"path": case["path"], "pr_blob_sha": C})
                expected = "Risk source PR-files evidence mismatch"
            with self.subTest(mutation=mutation):
                with self.assertRaisesRegex(ValueError, expected):
                    freeze(*data)

    def test_scoped_matrix_never_promotes_unknown_runtime_to_deletion(self):
        data = list(fixtures())
        data[2]["source_cases"][0]["source"]["status"] = "PR_HEAD_DRIFT"
        result = freeze(*data)
        scopes = result["scope_evidence"]
        self.assertEqual(scopes["isolated_read_only_integration"]["blocking_source_cases"], [])
        self.assertEqual(scopes["production_activation"]["decision"], "BLOCKED")
        self.assertEqual(scopes["legacy_deletion"]["unverified_consumer_count"], 2)
        self.assertIn("unknown.yml", scopes["production_activation"]["unverified_write_destinations"])
        self.assertEqual(len(result["source_evidence_matrix"]), 6)

    def test_runtime_assessment_bound_to_current_main(self):
        data = list(fixtures())
        data[6]["current_main_sha"] = "f" * 40
        with self.assertRaisesRegex(ValueError, "runtime assessment main"):
            freeze(*data)

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
