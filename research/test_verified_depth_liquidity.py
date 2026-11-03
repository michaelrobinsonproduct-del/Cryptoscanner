"""E2 raw depth-to-qualified-outcome-to-scorer liquidity contract."""
import hashlib
import json
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch
from research.prospective_outcome_adapter import verified_rows
from research.evaluate_challenger import evaluate

def fixture(root, *, size="0.25", price="100", pair="XBTUSD"):
    market="XXBTZUSD"
    depth=json.dumps({"error":[],"result":{market:{"asks":[[price,size,"1700000000"]],"bids":[["99","1","1700000000"]]}}}).encode()
    trades=b'{"error":[],"result":{"XXBTZUSD":[["99","1","1700000000"]],"last":"1"}}'
    receipts=[]
    for stage,raw in (("depth",depth),("trades",trades)):
        name=f"{stage}.json"
        (root/name).write_bytes(raw)
        receipts.append({"stage":stage,"file":name,"bytes":len(raw),"sha256":hashlib.sha256(raw).hexdigest()})
    evidence={"pair_requested":pair,"pair_source":market,"eligible_point_in_time_snapshot":True,
              "depth_receipt":{"sha256":receipts[0]["sha256"],"first_observed_at":1700000002},
              "trades_receipt":{"sha256":receipts[1]["sha256"],"first_observed_at":1700000002},
              "newest_trade_event_at":"1700000000","bid_level_event_at":"1700000000",
              "ask_level_event_at":"1700000000","best_bid":"99","best_ask":"100"}
    (root/"evidence.json").write_text(json.dumps(evidence))
    (root/"manifest.json").write_text(json.dumps({
        "mode":"ONE_SHOT_PROSPECTIVE_PUBLIC_TLS_RESEARCH_ONLY","pairs_requested":1,
        "entries":[{"pair":pair,"status":"ELIGIBLE","source_market":market,
                    "evidence_file":"evidence.json","raw":receipts}]}))
    return receipts[0]["sha256"]

class VerifiedDepthLiquidityTests(unittest.TestCase):
    def test_raw_depth_proves_executable_ask_notional(self):
        with tempfile.TemporaryDirectory() as tmp:
            fixture(Path(tmp))
            rows, abstentions=verified_rows(tmp)
            self.assertEqual(abstentions,[])
            self.assertEqual(rows[0]["entry_liquidity_usd"],25.0)

    def test_mismatch_fails_closed(self):
        with tempfile.TemporaryDirectory() as tmp:
            fixture(Path(tmp),price="101")
            with self.assertRaisesRegex(ValueError,"depth/evidence ask mismatch"):
                verified_rows(tmp)

    def test_missing_liquidity_cannot_be_invented_by_scores(self):
        with tempfile.TemporaryDirectory() as tmp:
            root=Path(tmp)
            sha=fixture(root,size="0.01")
            outcome={"pair":"XBTUSD","entry_first_observed_at":1700000002,
                     "entry_source_sha256":sha,"entry_liquidity_usd":1.0,
                     "status":"QUALIFIED_OBSERVED_PATH","ge30pct":False}
            scores=[{"pair":"XBTUSD","entry_first_observed_at":1700000002,
                     "source_sha256":sha,"observed_at":1700000001,
                     "baseline_score":0.2,"challenger_score":0.3,
                     "entry_liquidity_usd":999999.0}]
            path=root/"scores.json"
            path.write_text(json.dumps(scores))
            with patch("research.evaluate_challenger.evaluate_index",
                       return_value={"rounds_verified":13,"snapshots_verified":52,
                                     "abstentions":[],"outcomes":[outcome]}):
                result=evaluate("unused",path,1700001000)
            self.assertEqual(result["excluded"]["INSUFFICIENT_ENTRY_LIQUIDITY"],1)
            self.assertIsNone(result["held_out_lift"])

if __name__=="__main__":
    unittest.main()
