"""Read-only adapter for externally verified, source-qualified forward labels.

This adapter does NOT authenticate Kraken archives. The caller must supply a
separately verified receipt and source-qualified outcome records. Unverified
rows abstain; neither predictions nor missing candles create synthetic labels.
"""
import argparse
import json
import os
import tempfile
from pathlib import Path
from datetime import datetime, timedelta, timezone
from .shadow_learning_evidence import utc_time, evaluate_shadow_release, canonical_digest

HORIZONS = (1, 6, 24, 48)

def normalized_utc(value):
    """Normalize aware source timestamps without accepting naive times."""
    if not isinstance(value, str):
        raise ValueError("Missing timestamp")
    parsed = datetime.fromisoformat(value.replace("Z", "+00:00"))
    if parsed.tzinfo is None or parsed.utcoffset() is None:
        raise ValueError("Timestamp lacks timezone")
    return parsed.astimezone(timezone.utc)



def build_heldout_evidence(outcomes, baseline_decisions, challenger_decisions, *,
                           training_end_utc, holdout_start_utc, evaluation_asof_utc,
                           baseline_version, challenger_version, source_receipt=None,
                           minimum_holdout=30):
    """Join identical point-in-time prediction IDs, reject incomplete evidence.

    outcomes: records with prediction_id, entry_utc, feature_asof_utc,
    horizon_hours, hit, source_sha256, source_authenticated,
    liquidity_qualified, coverage_complete, label_mature_utc.
    Each decision mapping must explicitly cover every eligible 48h row.
    """
    train = utc_time(training_end_utc)
    start = utc_time(holdout_start_utc)
    cutoff = utc_time(evaluation_asof_utc)
    if start < train + timedelta(hours=48):
        raise ValueError("Holdout violates 48h purge")
    if not isinstance(outcomes, list) or not isinstance(baseline_decisions, dict) or not isinstance(challenger_decisions, dict):
        raise ValueError("Invalid outcome or decision input")
    eligible = {}
    abstentions = {}
    for record in outcomes:
        if not isinstance(record, dict):
            raise ValueError("Malformed outcome")
        key = record.get("prediction_id")
        horizon = record.get("horizon_hours")
        if not isinstance(key, str) or not key or type(horizon) is not int or horizon not in HORIZONS:
            raise ValueError("Invalid prediction identity or horizon")
        identity = (key, horizon)
        if identity in eligible or identity in abstentions:
            raise ValueError("Duplicate prediction/horizon")
        reason = None
        try:
            entry = normalized_utc(record["entry_utc"])
            feature = normalized_utc(record["feature_asof_utc"])
            mature = normalized_utc(record["label_mature_utc"])
            if entry < start or feature > entry or mature < entry + timedelta(hours=horizon) or mature > cutoff:
                reason = "OUT_OF_WINDOW_OR_IMMATURE"
        except (KeyError, ValueError, TypeError):
            reason = "INVALID_TIME"
        if not reason and record.get("coverage_complete") is not True:
            reason = "INCOMPLETE_SOURCE_COVERAGE"
        if not reason and (record.get("source_authenticated") is not True or record.get("liquidity_qualified") is not True):
            reason = "UNQUALIFIED_SOURCE_OR_LIQUIDITY"
        digest = record.get("source_sha256")
        if not reason and (not isinstance(digest, str) or len(digest) != 64 or any(c not in "0123456789abcdef" for c in digest.lower())):
            reason = "INVALID_SOURCE_DIGEST"
        if not reason and type(record.get("hit")) is not bool:
            reason = "UNKNOWN_OUTCOME"
        if reason:
            abstentions[identity] = reason
        else:
            eligible[identity] = record
    # One immutable event per prediction across ALL horizons, including abstentions.
    # Normalize equivalent UTC offsets; never let malformed abstaining evidence
    # bypass the cross-horizon join or silently redefine its source identity.
    by_prediction = {}
    for record in outcomes:
        key = record["prediction_id"]
        if not all(field in record for field in ("entry_utc", "feature_asof_utc", "source_sha256")):
            raise ValueError("Missing cross-horizon prediction/source identity")
        try:
            entry_identity = normalized_utc(record["entry_utc"])
            feature_identity = normalized_utc(record["feature_asof_utc"])
        except (TypeError, ValueError):
            # Even an all-abstaining prediction must preserve an auditable
            # immutable event identity. Otherwise a later qualified horizon
            # could silently attach to a different event.
            raise ValueError("Invalid cross-horizon prediction/source identity")
        digest = record["source_sha256"]
        if not isinstance(digest, str) or len(digest) != 64 or any(c not in "0123456789abcdef" for c in digest.lower()):
            raise ValueError("Invalid cross-horizon prediction/source identity")
        identity = (entry_identity, feature_identity, digest.lower())
        if key in by_prediction and by_prediction[key] != identity:
            raise ValueError("Cross-horizon prediction/source identity mismatch")
        by_prediction[key] = identity
    # A complete four-horizon outcome is required for a comparable learning
    # cohort. A valid 48h label alone must not hide missing 1/6/24h evidence.
    selected = {}
    incomplete_predictions = {}
    all_predictions = sorted({key for key, _ in eligible} | {key for key, _ in abstentions})
    for key in all_predictions:
        missing = [h for h in HORIZONS if (key, h) not in eligible]
        if missing:
            incomplete_predictions[key] = missing
        else:
            selected[key] = eligible[(key, 48)]
    if set(selected) != set(baseline_decisions) or set(selected) != set(challenger_decisions):
        raise ValueError("Decisions do not cover identical eligible 48h cohort")
    if any(type(v) is not bool for v in baseline_decisions.values()) or any(type(v) is not bool for v in challenger_decisions.values()):
        raise ValueError("Non-binary decision")
    def versioned(version, decisions):
        rows = []
        for key in sorted(selected):
            record = selected[key]
            rows.append(dict(prediction_id=key, partition="held_out", horizon_hours=48,
                             source_authenticated=True, liquidity_qualified=True,
                             source_sha256=record["source_sha256"], hit=record["hit"],
                             watch=decisions[key], entry_utc=normalized_utc(record["entry_utc"]).isoformat(),
                             feature_asof_utc=normalized_utc(record["feature_asof_utc"]).isoformat(),
                             label_mature_utc=normalized_utc(record["label_mature_utc"]).isoformat(),
                             holdout_start_utc=holdout_start_utc))
        return dict(version=version, training_end_utc=training_end_utc,
                    evaluation_asof_utc=evaluation_asof_utc, source_receipt=source_receipt,
                    observations=rows)
    result = evaluate_shadow_release(versioned(baseline_version, baseline_decisions),
                                     versioned(challenger_version, challenger_decisions),
                                     minimum_holdout=minimum_holdout)
    # The receipt is a claim until independently checked against actual bytes.
    # Never authorize evidence qualification from a caller-supplied receipt alone.
    result["source_receipt_qualified"] = False
    result["status"] = "NO_QUALIFIED_RULE"
    result["promotion_authorized"] = False
    result["outcome_coverage"] = {str(h): sum(k[1] == h for k in eligible) for h in HORIZONS}
    # Descriptive labels are counts from caller-provided rows, NOT authenticated
    # Kraken history or measured learning lift. Preserve full four-horizon
    # hit/miss distribution for downstream read-only B reporting.
    result["eligible_horizon_counts"] = {
        str(h): {"hits": sum(record["hit"] is True for (key, hh), record in eligible.items() if hh == h),
                 "misses": sum(record["hit"] is False for (key, hh), record in eligible.items() if hh == h)}
        for h in HORIZONS}
    # Distinguish the four-horizon comparable cohort from all individually
    # eligible rows. A partial prediction must never inflate comparable hit
    # rates or be mistaken for an independently verified historical win.
    result["complete_cohort_horizon_counts"] = {
        str(h): {
            "hits": sum(eligible[(key, h)]["hit"] is True for key in selected),
            "misses": sum(eligible[(key, h)]["hit"] is False for key in selected),
        } for h in HORIZONS
    }
    result["complete_cohort_horizon_rates"] = {
        str(h): (result["complete_cohort_horizon_counts"][str(h)]["hits"] / len(selected)
                 if selected else None) for h in HORIZONS
    }
    result["source_qualified_prediction_count"] = len(selected)
    result["counts_independently_authenticated"] = False
    result["abstention_counts"] = {reason: list(abstentions.values()).count(reason)
                                    for reason in sorted(set(abstentions.values()))}
    result["source_authentication_verified_by_adapter"] = False
    result["incomplete_prediction_horizons"] = {key: missing for key, missing in sorted(incomplete_predictions.items())}
    result["four_horizon_complete_predictions"] = len(selected)
    result["observed_prediction_count"] = len(all_predictions)
    result["excluded_prediction_count"] = len(all_predictions) - len(selected)
    result["baseline_challenger_same_cohort"] = True
    result["cohort_join_digest"] = canonical_digest(sorted(selected))
    return result


