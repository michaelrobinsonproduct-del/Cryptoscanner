"""Read-only adapter for externally verified, source-qualified forward labels.

This adapter does NOT authenticate Kraken archives. The caller must supply a
separately verified receipt and source-qualified outcome records. Unverified
rows abstain; neither predictions nor missing candles create synthetic labels.
"""
import argparse
import json
from pathlib import Path
from datetime import timedelta
from math import isfinite
from .shadow_learning_evidence import utc_time, evaluate_shadow_release, canonical_digest

HORIZONS = (1, 6, 24, 48)



def reconstruct_forward_outcomes(predictions, candles, *, evaluation_asof_utc):
    """Reconstruct real 1/6/24/48h forward outcomes from supplied timestamped candles.

    Candles must be source-backed observations, never interpolated prices.
    This function deliberately does not authenticate the source: downstream
    evidence must independently verify the archive before qualifying a rule.
    """
    from datetime import timedelta
    asof = utc_time(evaluation_asof_utc)
    by_pair = {}
    for candle in candles:
        pair = candle["pair"]
        timestamp = utc_time(candle["timestamp_utc"])
        close = float(candle["close"])
        high = float(candle["high"])
        if not (isfinite(close) and isfinite(high) and 0 < close <= high):
            raise ValueError("Invalid observed candle price")
        by_pair.setdefault(pair, []).append((timestamp, close, high))
    for observations in by_pair.values():
        observations.sort(key=lambda item: item[0])
        if len({item[0] for item in observations}) != len(observations):
            raise ValueError("Duplicate candle timestamp")
    outcomes = []
    seen = set()
    for prediction in predictions:
        key = prediction["prediction_id"]
        if key in seen:
            raise ValueError("Duplicate prediction")
        seen.add(key)
        entry = utc_time(prediction["entry_utc"])
        feature = utc_time(prediction["feature_asof_utc"])
        if feature > entry:
            raise ValueError("Prediction features occur after entry")
        price = float(prediction["entry_price"])
        if not isfinite(price) or price <= 0:
            raise ValueError("Invalid entry price")
        observations = by_pair.get(prediction["pair"], [])
        for horizon in HORIZONS:
            end = entry + timedelta(hours=horizon)
            observed = [(t, close, high) for t, close, high in observations if entry < t <= end]
            mature = end <= asof
            # A missing interval cannot be silently treated as a miss.
            complete = mature and bool(observed) and all(
                observed[i][0] - observed[i - 1][0] == timedelta(minutes=5)
                for i in range(1, len(observed))
            ) and observed[0][0] == entry + timedelta(minutes=5) and observed[-1][0] == end
            max_return = max((high / price - 1 for _, _, high in observed), default=None)
            close_return = observed[-1][1] / price - 1 if complete else None
            outcomes.append({
                "prediction_id": key, "pair": prediction["pair"],
                "entry_utc": prediction["entry_utc"],
                "feature_asof_utc": prediction["feature_asof_utc"],
                "horizon_hours": horizon, "label_mature_utc": end.isoformat(),
                "entry_price": price, "close_return": close_return,
                "max_favorable_return": max_return if complete else None,
                "hit": max_return >= 0.30 if complete else None,
                "coverage_complete": complete,
                "source_sha256": prediction.get("source_sha256"),
                "source_authenticated": False,
                "liquidity_qualified": prediction.get("liquidity_qualified") is True,
                "outcome_status": "MATURE" if complete else
                    ("IMMATURE" if not mature else "MISSING_CANDLES"),
            })
    return outcomes


