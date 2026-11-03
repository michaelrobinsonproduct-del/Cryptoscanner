"""Research-only acquisition receipt ingestion and authenticated depth binding.

Input receipts MUST have been written synchronously at scoring time by
capture_acquisition_scores.capture_score. This module never manufactures
historical timestamps or writes to the production paper ledger.
"""
import argparse
import hashlib
import json
import os
from pathlib import Path

from research.bind_acquisition_receipts import bind
from research.depth_acquisition_associations import verified_associations


def load_captures(directory):
    directory = Path(directory)
    if not directory.is_dir():
        raise ValueError("capture directory missing")
    receipts = []
    seen = set()
    for path in sorted(directory.glob("*.json")):
        if path.is_symlink() or not path.is_file():
            raise ValueError("unsafe capture path")
        raw = path.read_bytes()
        if len(raw) > 16384:
            raise ValueError("oversized score capture")
        record = json.loads(raw)
        pid = record.get("prediction_id")
        if (not isinstance(pid, str) or len(pid) != 64
                or any(c not in "0123456789abcdef" for c in pid)
                or path.name != pid + ".json" or pid in seen
                or record.get("schema") != 1
                or record.get("mode") != "RESEARCH_ONLY"):
            raise ValueError("invalid or duplicate score capture")
        seen.add(pid)
        receipts.append(record)
    return receipts


def evaluate(ledger, depth_directory, captures_directory, associations_directory=None):
    captures = load_captures(captures_directory)
    # Independently verified source rows are selected by binder; raw capture
    # claims are not sufficient to establish authenticated depth.
    original_captures = captures
    association_exclusions = []
    if associations_directory is not None:
        captures, association_exclusions, _ = verified_associations(
            captures_directory, associations_directory, depth_directory)
    if associations_directory is None:\n        raise ValueError("authenticated depth associations required")\n    report = bind(ledger, depth_directory, captures)
    report["association_exclusions"] = association_exclusions
    report["association_excluded_count"] = len(association_exclusions)
    report["capture_count"] = len(original_captures)
    report["capture_sha256"] = hashlib.sha256(
        json.dumps(original_captures, sort_keys=True, separators=(",", ":")).encode()
    ).hexdigest()
    # These independently bound receipts are the only allowable input to E2/E3.\n    # Never export raw captures or caller-supplied depth claims as authenticated.\n    report["reconciliation_receipts"] = [dict(r) for r in report["accepted"]]\n    report["reconciliation_receipt_count"] = len(report["reconciliation_receipts"])\n    report["mode"] = "RESEARCH_ONLY_ACQUISITION_PIPELINE"
    report["production_applied"] = False
    return report


def write_new(path, report):
    """Exclusive create; no silent replacement of a previous evaluation."""
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    payload = (json.dumps(report, sort_keys=True, allow_nan=False) + "\n").encode()
    fd = os.open(path, os.O_WRONLY | os.O_CREAT | os.O_EXCL, 0o600)
    with os.fdopen(fd, "wb") as stream:
        stream.write(payload)
        stream.flush()
        os.fsync(stream.fileno())
    return hashlib.sha256(payload).hexdigest()


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--paper-ledger", required=True)
    parser.add_argument("--depth-directory", required=True)
    parser.add_argument("--captures-directory", required=True)
    parser.add_argument("--output", required=True)
    parser.add_argument("--associations-directory", required=True)
    args = parser.parse_args()
    ledger = json.loads(Path(args.paper_ledger).read_bytes())
    report = evaluate(ledger, args.depth_directory, args.captures_directory,
                      args.associations_directory)
    digest = write_new(args.output, report)
    print(json.dumps({"accepted": report["accepted_count"],
                      "excluded": report["excluded_count"],
                      "source_abstentions": len(report["source_abstentions"]),
                      "report_sha256": digest}, sort_keys=True))


if __name__ == "__main__":
    main()
