"""Offline SQLite backup/restore verification. Does not clean or modify the source."""
import argparse
from contextlib import closing
import hashlib
import json
import shutil
import sqlite3
import tempfile
from pathlib import Path

def inventory(db):
    db = Path(db)
    if not db.is_file():
        raise FileNotFoundError(db)
    con = sqlite3.connect(db.resolve().as_uri() + '?mode=ro', uri=True)
    try:
        if con.execute('PRAGMA integrity_check').fetchone()[0] != 'ok':
            raise RuntimeError('source integrity failed')
        tables = [r[0] for r in con.execute("SELECT name FROM sqlite_master WHERE type='table' AND name NOT LIKE 'sqlite_%' ORDER BY name")]
        result = {}
        for table in tables:
            ident = '"' + table.replace('"', '""') + '"'
            digest = hashlib.sha256()
            count = 0
            for row in con.execute('SELECT * FROM ' + ident + ' ORDER BY rowid'):
                digest.update(json.dumps(row, ensure_ascii=False, separators=(',', ':'), default=str).encode())
                digest.update(b'\n')
                count += 1
            result[table] = {'rows': count, 'sha256': digest.hexdigest()}
        return result
    finally:
        con.close()

def verify_copy(db, destination):
    db, destination = Path(db), Path(destination)
    if db.resolve() == destination.resolve():
        raise ValueError('destination must differ from source')
    if destination.exists():
        raise FileExistsError('refusing to overwrite existing backup')
    if not destination.parent.is_dir():
        raise FileNotFoundError(destination.parent)
    source_size = db.stat().st_size
    free = shutil.disk_usage(destination.parent).free
    if free < max(source_size * 2, 16 * 1024 * 1024):
        raise RuntimeError('insufficient backup disk headroom')
    before = inventory(db)
    source = sqlite3.connect(db.resolve().as_uri() + '?mode=ro', uri=True)
    try:
        with closing(sqlite3.connect(destination)) as target:
            source.backup(target)
    except BaseException:
        destination.unlink(missing_ok=True)
        raise
    finally:
        source.close()
    after = inventory(destination)
    if before != after:
        raise RuntimeError('backup row/hash parity failed')
    with tempfile.TemporaryDirectory(prefix='sqlite-restore-', dir=destination.parent) as tmp:
        restored = Path(tmp) / 'restored.sqlite3'
        shutil.copy2(destination, restored)
        if inventory(restored) != before:
            raise RuntimeError('restore verification failed')
    return {'status': 'VERIFIED', 'source_bytes': source_size, 'backup_bytes': destination.stat().st_size,
            'free_bytes_before': free, 'tables': before, 'live_database_modified': False}

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('source')
    parser.add_argument('backup')
    args = parser.parse_args()
    print(json.dumps(verify_copy(args.source, args.backup), sort_keys=True))

if __name__ == '__main__':
    main()
