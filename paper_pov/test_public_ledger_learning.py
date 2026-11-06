"""Real public paper-ledger schema integration acceptance."""
import json
import tempfile
import unittest
from pathlib import Path
from paper_pov.public_ledger_learning import learn_from_public_ledger, process_ledger_file, render_learning_report

class PublicLedgerAcceptance(unittest.TestCase):
    def test_abstentions_are_not_learning_labels(self):
        ledger = {
            "schema": 1, "generation": 96,
            "archived": {"predictions": 740},
            "predictions": [{"prediction_id": "p", "as_of": "2026-11-05T00:00:00Z",
                             "pair": "TESTUSD", "price": 1.0,
                             "baseline_score": 60, "challenger_score": 65}],
            "outcomes": [{"prediction_id": "p", "horizon_hours": 1,
                          "status": "ABSTAIN_GAP", "target_at": "2026-11-05T01:00:00Z"}],
        }
        with tempfile.TemporaryDirectory() as folder:
            source = Path(folder) / "ledger.json"
            output = Path(folder) / "learning.json"
            source.write_text(json.dumps(ledger), encoding="utf-8")
            result = process_ledger_file(source, output)
            self.assertEqual(result["eligible_training_count"], 0)
            self.assertEqual(result["outcome_counts"]["1"]["abstentions"], 1)
            self.assertEqual(result["archived_prediction_count"], 740)
            self.assertFalse(result["promotion_authorized"])
            self.assertIn("Retained trainable labels: 0", render_learning_report(result))
            self.assertEqual(json.loads(output.read_text())["evidence_digest"], result["evidence_digest"])

if __name__ == "__main__":
    unittest.main()
