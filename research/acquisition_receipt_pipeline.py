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
    if associations_directory is None:
        raise ValueError("authenticated depth associations required")
    original_captures = captures
    association_exclusions = []
    if associations_directory is not None:
        captures, association_exclusions, _ = verified_associations(
            captures_directory, associations_directory, depth_directory)
    report = bind(ledger, depth_directory, captures)
    report["association_exclusions"] = association_exclusions
    report["association_excluded_count"] = len(association_exclusions)
    report["capture_count"] = len(original_captures)
    report["capture_sha256"] = hashlib.sha256(
        json.dumps(original_captures, sort_keys=True, separators=(",", ":")).encode()
    ).hexdigest()
    # These independently bound receipts are the only allowable input to E2/E3.
    # Never export raw captures or caller-supplied depth claims as authenticated.
    report["reconciliation_receipts"] = [dict(r) for r in report["accepted"]]
    report["reconciliation_receipt_count"] = len(report["reconciliation_receipts"])
    report["mode"] = "RESEARCH_ONLY_ACQUISITION_PIPELINE"
    report["production_applied"] = False
    return report

def evaluate_learning(ledger, depth_directory, captures_directory, associations_directory,
                      evidence, *, split_at, baseline_version, challenger_version,
                      evidence_sha256):
    """Authenticate score/depth, reconcile source outcomes, then decide shadow only."""
    from research.reconcile_paper_scores import reconcile
    binding = evaluate(ledger, depth_directory, captures_directory, associations_directory)
    result = reconcile(
        ledger, evidence, split_at=split_at, baseline_version=baseline_version,
        challenger_version=challenger_version, evidence_sha256=evidence_sha256,
        score_receipts=binding["reconciliation_receipts"])
    result["acquisition_coverage"] = {
        "captures": binding["capture_count"],
        "authenticated_receipts": binding["reconciliation_receipt_count"],
        "association_exclusions": binding["association_excluded_count"],
        "binder_exclusions": binding["excluded_count"],
        "verified_depth_rows": binding["verified_depth_rows"],
        "depth_abstentions": len(binding["source_abstentions"])}
    result["production_applied"] = False
    return result


def evaluate_learning_horizons(ledger, depth_directory, captures_directory,
                               associations_directory, round_index, *, split_at,
                               baseline_version, challenger_version, evidence_sha256):
    """One authenticated score binding, four independent held-out horizons."""
    from research.reconcile_paper_scores import reconcile
    from research.prospective_round_store import evaluate_index
    binding = evaluate(ledger, depth_directory, captures_directory, associations_directory)
    results = {}
    for hours in (1, 6, 24, 48):
        evidence = evaluate_index(round_index, hours)
        result = reconcile(ledger, evidence, split_at=split_at,
                           baseline_version=baseline_version,
                           challenger_version=challenger_version,
                           evidence_sha256=evidence_sha256,
                           score_receipts=binding["reconciliation_receipts"])
        results[str(hours)] = result
    return {"mode": "RESEARCH_ONLY_MULTI_HORIZON_LEARNING",
            "acquisition_coverage": {
                "captures": binding["capture_count"],
                "authenticated_receipts": binding["reconciliation_receipt_count"],
                "association_exclusions": binding["association_excluded_count"],
                "binder_exclusions": binding["excluded_count"]},
            "horizon_comparisons": results, "production_applied": False}


def evaluate_horizons(round_index, horizons=(1, 6, 24, 48)):
    """Read-only qualified horizon coverage; missing future data is never a miss."""
    from research.prospective_round_store import evaluate_index
    result = {}
    for hours in horizons:
        if hours not in (1, 6, 24, 48):
            raise ValueError("unsupported evaluation horizon")
        evidence = evaluate_index(round_index, hours)
        outcomes = evidence["outcomes"]
        qualified = [r for r in outcomes if r.get("status") == "QUALIFIED_OBSERVED_PATH"]
        result[str(hours)] = {
            "rounds_verified": evidence["rounds_verified"],
            "snapshots_verified": evidence["snapshots_verified"],
            "qualified": len(qualified),
            "observed_ge30pct": sum(r.get("ge30pct") is True for r in qualified),
            "incomplete_or_unqualified": len(outcomes) - len(qualified),
            "source_abstentions": len(evidence["abstentions"]),
            "production_applied": False}
    return result


