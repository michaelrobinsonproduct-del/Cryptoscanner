"""Run one fresh paper scan, then acquire and bind prospective Kraken depth."""
import argparse
import json
from pathlib import Path
from research.live_score_capture import capture_live_scan
from research.acquisition_receipt_pipeline import load_captures
from research.kraken_prospective_batch import collect
from research.depth_acquisition_associations import associate_indexed_captures
from research.prospective_round_store import append_round


def run(root):
    root = Path(root)
    root.mkdir(parents=True, exist_ok=False)
    scores = root / "scores"
    captured = capture_live_scan(scores)
    pairs = [row["pair"] for row in load_captures(scores)][:8]
    if not pairs:
        raise ValueError("no captured WATCH markets")
    depth_dir = root / "depth"
    source = collect(pairs, depth_dir)
    index_path = root / "round-index.jsonl"
    indexed = append_round(index_path, depth_dir)
    binding = associate_indexed_captures(scores, index_path, root / "associations")
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
