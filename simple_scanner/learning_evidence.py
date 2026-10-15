"""Fail-closed evidence validation for future model promotion.

Historical watchlist outcomes alone cannot establish full-market breakout recall.
No production scoring, filesystem, network, or database side effects.
"""
import math

REQUIRED_HORIZONS = (1, 3, 6, 24)

def assess_evidence(report):
    reasons = []
    if not isinstance(report, dict):
        return {"sufficient": False, "reasons": ["missing_report"]}
    if report.get("coverage") != "FULL_MARKET_FEATURES":
        reasons.append("full_market_features_missing")
    if report.get("split") != "CHRONOLOGICAL_UNSEEN":
        reasons.append("unseen_holdout_missing")
    if report.get("feature_timestamps_verified") is not True:
        reasons.append("feature_timing_unverified")
    if report.get("market_outcome_coverage_verified") is not True:
        reasons.append("market_outcome_coverage_unverified")
    for h in REQUIRED_HORIZONS:
        row = report.get("horizons", {}).get(h)
        if not isinstance(row, dict):
            reasons.append(f"missing_{h}h")
            continue
        n = row.get("cohorts")
        if type(n) is not int or n < 40:
            reasons.append(f"insufficient_{h}h")
        for key in ("breakout_recall_delta", "delta_pct"):
            v = row.get(key)
            if type(v) not in (int, float) or not math.isfinite(v):
                reasons.append(f"invalid_{h}h_{key}")
    return {"sufficient": not reasons, "reasons": reasons}
