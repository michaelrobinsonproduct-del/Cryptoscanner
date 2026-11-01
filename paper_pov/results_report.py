"""Public, deterministic, paper-only scan results from a real persisted run.

No trading authorization, calibrated confidence, exchange-event timestamp,
held-out lift, or complete missed-mover claim is inferred here.
"""
import argparse
import datetime as dt
import hashlib
import json
import math
import os
import re
import tempfile
from pathlib import Path

from .scanner import STABLE, atomic_json, utc

SHA = re.compile(r"[0-9a-f]{40}")
RUN = re.compile(r"[0-9]+")
PAIR = re.compile(r"[A-Za-z0-9._/-]{1,64}")
HORIZONS = (1, 6, 24, 48)


def _number(value, label):
    if isinstance(value, bool) or not isinstance(value, (int, float)):
        raise ValueError("Invalid " + label)
    n = float(value)
    if not math.isfinite(n):
        raise ValueError("Nonfinite " + label)
    return n


def _utc(value):
    if not isinstance(value, str):
        raise ValueError("Missing UTC timestamp")
    return utc(value)


def render(scan, score, *, run_id, source_sha, ledger_commit):
    if not RUN.fullmatch(str(run_id)) or not SHA.fullmatch(source_sha) or not SHA.fullmatch(ledger_commit):
        raise ValueError("Missing immutable GitHub run/source/ledger identity")
    if scan.get("mode") != "PAPER_ONLY" or scan.get("buy_approved") is not False:
        raise ValueError("Non-paper or trading-authorized scan")
    if scan.get("production_applied") is not False or score.get("production_applied") is not False:
        raise ValueError("Production application is prohibited")
    if scan.get("forward_labels") != 0 or score.get("held_out_lift") is not None:
        raise ValueError("Unverified predictive claim")
    as_of = _utc(scan["as_of"])
    if _utc(scan["started_at"]) > as_of:
        raise ValueError("Invalid scan clock")
    watches = scan["watch"]
    observations = scan["observations"]
    if not isinstance(watches, list) or not 1 <= len(watches) <= 12:
        raise ValueError("Missing or excessive watch candidates")
    if not isinstance(observations, list) or len(observations) != scan.get("observed_markets"):
        raise ValueError("Missing market universe evidence")
    if type(score.get("generation")) is not int or score["generation"] < 1:
        raise ValueError("Unpersisted ledger generation")
    for field in ("actual_scans", "immutable_predictions", "market_observations",
                  "matured_labels", "gap_abstentions", "observed_30pct_hits"):
        if type(score.get(field)) is not int or score[field] < 0:
            raise ValueError("Invalid scoreboard " + field)
    if score["actual_scans"] != score["generation"] or score["immutable_predictions"] < len(watches):
        raise ValueError("Inconsistent scoreboard")
    if score["observed_30pct_hits"] > score["matured_labels"]:
        raise ValueError("Observed hits exceed eligible matured labels")
    for field in ("eligible_pairs", "observed_markets", "ohlc_screened"):
        if type(scan.get(field)) is not int or scan[field] < 0:
            raise ValueError("Invalid market coverage " + field)
    if not len(observations) <= scan["eligible_pairs"] or not scan["ohlc_screened"] <= len(observations):
        raise ValueError("Market coverage exceeds observed/eligible universe")
    if score["market_observations"] < len(observations):
        raise ValueError("Unpersisted observations")
    if not re.fullmatch(r"[0-9a-f]{64}", score.get("ledger_sha256", "")):
        raise ValueError("Missing sealed ledger checksum")
    ages = []
    quotes = {}
    for o in observations:
        pair = o.get("pair")
        if not isinstance(pair, str) or not PAIR.fullmatch(pair) or pair in quotes:
            raise ValueError("Invalid or duplicate observed pair")
        age = (as_of - _utc(o["observed_at"])).total_seconds()
        if not 0 <= age <= 600 or _number(o["price"], "quote price") <= 0:
            raise ValueError("Stale, future, or invalid quote")
        ages.append(age)
        quotes[pair] = o
    lines = [
        "# Kraken paper scanner — verified results",
        "",
        "**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders",
        "",
        f"**UTC as-of:** {as_of.isoformat()}  ",
        f"**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/{run_id}  ",
        f"**Source SHA:** {source_sha}  ",
        f"**Ledger commit:** {ledger_commit}  ",
        f"**Ledger generation:** {score['generation']} (remote push/readback verified)",
        "",
        f"**Freshness:** Kraken public ticker client-observed, max quote age {max(ages):.0f}s (limit 600s). "
        "Ticker exchange-event freshness is NOT independently proven.",
        f"**Eligible Kraken USD pairs:** {scan['eligible_pairs']}; "
        f"valid market observations: {len(observations)}; OHLC screened: {scan['ohlc_screened']}.",
        "",
        "## Top WATCH candidates — paper only",
        "",
        "| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | Confidence / risk | Status |",
        "|---:|---|---:|---:|---:|---:|---:|---:|---:|---|---|---|",
    ]
    records = []
    seen = set()
    for index, p in enumerate(watches, 1):
        pair, symbol = p.get("pair"), p.get("symbol")
        if not isinstance(pair, str) or not PAIR.fullmatch(pair) or pair in seen:
            raise ValueError("Duplicate or invalid prediction pair")
        if not isinstance(symbol, str) or not PAIR.fullmatch(symbol) or "/" not in symbol:
            raise ValueError("Invalid prediction symbol")
        if symbol.split("/")[0].upper() in STABLE:
            raise ValueError("Stablecoin escaped scanner exclusions")
        if p.get("rank") != index or p.get("status") != "PAPER_WATCH" or _utc(p["as_of"]) != as_of:
            raise ValueError("Prediction rank/status/as-of mismatch")
        quote = quotes.get(pair)
        if quote is None or _number(p["price"], "watch price") != _number(quote["price"], "quote price"):
            raise ValueError("Prediction price lacks same-run quote provenance")
        if _utc(p["quote_observed_at"]) != _utc(quote["observed_at"]):
            raise ValueError("Prediction quote timestamp mismatch")
        if _number(p["ohlc_age_seconds"], "OHLC age") < 0 or p["ohlc_age_seconds"] > 600:
            raise ValueError("Stale OHLC")
        for key in ("move_since_utc_open_pct", "move15_pct", "volume_accel",
                    "spread_bps", "baseline_score", "challenger_score"):
            _number(p[key], key)
        price = _number(p["price"], "watch price")
        seen.add(pair)
        records.append({"rank": index, "symbol": symbol, "price_usd": price,
                        "status": "WATCH_PAPER_ONLY", "confidence": "NOT_CALIBRATED",
                        "risk": "HIGH_UNVALIDATED", "move_since_utc_open_pct": p["move_since_utc_open_pct"],
                        "move15_pct": p["move15_pct"], "volume_accel": p["volume_accel"],
                        "spread_bps": p["spread_bps"], "baseline_score": p["baseline_score"],
                        "challenger_score": p["challenger_score"],
                        "quote_observed_at": quote["observed_at"],
                        "ohlc_age_seconds": p["ohlc_age_seconds"],
                        "prediction_id": p["prediction_id"]})
        lines.append(f"| {index} | {symbol} | {price:.8g} | "
                     f"{p['challenger_score']:.3f} | {p['baseline_score']:.3f} | "
                     f"{p['move_since_utc_open_pct']:+.2f}% | {p['move15_pct']:+.2f}% | "
                     f"{p['volume_accel']:.2f}x | {p['spread_bps']:.1f} | "
                     f"{_utc(quote['observed_at']).isoformat()} | "
                     "NOT CALIBRATED / HIGH | WATCH |")
    # The aggregate ledger count cannot be allocated to individual horizons
    # without independent evidence. Never manufacture a per-horizon success.
    horizon_status = ("NOT_MATURED_OR_INELIGIBLE" if score["matured_labels"] == 0
                      else "PER_HORIZON_NOT_INDEPENDENTLY_VERIFIED")
    horizons = {str(h): {"status": horizon_status, "verified_matured_count": None,
                         "verified_hits": None} for h in HORIZONS}
    abstentions = scan.get("abstentions", [])
    if not isinstance(abstentions, list):
        raise ValueError("Invalid abstentions")
    lines.extend([
        "",
        "**Confidence:** uncalibrated research heuristics, NOT validated probabilities. "
        "**BUY:** none authorized. Numerical baseline/challenger scores are uncalibrated paper-only ranking values, not probabilities or validated improvement.",
        "",
        "## Learning and coverage",
        "",
        "| Forward horizon | Evidence status | Verified matured / hits |",
        "|---|---|---|",
        *[f"| {h}h | {horizon_status.replace('_', ' ')} | NOT VERIFIED |" for h in HORIZONS],
        "",
        f"- Persisted scans: {score['actual_scans']}; predictions: {score['immutable_predictions']}; "
        f"observations: {score['market_observations']}.",
        f"- Matured sampled outcomes across 1/6/24/48h: {score['matured_labels']}; "
        f"gap abstentions: {score['gap_abstentions']}. "
        + ("All horizons NOT MATURED / NOT ELIGIBLE so far." if score["matured_labels"] == 0
           else "Per-horizon counts require independent audit; do not infer held-out lift."),
        f"- Observed +30% hits: {score['observed_30pct_hits']} (sampled only; not a success-rate estimate).",
        "- False positives / missed movers: NOT VERIFIED without eligible continuous outcome coverage.",
        "- Baseline vs challenger: recorded as-of; unbiased held-out lift NOT MEASURED.",
        "- Stablecoin bases excluded by scanner policy: " + ", ".join(sorted(STABLE))
        + ". Exact excluded count NOT RECORDED.",
        "- DEX: NOT USED; no DEX freshness gate.",
        f"- OHLC screening abstentions: {len(abstentions)}; "
        "details in immutable scan JSON artifact.",
        "- Storage: checksum-sealed ledger pushed non-force and read back before this report. "
        "Independent artifact recovery is NOT VERIFIED by this scan alone.",
        "- Errors: none in successful committed scan; a failed workflow must not publish a SUCCESS report.",
        "",
    ])
    payload = {"schema": 1, "status": "SUCCESS_PAPER_ONLY", "run_id": str(run_id),
               "as_of": as_of.isoformat(), "source_sha": source_sha,
               "ledger_commit": ledger_commit, "ledger_generation": score["generation"],
               "ledger_sha256": score["ledger_sha256"], "remote_readback_verified": True,
               "eligible_pairs": scan["eligible_pairs"], "observed_markets": len(observations),
               "max_client_quote_age_seconds": max(ages),
               "exchange_event_freshness_verified": False, "candidates": records,
               "stablecoin_exclusion_count": None, "abstentions": len(abstentions),
               "matured_labels": score["matured_labels"], "gap_abstentions": score["gap_abstentions"],
               "observed_30pct_hits": score["observed_30pct_hits"],
               "false_positives": None, "missed_movers": None, "held_out_lift": None,
               "horizons": horizons, "storage_recovery_verified_this_run": False,
               "dex_freshness_gated": False, "production_applied": False, "buy_approved": False}
    return payload, "\n".join(lines)


