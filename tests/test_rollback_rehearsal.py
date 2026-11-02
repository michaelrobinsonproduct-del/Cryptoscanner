"""Isolated rollback rehearsal: fixture DB only, no live storage or deployment."""
import sqlite3
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch
from simple_scanner.external_backup import export_verified
from simple_scanner.storage_safety import inventory

class RollbackRehearsalTests(unittest.TestCase):
    def test_fixture_backup_restore_preserves_original_and_data(self):
        with tempfile.TemporaryDirectory() as root:
            base=Path(root)
            srcdir=base/'source'; dst=base/'independent'; srcdir.mkdir(); dst.mkdir()
            source=srcdir/'history.sqlite3'; backup=dst/'backup.sqlite3'
            with sqlite3.connect(source) as con:
                con.execute('CREATE TABLE events (run_at TEXT, pair TEXT, value BLOB)')
                con.executemany('INSERT INTO events VALUES(?,?,?)',
                                [('t1','BTC',b'original'),('t2','ETH',b'\\x00\\xff')])
            original=inventory(source)
            with patch('simple_scanner.external_backup._device',
                       side_effect=lambda p: 2 if p == dst else 1):
                receipt=export_verified(source,backup)
            self.assertEqual(receipt['status'],'VERIFIED')
            self.assertTrue(receipt['independent_filesystem'])
            self.assertFalse(receipt['source_data_modified'])
            restored=base/'restored.sqlite3'
            restored.write_bytes(backup.read_bytes())
            self.assertEqual(inventory(restored),original)
            self.assertEqual(inventory(source),original)
            with sqlite3.connect(restored) as con:
                con.execute('INSERT INTO events VALUES(?,?,?)',('t3','SOL',b'rollback-test'))
            self.assertNotEqual(inventory(restored),original)
            self.assertEqual(inventory(source),original)
            self.assertEqual(inventory(backup),original)

    def test_failed_restore_detection_cannot_mutate_source(self):
        with tempfile.TemporaryDirectory() as root:
            source=Path(root)/'source.sqlite3'
            with sqlite3.connect(source) as con:
                con.execute('CREATE TABLE history (value INTEGER)')
                con.execute('INSERT INTO history VALUES(7)')
            before=inventory(source)
            corrupted=Path(root)/'corrupt.sqlite3'
            corrupted.write_bytes(b'not sqlite')
            with self.assertRaises(sqlite3.DatabaseError):
                inventory(corrupted)
            self.assertEqual(inventory(source),before)

if __name__=='__main__':
    unittest.main()
