"""Read-only bridge from existing C integration report to conservative receipt verdict.

C's historical parity/recovery report is not a live Kraken quote receipt.
Never promote its WATCH count to a verified live WATCH candidate.
"""
import argparse
import json
from pathlib import Path


def assess_c_integration(report):
    if not isinstance(report, dict) or report.get("schema") != "c_read_only_integration_v1":
        return {"accepted": False, "status": "INVALID_REPORT", "errors": ["invalid_c_schema"]}
    errors = []
    if report.get("production_applied") is not False:
        errors.append("unexpected_production_application")
    if report.get("trading_approved") is not False:
        errors.append("unexpected_trading_approval")
    if report.get("exchange_event_freshness_verified") is not False:
        errors.append("unexpected_live_freshness_claim")
    if report.get("status") != "ABSTAIN_LEGACY_QUOTE_EVIDENCE":
        errors.append("not_legacy_abstention")
    if report.get("historical_artifact_parity") is not True:
        errors.append("historical_parity_unverified")
    if report.get("recovery_verified") is not True:
        errors.append("recovery_unverified")
    if report.get("a2_snapshot_attached") is True:
        digest = report.get("a2_receipt_sha256")
        if not isinstance(digest, str) or len(digest) != 64 or any(c not in "0123456789abcdef" for c in digest):
            errors.append("invalid_a2_receipt_digest")
        count = report.get("a2_watch_count")
        if type(count) is not int or count < 1:
            errors.append("invalid_a2_watch_count")
    return {
        "accepted": not errors,
        "status": "ABSTAIN_LEGACY_QUOTE_EVIDENCE" if not errors else "INVALID_REPORT",
        "live_watch_certified": False,
        "source_cohort": report.get("a2_source_cohort") if report.get("a2_snapshot_attached") is True else None,
        "errors": errors,
    }


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("report", type=Path)
    args = parser.parse_args()
    try:
        verdict = assess_c_integration(json.loads(args.report.read_text()))
    except (OSError, ValueError, TypeError):
        verdict = {"accepted": False, "status": "INVALID_REPORT", "errors": ["unreadable_report"]}
    print(json.dumps(verdict, sort_keys=True))
    return 0 if verdict["accepted"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
