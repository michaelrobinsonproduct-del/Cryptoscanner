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

    def test_utf8_bom_accepted(self):
        with archive([("MANIFEST.json", b"\xef\xbb\xbf"+json.dumps({"build": "q2"}).encode())]) as z:
            r = inspect_archive(z, [])
        self.assertEqual(r["manifest_top_level_keys"], ["build"])


if __name__ == "__main__":
    unittest.main()
