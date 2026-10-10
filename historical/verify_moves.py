"""Reject mislabeled or internally inconsistent historical episodes before artifact upload."""
import json
import math
from datetime import datetime, timezone
from pathlib import Path

path = Path("historical/output/moves.ndjson")
summary = json.loads(Path("historical/output/summary.json").read_text())
count = 0
seen = set()
for line_number, line in enumerate(path.open(encoding="utf-8"), 1):
    if not line.strip():
        raise ValueError(f"blank move episode at {line_number}")
    row = json.loads(line)
    evidence = row.get("evidence") or {}
    if evidence.get("retrospective_label_only") is not True:
        raise ValueError(f"unmarked retrospective episode at {line_number}")
    if evidence.get("live_alert_verified") is not False:
        raise ValueError(f"unverified episode claims live verification at {line_number}")
    if row.get("caught_early") is not False or row.get("earliest_signal_at") is not None:
        raise ValueError(f"historical episode claims live early catch at {line_number}")
    if evidence.get("max_anchor_gap_minutes") != 15:
        raise ValueError(f"unexpected episode grouping policy at {line_number}")
    if not isinstance(row.get("pair"), str) or not row["pair"].strip():
        raise ValueError(f"missing market pair at {line_number}")
    start = datetime.fromisoformat(row["move_start"].replace("Z", "+00:00"))
    peak_anchor = datetime.fromisoformat(evidence["max_return_anchor"].replace("Z", "+00:00"))
    if start.tzinfo is None or peak_anchor.tzinfo is None:
        raise ValueError(f"naive episode time at {line_number}")
    start = start.astimezone(timezone.utc)
    peak_anchor = peak_anchor.astimezone(timezone.utc)
    if not (datetime(2025, 10, 4, tzinfo=timezone.utc) <= start <= peak_anchor < datetime(2026, 7, 1, tzinfo=timezone.utc)):
        raise ValueError(f"invalid episode date at {line_number}")
    if (start.minute % 15 or peak_anchor.minute % 15 or start.second or peak_anchor.second):
        raise ValueError(f"episode anchor misaligned at {line_number}")
    for value in (row.get("baseline_price"), evidence.get("max_return_baseline_price")):
        if not isinstance(value, (int, float)) or not math.isfinite(value) or value <= 0:
            raise ValueError(f"invalid episode baseline at {line_number}")
    ret = row.get("max_return_pct")
    if not isinstance(ret, (int, float)) or not math.isfinite(ret) or ret < 20:
        raise ValueError(f"invalid major mover return at {line_number}")
    if not isinstance(evidence.get("windows"), int) or evidence["windows"] < 1:
        raise ValueError(f"invalid episode window count at {line_number}")
    key = (row["pair"], start)
    if key in seen:
        raise ValueError(f"duplicate episode key at {line_number}")
    seen.add(key)
    count += 1
if count != summary["move_episodes"]:
    raise ValueError(f"episode count mismatch: {count} vs {summary['move_episodes']}")
if count == 0:
    raise ValueError("empty episode artifact")
print(json.dumps({"episodes_verified": count, "retrospective_live_catches": 0, "ok": True}))
