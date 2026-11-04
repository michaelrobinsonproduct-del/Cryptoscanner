"""Read-only preselection universe export for unbiased prospective miss analysis.

Ticker-only evidence: NOT source-authenticated future outcomes or learning labels.
"""
import argparse
import json
from pathlib import Path
from paper_pov.candidate_snapshot import read_snapshot


def export_universe(latest, now=None):
    verified = read_snapshot(latest, now=now)
    report = json.loads(Path(latest).read_bytes())
    rows = report.get("preselection_universe")
    coverage = report.get("preselection_coverage")
    if not isinstance(rows, list) or not isinstance(coverage, dict):
        raise ValueError("missing preselection universe")
    if len(rows) != verified["observed_markets"] or coverage != {
        "valid_tickers": len(rows),
        "screen_passed": report["screened_markets"],
        "screen_rejected": len(rows) - report["screened_markets"],
    }:
        raise ValueError("preselection coverage mismatch")
    if len({x["pair"] for x in rows}) != len(rows):
        raise ValueError("duplicate preselection market")
    if any(x["screen_passed"] == bool(x["screen_rejections"]) or
           x["quote_timestamp_semantics"] != "client_observed_not_exchange_event_time"
           for x in rows):
        raise ValueError("invalid preselection status or provenance")
    return {"schema": "paper_preselection_v1", "as_of": verified["as_of"],
            "receipt_sha256": verified["receipt_sha256"],
            "coverage": coverage, "markets": rows,
            "future_outcomes_authenticated": False, "qualified_for_learning": False,
            "production_applied": False}


def main():
    p = argparse.ArgumentParser()
    p.add_argument("latest")
    p.add_argument("--output", required=True)
    args = p.parse_args()
    Path(args.output).write_text(json.dumps(export_universe(args.latest), sort_keys=True, allow_nan=False) + "\n")


if __name__ == "__main__":
    main()
