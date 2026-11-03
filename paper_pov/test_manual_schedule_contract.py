"""Fixture-backed end-to-end read-only result contract tests."""
import copy
import hashlib
import io
import json
import tempfile
import zipfile
from pathlib import Path
import unittest

from paper_pov.manual_schedule_contract import inspect, load_verified_artifact
from paper_pov.results_report import render
from paper_pov.test_results_report import fixture


class ManualScheduledContractTests(unittest.TestCase):
    def pair(self):
        scan, score = fixture()
        manual, _ = render(copy.deepcopy(scan), copy.deepcopy(score), run_id="41235442591",
                           source_sha="a" * 40, ledger_commit="b" * 40,
                           event="workflow_dispatch")
        scheduled, _ = render(copy.deepcopy(scan), copy.deepcopy(score), run_id="41235442592",
                              source_sha="a" * 40, ledger_commit="b" * 40,
                              event="schedule", originating_cron="39 * * * *")
        return manual, scheduled

    def test_real_renderer_both_entry_modes_contract(self):
        m, s = self.pair()
        report = inspect(m, s)
        self.assertTrue(report["candidate_schema_parity"])
        self.assertEqual(report["manual_watch_count"], 2)
        self.assertEqual(report["scheduled_watch_count"], 2)
        self.assertFalse(report["market_time_candidate_equality_claimed"])

    def test_fail_closed_provenance_and_safety(self):
        for key, value in (("remote_readback_verified", False),
                           ("buy_approved", True), ("ledger_sha256", "fake"),
                           ("max_client_quote_age_seconds", 601),
                           ("source_sha", "unverified")):
            with self.subTest(key=key):
                m, s = self.pair()
                s[key] = value
                with self.assertRaises(ValueError):
                    inspect(m, s)

    def test_reject_spoofed_schedule_and_drifted_schema(self):
        for key, value in (("originating_cron", "10 * * * *"),
                           ("scheduled_slot_utc_minute", 9),
                           ("scheduled_slot_verified", False)):
            with self.subTest(key=key):
                m, s = self.pair()
                s[key] = value
                with self.assertRaises(ValueError):
                    inspect(m, s)
        m, s = self.pair()
        del s["candidates"][0]["quote_observed_at"]
        with self.assertRaisesRegex(ValueError, "candidate schema"):
            inspect(m, s)
        m, s = self.pair()
        s["untrusted_extra"] = True
        with self.assertRaisesRegex(ValueError, "result schema"):
            inspect(m, s)


    def test_signed_zip_real_renderer_roundtrip_and_tamper(self):
        manual, scheduled = self.pair()
        def archive(path, payload, *, corrupt=False, extra=False):
            data = json.dumps(payload, sort_keys=True).encode()
            markdown = b"# verified paper result\\n"
            manifest = (hashlib.sha256(data).hexdigest() + "  results.json\\n"
                        + hashlib.sha256(markdown).hexdigest() + "  results.md\\n").encode()
            with zipfile.ZipFile(path, "w") as z:
                z.writestr("results.json", data + (b" " if corrupt else b""))
                z.writestr("results.md", markdown)
                z.writestr("SHA256SUMS", manifest)
                if extra:
                    z.writestr("unexpected.json", b"{}")
        with tempfile.TemporaryDirectory() as tmp:
            m, s = Path(tmp) / "manual.zip", Path(tmp) / "scheduled.zip"
            archive(m, manual)
            archive(s, scheduled)
            self.assertTrue(inspect(load_verified_artifact(m), load_verified_artifact(s))["candidate_schema_parity"])
            archive(s, scheduled, corrupt=True)
            with self.assertRaisesRegex(ValueError, "checksum mismatch"):
                load_verified_artifact(s)
            archive(s, scheduled, extra=True)
            with self.assertRaisesRegex(ValueError, "ZIP members"):
                load_verified_artifact(s)

    def test_zip_rejects_duplicate_member_and_oversized_input(self):
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "bad.zip"
            with zipfile.ZipFile(path, "w") as z:
                z.writestr("results.json", b"{}")
                z.writestr("results.json", b"{}")
                z.writestr("results.md", b"")
                z.writestr("SHA256SUMS", b"")
            with self.assertRaisesRegex(ValueError, "ZIP members"):
                load_verified_artifact(path)
            path.write_bytes(b"x" * 2_000_001)
            with self.assertRaisesRegex(ValueError, "Oversized results ZIP"):
                load_verified_artifact(path)


if __name__ == "__main__":
    unittest.main()
