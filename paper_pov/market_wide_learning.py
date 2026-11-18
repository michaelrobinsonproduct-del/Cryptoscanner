"""Build prediction-independent learning anchors from completed five-minute candles.

Input candles use close timestamps, not Kraken interval-open timestamps.
Caller must authenticate source and supply the point-in-time eligible universe.
No production decisions or ledger writes.
"""
from datetime import timedelta
from math import isfinite
from .shadow_learning_evidence import utc_time, canonical_digest
from .heldout_outcome_adapter import reconstruct_forward_outcomes
from .frozen_historical_shadow import features_at_entry

def build_market_cohort(candles, *, eligible_pairs, evaluation_asof_utc):
    asof = utc_time(evaluation_asof_utc)
    eligible = set(eligible_pairs)
    grouped = {}
    for c in candles:
        if c["pair"] not in eligible:
            continue
        t = utc_time(c["timestamp_utc"])
        if t > asof:
            continue
        close, high = float(c["close"]), float(c["high"])
        if not (isfinite(close) and isfinite(high) and 0 < close <= high):
            raise ValueError("Invalid candle")
        grouped.setdefault(c["pair"], []).append((t, c))
    anchors, observed = [], []
    for pair, rows in sorted(grouped.items()):
        rows.sort(key=lambda r: r[0])
        if len({t for t, _ in rows}) != len(rows):
            raise ValueError("Duplicate candle")
        observed.extend(c for _, c in rows)
        for i in range(3, len(rows)):
            t, c = rows[i]
            if t + timedelta(hours=1) > asof:
                break
            if t.minute or t.second or t.microsecond:
                continue
            window = rows[i-3:i+1]
            if any(window[j][0]-window[j-1][0] != timedelta(minutes=5) for j in range(1,4)):
                continue
            p = float(c["close"])
            # Reuse the existing six-feature contract; label discovery remains
            # independent of whether the full feature window is available.
            features = features_at_entry(rows[max(0, i-12):i+1], t)
            anchors.append({"prediction_id": canonical_digest([pair,t.isoformat()]),
                            "pair": pair, "entry_utc": t.isoformat(),
                            "feature_asof_utc": t.isoformat(), "entry_price": p,
                            "features": features or {},
                            "feature_complete": features is not None,
                            "liquidity_qualified": False})
    outcomes = reconstruct_forward_outcomes(anchors, observed, evaluation_asof_utc=evaluation_asof_utc)
    per_horizon = {}
    for h in (1, 6, 24, 48):
        rows = [o for o in outcomes if o["horizon_hours"] == h]
        per_horizon[str(h)] = {
            "hits": sum(o["hit"] is True for o in rows),
            "misses": sum(o["hit"] is False for o in rows),
            "immature": sum(o["outcome_status"] == "IMMATURE" for o in rows),
            "missing_candles": sum(o["outcome_status"] == "MISSING_CANDLES" for o in rows),
        }
    return {"anchors": anchors, "outcomes": outcomes,
            "per_horizon": per_horizon,
            "feature_complete_anchors": sum(a["feature_complete"] for a in anchors),
            "missing_eligible_pairs": sorted(eligible - set(grouped)),
            "eligible_pairs": sorted(eligible), "observed_pairs": sorted(grouped),
            "source_authenticated": False, "production_applied": False,
            "promotion_authorized": False}
