"""Read-only GitHub artifact transport acceptance with a fake gh CLI."""
import hashlib
import json
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch
from paper_pov.github_sealed_bundle_readback import read_run

class GitHubSealedBundleReadbackTests(unittest.TestCase):
    def _run(self, *, tamper=None, origin="schedule"):
        metadata={"databaseId":123,"status":"completed","conclusion":"success",
                  "event":origin,"headBranch":"main",
                  "workflowName":"Public Kraken Paper POV (scheduled, isolated ledger)",
                  "headSha":"a"*40}
        def fake_runner(args):
            if args[1:3]==["run","view"]:
                return json.dumps(metadata).encode()
            if args[1:3]==["run","download"]:
                root=Path(args[-1])
                for name in ("latest.json","scoreboard.json","ledger.json","slot_receipt.json"):
                    (root/name).write_bytes((name+"-content").encode())
                lines=[]
                for name in ("latest.json","scoreboard.json","ledger.json","slot_receipt.json"):
                    lines.append(hashlib.sha256((root/name).read_bytes()).hexdigest()+"  "+name)
                (root/"SHA256SUMS").write_text("\n".join(lines)+"\n")
                (root/"sealed-http-bundle.json").write_text('{"schema":"fixture"}')
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

    def test_corrupt_downloaded_artifact_rejected(self):
        for name in ("latest.json","scoreboard.json","ledger.json","slot_receipt.json"):
            with self.subTest(name=name), self.assertRaisesRegex(ValueError,"checksum mismatch"):
                self._run(tamper=name)

    def test_untrusted_workflow_origin_rejected(self):
        with self.assertRaisesRegex(ValueError,"untrusted paper workflow origin"):
            self._run(origin="pull_request")

if __name__=="__main__":
    unittest.main()
