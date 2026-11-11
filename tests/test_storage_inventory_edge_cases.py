import sqlite3
import tempfile
import unittest
from pathlib import Path
from simple_scanner.storage_safety import inventory, verify_copy

class InventoryEdgeCases(unittest.TestCase):
    def test_without_rowid_blob_and_schema_parity(self):
        with tempfile.TemporaryDirectory() as folder:
            source = Path(folder) / 'source.sqlite3'
            dest = Path(folder) / 'backup.sqlite3'
            with sqlite3.connect(source) as con:
                con.execute('CREATE TABLE items(k TEXT PRIMARY KEY, payload BLOB) WITHOUT ROWID')
                con.execute('CREATE INDEX items_payload ON items(payload)')
                con.execute('INSERT INTO items VALUES(?,?)', ('a', bytes([0, 255, 12])))
                con.execute('INSERT INTO items VALUES(?,?)', ('b', bytes([1, 2, 3])))
                con.commit()
            result = verify_copy(source, dest)
            self.assertEqual(result['status'], 'VERIFIED')
            self.assertEqual(inventory(source), inventory(dest))
            self.assertEqual(inventory(source)['items']['rows'], 2)

    def test_schema_change_detected_without_row_changes(self):
        with tempfile.TemporaryDirectory() as folder:
            a, b = Path(folder)/'a.sqlite3', Path(folder)/'b.sqlite3'
            for db in (a,b):
                with sqlite3.connect(db) as con:
                    con.execute('CREATE TABLE data(k TEXT)')
                    con.execute("INSERT INTO data VALUES('same')")
                    con.commit()
            with sqlite3.connect(b) as con:
                con.execute('CREATE INDEX idx_data ON data(k)')
                con.commit()
            self.assertNotEqual(inventory(a), inventory(b))

if __name__ == '__main__':
    unittest.main()
