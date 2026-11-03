"""D2 downloaded-artifact cross-readback regression."""
import hashlib
import json
from pathlib import Path
import tempfile
import unittest
import zipfile
from paper_pov.artifact_audit import audit


class ArtifactAuditTests(unittest.TestCase):
    def test_verified_pair_and_reject_tampered_candidate(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            quote = {"pair": "XBTUSD", "symbol": "XBT/USD",
                     "observed_at": "2026-11-03T19:58:33+00:00", "price": 50000}
            scan = {"as_of": "2026-11-03T19:58:41+00:00",
                    "eligible_pairs": 1, "observations": [quote], "watch": [quote]}
            board = {"generation": 1, "ledger_sha256": "a" * 64}
            state = {"generation": 1, "sha256": "a" * 64}
            report = {"run_id": "123", "source_sha": "b" * 40,
                      "ledger_commit": "c" * 40, "ledger_sha256": "a" * 64,
                      "ledger_generation": 1, "eligible_pairs": 1,
                      "observed_markets": 1, "buy_approved": False,
                      "production_applied": False,
                      "candidates": [{"rank": 1, "status": "WATCH_PAPER_ONLY", "symbol": "XBT/USD", "price_usd": 50000,
                                      "quote_observed_at": quote["observed_at"]}]}
            def pack(name, payload):
                path = root / name
                checksums = []
                with zipfile.ZipFile(path, "w") as z:
                    for filename, value in payload.items():
                        data = json.dumps(value).encode() if filename.endswith(".json") else value.encode()
                        z.writestr(filename, data)
                        checksums.append(hashlib.sha256(data).hexdigest() + "  " + filename)
                    z.writestr("SHA256SUMS", "\n".join(checksums) + "\n")
                return path
            ledger = pack("ledger.zip", {"latest.json": scan, "scoreboard.json": board,
                                         "ledger.json": state})
            def publication():
                return pack("results.zip", {"results.json": report, "results.md": "paper"})
            results = publication()
            proof = audit(ledger, results, run_id="123", source_sha="b" * 40,
                          ledger_commit="c" * 40)
            self.assertEqual(proof["max_client_quote_age_seconds"], 8)
            self.assertFalse(proof["published_quote_evidence"])
            self.assertFalse(proof["certified"])
            self.assertFalse(proof["client_quote_evidence_verified"])
            self.assertEqual(proof["status"], "ABSTAIN_LEGACY_QUOTE_EVIDENCE")
            report["candidates"][0]["symbol"] = "ETH/USD"
            results = publication()
            with self.assertRaisesRegex(ValueError, "membership/order"):
                audit(ledger, results)
            report["candidates"][0]["symbol"] = "XBT/USD"
            report["quote_evidence"] = [quote]
            results = publication()
            verified = audit(ledger, results)
            self.assertTrue(verified["certified"])
            self.assertTrue(verified["client_quote_evidence_verified"])
            report.pop("quote_evidence")
            report["candidates"] = None
            results = publication()
            with self.assertRaisesRegex(ValueError, "Missing WATCH arrays"):
                audit(ledger, results)
            report["candidates"] = [{"symbol": "XBT/USD", "price_usd": 50000,
                                     "quote_observed_at": quote["observed_at"]}]
            with self.assertRaisesRegex(ValueError, "identity mismatch"):
                audit(ledger, results, run_id="124", source_sha="b" * 40,
                      ledger_commit="c" * 40)
            report["candidates"][0]["status"] = "BUY"
            with self.assertRaisesRegex(ValueError, "rank/status mismatch"):
                audit(ledger, publication(), run_id="123", source_sha="b" * 40,
                      ledger_commit="c" * 40)
            report["candidates"][0]["status"] = "WATCH_PAPER_ONLY"
            report["candidates"][0]["price_usd"] = 1
            results = publication()
            with self.assertRaisesRegex(ValueError, "lacks retained quote"):
                audit(ledger, results)


if __name__ == "__main__":
    unittest.main()
