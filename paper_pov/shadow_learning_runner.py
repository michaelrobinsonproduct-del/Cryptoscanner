"""Execute the paper-only historical outcome and challenger learning pipeline."""
import argparse
import json
from pathlib import Path

from .heldout_outcome_adapter import (
    build_shadow_learning_state, save_shadow_learning_state,
)

def main(argv=None):
    parser = argparse.ArgumentParser(description="Run non-promotable paper learning")
    parser.add_argument("input_json", type=Path)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args(argv)
    payload = json.loads(args.input_json.read_text(encoding="utf-8"))
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
