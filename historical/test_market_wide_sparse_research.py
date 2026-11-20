import unittest
from datetime import datetime,timedelta,timezone
import io
from historical.market_wide_sparse_research import read_valid_member,bracketed_high_labels


class SparseArchiveResearchTest(unittest.TestCase):
    def test_only_bracketed_windows_reclassified_and_strict_rows_immutable(self):
        start=datetime(2026,7,1,tzinfo=timezone.utc)
        a=dict(prediction_id="a",entry_utc=start.isoformat(),entry_price=100)
        outcomes=[dict(prediction_id="a",horizon_hours=h,coverage_complete=False,
                       outcome_status="MISSING_CANDLES",hit=None) for h in (1,6,24,48)]
        cohort=dict(anchors=[a],outcomes=outcomes)
        rows=[(start,100,100),(start+timedelta(minutes=30),100,135),
              (start+timedelta(hours=2),95,110)]
        result,counts=bracketed_high_labels(cohort,rows,archive_start=start.isoformat(),
                archive_end=(start+timedelta(days=10)).isoformat())
        self.assertTrue(result["outcomes"][0]["hit"])
        self.assertFalse(result["outcomes"][0]["strict_coverage_complete"])
        self.assertEqual(counts["1"]["no_trade_intervals"],11)
        self.assertIsNone(result["outcomes"][1]["hit"])
        self.assertIsNone(cohort["outcomes"][0]["hit"])
        rows[1]=(rows[1][0],100,105)
        result,_=bracketed_high_labels(cohort,rows,archive_start=start.isoformat(),
                archive_end=(start+timedelta(days=10)).isoformat())
        self.assertIs(result["outcomes"][0]["hit"],False)
        self.assertIsNone(result["outcomes"][0]["close_return"])

    def test_reject_malformed_zero_trade_and_duplicate_rows(self):
        row=b"1782864000,100,100,100,100,1,1\n"
        for data in (row+row,row+b"bad\n",row+b"1782864300,100,100,100,100,0,0\n"):
            with self.assertRaises(ValueError):
                read_valid_member(io.BytesIO(data),"TESTUSD")

if __name__=="__main__":
    unittest.main()
