"""Read-only versioned shadow evidence gate. No production promotion capability."""
import hashlib
import json
import math
from datetime import datetime, timedelta, timezone


def utc_time(value):
    if not isinstance(value, str):
        raise ValueError('Missing UTC observation timestamp')
    try:
        parsed = datetime.fromisoformat(value.replace('Z', '+00:00'))
    except ValueError as exc:
        raise ValueError('Invalid observation timestamp') from exc
    if parsed.tzinfo is None or parsed.utcoffset() != timedelta(0):
        raise ValueError('Observation timestamp must be UTC')
    return parsed



def canonical_digest(value):
    return hashlib.sha256(json.dumps(value, sort_keys=True, separators=(",", ":"), allow_nan=False).encode()).hexdigest()


def evaluate_shadow_release(baseline, challenger, *, minimum_holdout=30):
    """Compare identical held-out identities, fail closed on missing or weak evidence.

    Each observation is a frozen, source-qualified held-out outcome with an
    immutable prediction ID, 48h label and the two versioned binary decisions.
    No input may contain post-entry features or in-sample observations.
    """
    if not isinstance(baseline, dict) or not isinstance(challenger, dict):
        raise ValueError("Missing versioned evidence")
    if baseline.get("version") == challenger.get("version"):
        raise ValueError("Baseline and challenger versions must differ")
    if not all(isinstance(x.get("version"), str) and x["version"].strip() for x in (baseline, challenger)):
        raise ValueError("Missing immutable version")
    if type(minimum_holdout) is not int or minimum_holdout < 1:
        raise ValueError("Invalid minimum holdout")
    train_a, train_b = baseline.get("training_end_utc"), challenger.get("training_end_utc")
    if train_a != train_b:
        raise ValueError("Training boundary mismatch")
    training_end = utc_time(train_a)
    asof_a, asof_b = baseline.get("evaluation_asof_utc"), challenger.get("evaluation_asof_utc")
    if asof_a != asof_b:
        raise ValueError("Evaluation cutoff mismatch")
    evaluation_asof = utc_time(asof_a)
    if evaluation_asof <= training_end + timedelta(hours=48):
        raise ValueError("Evaluation cutoff precedes held-out maturity window")
    a, b = baseline.get("observations"), challenger.get("observations")
    # A caller-supplied receipt is not publisher authentication. Until an
    # independently verified byte-level Kraken receipt is wired into this
    # evaluator, the shadow result is diagnostic only. The downstream B
    # consumer must never receive a self-attested qualified rule.
    receipt_valid = False
    if not isinstance(a, list) or not isinstance(b, list):
        raise ValueError("Missing held-out cohort")
    def normalize(rows):
        out = {}
        for row in rows:
            if not isinstance(row, dict):
                raise ValueError("Invalid row")
            key = row.get("prediction_id")
            if not isinstance(key, str) or not key or key in out:
                raise ValueError("Duplicate or missing prediction identity")
            if row.get("partition") != "held_out" or row.get("horizon_hours") != 48:
                raise ValueError("In-sample or wrong horizon")
            if row.get("source_authenticated") is not True or row.get("liquidity_qualified") is not True:
                raise ValueError("Unqualified evidence")
            if type(row.get("hit")) is not bool or type(row.get("watch")) is not bool:
                raise ValueError("Missing binary outcome/decision")
            if not isinstance(row.get("source_sha256"), str) or len(row["source_sha256"]) != 64:
                raise ValueError("Missing source identity")
            if any(row.get(field) is None for field in ("entry_utc", "label_mature_utc", "feature_asof_utc", "holdout_start_utc")):
                raise ValueError("Missing point-in-time evidence")
            entry = utc_time(row["entry_utc"])
            mature = utc_time(row["label_mature_utc"])
            feature = utc_time(row["feature_asof_utc"])
            start = utc_time(row["holdout_start_utc"])
            if start < training_end + timedelta(hours=48):
                raise ValueError("Held-out start violates 48h training purge")
            if feature > entry or entry < start or mature < entry + timedelta(hours=48) or mature > evaluation_asof:
                raise ValueError("Lookahead, in-sample entry or immature 48h outcome")
            if not all(c in "0123456789abcdef" for c in row["source_sha256"].lower()):
                raise ValueError("Malformed source SHA256")
            out[key] = row
        return out
    aa, bb = normalize(a), normalize(b)
    if len({row["holdout_start_utc"] for row in aa.values()}) > 1:
        raise ValueError("Mixed held-out start boundaries")
    if aa.keys() != bb.keys():
        raise ValueError("Different holdout universes")
    for key in aa:
        if any(aa[key][field] != bb[key][field] for field in ("hit", "source_sha256", "horizon_hours", "entry_utc", "label_mature_utc", "feature_asof_utc", "holdout_start_utc", "liquidity_qualified", "source_authenticated", "partition")):
            raise ValueError("Outcome or source mismatch")
    def metrics(rows):
        selected = [x for x in rows.values() if x["watch"]]
        true_positive = sum(x["hit"] for x in selected)
        movers = sum(x["hit"] for x in rows.values())
        false_positives = len(selected) - true_positive
        return {"false_positives": false_positives, "total_movers": movers,
                "recall": true_positive / movers if movers else None,
                "coverage": len(selected) / len(rows) if rows else None,
                "watched": len(selected), "true_positive": true_positive,
                "precision": true_positive / len(selected) if selected else None,
                "missed_movers": sum(x["hit"] and not x["watch"] for x in rows.values())}
    base, candidate = metrics(aa), metrics(bb)
    n = len(aa)
    return {"schema": "shadow_learning_evidence_v1",
            "baseline_version": baseline["version"], "challenger_version": challenger["version"],
            "cohort_size": n, "evaluation_asof_utc": asof_a, "baseline": base, "challenger": candidate,
            "precision_delta": (candidate["precision"] - base["precision"]
                                if base["precision"] is not None and candidate["precision"] is not None else None),
            "evidence_digest": canonical_digest({"baseline": baseline, "challenger": challenger}),
            "status": "NO_QUALIFIED_RULE",
            "source_receipt_qualified": receipt_valid,
            "measured_lift_verified": False, "diagnostic_only": True,
            "promotion_authorized": False, "production_applied": False}
