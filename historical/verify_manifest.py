"""Verify compact training artifact before publication; no network or secrets required."""
import hashlib
import json
from datetime import datetime, timezone
from pathlib import Path

root = Path("historical/output")
manifest = json.loads((root / "research_training_manifest.json").read_text())
training = root / "research_training.ndjson"
if not (manifest["production_ingested"] is False): raise ValueError("artifact must not claim ingestion")
if not (manifest["sampling_policy"] == "outcome_independent_hourly_utc"): raise ValueError("unexpected training sampling policy")
if not (manifest["source_rows"] >= manifest["training_rows"] > 0): raise ValueError("invalid row counts")
if not (manifest.get("research_population_schema_version") == 2): raise ValueError("historical manifest integrity failure")
if not (manifest.get("research_population_policy") == "all_eligible_15m_anchors"): raise ValueError("historical manifest integrity failure")
if not (manifest["training_file"] == str(training)): raise ValueError("training path mismatch")
if not (training.is_file()): raise ValueError("missing training dataset")

sha = hashlib.sha256()
count = 0
seen_anchors = set()
earliest = None
latest = None
with training.open("rb") as handle:
    for number, raw in enumerate(handle, 1):
        sha.update(raw)
        if not raw.strip():
            continue
        row = json.loads(raw)
        assert isinstance(row.get("pair"), str) and row["pair"].strip(), f"invalid pair at {number}"
        ts = datetime.fromisoformat(row["anchor_at"].replace("Z", "+00:00"))
        assert ts.tzinfo is not None, f"naive timestamp at {number}"
        ts = ts.astimezone(timezone.utc)
        key = (row["pair"], ts.isoformat())
        assert key not in seen_anchors, f"duplicate training observation at {number}"
        seen_anchors.add(key)
        assert ts.minute == 0 and ts.second == 0 and ts.microsecond == 0, f"training sample not hourly at {number}"
        assert datetime(2025, 10, 4, tzinfo=timezone.utc) <= ts < datetime(2026, 7, 1, tzinfo=timezone.utc), f"training sample outside archive at {number}"
        earliest = min(earliest, ts) if earliest else ts
        latest = max(latest, ts) if latest else ts
        count += 1

if not (count == manifest["training_rows"]): raise ValueError("training row count mismatch")
if not (sha.hexdigest() == manifest["training_sha256"]): raise ValueError("training checksum mismatch")
if not (earliest.isoformat() >= manifest["earliest_anchor_utc"]): raise ValueError("earliest timestamp outside source")
if not (latest.isoformat() <= manifest["latest_anchor_utc"]): raise ValueError("latest timestamp outside source")
print(json.dumps({"verified": True, "rows": count, "sha256": sha.hexdigest()}))
