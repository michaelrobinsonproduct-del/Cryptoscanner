"""Read-only bridge from E1's real Kraken trade-bar reconstruction to B learning.

The upstream pinned-byte SHA is not independent Kraken publisher attestation.
Every next-bar proxy entry remains excluded from qualified learning.
"""
import argparse
import hashlib
import json
from pathlib import Path
from datetime import datetime, timezone

HORIZONS = (1, 6, 24, 48)

def normalized_source_time(value):
    """Compare offset-aware reconstructed timestamps to frozen UTC receipts."""
    if not isinstance(value, str):
        raise ValueError("Invalid reconstructed timestamp")
    parsed = datetime.fromisoformat(value.replace("Z", "+00:00"))
    if parsed.tzinfo is None or parsed.utcoffset() is None:
        raise ValueError("Reconstructed timestamp lacks timezone")
    return parsed.astimezone(timezone.utc)

STATUSES = ("MATURED_OBSERVED", "ABSTAIN_ENTRY", "ABSTAIN_IMMATURE", "ABSTAIN_GAP")


def project_historical_execution(execution, *, frozen_predictions, frozen_selections=None, frozen_observation_times=None):
    if not isinstance(execution, dict) or execution.get("schema") != "historical_outcome_execution_v1":
        raise ValueError("Unsupported historical execution")
    batch = execution.get("outcomes")
    if not isinstance(batch, dict) or batch.get("schema") != "qualified_ohlc_outcome_batch_v1":
        raise ValueError("Unsupported reconstructed outcomes")
    if execution.get("source_authenticated") is not False or batch.get("source_authenticated") is not False:
        raise ValueError("Unexpected authentication claim")
    if execution.get("qualified_for_learning") is not False or execution.get("promotion_authorized") is not False:
        raise ValueError("Unexpected qualification claim")
    if not isinstance(frozen_predictions, list) or not frozen_predictions:
        raise ValueError("Missing frozen pre-outcome universe")
    universe = {}
    for prediction in frozen_predictions:
        if not isinstance(prediction, dict):
            raise ValueError("Malformed frozen prediction")
        pid, pair = prediction.get("prediction_id"), prediction.get("pair")
        if not isinstance(pid, str) or not pid or not isinstance(pair, str) or not pair or pid in universe:
            raise ValueError("Duplicate or malformed frozen identity")
        universe[pid] = pair
    if frozen_selections is not None:
        if not isinstance(frozen_selections, dict) or set(frozen_selections) != set(universe):
            raise ValueError("Incomplete frozen A2 selection mapping")
        if any(value not in ("WATCH", "SCREEN_REJECTED", "NOT_OHLC_SELECTED", "OHLC_ABSTAINED", "NOT_RANKED_WATCH") for value in frozen_selections.values()):
            raise ValueError("Invalid frozen A2 selection")
    # Preserve the frozen pre-outcome timestamps for chronological diagnostic
    # evaluation. These caller-supplied times are not publisher attestation.
    if frozen_observation_times is not None:
        from .shadow_learning_evidence import utc_time
        if not isinstance(frozen_observation_times, dict) or set(frozen_observation_times) != set(universe):
            raise ValueError("Incomplete frozen A2 timestamp mapping")
        for value in frozen_observation_times.values():
            utc_time(value)
    records = batch.get("records")
    if not isinstance(records, list) or len(records) != batch.get("prediction_count"):
        raise ValueError("Invalid reconstructed record count")
    digest = execution.get("outcome_input_sha256")
    if (not isinstance(digest, str) or len(digest) != 64
            or any(ch not in "0123456789abcdef" for ch in digest)):
        raise ValueError("Missing or invalid input digest")
    if batch.get("source_sha256") != execution["outcome_input_sha256"]:
        raise ValueError("Inconsistent reconstruction digest")
    counts = {str(h): {status: 0 for status in STATUSES} for h in HORIZONS}
    seen = set()
    diagnostic_rows = []
    for record in records:
        if not isinstance(record, dict):
            raise ValueError("Malformed reconstructed record")
        pid = record.get("prediction_id")
        if pid in seen or pid not in universe or record.get("pair") != universe[pid]:
            raise ValueError("Reconstruction does not match frozen prediction universe")
        seen.add(pid)
        # E1 may carry the original prediction timestamp. If present it must
        # match the frozen A2 receipt, not a later reconstructed observation.
        if frozen_observation_times is not None:
            if not isinstance(record.get("as_of"), str):
                raise ValueError("Reconstructed prediction lacks frozen A2 timestamp")
            from .shadow_learning_evidence import utc_time
            if normalized_source_time(record["as_of"]) != utc_time(frozen_observation_times[pid]):
                raise ValueError("Reconstructed prediction time differs from frozen A2 observation")
        if record.get("source_authenticated") is not False or record.get("entry_method") != "next_5m_bar_open_proxy":
            raise ValueError("Unexpected entry qualification or authentication")
        if record.get("source_sha256") != batch["source_sha256"]:
            raise ValueError("Inconsistent record source digest")
        labels = record.get("labels")
        if not isinstance(labels, list) or len(labels) != len(HORIZONS):
            raise ValueError("Incomplete horizon record")
        observed = set()
        for label in labels:
            if not isinstance(label, dict):
                raise ValueError("Malformed horizon label")
            horizon, status = label.get("horizon_hours"), label.get("status")
            if type(horizon) is not int or horizon not in HORIZONS or horizon in observed or status not in STATUSES:
                raise ValueError("Invalid or duplicate reconstructed horizon")
            observed.add(horizon)
            if status == "MATURED_OBSERVED":
                if type(label.get("observed_30pct_hit")) is not bool or label.get("qualified_for_learning") is not False:
                    raise ValueError("Unqualified observed label malformed")
            elif label.get("observed_30pct_hit") is not None:
                raise ValueError("Abstaining horizon cannot carry a hit")
            # A source or qualification assertion on any horizon is unsafe,
            # including abstentions: do not allow contradictory evidence to
            # be republished as an explicitly unqualified B diagnostic.
            if label.get("source_authenticated") is True or label.get("qualified_for_learning") is True:
                raise ValueError("Reconstructed horizon claims unsupported qualification")
            counts[str(horizon)][status] += 1
            diagnostic_rows.append({
                "prediction_id": pid, "pair": universe[pid],
                "frozen_selection_status": frozen_selections[pid] if frozen_selections is not None else None,
                "observation_asof_utc": frozen_observation_times[pid] if frozen_observation_times is not None else None,
                "horizon_hours": horizon, "status": status,
                "observed_30pct_hit": label.get("observed_30pct_hit") if status == "MATURED_OBSERVED" else None,
                "source_sha256": record["source_sha256"],
                "source_authenticated": False, "liquidity_qualified": False,
                "qualified_for_learning": False,
            })
        if observed != set(HORIZONS):
            raise ValueError("Missing reconstructed horizon")
    diagnostic_rows.sort(key=lambda x: (x["prediction_id"], x["horizon_hours"]))
    diagnostic_hit_miss = {
        str(h): {
            "observed_hits_unqualified": sum(x["observed_30pct_hit"] is True for x in diagnostic_rows if x["horizon_hours"] == h),
            "observed_misses_unqualified": sum(x["observed_30pct_hit"] is False for x in diagnostic_rows if x["horizon_hours"] == h),
        } for h in HORIZONS
    }
    # Preserve missed-mover diagnostics across the entire frozen A2 cohort.
    # This is descriptive, never qualified lift: entry is a next-bar proxy
    # and the pinned archive is not independently publisher-authenticated.
    diagnostic_selection_outcomes = {
        str(h): {selection: {"observed_hits_unqualified": 0,
                             "observed_misses_unqualified": 0,
                             "abstained": 0}
                 for selection in ("WATCH", "SCREEN_REJECTED", "NOT_OHLC_SELECTED",
                                   "OHLC_ABSTAINED", "NOT_RANKED_WATCH")}
        for h in HORIZONS
    } if frozen_selections is not None else None
    if diagnostic_selection_outcomes is not None:
        for row in diagnostic_rows:
            bucket = diagnostic_selection_outcomes[str(row["horizon_hours"])][row["frozen_selection_status"]]
            if row["observed_30pct_hit"] is True:
                bucket["observed_hits_unqualified"] += 1
            elif row["observed_30pct_hit"] is False:
                bucket["observed_misses_unqualified"] += 1
            else:
                bucket["abstained"] += 1
    canonical = json.dumps(sorted(universe.items()), separators=(",", ":")).encode()
    cohort_digest = hashlib.sha256(canonical).hexdigest()
    evidence_digest = hashlib.sha256(json.dumps(
        {"source_sha256": batch["source_sha256"], "counts": counts,
         "universe": sorted(universe.items()), "reconstructed": sorted(seen),
         "diagnostic_rows": diagnostic_rows,
         "diagnostic_selection_outcomes": diagnostic_selection_outcomes},
        sort_keys=True, separators=(",", ":")).encode()).hexdigest()
    missing = len(universe) - len(seen)
    # B's existing _learning_evidence contract expects exact cohort arithmetic,
    # explicit excluded identities and a digest. No incomplete archive cohort is
    # allowed to masquerade as qualified held-out evidence.
    exclusions = {pid: list(HORIZONS) for pid in sorted(universe)}
    abstentions = {"UNAUTHENTICATED_ARCHIVE_OR_PROXY_ENTRY": len(seen)}
    if missing:
        abstentions["NO_RECONSTRUCTED_OUTCOME"] = missing
    return {
        "schema": "paper_learning_handoff_v1",
        "status": "NO_QUALIFIED_RULE",
        "source": "historical_outcome_execution_v1",
        "outcome_input_sha256": batch["source_sha256"],
        "frozen_universe_digest": cohort_digest,
        "cohort_join_digest": cohort_digest,
        "evidence_digest": evidence_digest,
        "baseline_version": "NO_AUTHENTICATED_BASELINE",
        "challenger_version": "NO_AUTHENTICATED_CHALLENGER",
        "evaluation_asof_utc": None,
        "observed_prediction_count": len(universe),
        "complete_cohort_count": 0,
        "excluded_prediction_count": len(universe),
        "abstention_counts": abstentions,
        "incomplete_prediction_horizons": exclusions,
        "frozen_prediction_count": len(universe),
        "reconstructed_prediction_count": len(seen),
        "missing_prediction_count": len(universe) - len(seen),
        "diagnostic_horizon_status_counts": counts,
        "diagnostic_horizon_hit_miss": diagnostic_hit_miss,
        "diagnostic_outcome_rows": diagnostic_rows,
        "diagnostic_selection_outcomes": diagnostic_selection_outcomes,
        "qualified_cohort_count": 0,
        "source_authenticated": False,
        "measured_lift_verified": False,
        "live_watch_authorized": False,
        "promotion_authorized": False,
        "production_applied": False,
        "read_only": True,
        "reason": "Pinned trade bytes and proxy entry do not establish publisher authentication or executable liquidity",
    }


def main(argv=None):
    parser = argparse.ArgumentParser(description="Read-only historical outcomes to B abstention handoff")
    parser.add_argument("--execution", type=Path, required=True)
    parser.add_argument("--frozen-predictions", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args(argv)
    if args.output.exists():
        raise FileExistsError("Refusing to overwrite learning evidence")
    execution = json.loads(args.execution.read_text(encoding="utf-8"))
    frozen = json.loads(args.frozen_predictions.read_text(encoding="utf-8"))
    result = project_historical_execution(execution, frozen_predictions=frozen)
    args.output.write_text(json.dumps(result, sort_keys=True, indent=2) + "\n", encoding="utf-8")
    return result


if __name__ == "__main__":
    main()
