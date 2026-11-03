import unittest
from research.chronological_challenger import compare, PURGE_SECONDS


class ChallengerTests(unittest.TestCase):
    def row(self, i, t, hit=False, b=0.1, c=0.1):
        return {"pair":f"P{i}", "entry_first_observed_at":t,
                "status":"QUALIFIED_OBSERVED_PATH","ge30pct":hit,
                "baseline_score":b,"challenger_score":c}

    def test_purge_and_identical_held_out_cohort(self):
        split=1_000_000
        rows=[self.row(i,split-PURGE_SECONDS-100-i) for i in range(20)]
        rows += [self.row(30,split-10,True)]
        rows += [self.row(100+i,split+300*i,i==0,
                          1.0 if i==1 else 0.1,1.0 if i==0 else 0.1)
                 for i in range(20)]
        result=compare(rows,split_at=split)
        self.assertEqual(result["train_n"],20)
        self.assertEqual(result["held_out_n"],20)
        self.assertEqual(result["excluded"]["PURGED_48H"],1)
        self.assertEqual(result["baseline"]["top_decile_hits"],0)
        self.assertEqual(result["challenger"]["top_decile_hits"],1)
        self.assertEqual(result["held_out_lift"],0.5)
        self.assertEqual(result["rule"],"NO QUALIFIED RULE")
        self.assertFalse(result["production_applied"])

    def test_no_scores_or_unqualified_never_imply_lift(self):
        rows=[self.row(1,1)]
        rows[0]["status"]="ABSTAIN_INCOMPLETE"
        self.assertIsNone(compare(rows,split_at=2)["held_out_lift"])
        rows[0]["status"]="QUALIFIED_OBSERVED_PATH"
        del rows[0]["challenger_score"]
        self.assertEqual(compare(rows,split_at=2)["excluded"]["MISSING_POINT_IN_TIME_SCORES"],1)

    def test_duplicate_rejected(self):
        row=self.row(1,100)
        with self.assertRaisesRegex(ValueError,"duplicate"):
            compare([row,row],split_at=200)


if __name__=="__main__":
    unittest.main()
