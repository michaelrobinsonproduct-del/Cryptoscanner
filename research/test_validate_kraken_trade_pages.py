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
        self.assertEqual(validate_trade_pages(self.pages, **self.kw)["status"], "candidate_no_trades_requires_source_attestation")

    def test_missing_page_cursor_rejected(self):
        del self.pages[0]["cursor"]
        self.assertEqual(validate_trade_pages(self.pages, **self.kw)["status"], "invalid_cursor")

    def test_bad_source_rejected(self):
        self.assertEqual(validate_trade_pages(self.pages, **dict(self.kw, source="derived_from_ohlc"))["status"],
                         "unverified_complete_trade_interval")


    def test_truthy_strings_cannot_assert_completeness(self):
        for key in ("complete_cursor_chain", "started_before_interval", "ended_after_interval"):
            with self.subTest(key=key):
                r = validate_trade_pages(self.pages, **dict(self.kw, **{key: "false"}))
                self.assertEqual(r["status"], "unverified_complete_trade_interval")

    def test_boolean_start_or_end_is_not_an_epoch(self):
        for key in ("start", "end"):
            with self.subTest(key=key):
                r = validate_trade_pages(self.pages, **dict(self.kw, **{key: True}))
                self.assertEqual(r["status"], "invalid_interval")

    def test_boolean_trade_number_is_not_numeric_evidence(self):
        for position in (0, 1, 2):
            with self.subTest(position=position):
                pages = [dict(p, trades=list(p["trades"])) for p in self.pages]
                row = list(pages[0]["trades"][0])
                row[position] = True
                pages[0]["trades"][0] = tuple(row)
                self.assertEqual(validate_trade_pages(pages, **self.kw)["status"], "invalid_trade_row")

    def test_whitespace_only_trade_id_is_invalid(self):
        self.pages[0]["trades"][0] = (301, 100, 1, "   ")
        self.assertEqual(validate_trade_pages(self.pages, **self.kw)["status"],
                         "duplicate_or_invalid_trade_id")

    def test_boolean_trade_id_is_invalid(self):
        self.pages[0]["trades"][0] = (301, 100, 1, True)
        self.assertEqual(validate_trade_pages(self.pages, **self.kw)["status"],
                         "duplicate_or_invalid_trade_id")

    def test_cross_page_backward_timestamp_rejected(self):
        self.pages[1]["trades"][0] = (300, 120, 2, "t2")
        self.assertEqual(validate_trade_pages(self.pages, **self.kw)["status"],
                         "nonchronological_trade_page")

    def test_invalid_page_container_abstains(self):
        for pages in ({"cursor": "a"}, "not a page list", [], None):
            with self.subTest(pages=pages):
                self.assertEqual(validate_trade_pages(pages, **self.kw)["status"],
                                 "missing_or_oversized_pages")

    def test_negative_source_timestamp_rejected(self):
        self.pages[0]["trades"][0] = (-1, 100, 1, "t1")
        self.assertEqual(validate_trade_pages(self.pages, **self.kw)["status"],
                         "invalid_trade_row")


if __name__ == "__main__":
    unittest.main()
