# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-11T09:31:48.712561+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/42995613149
**Source SHA:** 21b4cf643df9f7a7adfddc959660920dd467c70b
**Ledger commit:** fd0b68220281c401532bbc1ef3663e993d11562e
**Ledger generation:** 274 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 7s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 624; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 606; valid market observations: 603; OHLC screened: 24.

## Top WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | Confidence / risk | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---|---|---|
| 1 | NIGHT/USD | 0.04403 | 97.520 | 77.591 | +5.03% | +0.99% | 14.47x | 2.3 | 2026-11-11T09:31:42.043655+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 2 | AVAX/USD | 8.583 | 77.376 | 71.408 | +2.59% | -0.10% | 1.65x | 3.5 | 2026-11-11T09:31:42.043655+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 3 | LINK/USD | 10.35564 | 69.570 | 52.430 | +0.70% | +0.43% | 6.67x | 6.1 | 2026-11-11T09:31:42.043655+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 4 | XLM/USD | 0.146302 | 62.093 | 54.154 | +1.18% | -0.02% | 1.80x | 5.1 | 2026-11-11T09:31:42.043655+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 5 | ADA/USD | 0.174609 | 61.522 | 55.108 | +0.46% | +0.28% | 1.50x | 6.2 | 2026-11-11T09:31:42.043655+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 6 | ZRO/USD | 1.543 | 59.542 | 42.263 | +0.59% | +0.46% | 22.12x | 13.0 | 2026-11-11T09:31:42.043655+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 7 | PYTH/USD | 0.06824 | 59.530 | 48.713 | +4.25% | +0.40% | 1.88x | 26.5 | 2026-11-11T09:31:42.043655+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 8 | XMR/USD | 570.62 | 57.851 | 57.128 | +1.42% | +0.44% | 0.85x | 15.6 | 2026-11-11T09:31:42.043655+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 9 | TON/USD | 1.171 | 52.884 | 48.940 | +2.81% | +2.08% | 0.35x | 17.1 | 2026-11-11T09:31:42.043655+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 10 | STX/USD | 0.3159 | 33.252 | 24.381 | +0.32% | +0.00% | 1.89x | 19.0 | 2026-11-11T09:31:42.043655+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 11 | PENGU/USD | 0.006228 | 25.245 | 33.763 | +0.48% | +0.24% | 0.03x | 4.8 | 2026-11-11T09:31:42.043655+00:00 | NOT CALIBRATED / HIGH | WATCH |

**Confidence:** uncalibrated research heuristics, NOT validated probabilities. **BUY:** none authorized. Numerical baseline/challenger scores are uncalibrated paper-only ranking values, not probabilities or validated improvement.

## Learning and coverage

| Forward horizon | Evidence status | Verified matured / hits |
|---|---|---|
| 1h | PER HORIZON NOT INDEPENDENTLY VERIFIED | NOT VERIFIED |
| 6h | PER HORIZON NOT INDEPENDENTLY VERIFIED | NOT VERIFIED |
| 24h | PER HORIZON NOT INDEPENDENTLY VERIFIED | NOT VERIFIED |
| 48h | PER HORIZON NOT INDEPENDENTLY VERIFIED | NOT VERIFIED |

- Persisted scans: 274; predictions: 2556; observations: 164395.
- Matured sampled outcomes across 1/6/24/48h: 1849; gap abstentions: 6792. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 0 (sampled only; not a success-rate estimate).
- False positives / missed movers: NOT VERIFIED without eligible continuous outcome coverage.
- Baseline vs challenger: recorded as-of; unbiased held-out lift NOT MEASURED.
- Online Kraken /USD stablecoin-base pairs excluded: 18 (counted from this scan's online AssetPairs metadata, not inferred from price).
- Stablecoin base exclusions: BRL1, BUSD, DAI, EUR, EURC, EUROP, EURQ, EURR, EURT, FDUSD, FRAX, GUSD, PYUSD, QCAD, RLUSD, TGBP, TUSD, USD, USD1, USDC, USDD, USDE, USDG, USDQ, USDR, USDS, USDT, ZUSD.
- DEX: NOT USED; no DEX freshness gate.
- OHLC screening abstentions: 13; details in immutable scan JSON artifact.
- Storage: checksum-sealed ledger pushed non-force and read back before this report. Independent artifact recovery is NOT VERIFIED by this scan alone.
- Errors: none in successful committed scan; a failed workflow must not publish a SUCCESS report.
