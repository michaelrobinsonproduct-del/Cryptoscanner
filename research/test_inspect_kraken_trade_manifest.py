import hashlib
import io
import json
import unittest
import zipfile

from inspect_kraken_trade_manifest import inspect_archive, MAX_MANIFEST_BYTES


def archive(entries):
    data = io.BytesIO()
    with zipfile.ZipFile(data, "w", compression=zipfile.ZIP_DEFLATED) as z:
        for name, content in entries:
            z.writestr(name, content)
    data.seek(0)
    return zipfile.ZipFile(data)


class TradeManifestTests(unittest.TestCase):
    def test_realistic_manifest_is_structural_only(self):
        raw = b'{"build":"2026Q2","pairs":4}'
        with archive([("MANIFEST.json", raw), ("DENTEUR.csv", b"fake")]) as z:
            r = inspect_archive(z, ["DENTEUR.csv", "BCHJPY.csv"])
        self.assertEqual(r["manifest_sha256"], hashlib.sha256(raw).hexdigest())
        self.assertEqual(r["manifest_top_level_keys"], ["build", "pairs"])
        self.assertTrue(r["selected_members"]["DENTEUR.csv"]["present"])
        self.assertFalse(r["selected_members"]["DENTEUR.csv"]["member_full_sha256_verified"])
        self.assertFalse(r["selected_members"]["BCHJPY.csv"]["present"])
        self.assertIn("not_authenticated", r["status"])

    def test_missing_manifest_fails_to_authenticate(self):
        with archive([("DENTEUR.csv", b"data")]) as z:
            r = inspect_archive(z, ["DENTEUR.csv"])
        self.assertEqual(r["status"], "missing_official_manifest")
        self.assertIsNone(r["manifest_sha256"])

    def test_duplicate_manifest_rejected(self):
        with archive([("MANIFEST.json", b"{}"), ("MANIFEST.json", b"{}")]) as z:
            with self.assertRaisesRegex(ValueError, "duplicate ZIP"):
                inspect_archive(z, [])

    def test_invalid_json_rejected(self):
        with archive([("MANIFEST.json", b"{broken")]) as z:
            with self.assertRaisesRegex(ValueError, "invalid official"):
                inspect_archive(z, [])

    def test_non_object_json_rejected(self):
        with archive([("MANIFEST.json", b"[]")]) as z:
            with self.assertRaisesRegex(ValueError, "JSON object"):
                inspect_archive(z, [])

    def test_oversized_manifest_rejected_before_decompression(self):
        with archive([("MANIFEST.json", b"x"*(MAX_MANIFEST_BYTES+1))]) as z:
            with self.assertRaisesRegex(ValueError, "oversized"):
                inspect_archive(z, [])

    def test_duplicate_selection_rejected(self):
        with archive([("MANIFEST.json", b"{}")]) as z:
            with self.assertRaisesRegex(ValueError, "duplicate selected"):
                inspect_archive(z, ["A.csv", "A.csv"])

    def test_traversal_selection_rejected(self):
        with archive([("MANIFEST.json", b"{}")]) as z:
            with self.assertRaisesRegex(ValueError, "unsafe selected"):
                inspect_archive(z, ["../A.csv"])

    def test_excessive_market_selection_rejected(self):
        with archive([("MANIFEST.json", b"{}")]) as z:
            with self.assertRaisesRegex(ValueError, "invalid bounded"):
                inspect_archive(z, ["A.csv"]*5)

    def test_dictionary_file_metadata_is_reported_but_not_authenticated(self):
        manifest = {"files": {"DENTEUR.csv": {"sha256": "a"*64, "rows": 100,
                                                "first": "2026-04-01"},
                              "OTHER.csv": {"sha256": "b"*64}},
                    "coverage": {"start": "2026-04-01", "end": "2026-06-30"},
                    "schema_version": 2}
        with archive([("MANIFEST.json", json.dumps(manifest))]) as z:
            r = inspect_archive(z, ["DENTEUR.csv"])
        meta = r["manifest_schema_summary"]
        self.assertEqual(meta["files"]["count"], 2)
        self.assertEqual(meta["selected_file_entries"]["DENTEUR.csv"]["scalar_fields"]["rows"], 100)
        self.assertNotIn("OTHER.csv", meta["selected_file_entries"])
        self.assertEqual(meta["scalars"]["schema_version"], 2)
        self.assertIn("not_authenticated", r["status"])

    def test_list_file_metadata_is_bounded_to_selected(self):
        manifest = {"files": [{"filename": "DENTEUR.csv", "rows": 11},
                              {"filename": "OTHER.csv", "rows": 22}]}
        with archive([("MANIFEST.json", json.dumps(manifest))]) as z:
            r = inspect_archive(z, ["DENTEUR.csv"])
        entries = r["manifest_schema_summary"]["selected_file_entries"]
        self.assertEqual(entries["DENTEUR.csv"]["scalar_fields"]["rows"], 11)
        self.assertEqual(len(entries), 1)

    def test_unbounded_scalar_values_are_redacted(self):
        manifest = {"release": "X"*300, "files": {"DENTEUR.csv": {"sha256": "X"*300}}}
        with archive([("MANIFEST.json", json.dumps(manifest))]) as z:
            r = inspect_archive(z, ["DENTEUR.csv"])
        self.assertEqual(r["manifest_schema_summary"]["scalars"]["release"]["type"], "str")
        self.assertEqual(r["manifest_schema_summary"]["selected_file_entries"]["DENTEUR.csv"]["scalar_fields"]["sha256"]["type"], "str")

    def test_utf8_bom_accepted(self):
        with archive([("MANIFEST.json", b"\xef\xbb\xbf"+json.dumps({"build": "q2"}).encode())]) as z:
            r = inspect_archive(z, [])
        self.assertEqual(r["manifest_top_level_keys"], ["build"])


    def test_manifest_string_file_list_crosschecks_zip(self):
        manifest = {"files": ["DENTEUR.csv", "BCHJPY.csv"], "pairs": 2,
                    "coverage": {"start": "2026-04-01", "end": "2026-06-30"}}
        with archive([("MANIFEST.json", json.dumps(manifest)),
                      ("DENTEUR.csv", b"trade-data")]) as z:
            r = inspect_archive(z, ["DENTEUR.csv", "BCHJPY.csv"])
        c = r["manifest_schema_summary"]["structural_consistency"]
        self.assertTrue(c["file_count_matches_pair_count"])
        self.assertTrue(c["listed_selected_members"]["DENTEUR.csv"])
        self.assertTrue(c["listed_selected_members"]["BCHJPY.csv"])
        self.assertTrue(c["listed_selected_members_in_zip"]["DENTEUR.csv"])
        self.assertFalse(c["listed_selected_members_in_zip"]["BCHJPY.csv"])
        self.assertEqual(c["coverage_fields"]["start"], "2026-04-01")
        self.assertFalse(c["source_authenticated"])
        self.assertEqual(c["complete_trade_intervals_verified"], 0)

    def test_manifest_pair_count_mismatch_is_explicit_not_completeness(self):
        manifest = {"files": ["DENTEUR.csv"], "pairs": 2}
        with archive([("MANIFEST.json", json.dumps(manifest)),
                      ("DENTEUR.csv", b"trade-data")]) as z:
            r = inspect_archive(z, ["DENTEUR.csv"])
        c = r["manifest_schema_summary"]["structural_consistency"]
        self.assertFalse(c["file_count_matches_pair_count"])
        self.assertFalse(c["source_authenticated"])

    def test_manifest_dict_listing_crosschecks_zip(self):
        manifest = {"files": {"DENTEUR.csv": {"rows": 100}}, "pairs": 1}
        with archive([("MANIFEST.json", json.dumps(manifest)),
                      ("DENTEUR.csv", b"trade-data")]) as z:
            r = inspect_archive(z, ["DENTEUR.csv"])
        c = r["manifest_schema_summary"]["structural_consistency"]
        self.assertTrue(c["listed_selected_members_in_zip"]["DENTEUR.csv"])
        self.assertTrue(c["file_count_matches_pair_count"])

    def test_unknown_manifest_listing_does_not_claim_completeness(self):
        manifest = {"files": None, "pairs": True, "coverage": ["unknown"]}
        with archive([("MANIFEST.json", json.dumps(manifest)),
                      ("DENTEUR.csv", b"trade-data")]) as z:
            r = inspect_archive(z, ["DENTEUR.csv"])
        c = r["manifest_schema_summary"]["structural_consistency"]
        self.assertIsNone(c["file_count_matches_pair_count"])
        self.assertIsNone(c["manifest_pair_count"])
        self.assertFalse(c["listed_selected_members"]["DENTEUR.csv"])
        self.assertFalse(c["source_authenticated"])

    def test_manifest_list_dict_listing_crosschecks_zip(self):
        manifest = {"files": [{"filename": "DENTEUR.csv", "rows": 2}], "pairs": 1}
        with archive([("MANIFEST.json", json.dumps(manifest)),
                      ("DENTEUR.csv", b"trade-data")]) as z:
            r = inspect_archive(z, ["DENTEUR.csv"])
        c = r["manifest_schema_summary"]["structural_consistency"]
        self.assertTrue(c["listed_selected_members_in_zip"]["DENTEUR.csv"])
        self.assertFalse(c["source_authenticated"])



if __name__ == "__main__":
    unittest.main()
