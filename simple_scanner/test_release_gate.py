import unittest
from simple_scanner.release_gate import validate, REQUIRED

class ReleaseGateTests(unittest.TestCase):
    def test_fails_closed_without_real_history(self):
        with self.assertRaisesRegex(ValueError, "actual_history_replay"):
            validate({"commit_sha":"abc"}, "abc")

    def test_rejects_synthetic_evidence_and_partial_coverage(self):
        e={"commit_sha":"abc", **{key:{"passed":True} for key in REQUIRED}}
        e["actual_history_replay"].update({"source":"synthetic", "rows":100})
        e["identity_coverage"].update({"verified":100, "total":100})
        with self.assertRaisesRegex(ValueError, "Real historical"):
            validate(e,"abc")
        e["actual_history_replay"]["source"]="production_sqlite_backup"
        e["identity_coverage"]["verified"]=99
        with self.assertRaisesRegex(ValueError, "Canonical identities"):
            validate(e,"abc")

    def test_exact_commit_required(self):
        e={"commit_sha":"abc", **{key:{"passed":True} for key in REQUIRED}}
        e["actual_history_replay"].update({"source":"production_sqlite_backup", "rows":100})
        e["identity_coverage"].update({"verified":100, "total":100})
        with self.assertRaisesRegex(ValueError, "exact release commit"):
            validate(e,"different")
        with self.assertRaisesRegex(ValueError, "previous production commit"):
            validate(e,"abc")
        e["rollback_verified"]["production_commit"]="d"*40
        self.assertTrue(validate(e,"abc"))

if __name__=="__main__":
    unittest.main()
