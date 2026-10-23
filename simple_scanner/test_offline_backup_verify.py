import sqlite3
import tempfile
import unittest
from pathlib import Path
from simple_scanner.offline_backup_verify import backup_and_verify

class OfflineBackupTests(unittest.TestCase):
    def test_round_trip_and_no_overwrite(self):
        with tempfile.TemporaryDirectory() as tmp:
            a, b, c = [Path(tmp)/x for x in ("source.db", "backup.db", "restore.db")]
            with sqlite3.connect(a) as db:
                db.execute("CREATE TABLE samples(id INTEGER PRIMARY KEY, value TEXT)")
                db.execute("INSERT INTO samples(value) VALUES ('test')")
            result = backup_and_verify(a, b, c)
            self.assertTrue(result["verified"])
            with sqlite3.connect(c) as db:
                self.assertEqual(db.execute("SELECT value FROM samples").fetchone()[0], "test")
            with self.assertRaises(FileExistsError):
                backup_and_verify(a, b, c)
    def test_rejects_source_overwrite(self):
        with tempfile.TemporaryDirectory() as tmp:
            a, b = Path(tmp)/"source.db", Path(tmp)/"restore.db"
            with sqlite3.connect(a) as db:
                db.execute("CREATE TABLE t(x)")
            with self.assertRaises(ValueError):
                backup_and_verify(a, a, b)

if __name__ == "__main__":
    unittest.main()
