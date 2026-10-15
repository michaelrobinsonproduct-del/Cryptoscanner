import unittest
from simple_scanner.model_versioning import fingerprint,plan_transition

class VersionTests(unittest.TestCase):
    def test_stable_fingerprint(self):
        self.assertEqual(fingerprint({"a":1,"b":2}),fingerprint({"b":2,"a":1}))
    def test_missing_evidence_rejected(self):
        self.assertFalse(plan_transition({"a":1},{"a":2},None,rollback_verified=True)["approved"])
    def test_rollback_unverified_rejected(self):
        self.assertFalse(plan_transition({"a":1},{"a":2},{"sufficient":True})["approved"])
    def test_identical_version_rejected(self):
        self.assertFalse(plan_transition({"a":1},{"a":1},{"sufficient":True},rollback_verified=True)["approved"])
    def test_invalid_weights_rejected(self):
        self.assertFalse(plan_transition({"a":1},{"a":float("nan")},{"sufficient":True},rollback_verified=True)["approved"])
    def test_proposal_does_not_mutate(self):
        old={"a":1};new={"a":2}
        result=plan_transition(old,new,{"sufficient":True},rollback_verified=True)
        self.assertTrue(result["approved"])
        self.assertEqual(result["rollback_to"],fingerprint(old))
        self.assertFalse(result["live_weights_modified"])
        self.assertFalse(result["buy_approved"])
        self.assertEqual(old,{"a":1})
