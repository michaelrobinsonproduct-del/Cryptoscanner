"""Read-only GitHub artifact transport acceptance with a fake gh CLI."""
import hashlib
import json
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch
from paper_pov.github_sealed_bundle_readback import read_run

class GitHubSealedBundleReadbackTests(unittest.TestCase):
    def _run(self, *, tamper=None, origin="schedule", legacy=False):
        metadata={"databaseId":123,"status":"completed","conclusion":"success",
                  "event":origin,"headBranch":"main",
                  "workflowName":"Public Kraken Paper POV (scheduled, isolated ledger)",
                  "headSha":"a"*40}
        def fake_runner(args):
            if args[1:3]==["run","view"]:
                return json.dumps(metadata).encode()
            if args[1:3]==["run","download"]:
                root=Path(args[-1])
                for name in (("latest.json","scoreboard.json","ledger.json") if legacy else ("latest.json","scoreboard.json","ledger.json","slot_receipt.json")):
                    (root/name).write_bytes((json.dumps({"run_id":"123","source_sha":"a"*40,"historical_quotes_reconstructed":False}) if name=="slot_receipt.json" else name+"-content").encode())
                if not legacy:
                    (root/"sealed-http-bundle.json").write_text('{"schema":"fixture"}')
                lines=[]
                for name in (("latest.json","scoreboard.json","ledger.json") if legacy else ("latest.json","scoreboard.json","ledger.json","slot_receipt.json","sealed-http-bundle.json")):
                    lines.append(hashlib.sha256((root/name).read_bytes()).hexdigest()+"  "+name)
                (root/"SHA256SUMS").write_text("\n".join(lines)+"\n")
                if tamper:
                    (root/tamper).write_bytes(b"tampered")
                return b""
            raise AssertionError(args)
        with patch("paper_pov.github_sealed_bundle_readback.build_bundle",return_value={"schema":"fixture"}):
            return read_run("owner/repo","123",runner=fake_runner)

    def test_successful_main_run_and_checksum_bound_delivery(self):
        actual=self._run()
        self.assertEqual(actual["source_run_id"],123)
        self.assertFalse(actual["publisher_authenticated"])
        self.assertEqual(actual["bundle"],{"schema":"fixture"})
        self.assertTrue(actual["sealed"])
        self.assertFalse(actual["watch_delivery_authorized"])

    def test_corrupt_downloaded_artifact_rejected(self):
        for name in ("latest.json","scoreboard.json","ledger.json","slot_receipt.json"):
            with self.subTest(name=name), self.assertRaisesRegex(ValueError,"checksum mismatch"):
                self._run(tamper=name)

    def test_untrusted_workflow_origin_rejected(self):
        with self.assertRaisesRegex(ValueError,"untrusted paper workflow origin"):
            self._run(origin="pull_request")


    def test_real_legacy_artifact_contract_is_readable_without_fake_watch(self):
        actual=self._run(legacy=True)
        self.assertEqual(actual["artifact_status"],"CHECKSUM_VERIFIED_LEGACY_NO_RECEIPT")
        self.assertFalse(actual["sealed"])
        self.assertFalse(actual["watch_delivery_authorized"])
        self.assertFalse(actual["publisher_authenticated"])

    def test_legacy_artifact_checksum_corruption_rejected(self):
        with self.assertRaisesRegex(ValueError,"checksum mismatch"):
            self._run(legacy=True,tamper="latest.json")

    def test_sealed_bundle_checksum_corruption_rejected(self):
        with self.assertRaisesRegex(ValueError,"sealed artifact checksum mismatch"):
            self._run(tamper="sealed-http-bundle.json")

if __name__=="__main__":
    unittest.main()
