"""Capture research-only score evidence at scoring time, before depth observation.

Caller must invoke capture_score synchronously when a score is computed.  Never
backfill timestamps from historical ledger rows. The depth association is made
later by bind_acquisition_receipts using independently verified source bytes.
"""
import hashlib
import json
import math
import os
import time
from pathlib import Path


def capture_score(directory, *, prediction_id, pair, baseline_score,
                  challenger_score, observed_at=None):
    if not isinstance(prediction_id, str) or len(prediction_id) != 64 or any(
        c not in "0123456789abcdef" for c in prediction_id
    ):
        raise ValueError("invalid prediction identity")
    if not isinstance(pair, str) or not pair.strip():
        raise ValueError("invalid pair")
    for score in (baseline_score, challenger_score):
        if type(score) not in (int, float) or not math.isfinite(score):
            raise ValueError("nonfinite score")
    # A caller may supply the actual event timestamp for deterministic tests,
    # but this API must be invoked at acquisition, never from old ledger data.
    timestamp = time.time() if observed_at is None else observed_at
    if type(timestamp) not in (int, float) or not math.isfinite(timestamp) or timestamp < 0:
        raise ValueError("invalid observation timestamp")
    record = {"schema": 1, "prediction_id": prediction_id, "pair": pair,
              "baseline_score": baseline_score, "challenger_score": challenger_score,
              "score_observed_at": timestamp, "mode": "RESEARCH_ONLY"}
    raw = (json.dumps(record, sort_keys=True, separators=(",", ":"), allow_nan=False) + "\n").encode()
    path = Path(directory)
    path.mkdir(parents=True, exist_ok=True)
    target = path / (prediction_id + ".json")
    # Exclusive creation: a retry may not rewrite score or observation time.
    fd = os.open(target, os.O_WRONLY | os.O_CREAT | os.O_EXCL, 0o600)
    try:
        with os.fdopen(fd, "wb") as output:
            output.write(raw)
            output.flush()
            os.fsync(output.fileno())
    except BaseException:
        target.unlink(missing_ok=True)
        raise
    return {"path": str(target), "sha256": hashlib.sha256(raw).hexdigest(), "receipt": record}


def attach_verified_depth(capture, source_row):
    """Bind only after source validation; preserve original capture bytes."""
    record = capture["receipt"]
    if record["pair"] != source_row["pair"]:
        raise ValueError("pair mismatch")
    if record["score_observed_at"] > source_row["first_observed_at"]:
        raise ValueError("score recorded after depth observation")
    source = source_row["source_sha256"]
    if not isinstance(source, str) or len(source) != 64:
        raise ValueError("invalid source digest")
    return {k: record[k] for k in ("prediction_id", "pair", "baseline_score",
                                   "challenger_score", "score_observed_at")} | {
        "source_sha256": source
    }
