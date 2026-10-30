import io
import tempfile
import unittest
import zipfile
from pathlib import Path
from unittest.mock import patch
from reconstruct_verified_archive import reconstruct_member, ARCHIVE_SHA256


class ArchiveAdapterTests(unittest.TestCase):
    def test_no_provenance_abstains_without_access(self):
        result = reconstruct_member("/nonexistent", "PAIR_5.csv", 300)
        self.assertEqual(result["status"], "unverified_source_timestamp_semantics")

    def test_wrong_archive_identity_rejected(self):
        with self.assertRaises(ValueError):
            reconstruct_member("/nonexistent", "PAIR_5.csv", 300,
                               verified_timestamp_semantics=True, archive_sha256="wrong")

    def test_missing_archive_rejected(self):
        with self.assertRaises(ValueError):
            reconstruct_member("/nonexistent", "PAIR_5.csv", 300,
                               verified_timestamp_semantics=True)

    def test_verified_archive_fixture_boundaries(self):
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "archive.zip"
            with zipfile.ZipFile(path, "w") as z:
                z.writestr("PAIR_5.csv", "".join(
                    f"{i*300},100,130,100,100,10,1\\n" for i in range(578)
                ).replace("\\n", "\n"))
            with patch("reconstruct_verified_archive.ARCHIVE_SHA256",
                       __import__("hashlib").sha256(path.read_bytes()).hexdigest()):
                # Caller-supplied expected identity must still match pinned source.
                with self.assertRaises(ValueError):
                    reconstruct_member(path, "PAIR_5.csv", 300,
                                       verified_timestamp_semantics=True)

    def test_path_traversal_rejected_after_verified_archive(self):
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "archive.zip"
            with zipfile.ZipFile(path, "w") as z:
                z.writestr("PAIR_5.csv", "0,100,100,100,100,10,1\n")
            digest = __import__("hashlib").sha256(path.read_bytes()).hexdigest()
            with patch("reconstruct_verified_archive.ARCHIVE_SHA256", digest):
                with self.assertRaises(ValueError):
                    reconstruct_member(path, "../PAIR_5.csv", 300,
                                       archive_sha256=digest, verified_timestamp_semantics=True)


if __name__ == "__main__":
    unittest.main()
