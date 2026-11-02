"""Offline fail-closed pagination tests for repository inventory (no network)."""
import unittest
from unittest.mock import patch
from audit_tools.full_scanner_inventory import gh_pages, reconcile_pr_snapshot, remote_main_paths, remote_main_blobs, compare_pr_blobs, build_consumer_graph, workflow_branch_references, inventory_workflow_source, workflow_orchestration_references, apply_semantic_review, classify_declared_write_surfaces, assess_external_runtime_snapshot, audit_gate_decision


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

    def test_actual_main_workflow_provenance(self):
        source="""on:
  workflow_dispatch:
  schedule:
    - cron: '3,33 * * * *'
permissions:
  contents: write
steps:
  - uses: actions/checkout@v4
    with:
      ref: simplified-scanner-recovery-20261011
  - name: Persist
    run: git push origin HEAD:refs/heads/simple-history
"""
        workflow=inventory_workflow_source(".github/workflows/kraken-recovery-schedule.yml",source)
        self.assertEqual(workflow["branch_references"]["checkout_refs"],
                         ["simplified-scanner-recovery-20261011"])
        self.assertEqual(workflow["branch_references"]["branch_ref_mentions"],["simple-history"])
        graph=build_consumer_graph([workflow],{"snapshot_utc":"2026-11-02T02:17:00Z"},
                                   "a"*40,"b"*40,workflow_source="remote_main")
        self.assertTrue(all(e["evidence"]=="remote_main:"+"b"*40 for e in graph["edges"]))
        self.assertTrue(workflow["writes_contents"])
        self.assertFalse(graph["cleanup_authorized"])


    def test_legacy_script_source_is_branch_pinned_not_main(self):
        source="""name: Old Kraken recovery
on:
  schedule:
    - cron: '3,33 * * * *'
jobs:
  scan:
    steps:
      - uses: actions/checkout@v4
        with:
          ref: simplified-scanner-recovery-20261011
      - run: python simple_scanner/scan.py
"""
        w=inventory_workflow_source(".github/workflows/kraken-recovery-schedule.yml",source)
        graph=build_consumer_graph([w],{"snapshot_utc":"2026-11-02T05:00:00Z"},"a"*40,"b"*40,workflow_source="remote_main")
        scripts=[e for e in graph["edges"] if e["kind"]=="invokes_script"]
        self.assertEqual(len(scripts),1)
        self.assertEqual(scripts[0]["target_checkout_ref"],"simplified-scanner-recovery-20261011")
        self.assertEqual(scripts[0]["target"],"repo-script:simple_scanner/scan.py")
        self.assertFalse(scripts[0]["observed_runtime"])

    def test_dynamic_checkout_does_not_assign_source_ref(self):
        source="""name: Dynamic source
on:
  workflow_dispatch:
jobs:
  scan:
    steps:
      - uses: actions/checkout@v4
        with:
          ref: \${{ github.sha }}
      - run: python simple_scanner/scan.py
"""
        w=inventory_workflow_source(".github/workflows/dynamic.yml",source)
        graph=build_consumer_graph([w],{"snapshot_utc":"2026-11-02T05:00:00Z"},"a"*40,"b"*40)
        scripts=[e for e in graph["edges"] if e["kind"]=="invokes_script"]
        self.assertEqual(len(scripts),1)
        self.assertNotIn("target_checkout_ref",scripts[0])
        self.assertTrue(any("Dynamic checkout" in u for u in graph["unknowns"]))

    def test_unrecognized_workflow_provenance_fails_closed(self):
        with self.assertRaisesRegex(ValueError,"Unrecognized"):
            build_consumer_graph([],{"snapshot_utc":"2026-11-02T02:17:00Z"},
                                 "a"*40,"b"*40,workflow_source="guessed")

    def test_unresolved_dynamic_checkout_blocks_cleanup(self):
        workflow={"path":".github/workflows/full-scanner-inventory.yml",
                  "scripts":[],"python_modules":[],"ledger_ref":False,
                  "branch_references":{"checkout_refs":[],"branch_ref_mentions":[],
                                       "unresolved_checkout_refs":["dynamic expression"]}}
        graph=build_consumer_graph([workflow],{"snapshot_utc":"2026-11-02T02:17:00Z"},"a"*40,"b"*40)
        self.assertIn("Dynamic checkout ref unresolved in .github/workflows/full-scanner-inventory.yml",
                      graph["unknowns"])
        self.assertFalse(graph["cleanup_authorized"])

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



