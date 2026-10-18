"""Operator-invoked SQLite online backup. Never runs from scanner or CI.

Reads production SQLite through the SQLite backup API, which obtains a
consistent snapshot without creating a second database writer. Requires
operator-controlled destination outside the mounted production volume.
"""
import argparse
import os
from pathlib import Path
import sqlite3
import sys

def backup(source, destination):
    source, destination = Path(source).resolve(), Path(destination).resolve()
    if not source.is_file() or not source.stat().st_size:
        raise ValueError("Source history database missing or empty")
    if source == destination or source.parent == destination.parent:
        raise ValueError("Backup destination must be outside source directory")
    if destination.exists():
        raise FileExistsError("Never overwrite an existing backup")
    if not destination.parent.is_dir():
        raise ValueError("Destination parent directory must exist")
    if os.statvfs(destination.parent).f_bavail * os.statvfs(destination.parent).f_frsize < source.stat().st_size * 2:
        raise OSError("Insufficient destination free space")
    # Immutable mode is unsafe for live WAL databases; use normal read-only
    # SQLite connection so the backup API sees committed transactions.
    uri = source.as_uri() + "?mode=ro"
    try:
        with sqlite3.connect(uri, uri=True, timeout=10) as src:
            with sqlite3.connect(destination, timeout=10) as dst:
                src.backup(dst, pages=256, sleep=0.05)
                if dst.execute("PRAGMA integrity_check").fetchone()[0] != "ok":
                    raise RuntimeError("Backup integrity check failed")
    except Exception:
        destination.unlink(missing_ok=True)
        raise
    return destination

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--source", required=True)
    parser.add_argument("--destination", required=True)
    args = parser.parse_args()
    print("BACKUP_VERIFIED " + str(backup(args.source, args.destination)))

if __name__ == "__main__":
    main()
