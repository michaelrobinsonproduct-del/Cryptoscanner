"""Bounded, fail-closed coverage boundary and contiguous 5-minute window analysis.

A perfect overlap match is not evidence of source completeness.
No source downloads, production access, trading, or label promotion.
"""
from collections import Counter
from math import isfinite

STEP = 300
MAX_ROWS = 250000
HORIZONS = (1, 6, 24, 48)


def coverage(ohlc_rows, trade_records):
    if len(ohlc_rows) > MAX_ROWS or len(trade_records) > MAX_ROWS:
        raise ValueError("coverage resource cap")
    if not ohlc_rows or not trade_records:
        return {"status": "insufficient_evidence", "real_labels": 0}
    starts = []
    for row in ohlc_rows:
        if len(row) != 7 or not all(isfinite(float(v)) for v in row):
            raise ValueError("invalid OHLC row")
        ts = int(row[0])
        if float(row[0]) != ts or ts % STEP:
            raise ValueError("unaligned candle timestamp")
        starts.append(ts)
    if starts != sorted(set(starts)):
        raise ValueError("unordered or duplicate OHLC timestamp")
    times = [float(r[0]) for r in trade_records]
    if any(not isfinite(t) or t < 0 for t in times) or times != sorted(times):
        raise ValueError("invalid or unordered trade timestamps")
    first, last = times[0], times[-1]
    low, high = int(first // STEP) * STEP, int(last // STEP) * STEP
    buckets = {int(t // STEP) * STEP for t in times}
    source = set(starts)
    before = sum(t < low for t in starts)
    after = sum(t > high for t in starts)
    inside = sum(low <= t <= high and t not in buckets for t in starts)
    absent_buckets = len(buckets - source)
    matched = len(buckets & source)
    # Longest run of *observed matching intervals*, not independently
    # attested full-source coverage.
    best, current = 0, 0
    for ts in range(low, high + STEP, STEP):
        if ts in buckets and ts in source:
            current += 1
            best = max(best, current)
        else:
            current = 0
    return {"status": "candidate_coverage_only",
            "first_trade_timestamp": first, "last_trade_timestamp": last,
            "first_trade_bucket": low, "last_trade_bucket": high,
            "ohlc_before_trade_period": before,
            "ohlc_after_trade_period": after,
            "ohlc_within_trade_period_without_trade_bucket": inside,
            "trade_buckets_without_ohlc": absent_buckets,
            "candidate_matching_buckets": matched,
            "ohlc_unmatched_reconciled": before + after + inside,
            "longest_contiguous_matching_5m_buckets": best,
            "longest_candidate_hours": best * 5 / 60,
            "candidate_horizon_window_counts": {
                str(h): max(0, best - (h * 12)) for h in HORIZONS},
            "independent_completeness_verified": False,
            "real_labels": 0,
            "held_out_evaluation": "not_authorized"}
