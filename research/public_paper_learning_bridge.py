"""Read-only E bridge for real paper artifacts lacking authenticated acquisition receipts.

Paper outcomes are descriptive, NEVER source-qualified E1 labels or held-out lift.
"""
import argparse
from collections import Counter
import hashlib
import json
from pathlib import Path

from paper_pov.ledger import verify
from research.learning_feedback import decide

HORIZONS = (1, 6, 24, 48)


def evaluate(ledger, *, baseline_version="paper-baseline", challenger_version="paper-challenger"):
    verify(ledger)
    predictions = ledger["predictions"]
    by_id = {p["prediction_id"]: p for p in predictions}
    if len(by_id) != len(predictions):
        raise ValueError("duplicate prediction identity")
    # Neither the sealed paper ticker nor its price observations authenticate
    # contemporaneous Kraken depth, bid/ask or score-to-source associations.
    authenticated = sum(
        isinstance(p.get("source_sha256"), str)
        and isinstance(p.get("score_observed_at"), (int, float))
        and isinstance(p.get("entry_first_observed_at"), (int, float))
        for p in predictions)
    if authenticated:
        raise ValueError("unexpected acquisition claims: use verified depth binder")
    counts = {}
    for hours in HORIZONS:
        rows = [o for o in ledger["outcomes"] if o["horizon_hours"] == hours]
        if any(o["prediction_id"] not in by_id for o in rows):
            raise ValueError("orphan outcome")
        status = dict(sorted(Counter(o["status"] for o in rows).items()))
        counts[str(hours)] = {"paper_outcomes": len(rows), "paper_status_counts": status,
                              "authenticated_entry_labels": 0,
                              "held_out_n": 0, "rule": "NO QUALIFIED RULE"}
    evidence_sha = hashlib.sha256(json.dumps(
        {"ledger_sha256": ledger["sha256"], "counts": counts},
        sort_keys=True, separators=(",", ":")).encode()).hexdigest()
    shadow = decide({"production_applied": False, "held_out_n": 0,
                     "held_out_lift": None, "rule": "NO QUALIFIED RULE"},
                    baseline_version=baseline_version,
                    challenger_version=challenger_version,
                    evidence_sha256=evidence_sha)
    return {"mode": "REAL_PAPER_DESCRIPTIVE_NOT_AUTHENTICATED_DEPTH",
            "ledger_sha256": ledger["sha256"],
            "paper_predictions": len(predictions),
            "paper_observations": len(ledger["observations"]),
            "horizons": counts, "shadow_decision": shadow,
            "missing": ["acquisition_time_score_receipts",
                        "authenticated_depth_associations",
                        "prospective_round_index_with_contiguous_quotes"],
            "production_applied": False}


def main():
    p = argparse.ArgumentParser()
    p.add_argument("--ledger", required=True)
    p.add_argument("--output", required=True)
    args = p.parse_args()
    report = evaluate(json.loads(Path(args.ledger).read_bytes()))
    output = Path(args.output)
    with output.open("x") as stream:
        json.dump(report, stream, sort_keys=True, indent=2, allow_nan=False)
        stream.write("\n")
    print(json.dumps(report, sort_keys=True))


if __name__ == "__main__":
    main()
