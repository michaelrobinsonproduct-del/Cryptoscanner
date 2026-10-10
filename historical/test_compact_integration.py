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
                "major_mover": (minute == 15 or (minute == 0 and hour % 2 == 0)),
                "still_early": minute == 15,
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
    assert sum(bool(row["major_mover"]) for row in training) == 2, "hourly sampling excluded winners"
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

    # Rebuild clean input and exercise the verifier against forged provenance.
    (output / "research.ndjson").write_text(
        "".join(json.dumps(row) + "\n" for row in rows), encoding="utf-8"
    )
    result = run(COMPACT, temp)
    assert result.returncode == 0, result.stderr
    manifest_path = output / "research_training_manifest.json"
    valid_manifest = json.loads(manifest_path.read_text())
    for field, forged in [
        ("research_population_schema_version", 1),
        ("research_population_policy", "winner_only"),
        ("sampling_policy", "outcome_conditioned"),
        ("production_ingested", True),
        ("training_rows", 999),
        ("training_sha256", "0" * 64),
    ]:
        changed = dict(valid_manifest)
        changed[field] = forged
        manifest_path.write_text(json.dumps(changed), encoding="utf-8")
        result = run(VERIFY, temp)
        assert result.returncode != 0, f"forged manifest field accepted: {field}"
        print("PASS reject_forged_" + field)
    manifest_path.write_text(json.dumps(valid_manifest), encoding="utf-8")
    assert run(VERIFY, temp).returncode == 0
    print("PASS restore_valid_manifest")


    # Reject invalid source records, not just corrupt derived artifacts.
    for label, invalid in [
        ("blank_pair", {**rows[0], "pair": "   "}),
        ("naive_anchor", {**rows[0], "anchor_at": "2026-01-02T00:00:00"}),
        ("off_grid_anchor", {**rows[0], "anchor_at": "2026-01-02T00:01:00+00:00"}),
        ("before_archive", {**rows[0], "anchor_at": "2025-10-03T00:00:00+00:00"}),
        ("after_archive", {**rows[0], "anchor_at": "2026-07-01T00:00:00+00:00"}),
    ]:
        (output / "research.ndjson").write_text(json.dumps(invalid) + "\n", encoding="utf-8")
        result = run(COMPACT, temp)
        assert result.returncode != 0, f"invalid source accepted: {label}"
        print("PASS reject_source_" + label)
