import json
import tempfile
import unittest
from pathlib import Path
from research.learning_feedback import decide,append_decision

SHA="b"*64


class LearningFeedbackTests(unittest.TestCase):
    def comparison(self,lift=0.5,n=40):
        return {"production_applied":False,"held_out_n":n,"held_out_lift":lift,
                "baseline":{"top_decile_n":4,"top_decile_hits":1},
                "challenger":{"top_decile_n":4,"top_decile_hits":3}}

    def decision(self,comparison):
        return decide(comparison,baseline_version="baseline-v1",challenger_version="challenger-v2",
                      evidence_sha256=SHA)

    def test_qualified_improvement_is_shadow_only(self):
        d=self.decision(self.comparison())
        self.assertEqual(d["decision"],"SHADOW_ELIGIBLE_REVIEW")
        self.assertEqual(d["active_shadow_version"],"challenger-v2")
        self.assertFalse(d["production_applied"])

    def test_no_improvement_or_insufficient_evidence_keeps_baseline(self):
        for comparison in (self.comparison(lift=0),self.comparison(n=3),
                           {"production_applied":False,"held_out_n":0,"held_out_lift":None}):
            d=self.decision(comparison)
            self.assertEqual(d["decision"],"KEEP_BASELINE")
            self.assertEqual(d["active_shadow_version"],"baseline-v1")

    def test_inconsistent_lift_cannot_promote(self):
        self.assertEqual(self.decision(self.comparison(lift=0.9))["decision"],"KEEP_BASELINE")

    def test_append_and_tamper_detection(self):
        with tempfile.TemporaryDirectory() as tmp:
            path=Path(tmp)/"ledger.jsonl"
            d=self.decision(self.comparison())
            first=append_decision(path,d)
            second=append_decision(path,self.decision(self.comparison(n=3)))
            self.assertEqual(second["previous_sha256"],first["record_sha256"])
            records=path.read_text().splitlines()
            row=json.loads(records[0])
            row["decision"]["active_shadow_version"]="forged"
            path.write_text(json.dumps(row)+"\n"+records[1]+"\n")
            with self.assertRaisesRegex(ValueError,"tampered"):
                append_decision(path,d)

    def test_production_write_rejected(self):
        with tempfile.TemporaryDirectory() as tmp:
            d=self.decision(self.comparison())
            d["production_applied"]=True
            with self.assertRaisesRegex(ValueError,"production"):
                append_decision(Path(tmp)/"ledger",d)


if __name__=="__main__":
    unittest.main()
