import datetime as dt
import tempfile
import json
import hashlib
from pathlib import Path
import unittest
from paper_pov.verified_trade_bars import trades_to_bars, convert_verified_partition, convert_manifest_partition

START = dt.datetime(2026, 1, 1, tzinfo=dt.timezone.utc)


def trade(minutes, price, volume=1, pair="XUSD"):
    return {"pair": pair, "timestamp": (START + dt.timedelta(minutes=minutes)).isoformat(),
            "price": price, "volume": volume}


class VerifiedTradeBarsTests(unittest.TestCase):
    def test_ohlcv_and_unfilled_gap(self):
        bars = trades_to_bars([trade(0, 100), trade(1, 110, 2),
                               trade(2, 90, 3), trade(10, 105)], pair="XUSD")
        self.assertEqual(len(bars), 2)
        self.assertEqual((bars[0]["open"], bars[0]["high"],
                          bars[0]["low"], bars[0]["close"]), (100, 110, 90, 90))
        self.assertEqual(bars[0]["volume"], 6)
        self.assertEqual(bars[0]["trade_count"], 3)
        self.assertEqual(bars[1]["open_at"], (START + dt.timedelta(minutes=10)).isoformat())

    def test_cross_pair_and_unsorted_rejected(self):
        with self.assertRaisesRegex(ValueError, "Cross-market"):
            trades_to_bars([trade(0, 100, pair="YUSD")], pair="XUSD")
        with self.assertRaisesRegex(ValueError, "Out-of-order"):
            trades_to_bars([trade(2, 100), trade(0, 100)], pair="XUSD")

    def test_bad_trade_values_rejected(self):
        with self.assertRaises(ValueError):
            trades_to_bars([trade(0, 0)], pair="XUSD")
        with self.assertRaises(ValueError):
            trades_to_bars([trade(0, 100, volume=float("nan"))], pair="XUSD")

    def test_verified_partition_receipt_required(self):
        receipt = {"schema": "archive_partition_verification_v1",
                   "status": "BYTES_MATCH_PINNED_MANIFEST",
                   "partitions": [{"file": "XUSD.csv", "sha256": "a" * 64}]}
        result = convert_verified_partition([trade(0, 100)], pair="XUSD",
                                             verification=receipt, partition_file="XUSD.csv")
        self.assertEqual(result["bar_count"], 1)
        self.assertFalse(result["source_authenticated"])
        self.assertFalse(result["qualified_for_learning"])
        with self.assertRaisesRegex(ValueError, "not present"):
            convert_verified_partition([], pair="XUSD", verification=receipt,
                                       partition_file="YUSD.csv")


    def test_end_to_end_manifest_verified_jsonl_partition(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            data = (json.dumps(trade(0, 100)) + '\n' +
                    json.dumps(trade(1, 105)) + '\n').encode()
            (root / 'XUSD.jsonl').write_bytes(data)
            manifest = {'schema': 'kraken_archive_manifest_v1', 'source': 'Kraken',
                        'partitions': [{'file': 'XUSD.jsonl', 'size_bytes': len(data),
                                        'sha256': hashlib.sha256(data).hexdigest()}]}
            result = convert_manifest_partition(manifest, root,
                                                partition_file='XUSD.jsonl', pair='XUSD')
            self.assertEqual(result['bar_count'], 1)
            self.assertEqual(result['bars'][0]['close'], 105)
            self.assertFalse(result['qualified_for_learning'])
            (root / 'XUSD.jsonl').write_bytes(data.replace(b'105', b'106'))
            with self.assertRaisesRegex(ValueError, 'checksum'):
                convert_manifest_partition(manifest, root,
                                           partition_file='XUSD.jsonl', pair='XUSD')

if __name__ == "__main__":
    unittest.main()
