"""Pure, fail-closed promotion decision. No trading, I/O, or live model mutation."""
import math

REQUIRED_HORIZONS = (1, 3, 6, 24)
MIN_COHORTS = 40
MIN_IMPROVEMENT_PP = 0.10

def decide_promotion(horizons, *, history_integrity, dex_errors, prior_approved=False):
    """Return an auditable decision; this function never changes production."""
    reasons = []
    if history_integrity != "ok":
        reasons.append("history_integrity")
    if dex_errors != 0:
        reasons.append("dex_errors")
    if prior_approved:
        reasons.append("existing_promotion_pending")
    for h in REQUIRED_HORIZONS:
        row = horizons.get(h)
        if not isinstance(row, dict):
            reasons.append(f"missing_{h}h")
            continue
        samples = row.get("cohorts")
        delta = row.get("delta_pct")
        breakout = row.get("breakout_recall_delta")
        if type(samples) is not int or samples < MIN_COHORTS:
            reasons.append(f"insufficient_{h}h")
        if not isinstance(delta, (int, float)) or not math.isfinite(delta) or delta < MIN_IMPROVEMENT_PP:
            reasons.append(f"no_return_improvement_{h}h")
        if not isinstance(breakout, (int, float)) or not math.isfinite(breakout) or breakout < 0:
            reasons.append(f"breakout_recall_regression_{h}h")
    return {"eligible": not reasons, "reasons": reasons,
            "mode": "DECISION_ONLY", "live_weights_modified": False,
            "buy_approved": False}
