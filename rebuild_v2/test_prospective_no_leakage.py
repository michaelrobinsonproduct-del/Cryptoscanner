"""Regression test: prospective validation must not select hindsight maxima."""
import sqlite3
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch


class ProspectiveNoLeakageTests(unittest.TestCase):
    def test_earliest_pair_day_observation_is_used(self):
        import history
        with tempfile.TemporaryDirectory() as folder:
            with patch.object(history, "DB", Path(folder) / "history.sqlite3"):
                with history.connect() as con:
                    for day in range(1, 11):
                        date=f"2026-09-{day:02d}"
                        for pair in ("AAAUSD", "BBBUSD"):
                            for hour, score, hit in ((0, 10, 0), (1, 99, 1)):
                                rid=f"{date}T{hour:02d}:00:00+00:00-{pair}"
                                con.execute("INSERT INTO runs VALUES (?,?,?,?)",
                                            (rid,f"{date}T{hour:02d}:00:00+00:00","COMPLETE","{}"))
                                con.execute("INSERT INTO observations VALUES (?,?,?,?,?)",
                                            (rid,pair,1.0,score,"WATCH"))
                                con.execute("INSERT INTO outcomes VALUES (?,?,?,?,?)",
                                            (rid,pair,4,6.0 if hit else 0.0,rid))
                result=history.prospective_learning(min_days=10,min_pairs=2)
                self.assertEqual(result["pair_days"],20)
                self.assertEqual(result["days"],10)
                self.assertFalse(result["validated"])
                self.assertEqual(result["adjustment"],0)
                # Old MAX(score)/MAX(hit) logic would select 99 and a win.
                self.assertEqual(result["status"],"INSUFFICIENT_DATA")


if __name__=="__main__":
    unittest.main()
