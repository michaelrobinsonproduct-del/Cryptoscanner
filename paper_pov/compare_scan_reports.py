"""Read-only comparison of two existing scanner JSON reports.

Never dispatches scans or writes the paper ledger. Produces an explicit
comparison artifact suitable for CI and manual/scheduled acceptance.
"""
import argparse
import json
from pathlib import Path
from .candidate_snapshot_contract import candidate_snapshot, compare_invocations
from .scanner import atomic_json


def compare_reports(manual_report, scheduled_report, *, manual_sha, scheduled_sha):
    a = candidate_snapshot(manual_report, source_sha=manual_sha, invocation="manual")
    b = candidate_snapshot(scheduled_report, source_sha=scheduled_sha, invocation="scheduled")
    if manual_sha != scheduled_sha:
        return {"schema": "paper_scan_parity_v1", "equivalent": False,
                "reason": "SOURCE_SHA_MISMATCH", "manual_sha": manual_sha,
                "scheduled_sha": scheduled_sha, "production_applied": False}
    comparison = compare_invocations(a, b)
    comparison["manual_report_sha256"] = a["report_sha256"]
    comparison["scheduled_report_sha256"] = b["report_sha256"]
    comparison["source_sha"] = manual_sha
    return comparison


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--manual-report", required=True)
    parser.add_argument("--scheduled-report", required=True)
    parser.add_argument("--manual-sha", required=True)
    parser.add_argument("--scheduled-sha", required=True)
    parser.add_argument("--output", required=True)
    args = parser.parse_args()
    result = compare_reports(json.loads(Path(args.manual_report).read_text()),
                             json.loads(Path(args.scheduled_report).read_text()),
                             manual_sha=args.manual_sha, scheduled_sha=args.scheduled_sha)
    atomic_json(args.output, result)
    print(json.dumps(result, sort_keys=True))
    if not result["equivalent"]:
        raise SystemExit(2)


if __name__ == "__main__":
    main()
