"""Read-only adapter for externally verified, source-qualified forward labels.

This adapter does NOT authenticate Kraken archives. The caller must supply a
separately verified receipt and source-qualified outcome records. Unverified
rows abstain; neither predictions nor missing candles create synthetic labels.
"""
import argparse
import json
from pathlib import Path
from datetime import timedelta
from .shadow_learning_evidence import utc_time, evaluate_shadow_release, canonical_digest

HORIZONS = (1, 6, 24, 48)


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
            entry = utc_time(record["entry_utc"])
            feature = utc_time(record["feature_asof_utc"])
            mature = utc_time(record["label_mature_utc"])
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
    # A single immutable prediction cannot acquire a different entry time,
    # feature cutoff or source identity at a later horizon. Reject conflicting
    # records rather than treating them as independent favorable labels.
    by_prediction = {}
    for (key, horizon), record in eligible.items():
        identity = (record["entry_utc"], record["feature_asof_utc"], record["source_sha256"])
        if key in by_prediction and by_prediction[key] != identity:
            raise ValueError("Cross-horizon prediction/source identity mismatch")
        by_prediction[key] = identity
    selected = {key: row for (key, horizon), row in eligible.items() if horizon == 48}
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
                             watch=decisions[key], entry_utc=record["entry_utc"],
                             feature_asof_utc=record["feature_asof_utc"],
                             label_mature_utc=record["label_mature_utc"],
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
    result["abstention_counts"] = {reason: list(abstentions.values()).count(reason)
                                    for reason in sorted(set(abstentions.values()))}
    result["source_authentication_verified_by_adapter"] = False
    result["cohort_join_digest"] = canonical_digest(sorted(selected))
    return result


def main(argv=None):
    """Read-only B handoff: JSON input to explicit non-promotable evidence JSON."""
    parser = argparse.ArgumentParser(description="Build non-promotable held-out evidence")
    parser.add_argument("input_json", type=Path)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args(argv)
    payload = json.loads(args.input_json.read_text(encoding="utf-8"))
    if not isinstance(payload, dict):
        raise ValueError("Evidence input must be an object")
    result = build_heldout_evidence(**payload)
    if result["promotion_authorized"] or result["status"] != "NO_QUALIFIED_RULE":
        raise ValueError("Unverified evidence must not authorize release")
    args.output.write_text(json.dumps(result, sort_keys=True, indent=2) + "\n", encoding="utf-8")
    return result


if __name__ == "__main__":
    main()
