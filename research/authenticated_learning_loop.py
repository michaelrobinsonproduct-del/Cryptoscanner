"""Authenticated score-to-outcome chronological comparison and versioned shadow feedback.

Only immutable score/depth associations and source-verified complete paths
contribute labels. All other captures abstain; no production promotion.
"""
import hashlib
import json
import math
from pathlib import Path

from research.acquisition_receipt_pipeline import load_captures
from research.depth_acquisition_associations import verified_associations
from research.prospective_round_store import evaluate_index
from research.learning_feedback import decide, append_decision

HORIZONS = (1, 6, 24, 48)
PURGE_SECONDS = 48 * 3600


def compare(captures_dir, associations_dir, round_index, *, horizon_hours=1,
            baseline_version="paper-baseline-v1", challenger_version="paper-challenger-v1",
            ledger_path=None):
    if horizon_hours not in HORIZONS:
        raise ValueError("unsupported horizon")
    captures = load_captures(captures_dir)
    verified, excluded, provenance = verified_associations(
        captures_dir, associations_dir, round_index)
    outcomes = evaluate_index(round_index, horizon_hours)
    by_source = {}
    for row in outcomes["outcomes"]:
        key = (row["pair"], row["entry_source_sha256"])
        if key in by_source:
            raise ValueError("duplicate source outcome identity")
        by_source[key] = row
    qualified = []
    abstentions = list(excluded)
    for capture in verified:
        outcome = by_source.get((capture["pair"], capture["source_sha256"]))
        if outcome is None or outcome["status"] != "QUALIFIED_OBSERVED_PATH":
            abstentions.append({"prediction_id": capture["prediction_id"],
                                "reason": outcome["status"] if outcome else "MISSING_SOURCE_OUTCOME"})
            continue
        if outcome.get("entry_liquidity_usd") is None or outcome["entry_liquidity_usd"] < 20:
            abstentions.append({"prediction_id": capture["prediction_id"],
                                "reason": "INSUFFICIENT_ENTRY_LIQUIDITY"})
            continue
        if type(outcome.get("ge30pct")) is not bool:
            raise ValueError("invalid qualified outcome")
        qualified.append({**capture, "positive": outcome["ge30pct"],
                          "entry_at": outcome["entry_first_observed_at"]})
    qualified.sort(key=lambda r: (r["entry_at"], r["prediction_id"]))
    if len({r["prediction_id"] for r in qualified}) != len(qualified):
        raise ValueError("duplicate qualified prediction")
    # Strict time-ordered split with a 48h embargo, preventing horizon overlap.
    split = math.floor(len(qualified) * 0.7)
    train = qualified[:split]
    test_start = qualified[split]["entry_at"] if split < len(qualified) else None
    train = [r for r in train if test_start is not None
             and r["entry_at"] + PURGE_SECONDS < test_start]
    held = qualified[split:] if train else []
    def top_decile(rows, score):
        n = max(1, math.ceil(len(rows) / 10)) if rows else 0
        ranked = sorted(rows, key=lambda r: (-r[score], r["prediction_id"]))
        return {"top_decile_n": n,
                "top_decile_hits": sum(r["positive"] for r in ranked[:n])}
    baseline = top_decile(held, "baseline_score")
    challenger = top_decile(held, "challenger_score")
    lift = ((challenger["top_decile_hits"] - baseline["top_decile_hits"]) /
            baseline["top_decile_n"]) if held else None
    comparison = {"production_applied": False, "horizon_hours": horizon_hours,
                  "captures_total": len(captures), "associations_verified": len(verified),
                  "source_snapshots_verified": outcomes["snapshots_verified"],
                  "qualified_n": len(qualified), "train_n": len(train),
                  "held_out_n": len(held), "purge_seconds": PURGE_SECONDS,
                  "baseline": baseline, "challenger": challenger,
                  "held_out_lift": lift, "abstentions": abstentions,
                  "source_abstentions": provenance["source_abstentions"],
                  "rule": "QUALIFIED_COMPARISON" if held else "NO QUALIFIED RULE"}
    raw = json.dumps(comparison, sort_keys=True, separators=(",", ":"), allow_nan=False).encode()
    decision = decide(comparison, baseline_version=baseline_version,
                      challenger_version=challenger_version,
                      evidence_sha256=hashlib.sha256(raw).hexdigest())
    if ledger_path is not None:
        append_decision(ledger_path, decision)
    return {"comparison": comparison, "shadow_decision": decision}


def evaluate_all(captures_dir, associations_dir, round_index, *, ledger_path=None):
    reports = {str(h): compare(captures_dir, associations_dir, round_index,
                              horizon_hours=h) for h in HORIZONS}
    if ledger_path is not None:
        # One versioned decision per completed batch, based on the 48h horizon.
        append_decision(ledger_path, reports["48"]["shadow_decision"])
    return {"mode": "RESEARCH_ONLY_AUTHENTICATED_HELD_OUT",
            "horizons": reports, "production_applied": False}
