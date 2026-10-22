"""Read-only SQLite integrity and deterministic historical row inventory."""
import hashlib
import json
import sqlite3
from pathlib import Path

def inventory(db):
    db = Path(db)
    if not db.is_file():
        raise FileNotFoundError(db)
    with sqlite3.connect(db.resolve().as_uri() + '?mode=ro', uri=True) as con:
        checks = [r[0] for r in con.execute('PRAGMA integrity_check')]
        if checks != ['ok']:
            raise RuntimeError('SQLite integrity failed: ' + repr(checks[:3]))
        schema = [tuple(r) for r in con.execute(
            "SELECT type,name,tbl_name,sql FROM sqlite_master "
            "WHERE name NOT LIKE 'sqlite_%' ORDER BY type,name,tbl_name")]
        result = {}
        for (table,) in con.execute(
            "SELECT name FROM sqlite_master WHERE type='table' AND name NOT LIKE 'sqlite_%' ORDER BY name"):
            ident = '"' + table.replace('"', '""') + '"'
            # Sort canonical serialized rows, so WITHOUT ROWID tables and differing
            # physical insertion order produce the same content fingerprint.
            hashes = []
            for row in con.execute('SELECT * FROM ' + ident):
                values = [{'blob': v.hex()} if isinstance(v, bytes) else v for v in row]
                encoded = json.dumps(values, ensure_ascii=False, separators=(',', ':'), allow_nan=False)
                hashes.append(hashlib.sha256(encoded.encode('utf-8')).digest())
            digest = hashlib.sha256(b''.join(sorted(hashes))).hexdigest()
            result[table] = {'rows': len(hashes), 'sha256': digest}
        result['__schema_sha256__'] = hashlib.sha256(
            json.dumps(schema, ensure_ascii=False, separators=(',', ':')).encode('utf-8')).hexdigest()
        return result

def verify_copy(db, destination):
    """Offline fixture backup with restore verification; not a production exporter."""
    import shutil
    import tempfile
    from contextlib import closing
    source, destination = Path(db), Path(destination)
    if source.resolve() == destination.resolve():
        raise ValueError('destination must differ from source')
    if destination.exists() or destination.is_symlink():
        raise FileExistsError('refusing to overwrite existing backup')
    if not destination.parent.is_dir():
        raise FileNotFoundError(destination.parent)
    source_size = source.stat().st_size
    free = shutil.disk_usage(destination.parent).free
    if free < max(source_size * 2, 16 * 1024 * 1024):
        raise RuntimeError('insufficient backup disk headroom')
    before = inventory(source)
    try:
        with closing(sqlite3.connect(source.resolve().as_uri() + '?mode=ro', uri=True)) as src:
            with closing(sqlite3.connect(destination)) as dst:
                src.backup(dst)
        if inventory(destination) != before:
            raise RuntimeError('backup row/hash parity failed')
        with tempfile.TemporaryDirectory(prefix='sqlite-restore-', dir=destination.parent) as tmp:
            restored = Path(tmp) / 'restored.sqlite3'
            shutil.copy2(destination, restored)
            if inventory(restored) != before:
                raise RuntimeError('restore verification failed')
    except BaseException:
        destination.unlink(missing_ok=True)
        raise
    return {'status': 'VERIFIED', 'source_bytes': source_size,
            'backup_bytes': destination.stat().st_size,
            'free_bytes_before': free, 'tables': before, 'live_database_modified': False}

def main():
    import argparse
    p = argparse.ArgumentParser()
    p.add_argument('source')
    p.add_argument('backup')
    args = p.parse_args()
    print(json.dumps(verify_copy(args.source, args.backup), sort_keys=True))

if __name__ == '__main__':
    main()
