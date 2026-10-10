"""Missed breakout analysis must not count overlapping scans or hindsight wins."""
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch


class MissReportTests(unittest.TestCase):
    def test_later_same_day_winner_does_not_count_as_early_miss(self):
        import history
        with tempfile.TemporaryDirectory() as folder:
            with patch.object(history,"DB",Path(folder)/"history.sqlite3"):
                with history.connect() as con:
                    for day in (1,2):
                        for hour,ret in ((0,0.0),(1,18.0),(2,22.0)):
                            created=f"2026-09-{day:02d}T{hour:02d}:00:00+00:00"
                            rid=f"{created}-TEST"
                            con.execute("INSERT INTO runs VALUES (?,?,?,?)",(rid,created,"COMPLETE","{}"))
                            con.execute("INSERT INTO observations VALUES (?,?,?,?,?)",(rid,"TESTUSD",1.0,30.0,"NOT_SELECTED"))
                            con.execute("INSERT INTO outcomes VALUES (?,?,?,?,?)",(rid,"TESTUSD",4,ret,created))
                    created="2026-09-03T00:00:00+00:00"
                    con.execute("INSERT INTO runs VALUES (?,?,?,?)",(created,created,"COMPLETE","{}"))
                    con.execute("INSERT INTO observations VALUES (?,?,?,?,?)",(created,"TESTUSD",1.0,30.0,"NOT_SELECTED"))
                    con.execute("INSERT INTO outcomes VALUES (?,?,?,?,?)",(created,"TESTUSD",4,8.0,created))
                misses=history.miss_report()
                self.assertEqual(misses,[{"pair":"TESTUSD","missed_breakouts":1,"best_return_pct":8.0}])


if __name__=="__main__":
    unittest.main()