def main():
    p = argparse.ArgumentParser()
    for arg in ("scan", "scoreboard", "run-id", "source-sha", "ledger-commit", "output-dir"):
        p.add_argument("--" + arg, required=True)
    a = p.parse_args()
    scan = json.loads(Path(a.scan).read_text())
    score = json.loads(Path(a.scoreboard).read_text())
    payload, markdown = render(scan, score, run_id=a.run_id,
                               source_sha=a.source_sha, ledger_commit=a.ledger_commit)
    directory = Path(a.output_dir)
    directory.mkdir(parents=True, exist_ok=True)
    atomic_json(directory / "results.json", payload)
    fd, tmp = tempfile.mkstemp(dir=directory, prefix=".results-", suffix=".tmp")
    try:
        with os.fdopen(fd, "w") as f:
            f.write(markdown + "\n")
            f.flush()
            os.fsync(f.fileno())
        os.replace(tmp, directory / "results.md")
    finally:
        if os.path.exists(tmp):
            os.unlink(tmp)
    digests = []
    for name in ("results.json", "results.md"):
        digests.append(hashlib.sha256((directory / name).read_bytes()).hexdigest() + "  " + name)
    (directory / "SHA256SUMS").write_text("\n".join(digests) + "\n")
    print("PAPER_RESULTS_VERIFIED", a.run_id, payload["ledger_generation"],
          len(payload["candidates"]))


if __name__ == "__main__":
    main()
