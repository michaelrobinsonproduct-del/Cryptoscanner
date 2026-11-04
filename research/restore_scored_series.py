"""Restore immutable research rounds across GitHub jobs, then collect one real follow-up.

Input is a previously published scored series directory. Archive relocation changes
only local paths in a *new* index; original receipts/manifest bytes remain untouched.
Never infer elapsed time, synthesize quotes, modify the source or write production.
"""
import argparse
import hashlib
import json
import shutil
from pathlib import Path

from research.prospective_round_store import append_round, evaluate_index
from research.authenticated_learning_loop import evaluate_all
from research.prospective_outcome_adapter import verified_rows
from research.acquisition_receipt_pipeline import load_captures
from research.kraken_prospective_batch import collect, MAX_PAIRS


def restore_and_capture(previous, output_root, *, collector=collect):
    previous = Path(previous).resolve(strict=True)
    output = Path(output_root)
    if not previous.is_dir() or previous.is_symlink():
        raise ValueError("invalid previous scored series")
    old_index = previous / "entry" / "round-index.jsonl"
    old_scores = previous / "entry" / "scores"
    if not old_index.is_file() or old_index.is_symlink() or not old_scores.is_dir():
        raise ValueError("missing scored entry/index")
    captures = load_captures(old_scores)
    pairs = list(dict.fromkeys(c["pair"] for c in captures))
    if not 1 <= len(pairs) <= MAX_PAIRS:
        raise ValueError("invalid original scored market cohort")
    lines = old_index.read_text().splitlines()
    if not 1 <= len(lines) <= 576:  # permits the 577th terminal 48-hour round
        raise ValueError("invalid round count")
    records = [json.loads(line) for line in lines]
    if len({r["batch"] for r in records}) != len(records):
        raise ValueError("duplicate original source round")
    # The old GitHub runner's absolute directories may not exist in this job.
    # Map each indexed round by its *expected ordinal* within the downloaded
    # artifact, then independently re-verify each local manifest and raw receipt.
    # Never dereference the untrusted original path from the JSON index.
    normalized = []
    for ordinal, record in enumerate(records):
        old_name = record.get("batch")
        if not isinstance(old_name, str) or not Path(old_name).is_absolute():
            raise ValueError("invalid archived batch locator")
        expected = "depth" if ordinal == 0 else "depth-%03d" % ordinal
        if Path(old_name).name != expected:
            raise ValueError("unexpected indexed round ordinal")
        relative = Path("entry/depth") if ordinal == 0 else Path(expected)
        original = previous / relative
        if original.is_symlink() or not original.is_dir():
            raise ValueError("missing local indexed round")
        manifest = original / "manifest.json"
        if manifest.is_symlink() or not manifest.is_file():
            raise ValueError("missing immutable source manifest")
        if hashlib.sha256(manifest.read_bytes()).hexdigest() != record["manifest_sha256"]:
            raise ValueError("source manifest digest mismatch")
        manifest_doc = json.loads(manifest.read_bytes())
        round_pairs = [item.get("pair") for item in manifest_doc.get("entries", [])]
        if len(round_pairs) != len(pairs) or set(round_pairs) != set(pairs):
            raise ValueError("indexed round differs from scored cohort")
        rows, abstentions = verified_rows(original)
        if len(rows) != record["snapshots_verified"] or len(abstentions) != record["abstentions"]:
            raise ValueError("original source coverage drift")
        normalized.append((record, relative))
    # Explicitly reject symlinks anywhere in archived evidence (including score files).
    if any(item.is_symlink() for item in previous.rglob("*")):
        raise ValueError("unsafe archived symlink")
    if output.exists():
        raise FileExistsError("destination must be new")
    shutil.copytree(previous, output, symlinks=False)
    new_index = output / "entry" / "round-index.jsonl"
    # Preserve original index bytes as read-only evidence, separately from
    # newly relocated index. Never rewrite the caller's original artifact.
    original_bytes = old_index.read_bytes()
    (output / "entry" / "original-index.jsonl").write_bytes(original_bytes)
    relocated = []
    for record, relative in normalized:
        target = output / relative
        updated = dict(record, batch=str(target.resolve(strict=True)))
        relocated.append(json.dumps(updated, sort_keys=True, separators=(",", ":")))
    new_index.write_text("\n".join(relocated) + "\n")
    # Verify *all* copied retained rounds before the next independent collection.
    evaluate_index(new_index, 1)
    number = len(relocated)
    destination = output / ("depth-%03d" % number)
    collector(pairs, destination)
    # A successful collection must actually cover the original scored cohort;
    # never index a substituted market simply because the collector returned.
    manifest_doc = json.loads((destination / "manifest.json").read_bytes())
    collected_pairs = [row.get("pair") for row in manifest_doc.get("entries", [])]
    if len(collected_pairs) != len(pairs) or set(collected_pairs) != set(pairs):
        raise ValueError("new depth round differs from scored cohort")
    append_round(new_index, destination)
    coverage = {str(h): evaluate_index(new_index, h) for h in (1, 6, 24, 48)}
    learning = evaluate_all(output / "entry" / "scores",\n                            output / "entry" / "associations", new_index,\n                            ledger_path=output / "shadow-decisions.jsonl")\n    return {"mode": "RESEARCH_ONLY_CROSS_JOB_FOLLOWUP",
            "rounds_verified": number + 1,
            "original_index_sha256": hashlib.sha256(original_bytes).hexdigest(),
            "round_index": str(new_index), "scored_pairs": pairs,
            "coverage": coverage, "learning": learning, "production_applied": False,
            "trading_approved": False}


def main():
    p = argparse.ArgumentParser()
    p.add_argument("--previous", required=True)
    p.add_argument("--output-root", required=True)
    a = p.parse_args()
    print(json.dumps(restore_and_capture(a.previous, a.output_root), sort_keys=True))


if __name__ == "__main__":
    main()
