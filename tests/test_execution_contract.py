"""Read-only contract checks for isolated manual/cron acceptance fixtures."""
import unittest
from unittest.mock import patch
from simple_scanner import execute_once

class ExecutionContractTests(unittest.TestCase):
    def test_manual_and_cron_share_pipeline(self):
        self.assertEqual(execute_once.MODULES, (
            'simple_scanner.scan', 'simple_scanner.history',
            'simple_scanner.shadow_learning', 'simple_scanner.dex_guard'))
        self.assertEqual(execute_once.REQUIRED,
                         ('SCAN_SUMMARY','WATCH_SUMMARY','HISTORY_PERSISTED'))

    def test_invalid_origin_fails_before_filesystem_access(self):
        with patch.object(execute_once.Path, 'mkdir', side_effect=AssertionError('filesystem touched')):
            with self.assertRaises(ValueError):
                execute_once.execute('unknown')

    def test_shadow_promotion_not_in_execution_pipeline(self):
        self.assertNotIn('simple_scanner.promote', execute_once.MODULES)
        self.assertNotIn('simple_scanner.offline_replay', execute_once.MODULES)
        self.assertNotIn('simple_scanner.offline_scoring_comparison', execute_once.MODULES)

if __name__=='__main__':
    unittest.main()
