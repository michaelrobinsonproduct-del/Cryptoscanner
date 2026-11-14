"""Combine independently verified same-run paper and legacy-shadow WATCH reports.

Read-only reporting. No Kraken requests, ledger writes, scoring or trading.
"""
import argparse
import hashlib
import json
import re
from pathlib import Path

SHA40 = re.compile(r"[0-9a-f]{40}\Z")
SHA64 = re.compile(r"[0-9a-f]{64}\Z")
SYMBOL = re.compile(r"[A-Z0-9._-]+/USD\Z")


def _read_verified(directory, filenames, manifest_name):
    root = Path(directory)
    lines = (root / manifest_name).read_text().splitlines()
    if len(lines) != len(filenames):
        raise ValueError("Unexpected checksum file count")
    for line, name in zip(lines, filenames):
        if "  " not in line:
            raise ValueError("Malformed checksum manifest")
        expected, actual_name = line.split("  ", 1)
        if actual_name != name or not SHA64.fullmatch(expected):
            raise ValueError("Wrong or invalid checksum name")
        if hashlib.sha256((root / name).read_bytes()).hexdigest() != expected:
            raise ValueError("Artifact checksum mismatch: " + name)
    return json.loads((root / filenames[0]).read_text())


def _ranked(items, score_key, with_trades=False):
    if not isinstance(items, list) or len(items) > 12:
        raise ValueError("Invalid ranked WATCH list")
    out = []
    seen = set()
    for i, x in enumerate(items, 1):
        if (not isinstance(x, dict) or x.get("rank") != i
                or not isinstance(x.get("symbol"), str)
                or not SYMBOL.fullmatch(x["symbol"])
                or x["symbol"] in seen or x.get("status") != "WATCH_PAPER_ONLY"):
            raise ValueError("Invalid or duplicated WATCH candidate")
        seen.add(x["symbol"])
        values = ("price_usd", "move15_pct", "volume_accel", score_key)
        if any(isinstance(x.get(k), bool) or not isinstance(x.get(k), (int, float))
               for k in values):
            raise ValueError("Missing numerical WATCH evidence")
        if not isinstance(x.get("quote_observed_at"), str) or not x["quote_observed_at"]:
            raise ValueError("Missing quote provenance")
        row = {"rank": i, "symbol": x["symbol"], "price_usd": x["price_usd"],
               "move15_pct": x["move15_pct"], "volume_accel": x["volume_accel"],
               "score": x[score_key], "quote_observed_at": x["quote_observed_at"]}
        if with_trades:
            row["trades_24h"] = x.get("trades_24h")
        out.append(row)
    return out


def combine(paper, legacy):
    """Tie the independent lists to the exact SAME writer run without relabeling."""
    if (paper.get("schema") != 2 or paper.get("publication_mode") != "ATOMIC_LEDGER_RESULTS"
            or paper.get("status") != "SUCCESS_PAPER_ONLY"
            or paper.get("remote_readback_verified") is not True
            or paper.get("production_applied") is not False
            or paper.get("buy_approved") is not False
            or not SHA64.fullmatch(paper.get("ledger_sha256", ""))):
        raise ValueError("Paper publication is not a verified atomic source")
    writer_id = str(paper.get("run_id", ""))
    shadow_id = str(legacy.get("run_id", ""))
    sha = paper.get("source_sha", "")
    if (not writer_id.isdigit() or not shadow_id.isdigit() or writer_id == shadow_id
            or not SHA40.fullmatch(sha) or legacy.get("source_sha") != sha
            or str(legacy.get("trigger_paper_run_id")) != writer_id
            or legacy.get("mode") != "LEGACY_INSPIRED_SHADOW"
            or legacy.get("independent_execution") is not True
            or legacy.get("production_applied") is not False
            or legacy.get("buy_approved") is not False
            or legacy.get("trade_executed") is not False
            or legacy.get("held_out_lift") is not None
            or legacy.get("status") not in ("WATCH_PAPER_ONLY", "NO_SIGNALS")):
        raise ValueError("Legacy shadow is not independently linked to this paper scan")
    challenger = _ranked(paper.get("candidates"), "challenger_score")
    legacy_watch = _ranked(legacy.get("candidates"), "legacy_score", with_trades=True)
    if legacy.get("status") == "NO_SIGNALS" and legacy_watch:
        raise ValueError("Legacy NO_SIGNALS contradicted by WATCH candidates")
    if legacy.get("status") == "WATCH_PAPER_ONLY" and not legacy_watch:
        raise ValueError("Legacy WATCH lacks candidates")
    scores = paper.get("rankings", {})
    if (scores.get("population") != "SAME_OHLC_VERIFIED_WATCH_POOL"
            or not isinstance(scores.get("challenger"), list)
            or [x["symbol"] for x in scores["challenger"]] !=
               [x["symbol"] for x in challenger]):
        raise ValueError("Missing independent challenger ranking identity")
    legacy_set = {x["symbol"] for x in legacy_watch}
    overlap = [x["symbol"] for x in challenger if x["symbol"] in legacy_set]
    return {
        "schema": 1, "mode": "SAME_WRITER_DUAL_SCANNER_REPORT",
        "status": "TWO_INDEPENDENT_SOURCES_VERIFIED", "paper_only": True,
        "writer_run_id": writer_id, "legacy_run_id": shadow_id,
        "source_sha": sha, "ledger_generation": paper["ledger_generation"],
        "ledger_sha256": paper["ledger_sha256"],
        "paper_as_of": paper["as_of"], "legacy_as_of": legacy["as_of"],
        "paper_observed_markets": paper["observed_markets"],
        "legacy_status": legacy["status"],
        "challenger_watch": challenger, "legacy_watch": legacy_watch,
        "baseline_rankings": scores["baseline"],
        "overlap_symbols": overlap,
        "overlap_basis": "same writer run; independent source artifacts; exact /USD symbols",
        "read_only_learning": "SEPARATE_WORKFLOW",
        "production_applied": False, "buy_approved": False,
    }


