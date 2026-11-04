"""Read-only preselection universe export for unbiased prospective miss analysis.

Ticker-only evidence: NOT source-authenticated future outcomes or learning labels.
"""
import argparse
import datetime as dt
import hashlib
import json
from pathlib import Path
from paper_pov.candidate_snapshot import read_snapshot


def export_universe(latest, now=None, historical=False):
    # Historical analysis must not masquerade as a currently fresh WATCH feed.
    # Validate the original sealed receipt at its own scan timestamp, then mark
    # the resulting universe explicitly historical and non-actionable.
    if historical:
        payload = json.loads(Path(latest).read_bytes())
        stamp = dt.datetime.fromisoformat(payload["as_of"].replace("Z", "+00:00"))
        if stamp.tzinfo is None or stamp.utcoffset() is None:
            raise ValueError("invalid historical timestamp")
        verified = read_snapshot(latest, now=stamp)
    else:
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
    decisions = report.get("preselection_decisions")
    allowed = {"SCREEN_REJECTED", "NOT_OHLC_SELECTED", "OHLC_ABSTAINED", "WATCH", "NOT_RANKED_WATCH"}
    if not isinstance(decisions, dict) or set(decisions) - allowed or sum(decisions.values()) != len(rows):
        raise ValueError("invalid preselection decision accounting")
    if any(x.get("selection_status") not in allowed or
           (x["selection_status"] == "WATCH") != (x.get("watch_rank") is not None) or
           (x["selection_status"] == "OHLC_ABSTAINED") != (x.get("ohlc_abstention_category") is not None) or
           (x["screen_passed"]) != (x.get("baseline_score") is not None)
           for x in rows):
        raise ValueError("invalid preselection decision provenance")
    if {name: sum(x["selection_status"] == name for x in rows) for name in decisions} != decisions:
        raise ValueError("preselection decision totals mismatch")
    # Deterministic receipt-bound identity for EVERY observed ticker, including
    # screen rejects and OHLC budget exclusions. Never call these outcome labels.
    for row in rows:
        row["observation_id"] = hashlib.sha256(
            ("paper-preselection-v1|" + verified["receipt_sha256"] + "|" + row["pair"]).encode()
        ).hexdigest()
    watch_by_pair = {x["pair"]: x for x in verified["watch"]}
    if any(row["watch_rank"] != watch_by_pair[row["pair"]]["rank"]
           for row in rows if row["selection_status"] == "WATCH"):
        raise ValueError("WATCH rank differs from sealed candidate snapshot")
    if set(watch_by_pair) != {row["pair"] for row in rows if row["selection_status"] == "WATCH"}:
        raise ValueError("WATCH identities differ from complete preselection")
    return {"schema": "paper_preselection_v1", "as_of": verified["as_of"],
            "receipt_sha256": verified["receipt_sha256"],
            "coverage": coverage, "selection_decisions": decisions, "markets": rows,
            "identity_semantics": "sha256(paper-preselection-v1|receipt_sha256|pair)",
            "future_outcomes_authenticated": False, "qualified_for_learning": False,
            "production_applied": False,
            "snapshot_use": "HISTORICAL_RESEARCH_ONLY" if historical else "FRESH_PAPER_OBSERVATION",
            "live_watch_eligible": not historical}


def main():
    p = argparse.ArgumentParser()
    p.add_argument("latest")
    p.add_argument("--output", required=True)
    p.add_argument("--historical", action="store_true", help="receipt-verified historical universe; never live WATCH")
    args = p.parse_args()
    Path(args.output).write_text(json.dumps(export_universe(args.latest, historical=args.historical), sort_keys=True, allow_nan=False) + "\n")


if __name__ == "__main__":
    main()
