"""Adversarial offline evidence validation; never contacts GitHub or Kraken."""
import hashlib
import json
import tempfile
import unittest
from pathlib import Path
from research.verify_marketwide_artifacts import verify_artifacts, FILES, LEDGER

HEAD = "a" * 40
LEDGER_SHA = "b" * 64
LEDGER_COMMIT = "c" * 40


def write_json(path, data):
    path.write_text(json.dumps(data, sort_keys=True) + "\n")


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def fixture(directory):
    base = Path(directory)
    ledger = {"sha256": LEDGER_SHA, "generation": 51}
    window = {"eligible": 30872, "matured": 0, "immature": 30872,
              "abstain_gap": 0, "movers_20": 0, "movers_30": 0,
              "watch_eligible": 584, "watch_immature": 584,
              "watch_abstain_gap": 0, "watch_matured": 0,
              "watch_20": 0, "watch_30": 0,
              "watch_false_positive_20": 0, "watch_false_positive_30": 0,
              "missed_20": 0, "missed_30": 0}
    episode_window = {"coverage": {
        **{k: window[k] for k in ("eligible","matured","immature","abstain_gap",
                                   "movers_20","watch_eligible","watch_immature",
                                   "watch_abstain_gap","watch_matured",
                                   "watch_false_positive_20","watch_false_positive_30",
                                   "missed_20","missed_30")},
        "movers": 0, "watch_positive_20": 0, "watch_positive": 0,
        **{k: 0 for k in ("abstain_conflicting_quotes", "abstain_future_entry_quotes",
                         "abstain_no_future_observation", "abstain_missing_horizon_anchor",
                         "abstain_stale_entry", "abstain_discontinuous_path",
                         "watch_abstain_conflicting_quotes", "watch_abstain_future_entry_quotes",
                         "watch_abstain_no_future_observation", "watch_abstain_missing_horizon_anchor",
                         "watch_abstain_stale_entry", "watch_abstain_discontinuous_path")}},
        "unique_mover_episodes_20": 0, "unique_mover_episodes": 0,
        "watch_captured_episodes_20": 0, "watch_captured_episodes": 0,
        "watch_first_entry_episodes_20": 0, "watch_late_only_episodes_20": 0,
        "watch_first_entry_episodes_30": 0, "watch_late_only_episodes_30": 0,
        "missed_mover_episodes_20": 0, "missed_mover_episodes_30": 0,
        "watch_first_entry_recall_20": None, "watch_first_entry_recall_30": None,
        **{"episode_first_entry_feature_distributions" + suffix:
           {lag: {"n": 0, "distinct_pairs": 0} for lag in ("30m","60m","180m")}
           for suffix in ("", "_20")},
        **{"episode_first_entry_feature_coverage_" + suffix:
           {lag: {"episodes": 0, "with_asof_feature": 0,
                  "without_asof_feature": 0, "distinct_covered_pairs": 0,
                  "covered_fraction": None} for lag in ("30m","60m","180m")}
           for suffix in ("20","30")}}
    outcomes = {"horizons": {h: dict(window) for h in ("1","6","24","48")},
                "observed_run_count": 51, "observed_entry_count": 30872,
                "source_authenticated": False, "complete_market_history": False,
                "eligible_for_model_promotion": False}
    episodes = {"horizons": {h: json.loads(json.dumps(episode_window)) for h in ("1","6","24","48")},
                "source": {"ledger_sha256": LEDGER_SHA, "generation": 51,
                           "runs": 51, "observations": 30872,
                           "source_authenticated": False,
                           "complete_market_history": False,
                           "eligible_for_model_promotion": False}}
    write_json(base / LEDGER, ledger)
    write_json(base / FILES[0], outcomes)
    write_json(base / FILES[1], episodes)
    provenance = {"research_source_commit": HEAD,
                  "paper_ledger_branch_commit": LEDGER_COMMIT,
                  "verified_ledger_export_sha256": digest(base / LEDGER),
                  "outcome_report_sha256": digest(base / FILES[0]),
                  "episode_report_sha256": digest(base / FILES[1]),
                  "observed_run_count": 51, "observed_entry_count": 30872,
                  "source_authenticated": False,
                  "complete_market_history": False,
                  "eligible_for_model_promotion": False}
    write_json(base / FILES[2], provenance)
    reseal(base)


