import unittest
from datetime import datetime, timedelta, timezone
from paper_pov.early_objective_shadow import early_label, interaction_features, learned_replay


class EarlyObjectiveTests(unittest.TestCase):
    def features(self,m=.01):
        return dict(momentum_5m=.01,momentum_15m=.01,momentum_60m=m,
                    volume_accel=3.,trade_accel=2.,volatility_60m=.005)

    def test_complete_early_objective_and_unknowns(self):
        p=dict(features=self.features())
        o=dict(coverage_complete=True,hit=True,observed_lead_hours_upper_bound=6)
        self.assertTrue(early_label(p,o))
        self.assertFalse(early_label(dict(features=self.features(.1)),o))
        self.assertIsNone(early_label(p,dict(o,coverage_complete=False)))
        self.assertIsNone(early_label(p,dict(o,observed_lead_hours_upper_bound=None)))
        self.assertFalse(early_label(p,dict(o,hit=False)))
        self.assertFalse(early_label(p,dict(o,observed_lead_hours_upper_bound=1)))
        self.assertGreater(interaction_features(self.features())["activity_x_quiet"],
                           interaction_features(self.features(.2))["activity_x_quiet"])

    def test_fit_chronological_and_preserves_unlabeled_holdout(self):
        start=datetime(2026,1,1,tzinfo=timezone.utc)
        at=lambda d:(start+timedelta(days=d)).isoformat()
        rows=[]; outcomes=[]
        for k,day,m,hit in (("a",0,.01,True),("b",0,.2,False),
                              ("c",5,.01,True),("d",5,.2,False)):
            rows.append(dict(prediction_id=k,entry_utc=at(day),feature_asof_utc=at(day),
                             features=self.features(m)))
            outcomes.append(dict(prediction_id=k,horizon_hours=48,label_mature_utc=at(day+2),
                                 coverage_complete=True,hit=hit,observed_lead_hours_upper_bound=6))
        outcomes[-1].update(coverage_complete=False,hit=None)
        report=learned_replay(rows,outcomes,[(rows[2:],["d"],["c"])],
                              training_end_utc=at(3),holdout_start_utc=at(5))
        for model in report["models"].values():
            self.assertEqual(model["training_count"],2)
            self.assertEqual(model["holdout_count"],2)
        self.assertEqual(report["metrics"]["baseline"]["unknown"],1)
        self.assertEqual(report["metrics"]["baseline"]["paired_alerts_each"],0)
        self.assertEqual(report["metrics"]["learned_early_objective"]["early_hits"],1)
        self.assertFalse(report["production_applied"])
        with self.assertRaisesRegex(ValueError,"purge"):
            learned_replay(rows,outcomes,[],training_end_utc=at(3),holdout_start_utc=at(4))
