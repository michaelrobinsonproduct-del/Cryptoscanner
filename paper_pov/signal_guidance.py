"""Read-only, explainable signal confidence, investment risk, and action tiers.

The strength index is a heuristic setup-quality score, NOT the probability of a
30% gain in 48h. Those odds require independently qualified historical labels.
This module never changes scanner scores, predictions, trades or learning.
"""
import math

VERSION = "paper-signal-guidance-v1"
TARGET_GAIN_PCT = 30
TARGET_HOURS = 48


def _finite_number(value, field):
    if isinstance(value, bool) or not isinstance(value, (int, float)):
        raise ValueError("Invalid guidance feature: " + field)
    number = float(value)
    if not math.isfinite(number):
        raise ValueError("Nonfinite guidance feature: " + field)
    return number


def assess(candidate, *, score_field="challenger_score", overlap=False,
           validated_calibration=None):
    """Classify current setup; never infer profit odds from a model ranking."""
    if score_field not in ("challenger_score", "legacy_score"):
        raise ValueError("Unknown scanner score field")
    score = _finite_number(candidate[score_field], score_field)
    movement = _finite_number(candidate["move15_pct"], "move15_pct")
    volume = _finite_number(candidate["volume_accel"], "volume_accel")
    price = _finite_number(candidate["price_usd"], "price_usd")
    if price <= 0 or volume < 0 or not isinstance(overlap, bool):
        raise ValueError("Invalid candidate or overlap evidence")
    spread = candidate.get("spread_bps")
    if spread is not None:
        spread = _finite_number(spread, "spread_bps")
        if spread < 0:
            raise ValueError("Negative spread")
    strength = min(100, max(0, score)) * 0.50
    strength += 15 if movement >= 0.2 else (5 if movement >= 0 else -10)
    strength += 25 if volume >= 2 else (15 if volume >= 1.3 else
                                        (5 if volume >= 1 else 0))
    strength += 0 if spread is None else (15 if spread <= 10 else
                 (10 if spread <= 20 else (5 if spread <= 35 else 0)))
    if overlap:
        strength += 10
    strength = int(round(max(0, min(100, strength))))

    risk = 55  # Every early-stage crypto entry has at least HIGH risk.
    reasons = ["Speculative crypto price volatility and uncertain 30% outcome"]
    if spread is None:
        risk += 15
        reasons.append("Bid-ask spread unavailable for this independent signal")
    elif spread > 40:
        risk += 22
        reasons.append("Wide bid-ask spread (>40 bps)")
    elif spread > 20:
        risk += 12
        reasons.append("Elevated bid-ask spread (>20 bps)")
    elif spread > 10:
        risk += 6
        reasons.append("Moderate bid-ask spread (>10 bps)")
    traded_notional = candidate.get("notional_24h_usd")
    if traded_notional is None:
        risk += 5
        reasons.append("24h traded notional unavailable")
    else:
        traded_notional = _finite_number(traded_notional, "notional_24h_usd")
        if traded_notional < 0:
            raise ValueError("Negative traded notional")
        if traded_notional < 250000:
            risk += 12
            reasons.append("Thin reported 24h USD turnover (<$250k)")
        elif traded_notional < 1000000:
            risk += 5
            reasons.append("Limited reported 24h USD turnover (<$1m)")
    if volume < 0.75:
        risk += 15
        reasons.append("Volume acceleration below 0.75x")
    elif volume < 1.25:
        risk += 7
        reasons.append("Weak volume acceleration (<1.25x)")
    if movement < -1:
        risk += 10
        reasons.append("Negative 15-minute momentum below -1%")
    elif movement < 0:
        risk += 6
        reasons.append("Negative 15-minute momentum")
    elif movement > 3:
        risk += 10
        reasons.append("Strong recent rise creates chase/reversal risk")
    risk = min(100, risk)
    risk_band = "EXTREME" if risk >= 85 else ("VERY_HIGH" if risk >= 70 else "HIGH")
    strength_band = "STRONG" if strength >= 70 else (
        "MODERATE" if strength >= 45 else "WEAK")

    # A validated positive-predictive estimate cannot be inferred from the
    # current learning artifacts (source_authenticated=False, insufficient
    # chronological 48h labels). Only an independently qualified held-out
    # calibration would permit even considering a more substantial entry.
    calibrated_odds = None
    qualified = False
    if validated_calibration is not None:
        if not isinstance(validated_calibration, dict):
            raise ValueError("Invalid calibration")
        qualified = (validated_calibration.get("source_authenticated") is True
                     and validated_calibration.get("independent_held_out") is True
                     and validated_calibration.get("qualified_48h_samples", 0) >= 100
                     and validated_calibration.get("calibration_verified") is True)
        if qualified:
            calibrated_odds = _finite_number(
                validated_calibration["probability_pct"], "probability_pct")
            if not 0 <= calibrated_odds <= 100:
                raise ValueError("Invalid calibrated probability")
    if (qualified and calibrated_odds >= 65 and strength >= 80 and
            risk_band == "HIGH" and overlap and movement > 0 and volume >= 2):
        action = "CONSIDER_MORE_SUBSTANTIAL_ENTRY"
    elif (strength >= 75 and risk_band == "HIGH" and movement >= 0.2
          and volume >= 1.5 and (overlap or score >= 70)):
        action = "CONSIDER_SMALL_ENTRY"
    elif risk_band == "EXTREME" or strength < 35 or movement < -1.2:
        action = "DO_NOTHING"
    else:
        action = "WATCH"
    return {
        "schema": VERSION,
        "target_gain_pct": TARGET_GAIN_PCT,
        "horizon_hours": TARGET_HOURS,
        "gain_probability_pct": calibrated_odds,
        "gain_probability_status": ("VALIDATED_HELD_OUT" if qualified
                                    else "NOT_CALIBRATED_INSUFFICIENT_48H_EVIDENCE"),
        "signal_confidence_score": strength,
        "signal_confidence": strength_band,
        "signal_confidence_is_probability": False,
        "risk_score": risk,
        "risk": risk_band,
        "risk_reasons": reasons,
        "independent_legacy_overlap_verified": overlap,
        "recommendation": action,
        "recommendation_is_trade_authorization": False,
        "large_entry_requires_validated_calibration": True,
    }


def action_text(action):
    return {
        "DO_NOTHING": "Do nothing",
        "WATCH": "Watch",
        "CONSIDER_SMALL_ENTRY": "Consider small entry",
        "CONSIDER_MORE_SUBSTANTIAL_ENTRY": "Consider more substantial entry",
    }[action]
