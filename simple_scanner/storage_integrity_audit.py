"""Read-only storage and learning integrity audit. Never mutates scanner data."""
import argparse
import json
import sqlite3
from pathlib import Path

def audit(path, *, max_bytes=None):
    path = Path(path)
    uri = "file:" + str(path.resolve()) + "?mode=ro"
    with sqlite3.connect(uri, uri=True) as con:
        integrity = con.execute("PRAGMA integrity_check").fetchone()[0]
        tables = {r[0] for r in con.execute("SELECT name FROM sqlite_master WHERE type='table'")}
        required = {"snapshots", "candidate_features", "outcomes", "market_observations", "market_signals"}
        if not required <= tables:
            raise AssertionError("Missing learning tables: " + repr(sorted(required-tables)))
        counts = {name: con.execute("SELECT COUNT(*) FROM " + name).fetchone()[0] for name in sorted(required)}
        unmatched = con.execute("""SELECT COUNT(*) FROM outcomes o
            LEFT JOIN snapshots s ON o.run_at=s.run_at AND o.pair=s.pair
            WHERE s.run_at IS NULL""").fetchone()[0]
        missing_features = con.execute("""SELECT COUNT(*) FROM snapshots s
            LEFT JOIN candidate_features f ON s.run_at=f.run_at AND s.pair=f.pair
            WHERE f.run_at IS NULL""").fetchone()[0]
        page_size = con.execute("PRAGMA page_size").fetchone()[0]
        pages = con.execute("PRAGMA page_count").fetchone()[0]
        freelist = con.execute("PRAGMA freelist_count").fetchone()[0]
    report = {
        "integrity": integrity, "counts": counts,
        "orphan_outcomes": unmatched, "snapshots_missing_features": missing_features,
        "db_bytes": path.stat().st_size,
        "page_bytes": page_size, "pages": pages, "free_pages": freelist,
        "reclaimable_inside_db_bytes": freelist * page_size,
        "max_bytes": max_bytes,
    }
    report["passed"] = (
        integrity == "ok" and unmatched == 0 and missing_features == 0
        and (max_bytes is None or report["db_bytes"] <= max_bytes)
    )
    return report

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("db")
    parser.add_argument("--max-bytes", type=int)
    args = parser.parse_args()
    result = audit(args.db, max_bytes=args.max_bytes)
    print(json.dumps(result, sort_keys=True))
    raise SystemExit(0 if result["passed"] else 1)
