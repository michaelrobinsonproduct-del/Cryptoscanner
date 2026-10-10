"""Synthetic end-to-end compaction and artifact verification, no Kraken downloads."""
import json
import subprocess
import sys
import tempfile
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
COMPACT = ROOT / "historical" / "compact.py"
VERIFY = ROOT / "historical" / "verify_manifest.py"

def run(script, cwd):
    return subprocess.run([sys.executable, str(script)], cwd=cwd, text=True, capture_output=True)

with tempfile.TemporaryDirectory() as temp:
    output = Path(temp) / "historical" / "output"
    output.mkdir(parents=True)
    rows = []
    # Hourly selection must be independent of the future outcome.
    for hour in range(4):
        for minute in (0, 15, 30, 45):
            ts = datetime(2026, 1, 2, hour, minute, tzinfo=timezone.utc)
            rows.append({
                "pair": "XBTUSD", "anchor_at": ts.isoformat(),
                "major_mover": minute == 15, "still_early": minute == 15,
                "control_sampled": minute == 45, "max_forward_return_pct": 40 if minute == 15 else 0,
            })
    (output / "research.ndjson").write_text(
        "".join(json.dumps(row) + "\n" for row in rows), encoding="utf-8"
    )
    result = run(COMPACT, temp)
    assert result.returncode == 0, result.stderr
    training = [json.loads(line) for line in (output / "research_training.ndjson").read_text().splitlines()]
    assert len(training) == 4
    assert all(datetime.fromisoformat(row["anchor_at"]).minute == 0 for row in training)
    assert all(not row["major_mover"] for row in training), "outcome-dependent rows leaked into sample"
    result = run(VERIFY, temp)
    assert result.returncode == 0, result.stderr
    manifest = json.loads((output / "research_training_manifest.json").read_text())
    assert manifest["source_rows"] == 16 and manifest["training_rows"] == 4
    assert manifest["production_ingested"] is False
    assert manifest.get("research_population_schema_version") == 2
    assert manifest.get("research_population_policy") == "all_eligible_15m_anchors"
    print("PASS unbiased_hourly_compaction_and_manifest")

    # Verify that a corrupted dataset is rejected by checksum.
    with (output / "research_training.ndjson").open("a") as handle:
        handle.write("{}\n")
    result = run(VERIFY, temp)
    assert result.returncode != 0, "corrupted training artifact was accepted"
    print("PASS reject_corrupted_training_artifact")

    # Rebuild and ensure duplicate anchors are rejected.
    (output / "research.ndjson").write_text(
        "".join(json.dumps(row) + "\n" for row in rows + [rows[0]]), encoding="utf-8"
    )
    result = run(COMPACT, temp)
    assert result.returncode != 0, "duplicate source observation was accepted"
    print("PASS reject_duplicate_source_anchor")