def project_learning_handoff(result):
    """Minimal read-only B integration contract; never carries an executable rule."""
    if (not isinstance(result, dict) or result.get("schema") != "shadow_learning_evidence_v1"
            or result.get("promotion_authorized") is not False
            or result.get("production_applied") is not False
            or result.get("status") != "NO_QUALIFIED_RULE"
            or result.get("source_authentication_verified_by_adapter") is not False
            or result.get("source_receipt_qualified") is not False
            or result.get("counts_independently_authenticated") is not False
            or result.get("measured_lift_verified") is True
            or result.get("live_watch_authorized") is True
            or result.get("source_authenticated") is True):
        raise ValueError("Unsafe or unverified learning handoff")
    return {"schema": "paper_learning_handoff_v1", "status": "NO_QUALIFIED_RULE",
            "baseline_version": result["baseline_version"],
            "challenger_version": result["challenger_version"],
            "evaluation_asof_utc": result["evaluation_asof_utc"],
            "evidence_digest": result["evidence_digest"],
            "cohort_join_digest": result["cohort_join_digest"],
            "observed_prediction_count": result["observed_prediction_count"],
            "complete_cohort_count": result["four_horizon_complete_predictions"],
            "excluded_prediction_count": result["excluded_prediction_count"],
            "complete_cohort_horizon_counts": result["complete_cohort_horizon_counts"],
            "complete_cohort_horizon_rates": result["complete_cohort_horizon_rates"],
            "abstention_counts": result["abstention_counts"],
            "incomplete_prediction_horizons": result["incomplete_prediction_horizons"],
            "source_authenticated": False, "measured_lift_verified": False,
            "live_watch_authorized": False, "promotion_authorized": False,
            "production_applied": False, "read_only": True}