class WorkflowOrchestrationTests(unittest.TestCase):
    def test_cadence_post_links_existing_writer(self):
        cadence="""name: Owner-authenticated independent paper cadence
on:
  issue_comment:
    types: [created]
jobs:
  wake:
    steps:
      - run: |
          gh api "repos/$GITHUB_REPOSITORY/actions/workflows/paper-pipeline.yml/runs?per_page=100"
          gh api -X POST "repos/$GITHUB_REPOSITORY/actions/workflows/paper-pipeline.yml/dispatches" -f ref=main
"""
        writer="""name: Public Kraken Paper POV (scheduled, isolated ledger)
on:
  workflow_dispatch:
jobs:
  writer:
    steps: []
"""
        w=[inventory_workflow_source(".github/workflows/paper-cadence-wake.yml",cadence),
           inventory_workflow_source(".github/workflows/paper-pipeline.yml",writer)]
        self.assertEqual(w[0]["orchestration"]["dispatch_workflows"],["paper-pipeline.yml"])
        graph=build_consumer_graph(w,{"snapshot_utc":"2026-11-02T05:00:00Z"},"a"*40,"b"*40,workflow_source="remote_main")
        matches=[e for e in graph["edges"] if e["kind"]=="explicit_workflow_dispatch_post"]
        self.assertEqual(len(matches),1)
        self.assertEqual(matches[0]["target"],"github-workflow:.github/workflows/paper-pipeline.yml")
        self.assertEqual(matches[0]["evidence"],"remote_main:"+"b"*40)
        self.assertFalse(matches[0]["observed_runtime"])

    def test_learning_subscription_resolves_display_name(self):
        writer="""name: Public Kraken Paper POV (scheduled, isolated ledger)
on:
  workflow_dispatch:
"""
        learning="""name: Independent PAPER sampled-outcome research (read only)
on:
  workflow_run:
    workflows: ["Public Kraken Paper POV (scheduled, isolated ledger)"]
    types: [completed]
permissions:
  contents: read
"""
        w=[inventory_workflow_source(".github/workflows/paper-pipeline.yml",writer),
           inventory_workflow_source(".github/workflows/paper-learning-outcomes-shadow.yml",learning)]
        self.assertEqual(w[1]["orchestration"]["workflow_run_names"],
                         ["Public Kraken Paper POV (scheduled, isolated ledger)"])
        graph=build_consumer_graph(w,{"snapshot_utc":"2026-11-02T05:00:00Z"},"a"*40,"b"*40,workflow_source="remote_main")
        matches=[e for e in graph["edges"] if e["kind"]=="workflow_run_subscription"]
        self.assertEqual(len(matches),1)
        self.assertEqual(matches[0]["target"],"github-workflow:.github/workflows/paper-pipeline.yml")

    def test_multiline_subscription_and_unknown_name_fail_closed(self):
        source="""name: Child
on:
  workflow_run:
    workflows:
      - "Never deployed parent"
      - "Other parent"
    types: [completed]
"""
        w=inventory_workflow_source(".github/workflows/child.yml",source)
        self.assertEqual(len(w["orchestration"]["workflow_run_names"]),2)
        graph=build_consumer_graph([w],{"snapshot_utc":"2026-11-02T05:00:00Z"},"a"*40,"b"*40)
        self.assertEqual(len([e for e in graph["edges"] if e["kind"]=="unresolved_workflow_run_name"]),2)
        self.assertTrue(any("not uniquely mapped" in x for x in graph["unknowns"]))
        self.assertFalse(graph["cleanup_authorized"])

    def test_get_comment_and_echo_are_not_dispatch_edges(self):
        source="""name: No dispatch
on:
  workflow_dispatch:
jobs:
  audit:
    steps:
      - run: |
          # gh api -X POST "repos/x/y/actions/workflows/other.yml/dispatches"
          echo 'gh api -X POST "repos/x/y/actions/workflows/other.yml/dispatches"'
          gh api "repos/x/y/actions/workflows/other.yml/runs"
          gh api -X GET "repos/x/y/actions/workflows/other.yml/dispatches"
"""
        refs=workflow_orchestration_references(source)
        self.assertEqual(refs["dispatch_workflows"],[])
        self.assertEqual(refs["workflow_run_names"],[])

    def test_dynamic_dispatch_is_unknown_not_guessed(self):
        source="""name: Dynamic
on:
  workflow_dispatch:
jobs:
  wake:
    steps:
      - run: |
          gh api -X POST "repos/$GITHUB_REPOSITORY/actions/workflows/\${TARGET}/dispatches"
"""
        refs=workflow_orchestration_references(source)
        self.assertEqual(refs["dispatch_workflows"],[])
        self.assertTrue(refs["unresolved"])

    def test_top_level_on_only(self):
        source="""name: Literal
on:
  workflow_dispatch:
jobs:
  test:
    steps:
      - run: |
          echo on:
          echo '  workflow_run:'
          echo '    workflows: ["Fake"]'
"""
        self.assertEqual(workflow_orchestration_references(source)["workflow_run_names"],[])

