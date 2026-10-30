import io
import json
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch
from probe_independent_kraken_trades import probe, run


class FakeResponse:
    status = 200
    headers = {}
    def __init__(self, payload):
        self.data = io.BytesIO(json.dumps(payload).encode())
    def __enter__(self): return self
    def __exit__(self, *args): return False
    def read(self, size): return self.data.read(size)


class RealTradeProbeTests(unittest.TestCase):
    def test_valid_source_still_does_not_prove_history(self):
        p = {"error": [], "result": {"XXBTZUSD": [["100", "1", 1780000000.0, "b", "m", ""]], "last": "1"}}
        r = probe(opener=lambda *a, **k: FakeResponse(p))
        self.assertEqual(r["observed_trade_count"], 1)
        self.assertFalse(r["complete_2026q2_interval_verified"])
        self.assertEqual(r["historical_labels"], 0)

    def test_api_error_fails(self):
        with self.assertRaises(RuntimeError):
            probe(opener=lambda *a, **k: FakeResponse({"error": ["EGeneral:fail"], "result": {}}))

    def test_unexpected_response_fails(self):
        with self.assertRaises(RuntimeError):
            probe(opener=lambda *a, **k: FakeResponse({"error": [], "result": {"last": "1"}}))

    def test_bad_pair_fails_before_network(self):
        with self.assertRaises(ValueError):
            probe(pair="../../secret")

    def test_overwrite_fails_before_network(self):
        with tempfile.TemporaryDirectory() as d:
            p = Path(d) / "report.json"
            p.write_text("keep")
            with self.assertRaises(FileExistsError):
                run(p)
            self.assertEqual(p.read_text(), "keep")


if __name__ == "__main__":
    unittest.main()