def source_only_coverage(round_index, output):
    """Execute E1 without requiring unrelated paper score/depth receipts."""
    if not round_index:
        raise ValueError("authenticated round index required")
    report = {"round_index_sha256": hashlib.sha256(Path(round_index).read_bytes()).hexdigest(),
              "mode": "RESEARCH_ONLY_SOURCE_COVERAGE",
              "horizon_coverage": evaluate_horizons(round_index),
              "production_applied": False}
    return write_new(output, report)


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
    parser.add_argument("--paper-ledger")
    parser.add_argument("--depth-directory")
    parser.add_argument("--captures-directory")
    parser.add_argument("--output", required=True)
    parser.add_argument("--associations-directory")
    parser.add_argument("--associate-verified-depth", action="store_true",
                        help="Bind scoring-time receipts to verified source before E1-E3")
    parser.add_argument("--round-index")
    parser.add_argument("--all-horizon-coverage", action="store_true")
    parser.add_argument("--all-horizon-learning", action="store_true")
    parser.add_argument("--split-at", type=float)
    parser.add_argument("--baseline-version")
    parser.add_argument("--challenger-version")
    parser.add_argument("--learning-ledger", help="Research-only append-only E3 decisions")
    args = parser.parse_args()
    if args.associate_verified_depth and not args.paper_ledger:
        parser.error("automatic association requires a paper ledger")
    if args.associate_verified_depth and args.all_horizon_coverage and not args.round_index:
        parser.error("coverage evaluation requires round index")
    if args.associate_verified_depth and args.all_horizon_learning and not (
            args.round_index and args.split_at is not None and
            args.baseline_version and args.challenger_version):
        parser.error("multi-horizon learning requires index, split and versions")
    if args.associate_verified_depth and Path(args.output).exists():
        parser.error("output exists; refusing to create associations before report")
    if args.associate_verified_depth:
        if not all((args.captures_directory, args.depth_directory, args.associations_directory)):
            parser.error("automatic association requires captures, depth and association directories")
        from research.depth_acquisition_associations import associate_captured_scores
        association_report = associate_captured_scores(
            args.captures_directory, args.depth_directory, args.associations_directory)
        print(json.dumps({"association_attempted": True,
                          "associated": len(association_report["associated"]),
                          "excluded": len(association_report["excluded"])}, sort_keys=True))
    source_only = (args.all_horizon_coverage and not any((
        args.paper_ledger, args.depth_directory, args.captures_directory,
        args.associations_directory, args.split_at is not None,
        args.baseline_version, args.challenger_version, args.learning_ledger)))
    if source_only:
        digest = source_only_coverage(args.round_index, args.output)
        print(json.dumps({"mode": "RESEARCH_ONLY_SOURCE_COVERAGE",
                          "report_sha256": digest}, sort_keys=True))
        return
    if not all((args.paper_ledger, args.depth_directory,
                args.captures_directory, args.associations_directory)):
        parser.error("score/depth evaluation requires all authenticated inputs")
    if args.all_horizon_learning:
        if not (args.round_index and args.split_at is not None and
                args.baseline_version and args.challenger_version):
            parser.error("multi-horizon learning requires index, split and versions")
        if args.learning_ledger:
            parser.error("multi-horizon learning cannot append multiple shadow decisions")
        ledger_bytes = Path(args.paper_ledger).read_bytes()
        index_bytes = Path(args.round_index).read_bytes()
        report = evaluate_learning_horizons(
            json.loads(ledger_bytes), args.depth_directory, args.captures_directory,
            args.associations_directory, args.round_index, split_at=args.split_at,
            baseline_version=args.baseline_version,
            challenger_version=args.challenger_version,
            evidence_sha256=hashlib.sha256(ledger_bytes + index_bytes).hexdigest())
        digest = write_new(args.output, report)
        print(json.dumps({"mode": report["mode"], "report_sha256": digest}, sort_keys=True))
        return
    ledger = json.loads(Path(args.paper_ledger).read_bytes())
    report = evaluate(ledger, args.depth_directory, args.captures_directory,
                      args.associations_directory)
    requested = [args.split_at is not None,
                 args.baseline_version is not None, args.challenger_version is not None]
    if args.all_horizon_coverage and not args.round_index:
        parser.error("--all-horizon-coverage requires --round-index")
    if any(requested):
        if not all(requested) or args.round_index is None:
            parser.error("round-index, split-at and both versions must be supplied together")
        from research.prospective_round_store import evaluate_index
        from research.learning_feedback import append_decision
        index_bytes = Path(args.round_index).read_bytes()
        evidence = evaluate_index(args.round_index, 1)
        report = evaluate_learning(
            ledger, args.depth_directory, args.captures_directory,
            args.associations_directory, evidence, split_at=args.split_at,
            baseline_version=args.baseline_version,
            challenger_version=args.challenger_version,
            evidence_sha256=hashlib.sha256(
                Path(args.paper_ledger).read_bytes() + index_bytes).hexdigest())
        if args.learning_ledger:
            report["learning_record"] = append_decision(
                args.learning_ledger, report["shadow_decision"])
    elif args.learning_ledger:
        parser.error("learning-ledger requires complete E2/E3 evaluation arguments")
    if args.all_horizon_coverage:
        report["horizon_coverage"] = evaluate_horizons(args.round_index)
    digest = write_new(args.output, report)
    print(json.dumps({"authenticated_receipts": report.get("reconciliation_receipt_count",
                           report.get("acquisition_coverage", {}).get("authenticated_receipts", 0)),
                      "shadow_decision": report.get("shadow_decision", {}).get("decision"),
                      "report_sha256": digest}, sort_keys=True))


if __name__ == "__main__":
    main()
