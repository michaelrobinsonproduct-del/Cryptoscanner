"""Restore immutable research rounds across GitHub jobs, then collect one real follow-up.

Input is a previously published scored series directory. Archive relocation changes
only local paths in a *new* index; original receipts/manifest bytes remain untouched.
Never infer elapsed time, synthesize quotes, modify the source or write production.
"""
import argparse
import hashlib
import json
import shutil
import time
from pathlib import Path

from research.prospective_round_store import append_round, evaluate_index
from research.authenticated_learning_loop import evaluate_all
from research.prospective_outcome_adapter import verified_rows
from research.acquisition_receipt_pipeline import load_captures
from research.kraken_prospective_batch import collect, MAX_PAIRS


def restore_and_capture(previous, output_root, *, collector=collect, followup_rounds=1,
                        interval_seconds=300, clock=time.monotonic, sleep=time.sleep,
                        epoch_clock=time.time):
    if type(followup_rounds) is not int or not 1 <= followup_rounds <= 13:
        raise ValueError("follow-up rounds must be 1..13")
    if type(interval_seconds) is not int or interval_seconds < 300:
        raise ValueError("minimum source interval is 300 seconds")
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
    # Each continuation retains its predecessor's report without replacing
    # immutable evidence; the newest report is always the root report.
    prior_report = output / "continuation-report.json"
    if prior_report.exists():
        history = output / "continuation-history"
        history.mkdir(exist_ok=True)
        history_target = history / ("through-%03d-rounds.json" % len(records))
        prior_report.rename(history_target)
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
    first = len(relocated)
    acquired_rounds = min(followup_rounds, 577 - first)
    # Preserve the preceding real receipt time so cross-job continuation can
    # actually begin on the next five-minute slot instead of starting early.
    previous_rows, _ = verified_rows(output / normalized[-1][1])
    last_observed = max((float(row["first_observed_at"]) for row in previous_rows), default=None)
    deadline = last_observed + interval_seconds if last_observed is not None else None
    wait = max(0.0, deadline - float(epoch_clock())) if deadline is not None else 0.0
    if wait > interval_seconds + 60:
        raise ValueError("previous source observation is in the future")
    if wait:
        sleep(wait)
    # A 13-round continuation retains twelve bounded five-minute intervals in
    # one runner, rather than depending on a fresh manual dispatch each slot.
    # The first observation is made now: missed intervals are never synthesized.
    started = clock()
    for offset in range(acquired_rounds):
        target = started + offset * interval_seconds
        delay = target - clock()
        if delay > 0:
            sleep(delay)
        number = first + offset
        destination = output / ("depth-%03d" % number)
        collector(pairs, destination)
        # Each newly collected market MUST be the original scored cohort.
        manifest_doc = json.loads((destination / "manifest.json").read_bytes())
        collected_pairs = [row.get("pair") for row in manifest_doc.get("entries", [])]
        if len(collected_pairs) != len(pairs) or set(collected_pairs) != set(pairs):
            raise ValueError("new depth round differs from scored cohort")
        append_round(new_index, destination)
    coverage = {str(h): evaluate_index(new_index, h) for h in (1, 6, 24, 48)}
    learning = evaluate_all(output / "entry" / "scores",
                            output / "entry" / "associations", new_index,
                            ledger_path=output / "shadow-decisions.jsonl")
    report = {"mode": "RESEARCH_ONLY_CROSS_JOB_FOLLOWUP",
            "rounds_verified": first + acquired_rounds,
            "followup_rounds_requested": followup_rounds,
            "followup_rounds_acquired": acquired_rounds,
            "previous_last_observed_at": last_observed,
            "resume_wait_seconds": wait,
            "original_index_sha256": hashlib.sha256(original_bytes).hexdigest(),
            "round_index": str(new_index), "scored_pairs": pairs,
            "coverage": coverage, "learning": learning, "production_applied": False,
            "trading_approved": False}
    with (output / "continuation-report.json").open("x", encoding="utf-8") as handle:
        json.dump(report, handle, sort_keys=True, allow_nan=False)
        handle.write("\n")
    return report


def main():
    p = argparse.ArgumentParser()
    p.add_argument("--previous", required=True)
    p.add_argument("--output-root", required=True)
    p.add_argument("--followup-rounds", type=int, default=1)
    a = p.parse_args()
    print(json.dumps(restore_and_capture(a.previous, a.output_root,
                                         followup_rounds=a.followup_rounds), sort_keys=True))


if __name__ == "__main__":
    main()
