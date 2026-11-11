import unittest
from research.source_qualified_outcomes import qualify


def row(i, bid="100", ask="100", observed_delay=2):
    return {"pair": "XBTUSD", "event_at": 1700000000 + i * 300,
            "first_observed_at": 1700000002 + i * 300 + observed_delay,
            "source_sha256": "a" * 64, "bid": bid, "ask": ask}


class QualifiedOutcomeTests(unittest.TestCase):
    def test_positive_observed_path(self):
        rows = [row(i, bid="131" if i == 7 else "100") for i in range(13)]
        self.assertTrue(qualify(rows[0], rows[1:])["ge30pct"])

    def test_negative_observed_path(self):
        rows = [row(i) for i in range(13)]
        self.assertFalse(qualify(rows[0], rows[1:])["ge30pct"])

    def test_missing_slot_abstains(self):
        rows = [row(i) for i in range(13) if i != 5]
        self.assertEqual(qualify(rows[0], rows[1:])["status"], "ABSTAIN_INCOMPLETE")

    def test_duplicate_slot_abstains(self):
        rows = [row(i) for i in range(13)]
        rows[5] = row(4)
        self.assertEqual(qualify(rows[0], rows[1:])["status"], "ABSTAIN_PATH_GAP")

    def test_stale_event_abstains(self):
        rows = [row(i) for i in range(13)]
        rows[5]["first_observed_at"] += 601
        self.assertEqual(qualify(rows[0], rows[1:])["status"], "ABSTAIN_OBSERVATION_TIME")

    def test_missing_receipt_abstains(self):
        rows = [row(i) for i in range(13)]
        rows[4]["source_sha256"] = ""
        self.assertEqual(qualify(rows[0], rows[1:])["status"], "ABSTAIN_SOURCE_RECEIPT")

    def test_cross_market_abstains(self):
        rows = [row(i) for i in range(13)]
        rows[8]["pair"] = "ETHUSD"
        self.assertEqual(qualify(rows[0], rows[1:])["status"], "ABSTAIN_PATH_GAP")


if __name__ == "__main__":
    unittest.main()
