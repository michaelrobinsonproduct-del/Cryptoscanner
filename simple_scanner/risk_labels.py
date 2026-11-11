"""Read-only, conservative research risk labels. Never controls candidate selection or BUY approval."""
import math

RISK_LEVELS = ("LOW", "MEDIUM", "HIGH", "EXTREME")

def assess_risk(candidate):
    """Return risk and supporting reasons; fail closed on missing/invalid market evidence."""
    required = ("spread_bps", "notional_24h_usd", "move_15m_pct", "move_60m_pct", "volume_accel")
    values = {}
    for key in required:
        try:
            value = float(candidate[key])
        except (KeyError, TypeError, ValueError, OverflowError):
            return {"risk": "UNASSESSED", "risk_reasons": ["missing_or_invalid_" + key]}
        if not math.isfinite(value):
            return {"risk": "UNASSESSED", "risk_reasons": ["missing_or_invalid_" + key]}
        values[key] = value
    if candidate.get("status") != "WATCH_RESEARCH_ONLY":
        return {"risk": "UNASSESSED", "risk_reasons": ["candidate_not_validated"]}
    spread = values["spread_bps"]
    notional = values["notional_24h_usd"]
    m15 = abs(values["move_15m_pct"])
    m60 = abs(values["move_60m_pct"])
    accel = values["volume_accel"]
    if spread < 0 or notional < 0 or accel < 0:
        return {"risk": "UNASSESSED", "risk_reasons": ["invalid_market_metrics"]}
    reasons = []
    severity = 0
    def flag(level, reason):
        nonlocal severity
        severity = max(severity, level)
        reasons.append(reason)
    if notional < 250_000: flag(3, "very_low_24h_notional")
    elif notional < 1_000_000: flag(2, "low_24h_notional")
    elif notional < 10_000_000: flag(1, "moderate_24h_notional")
    if spread > 100: flag(3, "extreme_spread")
    elif spread > 45: flag(2, "wide_spread")
    elif spread > 20: flag(1, "elevated_spread")
    if m15 > 10 or m60 > 20: flag(3, "extreme_short_term_move")
    elif m15 > 5 or m60 > 12: flag(2, "large_short_term_move")
    elif m15 > 2 or m60 > 6: flag(1, "elevated_short_term_move")
    if accel > 20: flag(2, "unusual_volume_acceleration")
    elif accel > 8: flag(1, "high_volume_acceleration")
    return {"risk": RISK_LEVELS[severity], "risk_reasons": reasons or ["no_thresholds_exceeded"]}
