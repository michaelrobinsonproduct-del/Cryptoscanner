"""E2/E3 read-only paper-ledger reconciliation with authenticated depth episodes.

The paper ticker has client-observed timestamps but no depth-source SHA.
It is NEVER silently relabeled as a source-qualified depth prediction.
"""
import argparse
import json
from collections import Counter
from pathlib import Path

from paper_pov.ledger import verify
from paper_pov.scanner import utc
from research.prospective_round_store import evaluate_index
from research.chronological_challenger import compare
from research.learning_feedback import decide


def reconcile(ledger, evidence, *, split_at, baseline_version, challenger_version,
              evidence_sha256):
    verify(ledger)
    predictions=ledger["predictions"]
    outcomes=evidence["outcomes"]
    if evidence.get("production_applied") is not False:
        raise ValueError("nonresearch source outcomes")
    by_pair={}
    for outcome in outcomes:
        key=(outcome["pair"],outcome["entry_first_observed_at"])
        if key in by_pair:
            raise ValueError("duplicate source outcome")
        by_pair[key]=outcome
    receipts=[]
    excluded=Counter()
    # A paper prediction is timestamped by the scanner run, not by a depth
    # receipt. Even a same-pair, same-second match is not source authentication.
    for p in predictions:
        if "source_sha256" not in p or "entry_first_observed_at" not in p:
            excluded["PAPER_TICKER_LACKS_DEPTH_SOURCE_RECEIPT"]+=1
            continue
        key=(p["pair"],p["entry_first_observed_at"])
        o=by_pair.get(key)
        if o is None:
            excluded["NO_AUTHENTICATED_MATCHING_OUTCOME"]+=1
            continue
        if p["source_sha256"]!=o["entry_source_sha256"]:
            excluded["DEPTH_SOURCE_SHA_MISMATCH"]+=1
            continue
        # Historical ledger cannot gain a source receipt after the fact:
        # a valid pre-entry receipt must be explicitly persisted.
        if "score_observed_at" not in p or p["score_observed_at"]>o["entry_first_observed_at"]:
            excluded["NO_PRE_ENTRY_SCORE_RECEIPT"]+=1
            continue
        receipts.append({**o,"baseline_score":p["baseline_score"],
                         "challenger_score":p["challenger_score"]})
    comparison=compare(receipts,split_at=split_at)
    comparison["excluded"].update(excluded)
    comparison["source_rounds_verified"]=evidence["rounds_verified"]
    comparison["source_snapshots_verified"]=evidence["snapshots_verified"]
    comparison["source_qualified_episodes"]=evidence["qualified_first_entry_episodes"]
    comparison["source_abstentions"]=len(evidence["abstentions"])
    comparison["paper_predictions_examined"]=len(predictions)
    decision=decide(comparison,baseline_version=baseline_version,
                    challenger_version=challenger_version,evidence_sha256=evidence_sha256)
    return {"comparison":comparison,"shadow_decision":decision}


def main():
    import hashlib
    parser=argparse.ArgumentParser()
    parser.add_argument("--paper-ledger",required=True)
    parser.add_argument("--round-index",required=True)
    parser.add_argument("--split-at",required=True,type=float)
    parser.add_argument("--baseline-version",required=True)
    parser.add_argument("--challenger-version",required=True)
    args=parser.parse_args()
    ledger_bytes=Path(args.paper_ledger).read_bytes()
    index_bytes=Path(args.round_index).read_bytes()
    ledger=json.loads(ledger_bytes)
    evidence=evaluate_index(args.round_index,1)
    result=reconcile(ledger,evidence,split_at=args.split_at,
                     baseline_version=args.baseline_version,
                     challenger_version=args.challenger_version,
                     evidence_sha256=hashlib.sha256(ledger_bytes+index_bytes).hexdigest())
    print(json.dumps(result,sort_keys=True,allow_nan=False))


if __name__=="__main__":
    main()
