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


def bind_a2_projection(projection, predictions):
    """Consume the retained, receipt-bound A2 full-universe E projection.

    The projection is diagnostic evidence, not independent publisher authentication.
    All non-WATCH identities remain explicit in the B cohort.
    """
    from .historical_preselection_binding import bind_preselection_history
    if not isinstance(projection, dict) or projection.get("schema") != "a2_historical_e_preselection_v1":
        raise ValueError("Invalid retained A2 projection")
    if (projection.get("status") != "NO_QUALIFIED_RULE" or
            projection.get("source_authenticated") is not False or
            projection.get("historical_outcomes_available") is not False or
            projection.get("promotion_authorized") is not False or
            projection.get("production_applied") is not False):
        raise ValueError("Unsafe A2 projection qualification")
    receipt = projection.get("a_receipt_sha256")
    if not isinstance(receipt, str) or len(receipt) != 64 or any(c not in "0123456789abcdef" for c in receipt):
        raise ValueError("Missing A2 receipt identity")
    frozen, watches = projection.get("frozen_predictions"), projection.get("e1_watch_predictions")
    if not isinstance(frozen, list) or not isinstance(watches, list) or not frozen:
        raise ValueError("Missing A2 frozen universe")
    ids = [p.get("prediction_id") for p in frozen if isinstance(p, dict)]
    if len(ids) != len(frozen) or len(set(ids)) != len(ids):
        raise ValueError("Duplicate A2 frozen identity")
    for p in frozen:
        if not isinstance(p.get("pair"), str) or not p["pair"] or not isinstance(p.get("prediction_id"), str) or len(p["prediction_id"]) != 64:
            raise ValueError("Malformed A2 frozen identity")
    watch_ids = {p.get("prediction_id") for p in watches if isinstance(p, dict)}
    if len(watch_ids) != len(watches) or not watch_ids.issubset(set(ids)):
        raise ValueError("Invalid A2 WATCH subset")
    if predictions != watches:
        # Order is irrelevant, but the identity, time and decision are not.
        def indexed(rows):
            return {p["prediction_id"]: p for p in rows}
        if not isinstance(predictions, list) or len(predictions) != len(watches) or indexed(predictions) != indexed(watches):
            raise ValueError("E1 predictions differ from sealed A2 WATCH sample")
    if (projection.get("frozen_observation_count") != len(frozen) or
            projection.get("watch_count") != len(watches) or
            projection.get("nonwatch_without_outcomes") != len(frozen) - len(watches)):
        raise ValueError("A2 frozen universe arithmetic mismatch")
    return {"frozen_predictions": frozen, "e1_watch_predictions": watches,
            "preselection_observation_count": len(frozen),
            "watch_outcome_input_count": len(watches),
            "unobserved_nonwatch_count": len(frozen) - len(watches),
            "a_receipt_sha256": receipt, "unbiased_learning_qualified": False}


def run_pipeline(manifest, root, schema, partitions, predictions, observed_until, *, preselection_history=None, a2_projection=None):
    if preselection_history is not None and a2_projection is not None:
        raise ValueError("Select one frozen A provenance source")
    binding = bind_a2_projection(a2_projection, predictions) if a2_projection is not None else None
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
    parser.add_argument("--a2-projection", help="Retained E A2 receipt-bound preselection JSON")
    parser.add_argument("--a-receipts-dir", help="Original sealed A receipts; verify via A export_receipt_history")
    args = parser.parse_args(argv)
    if sum(bool(v) for v in (args.preselection_history, args.a_receipts_dir, args.a2_projection)) > 1:
        parser.error("Select only one A preselection provenance source")
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
                          preselection_history=history,
                          a2_projection=read("a2_projection") if args.a2_projection else None)
    output.write_text(json.dumps(result, sort_keys=True, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"prediction_count": result["execution"]["prediction_count"],
                      "status_counts": result["execution"]["status_counts"],
                      "qualified_cohort_count": result["handoff"]["qualified_cohort_count"],
                      "learning_status": result["delivery"]["status"]}, sort_keys=True))


if __name__ == "__main__":
    main()
