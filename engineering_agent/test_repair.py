import unittest
from repair import valid_path, validate_changes

class GuardTests(unittest.TestCase):
    def test_allows_scanner_python(self):
        self.assertTrue(valid_path("simple_scanner/scan.py"))
        self.assertFalse(valid_path("simple_scanner/../secrets.py"))
        self.assertFalse(valid_path(".github/workflows/test.yml"))
        self.assertFalse(valid_path("simple_scanner/config.env"))

    def test_rejects_duplicate(self):
        with self.assertRaises(ValueError):
            validate_changes([{"path": "simple_scanner/scan.py", "content": "a"},
                              {"path": "simple_scanner/scan.py", "content": "b"}])

    def test_rejects_empty(self):
        with self.assertRaises(ValueError):
            validate_changes([])

    def test_accepts_bounded(self):
        self.assertEqual(len(validate_changes([{"path": "simple_scanner/scan.py",
                                                "content": "print(1)"}])), 1)

if __name__ == "__main__":
    unittest.main()
