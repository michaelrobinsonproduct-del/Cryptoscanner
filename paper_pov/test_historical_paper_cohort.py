"""Focused historical per-prediction cohort recovery acceptance."""
import unittest
from paper_pov.historical_paper_cohort import reconstruct_history

class HistoricalPaperCohortTest(unittest.TestCase):
    def test_maturing_prediction_is_recovered_once(self):
        prediction = {"prediction_id": "p", "as_of": "2026-11-01T00:00:00Z",
                      "baseline_score": 60, "challenger_score": 65}
        early = {"schema": 1, "generation": 1, "predictions": [prediction],
                 "outcomes": [{"prediction_id": "p", "horizon_hours": 48,
                               "status": "ABSTAIN_GAP"}]}
        late = {"schema": 1, "generation": 2, "predictions": [prediction],
                "outcomes": [{"prediction_id": "p", "horizon_hours": 48,
                              "status": "MATURE_MISS"}]}
        result = reconstruct_history([("new", late), ("old", early)])
        self.assertEqual(result["unique_predictions"], 1)
        self.assertEqual(result["unique_outcomes"], 1)
        self.assertEqual(result["recovered_mature_outcomes"], 1)
        self.assertFalse(result["source_authenticated"])
        self.assertFalse(result["promotion_authorized"])
        carried = {"schema": "recovered_cohort", "generation": -1,
                   "predictions": result["prediction_rows"],
                   "outcomes": result["outcome_rows"]}
        replay = reconstruct_history([("retained", carried), ("new", late)])
        self.assertEqual(replay["recovered_mature_outcomes"], 1)
        self.assertEqual(replay["unique_predictions"], 1)

if __name__ == "__main__":
    unittest.main()
