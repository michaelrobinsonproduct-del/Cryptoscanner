import hashlib
import json
import os
from datetime import datetime, timezone

src = "historical/output/research.ndjson"
dst = "historical/output/research_training.ndjson"
manifest_path = "historical/output/research_training_manifest.json"
seen = set()
kept = 0
processed = 0
earliest = None
latest = None
digest = hashlib.sha256()

with open(src, encoding="utf-8") as source, open(dst, "w", encoding="utf-8") as target:
    for line_number, line in enumerate(source, 1):
        if not line.strip():
            continue
        x = json.loads(line)
        pair = x.get("pair")
        anchor = x.get("anchor_at")
        if not isinstance(pair, str) or not pair.strip() or not isinstance(anchor, str):
            raise ValueError(f"invalid historical row at line {line_number}")
        timestamp = datetime.fromisoformat(anchor.replace("Z", "+00:00"))
        if timestamp.tzinfo is None:
            raise ValueError(f"historical row has no timezone at line {line_number}")
        anchor_utc = timestamp.astimezone(timezone.utc)
        if anchor_utc.minute % 15 != 0 or anchor_utc.second != 0 or anchor_utc.microsecond != 0:
            raise ValueError(f"historical anchor is not on a 15-minute boundary at line {line_number}")
        if anchor_utc < datetime(2025, 10, 4, tzinfo=timezone.utc) or anchor_utc >= datetime(2026, 7, 1, tzinfo=timezone.utc):
            raise ValueError(f"historical anchor outside source coverage at line {line_number}")
        if anchor_utc > datetime.now(timezone.utc):
            raise ValueError(f"future historical anchor at line {line_number}")
        earliest = min(earliest, anchor_utc) if earliest else anchor_utc
        latest = max(latest, anchor_utc) if latest else anchor_utc
        processed += 1
        key = (pair, anchor_utc.isoformat())
        if key in seen:
            raise ValueError(f"duplicate pair/anchor at line {line_number}")
        seen.add(key)
        # Outcome-independent hourly sampling avoids selecting training rows by future returns.
        keep = anchor_utc.minute == 0
        if keep:
            serialized = json.dumps(x, separators=(",", ":")) + "\n"
            target.write(serialized)
            digest.update(serialized.encode("utf-8"))
            kept += 1

if processed == 0 or kept == 0:
    raise RuntimeError("empty historical training dataset")

manifest = {
    "source": src,
    "training_file": dst,
    "source_rows": processed,
    "training_rows": kept,
    "earliest_anchor_utc": earliest.isoformat(),
    "latest_anchor_utc": latest.isoformat(),
    "training_sha256": digest.hexdigest(),
    "generated_at_utc": datetime.now(timezone.utc).isoformat(),
    "production_ingested": False,
    "sampling_policy": "outcome_independent_hourly_utc",
    "selection_bias_warning": "Historical research rows are outcome-enriched; train only on this time-sampled subset, with temporal holdout.",
}
with open(manifest_path, "w", encoding="utf-8") as out:
    json.dump(manifest, out, indent=2)
print(json.dumps(manifest))