def main(argv=None):
    """Read-only B handoff: JSON input to explicit non-promotable evidence JSON."""
    parser = argparse.ArgumentParser(description="Build non-promotable held-out evidence")
    parser.add_argument("input_json", type=Path)
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--delivery-output", type=Path, help="Separate non-promotable B learning handoff")
    args = parser.parse_args(argv)
    payload = json.loads(args.input_json.read_text(encoding="utf-8"))
    if not isinstance(payload, dict):
        raise ValueError("Evidence input must be an object")
    result = build_heldout_evidence(**payload)
    if result["promotion_authorized"] or result["status"] != "NO_QUALIFIED_RULE":
        raise ValueError("Unverified evidence must not authorize release")
    if args.delivery_output and args.delivery_output == args.output:
        raise ValueError("Learning handoff and full evidence must use separate paths")
    if args.output.exists() or (args.delivery_output and args.delivery_output.exists()):
        raise FileExistsError("Refusing to overwrite existing evidence")
    rendered = [(args.output, json.dumps(result, sort_keys=True, indent=2, allow_nan=False) + "\n")]
    if args.delivery_output:
        rendered.append((args.delivery_output, json.dumps(
            project_learning_handoff(result), sort_keys=True, indent=2, allow_nan=False) + "\n"))
    if len({path.resolve() for path, _ in rendered}) != len(rendered):
        raise ValueError("Learning outputs must have distinct paths")
    staged, published = [], []
    try:
        for destination, content in rendered:
            with tempfile.NamedTemporaryFile(mode="w", encoding="utf-8",
                                             dir=destination.parent, prefix=".heldout-",
                                             delete=False) as handle:
                staged.append(Path(handle.name))
                handle.write(content)
                handle.flush()
                os.fsync(handle.fileno())
        for (destination, _), temporary in zip(rendered, staged):
            # Exclusive publication cannot overwrite a concurrent worker.
            os.link(temporary, destination)
            published.append(destination)
    except Exception:
        for destination in published:
            destination.unlink(missing_ok=True)
        raise
    finally:
        for temporary in staged:
            temporary.unlink(missing_ok=True)
    return result


if __name__ == "__main__":
    main()
