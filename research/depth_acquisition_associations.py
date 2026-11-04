"""Research-only immutable depth associations, independently verified against raw Kraken bytes.

Capture must happen when the source is acquired, not from historical predictions.
Association files do not modify sealed score captures or the production ledger.
"""
import hashlib
import json
import os
import math
from pathlib import Path

from research.prospective_outcome_adapter import verified_rows


def _digest(value):
    return isinstance(value, str) and len(value) == 64 and all(c in "0123456789abcdef" for c in value)


def write_association(directory, *, prediction_id, pair, source_sha256, score_receipt_sha256,
                      source_first_observed_at=None):
    if not all(map(_digest, (prediction_id, source_sha256, score_receipt_sha256))):
        raise ValueError("invalid receipt digest")
    if not isinstance(pair, str) or not pair.strip():
        raise ValueError("invalid pair")
    record = {"schema": 1, "mode": "RESEARCH_ONLY", "prediction_id": prediction_id,
              "pair": pair, "source_sha256": source_sha256,
              "score_receipt_sha256": score_receipt_sha256}
    if source_first_observed_at is not None:\n        if type(source_first_observed_at) not in (float, int) or not math.isfinite(source_first_observed_at) or source_first_observed_at <= 0:\n            raise ValueError("invalid source receipt observation timestamp")\n        record["source_first_observed_at"] = source_first_observed_at\n    raw = (json.dumps(record, sort_keys=True, separators=(",", ":")) + "\n").encode()
    root = Path(directory)
    root.mkdir(parents=True, exist_ok=True)
    target = root / (prediction_id + ".json")
    fd = os.open(target, os.O_CREAT | os.O_EXCL | os.O_WRONLY, 0o600)
    with os.fdopen(fd, "wb") as out:
        out.write(raw)
        out.flush()
        os.fsync(out.fileno())
    return {"path": str(target), "sha256": hashlib.sha256(raw).hexdigest()}


def verified_associations(captures_directory, associations_directory, depth_directory):
    """Fail closed: association must match score bytes AND independently verified depth.

    Missing associations are explicit abstentions; malformed or forged records
    never silently become qualified evidence.
    """
    capture_root = Path(captures_directory)
    association_root = Path(associations_directory)
    if not association_root.is_dir():
        raise ValueError("association directory missing")
    if Path(depth_directory).is_file():
        rows, source_abstentions, _ = verified_index_rows(depth_directory)
    else:
        rows, source_abstentions = verified_rows(depth_directory)
    # The same authentic Kraken raw bytes can be seen in separate acquisition
    # rounds. SHA256 alone is not a unique point-in-time observation identity.
    verified = {}
    for row in rows:
        verified.setdefault((row["pair"], row["source_sha256"]), []).append(row)
    enriched, exclusions = [], []
    for path in sorted(capture_root.glob("*.json")):
        if path.is_symlink() or not path.is_file():
            raise ValueError("unsafe capture path")
        raw = path.read_bytes()
        if len(raw) > 16384:
            raise ValueError("oversized capture")
        capture = json.loads(raw)
        pid = capture.get("prediction_id")
        if not _digest(pid) or path.name != pid + ".json":
            raise ValueError("invalid capture identity")
        association_path = association_root / path.name
        if not association_path.exists():
            exclusions.append({"prediction_id": pid, "reason": "MISSING_DEPTH_ASSOCIATION"})
            continue
        if association_path.is_symlink() or not association_path.is_file():
            raise ValueError("unsafe association path")
        association_raw = association_path.read_bytes()
        if len(association_raw) > 16384:
            raise ValueError("oversized association")
        association = json.loads(association_raw)
        if (association.get("schema") != 1 or association.get("mode") != "RESEARCH_ONLY"
                or association.get("prediction_id") != pid
                or association.get("pair") != capture.get("pair")
                or association.get("score_receipt_sha256") != hashlib.sha256(raw).hexdigest()):
            exclusions.append({"prediction_id": pid, "reason": "SCORE_ASSOCIATION_MISMATCH"})
            continue
        source = association.get("source_sha256")
        candidates = verified.get((capture.get("pair"), source), [])
        observed_at = association.get("source_first_observed_at")
        if observed_at is not None:
            candidates = [row for row in candidates
                          if row["first_observed_at"] == observed_at]
        if len(candidates) != 1:
            exclusions.append({"prediction_id": pid, "reason":
                "AMBIGUOUS_SOURCE_RECEIPT" if len(candidates) > 1
                else "UNVERIFIED_DEPTH_ASSOCIATION"})
            continue
        row = candidates[0]
        observed = capture.get("score_observed_at")
        if type(observed) not in (int, float) or not (
                0 <= observed <= row["first_observed_at"] <= observed + 600):
            exclusions.append({"prediction_id": pid, "reason": "SCORE_NOT_PRE_ENTRY"})
            continue
        enriched.append({**capture, "source_sha256": source,
                         "source_first_observed_at": row["first_observed_at"]})
    return enriched, exclusions, {"verified_depth_rows": len(rows),
                                  "source_abstentions": source_abstentions}


