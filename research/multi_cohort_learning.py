"""Read-only E1-E3 multi-cohort source-qualified learning entry point.

Supply separate, retained scored-series directories; each source index,
score receipt and depth association is independently verified. No historical
backfill, orders, scorer promotion or production writes.
"""
import argparse
import json
from research.authenticated_learning_loop import evaluate_cohorts
from research.acquisition_receipt_pipeline import write_new


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--cohort", action="append", required=True,
                        help="retained scored-series directory (repeat for distinct cohorts)")
    parser.add_argument("--output", required=True, help="new research-only report path")
    parser.add_argument("--shadow-ledger", help="optional append-only research decision ledger")
    args = parser.parse_args()
    result = evaluate_cohorts(args.cohort, ledger_path=args.shadow_ledger)
    result["report_sha256"] = write_new(args.output, result)
    p = result["horizons"]["48"]["comparison"]
    print(json.dumps({"cohorts": result["cohorts"], "qualified_48h": p["qualified_n"],
                      "held_out_n": p["held_out_n"], "held_out_lift": p["held_out_lift"],
                      "rule": p["rule"], "shadow_decision": result["shadow_decision"]["decision"],
                      "production_applied": False}, sort_keys=True))


if __name__ == "__main__":
    main()
