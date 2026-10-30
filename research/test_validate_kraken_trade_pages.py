import unittest
from validate_kraken_trade_pages import validate_trade_pages


class TradePageEvidenceTests(unittest.TestCase):
    def setUp(self):
        self.pages = [{"cursor": "a", "trades": [(301, 100, 1, "t1")]},
                      {"requested_since": "a", "cursor": "b",
                       "trades": [(450, 120, 2, "t2"), (599, 110, 2, "t3")]}]
        self.kw = dict(start=300, end=600, complete_cursor_chain=True,
                       started_before_interval=True, ended_after_interval=True)

    def test_missing_completeness_attestation_abstains(self):
        self.assertEqual(validate_trade_pages(self.pages, start=300, end=600)["status"],
                         "unverified_complete_trade_interval")

    def test_valid_cursor_chain_is_candidate_not_proof(self):
        r = validate_trade_pages(self.pages, **self.kw)
        self.assertEqual(r["status"], "candidate_complete_trade_interval_requires_source_attestation")
        self.assertEqual(r["count"], 3)

    def test_broken_cursor_chain_rejected(self):
        self.pages[1]["requested_since"] = "wrong"
        self.assertEqual(validate_trade_pages(self.pages, **self.kw)["status"], "broken_cursor_chain")

    def test_duplicate_trade_id_rejected(self):
        self.pages[1]["trades"][0] = (450, 120, 2, "t1")
        self.assertEqual(validate_trade_pages(self.pages, **self.kw)["status"], "duplicate_or_invalid_trade_id")

    def test_unaligned_interval_rejected(self):
        self.assertEqual(validate_trade_pages(self.pages, **dict(self.kw, start=301))["status"], "invalid_interval")

    def test_no_trade_abstains(self):
        self.pages[0]["trades"] = [(200, 100, 1, "t1")]
        self.pages[1]["trades"] = [(600, 120, 2, "t2")]
        self.assertEqual(validate_trade_pages(self.pages, **self.kw)["status"], "no_trades_in_interval")

    def test_missing_page_cursor_rejected(self):
        del self.pages[0]["cursor"]
        self.assertEqual(validate_trade_pages(self.pages, **self.kw)["status"], "invalid_cursor")

    def test_bad_source_rejected(self):
        self.assertEqual(validate_trade_pages(self.pages, **dict(self.kw, source="derived_from_ohlc"))["status"],
                         "unverified_complete_trade_interval")


if __name__ == "__main__":
    unittest.main()
