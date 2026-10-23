import sqlite3
import tempfile
import unittest
from contextlib import closing
from pathlib import Path
from unittest.mock import patch
from simple_scanner.storage_safety import inventory, verify_copy

class StorageSafetyTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.folder = Path(self.temp.name)
        self.db = self.folder / 'history.sqlite3'
        with closing(sqlite3.connect(self.db)) as con:
            con.execute('CREATE TABLE snapshots(run_at TEXT, pair TEXT, price REAL)')
            con.execute('CREATE TABLE outcomes(run_at TEXT, pair TEXT, return_pct REAL)')
            con.executemany('INSERT INTO snapshots VALUES(?,?,?)', [('a','BTC/USD',1.1),('b','ETH/USD',2.2)])
            con.execute('INSERT INTO outcomes VALUES(?,?,?)', ('a','BTC/USD',12.5))
            con.commit()

    def test_backup_restore_and_history_parity(self):
        before = self.db.read_bytes()
        report = verify_copy(self.db, self.folder / 'copy.sqlite3')
        self.assertEqual(report['status'], 'VERIFIED')
        self.assertEqual(report['tables']['snapshots']['rows'], 2)
        self.assertEqual(report['tables']['outcomes']['rows'], 1)
        self.assertEqual(self.db.read_bytes(), before)

    def test_no_overwrite(self):
        (self.folder / 'existing.sqlite3').write_bytes(b'keep')
        with self.assertRaises(ValueError):
            verify_copy(self.db, self.db)
        with self.assertRaises(FileExistsError):
            verify_copy(self.db, self.folder / 'existing.sqlite3')

    def test_insufficient_headroom(self):
        from collections import namedtuple
        usage = namedtuple('usage', 'total used free')
        with patch('simple_scanner.storage_safety.shutil.disk_usage', return_value=usage(100, 99, 1)):
            with self.assertRaisesRegex(RuntimeError, 'headroom'):
                verify_copy(self.db, self.folder / 'copy.sqlite3')
        self.assertFalse((self.folder / 'copy.sqlite3').exists())

    def test_corrupt_source_rejected(self):
        self.db.write_bytes(b'not a database')
        with self.assertRaises(sqlite3.DatabaseError):
            inventory(self.db)

    def test_backup_tampering_detected(self):
        verify_copy(self.db, self.folder / 'copy.sqlite3')
        with closing(sqlite3.connect(self.folder / 'copy.sqlite3')) as con:
            con.execute("UPDATE outcomes SET return_pct=999")
            con.commit()
        self.assertNotEqual(inventory(self.db), inventory(self.folder / 'copy.sqlite3'))

if __name__ == '__main__':
    unittest.main()
