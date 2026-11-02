"""Adversarial source-bound scoped audit tests; no GitHub/network required."""
import base64
import copy
import unittest
from audit_tools.bounded_audit_scope import CASES, assess, git_blob_sha, source_identity

class BoundedAuditScopeTests(unittest.TestCase):
    def row(self, case, content, api_sha=None):
        raw=content.encode()
        return {"head_sha":case["expected_head_sha"],
                "file_blob_comparisons":[{"path":case["path"],"pr_blob_sha":api_sha or git_blob_sha(raw)}]}
    def payload(self, content):
        raw=content.encode()
        return {"encoding":"base64","content":base64.b64encode(raw).decode(),"sha":git_blob_sha(raw)}
    def synthetic(self):
        case={"pr":7,"path":"simple_scanner/scan.py","sha":git_blob_sha(b"market_prices SIMPLE_SCANNER_DATA_DIR"),
              "head_sha":"a"*40,"expected_head_sha":"a"*40,
              "require":("market_prices","SIMPLE_SCANNER_DATA_DIR")}
        content="market_prices SIMPLE_SCANNER_DATA_DIR"
        return case,content

    def test_exact_source_identity_and_pr_files_api_mismatch_are_separate(self):
        case,content=self.synthetic()
        row=self.row(case,content,"f"*40)
        identity=source_identity(case,row,self.payload(content))
        self.assertEqual(identity["status"],"VERIFIED_EXACT_HEAD_SOURCE")
        self.assertTrue(identity["pr_files_api_discrepancy"])
        self.assertEqual(identity["calculated_sha"],case["sha"])

    def test_stale_head_abstains_before_fetch(self):
        case,content=self.synthetic()
        row=self.row(case,content);row["head_sha"]="b"*40
        self.assertEqual(source_identity(case,row,self.payload(content))["status"],"PR_HEAD_DRIFT")

    def test_source_sha_or_bytes_tamper_abstains(self):
        case,content=self.synthetic()
        row=self.row(case,content)
        payload=self.payload(content);payload["sha"]="c"*40
        self.assertEqual(source_identity(case,row,payload)["status"],"SOURCE_BLOB_MISMATCH")
        payload=self.payload(content+" tampered")
        self.assertEqual(source_identity(case,row,payload)["status"],"SOURCE_BLOB_MISMATCH")
        self.assertEqual(source_identity(case,row,{"encoding":"utf-8"})["status"],"UNVERIFIED_SOURCE_RESPONSE")

    def test_missing_required_contract_or_forbidden_segment_claim_abstains(self):
        case,content=self.synthetic()
        case["sha"]=git_blob_sha(b"market_prices")
        self.assertEqual(source_identity(case,self.row(case,"market_prices"),self.payload("market_prices"))["status"],
                         "SOURCE_CONTRACT_MISMATCH")
        case["forbid"]=("segment-manifest",)
        forbidden_content=content+" segment-manifest"
        case["sha"]=git_blob_sha(forbidden_content.encode())
        self.assertEqual(source_identity(case,self.row(case,forbidden_content),
                                         self.payload(forbidden_content))["status"],"SOURCE_CONTRACT_MISMATCH")

    def test_all_findings_restrict_activation_and_deletion_not_isolated_tests(self):
        self.assertEqual({c["pr"] for c in CASES},{4,7,33,40})
        self.assertTrue(all(c["block_production"] and c["block_deletion"] for c in CASES))
        self.assertTrue(all(c["expected_head_sha"] and len(c["sha"])==40 for c in CASES))

    def test_scoped_decision_cannot_claim_full_certification(self):
        inventory={"main_sha":"a"*40,"ledger_sha":"b"*40,"checkout_sha":"c"*40,
                   "open_prs":[]}
        result=assess(inventory,{})
        self.assertEqual(result["source_verified"],0)
        self.assertEqual(result["scopes"]["isolated_read_only_integration"],
                         "PREPARE_AND_TEST_ONLY_PENDING_B_V")
        self.assertFalse(result["full_audit_certified"])
        self.assertFalse(result["cleanup_authorized"])
        self.assertFalse(result["production_mutation_authorized"])
        self.assertEqual(len(result["finite_blockers"]),3)

if __name__ == "__main__":
    unittest.main()
