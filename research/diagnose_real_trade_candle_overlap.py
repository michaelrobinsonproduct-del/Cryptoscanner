"""Read-only, bounded trade-to-candle diagnostics; never promotes labels."""
from collections import Counter
from math import isfinite
from match_historical_trades_to_ohlcvt import aggregate
from verify_trade_candle_provenance import verify_open_boundary

MAX_DIAGNOSTIC_INTERVALS = 250000


def diagnose(ohlc_rows, trades):
    if len(ohlc_rows) > MAX_DIAGNOSTIC_INTERVALS or len(trades) > 250000:
        raise ValueError("diagnostic resource cap")
    if not trades or not ohlc_rows:
        return {"status": "insufficient_evidence", "exact_candidate_matches": 0,
                "verified_complete_intervals": 0, "real_labels": 0}
    aggregated, buckets = aggregate(trades)
    source = {}
    for row in ohlc_rows:
        if len(row) != 7 or not all(isfinite(float(x)) for x in row):
            raise ValueError("invalid OHLC source row")
        ts = int(row[0])
        if float(row[0]) != ts or ts % 300 or ts in source:
            raise ValueError("unaligned or duplicate source candle")
        source[ts] = row
    counts = Counter()
    examples = {}
    for ts, records in buckets.items():
        if ts not in source:
            status = "trade_bucket_missing_from_ohlc"
        else:
            status = verify_open_boundary(source[ts], records,
                                          independent_trade_source=True)["status"]
        counts[status] += 1
        if status not in examples:
            examples[status] = ts
    absent = sum(ts not in buckets for ts in source)
    exact = counts["verified_open_boundary"]
    # Exact matching supports interval-specific evidence, not completeness
    # of the entire source archive or permission to create labels.
    return {"status": "candidate_diagnostics_only",
            "trade_intervals": len(buckets),
            "ohlc_intervals": len(source),
            "candidate_overlaps": len(buckets) - counts["trade_bucket_missing_from_ohlc"],
            "exact_candidate_matches": exact,
            "mismatch_counts": dict(sorted(counts.items())),
            "first_example_timestamps": examples,
            "ohlc_intervals_without_trade_bucket": absent,
            "verified_complete_intervals": 0,
            "real_labels": 0,
            "held_out_evaluation": "not_authorized",
            "completeness_gate": "independent_trade_archive_coverage_unverified"}
