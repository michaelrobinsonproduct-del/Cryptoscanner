import json
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch
from research.evaluate_challenger import evaluate

SHA="a"*64


class ScoreJoinTests(unittest.TestCase):
    def outcome(self):
        return {"rounds_verified":13,"snapshots_verified":52,"abstentions":[],
                "outcomes":[{"pair":"XBTUSD","entry_first_observed_at":1000,
                             "entry_source_sha256":SHA,"status":"QUALIFIED_OBSERVED_PATH",
                             "ge30pct":False}]}

    def run_join(self, score):
        with tempfile.TemporaryDirectory() as directory:
            path=Path(directory)/"scores.json"
            path.write_text(json.dumps([score]))
            with patch("research.evaluate_challenger.evaluate_index",return_value=self.outcome()):
                return evaluate("unused",path,200000)

    def test_source_bound_early_score(self):
        result=self.run_join({"pair":"XBTUSD","entry_first_observed_at":1000,
                              "source_sha256":SHA,"observed_at":999,
                              "baseline_score":0.1,"challenger_score":0.2,"entry_liquidity_usd":100.0})
        self.assertEqual(result["train_n"],1)
        self.assertEqual(result["source_snapshots_verified"],52)
        self.assertIsNone(result["held_out_lift"])

    def test_missing_liquidity_is_explicit_abstention(self):
        score={"pair":"XBTUSD","entry_first_observed_at":1000,
               "source_sha256":SHA,"observed_at":999,
               "baseline_score":0.1,"challenger_score":0.2}
        result=self.run_join(score)
        self.assertEqual(result["excluded"]["MISSING_ENTRY_LIQUIDITY"],1)
        self.assertEqual(result["train_n"],0)

    def test_mismatched_sha_rejected(self):
        with self.assertRaisesRegex(ValueError,"does not match"):
            self.run_join({"pair":"XBTUSD","entry_first_observed_at":1000,
                           "source_sha256":"b"*64,"observed_at":999,
                           "baseline_score":0.1,"challenger_score":0.2})

    def test_late_score_rejected(self):
        with self.assertRaisesRegex(ValueError,"not available"):
            self.run_join({"pair":"XBTUSD","entry_first_observed_at":1000,
                           "source_sha256":SHA,"observed_at":1001,
                           "baseline_score":0.1,"challenger_score":0.2})


if __name__=="__main__":
    unittest.main()
