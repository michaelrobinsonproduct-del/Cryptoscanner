# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-09T01:19:31.136424+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/42544876974
**Source SHA:** 2e61fb99d99df9994e5a3e59add72d1b2b1fac71
**Ledger commit:** d2eba9d19ebbde65ace3078a1302a6e49f2a5fb1
**Ledger generation:** 174 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 7s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 624; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 606; valid market observations: 606; OHLC screened: 24.

## Top WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | Confidence / risk | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---|---|---|
| 1 | ZEC/USD | 1232.43 | 73.076 | 63.434 | +1.65% | -0.24% | 2.09x | 6.3 | 2026-11-09T01:19:24.635390+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 2 | UAI/USD | 0.06494 | 70.094 | 67.641 | +5.89% | +0.90% | 0.80x | 24.6 | 2026-11-09T01:19:24.635390+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 3 | ENA/USD | 0.1515 | 65.887 | 62.554 | +2.02% | -0.33% | 1.50x | 13.2 | 2026-11-09T01:19:24.635390+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 4 | SUI/USD | 0.8349 | 62.827 | 66.773 | +1.77% | -0.29% | 0.75x | 1.2 | 2026-11-09T01:19:24.635390+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 5 | PEPE/USD | 5.053e-06 | 62.601 | 66.042 | +2.14% | -0.16% | 0.73x | 7.9 | 2026-11-09T01:19:24.635390+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 6 | XLM/USD | 0.146971 | 60.273 | 57.481 | +0.54% | -0.21% | 1.38x | 2.6 | 2026-11-09T01:19:24.635390+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 7 | UNI/USD | 6.897 | 59.667 | 53.304 | +1.67% | -0.27% | 1.77x | 9.1 | 2026-11-09T01:19:24.635390+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 8 | SOL/USD | 87.27 | 58.710 | 61.066 | +0.95% | -0.17% | 0.85x | 1.1 | 2026-11-09T01:19:24.635390+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 9 | TAO/USD | 217.7286 | 58.595 | 52.645 | +0.45% | -0.61% | 1.90x | 9.1 | 2026-11-09T01:19:24.635390+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 10 | AAVE/USD | 128.35 | 57.501 | 53.926 | +1.91% | +0.09% | 1.31x | 5.5 | 2026-11-09T01:19:24.635390+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 11 | PAXG/USD | 4092.59 | 56.355 | 41.554 | +1.13% | -0.04% | 4.03x | 1.2 | 2026-11-09T01:19:24.635390+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 12 | AUD/USD | 0.68858 | 55.069 | 39.866 | +0.26% | +0.04% | 10.02x | 1.2 | 2026-11-09T01:19:24.635390+00:00 | NOT CALIBRATED / HIGH | WATCH |

**Confidence:** uncalibrated research heuristics, NOT validated probabilities. **BUY:** none authorized. Numerical baseline/challenger scores are uncalibrated paper-only ranking values, not probabilities or validated improvement.

## Learning and coverage

| Forward horizon | Evidence status | Verified matured / hits |
|---|---|---|
| 1h | PER HORIZON NOT INDEPENDENTLY VERIFIED | NOT VERIFIED |
| 6h | PER HORIZON NOT INDEPENDENTLY VERIFIED | NOT VERIFIED |
| 24h | PER HORIZON NOT INDEPENDENTLY VERIFIED | NOT VERIFIED |
| 48h | PER HORIZON NOT INDEPENDENTLY VERIFIED | NOT VERIFIED |

- Persisted scans: 174; predictions: 1496; observations: 105152.
- Matured sampled outcomes across 1/6/24/48h: 816; gap abstentions: 4379. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 0 (sampled only; not a success-rate estimate).
- False positives / missed movers: NOT VERIFIED without eligible continuous outcome coverage.
- Baseline vs challenger: recorded as-of; unbiased held-out lift NOT MEASURED.
- Online Kraken /USD stablecoin-base pairs excluded: 18 (counted from this scan's online AssetPairs metadata, not inferred from price).
- Stablecoin base exclusions: BRL1, BUSD, DAI, EUR, EURC, EUROP, EURQ, EURR, EURT, FDUSD, FRAX, GUSD, PYUSD, QCAD, RLUSD, TGBP, TUSD, USD, USD1, USDC, USDD, USDE, USDG, USDQ, USDR, USDS, USDT, ZUSD.
- DEX: NOT USED; no DEX freshness gate.
- OHLC screening abstentions: 4; details in immutable scan JSON artifact.
- Storage: checksum-sealed ledger pushed non-force and read back before this report. Independent artifact recovery is NOT VERIFIED by this scan alone.
- Errors: none in successful committed scan; a failed workflow must not publish a SUCCESS report.
