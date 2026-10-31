import copy
import unittest
from select_inventory_cohorts import EXPECTED_SHA256, select_cohorts


def fixture():
    data = {"archive_verification": {"sha256": EXPECTED_SHA256, "integrity_verified": True},
            "five_minute_members": 4, "five_minute_csv_inventory": []}
    for i, density in enumerate((.05, .2, .4, .8)):
        span = 20000
        n = int(span * density)
        data["five_minute_csv_inventory"].append({"member": f"COIN{i}USD_5.csv",
            "crc_checked": True, "invalid_rows": 0, "adjacent_duplicates": 0,
            "out_of_order_rows": 0, "earliest_epoch": 0,
            "latest_epoch": (span-1)*300, "rows": n,
            "gap_intervals": 1, "uncompressed_bytes": 100000})
    return data


class Tests(unittest.TestCase):
    def test_cross_density_and_no_labels(self):
        result = select_cohorts(fixture(), per_cohort=1)
        self.assertEqual(result["cohort_eligible_counts"], [1, 1, 1, 1])
        self.assertEqual(result["selected_count"], 4)
        self.assertEqual(result["real_labels"], 0)
        self.assertFalse(result["independent_trade_completeness"])

    def test_deterministic_order(self):
        a = fixture()
        b = copy.deepcopy(a)
        b["five_minute_csv_inventory"].reverse()
        self.assertEqual(select_cohorts(a), select_cohorts(b))

    def test_wrong_digest_rejected(self):
        a = fixture(); a["archive_verification"]["sha256"] = "fake"
        with self.assertRaises(ValueError): select_cohorts(a)

    def test_gap_accounting_rejected(self):
        a = fixture(); a["five_minute_csv_inventory"][0]["gap_intervals"] = 20000
        with self.assertRaises(ValueError): select_cohorts(a)

    def test_duplicate_member_rejected(self):
        a = fixture(); a["five_minute_csv_inventory"][1]["member"] = "COIN0USD_5.csv"
        with self.assertRaises(ValueError): select_cohorts(a)

    def test_invalid_crc_rejected(self):
        a = fixture(); a["five_minute_csv_inventory"][0]["crc_checked"] = False
        with self.assertRaises(ValueError): select_cohorts(a)

    def test_invalid_cap_rejected(self):
        with self.assertRaises(ValueError): select_cohorts(fixture(), per_cohort=0)


if __name__ == "__main__": unittest.main()
