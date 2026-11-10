# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-10T01:30:33.860306+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/42736065936
**Source SHA:** 32879d90c1814e81374f7fba8e155a6735f1cfc0
**Ledger commit:** bfd03a08d04ab1a36216649b44adcb42aa8c3e0b
**Ledger generation:** 221 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 9s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 624; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 606; valid market observations: 435; OHLC screened: 24.

## Top WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | Confidence / risk | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---|---|---|
| 1 | XRP/USD | 1.10267 | 74.400 | 58.265 | +0.47% | +0.23% | 2.87x | 0.1 | 2026-11-10T01:30:25.054809+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 2 | UNI/USD | 7.0227 | 66.648 | 58.477 | +0.75% | -0.26% | 1.95x | 3.6 | 2026-11-10T01:30:25.054809+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 3 | ZEC/USD | 1173.86 | 59.255 | 60.024 | +0.98% | -0.10% | 0.97x | 3.7 | 2026-11-10T01:30:25.054809+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 4 | NIGHT/USD | 0.04088 | 59.089 | 43.722 | +0.99% | +0.07% | 3.92x | 2.4 | 2026-11-10T01:30:25.054809+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 5 | ENA/USD | 0.1537 | 57.202 | 43.500 | +0.39% | -0.26% | 16.50x | 13.0 | 2026-11-10T01:30:25.054809+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 6 | AVAX/USD | 8.728 | 54.167 | 59.179 | +1.01% | +0.06% | 0.47x | 5.7 | 2026-11-10T01:30:25.054809+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 7 | PEPE/USD | 5.14e-06 | 53.070 | 54.537 | +0.35% | +0.19% | 0.76x | 5.8 | 2026-11-10T01:30:25.054809+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 8 | HBAR/USD | 0.06693 | 50.199 | 37.916 | +0.30% | +0.22% | 2.12x | 1.5 | 2026-11-10T01:30:25.054809+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 9 | ALGO/USD | 0.0928 | 49.889 | 34.458 | +0.53% | +0.09% | 4.16x | 3.2 | 2026-11-10T01:30:25.054809+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 10 | FET/USD | 0.1444 | 45.730 | 29.690 | +0.42% | +0.21% | 6.48x | 13.9 | 2026-11-10T01:30:25.054809+00:00 | NOT CALIBRATED / HIGH | WATCH |

**Confidence:** uncalibrated research heuristics, NOT validated probabilities. **BUY:** none authorized. Numerical baseline/challenger scores are uncalibrated paper-only ranking values, not probabilities or validated improvement.

## Learning and coverage

| Forward horizon | Evidence status | Verified matured / hits |
|---|---|---|
| 1h | PER HORIZON NOT INDEPENDENTLY VERIFIED | NOT VERIFIED |
| 6h | PER HORIZON NOT INDEPENDENTLY VERIFIED | NOT VERIFIED |
| 24h | PER HORIZON NOT INDEPENDENTLY VERIFIED | NOT VERIFIED |
| 48h | PER HORIZON NOT INDEPENDENTLY VERIFIED | NOT VERIFIED |

- Persisted scans: 221; predictions: 2044; observations: 133418.
- Matured sampled outcomes across 1/6/24/48h: 1189; gap abstentions: 5406. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 0 (sampled only; not a success-rate estimate).
- False positives / missed movers: NOT VERIFIED without eligible continuous outcome coverage.
- Baseline vs challenger: recorded as-of; unbiased held-out lift NOT MEASURED.
- Online Kraken /USD stablecoin-base pairs excluded: 18 (counted from this scan's online AssetPairs metadata, not inferred from price).
- Stablecoin base exclusions: BRL1, BUSD, DAI, EUR, EURC, EUROP, EURQ, EURR, EURT, FDUSD, FRAX, GUSD, PYUSD, QCAD, RLUSD, TGBP, TUSD, USD, USD1, USDC, USDD, USDE, USDG, USDQ, USDR, USDS, USDT, ZUSD.
- DEX: NOT USED; no DEX freshness gate.
- OHLC screening abstentions: 14; details in immutable scan JSON artifact.
- Storage: checksum-sealed ledger pushed non-force and read back before this report. Independent artifact recovery is NOT VERIFIED by this scan alone.
- Errors: none in successful committed scan; a failed workflow must not publish a SUCCESS report.