def train_shadow_challenger(predictions, outcomes, *, training_end_utc,
                            holdout_start_utc, feature_names):
    """Learn from mature historical +30% labels without changing live scoring."""
    training_end = utc_time(training_end_utc)
    holdout_start = utc_time(holdout_start_utc)
    if holdout_start < training_end + timedelta(hours=48):
        raise ValueError("48h chronological purge required")
    labels = {}
    for outcome in outcomes:
        if outcome.get("horizon_hours") != 48 or outcome.get("coverage_complete") is not True:
            continue
        if type(outcome.get("hit")) is not bool:
            continue
        if utc_time(outcome["label_mature_utc"]) > training_end:
            continue
        key = outcome["prediction_id"]
        if key in labels:
            raise ValueError("Duplicate training label")
        labels[key] = outcome["hit"]
    training = []
    heldout = []
    for prediction in predictions:
        entry = utc_time(prediction["entry_utc"])
        if utc_time(prediction["feature_asof_utc"]) > entry:
            raise ValueError("Feature lookahead")
        values = prediction.get("features", {})
        if not all(isinstance(values.get(k), (int, float)) and isfinite(values[k]) for k in feature_names):
            continue
        if entry < training_end and prediction["prediction_id"] in labels:
            training.append((prediction, labels[prediction["prediction_id"]]))
        elif entry >= holdout_start:
            heldout.append(prediction)
    positives = [p for p, hit in training if hit]
    negatives = [p for p, hit in training if not hit]
    state = {"schema": "shadow_challenger_v1", "training_count": len(training),
             "positive_count": len(positives), "negative_count": len(negatives),
             "holdout_count": len(heldout), "training_end_utc": training_end_utc,
             "holdout_start_utc": holdout_start_utc, "feature_names": list(feature_names),
             "promotion_authorized": False, "production_applied": False}
    if not positives or not negatives or not feature_names:
        state["status"] = "INSUFFICIENT_LABEL_VARIETY"
        state["shadow_decisions"] = {}
    else:
        centers = {key: sum(p["features"][key] for p, _ in training) / len(training)
                   for key in feature_names}
        scales = {key: max((sum((p["features"][key] - centers[key]) ** 2
                                  for p, _ in training) / len(training)) ** 0.5, 1e-9)
                  for key in feature_names}
        weights = {key: (
            sum((p["features"][key] - centers[key]) / scales[key] for p in positives) / len(positives)
            - sum((p["features"][key] - centers[key]) / scales[key] for p in negatives) / len(negatives))
            for key in feature_names}
        state["feature_weights"] = weights
        state["feature_centers"] = centers
        state["feature_scales"] = scales
        state["shadow_scores"] = {
            p["prediction_id"]: sum((p["features"][key] - centers[key]) / scales[key] * weights[key]
                                    for key in feature_names) for p in heldout}
        state["status"] = "SHADOW_ONLY"
    state["version"] = canonical_digest(state)
    return state


def evaluate_shadow_scores(challenger, outcomes, baseline_decisions, *, threshold=0.0):
    """Compare baseline and challenger on the identical matured 48h cohort."""
    if challenger.get("status") != "SHADOW_ONLY":
        return {"status": "NO_QUALIFIED_RULE", "reason": "INSUFFICIENT_TRAINING",
                "promotion_authorized": False}
    labels = {row["prediction_id"]: row["hit"] for row in outcomes
              if row.get("horizon_hours") == 48 and row.get("coverage_complete") is True
              and type(row.get("hit")) is bool
              and utc_time(row["label_mature_utc"]) <= utc_time(challenger["evaluation_asof_utc"])}
    scores = challenger["shadow_scores"]
    ids = sorted(set(scores) & set(labels))
    if set(ids) != set(scores) or set(ids) != set(baseline_decisions):
        return {"schema": "shadow_score_comparison_v1", "status": "INCOMPLETE_HELDOUT_COHORT",
                "missing_labels": len(set(scores) - set(labels)),
                "missing_baseline": len(set(scores) - set(baseline_decisions)),
                "promotion_authorized": False, "production_applied": False}
    def metrics(decisions):
        watched = [key for key in ids if decisions[key]]
        hits = sum(labels[key] for key in watched)
        movers = sum(labels[key] for key in ids)
        return {"cohort": len(ids), "watched": len(watched), "true_positives": hits,
                "false_positives": len(watched) - hits,
                "precision": hits / len(watched) if watched else None,
                "recall": hits / movers if movers else None,
                "coverage": len(watched) / len(ids) if ids else None,
                "missed_movers": movers - hits}
    base = metrics(baseline_decisions)
    shadow = metrics({key: scores[key] >= threshold for key in ids})
    return {"schema": "shadow_score_comparison_v1", "status": "SHADOW_EVALUATED",
            "challenger_version": challenger["version"], "baseline": base,
            "challenger": shadow, "cohort_ids_digest": canonical_digest(ids),
            "measured_lift_verified": False, "promotion_authorized": False,
            "production_applied": False}


