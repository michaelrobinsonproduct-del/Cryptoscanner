"""Bounded exclusion census for retained Kraken trade/OHLC evidence.

This is a descriptive source-coverage diagnostic, not a completeness proof.
A missing candle and missing trade bucket inside a retained period is an
unknown interval, never an independently verified no-trade bar.
"""
import math

STEP = 300
HORIZONS = (1, 6, 24, 48)
MAX_CANDLES = 8000
MAX_TRADE_BUCKETS = 250000


def assess(ohlc_rows, trade_buckets, exact_timestamps):
    """Partition overlap and forward exclusions without inventing labels."""
    if not 0 < len(ohlc_rows) <= MAX_CANDLES:
        raise ValueError("invalid OHLC selection size")
    if not isinstance(trade_buckets, dict) or not 0 < len(trade_buckets) <= MAX_TRADE_BUCKETS:
        raise ValueError("invalid trade bucket selection size")
    ohlc = set()
    previous = None
    for row in ohlc_rows:
        if len(row) != 7:
            raise ValueError("invalid OHLC row shape")
        t = row[0]
        if (isinstance(t, bool) or not isinstance(t, (int, float))
                or not math.isfinite(t) or t != int(t) or t < 0 or int(t) % STEP
                or (previous is not None and t <= previous)):
            raise ValueError("invalid OHLC chronology")
        t = int(t)
        ohlc.add(t)
        previous = t
    trade = set()
    for t, records in trade_buckets.items():
        if (type(t) is not int or t < 0 or t % STEP
                or not isinstance(records, list) or not records):
            raise ValueError("invalid trade bucket")
        trade.add(t)
    if not isinstance(exact_timestamps, (set, frozenset)):
        raise ValueError("invalid exact timestamp selection")
    exact = set(exact_timestamps)
    if any(type(t) is not int or t not in ohlc or t not in trade for t in exact):
        raise ValueError("exact timestamp without both sources")

    lo = max(min(ohlc), min(trade))
    hi = min(max(ohlc), max(trade))
    if lo > hi:
        overlap = {"intervals_in_shared_observed_span": 0,
                   "exact_candidate_intervals": 0,
                   "both_present_but_nonmatching": 0,
                   "ohlc_only_intervals": 0,
                   "trade_only_intervals": 0,
                   "neither_source_observed_intervals": 0}
    else:
        span = (hi - lo) // STEP + 1
        both = {t for t in ohlc & trade if lo <= t <= hi}
        o_only = {t for t in ohlc - trade if lo <= t <= hi}
        t_only = {t for t in trade - ohlc if lo <= t <= hi}
        matches = {t for t in exact if lo <= t <= hi}
        neither = span - len(both) - len(o_only) - len(t_only)
        if neither < 0 or len(matches) > len(both):
            raise AssertionError("overlap partition invariant")
        overlap = {"intervals_in_shared_observed_span": span,
                   "exact_candidate_intervals": len(matches),
                   "both_present_but_nonmatching": len(both) - len(matches),
                   "ohlc_only_intervals": len(o_only),
                   "trade_only_intervals": len(t_only),
                   "neither_source_observed_intervals": neither}
        if sum(value for key, value in overlap.items()
               if key != "intervals_in_shared_observed_span") != span:
            raise AssertionError("overlap conservation failed")

    windows = {}
    ohlc_tail, trade_tail = max(ohlc), max(trade)
    for hours in HORIZONS:
        counts = {"candidate_entries": len(exact), "complete_descriptive_windows": 0,
                  "excluded_beyond_ohlc_tail": 0,
                  "excluded_beyond_trade_tail": 0,
                  "excluded_missing_ohlc_future": 0,
                  "excluded_missing_trade_future": 0,
                  "excluded_nonmatching_future": 0,
                  "verified_predictive_labels": 0}
        for t in exact:
            end = t + hours * 3600
            if end > ohlc_tail:
                key = "excluded_beyond_ohlc_tail"
            elif end > trade_tail:
                key = "excluded_beyond_trade_tail"
            else:
                key = "complete_descriptive_windows"
                for i in range(1, hours * 12 + 1):
                    future = t + i * STEP
                    if future not in ohlc:
                        key = "excluded_missing_ohlc_future"
                        break
                    if future not in trade:
                        key = "excluded_missing_trade_future"
                        break
                    if future not in exact:
                        key = "excluded_nonmatching_future"
                        break
            counts[key] += 1
        if sum(v for k, v in counts.items() if k.startswith("excluded_")
               or k == "complete_descriptive_windows") != len(exact):
            raise AssertionError("horizon exclusion conservation failed")
        windows[str(hours)] = counts
    return {
        "status": "bounded_trade_ohlc_coverage_not_source_authenticated",
        "ohlc_first_open_utc_seconds": min(ohlc),
        "ohlc_last_open_utc_seconds": max(ohlc),
        "trade_first_observed_bucket_utc_seconds": min(trade),
        "trade_last_observed_bucket_utc_seconds": max(trade),
        "ohlc_observed_candles": len(ohlc),
        "trade_observed_buckets": len(trade),
        "overlap": overlap,
        "horizons": windows,
        "no_trade_inference": "not_authorized_for_unobserved_intervals",
        "retained_edges_complete": False,
        "independent_trade_source_completeness_verified": False,
        "verified_predictive_labels": 0,
        "held_out_evaluation": "not_authorized",
        "production_modified": False,
    }
