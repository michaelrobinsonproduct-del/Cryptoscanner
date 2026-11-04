"""Exercise actual E1 pinned trade files through E's handoff and B's consumer.

CI supplies E1 and B source from their existing owner branches at runtime.
No production writer, network market data, or qualified learning decisions.
"""
import datetime as dt
import hashlib
import sys
import tempfile
import types
import unittest
from pathlib import Path
from unittest.mock import patch

from .historical_execution_learning_bridge import project_historical_execution
from .historical_e1_b_pipeline import run_pipeline, bind_a2_projection, audit_a2_trade_partition_overlap, research_full_universe_predictions
from .historical_preselection_binding import bind_preselection_history


class RealHistoricalE1ToBTests(unittest.TestCase):
    def test_a_historical_universe_retains_unselected_markets(self):
        receipt = "a" * 64
        def market(pair, status):
            return {"pair": pair, "selection_status": status,
                    "observation_id": hashlib.sha256(
                        ("paper-preselection-v1|" + receipt + "|" + pair).encode()).hexdigest()}
        rows = [market("XUSD", "WATCH"), market("YUSD", "SCREEN_REJECTED")]
        history = {"schema": "paper_preselection_history_v1",
                   "snapshot_use": "HISTORICAL_RESEARCH_ONLY",
                   "future_outcomes_authenticated": False, "qualified_for_learning": False,
                   "receipt_count": 1, "market_observation_count": 2,
                   "snapshots": [{"schema": "paper_preselection_v1",
                                  "snapshot_use": "HISTORICAL_RESEARCH_ONLY",
                                  "receipt_sha256": receipt,
                                  "as_of": "2026-01-01T00:00:00+00:00",
                                  "coverage": {"valid_tickers": 2}, "markets": rows}]}
        watch = [{"prediction_id": rows[0]["observation_id"], "pair": "XUSD",
                  "as_of": "2026-01-01T00:00:00+00:00", "status": "PAPER_WATCH"}]
        binding = bind_preselection_history(history, watch)
        self.assertEqual(binding["preselection_observation_count"], 2)
        self.assertEqual(binding["unobserved_nonwatch_count"], 1)
        self.assertFalse(binding["unbiased_learning_qualified"])
        with self.assertRaisesRegex(ValueError, "WATCH sample"):
            bind_preselection_history(history, [])
        # Run the actual A frozen universe through E1 and B; the non-WATCH
        # market remains a missing outcome rather than an invented miss.
        start = dt.datetime(2026, 1, 1, tzinfo=dt.timezone.utc)
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            raw = b"".join(
                f"{int((start + dt.timedelta(minutes=5*i)).timestamp())},100,1\n".encode()
                for i in range(578))
            (root / "XUSD.csv").write_bytes(raw)
            manifest = {"schema": "kraken_archive_manifest_v1", "source": "Kraken",
                        "partitions": [{"file": "XUSD.csv", "size_bytes": len(raw),
                                        "sha256": hashlib.sha256(raw).hexdigest()}]}
            schema = {"format": "kraken_trade_csv_explicit_v1",
                      "timestamp_unit": "seconds",
                      "columns": {"timestamp": 0, "price": 1, "volume": 2},
                      "header": False, "column_count": 3}
            transport_stub = types.ModuleType("paper_pov.github_sealed_bundle_readback")
            transport_stub.read_run = lambda *args, **kwargs: None
            with patch.dict(sys.modules, {"paper_pov.github_sealed_bundle_readback": transport_stub}):
                result = run_pipeline(
                    manifest, root, schema, {"XUSD": "XUSD.csv"}, watch,
                    (start + dt.timedelta(hours=49)).isoformat(),
                    preselection_history=history)
            self.assertEqual(result["handoff"]["reconstructed_prediction_count"], 1)
            self.assertEqual(result["handoff"]["missing_prediction_count"], 1)
            self.assertEqual(result["handoff"]["abstention_counts"],
                             {"UNAUTHENTICATED_ARCHIVE_OR_PROXY_ENTRY": 1,
                              "NO_RECONSTRUCTED_OUTCOME": 1})
            self.assertEqual(result["delivery"]["observed_prediction_count"], 2)
            self.assertEqual(result["delivery"]["status"], "NO_QUALIFIED_RULE")

            # Exercise the retained E A2 projection through the SAME real
            # pinned-trade E1 reconstruction and B delivery consumer.
            projection = {"schema": "a2_historical_e_preselection_v1",
                          "a_receipt_sha256": receipt,
                          "status": "NO_QUALIFIED_RULE",
                          "source_authenticated": False,
                          "historical_outcomes_available": False,
                          "promotion_authorized": False, "production_applied": False,
                          "frozen_predictions": binding["frozen_predictions"],
                          "e1_watch_predictions": watch,
                          "frozen_observation_count": 2, "watch_count": 1,
                          "nonwatch_without_outcomes": 1}
            with patch.dict(sys.modules, {"paper_pov.github_sealed_bundle_readback": transport_stub}):
                retained = run_pipeline(
                    manifest, root, schema, {"XUSD": "XUSD.csv"}, watch,
                    (start + dt.timedelta(hours=49)).isoformat(),
                    a2_projection=projection)
            complete_projection = dict(projection, frozen_observations=[
                {"prediction_id": rows[0]["observation_id"], "pair": "XUSD",
                 "as_of": start.isoformat(), "selection_status": "WATCH"},
                {"prediction_id": rows[1]["observation_id"], "pair": "YUSD",
                 "as_of": start.isoformat(), "selection_status": "SCREEN_REJECTED"}])
            research_predictions = research_full_universe_predictions(complete_projection)
            self.assertEqual(len(research_predictions), 2)
            self.assertEqual({p["pair"] for p in research_predictions}, {"XUSD", "YUSD"})
            with patch.dict(sys.modules, {"paper_pov.github_sealed_bundle_readback": transport_stub}):
                all_markets = run_pipeline(
                    manifest, root, schema, {"XUSD": "XUSD.csv"}, watch,
                    (start + dt.timedelta(hours=49)).isoformat(),
                    a2_projection=complete_projection, full_universe_research=True)
            self.assertTrue(all_markets["research_full_universe"])
            self.assertEqual(all_markets["handoff"]["reconstructed_prediction_count"], 2)
            self.assertEqual(all_markets["handoff"]["missing_prediction_count"], 0)
            self.assertEqual(all_markets["delivery"]["observed_prediction_count"], 2)
            self.assertEqual(all_markets["delivery"]["status"], "NO_QUALIFIED_RULE")
            self.assertEqual(all_markets["handoff"]["qualified_cohort_count"], 0)
            self.assertEqual({r["observation_asof_utc"] for r in all_markets["handoff"]["diagnostic_outcome_rows"]}, {start.isoformat()})
            self.assertTrue(all(r["observation_asof_utc"] is None for r in retained["handoff"]["diagnostic_outcome_rows"]))
            self.assertFalse(all_markets["handoff"]["source_authenticated"])
            decisions = {(r["pair"], r["frozen_selection_status"]) for r in all_markets["handoff"]["diagnostic_outcome_rows"]}
            self.assertEqual(decisions, {("XUSD", "WATCH"), ("YUSD", "SCREEN_REJECTED")})
            selection_outcomes = all_markets["handoff"]["diagnostic_selection_outcomes"]
            for horizon in ("1", "6", "24", "48"):
                self.assertEqual(sum(sum(bucket.values()) for bucket in
                                     selection_outcomes[horizon].values()), 2)
                self.assertEqual(selection_outcomes[horizon]["SCREEN_REJECTED"]["abstained"], 1)
            self.assertEqual(selection_outcomes["48"]["WATCH"]["observed_misses_unqualified"], 1)
            self.assertEqual(selection_outcomes["48"]["WATCH"]["observed_hits_unqualified"], 0)

            overlap = audit_a2_trade_partition_overlap(
                dict(projection, frozen_observations=[
                    {"prediction_id": rows[0]["observation_id"], "pair": "XUSD",
                     "as_of": start.isoformat(), "selection_status": "WATCH"},
                    {"prediction_id": rows[1]["observation_id"], "pair": "YUSD",
                     "as_of": start.isoformat(), "selection_status": "SCREEN_REJECTED"}]),
                manifest, root, schema, {"XUSD": "XUSD.csv"},
                observed_until=(start + dt.timedelta(hours=49)).isoformat())
            with self.assertRaisesRegex(ValueError, "reused across A2 markets"):
                audit_a2_trade_partition_overlap(
                    complete_projection, manifest, root, schema,
                    {"XUSD": "XUSD.csv", "YUSD": "XUSD.csv"},
                    observed_until=(start + dt.timedelta(hours=49)).isoformat())
            with self.assertRaisesRegex(ValueError, "outside frozen A2 cohort"):
                audit_a2_trade_partition_overlap(
                    complete_projection, manifest, root, schema,
                    {"XUSD": "XUSD.csv", "ZUSD": "ZUSD.csv"},
                    observed_until=(start + dt.timedelta(hours=49)).isoformat())
            self.assertEqual(sum(overlap["status_counts"].values()), 2)
            self.assertEqual(overlap["status_counts"]["NO_PINNED_PARTITION"], 1)
            self.assertEqual(overlap["status_counts"]["ENTRY_BAR_PRESENT_UNQUALIFIED"], 1)
            self.assertEqual(overlap["qualified_outcome_count"], 0)
            self.assertEqual(len(overlap["cohort_coverage"]), 2)
            coverage = {x["pair"]: x for x in overlap["cohort_coverage"]}
            self.assertEqual(coverage["YUSD"]["horizons"]["48"], "NO_PINNED_PARTITION")
            self.assertEqual(coverage["XUSD"]["horizons"]["48"], "COMPLETE_BAR_PATH_UNQUALIFIED")
            self.assertEqual(coverage["XUSD"]["entry_status"], "ENTRY_BAR_PRESENT_UNQUALIFIED")
            # The 48h target opens at 48:05 but is only observable at
            # 48:10. E's all-market audit must agree with E1's closed bars.
            cutoff_projection = dict(projection, frozen_observations=[
                {"prediction_id": rows[0]["observation_id"], "pair": "XUSD",
                 "as_of": start.isoformat(), "selection_status": "WATCH"},
                {"prediction_id": rows[1]["observation_id"], "pair": "YUSD",
                 "as_of": start.isoformat(), "selection_status": "SCREEN_REJECTED"}])
            before_close = audit_a2_trade_partition_overlap(
                cutoff_projection, manifest, root, schema, {"XUSD": "XUSD.csv"},
                observed_until=(start + dt.timedelta(hours=48, minutes=5)).isoformat())
            after_close = audit_a2_trade_partition_overlap(
                cutoff_projection, manifest, root, schema, {"XUSD": "XUSD.csv"},
                observed_until=(start + dt.timedelta(hours=48, minutes=10)).isoformat())
            before = next(x for x in before_close["cohort_coverage"] if x["pair"] == "XUSD")
            after = next(x for x in after_close["cohort_coverage"] if x["pair"] == "XUSD")
            self.assertEqual(before["horizons"]["48"], "ABSTAIN_IMMATURE")
            self.assertEqual(after["horizons"]["48"], "COMPLETE_BAR_PATH_UNQUALIFIED")

            # The decision timestamp's own 5m bar must never count as entry.
            earlier = dict(projection, frozen_observations=[
                {"prediction_id": rows[0]["observation_id"], "pair": "XUSD",
                 "as_of": (start + dt.timedelta(minutes=5)).isoformat(),
                 "selection_status": "WATCH"},
                {"prediction_id": rows[1]["observation_id"], "pair": "YUSD",
                 "as_of": start.isoformat(), "selection_status": "SCREEN_REJECTED"}])
            # A WATCH decision cannot silently move independently of its frozen observation.
            with self.assertRaisesRegex(ValueError, "observation time mismatch"):
                audit_a2_trade_partition_overlap(earlier, manifest, root, schema, {"XUSD": "XUSD.csv"}, observed_until=(start + dt.timedelta(hours=49)).isoformat())
            shifted = audit_a2_trade_partition_overlap(
                dict(earlier, e1_watch_predictions=[dict(watch[0], as_of=(start + dt.timedelta(minutes=5)).isoformat())]),
                manifest, root, schema, {"XUSD": "XUSD.csv"},
                observed_until=(start + dt.timedelta(hours=49)).isoformat())
            self.assertEqual(sum(shifted["status_counts"].values()), 2)
            # Future trade bars cannot satisfy a decision's entry or horizon
            # when they were not complete at the specified observation cutoff.
            early_cutoff = audit_a2_trade_partition_overlap(
                dict(projection, frozen_observations=[
                    {"prediction_id": rows[0]["observation_id"], "pair": "XUSD",
                     "as_of": start.isoformat(), "selection_status": "WATCH"},
                    {"prediction_id": rows[1]["observation_id"], "pair": "YUSD",
                     "as_of": start.isoformat(), "selection_status": "SCREEN_REJECTED"}]),
                manifest, root, schema, {"XUSD": "XUSD.csv"},
                observed_until=(start + dt.timedelta(minutes=5)).isoformat())
            self.assertEqual(early_cutoff["status_counts"]["NO_ENTRY_BAR"], 1)
            self.assertEqual(early_cutoff["diagnostic_horizon_coverage"]["1"]["ABSTAIN_IMMATURE"], 1)


            self.assertEqual(retained["handoff"], result["handoff"])
            self.assertEqual(retained["delivery"], result["delivery"])
            self.assertEqual(retained["preselection_binding"]["a_receipt_sha256"], receipt)
            for changed in (
                dict(projection, source_authenticated=True),
                dict(projection, frozen_observation_count=1),
                dict(projection, e1_watch_predictions=[])):
                with self.assertRaises(ValueError):
                    bind_a2_projection(changed, watch)
            with self.assertRaisesRegex(ValueError, "WATCH sample"):
                bind_a2_projection(projection, [])
            altered = dict(projection, frozen_predictions=[
                dict(binding["frozen_predictions"][0], prediction_id="f" * 64),
                binding["frozen_predictions"][1]])
            with self.assertRaisesRegex(ValueError, "sealed receipt"):
                bind_a2_projection(altered, watch)



    def test_historical_outputs_roll_back_partial_publication(self):
        from .historical_e1_b_pipeline import main
        from unittest.mock import patch as mock_patch
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            for name in ("manifest", "schema", "partitions", "predictions", "a2"):
                (root / (name + ".json")).write_text("{}", encoding="utf-8")
            output, overlap = root / "result.json", root / "overlap.json"
            argv = [
                "--manifest", str(root / "manifest.json"),
                "--root", str(root),
                "--schema", str(root / "schema.json"),
                "--partitions", str(root / "partitions.json"),
                "--predictions", str(root / "predictions.json"),
                "--a2-projection", str(root / "a2.json"),
                "--observed-until", "2026-01-03T00:00:00+00:00",
                "--output", str(output),
                "--full-cohort-overlap-output", str(overlap),
            ]
            fake = {"execution": {"prediction_count": 0, "status_counts": {}},
                    "handoff": {"qualified_cohort_count": 0},
                    "delivery": {"status": "NO_QUALIFIED_RULE"}}
            from . import historical_e1_b_pipeline as pipeline
            original_link = pipeline.os.link
            def fail_second(source, destination):
                if Path(destination) == overlap:
                    raise OSError("injected second publication failure")
                return original_link(source, destination)
            with mock_patch.object(pipeline, "bind_a2_projection", return_value=None), \
                 mock_patch.object(pipeline, "audit_a2_trade_partition_overlap", return_value={}), \
                 mock_patch.object(pipeline, "run_pipeline", return_value=fake), \
                 mock_patch.object(pipeline.os, "link", side_effect=fail_second):
                with self.assertRaisesRegex(OSError, "injected second"):
                    main(argv)
            self.assertFalse(output.exists())
            self.assertFalse(overlap.exists())
            self.assertEqual(list(root.glob(".e1-b-*")), [])

    def test_pinned_csv_to_four_horizons_to_b_read_only(self):
        from .historical_outcome_execution import run_historical_outcomes
        # B's module imports its transport at import time; the projection below
        # only needs _learning_evidence, not any transport or external services.
        transport_stub = types.ModuleType("paper_pov.github_sealed_bundle_readback")
        transport_stub.read_run = lambda *args, **kwargs: None
        with patch.dict(sys.modules, {"paper_pov.github_sealed_bundle_readback": transport_stub}):
            from .github_delivery_projection import _learning_evidence

        start = dt.datetime(2026, 1, 1, tzinfo=dt.timezone.utc)
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            raw = b"".join(
                f"{int((start + dt.timedelta(minutes=5*i)).timestamp())},{100+i*0.01:.2f},1\n".encode()
                for i in range(578))
            (root / "XUSD.csv").write_bytes(raw)
            manifest = {"schema": "kraken_archive_manifest_v1", "source": "Kraken",
                        "partitions": [{"file": "XUSD.csv", "size_bytes": len(raw),
                                        "sha256": hashlib.sha256(raw).hexdigest()}]}
            schema = {"format": "kraken_trade_csv_explicit_v1",
                      "timestamp_unit": "seconds",
                      "columns": {"timestamp": 0, "price": 1, "volume": 2},
                      "header": False, "column_count": 3}
            predictions = [
                {"prediction_id": "p1", "pair": "XUSD", "status": "PAPER_WATCH",
                 "as_of": start.isoformat()},
                {"prediction_id": "p2", "pair": "YUSD", "status": "PAPER_WATCH",
                 "as_of": start.isoformat()}]
            with patch.dict(sys.modules, {"paper_pov.github_sealed_bundle_readback": transport_stub}):
                integrated = run_pipeline(
                    manifest, root, schema, {"XUSD": "XUSD.csv"}, predictions,
                    (start + dt.timedelta(hours=49)).isoformat())
            result, handoff, projected = (integrated["execution"], integrated["handoff"], integrated["delivery"])
            self.assertEqual(projected, _learning_evidence(handoff))
            self.assertEqual(result["status_counts"]["48h:MATURED_OBSERVED"], 1)
            self.assertEqual(result["status_counts"]["48h:ABSTAIN_ENTRY"], 1)
            self.assertEqual(handoff["diagnostic_horizon_status_counts"]["48"]["ABSTAIN_ENTRY"], 1)
            self.assertEqual(projected["observed_prediction_count"], 2)
            self.assertEqual(projected["complete_cohort_count"], 0)
            self.assertEqual(projected["excluded_prediction_count"], 2)
            self.assertEqual(projected["status"], "NO_QUALIFIED_RULE")
            self.assertEqual(len(handoff["diagnostic_outcome_rows"]), 8)
            self.assertEqual(handoff["diagnostic_horizon_hit_miss"]["48"]["observed_hits_unqualified"] +
                             handoff["diagnostic_horizon_hit_miss"]["48"]["observed_misses_unqualified"], 1)
            self.assertEqual(sum(row["status"] == "ABSTAIN_ENTRY" for row in handoff["diagnostic_outcome_rows"]), 4)
            self.assertTrue(all(row["qualified_for_learning"] is False and
                                row["source_authenticated"] is False and
                                row["liquidity_qualified"] is False
                                for row in handoff["diagnostic_outcome_rows"]))

            self.assertFalse(projected["promotion_authorized"])
            # The 48h target opens at +48h05; its high is not observable
            # until the entire target bar closes at +48h10.
            with patch.dict(sys.modules, {"paper_pov.github_sealed_bundle_readback": transport_stub}):
                not_closed = run_pipeline(
                    manifest, root, schema, {"XUSD": "XUSD.csv"}, predictions,
                    (start + dt.timedelta(hours=48, minutes=5)).isoformat())
                closed = run_pipeline(
                    manifest, root, schema, {"XUSD": "XUSD.csv"}, predictions,
                    (start + dt.timedelta(hours=48, minutes=10)).isoformat())
            self.assertEqual(not_closed["execution"]["status_counts"].get("48h:MATURED_OBSERVED", 0), 0)
            self.assertEqual(not_closed["execution"]["status_counts"]["48h:ABSTAIN_IMMATURE"], 1)
            self.assertEqual(closed["execution"]["status_counts"]["48h:MATURED_OBSERVED"], 1)
            # Mutation of pinned bytes must fail BEFORE E can hand anything to B.
            (root / "XUSD.csv").write_bytes(raw.replace(b"100.00", b"101.00", 1))
            with self.assertRaisesRegex(ValueError, "checksum"):
                run_historical_outcomes(
                    manifest, root, schema, {"XUSD": "XUSD.csv"}, predictions,
                    (start + dt.timedelta(hours=49)).isoformat())


if __name__ == "__main__":
    unittest.main()