def associate_captured_scores(captures_directory, depth_directory, associations_directory):
    from research.acquisition_receipt_pipeline import load_captures
    captures = load_captures(captures_directory)
    rows, abstentions = verified_rows(depth_directory)
    accepted, excluded = [], []
    for capture in captures:
        pid = capture['prediction_id']
        timestamp = capture['score_observed_at']
        matches = [row for row in rows if row['pair'] == capture['pair']
                   and timestamp <= row['first_observed_at'] <= timestamp + 600]
        if len(matches) != 1:
            excluded.append({'prediction_id': pid, 'reason': 'NO_UNIQUE_TIMELY_DEPTH'})
            continue
        digest = hashlib.sha256((Path(captures_directory) / (pid + '.json')).read_bytes()).hexdigest()
        write_association(associations_directory, prediction_id=pid,
                          pair=capture['pair'], source_sha256=matches[0]['source_sha256'],
                          score_receipt_sha256=digest,
                          source_first_observed_at=matches[0]["first_observed_at"])
        accepted.append(pid)
    return {'associated': accepted, 'excluded': excluded,
            'source_abstentions': abstentions, 'production_applied': False}



def verified_index_rows(round_index):
    """Authenticate all indexed prospective source batches without writing."""
    index = Path(round_index)
    records = [json.loads(line) for line in index.read_text().splitlines() if line.strip()]
    if len({r["batch"] for r in records}) != len(records):
        raise ValueError("duplicate indexed batch")
    rows, abstentions = [], []
    for record in records:
        batch = Path(record["batch"])
        if not batch.is_dir() or batch.is_symlink():
            raise ValueError("unsafe indexed batch directory")
        manifest = batch / "manifest.json"
        if manifest.is_symlink() or not manifest.is_file():
            raise ValueError("unsafe indexed manifest")
        if hashlib.sha256(manifest.read_bytes()).hexdigest() != record["manifest_sha256"]:
            raise ValueError("indexed manifest mismatch")
        verified, excluded = verified_rows(batch)
        if len(verified) != record["snapshots_verified"] or len(excluded) != record["abstentions"]:
            raise ValueError("indexed source coverage mismatch")
        rows.extend(verified)
        abstentions.extend(excluded)
    return rows, abstentions, len(records)


def associate_indexed_captures(captures_directory, round_index, associations_directory):
    """Match captured scores across immutable, manifest-verified prospective rounds."""
    from research.acquisition_receipt_pipeline import load_captures
    rows, abstentions, round_count = verified_index_rows(round_index)
    accepted, excluded = [], []
    for capture in load_captures(captures_directory):
        pid = capture["prediction_id"]
        observed = capture["score_observed_at"]
        matches = [row for row in rows if row["pair"] == capture["pair"]
                   and observed <= row["first_observed_at"] <= observed + 600]
        if len(matches) != 1:
            excluded.append({"prediction_id": pid, "reason": "NO_UNIQUE_TIMELY_DEPTH"})
            continue
        if matches[0].get("entry_liquidity_usd") is None or matches[0]["entry_liquidity_usd"] < 20:
            excluded.append({"prediction_id": pid, "reason": "INSUFFICIENT_VERIFIED_LIQUIDITY"})
            continue
        receipt = hashlib.sha256((Path(captures_directory) / (pid + ".json")).read_bytes()).hexdigest()
        write_association(associations_directory, prediction_id=pid,
                          pair=capture["pair"], source_sha256=matches[0]["source_sha256"],
                          score_receipt_sha256=receipt,
                          source_first_observed_at=matches[0]["first_observed_at"])
        accepted.append(pid)
    return {"associated": accepted, "excluded": excluded, "source_abstentions": abstentions,
            "rounds_verified": round_count, "production_applied": False}


def main():
    import argparse
    from research.acquisition_receipt_pipeline import write_new
    p = argparse.ArgumentParser()
    for name in ("captures-directory", "associations-directory", "report"):
        p.add_argument("--" + name, required=True)
    source = p.add_mutually_exclusive_group(required=True)
    source.add_argument("--depth-directory")
    source.add_argument("--round-index")
    a = p.parse_args()
    report = (associate_indexed_captures(a.captures_directory, a.round_index, a.associations_directory)
              if a.round_index else associate_captured_scores(
                  a.captures_directory, a.depth_directory, a.associations_directory))
    write_new(a.report, report)
    print(json.dumps({"associated": len(report["associated"]), "excluded": len(report["excluded"])}))


if __name__ == "__main__":
    main()
