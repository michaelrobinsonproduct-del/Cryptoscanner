"""Research-only E2 CLI: join authenticated E1 labels to point-in-time score receipts."""
import argparse
import json
from pathlib import Path
from research.prospective_round_store import evaluate_index
from research.chronological_challenger import compare
from research.learning_feedback import decide, append_decision
import hashlib


def evaluate(index_path, scores_path, split_at):
    evidence=evaluate_index(index_path,1)
    score_rows=json.loads(Path(scores_path).read_text())
    if not isinstance(score_rows,list):
        raise ValueError("score receipts must be a list")
    by_key={}
    for score in score_rows:
        if not isinstance(score, dict):
            raise ValueError("invalid score receipt")
        if not isinstance(score.get("source_sha256"), str) or len(score["source_sha256"]) != 64 or any(c not in "0123456789abcdef" for c in score["source_sha256"]):
            raise ValueError("score receipt missing authenticated source hash")
        key=(score["pair"],score["entry_first_observed_at"])
        if key in by_key:
            raise ValueError("duplicate score receipt")
        if (type(score.get("observed_at")) not in (int,float)
                or score["observed_at"] > score["entry_first_observed_at"]
                or score["observed_at"] < 0):
            raise ValueError("score was not available at entry")
        if score["source_sha256"] != score.get("entry_source_sha256",score["source_sha256"]):
            raise ValueError("score source receipt mismatch")
        by_key[key]=score
    joined=[]
    for outcome in evidence["outcomes"]:
        key=(outcome["pair"],outcome["entry_first_observed_at"])
        scores=by_key.get(key,{})
        if scores and scores["source_sha256"] != outcome.get("entry_source_sha256"):
            raise ValueError("prediction source receipt does not match verified entry")
        joined.append({**outcome,
                       "baseline_score":scores.get("baseline_score"),
                       "challenger_score":scores.get("challenger_score"),
                       "entry_liquidity_usd":outcome.get("entry_liquidity_usd")})
    result=compare(joined,split_at=split_at)
    result["source_rounds_verified"]=evidence["rounds_verified"]
    result["source_snapshots_verified"]=evidence["snapshots_verified"]
    result["source_abstentions"]=len(evidence["abstentions"])
    return result


def main():
    p=argparse.ArgumentParser()
    p.add_argument("--round-index",required=True)
    p.add_argument("--score-receipts",required=True)
    p.add_argument("--split-at",required=True,type=float)
    p.add_argument("--baseline-version")
    p.add_argument("--challenger-version")
    p.add_argument("--learning-ledger")
    args=p.parse_args()
    result=evaluate(args.round_index,args.score_receipts,args.split_at)
    print("CHRONOLOGICAL_CHALLENGER",json.dumps(result,sort_keys=True))
    if args.learning_ledger:
        if not args.baseline_version or not args.challenger_version:
            p.error("learning ledger requires both version IDs")
        evidence_hash=hashlib.sha256(
            (Path(args.round_index).read_bytes()+Path(args.score_receipts).read_bytes())).hexdigest()
        decision=decide(result,baseline_version=args.baseline_version,
                        challenger_version=args.challenger_version,
                        evidence_sha256=evidence_hash)
        record=append_decision(args.learning_ledger,decision)
        print("SHADOW_LEARNING_DECISION",json.dumps(record,sort_keys=True))


if __name__=="__main__":
    main()
