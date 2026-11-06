"""Execute the paper-only historical outcome and challenger learning pipeline."""
import argparse
import json
from pathlib import Path

from .heldout_outcome_adapter import (
    build_shadow_learning_state, save_shadow_learning_state, read_shadow_learning_state,
)

def score_future_paper_predictions(state_path, predictions):
    """Score later paper candidates using a frozen shadow model; no WATCH promotion."""
    state = read_shadow_learning_state(state_path)
    model = state["challenger"]
    if model["status"] != "SHADOW_ONLY":
        return {"status": "NO_QUALIFIED_RULE", "scores": [], "promotion_authorized": False}
    keys = model["feature_names"]
    results = []
    for candidate in predictions:
        features = candidate.get("features", {})
        if any(k not in features for k in keys):
            continue
        score = sum((features[k] - model["feature_centers"][k])
                    / model["feature_scales"][k] * model["feature_weights"][k]
                    for k in keys)
        results.append({"prediction_id": candidate["prediction_id"],
                        "shadow_score": score, "challenger_version": model["version"],
                        "watch_authorized": False})
    return {"status": "SHADOW_ONLY", "scores": results,
            "promotion_authorized": False, "production_applied": False}


def main(argv=None):
    parser = argparse.ArgumentParser(description="Run non-promotable paper learning")
    parser.add_argument("input_json", type=Path)
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--predictions-jsonl", type=Path)
    parser.add_argument("--candles-jsonl", type=Path)
    parser.add_argument("--baseline-json", type=Path)
    args = parser.parse_args(argv)
    payload = json.loads(args.input_json.read_text(encoding="utf-8"))
    if args.predictions_jsonl:
        payload["predictions"] = [json.loads(line) for line in
                                  args.predictions_jsonl.read_text(encoding="utf-8").splitlines()
                                  if line.strip()]
    if args.candles_jsonl:
        payload["candles"] = [json.loads(line) for line in
                              args.candles_jsonl.read_text(encoding="utf-8").splitlines()
                              if line.strip()]
    if args.baseline_json:
        payload["baseline_decisions"] = json.loads(args.baseline_json.read_text(encoding="utf-8"))
    state = build_shadow_learning_state(**payload)
    save_shadow_learning_state(args.output, state)
    print(json.dumps({
        "state_digest": state["state_digest"],
        "outcome_count": state["outcome_count"],
        "comparison_status": state["comparison"]["status"],
        "promotion_authorized": False,
    }, sort_keys=True))
    return state

if __name__ == "__main__":
    main()