def reseal(base):
    (base / "marketwide-SHA256SUMS").write_text(
        "".join(digest(base / name) + "  " + name + "\n" for name in FILES))


class ArtifactContractTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        self.base = Path(self.tmp.name)
        fixture(self.base)

    def test_valid_readonly_evidence(self):
        self.assertEqual(verify_artifacts(self.base, HEAD, LEDGER_COMMIT)["reports_checked"], 3)

    def test_missing_report_fails(self):
        (self.base / FILES[1]).unlink()
        with self.assertRaisesRegex(ValueError, "missing"):
            verify_artifacts(self.base, HEAD, LEDGER_COMMIT)

    def test_missing_checksum_file_fails(self):
        (self.base / "marketwide-SHA256SUMS").unlink()
        with self.assertRaisesRegex(ValueError, "missing"):
            verify_artifacts(self.base, HEAD, LEDGER_COMMIT)

    def test_tampered_report_fails_even_with_valid_provenance(self):
        (self.base / FILES[0]).write_text("{}")
        with self.assertRaisesRegex(ValueError, "checksum mismatch"):
            verify_artifacts(self.base, HEAD, LEDGER_COMMIT)

    def test_self_resealed_report_without_provenance_update_fails(self):
        (self.base / FILES[0]).write_text("{}")
        reseal(self.base)
        with self.assertRaisesRegex(ValueError, "provenance checksum mismatch"):
            verify_artifacts(self.base, HEAD, LEDGER_COMMIT)

    def test_wrong_remote_ledger_commit_fails(self):
        with self.assertRaisesRegex(ValueError, "remote ledger commit mismatch"):
            verify_artifacts(self.base, HEAD, "d"*40)

    def test_wrong_exact_head_fails(self):
        with self.assertRaisesRegex(ValueError, "source head mismatch"):
            verify_artifacts(self.base, "d"*40, LEDGER_COMMIT)

    def test_mismatched_ledger_identity_fails_even_if_resealed(self):
        e = json.loads((self.base / FILES[1]).read_text())
        e["source"]["generation"] = 50
        write_json(self.base / FILES[1], e)
        p = json.loads((self.base / FILES[2]).read_text())
        p["episode_report_sha256"] = digest(self.base / FILES[1])
        write_json(self.base / FILES[2], p)
        reseal(self.base)
        with self.assertRaisesRegex(ValueError, "ledger identity mismatch"):
            verify_artifacts(self.base, HEAD, LEDGER_COMMIT)

    def test_false_authentication_claim_fails_even_if_resealed(self):
        p = json.loads((self.base / FILES[2]).read_text())
        p["source_authenticated"] = True
        write_json(self.base / FILES[2], p)
        reseal(self.base)
        with self.assertRaisesRegex(ValueError, "claims authentication"):
            verify_artifacts(self.base, HEAD, LEDGER_COMMIT)

    def test_resealed_cross_report_mismatch_rejected(self):
        e = json.loads((self.base / FILES[1]).read_text())
        e["horizons"]["1"]["coverage"]["missed_30"] = 1
        write_json(self.base / FILES[1], e)
        p = json.loads((self.base / FILES[2]).read_text())
        p["episode_report_sha256"] = digest(self.base / FILES[1])
        write_json(self.base / FILES[2], p)
        reseal(self.base)
        with self.assertRaisesRegex(ValueError, "cross-report outcome mismatch"):
            verify_artifacts(self.base, HEAD, LEDGER_COMMIT)

    def test_resealed_missing_horizon_rejected(self):
        e = json.loads((self.base / FILES[1]).read_text())
        del e["horizons"]["48"]
        write_json(self.base / FILES[1], e)
        p = json.loads((self.base / FILES[2]).read_text())
        p["episode_report_sha256"] = digest(self.base / FILES[1])
        write_json(self.base / FILES[2], p)
        reseal(self.base)
        with self.assertRaisesRegex(ValueError, "missing or unexpected evaluation horizon"):
            verify_artifacts(self.base, HEAD, LEDGER_COMMIT)

    def test_resealed_nonfinite_research_statistic_rejected(self):
        e = json.loads((self.base / FILES[1]).read_text())
        e["horizons"]["1"]["pre_entry_price_feature_distributions"] = {"60m": {"mean": float("nan")}}
        write_json(self.base / FILES[1], e)
        p = json.loads((self.base / FILES[2]).read_text())
        p["episode_report_sha256"] = digest(self.base / FILES[1])
        write_json(self.base / FILES[2], p)
        reseal(self.base)
        with self.assertRaisesRegex(ValueError, "nonfinite research JSON"):
            verify_artifacts(self.base, HEAD, LEDGER_COMMIT)

    def reseal_episode_change(self, mutate):
        e = json.loads((self.base / FILES[1]).read_text())
        mutate(e["horizons"]["1"])
        write_json(self.base / FILES[1], e)
        p = json.loads((self.base / FILES[2]).read_text())
        p["episode_report_sha256"] = digest(self.base / FILES[1])
        write_json(self.base / FILES[2], p)
        reseal(self.base)

    def test_resealed_late_watch_claim_cannot_forge_first_entry_capture(self):
        self.reseal_episode_change(lambda h: h.update(
            watch_first_entry_episodes_30=1))
        with self.assertRaisesRegex(ValueError, "first-entry versus late WATCH"):
            verify_artifacts(self.base, HEAD, LEDGER_COMMIT)

    def test_resealed_gap_reason_cannot_disagree_with_unknown_denominator(self):
        self.reseal_episode_change(lambda h: h["coverage"].update(
            abstain_no_future_observation=1))
        with self.assertRaisesRegex(ValueError, "gap-reason partition"):
            verify_artifacts(self.base, HEAD, LEDGER_COMMIT)

    def test_resealed_watch_gap_reason_cannot_exceed_market_reason(self):
        self.reseal_episode_change(lambda h: h["coverage"].update(
            watch_abstain_stale_entry=1))
        with self.assertRaisesRegex(ValueError, "gap-reason partition"):
            verify_artifacts(self.base, HEAD, LEDGER_COMMIT)

    def test_resealed_first_entry_recall_cannot_be_fabricated(self):
        self.reseal_episode_change(lambda h: h.update(watch_first_entry_recall_30=0.5))
        with self.assertRaisesRegex(ValueError, "first-entry WATCH recall"):
            verify_artifacts(self.base, HEAD, LEDGER_COMMIT)

    def test_resealed_feature_coverage_cannot_invent_history(self):
        self.reseal_episode_change(lambda h: h["episode_first_entry_feature_coverage_20"]["60m"].update(
            with_asof_feature=1, without_asof_feature=0, covered_fraction=1.0))
        with self.assertRaisesRegex(ValueError, "first-entry feature coverage"):
            verify_artifacts(self.base, HEAD, LEDGER_COMMIT)

    def test_resealed_feature_coverage_cannot_hide_duplicate_pair_count(self):
        self.reseal_episode_change(lambda h: h["episode_first_entry_feature_distributions"]["30m"].update(
            distinct_pairs=1))
        with self.assertRaisesRegex(ValueError, "first-entry feature coverage"):
            verify_artifacts(self.base, HEAD, LEDGER_COMMIT)

    def test_workflow_only_uploads_after_successful_verification(self):
        workflow = (Path(__file__).resolve().parents[1] /
                    ".github/workflows/research-marketwide-checks.yml").read_text()
        verification = workflow.index("python -m research.verify_marketwide_artifacts --directory /tmp")
        upload = workflow.index("- uses: actions/upload-artifact@v4")
        self.assertLess(verification, upload)
        self.assertIn("if: success()", workflow[upload:])
        self.assertIn("if-no-files-found: error", workflow[upload:])
        self.assertNotIn("if: always()", workflow[upload:])

    def test_workflow_runs_contract_tests_before_replay(self):
        workflow = (Path(__file__).resolve().parents[1] /
                    ".github/workflows/research-marketwide-checks.yml").read_text()
        tests = workflow.index("research.test_verify_marketwide_artifacts -v")
        replay = workflow.index("python -m paper_pov.segmented_repository export-git")
        self.assertLess(tests, replay)

    def test_repeated_or_unexpected_checksums_fail(self):
        with (self.base / "marketwide-SHA256SUMS").open("a") as f:
            f.write(digest(self.base / FILES[0]) + "  " + FILES[0] + "\n")
        with self.assertRaisesRegex(ValueError, "repeated"):
            verify_artifacts(self.base, HEAD, LEDGER_COMMIT)


if __name__ == "__main__":
    unittest.main()
