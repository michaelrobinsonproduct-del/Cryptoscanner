"""Fail-closed comparison of manual and scheduled paper scanner results.

This is a read-only acceptance tool. It never dispatches scans or writes ledgers.
Both inputs must be captured from the same deterministic fixture/as-of clock.
"""
import argparse
import hashlib
import json
from pathlib import Path

FIELDS = ("schema", "mode", "buy_approved", "source", "started_at", "as_of",
          "eligible_pairs", "matched_tickers", "observed_markets",
          "ohlc_screened", "watch", "observations", "abstentions",
          "forward_labels", "held_out_lift", "production_applied")


def canonical(report):
    if not isinstance(report, dict):
        raise ValueError("scan report must be an object")
    missing = set(FIELDS) - set(report)
    if missing:
        raise ValueError("missing scanner fields: " + ", ".join(sorted(missing)))
    if report["mode"] != "PAPER_ONLY" or report["buy_approved"] is not False:
        raise ValueError("unsafe scanner mode")
    if report["production_applied"] is not False:
        raise ValueError("unexpected production application")
    if report["forward_labels"] != 0 or report["held_out_lift"] is not None:
        raise ValueError("unverified learning claim")
    for field in ("eligible_pairs", "matched_tickers", "observed_markets", "ohlc_screened"):
        if type(report[field]) is not int or report[field] < 0:
            raise ValueError("invalid scanner coverage: " + field)
    if not (report["ohlc_screened"] <= report["observed_markets"]
            <= report["matched_tickers"] <= report["eligible_pairs"]):
        raise ValueError("inconsistent scanner coverage")
    if not isinstance(report["watch"], list) or not isinstance(report["observations"], list):
        raise ValueError("invalid candidate or observation list")
    ids = [item.get("prediction_id") for item in report["watch"] if isinstance(item, dict)]
    if len(ids) != len(report["watch"]) or any(not isinstance(x, str) or not x for x in ids):
        raise ValueError("invalid prediction IDs")
    if len(set(ids)) != len(ids):
        raise ValueError("duplicate prediction IDs")
    return json.dumps(report, sort_keys=True,
                      separators=(",", ":"), allow_nan=False).encode()


def compare(manual, scheduled):
    a, b = canonical(manual), canonical(scheduled)
    if a != b:
        differences = [key for key in sorted(set(manual) | set(scheduled)) if manual.get(key) != scheduled.get(key) or (key in manual) != (key in scheduled)]
        raise ValueError("manual/scheduled fixture divergence: " + ", ".join(differences))
    return hashlib.sha256(a).hexdigest()


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("manual", type=Path)
    parser.add_argument("scheduled", type=Path)
    args = parser.parse_args()
    print("PAPER_MANUAL_SCHEDULED_PARITY_SHA256=" +
          compare(json.loads(args.manual.read_text()), json.loads(args.scheduled.read_text())))


if __name__ == "__main__":
    main()
