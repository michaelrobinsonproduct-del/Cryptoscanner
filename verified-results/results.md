# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-10T19:05:03.673435+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/42881329352
**Source SHA:** a401ca9b3fa5588c6780befb93e5eb91f2431f0f
**Ledger commit:** 1363f69d80bed762257f8bd54c5d671221c55e73
**Ledger generation:** 245 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 6s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 624; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 606; valid market observations: 599; OHLC screened: 21.

## Top WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | Confidence / risk | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---|---|---|
| 1 | TON/USD | 1.108 | 79.657 | 70.670 | +6.54% | +0.27% | 1.76x | 18.1 | 2026-11-10T19:04:57.304506+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 2 | NIGHT/USD | 0.04169 | 73.035 | 60.016 | +2.99% | -0.02% | 2.31x | 9.6 | 2026-11-10T19:04:57.304506+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 3 | PEPE/USD | 5.285e-06 | 71.438 | 73.490 | +3.18% | +0.30% | 0.64x | 7.6 | 2026-11-10T19:04:57.304506+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 4 | LIGHTER/USD | 3.36 | 63.901 | 53.511 | +3.93% | +0.33% | 1.88x | 17.8 | 2026-11-10T19:04:57.304506+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 5 | TRUMP/USD | 1.136 | 55.838 | 39.070 | +1.43% | +0.35% | 4.11x | 8.8 | 2026-11-10T19:04:57.304506+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 6 | XDC/USD | 0.03005 | 48.340 | 45.940 | +1.97% | -0.33% | 1.41x | 16.7 | 2026-11-10T19:04:57.304506+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 7 | CAP/USD | 0.102188 | 47.626 | 59.178 | +3.37% | -0.88% | 0.28x | 6.1 | 2026-11-10T19:04:57.304506+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 8 | ZRO/USD | 1.483 | 39.419 | 37.892 | +0.47% | +1.15% | 0.58x | 20.2 | 2026-11-10T19:04:57.304506+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 9 | UAI/USD | 0.0393 | 35.191 | 30.044 | +1.92% | -1.97% | 2.97x | 33.0 | 2026-11-10T19:04:57.304506+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 10 | MEGA/USD | 0.05069 | 32.415 | 28.482 | +1.81% | -0.71% | 1.75x | 33.6 | 2026-11-10T19:04:57.304506+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 11 | KAS/USD | 0.02993 | 30.416 | 31.273 | +0.64% | +0.00% | 0.91x | 13.4 | 2026-11-10T19:04:57.304506+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 12 | ICP/USD | 2.405 | 25.902 | 28.489 | +0.29% | -0.04% | 0.76x | 12.5 | 2026-11-10T19:04:57.304506+00:00 | NOT CALIBRATED / HIGH | WATCH |

**Confidence:** uncalibrated research heuristics, NOT validated probabilities. **BUY:** none authorized. Numerical baseline/challenger scores are uncalibrated paper-only ranking values, not probabilities or validated improvement.

## Learning and coverage

| Forward horizon | Evidence status | Verified matured / hits |
|---|---|---|
| 1h | PER HORIZON NOT INDEPENDENTLY VERIFIED | NOT VERIFIED |
| 6h | PER HORIZON NOT INDEPENDENTLY VERIFIED | NOT VERIFIED |
| 24h | PER HORIZON NOT INDEPENDENTLY VERIFIED | NOT VERIFIED |
| 48h | PER HORIZON NOT INDEPENDENTLY VERIFIED | NOT VERIFIED |

- Persisted scans: 245; predictions: 2256; observations: 146961.
- Matured sampled outcomes across 1/6/24/48h: 1311; gap abstentions: 6262. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 0 (sampled only; not a success-rate estimate).
- False positives / missed movers: NOT VERIFIED without eligible continuous outcome coverage.
- Baseline vs challenger: recorded as-of; unbiased held-out lift NOT MEASURED.
- Online Kraken /USD stablecoin-base pairs excluded: 18 (counted from this scan's online AssetPairs metadata, not inferred from price).
- Stablecoin base exclusions: BRL1, BUSD, DAI, EUR, EURC, EUROP, EURQ, EURR, EURT, FDUSD, FRAX, GUSD, PYUSD, QCAD, RLUSD, TGBP, TUSD, USD, USD1, USDC, USDD, USDE, USDG, USDQ, USDR, USDS, USDT, ZUSD.
- DEX: NOT USED; no DEX freshness gate.
- OHLC screening abstentions: 9; details in immutable scan JSON artifact.
- Storage: checksum-sealed ledger pushed non-force and read back before this report. Independent artifact recovery is NOT VERIFIED by this scan alone.
- Errors: none in successful committed scan; a failed workflow must not publish a SUCCESS report.
