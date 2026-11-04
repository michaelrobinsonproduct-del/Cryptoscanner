"""Run the existing E1 historical reconstruction and E-to-B learning handoff.

All input files are caller-supplied pinned historical archive evidence.
Never fetches live data, modifies scanner state or certifies source authenticity.
"""
import argparse
import json
from pathlib import Path

from .historical_outcome_execution import run_historical_outcomes
from .historical_execution_learning_bridge import project_historical_execution
from .historical_preselection_binding import bind_preselection_history


def run_pipeline(manifest, root, schema, partitions, predictions, observed_until, *, preselection_history=None):
    binding = None
    if preselection_history is not None:
        binding = bind_preselection_history(preselection_history, predictions)
    execution = run_historical_outcomes(
        manifest, root, schema, partitions, predictions, observed_until)
    frozen = binding["frozen_predictions"] if binding is not None else predictions
    handoff = project_historical_execution(execution, frozen_predictions=frozen)
    # Consume B's existing strict read-only learning contract rather than
    # introducing a second evaluator or reimplementing its qualification.
    from .github_delivery_projection import _learning_evidence
    delivery = _learning_evidence(handoff)
    if delivery["status"] != "NO_QUALIFIED_RULE" or delivery["promotion_authorized"]:
        raise ValueError("Historical source cannot authorize a learning rule")
    return {"execution": execution, "handoff": handoff, "delivery": delivery,
            "preselection_binding": binding}


def main(argv=None):
    parser = argparse.ArgumentParser(description="E1 pinned historical outcomes to B read-only consumer")
    for key in ("manifest", "root", "schema", "partitions", "predictions", "observed-until", "output"):
        parser.add_argument("--" + key, required=True)
    parser.add_argument("--preselection-history", help="A receipt-verified historical full-universe JSON")
    parser.add_argument("--a-receipts-dir", help="Original sealed A receipts; verify via A export_receipt_history")
    args = parser.parse_args(argv)
    if args.preselection_history and args.a_receipts_dir:
        parser.error("Use either --preselection-history or --a-receipts-dir")
    output = Path(args.output)
    if output.exists():
        raise FileExistsError("Refusing to overwrite prior historical evidence")
    def read(name):
        return json.loads(Path(getattr(args, name)).read_text(encoding="utf-8"))
    history = read("preselection_history") if args.preselection_history else None
    if args.a_receipts_dir:
        from .preselection_universe import export_receipt_history
        history = export_receipt_history(args.a_receipts_dir)
    result = run_pipeline(read("manifest"), args.root, read("schema"),
                          read("partitions"), read("predictions"), args.observed_until,
                          preselection_history=history)
    output.write_text(json.dumps(result, sort_keys=True, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"prediction_count": result["execution"]["prediction_count"],
                      "status_counts": result["execution"]["status_counts"],
                      "qualified_cohort_count": result["handoff"]["qualified_cohort_count"],
                      "learning_status": result["delivery"]["status"]}, sort_keys=True))


if __name__ == "__main__":
    main()
