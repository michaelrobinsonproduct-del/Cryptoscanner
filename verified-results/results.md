# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-09T15:46:42.966215+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/42647863295
**Source SHA:** 69b32fce88f9296ad7d9292e14e64b61178763c7
**Ledger commit:** 6c269ab8f9066002252dfabc641108053e00e728
**Ledger generation:** 200 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 9s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 624; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 606; valid market observations: 606; OHLC screened: 24.

## Top WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | Confidence / risk | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---|---|---|
| 1 | ONDO/USD | 0.38632 | 122.166 | 94.343 | +9.88% | +2.56% | 27.60x | 0.3 | 2026-11-09T15:46:34.459803+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 2 | ENA/USD | 0.1571 | 110.891 | 92.354 | +5.79% | +0.71% | 2.69x | 6.4 | 2026-11-09T15:46:34.459803+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 3 | SUI/USD | 0.8676 | 103.055 | 94.697 | +5.75% | +0.99% | 1.34x | 1.2 | 2026-11-09T15:46:34.459803+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 4 | AAVE/USD | 133.01 | 102.316 | 85.013 | +5.61% | +0.46% | 3.18x | 7.5 | 2026-11-09T15:46:34.459803+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 5 | PEPE/USD | 5.289e-06 | 101.855 | 94.324 | +6.91% | +0.82% | 1.34x | 11.4 | 2026-11-09T15:46:34.459803+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 6 | LINK/USD | 10.80647 | 91.948 | 79.032 | +3.90% | +0.82% | 1.88x | 6.5 | 2026-11-09T15:46:34.459803+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 7 | XDG/USD | 0.0707392 | 89.217 | 73.924 | +2.70% | +0.56% | 2.25x | 0.0 | 2026-11-09T15:46:34.459803+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 8 | ARB/USD | 0.183 | 85.210 | 82.351 | +10.31% | +1.78% | 0.40x | 10.9 | 2026-11-09T15:46:34.459803+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 9 | LTC/USD | 52.21 | 83.710 | 78.719 | +4.27% | +0.13% | 1.43x | 1.9 | 2026-11-09T15:46:34.459803+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 10 | ADA/USD | 0.182969 | 83.307 | 83.092 | +4.54% | +0.62% | 0.71x | 5.9 | 2026-11-09T15:46:34.459803+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 11 | TAO/USD | 225.1018 | 81.017 | 79.162 | +3.85% | +0.38% | 0.99x | 5.5 | 2026-11-09T15:46:34.459803+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 12 | ETH/USD | 2145.88 | 77.252 | 61.918 | +0.99% | +0.58% | 2.24x | 0.0 | 2026-11-09T15:46:34.459803+00:00 | NOT CALIBRATED / HIGH | WATCH |

**Confidence:** uncalibrated research heuristics, NOT validated probabilities. **BUY:** none authorized. Numerical baseline/challenger scores are uncalibrated paper-only ranking values, not probabilities or validated improvement.

## Learning and coverage

| Forward horizon | Evidence status | Verified matured / hits |
|---|---|---|
| 1h | PER HORIZON NOT INDEPENDENTLY VERIFIED | NOT VERIFIED |
| 6h | PER HORIZON NOT INDEPENDENTLY VERIFIED | NOT VERIFIED |
| 24h | PER HORIZON NOT INDEPENDENTLY VERIFIED | NOT VERIFIED |
| 48h | PER HORIZON NOT INDEPENDENTLY VERIFIED | NOT VERIFIED |

- Persisted scans: 200; predictions: 1803; observations: 120907.
- Matured sampled outcomes across 1/6/24/48h: 1033; gap abstentions: 4866. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 0 (sampled only; not a success-rate estimate).
- False positives / missed movers: NOT VERIFIED without eligible continuous outcome coverage.
- Baseline vs challenger: recorded as-of; unbiased held-out lift NOT MEASURED.
- Online Kraken /USD stablecoin-base pairs excluded: 18 (counted from this scan's online AssetPairs metadata, not inferred from price).
- Stablecoin base exclusions: BRL1, BUSD, DAI, EUR, EURC, EUROP, EURQ, EURR, EURT, FDUSD, FRAX, GUSD, PYUSD, QCAD, RLUSD, TGBP, TUSD, USD, USD1, USDC, USDD, USDE, USDG, USDQ, USDR, USDS, USDT, ZUSD.
- DEX: NOT USED; no DEX freshness gate.
- OHLC screening abstentions: 4; details in immutable scan JSON artifact.
- Storage: checksum-sealed ledger pushed non-force and read back before this report. Independent artifact recovery is NOT VERIFIED by this scan alone.
- Errors: none in successful committed scan; a failed workflow must not publish a SUCCESS report.
