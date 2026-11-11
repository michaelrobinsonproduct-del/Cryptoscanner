"""Operator-only SQLite backup to an independent filesystem; never auto-invoked."""
import argparse
import json
import shutil
import sqlite3
import tempfile
from contextlib import closing
from pathlib import Path
from .storage_safety import inventory

def _device(path):
    return Path(path).stat().st_dev

def export_verified(source, destination):
    source, destination = Path(source), Path(destination)
    if not source.is_file():
        raise FileNotFoundError(source)
    if not destination.parent.is_dir():
        raise FileNotFoundError(destination.parent)
    if destination.exists() or destination.is_symlink():
        raise FileExistsError('backup destination already exists')
    if source.resolve() == destination.resolve():
        raise ValueError('backup must differ from source')
    if _device(source) == _device(destination.parent):
        raise RuntimeError('backup destination must be on an independent filesystem')
    size = source.stat().st_size
    free = shutil.disk_usage(destination.parent).free
    if free < max(size * 2, 16 * 1024 * 1024):
        raise RuntimeError('insufficient destination headroom')
    before = inventory(source)
    with closing(sqlite3.connect(source.resolve().as_uri() + '?mode=ro', uri=True)) as src:
        try:
            with closing(sqlite3.connect(destination)) as out:
                src.backup(out)
            after = inventory(destination)
            if after != before:
                raise RuntimeError('backup parity mismatch')
            with tempfile.TemporaryDirectory(prefix='sqlite-restore-', dir=destination.parent) as tmp:
                restored = Path(tmp) / 'restore.sqlite3'
                shutil.copy2(destination, restored)
                if inventory(restored) != before:
                    raise RuntimeError('restore parity mismatch')
        except BaseException:
            destination.unlink(missing_ok=True)
            raise
    return {'status': 'VERIFIED', 'source_bytes': size, 'backup_bytes': destination.stat().st_size,
            'destination_free_bytes_before': free, 'tables': before,
            'independent_filesystem': True, 'source_data_modified': False}

def main():
    p = argparse.ArgumentParser(description='Explicit offline external SQLite backup; never invoked automatically')
    p.add_argument('source')
    p.add_argument('destination')
    a = p.parse_args()
    print(json.dumps(export_verified(a.source, a.destination), sort_keys=True))

if __name__ == '__main__':
    main()