def build_shadow_learning_state(predictions, candles, baseline_decisions, *,
                                training_end_utc, holdout_start_utc,
                                evaluation_asof_utc, feature_names):
    """Compose the outcome, learning, and evaluation stages into one paper-only state."""
    outcomes = reconstruct_forward_outcomes(
        predictions, candles, evaluation_asof_utc=evaluation_asof_utc)
    challenger = train_shadow_challenger(
        predictions, outcomes, training_end_utc=training_end_utc,
        holdout_start_utc=holdout_start_utc, feature_names=feature_names)
    challenger["evaluation_asof_utc"] = evaluation_asof_utc
    comparison = evaluate_shadow_scores(challenger, outcomes, baseline_decisions)
    result = {"schema": "paper_learning_state_v1",
              "evaluation_asof_utc": evaluation_asof_utc,
              "outcome_count": len(outcomes),
              "matured_count": sum(o["outcome_status"] == "MATURE" for o in outcomes),
              "hit_counts": {str(h): sum(o["horizon_hours"] == h and o["hit"] is True
                                         for o in outcomes) for h in HORIZONS},
              "challenger": challenger, "comparison": comparison,
              "source_authenticated": False, "promotion_authorized": False,
              "production_applied": False}
    result["state_digest"] = canonical_digest(result)
    return result


def save_shadow_learning_state(path, state):
    """Persist non-promotable learning evidence for a later paper-only reader."""
    if state.get("schema") != "paper_learning_state_v1" or state.get("promotion_authorized") is not False:
        raise ValueError("Unsafe learning state")
    target = Path(path)
    target.parent.mkdir(parents=True, exist_ok=True)
    data = json.dumps(state, sort_keys=True, indent=2, allow_nan=False) + "\n"
    if target.exists():
        previous = json.loads(target.read_text(encoding="utf-8"))
        if utc_time(previous["evaluation_asof_utc"]) > utc_time(state["evaluation_asof_utc"]):
            raise ValueError("Refusing to roll back learning generation")
    temporary = target.with_name(target.name + ".tmp")
    temporary.write_text(data, encoding="utf-8")
    temporary.replace(target)
    return state["state_digest"]


def read_shadow_learning_state(path):
    state = json.loads(Path(path).read_text(encoding="utf-8"))
    digest = state.pop("state_digest")
    if state.get("schema") != "paper_learning_state_v1":
        raise ValueError("Unexpected learning state schema")
    if digest != canonical_digest(state):
        raise ValueError("Learning state checksum mismatch")
    state["state_digest"] = digest
    if state.get("promotion_authorized") is not False or state.get("production_applied") is not False:
        raise ValueError("Learning state cannot change active scoring")
    return state


