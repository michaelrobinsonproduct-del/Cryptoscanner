# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-10T08:52:26.713828+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/42785878140
**Source SHA:** 47e99644e7d7ff00dca3e241f2bbbf508d9a3b56
**Ledger commit:** b3d685d3871d6cbc3c064b16ed9c85ec21211d59
**Ledger generation:** 229 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 8s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 624; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 606; valid market observations: 561; OHLC screened: 24.

## Top WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | Confidence / risk | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---|---|---|
| 1 | PEPE/USD | 5.329e-06 | 80.822 | 80.471 | +4.04% | -0.41% | 1.24x | 5.6 | 2026-11-10T08:52:18.604014+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 2 | NIGHT/USD | 0.04318 | 77.489 | 80.010 | +6.67% | -0.39% | 0.94x | 9.3 | 2026-11-10T08:52:18.604014+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 3 | XDC/USD | 0.03138 | 74.950 | 76.107 | +6.48% | -0.51% | 1.14x | 15.9 | 2026-11-10T08:52:18.604014+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 4 | ADA/USD | 0.178913 | 58.875 | 56.136 | +0.93% | +0.16% | 1.19x | 2.5 | 2026-11-10T08:52:18.604014+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 5 | CC/USD | 0.09245 | 52.936 | 40.254 | +1.07% | +0.03% | 2.25x | 4.3 | 2026-11-10T08:52:18.604014+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 6 | UNI/USD | 7.065 | 52.183 | 51.785 | +1.36% | +0.57% | 0.76x | 7.4 | 2026-11-10T08:52:18.604014+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 7 | XLM/USD | 0.147959 | 47.334 | 51.349 | +0.43% | +0.17% | 0.51x | 3.3 | 2026-11-10T08:52:18.604014+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 8 | TRX/USD | 0.318998 | 47.217 | 43.870 | +0.52% | -0.01% | 1.34x | 0.8 | 2026-11-10T08:52:18.604014+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 9 | HBAR/USD | 0.06704 | 41.126 | 37.201 | +0.46% | +0.15% | 1.32x | 6.0 | 2026-11-10T08:52:18.604014+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 10 | FET/USD | 0.1463 | 39.355 | 40.422 | +1.74% | +0.27% | 0.76x | 6.8 | 2026-11-10T08:52:18.604014+00:00 | NOT CALIBRATED / HIGH | WATCH |

**Confidence:** uncalibrated research heuristics, NOT validated probabilities. **BUY:** none authorized. Numerical baseline/challenger scores are uncalibrated paper-only ranking values, not probabilities or validated improvement.

## Learning and coverage

| Forward horizon | Evidence status | Verified matured / hits |
|---|---|---|
| 1h | PER HORIZON NOT INDEPENDENTLY VERIFIED | NOT VERIFIED |
| 6h | PER HORIZON NOT INDEPENDENTLY VERIFIED | NOT VERIFIED |
| 24h | PER HORIZON NOT INDEPENDENTLY VERIFIED | NOT VERIFIED |
| 48h | PER HORIZON NOT INDEPENDENTLY VERIFIED | NOT VERIFIED |

- Persisted scans: 229; predictions: 2093; observations: 137515.
- Matured sampled outcomes across 1/6/24/48h: 1189; gap abstentions: 5853. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 0 (sampled only; not a success-rate estimate).
- False positives / missed movers: NOT VERIFIED without eligible continuous outcome coverage.
- Baseline vs challenger: recorded as-of; unbiased held-out lift NOT MEASURED.
- Online Kraken /USD stablecoin-base pairs excluded: 18 (counted from this scan's online AssetPairs metadata, not inferred from price).
- Stablecoin base exclusions: BRL1, BUSD, DAI, EUR, EURC, EUROP, EURQ, EURR, EURT, FDUSD, FRAX, GUSD, PYUSD, QCAD, RLUSD, TGBP, TUSD, USD, USD1, USDC, USDD, USDE, USDG, USDQ, USDR, USDS, USDT, ZUSD.
- DEX: NOT USED; no DEX freshness gate.
- OHLC screening abstentions: 14; details in immutable scan JSON artifact.
- Storage: checksum-sealed ledger pushed non-force and read back before this report. Independent artifact recovery is NOT VERIFIED by this scan alone.
- Errors: none in successful committed scan; a failed workflow must not publish a SUCCESS report.
