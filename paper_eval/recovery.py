"""Fail-closed, read-only recovery proof for a public paper-scanner artifact.

A successful proof verifies the archived artifact against independently obtained
immutable Git ledger bytes. It does NOT establish future 30-day availability,
exchange-complete price evidence, a working live restore, or predictive lift.
"""
import argparse
import hashlib
import json
import re
from pathlib import Path

from paper_pov import ledger, segmented_storage

FILES = frozenset(("latest.json", "ledger.json", "scoreboard.json", "SHA256SUMS"))
DATA_FILES = FILES - {"SHA256SUMS"}
MAX_TOTAL_BYTES = 20_000_000
MAX_FILE_BYTES = 12_500_000
SHA_RE = re.compile(r"[0-9a-f]{40}\Z")
SUM_RE = re.compile(r"([0-9a-f]{64})  (latest\.json|ledger\.json|scoreboard\.json)\Z")


def load_bundle(directory):
    """Load four regular bounded files, refusing symlinks and unexpected entries."""
    root = Path(directory)
    if root.is_symlink() or not root.is_dir():
        raise ValueError("Missing or linked artifact directory")
    entries = list(root.iterdir())
    if {x.name for x in entries} != FILES or len(entries) != len(FILES):
        raise ValueError("Incomplete or unexpected artifact members")
    result = {}
    total = 0
    for entry in entries:
        if entry.is_symlink() or not entry.is_file():
            raise ValueError("Artifact contains linked or non-file member")
        size = entry.stat().st_size
        total += size
        if size > MAX_FILE_BYTES or total > MAX_TOTAL_BYTES:
            raise ValueError("Oversized artifact bundle")
        result[entry.name] = entry.read_bytes()
    return result


def verify_bundle(bundle, expected_ledger, expected_commit):
    """Prove exact recovery from an artifact against independent Git ledger bytes.

    expected_ledger must be read independently from the immutable ledger commit
    (e.g. git show SHA:paper-ledger.json), NOT from the artifact being checked.
    """
    if not isinstance(bundle, dict) or set(bundle) != FILES:
        raise ValueError("Incomplete or unexpected artifact members")
    if not SHA_RE.fullmatch(expected_commit or ""):
        raise ValueError("Missing exact immutable ledger commit")
    if not isinstance(expected_ledger, bytes):
        raise ValueError("Independent immutable ledger bytes required")
    if any(not isinstance(value, bytes) for value in bundle.values()):
        raise ValueError("Artifact members must be raw bytes")
    if (len(expected_ledger) > MAX_FILE_BYTES or
            any(len(value) > MAX_FILE_BYTES for value in bundle.values()) or
            sum(map(len, bundle.values())) > MAX_TOTAL_BYTES):
        raise ValueError("Oversized artifact bundle")
    if bundle["ledger.json"] != expected_ledger:
        raise ValueError("Artifact ledger differs from independent Git snapshot")

    try:
        lines = bundle["SHA256SUMS"].decode("ascii").splitlines()
    except UnicodeDecodeError as exc:
        raise ValueError("Invalid artifact SHA256SUMS encoding") from exc
    matches = [SUM_RE.fullmatch(line) for line in lines]
    if (len(matches) != len(DATA_FILES) or any(m is None for m in matches) or
            {m.group(2) for m in matches} != DATA_FILES):
        raise ValueError("Invalid or incomplete artifact SHA256SUMS manifest")
    for match in matches:
        name = match.group(2)
        if hashlib.sha256(bundle[name]).hexdigest() != match.group(1):
            raise ValueError("Artifact SHA256 mismatch for " + name)

    try:
        state = json.loads(bundle["ledger.json"])
        report = json.loads(bundle["latest.json"])
        scoreboard = json.loads(bundle["scoreboard.json"])
    except (ValueError, UnicodeDecodeError) as exc:
        raise ValueError("Invalid artifact JSON") from exc
    ledger.verify(state, segmented_storage.MAX_RAW_BYTES)
    if scoreboard != ledger.scoreboard(state, segmented_storage.MAX_RAW_BYTES):
        raise ValueError("Artifact scoreboard disagrees with recovered ledger")
    if not state["runs"] or state["generation"] == 0:
        raise ValueError("Artifact has no recoverable latest scan")
    latest = state["runs"][-1]
    if (report.get("mode") != "PAPER_ONLY" or
            report.get("buy_approved") is not False or
            report.get("production_applied") is not False):
        raise ValueError("Artifact latest report is not paper-only")
    report_hash = hashlib.sha256(ledger.canonical(report)).hexdigest()
    run_id = hashlib.sha256(
        (latest["source_sha"] + "|" + report_hash).encode()).hexdigest()
    if (latest["report_sha256"] != report_hash or latest["id"] != run_id or
            latest["as_of"] != report.get("as_of")):
        raise ValueError("Latest report does not bind to immutable ledger run")

    predictions = [p for p in state["predictions"] if p["run_id"] == run_id]
    observations = [o for o in state["observations"] if o["run_id"] == run_id]
    watch = report.get("watch")
    quotes = report.get("observations")
    if (not isinstance(watch, list) or not isinstance(quotes, list) or
            len(predictions) != len(watch) or len(observations) != len(quotes)):
        raise ValueError("Latest report count differs from ledger")
    pred_map = {p["pair"]: p for p in predictions}
    obs_map = {o["pair"]: o for o in observations}
    if len(pred_map) != len(watch) or len(obs_map) != len(quotes):
        raise ValueError("Duplicate latest report markets")
    for p in watch:
        actual = pred_map.get(p["pair"])
        if (actual is None or
                any(actual[field] != p[field] for field in
                    ("prediction_id", "as_of", "price", "baseline_score",
                     "challenger_score", "rank"))):
            raise ValueError("Latest watch differs from immutable prediction")
    for q in quotes:
        actual = obs_map.get(q["pair"])
        if (actual is None or actual["price"] != q["price"] or
                actual["at"] != q["observed_at"]):
            raise ValueError("Latest quote differs from immutable observation")
    return {
        "schema": 1,
        "mode": "READ_ONLY_PAPER_ARTIFACT_RECOVERY_PROOF",
        "ledger_commit": expected_commit,
        "ledger_generation": state["generation"],
        "ledger_sha256": state["sha256"],
        "source_sha": latest["source_sha"],
        "last_run_id": latest["id"],
        "scans_recovered": ledger.scoreboard(state, segmented_storage.MAX_RAW_BYTES)["actual_scans"],
        "latest_predictions_recovered": len(predictions),
        "latest_observations_recovered": len(observations),
        "manifest_members_verified": len(DATA_FILES),
        "remote_git_bytes_match": True,
        "restoration_to_live_writer_tested": False,
        "thirty_day_recovery_proven": False,
        "independent_held_out_lift": None,
        "production_applied": False,
    }


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--artifact-directory", required=True)
    parser.add_argument("--independent-ledger", required=True)
    parser.add_argument("--ledger-commit", required=True)
    parser.add_argument("--output", required=True)
    args = parser.parse_args()
    bundle = load_bundle(args.artifact_directory)
    independent = Path(args.independent_ledger).read_bytes()
    result = verify_bundle(bundle, independent, args.ledger_commit)
    result["report_sha256"] = hashlib.sha256(ledger.canonical(result)).hexdigest()
    from paper_pov.scanner import atomic_json
    atomic_json(args.output, result)
    if json.loads(Path(args.output).read_text()) != result:
        raise ValueError("Recovery proof readback mismatch")
    print("PAPER_ARTIFACT_RECOVERY_PROOF", json.dumps(result, sort_keys=True))


if __name__ == "__main__":
    main()
