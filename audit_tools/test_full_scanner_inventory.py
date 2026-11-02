"""Offline fail-closed pagination tests for repository inventory (no network)."""
import unittest
from unittest.mock import patch
from audit_tools.full_scanner_inventory import gh_pages, reconcile_pr_snapshot, remote_main_paths, remote_main_blobs, compare_pr_blobs, build_consumer_graph, workflow_branch_references


class BranchReferenceTests(unittest.TestCase):
    def test_actual_legacy_checkout_and_durable_history(self):
        source="""jobs:
  scan:
    steps:
      - uses: actions/checkout@v4
        with:
          ref: simplified-scanner-recovery-20261011
      - name: Restore
        run: |
          git fetch origin refs/heads/simple-history:refs/remotes/origin/simple-history
          git push origin HEAD:refs/heads/simple-history
"""
        refs=workflow_branch_references(source)
        self.assertEqual(refs["checkout_refs"],["simplified-scanner-recovery-20261011"])
        self.assertEqual(refs["branch_ref_mentions"],["simple-history"])
        self.assertEqual(refs["unresolved_checkout_refs"],[])

    def test_dynamic_checkout_is_not_a_verified_static_ref(self):
        source="""steps:
  - uses: actions/checkout@v4
    with:
      ref: \${{ github.event.pull_request.head.sha || github.sha }}
  - name: Done
    run: echo done
"""
        refs=workflow_branch_references(source)
        self.assertEqual(refs["checkout_refs"],[])
        self.assertEqual(len(refs["unresolved_checkout_refs"]),1)

    def test_default_checkout_does_not_invent_main(self):
        refs=workflow_branch_references("- uses: actions/checkout@v4\n")
        self.assertEqual(refs["checkout_refs"],[])
        self.assertEqual(refs["branch_ref_mentions"],[])

    def test_graph_preserves_static_vs_live_provenance(self):
        workflow={"path":".github/workflows/kraken-recovery-schedule.yml",
                  "scripts":[],"python_modules":[],"ledger_ref":False,
                  "branch_references":{"checkout_refs":["simplified-scanner-recovery-20261011"],
                    "branch_ref_mentions":["simple-history"],"unresolved_checkout_refs":[]}}
        graph=build_consumer_graph([workflow],{"snapshot_utc":"2026-11-02T02:17:00Z"},"a"*40,"b"*40)
        edges={(e["target"],e["kind"]) for e in graph["edges"]}
        self.assertIn(("github-ref:simplified-scanner-recovery-20261011","explicit_checkout_ref"),edges)
        self.assertIn(("github-ref:simple-history","static_branch_ref_mention"),edges)
        self.assertTrue(all(not e["observed_runtime"] for e in graph["edges"]))
        self.assertFalse(graph["cleanup_authorized"])

class PaginationTests(unittest.TestCase):
    def test_multiple_pages_are_all_included(self):
        with patch("audit_tools.full_scanner_inventory.gh", side_effect=[list(range(100)), [100,101]]) as mocked:
            result=gh_pages("repos/owner/repo/branches")
        self.assertEqual(len(result),102)
        self.assertEqual(result[-2:],[100,101])
        self.assertIn("page=2",mocked.call_args_list[-1].args[0])

    def test_full_last_page_requires_empty_followup(self):
        with patch("audit_tools.full_scanner_inventory.gh", side_effect=[list(range(100)), []]):
            self.assertEqual(len(gh_pages("repos/owner/repo/pulls?state=open")),100)

    def test_api_error_aborts(self):
        with patch("audit_tools.full_scanner_inventory.gh", return_value={"error":"403"}):
            with self.assertRaisesRegex(RuntimeError,"pagination failure"):
                gh_pages("repos/owner/repo/branches")

    def test_cap_aborts_instead_of_truncating(self):
        with patch("audit_tools.full_scanner_inventory.gh", return_value=list(range(100))):
            with self.assertRaisesRegex(RuntimeError,"limit reached"):
                gh_pages("repos/owner/repo/branches",max_pages=2)

class RemoteMainTreeTests(unittest.TestCase):
    SHA="a"*40

    def test_remote_main_not_checkout_paths(self):
        calls=[]
        def fetch(path):
            calls.append(path)
            return {"truncated":False,"tree":[
                {"type":"blob","path":"paper_pov/scanner.py","sha":"b"*40},
                {"type":"tree","path":"audit_tools"}]}
        paths=remote_main_paths(self.SHA,fetch)
        self.assertEqual(paths,{"paper_pov/scanner.py"})
        self.assertNotIn("audit_tools/full_scanner_inventory.py",paths)
        self.assertIn(self.SHA,calls[0])

    def test_truncated_tree_fails_closed(self):
        with self.assertRaisesRegex(RuntimeError,"truncated"):
            remote_main_paths(self.SHA,lambda _:{"truncated":True,"tree":[]})

    def test_api_error_fails_closed(self):
        with self.assertRaisesRegex(RuntimeError,"unavailable"):
            remote_main_paths(self.SHA,lambda _:{"error":"403"})

    def test_invalid_main_sha_fails_closed(self):
        with self.assertRaisesRegex(RuntimeError,"invalid"):
            remote_main_paths("not-a-sha",lambda _:None)

    def test_malformed_or_duplicate_tree_fails_closed(self):
        for entries in ([{"type":"blob"}],
                        [{"type":"blob","path":"x","sha":"b"*40},{"type":"blob","path":"x","sha":"c"*40}]):
            with self.subTest(entries=entries):
                with self.assertRaises(RuntimeError):
                    remote_main_paths(self.SHA,lambda _:{"truncated":False,"tree":entries})


