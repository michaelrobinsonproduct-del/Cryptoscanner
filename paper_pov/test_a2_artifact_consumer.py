"""End-to-end A2 artifact transport regression."""
import datetime as dt
import io
import json
import tempfile
import unittest
import zipfile
from pathlib import Path
from paper_pov.scanner import UTC, persist_report
from paper_pov.candidate_snapshot import read_snapshot
from paper_pov.a2_artifact_consumer import read_artifact_zip, read_published_artifact
from paper_pov.preselection_universe import export_universe

class ArtifactConsumerTests(unittest.TestCase):
    def setUp(self):
        self.now = dt.datetime(2026, 11, 3, 20, 0, tzinfo=UTC)
        self.report = {"as_of": self.now.isoformat(), "mode": "PAPER_ONLY",
                       "buy_approved": False, "scan_status": "ABSTAIN_NO_LIQUID_CANDIDATES",
                       "watch": [], "eligible_pairs": 1, "observed_markets": 1,
                       "abstention_counts": {"ohlc_gap_or_schema": 1}}
    def artifact(self, mutate=None):
        with tempfile.TemporaryDirectory() as d:
            root = Path(d)
            receipt = persist_report(root / "latest.json", self.report)
            files = {"latest.json": (root / "latest.json").read_bytes(),
                     "receipts/" + receipt.name: receipt.read_bytes(),
                     "verified-snapshot.json": json.dumps(read_snapshot(root / "latest.json", now=self.now)).encode()}
        if mutate:
            mutate(files)
        output = io.BytesIO()
        with zipfile.ZipFile(output, "w") as z:
            for name, data in files.items():
                z.writestr(name, data)
        return output.getvalue()
    def test_round_trip_and_recheck_at_download_time(self):
        result = read_artifact_zip(self.artifact(), now=self.now + dt.timedelta(seconds=30))
        self.assertEqual(result["scan_status"], "ABSTAIN_NO_LIQUID_CANDIDATES")
        self.assertGreater(result["snapshot_age_seconds"], 0)
        with self.assertRaisesRegex(ValueError, "stale"):
            read_artifact_zip(self.artifact(), now=self.now + dt.timedelta(minutes=11))
    def test_tampered_receipt_rejected(self):
        with self.assertRaisesRegex(ValueError, "receipt mismatch"):
            read_artifact_zip(self.artifact(lambda f: f.__setitem__("latest.json", b"{}")), now=self.now)
    def test_forged_export_rejected(self):
        def forge(f):
            x = json.loads(f["verified-snapshot.json"])
            x["observed_markets"] = 100
            f["verified-snapshot.json"] = json.dumps(x).encode()
        with self.assertRaisesRegex(ValueError, "exported consumer snapshot mismatch"):
            read_artifact_zip(self.artifact(forge), now=self.now)
    def test_extra_file_rejected(self):
        with self.assertRaisesRegex(ValueError, "invalid A2 artifact members"):
            read_artifact_zip(self.artifact(lambda f: f.__setitem__("untrusted.txt", b"bad")), now=self.now)
    def test_downloaded_directory_consumer_matches_receipt_and_preselection(self):
        # Exercise the exact B-facing directory contract with a complete
        # fixture-backed scanner report, including zero-WATCH abstention.
        from paper_pov.test_a1_a2_end_to_end import EndToEndCandidateTests
        fixture = EndToEndCandidateTests()
        fixture.setUp()
        for ticker in fixture.ticker.values():
            ticker["o"] = ticker["c"][0]
        from paper_pov.scanner import scan
        report = scan(api=fixture.api, clock=lambda: fixture.now, sleep=lambda _: None)
        with tempfile.TemporaryDirectory() as d:
            root = Path(d)
            receipt = persist_report(root / "latest.json", report)
            snapshot = read_snapshot(root / "latest.json", now=fixture.now)
            (root / "verified-snapshot.json").write_text(json.dumps(snapshot))
            universe = export_universe(root / "latest.json", now=fixture.now)
            (root / "preselection-universe.json").write_text(json.dumps(universe))
            with zipfile.ZipFile(root / "a2-verified-transport.zip", "w") as z:
                z.write(root / "latest.json", "latest.json")
                z.write(receipt, "receipts/" + receipt.name)
                z.write(root / "verified-snapshot.json", "verified-snapshot.json")
            accepted = read_published_artifact(root, now=fixture.now + dt.timedelta(seconds=30))
            self.assertEqual(accepted["snapshot"]["watch"], [])
            self.assertEqual(accepted["preselection"]["coverage"]["valid_tickers"], 25)
            self.assertFalse(accepted["preselection"]["qualified_for_learning"])
            tampered = dict(universe)
            tampered["receipt_sha256"] = "0" * 64
            (root / "preselection-universe.json").write_text(json.dumps(tampered))
            with self.assertRaisesRegex(ValueError, "published preselection universe mismatch"):
                read_published_artifact(root, now=fixture.now + dt.timedelta(seconds=30))
            (root / "preselection-universe.json").write_text(json.dumps(universe))
            with self.assertRaisesRegex(ValueError, "stale"):
                read_published_artifact(root, now=fixture.now + dt.timedelta(minutes=11))
if __name__ == "__main__":
    unittest.main()
