"""Offline-only SQLite backup and restore verification. Never connects to production."""
import argparse
import hashlib
import json
import sqlite3
from pathlib import Path

def digest(path):
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()

def backup_and_verify(source, destination, restored):
    source, destination, restored = map(Path, (source, destination, restored))
    if len({p.resolve() for p in (source, destination, restored)}) != 3:
        raise ValueError("source, backup and restore paths must differ")
    if destination.exists() or restored.exists():
        raise FileExistsError("Refusing to overwrite an existing file")
    if not source.is_file():
        raise FileNotFoundError(source)
    # No production writer or remote storage action: caller must provide an
    # authorized off-volume destination and must run this outside production.
    try:
        with sqlite3.connect(f"file:{source.resolve()}?mode=ro", uri=True) as src:
            with sqlite3.connect(destination) as dst:
                src.backup(dst)
        with sqlite3.connect(f"file:{destination.resolve()}?mode=ro", uri=True) as src:
            with sqlite3.connect(restored) as dst:
                src.backup(dst)
        checks = {}
        for label, path in (("backup", destination), ("restored", restored)):
            with sqlite3.connect(f"file:{path.resolve()}?mode=ro", uri=True) as db:
                checks[label] = db.execute("PRAGMA integrity_check").fetchone()[0]
        result = {"backup_sha256": digest(destination), "restore_sha256": digest(restored),
                  "integrity": checks, "backup_bytes": destination.stat().st_size,
                  "verified": checks == {"backup": "ok", "restored": "ok"} and digest(destination) == digest(restored)}
        if not result["verified"]:
            raise AssertionError("Restore verification failed")
        return result
    except Exception:
        # Preserve artifacts for diagnosis; never delete or modify source.
        raise

if __name__ == "__main__":
    p = argparse.ArgumentParser(description="Offline SQLite backup+restore test; never use live production source")
    p.add_argument("source")
    p.add_argument("backup")
    p.add_argument("restore")
    a = p.parse_args()
    print(json.dumps(backup_and_verify(a.source, a.backup, a.restore), sort_keys=True))
