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
    if not isinstance(report["watch"], list) or not isinstance(report["observations"], list):
        raise ValueError("invalid candidate or observation list")
    if not report["watch"]:
        raise ValueError("no WATCH candidates")
    ids = [item.get("prediction_id") for item in report["watch"] if isinstance(item, dict)]
    if len(ids) != len(report["watch"]) or any(not isinstance(x, str) or not x for x in ids):
        raise ValueError("invalid prediction IDs")
    if len(set(ids)) != len(ids):
        raise ValueError("duplicate prediction IDs")
    return json.dumps({k: report[k] for k in FIELDS}, sort_keys=True,
                      separators=(",", ":"), allow_nan=False).encode()


def compare(manual, scheduled):
    a, b = canonical(manual), canonical(scheduled)
    if a != b:
        differences = [key for key in FIELDS if manual[key] != scheduled[key]]
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
