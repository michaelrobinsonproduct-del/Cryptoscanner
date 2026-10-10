"""Regression tests for historical cycle idempotency and preservation."""
import importlib
import os
import sqlite3
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch


class CycleIdempotencyTests(unittest.TestCase):
    def test_duplicate_cycle_does_not_add_history_or_observations(self):
        import history
        with tempfile.TemporaryDirectory() as directory:
            with patch.object(history, "DB", Path(directory) / "history.sqlite3"):
                first = {
                    "started_at": "2026-10-10T16:45:01+00:00",
                    "completed_at": "2026-10-10T16:45:15+00:00",
                    "health": "COMPLETE",
                    "watch": [{"pair": "BTCUSD", "price": 100.0, "score": 5}],
                }
                second = {
                    **first,
                    "started_at": "2026-10-10T16:59:01+00:00",
                    "completed_at": "2026-10-10T16:59:15+00:00",
                    "watch": [{"pair": "ETHUSD", "price": 200.0, "score": 9}],
                }
                with patch.dict(os.environ, {"SCAN_CYCLE_ID": "2026-10-10T16:45:00Z"}):
                    history.store_run(first)
                    history.store_run(second)
                with sqlite3.connect(history.DB) as con:
                    self.assertEqual(con.execute("SELECT COUNT(*) FROM scan_cycles").fetchone()[0], 1)
                    self.assertEqual(con.execute("SELECT COUNT(*) FROM runs").fetchone()[0], 1)
                    self.assertEqual(con.execute("SELECT COUNT(*) FROM observations").fetchone()[0], 1)
                    self.assertEqual(con.execute("SELECT pair FROM observations").fetchone()[0], "BTCUSD")

    def test_distinct_cycles_both_persist(self):
        import history
        with tempfile.TemporaryDirectory() as directory:
            with patch.object(history, "DB", Path(directory) / "history.sqlite3"):
                for cycle, start in (
                    ("2026-10-10T16:45:00Z", "2026-10-10T16:45:01+00:00"),
                    ("2026-10-10T17:00:00Z", "2026-10-10T17:00:01+00:00"),
                ):
                    result = {"started_at": start, "completed_at": start, "health": "COMPLETE",
                              "watch": [{"pair": "BTCUSD", "price": 100.0, "score": 5}]}
                    with patch.dict(os.environ, {"SCAN_CYCLE_ID": cycle}):
                        history.store_run(result)
                with sqlite3.connect(history.DB) as con:
                    self.assertEqual(con.execute("SELECT COUNT(*) FROM scan_cycles").fetchone()[0], 2)
                    self.assertEqual(con.execute("SELECT COUNT(*) FROM runs").fetchone()[0], 2)


if __name__ == "__main__":
    unittest.main()
