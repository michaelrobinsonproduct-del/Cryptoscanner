import hashlib
import json
import tempfile
import unittest
from pathlib import Path
from paper_pov.archive_partition_gate import verify_partitions


class ArchivePartitionGateTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        self.root = Path(self.tmp.name)
        self.payload = b"2026-01-01T00:00:00Z,100,101,99,100\n"
        (self.root / "pair.csv").write_bytes(self.payload)
        self.manifest = {
            "schema": "kraken_archive_manifest_v1", "source": "Kraken",
            "partitions": [{"file": "pair.csv", "size_bytes": len(self.payload),
                            "sha256": hashlib.sha256(self.payload).hexdigest()}]}

    def test_verified_bytes_are_not_claimed_as_authenticated_source(self):
        result = verify_partitions(self.manifest, self.root)
        self.assertEqual(result["partitions_verified"], 1)
        self.assertFalse(result["source_authenticated"])
        self.assertFalse(result["qualified_for_learning"])

    def test_modified_partition_rejected(self):
        (self.root / "pair.csv").write_bytes(b"x" * len(self.payload))
        with self.assertRaisesRegex(ValueError, "checksum"):
            verify_partitions(self.manifest, self.root)

    def test_missing_partition_rejected(self):
        (self.root / "pair.csv").unlink()
        with self.assertRaises(FileNotFoundError):
            verify_partitions(self.manifest, self.root)

    def test_unsafe_path_rejected(self):
        self.manifest["partitions"][0]["file"] = "../pair.csv"
        with self.assertRaisesRegex(ValueError, "Unsafe"):
            verify_partitions(self.manifest, self.root)

    def test_duplicate_partition_rejected(self):
        self.manifest["partitions"].append(dict(self.manifest["partitions"][0]))
        with self.assertRaisesRegex(ValueError, "Duplicate"):
            verify_partitions(self.manifest, self.root)

    def test_unpinned_or_invalid_manifest_rejected(self):
        self.manifest["partitions"][0]["sha256"] = "bad"
        with self.assertRaisesRegex(ValueError, "digest"):
            verify_partitions(self.manifest, self.root)


if __name__ == "__main__":
    unittest.main()
