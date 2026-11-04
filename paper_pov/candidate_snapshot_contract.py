"""Read-only scanner snapshot contract shared by manual and scheduled invocations.

This module validates scanner output without creating a ledger writer, altering
the scanner's scoring, or inventing exchange timestamps.
"""
import hashlib
import json
import math
from .scanner import utc


def candidate_snapshot(report, *, source_sha, invocation):
    if invocation not in ("manual", "scheduled"):
        raise ValueError("Unknown invocation")
    if not isinstance(source_sha, str) or len(source_sha) != 40 or any(c not in "0123456789abcdef" for c in source_sha):
        raise ValueError("Invalid source commit")
    if not isinstance(report, dict):
        raise ValueError("Missing scanner report")
    # A snapshot is a read-only serialization of the existing scanner report,
    # not a new scoring path. Canonical digest must not depend on invocation.
    canonical = json.dumps(report, sort_keys=True, separators=(",", ":"), allow_nan=False).encode()
    return {"schema": "paper_scan_candidate_snapshot_v1",
            "invocation": invocation,
            "source_sha": source_sha,
            "report_sha256": hashlib.sha256(canonical).hexdigest(),
            "report": report,
            "production_applied": False}


def compare_invocations(manual, scheduled):
    for snapshot, kind in ((manual, "manual"), (scheduled, "scheduled")):
        if snapshot.get("schema") != "paper_scan_candidate_snapshot_v1" or snapshot.get("invocation") != kind:
            raise ValueError("Mismatched invocation snapshot")
    if manual["source_sha"] != scheduled["source_sha"]:
        raise ValueError("Different source commits")
    if manual["report_sha256"] != scheduled["report_sha256"]:
        return {"schema": "paper_scan_parity_v1", "equivalent": False,
                "reason": "REPORT_CONTENT_DIFFERS", "production_applied": False}
    return {"schema": "paper_scan_parity_v1", "equivalent": True,
            "reason": "IDENTICAL_REPORT_BYTES", "production_applied": False}
