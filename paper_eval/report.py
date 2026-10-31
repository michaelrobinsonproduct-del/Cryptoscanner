"""Read-only, independently checksummed evaluation of the public paper ledger.

Never writes to the scanner ledger, claims exchange-complete highs, or promotes
any model. An evaluation is only as complete as its recorded quote samples.
"""
import argparse
import hashlib
import json
from pathlib import Path

from paper_eval.audit import evaluate
from paper_pov.ledger import HORIZONS, canonical, verify
from paper_pov.segmented_storage import MAX_RAW_BYTES
from paper_pov.scanner import atomic_json


def report(state, ledger_commit):
    if not isinstance(ledger_commit, str) or len(ledger_commit) != 40 or any(
            c not in "0123456789abcdef" for c in ledger_commit):
        raise ValueError("Missing exact 40-character ledger commit SHA")
    verify(state, MAX_RAW_BYTES)
    result = {
        "schema": 1,
        "mode": "READ_ONLY_PAPER_AUDIT",
        "ledger_commit": ledger_commit,
        "ledger_generation": state["generation"],
        "ledger_sha256": state["sha256"],
        "horizons": {str(h): evaluate(state, horizon_hours=h, top_k=5)
                     for h in HORIZONS},
        "independent_held_out_lift": None,
        "production_applied": False,
        "limitations": (
            "Sampled public Kraken ticker observations only; not exchange-complete "
            "highs or all-market recall. Archived records not independently "
            "reconstructed. This is not a validated predictive strategy."
        ),
    }
    result["report_sha256"] = hashlib.sha256(canonical(result)).hexdigest()
    return result


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--ledger", required=True)
    parser.add_argument("--ledger-commit", required=True)
    parser.add_argument("--output", required=True)
    args = parser.parse_args()
    state = json.loads(Path(args.ledger).read_text())
    result = report(state, args.ledger_commit)
    atomic_json(args.output, result)
    assert json.loads(Path(args.output).read_text()) == result
    print("PAPER_READ_ONLY_AUDIT", json.dumps({
        "ledger_commit": result["ledger_commit"],
        "generation": result["ledger_generation"],
        "ledger_sha256": result["ledger_sha256"],
        "report_sha256": result["report_sha256"],
        "comparable_runs": {h: r["comparable_runs"]
                            for h, r in result["horizons"].items()},
        "held_out_lift": None, "production_applied": False,
    }, sort_keys=True))


if __name__ == "__main__":
    main()
