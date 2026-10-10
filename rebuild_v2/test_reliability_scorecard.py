"""Coverage must count unique completed 15-minute cycles, never retries."""
import datetime as dt
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch


class CoverageTests(unittest.TestCase):
    def test_duplicate_runs_cannot_inflate_coverage(self):
        import history
        now=dt.datetime(2026,10,11,12,10,tzinfo=dt.timezone.utc)
        with tempfile.TemporaryDirectory() as folder:
            with patch.object(history,"DB",Path(folder)/"history.sqlite3"):
                with history.connect() as con:
                    for index in range(97):
                        stamp=now-dt.timedelta(minutes=15*(96-index))
                        cycle=stamp.replace(minute=(stamp.minute//15)*15,second=0,microsecond=0)
                        rid=f"run-{index}"
                        con.execute("INSERT INTO runs VALUES (?,?,?,?)",(rid,stamp.isoformat(),"COMPLETE","{}"))
                        con.execute("INSERT INTO scan_cycles VALUES (?,?,?)",(cycle.isoformat().replace("+00:00","Z"),rid,stamp.isoformat()))
                    # Extra successful run with no unique scheduled cycle.
                    con.execute("INSERT INTO runs VALUES (?,?,?,?)",("retry",now.isoformat(),"COMPLETE","{}"))
                report=history.reliability_scorecard(now)["24h"]
                self.assertEqual(report["status"],"MEASURED")
                self.assertEqual(report["observed_completed"],report["expected_scheduled"])
                self.assertEqual(report["coverage_pct"],100.0)
                with history.connect() as con:
                    con.execute("DELETE FROM scan_cycles WHERE cycle_id=?",
                                ("2026-10-11T11:45:00Z",))
                report=history.reliability_scorecard(now)["24h"]
                self.assertEqual(report["observed_completed"],report["expected_scheduled"]-1)
                self.assertLess(report["coverage_pct"],100)


if __name__=="__main__":
    unittest.main()
