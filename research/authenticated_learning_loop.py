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


def _extract(captures_dir, associations_dir, round_index, horizon_hours):
    """Source-authenticate one scored cohort. Never join on pair alone."""
    captures = load_captures(captures_dir)
    if Path(associations_dir).is_dir():
        verified, excluded, provenance = verified_associations(
            captures_dir, associations_dir, round_index)
    else:
        verified = []
        excluded = [{"prediction_id": c["prediction_id"],
                     "reason": "MISSING_DEPTH_ASSOCIATION"} for c in captures]
        provenance = {"source_abstentions": []}
    outcomes = evaluate_index(round_index, horizon_hours)
    # Raw Kraken depth may be identical at different factual acquisition
    # times. A SHA-only join can attach a score to a later unrelated outcome.
    by_source = {}
    identities = set()
    for row in outcomes["outcomes"]:
        identity = (row["pair"], row["entry_source_sha256"],
                    row["entry_first_observed_at"])
        if identity in identities:
            raise ValueError("duplicate point-in-time source outcome identity")
        identities.add(identity)
        by_source.setdefault(identity[:2], []).append(row)
    qualified, abstentions = [], list(excluded)
    for capture in verified:
        candidates = by_source.get((capture["pair"], capture["source_sha256"]), [])
        if "source_first_observed_at" in capture:
            candidates = [row for row in candidates if
                          row["entry_first_observed_at"] ==
                          capture["source_first_observed_at"]]
        if len(candidates) != 1:
            abstentions.append({"prediction_id": capture["prediction_id"],
                                "reason": "AMBIGUOUS_SOURCE_OUTCOME"
                                if len(candidates) > 1 else "MISSING_SOURCE_OUTCOME"})
            continue
        outcome = candidates[0]
        if outcome["status"] != "QUALIFIED_OBSERVED_PATH":
            abstentions.append({"prediction_id": capture["prediction_id"],
                                "reason": outcome["status"]})
            continue
        if outcome.get("entry_liquidity_usd") is None or outcome["entry_liquidity_usd"] < 20:
            abstentions.append({"prediction_id": capture["prediction_id"],
                                "reason": "INSUFFICIENT_ENTRY_LIQUIDITY"})
            continue
        if type(outcome.get("ge30pct")) is not bool:
            raise ValueError("invalid qualified outcome")
        qualified.append({**capture, "positive": outcome["ge30pct"],
                          "entry_at": outcome["entry_first_observed_at"]})
    return {"captures": len(captures), "verified": len(verified),
            "snapshots": outcomes["snapshots_verified"], "qualified": qualified,
            "abstentions": abstentions, "source_abstentions": provenance["source_abstentions"]}


def _compare_extracted(extracted, *, horizon_hours, baseline_version,
                       challenger_version, ledger_path=None):
    qualified = [row for cohort in extracted for row in cohort["qualified"]]
    qualified.sort(key=lambda r: (r["entry_at"], r["prediction_id"]))
    if len({r["prediction_id"] for r in qualified}) != len(qualified):
        raise ValueError("duplicate qualified prediction across cohorts")
    if len({(r["pair"], r["source_sha256"]) for r in qualified}) != len(qualified):
        raise ValueError("duplicate qualified source receipt across cohorts")
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
    if baseline["top_decile_n"] < 5:
        lift = None
    comparison = {
        "production_applied": False, "horizon_hours": horizon_hours,
        "cohorts_verified": len(extracted),
        "captures_total": sum(c["captures"] for c in extracted),
        "associations_verified": sum(c["verified"] for c in extracted),
        "source_snapshots_verified": sum(c["snapshots"] for c in extracted),
        "qualified_n": len(qualified), "train_n": len(train),
        "held_out_n": len(held), "purge_seconds": PURGE_SECONDS,
        "baseline": baseline, "challenger": challenger,
        "held_out_lift": lift,
        "abstentions": [a for c in extracted for a in c["abstentions"]],
        "source_abstentions": [a for c in extracted for a in c["source_abstentions"]],
        "rule": "QUALIFIED_COMPARISON" if len(held) >= 20 and lift is not None else "NO QUALIFIED RULE"
    }
    raw = json.dumps(comparison, sort_keys=True, separators=(",", ":"), allow_nan=False).encode()
    decision = decide(comparison, baseline_version=baseline_version,
                      challenger_version=challenger_version,
                      evidence_sha256=hashlib.sha256(raw).hexdigest())
    if ledger_path is not None:
        append_decision(ledger_path, decision)
    return {"comparison": comparison, "shadow_decision": decision}


def compare(captures_dir, associations_dir, round_index, *, horizon_hours=1,
            baseline_version="paper-baseline-v1", challenger_version="paper-challenger-v1",
            ledger_path=None):
    if horizon_hours not in HORIZONS:
        raise ValueError("unsupported horizon")
    extracted = _extract(captures_dir, associations_dir, round_index, horizon_hours)
    return _compare_extracted([extracted], horizon_hours=horizon_hours,
                              baseline_version=baseline_version,
                              challenger_version=challenger_version,
                              ledger_path=ledger_path)


def evaluate_cohorts(cohort_roots, *, ledger_path=None):
    """Aggregate independent scored series with a single chronological held-out split.

    Each root is a fully retained research scored series with entry/scores,
    entry/associations and entry/round-index.jsonl. Every receipt is verified
    independently before combining observations; no hindsight score backfill.
    """
    roots = [Path(root).resolve(strict=True) for root in cohort_roots]
    if not roots or len({str(root) for root in roots}) != len(roots):
        raise ValueError("requires distinct scored research cohorts")
    reports = {}
    for horizon in HORIZONS:
        extracted = []
        for root in roots:
            if root.is_symlink() or not root.is_dir():
                raise ValueError("invalid scored cohort root")
            entry = root / "entry"
            extracted.append(_extract(entry / "scores", entry / "associations",
                                      entry / "round-index.jsonl", horizon))
        reports[str(horizon)] = _compare_extracted(
            extracted, horizon_hours=horizon,
            baseline_version="paper-baseline-v1",
            challenger_version="paper-challenger-v1")
    if ledger_path is not None:
        append_decision(ledger_path, reports["48"]["shadow_decision"])
    return {"mode": "RESEARCH_ONLY_MULTI_COHORT_LEARNING",
            "cohorts": len(roots), "horizons": reports,
            "shadow_decision": reports["48"]["shadow_decision"],
            "production_applied": False}



def evaluate_all(captures_dir, associations_dir, round_index, *, ledger_path=None):
    reports = {str(h): compare(captures_dir, associations_dir, round_index,
                              horizon_hours=h) for h in HORIZONS}
    if ledger_path is not None:
        # One versioned decision per completed batch, based on the 48h horizon.
        append_decision(ledger_path, reports["48"]["shadow_decision"])
    return {"mode": "RESEARCH_ONLY_AUTHENTICATED_HELD_OUT",
            "horizons": reports, "production_applied": False}
