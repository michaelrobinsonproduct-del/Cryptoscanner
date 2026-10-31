import tempfile
import unittest
import zipfile
from pathlib import Path
from run_consolidated_historical_e2e import discover_schema, analyze, candidate_trade_member, run


class ConsolidatedEndToEndTests(unittest.TestCase):
    def archives(self, root, trade_text, ohlc_text="300,100,101,100,101,5,2\n"):
        t, o = root/"trades.zip", root/"ohlc.zip"
        with zipfile.ZipFile(t,"w") as z: z.writestr("0GEUR.csv",trade_text)
        with zipfile.ZipFile(o,"w") as z: z.writestr("0GEUR_5.csv",ohlc_text)
        return t, o

    def test_schema_is_observed_not_assumed(self):
        with tempfile.TemporaryDirectory() as d:
            t,o=self.archives(Path(d),"300,100,2\n301,101,3\n302,102,4\n")
            with zipfile.ZipFile(t) as z:
                s=discover_schema(z,"0GEUR.csv")
                self.assertEqual(s["columns"],[3,3,3])

    def test_non_three_column_schema_abstains(self):
        with tempfile.TemporaryDirectory() as d:
            t,o=self.archives(Path(d),"300,100,2,extra\n301,101,3,extra\n302,102,4,extra\n")
            with zipfile.ZipFile(t) as tz, zipfile.ZipFile(o) as oz:
                r=analyze(oz,tz)
                self.assertEqual(r["status"],"abstain_unknown_trade_csv_schema")
                self.assertEqual(r["real_labels"],0)

    def test_candidate_match_cannot_claim_real_labels(self):
        with tempfile.TemporaryDirectory() as d:
            t,o=self.archives(Path(d),"1770000300,100,2\n1770000301,101,3\n1770000302,102,4\n",
                              "1770000300,100,102,100,102,9,3\n")
            with zipfile.ZipFile(t) as tz, zipfile.ZipFile(o) as oz:
                r=analyze(oz,tz)
                self.assertEqual(r["candidate_overlapping_candles"],1)
                self.assertEqual(r["real_labels"],0)

    def test_missing_pair_fails_closed(self):
        with tempfile.TemporaryDirectory() as d:
            t,o=self.archives(Path(d),"300,100,2\n")
            with zipfile.ZipFile(t) as tz:
                with self.assertRaises(RuntimeError):
                    candidate_trade_member(tz,"XBTUSD")

    def test_output_never_overwrites(self):
        with tempfile.TemporaryDirectory() as d:
            p=Path(d)/"report.json"
            p.write_text("keep")
            with self.assertRaises(FileExistsError): run(p)
            self.assertEqual(p.read_text(),"keep")


if __name__ == "__main__":
    unittest.main()
