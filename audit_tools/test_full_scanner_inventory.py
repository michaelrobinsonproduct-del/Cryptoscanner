"""Offline fail-closed pagination tests for repository inventory (no network)."""
import unittest
from unittest.mock import patch
from audit_tools.full_scanner_inventory import gh_pages

class PaginationTests(unittest.TestCase):
    def test_multiple_pages_are_all_included(self):
        with patch("audit_tools.full_scanner_inventory.gh", side_effect=[list(range(100)), [100,101]]) as mocked:
            result=gh_pages("repos/owner/repo/branches")
        self.assertEqual(len(result),102)
        self.assertEqual(result[-2:],[100,101])
        self.assertIn("page=2",mocked.call_args_list[-1].args[0])

    def test_full_last_page_requires_empty_followup(self):
        with patch("audit_tools.full_scanner_inventory.gh", side_effect=[list(range(100)), []]):
            self.assertEqual(len(gh_pages("repos/owner/repo/pulls?state=open")),100)

    def test_api_error_aborts(self):
        with patch("audit_tools.full_scanner_inventory.gh", return_value={"error":"403"}):
            with self.assertRaisesRegex(RuntimeError,"pagination failure"):
                gh_pages("repos/owner/repo/branches")

    def test_cap_aborts_instead_of_truncating(self):
        with patch("audit_tools.full_scanner_inventory.gh", return_value=list(range(100))):
            with self.assertRaisesRegex(RuntimeError,"limit reached"):
                gh_pages("repos/owner/repo/branches",max_pages=2)

if __name__=="__main__":
    unittest.main()
