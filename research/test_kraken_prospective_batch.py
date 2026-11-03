"""Adversarial offline tests: source receipts, fail-closed coverage, no promotion."""
import hashlib
import json
import tempfile
import unittest
from pathlib import Path
from urllib.parse import parse_qs, urlparse

from research.kraken_prospective_batch import collect


NOW = 1700000010.0


def fake_transport(path, *, stale=None, invalid=None):
    parsed = urlparse(path)
    pair = parse_qs(parsed.query)["pair"][0]
    if invalid == pair:
        return b'{"error":["EQuery:Invalid asset pair"],"result":{}}'
    event = NOW - 1000 if stale == pair else NOW - 10
    if parsed.path.endswith("/Depth"):
        result = {"bids": [["100", "2", event]], "asks": [["101", "3", event]]}
        return json.dumps({"error": [], "result": {pair: result}}).encode()
    if parsed.path.endswith("/Trades"):
        result = [["100", "0.5", event, "b", "l", ""]]
        return json.dumps({"error": [], "result": {pair: result, "last": "42"}}).encode()
    raise AssertionError("unexpected path")


class BatchTests(unittest.TestCase):
    def run_batch(self, pairs, transport=fake_transport, **kwargs):
        temp = tempfile.TemporaryDirectory()
        self.addCleanup(temp.cleanup)
        target = Path(temp.name) / "batch"
        result = collect(pairs, target, transport=transport, clock=lambda: NOW,
                         monotonic=lambda: 0, sleep=lambda _: None, **kwargs)
        return result, target

    def test_two_market_real_raw_receipts_and_coverage(self):
        result, target = self.run_batch(["XBTUSD", "ETHUSD"])
        self.assertEqual((result["pairs_requested"], result["pairs_eligible"]), (2, 2))
        self.assertEqual(result["certified_first_entry_episodes"], 0)
        self.assertIsNone(result["held_out_lift"])
        self.assertFalse(result["historical_first_observed_recovered"])
        self.assertFalse(result["production_applied"])
        self.assertEqual(json.loads((target / "manifest.json").read_text()), result)
        for entry in result["entries"]:
            self.assertEqual(entry["status"], "ELIGIBLE")
            self.assertEqual(len(entry["raw"]), 2)
            for receipt in entry["raw"]:
                raw = (target / receipt["file"]).read_bytes()
                self.assertEqual(hashlib.sha256(raw).hexdigest(), receipt["sha256"])
                self.assertEqual(len(raw), receipt["bytes"])
            evidence = json.loads((target / entry["evidence_file"]).read_text())
            self.assertTrue(evidence["eligible_point_in_time_snapshot"])
            self.assertEqual(evidence["depth_receipt"]["sha256"], entry["raw"][0]["sha256"])

    def test_stale_market_not_eligible(self):
        result, _ = self.run_batch(["XBTUSD", "ETHUSD"],
                                   transport=lambda p: fake_transport(p, stale="ETHUSD"))
        self.assertEqual((result["pairs_eligible"], result["pairs_stale"]), (1, 1))
        self.assertEqual(result["entries"][1]["status"], "STALE")

    def test_invalid_source_isolated_and_preserves_partial_receipt(self):
        result, target = self.run_batch(["XBTUSD", "ETHUSD", "SOLUSD"],
                                        transport=lambda p: fake_transport(p, invalid="ETHUSD"))
        self.assertEqual((result["pairs_eligible"], result["pairs_invalid"]), (2, 1))
        self.assertEqual(result["entries"][1]["failure_class"], "ValueError")
        self.assertTrue((target / result["entries"][1]["raw"][0]["file"]).exists())
        self.assertEqual(result["entries"][2]["status"], "ELIGIBLE")

    def test_bad_transport_bytes_rejected(self):
        result, _ = self.run_batch(["XBTUSD"], transport=lambda _: "not bytes")
        self.assertEqual(result["pairs_invalid"], 1)
        self.assertEqual(result["entries"][0]["raw"], [])

    def test_budget_skips_without_network(self):
        ticks = iter([0, 0, 181, 182])
        calls = []
        def transport(path):
            calls.append(path)
            return fake_transport(path)
        temp = tempfile.TemporaryDirectory()
        self.addCleanup(temp.cleanup)
        result = collect(["XBTUSD", "ETHUSD"], Path(temp.name) / "batch",
                         transport=transport, clock=lambda: NOW,
                         monotonic=lambda: next(ticks), sleep=lambda _: None)
        self.assertEqual((result["pairs_eligible"], result["pairs_budget_skipped"]), (1, 1))
        self.assertEqual(len(calls), 2)

    def test_duplicate_and_invalid_pair_rejected_before_network(self):
        for pairs in (["XBTUSD", "XBTUSD"], ["XBTUSD&admin=1"], [], ["A"] * 9):
            with self.subTest(pairs=pairs):
                with tempfile.TemporaryDirectory() as d:
                    with self.assertRaises(ValueError):
                        collect(pairs, Path(d) / "batch",
                                transport=lambda _: self.fail("network called"))

    def test_existing_output_cannot_be_overwritten(self):
        with tempfile.TemporaryDirectory() as d:
            directory = Path(d) / "batch"
            directory.mkdir()
            with self.assertRaises(FileExistsError):
                collect(["XBTUSD"], directory, transport=lambda _: self.fail("network called"))

    def test_all_invalid_not_silently_reported_as_coverage(self):
        result, _ = self.run_batch(["XBTUSD", "ETHUSD"],
                                   transport=lambda _: b'{"error":["bad"],"result":{}}')
        self.assertEqual(result["pairs_eligible"], 0)
        self.assertEqual(result["pairs_invalid"], 2)


if __name__ == "__main__":
    unittest.main()
