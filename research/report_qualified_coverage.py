"""E1/E2 factual source coverage and learning-readiness report.

Distinguishes right-censored entries at the end of a capture from actual
missing intermediate observations. Never turns an incomplete path into a loss.
"""
import argparse
from collections import Counter, defaultdict
import json
from pathlib import Path
from research.prospective_round_store import evaluate_index


def coverage(evidence):
    counts=Counter(o["status"] for o in evidence["outcomes"])
    per_pair=defaultdict(lambda:Counter())
    gaps=0
    right_censored=0
    for row in evidence["outcomes"]:
        per_pair[row["pair"]][row["status"]]+=1
        if row["status"]=="ABSTAIN_INCOMPLETE":
            observed=row.get("observed_forward_slots",0)
            expected=row.get("expected_forward_slots",12)
            if observed<expected:
                # A later complete entry for the same pair means this is a
                # genuine gap, not simply end-of-collection censoring.
                later=[o for o in evidence["outcomes"] if o["pair"]==row["pair"]
                       and o["entry_first_observed_at"]>row["entry_first_observed_at"]]
                if any(o["status"]=="QUALIFIED_OBSERVED_PATH" for o in later):
                    gaps+=1
                else:
                    right_censored+=1
    qualified=[o for o in evidence["outcomes"] if o["status"]=="QUALIFIED_OBSERVED_PATH"]
    positive=sum(o["ge30pct"] is True for o in qualified)
    return {"rounds_verified":evidence["rounds_verified"],
            "snapshots_verified":evidence["snapshots_verified"],
            "outcomes_total":len(evidence["outcomes"]),
            "status_counts":dict(sorted(counts.items())),
            "source_abstentions":len(evidence["abstentions"]),
            "right_censored_entries":right_censored,
            "incomplete_with_later_qualified_path":gaps,
            "qualified_entries":len(qualified),
            "qualified_positive_30pct":positive,
            "qualified_negative_30pct":len(qualified)-positive,
            "pairs":{p:dict(sorted(c.items())) for p,c in sorted(per_pair.items())},
            "held_out_lift":None,"rule":"NO QUALIFIED RULE",
            "production_applied":False}


def main():
    p=argparse.ArgumentParser()
    p.add_argument("--round-index",required=True)
    p.add_argument("--horizon-hours",type=int,default=1,choices=(1,6,24,48))
    p.add_argument("--output",required=True)
    args=p.parse_args()
    result=coverage(evaluate_index(args.round_index,args.horizon_hours))
    path=Path(args.output)
    if path.exists():
        raise FileExistsError("immutable coverage report already exists")
    path.parent.mkdir(parents=True,exist_ok=True)
    with path.open("x") as out:
        json.dump(result,out,sort_keys=True,indent=2)
        out.write("\n")
    print("SOURCE_QUALIFIED_COVERAGE",json.dumps(result,sort_keys=True))


if __name__=="__main__":
    main()
