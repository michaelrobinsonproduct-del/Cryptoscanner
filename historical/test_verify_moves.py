"""Exercise the real move-artifact validator against 100 deterministic corrupted datasets."""
import json
import subprocess
import sys
import tempfile
from datetime import datetime, timedelta, timezone
from pathlib import Path

VALIDATOR = Path(__file__).with_name("verify_moves.py").resolve()
base = datetime(2026, 1, 2, tzinfo=timezone.utc)

def episode(i):
    start = base + timedelta(minutes=15*i)
    return {
        "pair": "TESTUSD", "move_start": start.isoformat(), "peak_at": None,
        "baseline_price": 10.0, "peak_price": None, "max_return_pct": 20.0+i%80,
        "earliest_signal_at": None, "extension_at_signal_pct": None,
        "caught_early": False, "source": "kraken_archive_5m_2026q2",
        "evidence": {"windows": 1, "max_anchor_gap_minutes": 15,
                     "retrospective_label_only": True, "live_alert_verified": False,
                     "max_return_anchor": start.isoformat(),
                     "max_return_baseline_price": 10.0}
    }

with tempfile.TemporaryDirectory() as folder:
    root = Path(folder) / "historical" / "output"
    root.mkdir(parents=True)
    def run(rows, optimized=False):
        (root / "moves.ndjson").write_text("".join(json.dumps(row)+"\n" for row in rows))
        (root / "summary.json").write_text(json.dumps({"move_episodes": len(rows)}))
        command = [sys.executable]
        if optimized:
            command.append("-O")
        command.append(str(VALIDATOR))
        return subprocess.run(command, cwd=folder, capture_output=True, text=True)

    for i in range(100):
        valid = [episode(i)]
        result = run(valid, optimized=i%2==0)
        if result.returncode != 0:
            raise AssertionError(f"valid case {i} rejected: {result.stderr}")
        corrupt = episode(i)
        mode = i % 10
        if mode == 0: corrupt["caught_early"] = True
        elif mode == 1: corrupt["earliest_signal_at"] = corrupt["move_start"]
        elif mode == 2: corrupt["evidence"]["live_alert_verified"] = True
        elif mode == 3: corrupt["evidence"]["retrospective_label_only"] = False
        elif mode == 4: corrupt["evidence"]["max_anchor_gap_minutes"] = 1440
        elif mode == 5: corrupt["evidence"]["max_return_baseline_price"] = -1
        elif mode == 6: corrupt["max_return_pct"] = 19.9
        elif mode == 7: corrupt["evidence"]["windows"] = 0
        elif mode == 8: corrupt["move_start"] = "2026-01-02T00:01:00+00:00"
        else: corrupt["pair"] = ""
        result = run([corrupt], optimized=i%2==0)
        if result.returncode == 0:
            raise AssertionError(f"corrupt case {i} accepted")
    # Additional 100 negative cases exercise provenance and non-fabrication guarantees.
    for i in range(100):
        corrupt = episode(i)
        mode = i % 5
        if mode == 0: corrupt["source"] = "unknown"
        elif mode == 1: corrupt["peak_at"] = corrupt["move_start"]
        elif mode == 2: corrupt["peak_price"] = 12.0
        elif mode == 3: corrupt["extension_at_signal_pct"] = 1.0
        else: corrupt["evidence"]["max_return_anchor"] = "2026-01-01T00:00:00+00:00"
        result = run([corrupt], optimized=i%2==0)
        if result.returncode == 0:
            raise AssertionError(f"provenance corruption {i} accepted")
    for i in range(100):
        row = episode(i)
        row["evidence"]["windows"] = 2
        row["evidence"]["max_return_anchor"] = (datetime.fromisoformat(row["move_start"]) + timedelta(minutes=30)).isoformat()
        result = run([row], optimized=i%2==0)
        if result.returncode == 0:
            raise AssertionError(f"invalid grouped anchor accepted: {i}")
    for i in range(100):
        row = episode(i)
        mode = i % 4
        if mode == 0: row["baseline_price"] = True
        elif mode == 1: row["evidence"]["max_return_baseline_price"] = True
        elif mode == 2: row["max_return_pct"] = True
        else: row["evidence"]["windows"] = True
        result = run([row], optimized=i%2==0)
        if result.returncode == 0:
            raise AssertionError(f"boolean numeric field accepted: {i}")
    print("PASS 100 valid and 400 corrupted artifact scenarios")