class ExactBlobComparisonTests(unittest.TestCase):
    def test_same_path_different_contents_is_not_integrated(self):
        main={"paper_pov/scanner.py":"a"*40}
        changed=[{"filename":"paper_pov/scanner.py","sha":"b"*40,"status":"modified"}]
        rows=compare_pr_blobs(changed,main)
        self.assertEqual(rows[0]["comparison"],"DIFFERENT_BLOB_OR_UNKNOWN")
        self.assertEqual(rows[0]["main_blob_sha"],"a"*40)

    def test_exact_blob_equality_and_missing_file(self):
        main={"x.py":"a"*40}
        rows=compare_pr_blobs([
            {"filename":"x.py","sha":"a"*40,"status":"modified"},
            {"filename":"new.py","sha":"b"*40,"status":"added"},
            {"filename":"x.py","status":"removed"}],main)
        self.assertEqual([r["comparison"] for r in rows],
                         ["EXACT_BLOB_EQUAL","NOT_ON_MAIN","DIFFERENT_BLOB_OR_UNKNOWN"])

    def test_malformed_main_blob_sha_fails_closed(self):
        with self.assertRaisesRegex(RuntimeError,"invalid blob SHA"):
            remote_main_blobs("a"*40,lambda _:{
                "truncated":False,"tree":[{"type":"blob","path":"x","sha":"bad"}]})


class ConsumerGraphTests(unittest.TestCase):
    def test_static_edges_do_not_claim_live_invocation_or_cleanup(self):
        workflows=[{"path":".github/workflows/paper-pipeline.yml",
                    "scripts":["paper_pov/scanner.py"],"python_modules":[],
                    "ledger_ref":True}]
        runtime={"snapshot_utc":"2026-11-02T02:17:00Z",
                 "supabase":{"sample_source_consumers":[
                     {"function":"kraken-miss-learner","tables":["kraken_miss_learning"]}]},
                 "static_consumers":{"ios":{"source":"ios/KrakenEdge/ScannerAPI.swift",
                                             "endpoint":"https://example.invalid/dashboard"}}}
        graph=build_consumer_graph(workflows,runtime,"a"*40,"b"*40)
        self.assertFalse(graph["cleanup_authorized"])
        self.assertTrue(graph["unknowns"])
        self.assertTrue(all(not e["observed_runtime"] for e in graph["edges"]))
        self.assertTrue(any(e["target"]=="supabase-table:kraken_miss_learning" for e in graph["edges"]))
        self.assertTrue(any(e["target"]=="repo-script:paper_pov/scanner.py" for e in graph["edges"]))
        self.assertEqual(graph["remote_main_sha"],"b"*40)

    def test_empty_evidence_does_not_invent_runtime(self):
        graph=build_consumer_graph([],{"snapshot_utc":"2026-11-02T02:17:00Z"},"a"*40,"b"*40)
        self.assertEqual(graph["edges"],[])
        self.assertFalse(graph["cleanup_authorized"])


class SnapshotReconciliationTests(unittest.TestCase):
    def setUp(self):
        self.snapshot={"main_sha":"main-old","prs":[
            {"number":120,"head_sha":"head-old","classification":"needed"},
            {"number":80,"head_sha":"same-head","classification":"integrated"}]}
        self.rows=[{"number":80,"head_sha":"same-head"}]

    def test_main_drift_invalidates_old_integrated_claim(self):
        fetch=lambda _:{"state":"closed","merged_at":"2026-11-02T02:27:49Z",
                         "head":{"sha":"head-new"},"merge_commit_sha":"merge-120"}
        closed=reconcile_pr_snapshot(self.snapshot,self.rows,"main-new",fetch)
        self.assertEqual(self.rows[0]["triage_classification"],"unknown")
        self.assertEqual(self.rows[0]["triage_snapshot_classification"],"integrated")
        self.assertEqual(self.rows[0]["triage_stale_reason"],"MAIN_CHANGED_REQUIRES_SEMANTIC_REVIEW")
        self.assertTrue(closed[0]["merged"])
        self.assertEqual(closed[0]["final_head_sha"],"head-new")
        self.assertEqual(closed[0]["classification"],"integrated")

    def test_matching_main_and_head_retains_historical_classification(self):
        fetch=lambda _:{"state":"closed","merged_at":None,"head":{"sha":"head-old"}}
        closed=reconcile_pr_snapshot(self.snapshot,self.rows,"main-old",fetch)
        self.assertEqual(self.rows[0]["triage_classification"],"integrated")
        self.assertTrue(self.rows[0]["classification_valid_for_current_main"])
        self.assertFalse(closed[0]["merged"])
        self.assertEqual(closed[0]["classification"],"unknown")

    def test_closed_pr_api_ambiguity_fails_closed(self):
        with self.assertRaisesRegex(RuntimeError,"closed state unverified"):
            reconcile_pr_snapshot(self.snapshot,self.rows,"main-old",lambda _:{"error":"403"})

    def test_new_pr_cannot_inherit_classification(self):
        rows=[{"number":80,"head_sha":"same-head"},{"number":121,"head_sha":"new-head"}]
        reconcile_pr_snapshot(self.snapshot,rows,"main-old",
                              lambda _:{"state":"closed","merged_at":None,"head":{"sha":"head-old"}})
        self.assertEqual(rows[1]["triage_classification"],"unknown")
        self.assertEqual(rows[1]["triage_stale_reason"],"NEW_PR_NOT_IN_SNAPSHOT")


if __name__=="__main__":
    unittest.main()