def build_heldout_evidence(outcomes, baseline_decisions, challenger_decisions, *,
                           training_end_utc, holdout_start_utc, evaluation_asof_utc,
                           baseline_version, challenger_version, source_receipt=None,
                           minimum_holdout=30, prediction_universe=None):
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
    # Optional immutable preselection universe prevents selection-on-label bias:
    # every prediction observed before outcomes were known must be accounted for.
    if prediction_universe is not None:
        if (not isinstance(prediction_universe, list) or
                any(not isinstance(k, str) or not k for k in prediction_universe) or
                len(set(prediction_universe)) != len(prediction_universe)):
            raise ValueError("Invalid or duplicate prediction universe")
        universe = set(prediction_universe)
    else:
        universe = None
    eligible = {}
    abstentions = {}
    for record in outcomes:
        if not isinstance(record, dict):
            raise ValueError("Malformed outcome")
        key = record.get("prediction_id")
        horizon = record.get("horizon_hours")
        if not isinstance(key, str) or not key or type(horizon) is not int or horizon not in HORIZONS:
            raise ValueError("Invalid prediction identity or horizon")
        if universe is not None and key not in universe:
            raise ValueError("Outcome outside frozen prediction universe")
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
    # A prediction is one point-in-time event across all horizons, including
    # abstaining horizons. A failed source/coverage horizon cannot silently
    # redefine the entry or feature cutoff used by a valid 48h row.
    for (key, horizon), record in list(eligible.items()) + [(k, next(
            r for r in outcomes if (r["prediction_id"], r["horizon_hours"]) == k))
            for k in abstentions]:
        if not all(field in record for field in ("entry_utc", "feature_asof_utc", "source_sha256")):
            continue
        identity = (record["entry_utc"], record["feature_asof_utc"], record["source_sha256"])
        if key in by_prediction and by_prediction[key] != identity:
            raise ValueError("Cross-horizon prediction/source identity mismatch")
        by_prediction[key] = identity
    # A complete four-horizon outcome is required for a comparable learning
    # cohort. A valid 48h label alone must not hide missing 1/6/24h evidence.
    selected = {}
    incomplete_predictions = {}
    observed_ids = {key for key, _ in eligible} | {key for key, _ in abstentions}
    all_predictions = sorted(universe if universe is not None else observed_ids)
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
    # Descriptive labels are counts from caller-provided rows, NOT authenticated
    # Kraken history or measured learning lift. Preserve full four-horizon
    # hit/miss distribution for downstream read-only B reporting.
    result["eligible_horizon_counts"] = {
        str(h): {"hits": sum(record["hit"] is True for (key, hh), record in eligible.items() if hh == h),
                 "misses": sum(record["hit"] is False for (key, hh), record in eligible.items() if hh == h)}
        for h in HORIZONS}
    result["source_qualified_prediction_count"] = len(selected)
    result["counts_independently_authenticated"] = False
    result["abstention_counts"] = {reason: list(abstentions.values()).count(reason)
                                    for reason in sorted(set(abstentions.values()))}
    result["source_authentication_verified_by_adapter"] = False
    result["incomplete_prediction_horizons"] = {key: missing for key, missing in sorted(incomplete_predictions.items())}
    result["four_horizon_complete_predictions"] = len(selected)
    result["observed_prediction_count"] = len(all_predictions)
    result["excluded_prediction_count"] = len(all_predictions) - len(selected)
    result["unlabeled_prediction_count"] = len(set(all_predictions) - observed_ids)
    result["prediction_universe_frozen"] = universe is not None
    result["prediction_universe_digest"] = canonical_digest(all_predictions) if universe is not None else None
    result["complete_cohort_fraction"] = len(selected) / len(all_predictions) if all_predictions else None
    result["baseline_challenger_same_cohort"] = True
    result["cohort_join_digest"] = canonical_digest(sorted(selected))
    return result


def project_learning_handoff(result):
    """Minimal read-only B integration contract; never carries an executable rule."""
    if (not isinstance(result, dict) or result.get("schema") != "shadow_learning_evidence_v1"
            or result.get("promotion_authorized") is not False
            or result.get("production_applied") is not False
            or result.get("status") != "NO_QUALIFIED_RULE"
            or result.get("source_authentication_verified_by_adapter") is not False):
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
            "unlabeled_prediction_count": result["unlabeled_prediction_count"],
            "prediction_universe_frozen": result["prediction_universe_frozen"],
            "prediction_universe_digest": result["prediction_universe_digest"],
            "complete_cohort_fraction": result["complete_cohort_fraction"],
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
    args.output.write_text(json.dumps(result, sort_keys=True, indent=2) + "\n", encoding="utf-8")
    if args.delivery_output:
        args.delivery_output.write_text(json.dumps(project_learning_handoff(result), sort_keys=True, indent=2) + "\n", encoding="utf-8")
    return result


if __name__ == "__main__":
    main()
