import hashlib
import json
import tempfile
import unittest
from pathlib import Path

from research.prospective_outcome_adapter import coverage, verified_rows


def fixture(root):
    raw_depth = b'{"depth":"raw"}'
    raw_trades = b'{"trades":"raw"}'
    receipts = []
    for stage, raw in (("depth", raw_depth), ("trades", raw_trades)):
        name = "00-XBTUSD-" + stage + ".json"
        (root / name).write_bytes(raw)
        receipts.append({"stage": stage, "file": name,
                         "sha256": hashlib.sha256(raw).hexdigest(), "bytes": len(raw)})
    evidence = {
        "pair_requested": "XBTUSD", "pair_source": "XXBTZUSD",
        "eligible_point_in_time_snapshot": True,
        "depth_receipt": {"sha256": receipts[0]["sha256"], "first_observed_at": 1700000002},
        "trades_receipt": {"sha256": receipts[1]["sha256"]},
        "bid_level_event_at": "1700000000", "ask_level_event_at": "1700000000",
        "best_bid": "99", "best_ask": "100"
    }
    (root / "00-XBTUSD-evidence.json").write_text(json.dumps(evidence))
    manifest = {
        "mode": "ONE_SHOT_PROSPECTIVE_PUBLIC_TLS_RESEARCH_ONLY",
        "pairs_requested": 1,
        "entries": [{"pair": "XBTUSD", "status": "ELIGIBLE",
                     "source_market": "XXBTZUSD",
                     "evidence_file": "00-XBTUSD-evidence.json", "raw": receipts}]
    }
    (root / "manifest.json").write_text(json.dumps(manifest))
    return manifest, evidence


class AdapterTests(unittest.TestCase):
    def test_valid_snapshot_cannot_fabricate_future_episode(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            fixture(root)
            result = coverage(root)
            self.assertEqual(result["snapshots_verified"], 1)
            self.assertEqual(result["qualified_first_entry_episodes"], 0)
            self.assertEqual(result["outcome_statuses"], ["ABSTAIN_INCOMPLETE"])

    def test_raw_mutation_fails_closed(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            fixture(root)
            (root / "00-XBTUSD-depth.json").write_bytes(b"changed")
            with self.assertRaisesRegex(ValueError, "raw receipt mismatch"):
                verified_rows(root)

    def test_evidence_identity_mismatch(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            _, evidence = fixture(root)
            evidence["pair_source"] = "OTHER"
            (root / "00-XBTUSD-evidence.json").write_text(json.dumps(evidence))
            with self.assertRaisesRegex(ValueError, "source identity mismatch"):
                verified_rows(root)

    def test_incomplete_manifest_fails_closed(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            manifest, _ = fixture(root)
            manifest["pairs_requested"] = 2
            (root / "manifest.json").write_text(json.dumps(manifest))
            with self.assertRaisesRegex(ValueError, "manifest coverage mismatch"):
                verified_rows(root)

    def test_stale_quote_fails_closed(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            _, evidence = fixture(root)
            evidence["ask_level_event_at"] = "1699999000"
            (root / "00-XBTUSD-evidence.json").write_text(json.dumps(evidence))
            with self.assertRaisesRegex(ValueError, "stale quote"):
                verified_rows(root)

    def test_invalid_snapshot_is_explicit_abstention(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            manifest, _ = fixture(root)
            manifest["entries"][0]["status"] = "INVALID"
            (root / "manifest.json").write_text(json.dumps(manifest))
            result = coverage(root)
            self.assertEqual(result["snapshots_verified"], 0)
            self.assertEqual(result["abstentions"][0]["reason"], "NO_ELIGIBLE_SNAPSHOT")


if __name__ == "__main__":
    unittest.main()
