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



def load_sealed_scan(path):
    """Consume the A persisted WATCH and preselection views without writing a ledger."""
    root = Path(path)
    if not root.is_dir() or root.is_symlink():
        raise ValueError("expected scanner output directory")
    names = ("latest.json", "candidate-snapshot.json", "preselection-universe.json")
    if any((root / n).is_symlink() or not (root / n).is_file() for n in names):
        raise ValueError("missing or linked persisted scanner projection")
    raw = (root / names[0]).read_bytes()
    report = json.loads(raw)
    watch = json.loads((root / names[1]).read_bytes())
    universe = json.loads((root / names[2]).read_bytes())
    digest = hashlib.sha256(raw).hexdigest()
    if watch.get("receipt_sha256") != digest or universe.get("receipt_sha256") != digest:
        raise ValueError("projection receipt hash mismatch")
    if watch.get("watch") != report.get("watch") or watch.get("scan_status") != report.get("scan_status"):
        raise ValueError("WATCH projection differs from sealed scan")
    if universe.get("markets") != report.get("preselection_universe"):
        raise ValueError("preselection projection differs from sealed scan")
    if universe.get("selection_decisions") != report.get("preselection_decisions"):
        raise ValueError("preselection decisions differ")
    if watch.get("as_of") != report.get("as_of") or universe.get("as_of") != report.get("as_of"):
        raise ValueError("projection timestamp mismatch")
    if universe.get("future_outcomes_authenticated") is not False or universe.get("qualified_for_learning") is not False:
        raise ValueError("unqualified learning projection")
    from datetime import datetime, timezone
    stamp = datetime.fromisoformat(report["as_of"].replace("Z", "+00:00"))
    receipt = root / "receipts" / (stamp.astimezone(timezone.utc).strftime("%Y%m%dT%H%M%S%fZ") + ".json")
    if receipt.parent.is_symlink() or receipt.is_symlink() or not receipt.is_file() or receipt.read_bytes() != raw:
        raise ValueError("missing or mismatched immutable receipt")
    canonical(report)
    return report

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("manual", type=Path)
    parser.add_argument("scheduled", type=Path)
    args = parser.parse_args()
    print("PAPER_MANUAL_SCHEDULED_PARITY_SHA256=" +
          compare(load_sealed_scan(args.manual) if args.manual.is_dir() else json.loads(args.manual.read_text()),
                  load_sealed_scan(args.scheduled) if args.scheduled.is_dir() else json.loads(args.scheduled.read_text())))


if __name__ == "__main__":
    main()
