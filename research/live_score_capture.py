"""Research-only live scanner -> immutable scoring receipts.

Run synchronously after a fresh scan, before *separately acquired* Kraken
depth. Existing historical scan outputs must never be replayed as captures.
"""
import argparse
import datetime as dt
import json
from pathlib import Path

from paper_pov.scanner import scan, utc, UTC
from research.capture_acquisition_scores import capture_score


def capture_live_scan(directory, *, scanner=scan, clock=None):
    clock = clock or (lambda: dt.datetime.now(UTC))
    before = clock()
    report = scanner()
    after = clock()
    if report.get("mode") != "PAPER_ONLY" or report.get("production_applied") is not False:
        raise ValueError("not a research-compatible paper scan")
    if not isinstance(report.get("watch"), list) or not report["watch"]:
        raise ValueError("no WATCH scores to capture")
    as_of = utc(report["as_of"])
    if not (before <= as_of <= after and 0 <= (after-as_of).total_seconds() <= 600):
        raise ValueError("not a synchronous live scan")
    receipts = []
    for item in report["watch"]:
        if item.get("status") != "PAPER_WATCH":
            raise ValueError("invalid WATCH status")
        if item.get("as_of") != report["as_of"]:
            raise ValueError("inconsistent scoring timestamp")
        receipts.append(capture_score(
            directory, prediction_id=item["prediction_id"], pair=item["pair"],
            baseline_score=item["baseline_score"],
            challenger_score=item["challenger_score"],
            observed_at=after.timestamp()))
    return {"mode": "RESEARCH_ONLY_LIVE_SCORE_CAPTURE",
            "captures": len(receipts), "receipt_sha256": [r["sha256"] for r in receipts],
            "capture_directory": str(Path(directory)), "production_applied": False}


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--captures-directory", required=True)
    args = parser.parse_args()
    print(json.dumps(capture_live_scan(args.captures_directory), sort_keys=True))


if __name__ == "__main__":
    main()
