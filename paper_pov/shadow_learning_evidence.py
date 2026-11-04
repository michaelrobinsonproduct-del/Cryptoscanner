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
    a, b = baseline.get("observations"), challenger.get("observations")
    # Row-level booleans cannot independently authenticate Kraken archive data.
    receipt_a, receipt_b = baseline.get("source_receipt"), challenger.get("source_receipt")
    receipt_valid = (isinstance(receipt_a, dict) and receipt_a == receipt_b
                     and receipt_a.get("verification") == "independently_authenticated"
                     and isinstance(receipt_a.get("artifact_sha256"), str)
                     and len(receipt_a["artifact_sha256"]) == 64
                     and all(c in "0123456789abcdef" for c in receipt_a["artifact_sha256"].lower())
                     and isinstance(receipt_a.get("verifier_commit"), str)
                     and len(receipt_a["verifier_commit"]) == 40
                     and all(c in "0123456789abcdef" for c in receipt_a["verifier_commit"].lower()))
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
            if feature > entry or entry < start or mature < entry + timedelta(hours=48):
                raise ValueError("Lookahead, in-sample entry or immature 48h outcome")
            if not all(c in "0123456789abcdef" for c in row["source_sha256"].lower()):
                raise ValueError("Malformed source SHA256")
            out[key] = row
        return out
    aa, bb = normalize(a), normalize(b)
    if aa.keys() != bb.keys():
        raise ValueError("Different holdout universes")
    for key in aa:
        if any(aa[key][field] != bb[key][field] for field in ("hit", "source_sha256", "horizon_hours", "entry_utc", "label_mature_utc", "feature_asof_utc", "holdout_start_utc", "liquidity_qualified", "source_authenticated", "partition")):
            raise ValueError("Outcome or source mismatch")
    def metrics(rows):
        selected = [x for x in rows.values() if x["watch"]]
        true_positive = sum(x["hit"] for x in selected)
        return {"watched": len(selected), "true_positive": true_positive,
                "precision": true_positive / len(selected) if selected else None,
                "missed_movers": sum(x["hit"] and not x["watch"] for x in rows.values())}
    base, candidate = metrics(aa), metrics(bb)
    n = len(aa)
    qualified = (receipt_valid and n >= minimum_holdout and base["watched"] >= minimum_holdout
                 and candidate["watched"] >= minimum_holdout
                 and candidate["precision"] > base["precision"]
                 and candidate["missed_movers"] <= base["missed_movers"])
    return {"schema": "shadow_learning_evidence_v1",
            "baseline_version": baseline["version"], "challenger_version": challenger["version"],
            "cohort_size": n, "baseline": base, "challenger": candidate,
            "precision_delta": (candidate["precision"] - base["precision"]
                                if base["precision"] is not None and candidate["precision"] is not None else None),
            "evidence_digest": canonical_digest({"baseline": baseline, "challenger": challenger}),
            "status": "EVIDENCE_CANDIDATE_REVIEW_REQUIRED" if qualified else "NO_QUALIFIED_RULE",
            "source_receipt_qualified": receipt_valid,
            "promotion_authorized": False, "production_applied": False}