def markdown(report):
    out = [
        "# Cryptoscanner — challenger and independent legacy-inspired WATCH",
        "",
        "Paper only · high risk · scores are NOT calibrated probabilities · no BUY authorization",
        "",
        f"**Writer:** {report['writer_run_id']} · **Generation:** {report['ledger_generation']} · "
        f"**Legacy run:** {report['legacy_run_id']}",
        f"**Main quote time:** {report['paper_as_of']} · **Legacy report time:** {report['legacy_as_of']}",
        "",
        "## Challenger-scored WATCH (original canonical scanner)",
        "| # | Symbol | USD | Challenger score | 15m move | Volume x |",
        "|---:|---|---:|---:|---:|---:|",
    ]
    for x in report["challenger_watch"]:
        mark = " ⭐" if x["symbol"] in report["overlap_symbols"] else ""
        out.append(f"| {x['rank']} | {x['symbol']}{mark} | {x['price_usd']:.8g} | "
                   f"{x['score']:.2f} | {x['move15_pct']:+.2f}% | {x['volume_accel']:.2f}x |")
    out.extend([
        "",
        "## Independent legacy-inspired WATCH (separate Kraken sampling)",
        "| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h |",
        "|---:|---|---:|---:|---:|---:|---:|",
    ])
    if not report["legacy_watch"]:
        out.append("| — | No confirmed WATCH signals | — | — | — | — | — |")
    for x in report["legacy_watch"]:
        mark = " ⭐" if x["symbol"] in report["overlap_symbols"] else ""
        out.append(f"| {x['rank']} | {x['symbol']}{mark} | {x['price_usd']:.8g} | "
                   f"{x['score']:.2f} | {x['move15_pct']:+.2f}% | "
                   f"{x['volume_accel']:.2f}x | {x['trades_24h']} |")
    out.extend([
        "", "**Same-run overlap:** " +
        (", ".join(report["overlap_symbols"]) if report["overlap_symbols"] else "None"),
        "A ⭐ means both independently executed scanners identified the exact same /USD market.",
        "Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.",
        "Freshness must be checked using each candidate's quote_observed_at at delivery.",
        "Read-only learning is separate; no production-scoring promotion or trading.",
    ])
    return "\n".join(out) + "\n"


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--paper-dir", required=True)
    parser.add_argument("--legacy-dir", required=True)
    parser.add_argument("--paper-run-id", required=True)
    parser.add_argument("--shadow-run-id", required=True)
    parser.add_argument("--output-dir", required=True)
    args = parser.parse_args()
    paper = _read_verified(args.paper_dir, ["results.json", "results.md"], "SHA256SUMS")
    legacy = _read_verified(args.legacy_dir, ["legacy-shadow.json"], "LEGACY_SHA256SUMS")
    report = combine(paper, legacy)
    if (report["writer_run_id"] != args.paper_run_id
            or report["legacy_run_id"] != args.shadow_run_id):
        raise ValueError("Wrong writer/shadow workflow binding")
    output = Path(args.output_dir)
    output.mkdir(parents=True, exist_ok=True)
    items = {
        "dual-scanner.json": json.dumps(report, sort_keys=True, separators=(",", ":"),
                                       allow_nan=False).encode() + b"\n",
        "dual-scanner.md": markdown(report).encode(),
    }
    for name, data in items.items():
        (output / name).write_bytes(data)
    (output / "DUAL_SHA256SUMS").write_text("".join(
        hashlib.sha256(data).hexdigest() + "  " + name + "\n" for name, data in items.items()))
    print("DUAL_SCANNER_RESULTS_JSON " + json.dumps({
        "sha256": hashlib.sha256(items["dual-scanner.json"]).hexdigest(), "report": report,
    }, sort_keys=True, separators=(",", ":"), allow_nan=False))


if __name__ == "__main__":
    main()
