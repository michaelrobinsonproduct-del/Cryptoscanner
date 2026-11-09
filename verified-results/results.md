# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-09T21:55:46.678034+00:00
**GitHub trigger:** authenticated issue heartbeat (verified event=issue_comment; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/42706864682
**Source SHA:** 47efb405551d493df87bca8b2583b5611396f1fa
**Ledger commit:** 2fcb65e10499cbfec1cd7b5cfb232d5ec6252a6b
**Ledger generation:** 212 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 8s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 624; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 606; valid market observations: 602; OHLC screened: 24.

## Top WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | Confidence / risk | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---|---|---|
| 1 | ONDO/USD | 0.37335 | 106.453 | 97.705 | +6.19% | +0.08% | 1.84x | 0.3 | 2026-11-09T21:55:38.453613+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 2 | AVAX/USD | 8.641 | 105.291 | 96.526 | +8.98% | +0.23% | 1.76x | 6.9 | 2026-11-09T21:55:38.453613+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 3 | UNI/USD | 7.0721 | 96.302 | 81.909 | +4.25% | -0.12% | 3.08x | 5.7 | 2026-11-09T21:55:38.453613+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 4 | ENA/USD | 0.1546 | 94.550 | 77.278 | +4.11% | +0.45% | 4.84x | 13.0 | 2026-11-09T21:55:38.453613+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 5 | LIGHTER/USD | 3.251 | 91.403 | 76.250 | +6.31% | +0.03% | 18.93x | 9.2 | 2026-11-09T21:55:38.453613+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 6 | XDG/USD | 0.0699342 | 79.214 | 65.742 | +1.54% | +0.04% | 2.33x | 0.0 | 2026-11-09T21:55:38.453613+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 7 | SUI/USD | 0.8455 | 78.933 | 75.825 | +3.06% | +0.06% | 1.28x | 1.2 | 2026-11-09T21:55:38.453613+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 8 | VVV/USD | 21.859 | 77.328 | 78.399 | +8.97% | +0.02% | 0.88x | 5.9 | 2026-11-09T21:55:38.453613+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 9 | XLM/USD | 0.147413 | 74.628 | 59.906 | +0.84% | -0.06% | 3.78x | 2.0 | 2026-11-09T21:55:38.453613+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 10 | ARB/USD | 0.1749 | 73.491 | 78.947 | +5.42% | +0.11% | 0.40x | 5.7 | 2026-11-09T21:55:38.453613+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 11 | HYPE/USD | 75.27 | 71.175 | 61.855 | +1.07% | +0.29% | 1.79x | 1.3 | 2026-11-09T21:55:38.453613+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 12 | GBP/USD | 1.34378 | 68.983 | 59.144 | +0.61% | +0.03% | 1.97x | 0.3 | 2026-11-09T21:55:38.453613+00:00 | NOT CALIBRATED / HIGH | WATCH |

**Confidence:** uncalibrated research heuristics, NOT validated probabilities. **BUY:** none authorized. Numerical baseline/challenger scores are uncalibrated paper-only ranking values, not probabilities or validated improvement.

## Learning and coverage

| Forward horizon | Evidence status | Verified matured / hits |
|---|---|---|
| 1h | PER HORIZON NOT INDEPENDENTLY VERIFIED | NOT VERIFIED |
| 6h | PER HORIZON NOT INDEPENDENTLY VERIFIED | NOT VERIFIED |
| 24h | PER HORIZON NOT INDEPENDENTLY VERIFIED | NOT VERIFIED |
| 48h | PER HORIZON NOT INDEPENDENTLY VERIFIED | NOT VERIFIED |

- Persisted scans: 212; predictions: 1947; observations: 128167.
- Matured sampled outcomes across 1/6/24/48h: 1105; gap abstentions: 5192. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 0 (sampled only; not a success-rate estimate).
- False positives / missed movers: NOT VERIFIED without eligible continuous outcome coverage.
- Baseline vs challenger: recorded as-of; unbiased held-out lift NOT MEASURED.
- Online Kraken /USD stablecoin-base pairs excluded: 18 (counted from this scan's online AssetPairs metadata, not inferred from price).
- Stablecoin base exclusions: BRL1, BUSD, DAI, EUR, EURC, EUROP, EURQ, EURR, EURT, FDUSD, FRAX, GUSD, PYUSD, QCAD, RLUSD, TGBP, TUSD, USD, USD1, USDC, USDD, USDE, USDG, USDQ, USDR, USDS, USDT, ZUSD.
- DEX: NOT USED; no DEX freshness gate.
- OHLC screening abstentions: 7; details in immutable scan JSON artifact.
- Storage: checksum-sealed ledger pushed non-force and read back before this report. Independent artifact recovery is NOT VERIFIED by this scan alone.
- Errors: none in successful committed scan; a failed workflow must not publish a SUCCESS report.
