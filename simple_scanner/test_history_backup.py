"""Offline backup safety tests; never touch production storage."""
import sqlite3
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch
import os
from simple_scanner.history_backup import backup

class HistoryBackupTests(unittest.TestCase):
    def test_consistent_backup_and_integrity(self):
        with tempfile.TemporaryDirectory() as root:
            source_dir = Path(root)/"source"
            target_dir = Path(root)/"target"
            source_dir.mkdir()
            target_dir.mkdir()
            src = source_dir/"history.sqlite3"
            dst = target_dir/"copy.sqlite3"
            with sqlite3.connect(src) as con:
                con.execute("CREATE TABLE observations (pair TEXT, price REAL)")
                con.execute("INSERT INTO observations VALUES ('SOLUSD', 101)")
            original_stat = os.stat
            def separate_devices(path, *args, **kwargs):
                result = original_stat(path, *args, **kwargs)
                if str(path) == str(target_dir):
                    class DeviceOverride:
                        st_dev = result.st_dev + 1
                        def __getattr__(self, key):
                            return getattr(result, key)
                    return DeviceOverride()
                return result
            with patch('simple_scanner.history_backup.os.stat', side_effect=separate_devices):
                self.assertEqual(backup(src, dst), dst)
            with sqlite3.connect(dst) as con:
                self.assertEqual(con.execute("SELECT * FROM observations").fetchall(), [("SOLUSD", 101.0)])
            with patch('simple_scanner.history_backup.os.stat', side_effect=separate_devices):
                with self.assertRaises(FileExistsError):
                    backup(src, dst)
            with sqlite3.connect(src) as con:
                self.assertEqual(con.execute("SELECT COUNT(*) FROM observations").fetchone()[0], 1)

    def test_refuses_same_filesystem_even_when_directories_differ(self):
        with tempfile.TemporaryDirectory() as root:
            source_dir = Path(root)/"source"
            target_dir = Path(root)/"target"
            source_dir.mkdir()
            target_dir.mkdir()
            src = source_dir/"history.sqlite3"
            with sqlite3.connect(src) as con:
                con.execute("CREATE TABLE t(x)")
            with self.assertRaisesRegex(ValueError, "separate filesystem"):
                backup(src, target_dir/"copy.sqlite3")
            self.assertFalse((target_dir/"copy.sqlite3").exists())

    def test_refuses_source_directory(self):
        with tempfile.TemporaryDirectory() as root:
            src = Path(root)/"history.sqlite3"
            with sqlite3.connect(src) as con:
                con.execute("CREATE TABLE t(x)")
            with self.assertRaises(ValueError):
                backup(src, Path(root)/"copy.sqlite3")

if __name__ == "__main__":
    unittest.main()
