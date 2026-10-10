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
                # A low-only cohort must not be promoted by later same-day gains.
                self.assertEqual(result["status"],"INSUFFICIENT_DATA")
                with history.connect() as con:
                    selected=con.execute("""WITH ranked AS (
                        SELECT substr(r.created_at,1,10) AS day,o.pair,o.score,
                               x.return_pct,
                               ROW_NUMBER() OVER (
                                   PARTITION BY substr(r.created_at,1,10),o.pair
                                   ORDER BY r.created_at ASC,r.id ASC
                               ) AS rn
                        FROM outcomes x
                        JOIN observations o ON o.run_id=x.run_id AND o.pair=x.pair
                        JOIN runs r ON r.id=o.run_id
                        WHERE x.horizon_hours=4
                    ) SELECT score,return_pct FROM ranked WHERE rn=1""").fetchall()
                self.assertEqual(len(selected),20)
                self.assertTrue(all(score==10 and ret==0 for score,ret in selected))


    def test_late_winners_cannot_create_false_validation(self):
        import history
        with tempfile.TemporaryDirectory() as folder:
            with patch.object(history, "DB", Path(folder) / "history.sqlite3"):
                with history.connect() as con:
                    for day in range(1, 11):
                        date=f"2026-09-{day:02d}"
                        for idx in range(20):
                            pair=f"COIN{idx:02d}USD"
                            high=idx<10
                            # Earliest high-score entries lose, low-score entries win.
                            # Later high-score entries win; selecting daily maxima
                            # would fabricate high-score predictive success.
                            for hour, score, hit in (
                                (0, 90 if high else 10, 0 if high else 1),
                                (1, 99 if high else 10, 1 if high else 0),
                            ):
                                rid=f"{date}T{hour:02d}:00:00+00:00-{pair}"
                                con.execute("INSERT INTO runs VALUES (?,?,?,?)",
                                            (rid,f"{date}T{hour:02d}:00:00+00:00","COMPLETE","{}"))
                                con.execute("INSERT INTO observations VALUES (?,?,?,?,?)",
                                            (rid,pair,1.0,score,"WATCH"))
                                con.execute("INSERT INTO outcomes VALUES (?,?,?,?,?)",
                                            (rid,pair,4,6.0 if hit else 0.0,rid))
                result=history.prospective_learning(min_days=10,min_pairs=8)
                self.assertEqual(result["pair_days"],200)
                self.assertEqual(result["status"],"NO_VALIDATED_IMPROVEMENT")
                self.assertFalse(result["validated"])
                self.assertEqual(result["adjustment"],0)
                self.assertEqual(result["train"]["HIGH"],0)
                self.assertEqual(result["train"]["LOW"],1)
                self.assertEqual(result["test"]["HIGH"],0)
                self.assertEqual(result["test"]["LOW"],1)


    def test_unlabeled_earliest_signal_not_replaced_by_later_win(self):
        import history
        with tempfile.TemporaryDirectory() as folder:
            with patch.object(history,"DB",Path(folder)/"history.sqlite3"):
                with history.connect() as con:
                    for hour in (0,1):
                        stamp=f"2026-09-01T{hour:02d}:00:00+00:00"
                        con.execute("INSERT INTO runs VALUES (?,?,?,?)",(stamp,stamp,"COMPLETE","{}"))
                        con.execute("INSERT INTO observations VALUES (?,?,?,?,?)",(stamp,"GAPUSD",1.0,99.0,"WATCH"))
                        if hour:
                            con.execute("INSERT INTO outcomes VALUES (?,?,?,?,?)",(stamp,"GAPUSD",4,30.0,stamp))
                result=history.prospective_learning()
                self.assertEqual(result["pair_days"],0)
                self.assertFalse(result["validated"])
                self.assertEqual(result["adjustment"],0)


if __name__=="__main__":
    unittest.main()
