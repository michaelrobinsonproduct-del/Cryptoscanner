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
