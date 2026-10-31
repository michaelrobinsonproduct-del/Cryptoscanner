import io
import json
import tempfile
import unittest
import zipfile
from pathlib import Path

from inspect_kraken_trade_manifest import retained_trade_market_names
from verify_trade_revision_binding import verify, read_json


def reports():
    etag = '"revision-a"'
    trade = {
        "source_url": "https://assets.kraken.com/marketing/institutions/Kraken_Trades_2026Q2.zip",
        "source_archive_bytes_expected": 1334345194,
        "source_revision_validator": {"strong_etag": etag, "last_modified": "Fri, 16 Oct 2026 13:22:27 GMT"},
        "markets": {"BCHJPY.csv": {}, "DENTEUR.csv": {}},
    }
    official = {
        "source_url": trade["source_url"],
        "source_expected_archive_bytes": 1334345194,
        "source_revision_validator": dict(trade["source_revision_validator"]),
        "manifest_schema_summary": {"structural_consistency": {
            "manifest_file_count_matches_zip_csv_count": True,
            "file_count_matches_pair_count": True,
        }},
        "selected_members": {"BCHJPY.csv": {"present": True}, "DENTEUR.csv": {"present": True}},
    }
    return trade, official


class RevisionBindingTests(unittest.TestCase):
    def test_same_revision_is_not_authentication_or_label(self):
        t, m = reports()
        r = verify(t, m)
        self.assertTrue(r["same_source_revision"])
        self.assertEqual(r["real_labels"], 0)
        self.assertFalse(r["source_trade_archive_sha256_verified"])
        self.assertEqual(r["complete_trade_intervals_verified"], 0)
        self.assertEqual(r["held_out_evaluation"], "not_authorized")

    def test_mismatched_strong_etag_abstains(self):
        t, m = reports()
        m["source_revision_validator"]["strong_etag"] = '"revision-b"'
        self.assertFalse(verify(t, m)["same_source_revision"])

    def test_missing_or_weak_etag_abstains(self):
        for etag in (None, "", 'W/"revision-a"'):
            with self.subTest(etag=etag):
                t, m = reports()
                t["source_revision_validator"]["strong_etag"] = etag
                self.assertFalse(verify(t, m)["same_source_revision"])

    def test_source_url_and_size_mismatch_abstains(self):
        t, m = reports()
        m["source_expected_archive_bytes"] += 1
        self.assertEqual(verify(t, m)["status"], "abstain_source_identity_mismatch")
        t, m = reports()
        m["source_url"] = "https://example.org/other.zip"
        self.assertEqual(verify(t, m)["status"], "abstain_source_identity_mismatch")

    def test_manifest_count_mismatch_abstains(self):
        t, m = reports()
        m["manifest_schema_summary"]["structural_consistency"]["manifest_file_count_matches_zip_csv_count"] = False
        self.assertEqual(verify(t, m)["status"], "abstain_manifest_directory_inconsistent")

    def test_unchecked_actual_trade_market_abstains(self):
        t, m = reports()
        m["selected_members"].pop("DENTEUR.csv")
        self.assertEqual(verify(t, m)["status"], "abstain_trade_market_selection_unverified")

    def test_last_modified_mismatch_abstains(self):
        t, m = reports()
        m["source_revision_validator"]["last_modified"] = "Sat, 17 Oct 2026 13:22:27 GMT"
        self.assertEqual(verify(t, m)["status"], "abstain_last_modified_mismatch")

    def test_retained_actual_markets_instead_of_first_four(self):
        with tempfile.TemporaryDirectory() as temp:
            p = Path(temp) / "trades.zip"
            with zipfile.ZipFile(p, "w") as z:
                z.writestr("manifest.json", json.dumps({"markets": {"DENTEUR.csv": {}, "BCHJPY.csv": {}}}))
                z.writestr("trades/DENTEUR.csv", "data")
                z.writestr("trades/BCHJPY.csv", "data")
            self.assertEqual(retained_trade_market_names(p), ["BCHJPY.csv", "DENTEUR.csv"])

    def test_missing_retained_member_rejected(self):
        with tempfile.TemporaryDirectory() as temp:
            p = Path(temp) / "trades.zip"
            with zipfile.ZipFile(p, "w") as z:
                z.writestr("manifest.json", json.dumps({"markets": {"DENTEUR.csv": {}}}))
            with self.assertRaisesRegex(ValueError, "missing retained"):
                retained_trade_market_names(p)

    def test_bounded_report_reader_rejects_oversize(self):
        with tempfile.TemporaryDirectory() as temp:
            p = Path(temp) / "large.json"
            p.write_bytes(b"x" * 32769)
            with self.assertRaisesRegex(ValueError, "oversized"):
                read_json(p)


if __name__ == "__main__":
    unittest.main()