class CurrentSemanticReviewTests(unittest.TestCase):
    MAIN="a"*40
    HEAD="b"*40
    BLOB="c"*40

    def row(self,number=80,head=None,blob=None):
        return {"number":number,"head_sha":head or self.HEAD,
                "file_blob_comparisons":[{"path":"paper_pov/results_report.py",
                                          "pr_blob_sha":blob or self.BLOB}]}

    def matrix(self,number=80,head=None,blob=None):
        return {"schema":"cryptoscanner-current-semantic-pr-review-v1",
                "main_sha":self.MAIN,
                "prs":[{"number":number,"head_sha":head or self.HEAD,
                        "classification":"integrated","source_path":"paper_pov/results_report.py",
                        "source_blob_sha":blob or self.BLOB,
                        "reason":"Source-reviewed score/UTC behavior",
                        "release_authorized":False,"cleanup_authorized":False}]}

    def test_checked_in_matrix_is_complete_and_sha_bound_before_network(self):
        import json
        from pathlib import Path
        matrix=json.loads(Path("audit_tools/pr_semantic_current_20261102.json").read_text())
        rows=matrix["prs"]
        self.assertEqual(len(rows),22)
        self.assertEqual(len({x["number"] for x in rows}),22)
        self.assertEqual(len(matrix["main_sha"]),40)
        self.assertTrue(all(len(x["head_sha"])==40 and
                            len(x["source_blob_sha"])==40 and
                            x["source_path"] and
                            x["release_authorized"] is False and
                            x["cleanup_authorized"] is False for x in rows))
        self.assertEqual(matrix["review_status"],"PROVISIONAL_NOT_CERTIFIED")

    def test_pr40_raw_only_contract_is_not_marked_integrated(self):
        import json
        from pathlib import Path
        matrix=json.loads(Path("audit_tools/pr_semantic_current_20261102.json").read_text())
        pr=next(x for x in matrix["prs"] if x["number"]==40)
        self.assertEqual(pr["classification"],"conflicting")
        self.assertIn("paper-ledger.json",pr["reason"])
        self.assertIn("paper-segment-manifest.json",pr["reason"])
        self.assertFalse(pr["cleanup_authorized"])
        self.assertFalse(pr["release_authorized"])

    def test_exact_main_head_and_blob_give_provisional_disposition(self):
        rows=[self.row()]
        result=apply_semantic_review(self.matrix(),rows,self.MAIN)
        self.assertEqual(result["current_validated_count"],1)
        self.assertEqual(rows[0]["semantic_classification"],"integrated")
        self.assertFalse(result["certified"])
        self.assertFalse(result["cleanup_authorized"])

    def test_changed_pr_head_is_unknown_even_when_file_blob_matches(self):
        rows=[self.row(head="d"*40)]
        result=apply_semantic_review(self.matrix(),rows,self.MAIN)
        self.assertEqual(rows[0]["semantic_classification"],"unknown")
        self.assertEqual(rows[0]["semantic_review_reason"],"PR_HEAD_DRIFT")
        self.assertEqual(result["current_validated_count"],0)

    def test_changed_main_is_unknown_even_when_pr_head_matches(self):
        rows=[self.row()]
        apply_semantic_review(self.matrix(),rows,"d"*40)
        self.assertEqual(rows[0]["semantic_review_reason"],"MAIN_DRIFT")

    def test_changed_source_blob_is_unknown_even_with_matching_head(self):
        rows=[self.row(blob="d"*40)]
        apply_semantic_review(self.matrix(),rows,self.MAIN)
        self.assertEqual(rows[0]["semantic_review_reason"],"PR_SOURCE_BLOB_DRIFT_OR_MISSING")

    def test_self_modifying_audit_pr_cannot_self_certify(self):
        rows=[self.row(number=121)]
        apply_semantic_review(self.matrix(number=121),rows,self.MAIN)
        self.assertFalse(rows[0]["semantic_review_valid"])
        self.assertEqual(rows[0]["semantic_classification"],"unknown")

    def test_new_and_closed_prs_explicitly_recorded(self):
        rows=[self.row(),self.row(number=126)]
        result=apply_semantic_review(self.matrix(number=80),rows,self.MAIN)
        self.assertEqual(result["missing_prs"],[126])
        self.assertEqual(rows[1]["semantic_classification"],"unknown")
        result=apply_semantic_review(self.matrix(number=80),[self.row(number=126)],self.MAIN)
        self.assertEqual(result["no_longer_open_prs"],[80])

    def test_duplicate_and_release_claims_fail_closed(self):
        matrix=self.matrix()
        matrix["prs"].append(dict(matrix["prs"][0]))
        with self.assertRaisesRegex(ValueError,"Duplicate"):
            apply_semantic_review(matrix,[self.row()],self.MAIN)
        matrix=self.matrix()
        matrix["prs"][0]["cleanup_authorized"]=True
        with self.assertRaisesRegex(ValueError,"cannot authorize"):
            apply_semantic_review(matrix,[self.row()],self.MAIN)

    def test_missing_or_invalid_source_blob_cannot_validate_disposition(self):
        for blob in (None,"bad"):
            matrix=self.matrix()
            if blob is None:
                matrix["prs"][0].pop("source_blob_sha")
            else:
                matrix["prs"][0]["source_blob_sha"]=blob
            with self.subTest(blob=blob):
                with self.assertRaisesRegex(ValueError,"source blob SHA"):
                    apply_semantic_review(matrix,[self.row()],self.MAIN)

    def test_malformed_source_head_and_schema_fail_closed(self):
        matrix=self.matrix()
        matrix["prs"][0]["head_sha"]="short"
        with self.assertRaisesRegex(ValueError,"Malformed"):
            apply_semantic_review(matrix,[self.row()],self.MAIN)
        matrix=self.matrix()
        matrix["schema"]="unknown"
        with self.assertRaisesRegex(ValueError,"schema"):
            apply_semantic_review(matrix,[self.row()],self.MAIN)


