"""Synthetic adversarial artifact recovery tests; not live recovery evidence."""
import copy
import hashlib
import json
import tempfile
import unittest
from pathlib import Path

from paper_eval.recovery import load_bundle, verify_bundle
from paper_pov import ledger
from paper_pov.test_ledger import SHA, synthetic

COMMIT = "b" * 40


def fixture():
    report = synthetic(0)
    state = ledger.advance(ledger.empty(), report, SHA)
    members = {
        "latest.json": json.dumps(report, sort_keys=True).encode(),
        "ledger.json": json.dumps(state, sort_keys=True).encode(),
        "scoreboard.json": json.dumps(ledger.scoreboard(state), sort_keys=True).encode(),
    }
    members["SHA256SUMS"] = "".join(
        hashlib.sha256(members[name]).hexdigest() + "  " + name + "\n"
        for name in sorted(members)
    ).encode()
    return members


def reseal_manifest(bundle):
    bundle["SHA256SUMS"] = "".join(
        hashlib.sha256(bundle[name]).hexdigest() + "  " + name + "\n"
        for name in sorted(set(bundle) - {"SHA256SUMS"})
    ).encode()


class ArtifactRecoveryTests(unittest.TestCase):
    def test_exact_artifact_recovery_and_independent_git_bytes(self):
        bundle = fixture()
        proof = verify_bundle(bundle, bundle["ledger.json"], COMMIT)
        self.assertEqual(proof["ledger_generation"], 1)
        self.assertEqual(proof["latest_predictions_recovered"], 12)
        self.assertEqual(proof["manifest_members_verified"], 3)
        self.assertTrue(proof["remote_git_bytes_match"])
        self.assertFalse(proof["thirty_day_recovery_proven"])
        self.assertIsNone(proof["independent_held_out_lift"])

    def test_missing_and_extra_members_rejected(self):
        bundle = fixture()
        expected = bundle["ledger.json"]
        del bundle["scoreboard.json"]
        with self.assertRaisesRegex(ValueError, "artifact members"):
            verify_bundle(bundle, expected, COMMIT)
        bundle = fixture()
        bundle["unexpected.txt"] = b"x"
        with self.assertRaisesRegex(ValueError, "artifact members"):
            verify_bundle(bundle, expected, COMMIT)

    def test_modified_ledger_fails_even_if_manifest_resealed(self):
        bundle = fixture()
        expected = bundle["ledger.json"]
        state = json.loads(expected)
        state["predictions"][0]["baseline_score"] += 1
        ledger.seal(state)
        bundle["ledger.json"] = json.dumps(state, sort_keys=True).encode()
        reseal_manifest(bundle)
        with self.assertRaisesRegex(ValueError, "independent Git snapshot"):
            verify_bundle(bundle, expected, COMMIT)

    def test_modified_report_fails_even_if_manifest_resealed(self):
        bundle = fixture()
        expected = bundle["ledger.json"]
        report = json.loads(bundle["latest.json"])
        report["watch"][0]["challenger_score"] += 1
        bundle["latest.json"] = json.dumps(report, sort_keys=True).encode()
        reseal_manifest(bundle)
        with self.assertRaisesRegex(ValueError, "Latest report does not bind"):
            verify_bundle(bundle, expected, COMMIT)

    def test_resealed_scoreboard_fraud_rejected(self):
        bundle = fixture()
        expected = bundle["ledger.json"]
        score = json.loads(bundle["scoreboard.json"])
        score["matured_labels"] = 999
        bundle["scoreboard.json"] = json.dumps(score).encode()
        reseal_manifest(bundle)
        with self.assertRaisesRegex(ValueError, "scoreboard disagrees"):
            verify_bundle(bundle, expected, COMMIT)

    def test_corrupt_digest_rejected(self):
        bundle = fixture()
        expected = bundle["ledger.json"]
        bundle["scoreboard.json"] += b" "
        with self.assertRaisesRegex(ValueError, "SHA256 mismatch"):
            verify_bundle(bundle, expected, COMMIT)

    def test_duplicate_manifest_entry_and_path_traversal_rejected(self):
        bundle = fixture()
        expected = bundle["ledger.json"]
        lines = bundle["SHA256SUMS"].decode().splitlines()
        bundle["SHA256SUMS"] = ("\n".join([lines[0], lines[0], lines[2]]) + "\n").encode()
        with self.assertRaisesRegex(ValueError, "manifest"):
            verify_bundle(bundle, expected, COMMIT)
        bundle = fixture()
        bundle["SHA256SUMS"] = bundle["SHA256SUMS"].replace(
            b"  latest.json", b"  ../latest.json")
        with self.assertRaisesRegex(ValueError, "manifest"):
            verify_bundle(bundle, expected, COMMIT)

    def test_missing_immutable_git_commit_rejected(self):
        bundle = fixture()
        with self.assertRaisesRegex(ValueError, "immutable ledger commit"):
            verify_bundle(bundle, bundle["ledger.json"], "main")

    def test_bounded_sizes_reject_oversized_artifact(self):
        bundle = fixture()
        bundle["latest.json"] = b"x" * 12_500_001
        with self.assertRaisesRegex(ValueError, "Oversized"):
            verify_bundle(bundle, bundle["ledger.json"], COMMIT)

    def test_loader_refuses_symlink_and_extra_files(self):
        bundle = fixture()
        with tempfile.TemporaryDirectory() as d:
            root = Path(d)
            for name, value in bundle.items():
                (root / name).write_bytes(value)
            self.assertEqual(load_bundle(root), bundle)
            (root / "extra").write_text("untrusted")
            with self.assertRaisesRegex(ValueError, "artifact members"):
                load_bundle(root)
            (root / "extra").unlink()
            (root / "latest.json").unlink()
            (root / "latest.json").symlink_to(root / "ledger.json")
            with self.assertRaisesRegex(ValueError, "linked"):
                load_bundle(root)

    def test_latest_quote_rewrite_with_report_hash_rebound_rejected(self):
        bundle = fixture()
        expected = bundle["ledger.json"]
        report = json.loads(bundle["latest.json"])
        report["observations"][0]["price"] += 2
        bundle["latest.json"] = json.dumps(report, sort_keys=True).encode()
        reseal_manifest(bundle)
        with self.assertRaisesRegex(ValueError, "Latest report does not bind"):
            verify_bundle(bundle, expected, COMMIT)


if __name__ == "__main__":
    unittest.main()
