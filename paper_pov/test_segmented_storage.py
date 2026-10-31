"""Storage failure-injection tests. Synthetic data are not real Kraken performance."""
import copy
import datetime as dt
import hashlib
import json
import unittest
import zlib
import base64
import tempfile
from pathlib import Path
from paper_pov import segmented_writer

from paper_pov import ledger, segmented_storage as storage
from paper_pov.test_ledger import synthetic, SHA


def transition(before, minutes):
    report = synthetic(minutes)
    after = ledger.advance(before, report, SHA)
    return after, storage.make_segment(before, after, report, SHA)


class StorageTests(unittest.TestCase):
    def test_lossless_snapshot_and_chain(self):
        state = ledger.empty()
        segments = []
        for offset in (0, 30, 60, 90, 120):
            state, packed = transition(state, offset)
            segments.append(packed)
        packed_state = storage.pack_snapshot(state)
        self.assertEqual(storage.unpack_snapshot(packed_state), state)
        self.assertEqual(storage.replay_segments(segments), state)
        entries = [storage.manifest_entry(s) for s in segments]
        self.assertEqual(storage.verify_manifest_chain(entries, segments), state)

    def test_archive_survives_50h_eviction(self):
        before = ledger.empty()
        middle, first = transition(before, 0)
        last, second = transition(middle, 51 * 60)
        self.assertEqual(last["archived"]["scans"], 1)
        self.assertEqual(len(last["runs"]), 1)
        self.assertEqual(len(last["observations"]), 25)
        self.assertEqual(storage.replay_segments([first, second]), last)
        original = storage.read_segment(first)["report"]
        self.assertEqual(original["observations"], synthetic(0)["observations"])
        self.assertEqual(last["archived"]["gap_abstentions"], 48)

    def test_checkpoint_replay(self):
        first, s1 = transition(ledger.empty(), 0)
        second, s2 = transition(first, 30)
        self.assertEqual(storage.replay_segments([s2], storage.pack_snapshot(first)), second)

    def test_missing_and_duplicate_segments_fail(self):
        first, s1 = transition(ledger.empty(), 0)
        second, s2 = transition(first, 30)
        for items in ([s2], [s1, s1], [s2, s1]):
            with self.subTest(items=len(items)):
                with self.assertRaises(ValueError):
                    storage.replay_segments(items)

    def test_segment_corruption_fails(self):
        first, segment = transition(ledger.empty(), 0)
        corrupt = bytearray(segment)
        corrupt[len(corrupt) // 2] ^= 1
        with self.assertRaises(ValueError):
            storage.read_segment(bytes(corrupt))

    def test_manifest_corruption_and_inventory_fail(self):
        first, s1 = transition(ledger.empty(), 0)
        entry = storage.manifest_entry(s1)
        with self.assertRaisesRegex(ValueError, "inventory"):
            storage.verify_manifest_chain([entry], [])
        wrong = dict(entry, segment_sha256="0" * 64)
        with self.assertRaisesRegex(ValueError, "manifest"):
            storage.verify_manifest_chain([wrong], [s1])

    def test_interrupted_write_not_accepted(self):
        first, segment = transition(ledger.empty(), 0)
        for n in (0, 2, len(segment) // 2, len(segment) - 1):
            with self.subTest(n=n):
                with self.assertRaises(ValueError):
                    storage.read_segment(segment[:n])

    def test_forged_transition_rejected(self):
        first, s1 = transition(ledger.empty(), 0)
        segment = storage.read_segment(s1)
        segment["after_sha256"] = "f" * 64
        with self.assertRaisesRegex(ValueError, "transition"):
            storage.replay_segments([storage.pack_blob(segment, storage.SEGMENT_KIND)])

    def test_wrong_kind_and_noncanonical_fail(self):
        first, segment = transition(ledger.empty(), 0)
        with self.assertRaises(ValueError):
            storage.unpack_blob(segment, storage.SNAPSHOT_KIND)
        payload = json.loads(segment)
        with self.assertRaises(ValueError):
            storage.read_segment(json.dumps(payload, indent=2).encode() + b"junk")

    def test_oversized_packed_and_decompression_bomb_fail(self):
        with self.assertRaisesRegex(ValueError, "oversized"):
            storage.unpack_blob(b"x" * (storage.MAX_PACKED_BYTES + 1), storage.SEGMENT_KIND)
        bomb = {"format": storage.FORMAT, "kind": storage.SEGMENT_KIND,
                "raw_size": 10, "raw_sha256": "a" * 64,
                "payload": base64.b64encode(zlib.compress(b"Z" * 100000)).decode()}
        with self.assertRaises(ValueError):
            storage.unpack_blob(ledger.canonical(bomb), storage.SEGMENT_KIND)

    def test_capacity_15mb_representative_payload_compresses_below_12mb(self):
        # Compression is measured, not an assertion that real steady-state has
        # been measured. This fixture is deliberately synthetic and repetitive.
        fixture = {"observations": [{"run_id": "a" * 64,
                   "pair": "ETHUSD", "at": "2026-10-31T20:30:00+00:00",
                   "price": 1234.56} for _ in range(160000)]}
        raw = len(ledger.canonical(fixture))
        self.assertGreater(raw, 14_772_580)
        packed = storage.pack_blob(fixture, storage.SNAPSHOT_KIND)
        self.assertLess(len(packed), storage.MAX_PACKED_BYTES)
        self.assertEqual(storage.unpack_blob(packed, storage.SNAPSHOT_KIND), fixture)

    def test_immutability_of_original_inputs(self):
        original = ledger.empty()
        saved = copy.deepcopy(original)
        after, segment = transition(original, 0)
        self.assertEqual(original, saved)
        self.assertEqual(storage.read_segment(segment)["before_sha256"], original["sha256"])
        self.assertNotEqual(after["sha256"], original["sha256"])


    def test_100_half_hour_scans_1200_markets_measured_storage(self):
        # 99 historical transitions, then the 100th through the packed writer.
        # Avoid quadratic replays of synthetic history in this bounded CI test.
        # These are synthetic stress measurements, NOT real Kraken outcomes.
        state = ledger.empty()
        for i in range(100):
            report = synthetic(i * 30)
            at = report["as_of"]
            for n in range(len(report["observations"]), 1200):
                report["observations"].append({
                    "pair": "SYNTH%04dUSD" % n, "price": 1.01,
                    "observed_at": at})
            report["observed_markets"] = len(report["observations"])
            if i < 99:
                state = ledger.advance(state, report, SHA, storage.MAX_RAW_BYTES)
            else:
                packed_before = storage.pack_snapshot(state)
                packed, final_segment, score = storage.advance_segmented(
                    packed_before, report, SHA)
        restored = storage.unpack_snapshot(packed)
        raw_size = len(ledger.canonical(restored))
        self.assertEqual(restored["generation"], 100)
        self.assertGreater(raw_size, ledger.MAX_BYTES)
        self.assertLess(len(packed), storage.MAX_PACKED_BYTES)
        self.assertEqual(score["market_observations"], 120000)
        self.assertEqual(storage.read_segment(final_segment)["generation"], 100)
        print("MEASURED_SYNTHETIC_2_PER_HOUR_50H",
              json.dumps({"scans": 100, "markets_per_scan": 1200,
                          "raw_bytes": raw_size, "packed_bytes": len(packed),
                          "limit_bytes": storage.MAX_PACKED_BYTES,
                          "matured_labels": score["matured_labels"],
                          "production_applied": False}, sort_keys=True))

    def test_segmented_transition_does_not_mutate_input(self):
        before = ledger.empty()
        original = storage.pack_snapshot(before)
        next_snapshot, segment, score = storage.advance_segmented(
            original, synthetic(0), SHA)
        self.assertEqual(storage.unpack_snapshot(original), before)
        self.assertEqual(storage.unpack_snapshot(next_snapshot)["generation"], 1)
        self.assertEqual(storage.replay_segments([segment]),
                         storage.unpack_snapshot(next_snapshot))
        self.assertFalse(score["production_applied"])

    def test_atomic_transaction_staging_and_readback(self):
        previous = storage.pack_snapshot(ledger.empty())
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "transaction"
            manifest = segmented_writer.prepare(previous, synthetic(0), SHA, path)
            self.assertEqual(manifest["generation"], 1)
            self.assertEqual(segmented_writer.verify_prepared(previous, path), manifest)
            with self.assertRaises(FileExistsError):
                segmented_writer.prepare(previous, synthetic(0), SHA, path)
            segment = path / manifest["segment_name"]
            data = bytearray(segment.read_bytes())
            data[-10] ^= 1
            segment.write_bytes(data)
            with self.assertRaises(ValueError):
                segmented_writer.verify_prepared(previous, path)

    def test_incomplete_transaction_rejected(self):
        previous = storage.pack_snapshot(ledger.empty())
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "transaction"
            manifest = segmented_writer.prepare(previous, synthetic(0), SHA, path)
            (path / manifest["segment_name"]).unlink()
            with self.assertRaises(ValueError):
                segmented_writer.verify_prepared(previous, path)

if __name__ == "__main__":
    unittest.main()
