# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-11T09:04:41.231063+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/42991837797
**Source SHA:** 21b4cf643df9f7a7adfddc959660920dd467c70b
**Ledger commit:** da88eec770f96cc4c4775612e7d23ab57a902a3a
**Ledger generation:** 273 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 7s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 624; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 606; valid market observations: 603; OHLC screened: 24.

## Top WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | Confidence / risk | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---|---|---|
| 1 | TAO/USD | 219.0739 | 70.006 | 57.200 | +0.41% | -0.44% | 13.49x | 1.4 | 2026-11-11T09:04:34.473036+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 2 | ETH/USD | 2058.64 | 69.188 | 57.169 | +0.39% | -0.10% | 2.25x | 1.1 | 2026-11-11T09:04:34.473036+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 3 | XLM/USD | 0.145917 | 66.458 | 52.459 | +0.92% | -0.20% | 2.54x | 4.7 | 2026-11-11T09:04:34.473036+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 4 | AVAX/USD | 8.612 | 64.425 | 72.677 | +2.94% | -0.41% | 0.38x | 5.8 | 2026-11-11T09:04:34.473036+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 5 | NIGHT/USD | 0.04365 | 56.572 | 70.861 | +4.13% | -0.89% | 0.02x | 2.3 | 2026-11-11T09:04:34.473036+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 6 | XMR/USD | 568.33 | 53.792 | 57.149 | +1.01% | -0.11% | 0.72x | 9.9 | 2026-11-11T09:04:34.473036+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 7 | INJ/USD | 8.075 | 52.720 | 43.376 | +0.87% | -1.13% | 5.18x | 8.7 | 2026-11-11T09:04:34.473036+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 8 | ADA/USD | 0.174748 | 47.193 | 56.127 | +0.54% | -0.38% | 0.30x | 5.3 | 2026-11-11T09:04:34.473036+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 9 | SUI/USD | 0.8252 | 46.424 | 55.830 | +0.29% | -0.34% | 0.23x | 2.4 | 2026-11-11T09:04:34.473036+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 10 | LINK/USD | 10.32563 | 42.945 | 50.850 | +0.40% | -0.30% | 0.36x | 5.1 | 2026-11-11T09:04:34.473036+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 11 | CC/USD | 0.09005 | 35.586 | 38.880 | +0.64% | -0.17% | 0.75x | 5.6 | 2026-11-11T09:04:34.473036+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 12 | ONDO/USD | 0.3685 | 32.024 | 39.157 | +0.49% | -0.74% | 0.66x | 7.6 | 2026-11-11T09:04:34.473036+00:00 | NOT CALIBRATED / HIGH | WATCH |

**Confidence:** uncalibrated research heuristics, NOT validated probabilities. **BUY:** none authorized. Numerical baseline/challenger scores are uncalibrated paper-only ranking values, not probabilities or validated improvement.

## Learning and coverage

| Forward horizon | Evidence status | Verified matured / hits |
|---|---|---|
| 1h | PER HORIZON NOT INDEPENDENTLY VERIFIED | NOT VERIFIED |
| 6h | PER HORIZON NOT INDEPENDENTLY VERIFIED | NOT VERIFIED |
| 24h | PER HORIZON NOT INDEPENDENTLY VERIFIED | NOT VERIFIED |
| 48h | PER HORIZON NOT INDEPENDENTLY VERIFIED | NOT VERIFIED |

- Persisted scans: 273; predictions: 2545; observations: 163792.
- Matured sampled outcomes across 1/6/24/48h: 1849; gap abstentions: 6756. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 0 (sampled only; not a success-rate estimate).
- False positives / missed movers: NOT VERIFIED without eligible continuous outcome coverage.
- Baseline vs challenger: recorded as-of; unbiased held-out lift NOT MEASURED.
- Online Kraken /USD stablecoin-base pairs excluded: 18 (counted from this scan's online AssetPairs metadata, not inferred from price).
- Stablecoin base exclusions: BRL1, BUSD, DAI, EUR, EURC, EUROP, EURQ, EURR, EURT, FDUSD, FRAX, GUSD, PYUSD, QCAD, RLUSD, TGBP, TUSD, USD, USD1, USDC, USDD, USDE, USDG, USDQ, USDR, USDS, USDT, ZUSD.
- DEX: NOT USED; no DEX freshness gate.
- OHLC screening abstentions: 11; details in immutable scan JSON artifact.
- Storage: checksum-sealed ledger pushed non-force and read back before this report. Independent artifact recovery is NOT VERIFIED by this scan alone.
- Errors: none in successful committed scan; a failed workflow must not publish a SUCCESS report.
