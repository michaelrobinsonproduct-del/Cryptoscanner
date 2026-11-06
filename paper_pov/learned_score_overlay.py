"""Read-only E shadow-score overlay for an already sealed paper publication.

Never modifies the immutable result artifact or baseline WATCH ranking.
"""
import argparse
import json
from pathlib import Path


def render_shadow_overlay(published, shadow):
    if published.get("production_applied") is not False or published.get("buy_approved") is not False:
        raise ValueError("Expected paper-only publication")
    if shadow.get("production_applied") is not False or shadow.get("promotion_authorized") is not False:
        raise ValueError("Shadow scores cannot authorize trading or production changes")
    candidates = published.get("candidates", [])
    ids = [c["prediction_id"] for c in candidates]
    if len(set(ids)) != len(ids):
        raise ValueError("Duplicate published predictions")
    scored = shadow.get("scores", [])
    by_id = {row["prediction_id"]: row for row in scored}
    if len(by_id) != len(scored) or set(by_id) - set(ids):
        raise ValueError("Shadow score identity differs from published candidates")
    version = shadow.get("challenger_version", "UNAVAILABLE")
    lines = ["## Learned challenger — paper-only overlay", "",
             "Source scan: " + str(published["run_id"]),
             "Model version: " + str(version),
             "Learning status: " + str(shadow["status"]),
             "No automatic promotion; baseline WATCH order unchanged.", "",
             "| Symbol | Baseline | Existing challenger | Learned shadow |",
             "|---|---:|---:|---:|"]
    for candidate in candidates:
        row = by_id.get(candidate["prediction_id"])
        value = "NO QUALIFIED SCORE" if row is None else f'{row["shadow_score"]:.3f}'
        lines.append(f'| {candidate["symbol"]} | {candidate["baseline_score"]:.3f} | '
                     f'{candidate["challenger_score"]:.3f} | {value} |')
    return "\n".join(lines) + "\n"


def main(argv=None):
    parser = argparse.ArgumentParser()
    parser.add_argument("published_json", type=Path)
    parser.add_argument("shadow_scores_json", type=Path)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args(argv)
    published = json.loads(args.published_json.read_text())
    shadow = json.loads(args.shadow_scores_json.read_text())
    report = render_shadow_overlay(published, shadow)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(report)
    print("PAPER_SHADOW_OVERLAY", published["run_id"], len(shadow.get("scores", [])))


if __name__ == "__main__":
    main()