class WorkflowTriggerSourceTests(unittest.TestCase):
    def test_shell_fake_schedule_and_dispatch_not_reported(self):
        source="""name: Safe\non:\n  push:\njobs:\n  check:\n    steps:\n      - run: |\n          echo 'workflow_dispatch:'\n          echo 'schedule:'\n          echo 'cron: 9,39 * * * *'\n"""
        w=inventory_workflow_source(".github/workflows/safe.yml",source)
        self.assertFalse(w["has_dispatch"])
        self.assertFalse(w["has_schedule"])
        self.assertEqual(w["schedule_cron"],[])

    def test_real_cron_and_dispatch_parsed(self):
        source="""name: Writer\non:\n  schedule:\n    - cron: '9,39 * * * *'\n  workflow_dispatch:\njobs:\n  run:\n    steps: []\n"""
        w=inventory_workflow_source(".github/workflows/paper-pipeline.yml",source)
        self.assertTrue(w["has_dispatch"])
        self.assertTrue(w["has_schedule"])
        self.assertEqual(w["schedule_cron"],["9,39 * * * *"])

    def test_inline_triggers_not_dropped(self):
        w=inventory_workflow_source(".github/workflows/inline.yml", "name: Inline\non: [push, workflow_dispatch]\n")
        self.assertTrue(w["has_dispatch"])
        self.assertFalse(w["has_schedule"])


