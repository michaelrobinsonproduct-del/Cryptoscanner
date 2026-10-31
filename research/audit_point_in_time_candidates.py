"""Bounded, point-in-time *descriptive* early-mover research from retained Kraken rows.

Every feature uses closed candles at or before the entry decision (entry open+300).
Future peaks are kept separate and cannot be used as features. Exact trade/OHLC
matches are NOT proof of independently complete trades or executable fills.
This module never returns verified labels, training samples, or model lift.
"""
from math import isfinite
from audit_trade_candidate_windows import audit_candidate_windows, STEP, HORIZONS

MAX_EXAMPLES = 3
EARLY_PRIOR_RETURN_CEILING = 0.10


def audit_point_in_time_candidates(ohlc_rows, exact_timestamps):
    """Summarize strictly closed 15m entry features and later descriptive peaks.

    15m price change: close[t]/close[t-900]-1, requiring four matched
    consecutive candles. The three most recent matched closed candles supply
    a base-volume*close quote-volume PROXY and high/low range. Entry as-of
    is t+300; future opens are strictly greater than t.
    """
    validated = audit_candidate_windows(ohlc_rows, exact_timestamps)
    source = {int(row[0]): row for row in ohlc_rows}
    exact = set(exact_timestamps)
    last = max(source)
    feature_ready = {}
    missing_history = 0
    for t in sorted(exact):
        prior_times = [t - i * STEP for i in (3, 2, 1, 0)]
        if any(x not in exact for x in prior_times):
            missing_history += 1
            continue
        prior = [source[x] for x in prior_times]
        entry_close = prior[-1][4]
        prior_close = prior[0][4]
        quote_proxy = sum(row[4] * row[5] for row in prior[1:])
        range_15m = max(row[2] for row in prior[1:]) / min(row[3] for row in prior[1:]) - 1
        if not all(isfinite(v) for v in (entry_close, prior_close, quote_proxy, range_15m)):
            raise ValueError("nonfinite point-in-time feature")
        feature_ready[t] = {
            "entry_open_utc": t, "decision_as_of_utc": t + STEP,
            "prior_15m_return": entry_close / prior_close - 1,
            "prior_15m_quote_volume_proxy": quote_proxy,
            "prior_15m_high_low_range": range_15m,
        }
    horizon_reports = {}
    for hours in HORIZONS:
        n = hours * 12
        complete = beyond = missing_future = hits30 = early_hits30 = 0
        examples = []
        for t, features in feature_ready.items():
            if t + n * STEP > last:
                beyond += 1
                continue
            future = [source.get(t + i * STEP) if t + i * STEP in exact else None
                      for i in range(1, n + 1)]
            if any(row is None for row in future):
                missing_future += 1
                continue
            complete += 1
            peak = max(row[2] for row in future) / source[t][4] - 1
            hit = peak >= 0.30
            hits30 += hit
            early = features["prior_15m_return"] < EARLY_PRIOR_RETURN_CEILING
            early_hits30 += hit and early
            if len(examples) < MAX_EXAMPLES:
                examples.append({**features,
                                 "future_descriptive_peak_return": peak,
                                 "future_descriptive_peak_30": hit,
                                 "prior_return_below_10pct": early})
        if complete + beyond + missing_future != len(feature_ready):
            raise AssertionError("point-in-time feature window accounting mismatch")
        if complete > validated["horizons"][str(hours)]["candidate_full_future_windows"]:
            raise AssertionError("feature windows exceed exact future windows")
        horizon_reports[str(hours)] = {
            "feature_ready_entries": len(feature_ready),
            "descriptive_complete_future_windows": complete,
            "excluded_outside_retained_end": beyond,
            "excluded_missing_exact_future": missing_future,
            "descriptive_peak_30": hits30,
            "descriptive_peak_30_with_prior_return_below_10pct": early_hits30,
            "examples": examples,
            "real_labels": 0,
        }
    return {
        "status": "point_in_time_descriptive_only_unverified_trade_completeness",
        "entry_feature_source": "retained_exact_trade_ohlc_candidates_not_complete",
        "decision_as_of_rule": "entry_candle_open_plus_300_seconds",
        "features_use_future_candles": False,
        "feature_lookback_seconds": 900,
        "quote_volume_is_proxy_not_executed_notional": True,
        "early_prior_return_ceiling": EARLY_PRIOR_RETURN_CEILING,
        "candidate_exact_entries": len(exact),
        "feature_ready_entries": len(feature_ready),
        "excluded_missing_exact_15m_history": missing_history,
        "horizons": horizon_reports,
        "real_labels": 0,
        "held_out_evaluation": "not_authorized",
        "executable_fill_verified": False,
        "production_modified": False,
    }
