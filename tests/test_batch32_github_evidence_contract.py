"""Batch 32 offline evidence-contract acceptance; no GitHub API calls."""
import unittest
from pathlib import Path
from simple_scanner.fixture_github_evidence_contract import authenticated_comment_ids
from simple_scanner.fixture_receipt_reconciliation import marker
from simple_scanner.manual_acknowledgement_policy import acknowledgement_decision

ISSUE=81
RUN="run-1"
DIGEST="a"*64
TOKEN=marker(ISSUE,RUN,DIGEST)
AUTHOR="trusted-bot"

def snapshot(comments=None,**overrides):
    value={"complete":True,"issue_number":ISSUE,"comments":comments if comments is not None else []}
    value.update(overrides)
    return value

def comment(cid=900,body=TOKEN,author=AUTHOR,issue=ISSUE):
    return {"id":cid,"body":body,"author":author,"issue_number":issue}

class Batch32EvidenceTests(unittest.TestCase):
    def test_complete_matching_evidence_can_feed_pure_policy(self):
        ids=authenticated_comment_ids(ISSUE,RUN,DIGEST,snapshot([comment()]),AUTHOR)
        self.assertEqual(ids,[900])
        decision=acknowledgement_decision([{"issue_number":ISSUE}],[{"issue_number":ISSUE,"comment_id":ids[0]}])
        self.assertEqual(decision["acknowledge_issue_numbers"],[ISSUE])

    def test_incomplete_pagination_blocks_confirmation(self):
        with self.assertRaises(ValueError):
            authenticated_comment_ids(ISSUE,RUN,DIGEST,snapshot([comment()],complete=False),AUTHOR)

    def test_issue_binding_rejects_foreign_snapshot_or_comment(self):
        for evidence in (snapshot([comment()],issue_number=82),snapshot([comment(issue=82)])):
            with self.subTest(evidence=evidence),self.assertRaises(ValueError):
                authenticated_comment_ids(ISSUE,RUN,DIGEST,evidence,AUTHOR)

    def test_untrusted_author_rejected_even_with_exact_marker(self):
        with self.assertRaises(ValueError):
            authenticated_comment_ids(ISSUE,RUN,DIGEST,snapshot([comment(author="other-bot")]),AUTHOR)

    def test_duplicate_comment_ids_or_markers_fail_closed(self):
        for comments in ([comment(),comment()], [comment(),comment(cid=901)]):
            with self.subTest(comments=comments),self.assertRaises(ValueError):
                authenticated_comment_ids(ISSUE,RUN,DIGEST,snapshot(comments),AUTHOR)

    def test_ambiguous_post_without_receipt_is_unresolved(self):
        ids=authenticated_comment_ids(ISSUE,RUN,DIGEST,snapshot([comment(body="unrelated")]),AUTHOR)
        self.assertEqual(ids,[])
        decision=acknowledgement_decision([{"issue_number":ISSUE}],[])
        self.assertEqual(decision["status"],"RECONCILIATION_REQUIRED")
        self.assertFalse(decision["scan_rerun_required"])
        self.assertEqual(decision["safe_to_repost_issue_numbers"],[])

    def test_embedded_marker_is_not_a_valid_confirmation(self):
        ids=authenticated_comment_ids(ISSUE,RUN,DIGEST,snapshot([comment(body="prefix"+TOKEN+"suffix")]),AUTHOR)
        self.assertEqual(ids,[])

    def test_no_production_execution_integration(self):
        source=(Path(__file__).resolve().parents[1]/"simple_scanner/execute_once.py").read_text()
        self.assertNotIn("fixture_github_evidence_contract",source)
        self.assertNotIn("manual_acknowledgement_policy",source)

if __name__=="__main__":
    unittest.main()