class DeclaredWriteSurfaceTests(unittest.TestCase):
    def test_canonical_and_legacy_writers_are_distinct(self):
        source_main="""name: Paper
on:
  schedule:
    - cron: '9,39 * * * *'
permissions:
  contents: write
steps:
  - run: git push origin HEAD:refs/heads/paper-proof-ledger
"""
        source_legacy="""name: Legacy
on:
  schedule:
    - cron: '3,33 * * * *'
permissions:
  contents: write
steps:
  - uses: actions/checkout@v4
    with:
      ref: simplified-scanner-recovery-20261011
  - run: git push origin HEAD:refs/heads/simple-history
"""
        workflows=[inventory_workflow_source(".github/workflows/paper-pipeline.yml",source_main),
                   inventory_workflow_source(".github/workflows/kraken-recovery-schedule.yml",source_legacy)]
        census=classify_declared_write_surfaces(workflows,"a"*40)
        surfaces={r["workflow"]:r for r in census["surfaces"]}
        self.assertEqual(surfaces[".github/workflows/paper-pipeline.yml"]["write_destination_evidence"],"PAPER_LEDGER_REFERENCE")
        self.assertEqual(surfaces[".github/workflows/kraken-recovery-schedule.yml"]["write_destination_evidence"],"LEGACY_SIMPLE_HISTORY_REFERENCE")
        self.assertTrue(all(not r["execution_proven"] for r in census["surfaces"]))
        self.assertFalse(census["cleanup_authorized"])

    def test_unknown_write_destination_not_silently_classified_as_dead(self):
        unknown=inventory_workflow_source(".github/workflows/unknown.yml",
            "name: Unknown\\npermissions:\\n  contents: write\\nsteps:\\n  - run: echo maybe\\n")
        read_only=inventory_workflow_source(".github/workflows/read.yml",
            "name: Read\\npermissions:\\n  contents: read\\n")
        census=classify_declared_write_surfaces([unknown,read_only],"a"*40)
        self.assertEqual(census["unknown_write_destinations"],[".github/workflows/unknown.yml"])
        self.assertEqual(len(census["surfaces"]),1)
        self.assertFalse(census["surfaces"][0]["safe_to_delete"])


