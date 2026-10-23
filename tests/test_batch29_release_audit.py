"""Batch 29 consolidated, offline-only release readiness audit.

This checks test wiring and fail-closed release boundaries; it never invokes
live scanners, GitHub delivery, production storage or deployment.
"""
import pathlib
import unittest

ROOT=pathlib.Path(__file__).resolve().parents[1]
WORKFLOW=ROOT/".github/workflows/scanner-storage-safety.yml"
TEST_FILES=(
    "test_storage_safety.py",
    "test_storage_inventory_edge_cases.py",
    "test_dex_reliability.py",
    "test_kraken_freshness.py",
    "test_shadow_learning_guards.py",
    "test_offline_replay.py",
    "test_offline_scoring_comparison.py",
    "test_execution_contract.py",
    "test_execution_acceptance_fixtures.py",
    "test_rollback_rehearsal.py",
    "test_batch22_delivery_recovery.py",
    "test_batch22_source_recovery.py",
    "test_batch23_readiness.py",
    "test_batch23_reporting_reliability.py",
    "test_batch24_outbox.py",
    "test_batch24_crash_recovery.py",
    "test_batch25_reconciliation.py",
    "test_batch25_integrity.py",
    "test_batch26_isolated_readiness.py",
    "test_batch26_failure_matrix.py",
    "test_batch27_release_guards.py",
    "test_batch27_final_acceptance.py",
    "test_batch28_evidence_integrity.py",
)
FIXTURE_MODULES=(
    "simple_scanner/fixture_delivery_outbox.py",
    "simple_scanner/fixture_receipt_reconciliation.py",
)
RELEASE_BLOCKERS=(
    "independent live backup",
    "genuine production-history replay",
    "live rollback",
    "production delivery integration",
)

class ReleaseReadinessAudit(unittest.TestCase):
    def test_regression_families_are_wired_to_ci(self):
        workflow=WORKFLOW.read_text()
        for name in TEST_FILES:
            with self.subTest(test=name):
                self.assertTrue((ROOT/"tests"/name).is_file())
                self.assertIn("-p '"+name+"'",workflow)
        self.assertIn("test_batch29_release_audit.py",workflow)

    def test_fixture_modules_not_imported_by_production_executor(self):
        executor=(ROOT/"simple_scanner/execute_once.py").read_text()
        for module in FIXTURE_MODULES:
            self.assertNotIn(pathlib.Path(module).stem,executor)

    def test_audit_keeps_release_gates_explicitly_blocked(self):
        decision=(ROOT/"docs/batch29_release_audit.md").read_text().lower()
        for gate in RELEASE_BLOCKERS:
            with self.subTest(gate=gate):
                self.assertIn(gate,decision)
        self.assertIn("release decision: blocked",decision)
        self.assertIn("fixture-only",decision)

if __name__=="__main__":
    unittest.main()
