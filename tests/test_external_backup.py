import sqlite3
import tempfile
import unittest
from contextlib import closing
from pathlib import Path
from unittest.mock import patch
from simple_scanner.external_backup import export_verified
from simple_scanner.storage_safety import inventory

class ExternalBackupTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        root = Path(self.temp.name)
        self.src_dir = root / 'src'
        self.dest_dir = root / 'dest'
        self.src_dir.mkdir()
        self.dest_dir.mkdir()
        self.source = self.src_dir / 'history.sqlite3'
        self.destination = self.dest_dir / 'backup.sqlite3'
        with closing(sqlite3.connect(self.source)) as db:
            db.execute('CREATE TABLE snapshots (run_at TEXT, pair TEXT, price REAL)')
            db.execute('CREATE TABLE outcomes (run_at TEXT, pair TEXT, return_pct REAL)')
            db.executemany('INSERT INTO snapshots VALUES(?,?,?)', [('t1','BTC',1.0),('t2','ETH',2.0)])
            db.execute('INSERT INTO outcomes VALUES(?,?,?)', ('t1','BTC',20.0))
            db.commit()

    def test_same_device_rejected(self):
        with self.assertRaisesRegex(RuntimeError, 'independent filesystem'):
            export_verified(self.source, self.destination)
        self.assertFalse(self.destination.exists())

    def test_backup_and_restore_parity(self):
        original = self.source.read_bytes()
        with patch('simple_scanner.external_backup._device', side_effect=lambda p: 2 if p == self.dest_dir else 1):
            result = export_verified(self.source, self.destination)
        self.assertEqual(result['status'], 'VERIFIED')
        self.assertEqual(result['tables']['snapshots']['rows'], 2)
        self.assertEqual(inventory(self.source), inventory(self.destination))
        self.assertEqual(self.source.read_bytes(), original)

    def test_refuse_overwrite(self):
        self.destination.write_bytes(b'preserve')
        with self.assertRaises(FileExistsError):
            export_verified(self.source, self.destination)
        self.assertEqual(self.destination.read_bytes(), b'preserve')

    def test_headroom_rejected(self):
        with patch('simple_scanner.external_backup._device', side_effect=lambda p: 2 if p == self.dest_dir else 1), patch('simple_scanner.external_backup.shutil.disk_usage') as usage:
            usage.return_value = type('D', (), {'free': 1})()
            with self.assertRaisesRegex(RuntimeError, 'headroom'):
                export_verified(self.source, self.destination)
        self.assertFalse(self.destination.exists())

    def test_corrupt_source_rejected(self):
        self.source.write_bytes(b'bad sqlite')
        with patch('simple_scanner.external_backup._device', side_effect=lambda p: 2 if p == self.dest_dir else 1):
            with self.assertRaises(sqlite3.DatabaseError):
                export_verified(self.source, self.destination)
        self.assertFalse(self.destination.exists())