class ExternalRuntimeEvidenceTests(unittest.TestCase):
    MAIN = "a" * 40
    def snapshot(self, timestamp="2026-11-02T02:17:00Z", main=None):
        return {"schema":"cryptoscanner-external-runtime-audit-v1",
                "snapshot_utc":timestamp, "repo_main_sha":main or self.MAIN,
                "supabase":{"deployed_edge_functions":27}, "railway":{"active_deployments":0}}

    def at(self, iso):
        import datetime
        return datetime.datetime.fromisoformat(iso.replace("Z","+00:00"))

    def test_matching_recent_snapshot_is_still_not_live_authentication(self):
        x=assess_external_runtime_snapshot(self.snapshot(),self.MAIN,
                                           self.at("2026-11-02T02:20:00Z"))
        self.assertEqual(x["reason"],"SNAPSHOT_ONLY_NO_LIVE_AUTHENTICATION")
        self.assertEqual(x["age_seconds"],180)
        self.assertFalse(x["runtime_coverage_certified"])
        self.assertFalse(x["cleanup_authorized"])

    def test_stale_snapshot_is_explicitly_untrusted(self):
        x=assess_external_runtime_snapshot(self.snapshot(),self.MAIN,
                                           self.at("2026-11-02T06:30:00Z"))
        self.assertEqual(x["reason"],"STALE_SNAPSHOT")
        self.assertFalse(x["age_within_limit"])

    def test_changed_main_invalidates_even_recent_snapshot(self):
        x=assess_external_runtime_snapshot(self.snapshot(), "b"*40,
                                           self.at("2026-11-02T02:20:00Z"))
        self.assertEqual(x["reason"],"MAIN_SHA_MISMATCH")
        self.assertFalse(x["source_main_matches"])

    def test_future_or_malformed_timestamp_fails_closed(self):
        x=assess_external_runtime_snapshot(self.snapshot(),self.MAIN,
                                           self.at("2026-11-02T02:00:00Z"))
        self.assertEqual(x["reason"],"FUTURE_SNAPSHOT")
        with self.assertRaisesRegex(ValueError,"timestamp"):
            assess_external_runtime_snapshot(self.snapshot("2026-11-02T02:17:00"),self.MAIN)
        with self.assertRaisesRegex(ValueError,"schema"):
            assess_external_runtime_snapshot({"schema":"invented"},self.MAIN)

    def test_counts_do_not_masquerade_as_live_coverage(self):
        snap=self.snapshot()
        snap["supabase"]["deployed_edge_functions"]=0
        snap["railway"]["active_deployments"]=10
        x=assess_external_runtime_snapshot(snap,self.MAIN,self.at("2026-11-02T02:20:00Z"))
        self.assertEqual(x["evidence_class"],"snapshot_only")
        self.assertFalse(x["runtime_invocations_verified"])
        self.assertFalse(x["database_scheduler_verified"])


class AuditCertificationGateTests(unittest.TestCase):
    def test_unresolved_semantics_consumers_and_writer_are_explicit(self):
        semantic={"open_pr_count":22,"current_validated_count":12}
        graph={"unknowns":["dynamic checkout","unverified gateway"]}
        writes={"unknown_write_destinations":[".github/workflows/unknown.yml"]}
        runtime={"runtime_coverage_certified":False,"reason":"STALE_SNAPSHOT"}
        gate=audit_gate_decision(semantic,graph,writes,runtime,"a"*40,"b"*40)
        self.assertEqual(gate["status"],"NOT_CERTIFIED")
        self.assertEqual(gate["unresolved_pr_count"],10)
        self.assertEqual(gate["unknown_consumer_count"],2)
        self.assertEqual(gate["unknown_write_destination_count"],1)
        self.assertIn("EXTERNAL_RUNTIME_UNATTESTED",[b["id"] for b in gate["blockers"]])
        self.assertFalse(gate["cleanup_authorized"])

    def test_no_static_unknowns_does_not_fake_independent_certification(self):
        gate=audit_gate_decision(
            {"open_pr_count":1,"current_validated_count":1},
            {"unknowns":[]},{"unknown_write_destinations":[]},
            {"runtime_coverage_certified":False,"reason":"SNAPSHOT_ONLY_NO_LIVE_AUTHENTICATION"},
            "a"*40,"b"*40)
        self.assertEqual([x["id"] for x in gate["blockers"]],
                         ["EXTERNAL_RUNTIME_UNATTESTED","INDEPENDENT_VERIFIER_APPROVAL_MISSING"])
        self.assertFalse(gate["production_mutation_authorized"])


if __name__=="__main__":
    unittest.main()
