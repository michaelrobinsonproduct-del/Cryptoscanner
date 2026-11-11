"""Regression tests for DEX provider rate limiting."""
import unittest
import urllib.error
from unittest.mock import patch
from simple_scanner import dex

class DexRateLimitTests(unittest.TestCase):
    def test_http_429_is_not_retried(self):
        error = urllib.error.HTTPError("https://example.invalid",429,"Too Many Requests",{},None)
        with patch.object(dex.urllib.request,"urlopen",side_effect=error) as opener:
            with self.assertRaises(urllib.error.HTTPError):
                dex.fetch("solana")
            self.assertEqual(opener.call_count,1)
