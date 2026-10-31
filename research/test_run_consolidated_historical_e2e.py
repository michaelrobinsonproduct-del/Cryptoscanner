import tempfile
import unittest
import zipfile
from pathlib import Path
from run_consolidated_historical_e2e import discover_schema, analyze, candidate_trade_member, run, reconstruct_verified_outcomes


class ConsolidatedEndToEndTests(unittest.TestCase):
    def archives(self, root, trade_text, ohlc_text="300,100,101,100,101,5,2\n"):
        t, o = root/"trades.zip", root/"ohlc.zip"
        with zipfile.ZipFile(t,"w") as z: z.writestr("0GEUR.csv",trade_text)
        with zipfile.ZipFile(o,"w") as z: z.writestr("0GEUR_5.csv",ohlc_text)
        return t, o

    def test_schema_is_observed_not_assumed(self):
        with tempfile.TemporaryDirectory() as d:
            t,o=self.archives(Path(d),"timestamp,price,volume,type,order_type,misc,trade_id\n300,100,2,b,l,,a\n301,101,3,s,m,,b\n302,102,4,b,l,,c\n")
            with zipfile.ZipFile(t) as z:
                s=discover_schema(z,"0GEUR.csv")
                self.assertEqual(s["columns"],[7,7,7])
                self.assertTrue(s["official_header_match"])

    def test_non_three_column_schema_abstains(self):
        with tempfile.TemporaryDirectory() as d:
            t,o=self.archives(Path(d),"timestamp,price,volume,other\n300,100,2,extra\n301,101,3,extra\n")
            with zipfile.ZipFile(t) as tz, zipfile.ZipFile(o) as oz:
                r=analyze(oz,tz)
                self.assertEqual(r["status"],"abstain_unknown_trade_csv_schema")
                self.assertEqual(r["real_labels"],0)

    def test_candidate_match_cannot_claim_real_labels(self):
        with tempfile.TemporaryDirectory() as d:
            t,o=self.archives(Path(d),"timestamp,price,volume,type,order_type,misc,trade_id\n1770000300,100,2,b,l,,a\n1770000301,101,3,s,m,,b\n1770000302,102,4,b,l,,c\n",
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

    def test_no_real_labels_without_independent_source(self):
        rows = [(300, 100, 101, 100, 101, 5, 2)]
        trades = [(300, 100, 2, 0), (301, 101, 3, 1)]
        self.assertEqual(reconstruct_verified_outcomes(rows, trades)["real_labels"], 0)

    def test_no_real_labels_without_timestamp_semantics(self):
        rows = [(300, 100, 101, 100, 101, 5, 2)]
        trades = [(300, 100, 2, 0), (301, 101, 3, 1)]
        r = reconstruct_verified_outcomes(rows, trades, source_complete=True)
        self.assertEqual(r["status"], "abstain_unverified_independent_source")

    def test_exact_matching_does_not_create_immature_labels(self):
        rows = [(300, 100, 101, 100, 101, 5, 2)]
        trades = [(300, 100, 2, 0), (301, 101, 3, 1)]
        r = reconstruct_verified_outcomes(rows, trades, source_complete=True,
                                          trade_timestamp_semantics_verified=True)
        self.assertEqual(r["real_labels"], 0)

    def test_output_never_overwrites(self):
        with tempfile.TemporaryDirectory() as d:
            p=Path(d)/"report.json"
            p.write_text("keep")
            with self.assertRaises(FileExistsError): run(p)
            self.assertEqual(p.read_text(),"keep")


if __name__ == "__main__":
    unittest.main()
