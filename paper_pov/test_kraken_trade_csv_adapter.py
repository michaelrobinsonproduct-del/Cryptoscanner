import hashlib
import tempfile
import unittest
from pathlib import Path
from paper_pov.kraken_trade_csv_adapter import parse_trade_csv, convert_pinned_csv

SCHEMA = {"format": "kraken_trade_csv_explicit_v1", "timestamp_unit": "seconds",
          "columns": {"timestamp": 0, "price": 1, "volume": 2},
          "header": False, "column_count": 3}
RAW = b"1767225600,100,1\n1767225660,105,2\n1767226200,99,3\n"


class KrakenTradeCsvTests(unittest.TestCase):
    def test_strict_raw_csv_to_ohlcv_with_gap(self):
        import copy
        manifest = {"schema": "kraken_archive_manifest_v1", "source": "Kraken",
                    "partitions": [{"file": "trades.csv", "size_bytes": len(RAW),
                                    "sha256": hashlib.sha256(RAW).hexdigest()}]}
        with tempfile.TemporaryDirectory() as root:
            (Path(root) / "trades.csv").write_bytes(RAW)
            result = convert_pinned_csv(manifest, root, partition_file="trades.csv",
                                        pair="XUSD", schema=SCHEMA)
            self.assertEqual(result["parsed_trade_count"], 3)
            self.assertEqual(result["bar_count"], 2)
            self.assertEqual(result["bars"][0]["close"], 105)
            self.assertFalse(result["source_authenticated"])
            self.assertFalse(result["schema_authenticated"])

    def test_unit_mapping_required(self):
        with self.assertRaisesRegex(ValueError, "unit"):
            parse_trade_csv(RAW, pair="XUSD", schema={**SCHEMA, "timestamp_unit": "auto"})

    def test_missing_or_ambiguous_mapping_rejected(self):
        with self.assertRaises(ValueError):
            parse_trade_csv(RAW, pair="XUSD",
                            schema={**SCHEMA, "columns": {"timestamp": 0, "price": 0, "volume": 2}})

    def test_bad_rows_and_order_rejected(self):
        with self.assertRaisesRegex(ValueError, "width"):
            parse_trade_csv(b"1767225600,100\n", pair="XUSD", schema=SCHEMA)
        from paper_pov.verified_trade_bars import trades_to_bars
        with self.assertRaisesRegex(ValueError, "Out-of-order"):
            trades_to_bars(parse_trade_csv(RAW.splitlines(keepends=True)[::-1][0] +
                                           RAW.splitlines(keepends=True)[0], pair="XUSD",
                                           schema=SCHEMA), pair="XUSD")

    def test_tampered_pinned_csv_rejected(self):
        manifest = {"schema": "kraken_archive_manifest_v1", "source": "Kraken",
                    "partitions": [{"file": "trades.csv", "size_bytes": len(RAW),
                                    "sha256": hashlib.sha256(RAW).hexdigest()}]}
        with tempfile.TemporaryDirectory() as root:
            (Path(root) / "trades.csv").write_bytes(RAW.replace(b"105", b"106"))
            with self.assertRaisesRegex(ValueError, "checksum"):
                convert_pinned_csv(manifest, root, partition_file="trades.csv",
                                   pair="XUSD", schema=SCHEMA)


if __name__ == "__main__":
    unittest.main()
