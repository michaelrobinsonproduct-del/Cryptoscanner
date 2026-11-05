import unittest
from paper_pov.github_delivery_projection import project_delivery, project_published_result

SHA = "a" * 40
BASE = {"source_run_id": 123, "source_sha": SHA,
        "watch_delivery_authorized": False, "publisher_authenticated": False}


class DeliveryProjectionTests(unittest.TestCase):
    def test_sealed_historical_readback_never_becomes_live_watch(self):
        report = {"watch": [{"pair": "TAOUSD", "rank": 1}], "eligible_pairs": 605,
                  "matched_tickers": 605, "observed_markets": 602, "ohlc_screened": 600}
        transport = {**BASE, "sealed": True,
                     "bundle": {"schema": "paper_sealed_bundle_v1",
                                "receipt_json": __import__("json").dumps(report),
                                "candidate_snapshot": {"watch": report["watch"]}}}
        projected = project_delivery(transport)
        self.assertEqual(projected["historical_watch_count"], 1)
        self.assertEqual(projected["historical_coverage"]["observed_markets"], 602)
        self.assertEqual(projected["live_watch"], [])
        self.assertFalse(projected["live_watch_authorized"])
        self.assertTrue(projected["single_writer_read_only"])

    def test_checksum_only_legacy_exposes_no_unverified_watch(self):
        result = project_delivery({**BASE, "sealed": False,
                                   "artifact_status": "CHECKSUM_VERIFIED_LEGACY_NO_RECEIPT",
                                   "scoreboard": {"watch_count": 12}})
        self.assertEqual(result["status"], "LEGACY_CHECKSUM_ONLY")
        self.assertIsNone(result["historical_watch_count"])
        self.assertEqual(result["live_watch"], [])

    def test_inconsistent_sealed_candidate_projection_rejected(self):
        import json
        transport = {**BASE, "sealed": True,
                     "bundle": {"schema": "paper_sealed_bundle_v1",
                                "receipt_json": json.dumps({"watch": [{"pair": "TAOUSD"}]}),
                                "candidate_snapshot": {"watch": []}}}
        with self.assertRaisesRegex(ValueError, "inconsistent"):
            project_delivery(transport)

    def test_d_writer_recovery_reconciliation_is_separate_historical_cohort(self):
        base = {**BASE, "sealed": False, "artifact_status": "CHECKSUM_VERIFIED_LEGACY_NO_RECEIPT", "scoreboard": {}}
        recovery = {"status": "WRITER_CHECKSUM_ONLY", "remote_downloaded": True,
                    "ledger_writer_invoked": False, "production_applied": False,
                    "independently_authenticated": False, "run_id": "456", "source_sha": "b"*40,
                    "persisted_paper": {"ledger_generation": 7, "scan_status": "ABSTAIN_STALE",
                                        "live_replay_performed": False},
                    "remote_ledger_reconciliation": {"status": "UNAVAILABLE",
                        "reason": "REMOTE_LEDGER_QUERY_FAILED",
                        "independently_authenticated": False, "production_applied": False}}
        result = project_delivery(base, recovery)
        self.assertEqual(result["writer_reconciliation_status"], "UNAVAILABLE")
        self.assertEqual(result["writer_recovery"]["ledger_generation"], 7)
        self.assertEqual(result["writer_recovery"]["source_run_id"], 456)
        self.assertFalse(result["writer_recovery"]["same_scan_as_delivery"])
        self.assertEqual(result["live_watch"], [])
        for status, remote in (("MATCH", "c"*64), ("DIVERGED", "d"*64)):
            with self.subTest(status=status):
                recovery["remote_ledger_reconciliation"] = {
                    "status": status, "recovered_sha256": "c"*64, "remote_sha256": remote,
                    "independently_authenticated": False, "production_applied": False}
                self.assertEqual(project_delivery(base, recovery)["writer_reconciliation_status"], status)
        recovery["remote_ledger_reconciliation"]["status"] = "MATCH"
        with self.assertRaisesRegex(ValueError, "digest contradiction"):
            project_delivery(base, recovery)
        recovery["remote_ledger_reconciliation"] = None
        recovery["production_applied"] = True
        with self.assertRaisesRegex(ValueError, "not read-only"):
            project_delivery(base, recovery)

    def test_packed_ledger_canonical_match_despite_distinct_raw_bytes(self):
        base = {**BASE, "sealed": False, "artifact_status": "CHECKSUM_VERIFIED_LEGACY_NO_RECEIPT", "scoreboard": {}}
        d = {"status": "WRITER_CHECKSUM_ONLY", "remote_downloaded": True,
             "ledger_writer_invoked": False, "production_applied": False,
             "independently_authenticated": False, "run_id": "456", "source_sha": "b"*40,
             "persisted_paper": {"ledger_generation": 7, "scan_status": "ABSTAIN", "live_replay_performed": False},
             "remote_ledger_reconciliation": {"status": "MATCH", "reason": "PACKED_LEDGER_HEAD_COMPARISON",
                 "recovered_sha256": "a"*64, "remote_sha256": "b"*64,
                 "recovered_ledger_sha256": "c"*64, "remote_ledger_sha256": "c"*64,
                 "recovered_generation": 7, "remote_generation": 7,
                 "independently_authenticated": False, "production_applied": False}}
        self.assertEqual(project_delivery(base, d)["writer_reconciliation_status"], "MATCH")
        d["remote_ledger_reconciliation"]["remote_generation"] = 8
        with self.assertRaisesRegex(ValueError, "remote generation contradiction"):
            project_delivery(base, d)
        d["remote_ledger_reconciliation"]["remote_generation"] = 7
        d["remote_ledger_reconciliation"]["remote_ledger_sha256"] = "d"*64
        with self.assertRaisesRegex(ValueError, "digest contradiction"):
            project_delivery(base, d)

    def test_existing_c_handoff_in_shared_delivery_schema(self):
        base = {**BASE, "sealed": False, "artifact_status": "CHECKSUM_VERIFIED_LEGACY_NO_RECEIPT", "scoreboard": {}}
        replay = {"schema": "c_a2_read_only_candidates_v1", "production_applied": False,
                  "trading_approved": False, "live_watch_certified": False,
                  "status": "ABSTAIN_LEGACY_QUOTE_EVIDENCE",
                  "freshness_status": "HISTORICAL_ARTIFACT_NOT_LIVE",
                  "quote_timestamp_semantics": "client_observed_not_exchange_event_time",
                  "receipt_sha256": "a"*64, "watch_count": 1,
                  "watch": [{"pair": "TAOUSD", "rank": 1, "status": "PAPER_WATCH"}],
                  "eligible_pairs": 10, "observed_markets": 8,
                  "source_as_of": "2026-10-01T00:00:00Z",
                  "source_cohort": "authenticated_snapshot_distinct_from_historical_manual_scheduled"}
        result = project_delivery(base, historical_a2=replay)
        self.assertEqual(result["historical_a2"]["watch_count"], 1)
        self.assertFalse(result["historical_a2"]["live_watch_certified"])
        self.assertEqual(result["live_watch"], [])
        replay["live_watch_certified"] = True
        with self.assertRaises(ValueError):
            project_delivery(base, historical_a2=replay)

    def test_actual_paper_result_manual_scheduled_same_schema_and_abstention(self):
        from paper_pov.test_results_report import fixture
        from paper_pov.results_report import render
        scan, score = fixture()
        results = []
        for event, cron in (("workflow_dispatch", None), ("schedule", "9 * * * *")):
            result, _ = render(scan, score, run_id="41235442591", source_sha=SHA,
                               ledger_commit="b"*40, event=event, originating_cron=cron)
            projected = project_published_result(result)
            self.assertEqual(projected["github_event"], event)
            self.assertEqual(projected["live_watch"], [])
            self.assertEqual(projected["status"], "ABSTAIN_SAME_RUN_PERSISTED_WRITER_UNVERIFIED")
            self.assertFalse(projected["live_watch_authorized"])
            self.assertFalse(projected["exchange_event_freshness_verified"])
            results.append(projected)
        self.assertEqual(set(results[0]), set(results[1]))
        scan["watch"] = []
        abstain, _ = render(scan, score, run_id="41235442591", source_sha=SHA,
                            ledger_commit="b"*40, event="schedule", originating_cron="39 * * * *")
        self.assertEqual(project_published_result(abstain)["live_watch"], [])
        for field, value in (("remote_readback_verified", False),
                             ("production_applied", True),
                             ("exchange_event_freshness_verified", True)):
            with self.subTest(field=field), self.assertRaises(ValueError):
                project_published_result({**abstain, field: value})

    def test_actual_paper_delivery_with_separate_a2_receipt_and_d_writer(self):
        from paper_pov.test_results_report import fixture
        from paper_pov.results_report import render
        scan, score = fixture()
        a2 = {"schema": "a2_published_watch_delivery_v1",
              "source": "kraken_public_rest_client_observed",
              "receipt_sha256": "c"*64, "as_of": "2026-11-04T08:00:00Z",
              "scan_status": "WATCH", "watch_count": 1,
              "watch": [{"rank": 1, "symbol": "TAOUSD", "buy_approved": False}],
              "eligible_pairs": 605, "observed_markets": 602,
              "client_quote_freshness_verified": True,
              "single_writer_ledger_verified": False,
              "exchange_event_freshness_verified": False,
              "production_applied": False, "buy_approved": False}
        d = {"status": "WRITER_CHECKSUM_ONLY", "remote_downloaded": True,
             "ledger_writer_invoked": False, "production_applied": False,
             "independently_authenticated": False, "run_id": "456", "source_sha": "b"*40,
             "persisted_paper": {"ledger_generation": 7, "scan_status": "ABSTAIN_STALE",
                                 "live_replay_performed": False},
             "remote_ledger_reconciliation": {"status": "UNAVAILABLE",
                 "reason": "REMOTE_LEDGER_QUERY_FAILED",
                 "independently_authenticated": False, "production_applied": False}}
        outputs = []
        for event, cron in (("schedule", "9 * * * *"), ("workflow_dispatch", None)):
            published, _ = render(scan, score, run_id="41235442591", source_sha=SHA,
                                  ledger_commit="b"*40, event=event, originating_cron=cron)
            output = project_published_result(published, d, a2)
            self.assertEqual(output["writer_reconciliation_status"], "UNAVAILABLE")
            self.assertEqual(output["a2_receipt_cohort"]["receipt_sha256"], "c"*64)
            self.assertFalse(output["a2_receipt_cohort"]["same_scan_as_writer"])
            self.assertFalse(output["live_watch_authorized"])
            outputs.append(output)
        self.assertEqual(set(outputs[0]), set(outputs[1]))
        for status in ("ABSTAIN_NO_LIQUID_CANDIDATES", "ABSTAIN_NO_QUALIFIED_OHLC"):
            abstaining_a2 = {**a2, "scan_status": status, "watch": [], "watch_count": 0}
            result = project_published_result(published, d, abstaining_a2)
            self.assertEqual(result["a2_receipt_cohort"]["status"], status)
            self.assertEqual(result["a2_receipt_cohort"]["watch_count"], 0)
            self.assertFalse(result["live_watch_authorized"])
        with self.assertRaisesRegex(ValueError, "A2 scan status invalid"):
            project_published_result(published, d, {**a2, "scan_status": "ABSTAIN_NO_WATCH", "watch": [], "watch_count": 0})
        with self.assertRaisesRegex(ValueError, "falsely claims"):
            project_published_result(published, d, {**a2, "single_writer_ledger_verified": True})
        with self.assertRaisesRegex(ValueError, "count mismatch"):
            project_published_result(published, d, {**a2, "watch_count": 2})

    def test_delivery_rejects_quote_mismatch_stale_and_stablecoin(self):
        from copy import deepcopy
        from paper_pov.test_results_report import fixture
        from paper_pov.results_report import render
        scan, score = fixture()
        published, _ = render(scan, score, run_id="41235442591", source_sha=SHA,
                              ledger_commit="b"*40, event="workflow_dispatch")
        self.assertEqual(project_published_result(published)["live_watch"], [])
        self.assertEqual(project_published_result(published)["status"], "ABSTAIN_SAME_RUN_PERSISTED_WRITER_UNVERIFIED")
        bad = deepcopy(published)
        bad["candidates"][0]["price_usd"] *= 2
        with self.assertRaisesRegex(ValueError, "matching fresh quote"):
            project_published_result(bad)
        bad = deepcopy(published)
        bad["quote_evidence"][0]["symbol"] = "USDT/USD"
        with self.assertRaisesRegex(ValueError, "excluded published quote"):
            project_published_result(bad)
        bad = deepcopy(published)
        bad["quote_evidence"][0]["observed_at"] = "2020-01-01T00:00:00Z"
        with self.assertRaisesRegex(ValueError, "stale or invalid"):
            project_published_result(bad)
        bad = deepcopy(published)
        bad["max_client_quote_age_seconds"] = 0
        with self.assertRaisesRegex(ValueError, "freshness summary mismatch"):
            project_published_result(bad)

    def test_same_run_d_match_requires_exact_persisted_commit(self):
        from paper_pov.test_results_report import fixture
        from paper_pov.results_report import render
        scan, score = fixture()
        published, _ = render(scan, score, run_id="41235442591", source_sha=SHA,
                              ledger_commit="b"*40, event="workflow_dispatch")
        d = {"status": "VERIFIED_REMOTE_READBACK", "remote_downloaded": True,
             "ledger_writer_invoked": False, "production_applied": False,
             "independently_authenticated": True, "run_id": "41235442591",
             "source_sha": SHA,
             "persisted_paper": {"ledger_generation": published["ledger_generation"],
                                 "scan_status": "SUCCESS_PAPER_ONLY",
                                 "live_replay_performed": False},
             "remote_ledger_reconciliation": {
                 "status": "MATCH", "recovered_sha256": "c"*64,
                 "remote_sha256": "c"*64, "recovered_generation": published["ledger_generation"],
                 "remote_generation": published["ledger_generation"],
                 "independently_authenticated": False, "production_applied": False}}
        output = project_published_result(published, d)
        self.assertEqual(output["status"], "ABSTAIN_SAME_RUN_LEDGER_COMMIT_UNVERIFIED")
        self.assertEqual(output["live_watch"], [])
        self.assertFalse(output["fresh_watch_delivery_verified"])
        d["persisted_paper"]["ledger_commit"] = "f"*40
        with self.assertRaisesRegex(ValueError, "commit contradicts"):
            project_published_result(published, d)

    def test_same_run_exact_commit_match_authorizes_fresh_paper_watch(self):
        from datetime import datetime, timedelta, timezone
        from unittest.mock import patch
        from paper_pov.test_results_report import fixture
        from paper_pov.results_report import render
        from paper_pov.github_delivery_projection import project_published_result
        scan, score = fixture()
        published, _ = render(scan, score, run_id="41235442591",
                              source_sha=SHA, ledger_commit="b"*40,
                              event="workflow_dispatch")
        as_of = datetime.fromisoformat(published["as_of"].replace("Z", "+00:00"))
        d = {"status": "VERIFIED_REMOTE_READBACK", "remote_downloaded": True,
             "ledger_writer_invoked": False, "production_applied": False,
             "independently_authenticated": True, "run_id": published["run_id"],
             "source_sha": SHA,
             "persisted_paper": {"ledger_generation": published["ledger_generation"],
                                 "scan_status": "SUCCESS_PAPER_ONLY",
                                 "live_replay_performed": False,
                                 "ledger_commit": published["ledger_commit"]},
             "remote_ledger_reconciliation": {
                 "status": "MATCH", "recovered_sha256": "c"*64,
                 "recovered_ledger_sha256": published["ledger_sha256"],
                 "remote_ledger_sha256": published["ledger_sha256"],
                 "remote_sha256": "c"*64,
                 "recovered_generation": published["ledger_generation"],
                 "remote_generation": published["ledger_generation"],
                 "independently_authenticated": False, "production_applied": False}}
        class AtReceiptTime(datetime):
            @classmethod
            def now(cls, tz=None):
                return as_of + timedelta(seconds=30)
        with patch("datetime.datetime", AtReceiptTime):
            result = project_published_result(published, d)
        self.assertTrue(result["fresh_watch_delivery_verified"])
        self.assertTrue(result["live_watch_authorized"])
        self.assertEqual(result["live_watch"], published["candidates"])
        d["remote_ledger_reconciliation"]["recovered_ledger_sha256"] = "d"*64
        with patch("datetime.datetime", AtReceiptTime):
            with self.assertRaisesRegex(ValueError, "digest contradiction"):
                project_published_result(published, d)
        d["remote_ledger_reconciliation"]["recovered_ledger_sha256"] = published["ledger_sha256"]
        d["persisted_paper"]["ledger_commit"] = "f"*40
        with patch("datetime.datetime", AtReceiptTime):
            with self.assertRaisesRegex(ValueError, "commit contradicts"):
                project_published_result(published, d)

    def test_real_paper_results_zip_to_delivery_cli(self):
        import hashlib
        import io
        import json
        import tempfile
        import zipfile
        from pathlib import Path
        from unittest.mock import patch
        from paper_pov.github_delivery_projection import main
        from paper_pov.test_results_report import fixture
        from paper_pov.results_report import render
        scan, score = fixture()
        with tempfile.TemporaryDirectory() as folder:
            root = Path(folder)
            for event, cron in (("workflow_dispatch", None), ("schedule", "9 * * * *")):
                published, markdown = render(scan, score, run_id="41235442591", source_sha=SHA,
                                             ledger_commit="b"*40, event=event, originating_cron=cron)
                payload = json.dumps(published).encode()
                note = (markdown + "\n").encode()
                manifest = (hashlib.sha256(payload).hexdigest()+"  results.json\n"+
                            hashlib.sha256(note).hexdigest()+"  results.md\n").encode()
                artifact = root / (event + ".zip")
                with zipfile.ZipFile(artifact, "w") as z:
                    for name, data in (("results.json", payload), ("results.md", note), ("SHA256SUMS", manifest)):
                        z.writestr(name, data)
                output = root / (event + ".json")
                argv = ["delivery", "--published-artifact", str(artifact),
                        "--expected-run-id", "41235442591", "--expected-source-sha", SHA,
                        "--output", str(output)]
                with patch("sys.argv", argv), patch("sys.stdout", new_callable=io.StringIO):
                    main()
                projected = json.loads(output.read_text())
                self.assertEqual(projected["github_event"], event)
                self.assertEqual(projected["live_watch_authorized"], False)
                self.assertEqual(projected["live_watch"], [])
                self.assertEqual(projected["status"], "ABSTAIN_SAME_RUN_PERSISTED_WRITER_UNVERIFIED")
                with patch("sys.argv", argv[:-2] + ["--expected-source-sha", "f"*40]), patch("sys.stdout", new_callable=io.StringIO):
                    with self.assertRaises(ValueError):
                        main()

    def test_learning_handoff_same_manual_scheduled_schema_and_no_promotion(self):
        from paper_pov.test_results_report import fixture
        from paper_pov.results_report import render
        scan, score = fixture()
        learning = {"schema": "paper_learning_handoff_v1", "status": "NO_QUALIFIED_RULE",
                    "read_only": True, "source_authenticated": False,
                    "measured_lift_verified": False, "live_watch_authorized": False,
                    "promotion_authorized": False, "production_applied": False,
                    "evidence_digest": "a"*64, "cohort_join_digest": "b"*64,
                    "baseline_version": "baseline", "challenger_version": "shadow",
                    "evaluation_asof_utc": "2026-11-04T00:00:00Z",
                    "observed_prediction_count": 5, "complete_cohort_count": 3,
                    "excluded_prediction_count": 2,
                    "abstention_counts": {"INCOMPLETE_SOURCE_COVERAGE": 2},
                    "incomplete_prediction_horizons": {"p1": [48], "p2": [1, 6]}}
        outputs = []
        for event, cron in (("workflow_dispatch", None), ("schedule", "9 * * * *")):
            published, _ = render(scan, score, run_id="41235442591", source_sha=SHA,
                                  ledger_commit="b"*40, event=event, originating_cron=cron)
            output = project_published_result(published, learning_handoff=learning)
            self.assertEqual(output["learning"]["status"], "NO_QUALIFIED_RULE")
            self.assertEqual(output["learning"]["excluded_prediction_count"], 2)
            self.assertFalse(output["learning"]["promotion_authorized"])
            self.assertFalse(output["live_watch_authorized"])
            outputs.append(output)
        self.assertEqual(set(outputs[0]), set(outputs[1]))
        for mutation in ({"promotion_authorized": True}, {"source_authenticated": True},
                         {"complete_cohort_count": 4}, {"evidence_digest": "bad"}):
            with self.subTest(mutation=mutation), self.assertRaises(ValueError):
                project_published_result(published, learning_handoff={**learning, **mutation})

    def test_legacy_main_result_retains_complete_shared_delivery_status(self):
        # Main's existing persisted results have no quote_evidence. B's
        # downloaded-delivery consumer must report abstention, not KeyError.
        from paper_pov.test_results_report import fixture
        from paper_pov.results_report import render
        from paper_pov.github_delivery_projection import project_legacy_published_abstention
        scan, score = fixture()
        outputs = []
        for event, cron in (("workflow_dispatch", None), ("schedule", "9 * * * *")):
            published, _ = render(scan, score, run_id="41235442591",
                                  source_sha=SHA, ledger_commit="b"*40,
                                  event=event, originating_cron=cron)
            published.pop("quote_evidence")
            delivery = project_legacy_published_abstention(published)
            for field in ("source_run_id", "source_sha", "github_event",
                          "published_observed_markets", "published_quote_evidence_count",
                          "published_quote_complete", "writer_source_identity_matches_delivery",
                          "fresh_watch_delivery_verified", "learning_status",
                          "scoring_promotion_applied"):
                self.assertIn(field, delivery)
            self.assertEqual(delivery["status"], "ABSTAIN_PUBLISHED_QUOTE_EVIDENCE_MISSING")
            self.assertFalse(delivery["fresh_watch_delivery_verified"])
            self.assertFalse(delivery["published_quote_complete"])
            self.assertEqual(delivery["live_watch"], [])
            outputs.append(delivery)
        self.assertEqual(set(outputs[0]), set(outputs[1]))

    def test_untrusted_promotion_and_run_provenance_rejected(self):
        valid = {**BASE, "sealed": False,
                 "artifact_status": "CHECKSUM_VERIFIED_LEGACY_NO_RECEIPT", "scoreboard": {}}
        for update in ({"watch_delivery_authorized": True},
                       {"publisher_authenticated": True},
                       {"source_sha": "bad"},
                       {"source_run_id": "123"}):
            with self.subTest(update=update), self.assertRaises(ValueError):
                project_delivery({**valid, **update})


if __name__ == "__main__":
    unittest.main()
