import unittest
from research.kraken_prospective_manifest import plan


class ManifestTests(unittest.TestCase):
    def setUp(self):
        self.pairs = [f"P{i:03d}USD" for i in range(48)]

    def test_exact_48_six_bounded_batches(self):
        result = plan({"pairs": self.pairs})
        self.assertEqual(result["batch_count"], 6)
        self.assertEqual([len(x) for x in result["batches"]], [8] * 6)
        self.assertEqual(result["snapshots_collected"], 0)
        self.assertEqual(result["certified_first_entry_episodes"], 0)

    def test_order_independent_receipt(self):
        a = plan({"pairs": self.pairs})
        b = plan({"pairs": list(reversed(self.pairs))})
        self.assertEqual(a, b)

    def test_missing_or_extra_market_abstains(self):
        for pairs in (self.pairs[:-1], self.pairs + ["EXTRAUSD"]):
            with self.assertRaises(ValueError):
                plan({"pairs": pairs})

    def test_duplicates_and_unsafe_identifiers(self):
        for pairs in (self.pairs[:-1] + [self.pairs[0]],
                      self.pairs[:-1] + ["../../BAD"],
                      self.pairs[:-1] + ["ethusd"]):
            with self.assertRaises(ValueError):
                plan({"pairs": pairs})

    def test_bad_schema_and_batch_limit(self):
        for raw in (self.pairs, {"pairs": self.pairs, "verified": True},
                    {"pairs": "XBTUSD"}):
            with self.assertRaises(ValueError):
                plan(raw)
        for size in (0, 9):
            with self.assertRaises(ValueError):
                plan({"pairs": self.pairs}, batch_size=size)


if __name__ == "__main__":
    unittest.main()
