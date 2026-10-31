import io
import json
import tempfile
import unittest
import zipfile
from pathlib import Path

from inspect_kraken_trade_manifest import retained_trade_market_names
from verify_trade_revision_binding import verify, read_json, bounded_reuse_decision


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


    def test_revision_reuse_matching_strong_etag_and_metadata(self):
        t, m = reports()
        self.assertEqual(bounded_reuse_decision(t, m), "reuse")

    def test_same_etag_different_last_modified_requires_bounded_refresh(self):
        t, m = reports()
        m["source_revision_validator"]["last_modified"] = "Sat, 17 Oct 2026 13:22:27 GMT"
        self.assertEqual(bounded_reuse_decision(t, m), "refresh_bounded_trade_once")
        self.assertEqual(verify(t, m)["status"], "abstain_last_modified_mismatch")

    def test_missing_last_modified_requires_bounded_refresh(self):
        t, m = reports()
        del t["source_revision_validator"]["last_modified"]
        self.assertEqual(bounded_reuse_decision(t, m), "refresh_bounded_trade_once")

    def test_different_etag_never_recaptured_as_same_source(self):
        t, m = reports()
        m["source_revision_validator"]["strong_etag"] = '"revision-b"'
        self.assertEqual(bounded_reuse_decision(t, m), "abort_source_revision_conflict")

    def test_weak_or_missing_etag_aborts(self):
        for value in ("", 'W/"revision-a"', None):
            with self.subTest(value=value):
                t, m = reports()
                t["source_revision_validator"]["strong_etag"] = value
                self.assertEqual(bounded_reuse_decision(t, m), "abort_source_revision_conflict")

    def test_wrong_url_or_size_aborts_without_refresh(self):
        t, m = reports()
        m["source_url"] = "https://example.com/other.zip"
        self.assertEqual(bounded_reuse_decision(t, m), "abort_source_identity_mismatch")
        t, m = reports()
        m["source_expected_archive_bytes"] += 1
        self.assertEqual(bounded_reuse_decision(t, m), "abort_source_identity_mismatch")



    def test_missing_last_modified_never_claims_same_revision(self):
        t, m = reports()
        t["source_revision_validator"].pop("last_modified")
        self.assertFalse(verify(t, m)["same_source_revision"])

    def test_malformed_strong_etag_abstains_even_if_both_match(self):
        for value in ("unquoted", 'W/"weak"', '""', '"bad\\nvalue"', '"bad"quote"'):
            with self.subTest(value=value):
                t, m = reports()
                t["source_revision_validator"]["strong_etag"] = value
                m["source_revision_validator"]["strong_etag"] = value
                self.assertFalse(verify(t, m)["same_source_revision"])
                self.assertEqual(bounded_reuse_decision(t, m), "abort_source_revision_conflict")

    def test_zero_archive_size_is_not_source_identity(self):
        t, m = reports()
        t["source_archive_bytes_expected"] = 0
        m["source_expected_archive_bytes"] = 0
        self.assertFalse(verify(t, m)["same_source_revision"])

    def test_malformed_manifest_summary_abstains_not_crashes(self):
        for value in ([], "text", True, 0):
            with self.subTest(value=value):
                t, m = reports()
                m["manifest_schema_summary"] = value
                self.assertEqual(verify(t, m)["status"], "abstain_manifest_directory_inconsistent")

    def test_unsafe_market_names_abstain(self):
        for name in ("../BCHJPY.csv", "BCH-JPY.csv", "BCHJPY.txt", ".csv"):
            with self.subTest(name=name):
                t, m = reports()
                t["markets"] = {name: {}}
                m["selected_members"] = {name: {"present": True}}
                self.assertEqual(verify(t, m)["status"], "abstain_trade_market_selection_unverified")

    def test_official_last_modified_missing_abstains(self):
        t, m = reports()
        m["source_revision_validator"].pop("last_modified")
        self.assertFalse(verify(t, m)["same_source_revision"])
        self.assertEqual(bounded_reuse_decision(t, m), "refresh_bounded_trade_once")

if __name__ == "__main__":
    unittest.main()
