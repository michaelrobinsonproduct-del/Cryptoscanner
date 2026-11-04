"""Consume an actual published A2 receipt artifact as historical E evidence.

No future bars are inferred from a current A2 snapshot. All 1/6/24/48h
outcomes abstain until independently pinned trade partitions are supplied.
"""
import argparse
import json
import tempfile
import zipfile
from pathlib import Path

from .preselection_universe import export_receipt_history
from .historical_preselection_binding import bind_preselection_history


def project_a2_historical_artifact(archive):
    archive = Path(archive)
    if archive.is_symlink() or not archive.is_file() or archive.stat().st_size > 8_000_000:
        raise ValueError("Missing or unsafe downloaded A2 archive")
    with zipfile.ZipFile(archive) as z:
        infos = z.infolist()
        receipts = [i for i in infos if i.filename.startswith("receipts/") and i.filename.endswith(".json")]
        if len(receipts) != 1 or len(infos) > 30 or len({i.filename for i in infos}) != len(infos):
            raise ValueError("Unexpected A2 archive membership")
        if any(i.file_size > 2_000_000 or i.filename.startswith("/") or ".." in Path(i.filename).parts
               or (i.external_attr >> 16) & 0o170000 == 0o120000 for i in infos):
            raise ValueError("Unsafe A2 artifact member")
        receipt = z.read(receipts[0])
        if "latest.json" not in z.namelist() or z.read("latest.json") != receipt:
            raise ValueError("A2 immutable receipt mismatch")
    with tempfile.TemporaryDirectory() as directory:
        root = Path(directory)
        (root / "receipts").mkdir()
        (root / receipts[0].filename).write_bytes(receipt)
        history = export_receipt_history(root / "receipts")
    watch = []
    for snapshot in history["snapshots"]:
        for market in snapshot["markets"]:
            if market["selection_status"] == "WATCH":
                watch.append({"prediction_id": market["observation_id"],
                              "pair": market["pair"], "as_of": snapshot["as_of"],
                              "status": "PAPER_WATCH"})
    binding = bind_preselection_history(history, watch)
    return {"schema": "a2_historical_e_preselection_v1",
            "a_receipt_sha256": history["snapshots"][0]["receipt_sha256"],
            "as_of": history["snapshots"][0]["as_of"],
            "frozen_observation_count": binding["preselection_observation_count"],
            "watch_count": binding["watch_outcome_input_count"],
            "nonwatch_without_outcomes": binding["unobserved_nonwatch_count"],
            "frozen_predictions": binding["frozen_predictions"],
            "e1_watch_predictions": binding["e1_watch_predictions"],
            "source_authenticated": False,
            "historical_outcomes_available": False,
            "status": "NO_QUALIFIED_RULE",
            "promotion_authorized": False, "production_applied": False}


def main(argv=None):
    p = argparse.ArgumentParser()
    p.add_argument("--a2-artifact", required=True)
    p.add_argument("--output", required=True)
    args = p.parse_args(argv)
    out = Path(args.output)
    if out.exists():
        raise FileExistsError("Refusing to overwrite A2 historical projection")
    result = project_a2_historical_artifact(args.a2_artifact)
    out.write_text(json.dumps(result, sort_keys=True, indent=2) + "\n")
    print(json.dumps({k: result[k] for k in ("a_receipt_sha256", "frozen_observation_count",
                                            "watch_count", "nonwatch_without_outcomes", "status")}, sort_keys=True))


if __name__ == "__main__":
    main()
