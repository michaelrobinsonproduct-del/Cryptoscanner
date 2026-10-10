"""Prospective benchmark regression: no duplicate scan inflation or premature promotion."""
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch


class EarlyDetectionBenchmarkTests(unittest.TestCase):
    def test_first_labeled_pair_day_and_no_promotion(self):
        import history
        with tempfile.TemporaryDirectory() as folder:
            with patch.object(history,"DB",Path(folder)/"history.sqlite3"):
                with history.connect() as con:
                    for day in range(1,11):
                        for idx in range(6):
                            pair=f"P{idx}USD"
                            status="WATCH" if idx<3 else "NOT_SELECTED"
                            for hour in (0,1):
                                stamp=f"2026-09-{day:02d}T{hour:02d}:00:00+00:00"
                                rid=f"{stamp}-{pair}"
                                con.execute("INSERT INTO runs VALUES (?,?,?,?)",(rid,stamp,"COMPLETE","{}"))
                                con.execute("INSERT INTO observations VALUES (?,?,?,?,?)",(rid,pair,1.0,75.0,status))
                                # Later WATCH wins cannot retroactively improve earliest result.
                                ret=(9.0 if status=="WATCH" else 0.0) if hour else (0.0 if status=="WATCH" else 9.0)
                                con.execute("INSERT INTO outcomes VALUES (?,?,?,?,?)",(rid,pair,4,ret,stamp))
                result=history.early_detection_benchmark(min_pair_days=60)
                self.assertEqual(result["pair_days"],60)
                self.assertEqual(result["days"],10)
                self.assertEqual(result["status"],"DESCRIPTIVE_ONLY")
                self.assertEqual(result["watch"]["hit_rate"],0)
                self.assertEqual(result["baseline"]["hit_rate"],1)
                self.assertEqual(result["lift"],0)
                self.assertFalse(result["ranking_adjustment_allowed"])


if __name__=="__main__":
    unittest.main()
