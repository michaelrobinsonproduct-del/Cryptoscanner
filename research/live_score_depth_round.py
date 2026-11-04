"""Run one fresh paper scan, then acquire and bind prospective Kraken depth."""
import argparse
import json
from pathlib import Path
from research.live_score_capture import capture_live_scan
from research.acquisition_receipt_pipeline import load_captures
from research.kraken_prospective_batch import collect
from research.depth_acquisition_associations import associate_captured_scores


def run(root):
    root = Path(root)
    root.mkdir(parents=True, exist_ok=False)
    scores = root / "scores"
    captured = capture_live_scan(scores)
    pairs = [row["pair"] for row in load_captures(scores)][:8]
    if not pairs:
        raise ValueError("no captured WATCH markets")
    source = collect(pairs, root / "depth")
    binding = associate_captured_scores(scores, root / "depth", root / "associations")
    return {"mode": "RESEARCH_ONLY_PROSPECTIVE_SCORE_DEPTH",
            "scores_captured": captured["captures"],
            "depth_requested": source["pairs_requested"],
            "depth_eligible": source["pairs_eligible"],
            "associated": len(binding["associated"]),
            "excluded": binding["excluded"],
            "production_applied": False}


def main():
    p = argparse.ArgumentParser()
    p.add_argument("--output-dir", required=True)
    a = p.parse_args()
    print(json.dumps(run(a.output_dir), sort_keys=True))


if __name__ == "__main__":
    main()
