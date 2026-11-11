# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-11T03:37:47.256722+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/42953837376
**Source SHA:** 51fbc41d801fe95ef29f602a2c814853ca9858b8
**Ledger commit:** fd879f621733630adc0acc216056801ddc4a63d0
**Ledger generation:** 262 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 9s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 624; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 606; valid market observations: 602; OHLC screened: 24.

## Top WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | Confidence / risk | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---|---|---|
| 1 | INJ/USD | 8.373 | 81.519 | 72.029 | +4.60% | +0.38% | 1.76x | 6.0 | 2026-11-11T03:37:38.559218+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 2 | XDG/USD | 0.0683271 | 72.255 | 58.677 | +0.57% | -0.28% | 3.85x | 0.6 | 2026-11-11T03:37:38.559218+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 3 | NEAR/USD | 3.697 | 68.198 | 74.675 | +3.16% | -0.58% | 0.64x | 4.9 | 2026-11-11T03:37:38.559218+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 4 | XRP/USD | 1.05959 | 65.903 | 57.925 | +0.42% | -0.25% | 1.92x | 0.1 | 2026-11-11T03:37:38.559218+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 5 | ZRO/USD | 1.594 | 65.192 | 62.081 | +3.91% | +0.13% | 1.25x | 12.6 | 2026-11-11T03:37:38.559218+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 6 | ONDO/USD | 0.3714 | 65.004 | 50.246 | +1.28% | -0.05% | 2.55x | 1.6 | 2026-11-11T03:37:38.559218+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 7 | ETH/USD | 2060.15 | 64.904 | 58.219 | +0.46% | -0.14% | 1.74x | 0.0 | 2026-11-11T03:37:38.559218+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 8 | AAVE/USD | 124.99 | 57.402 | 58.065 | +1.30% | -0.33% | 1.10x | 4.0 | 2026-11-11T03:37:38.559218+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 9 | SUI/USD | 0.8316 | 56.886 | 61.885 | +1.07% | -0.04% | 0.52x | 1.2 | 2026-11-11T03:37:38.559218+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 10 | TAO/USD | 220.313 | 54.279 | 60.425 | +0.98% | -0.15% | 0.46x | 2.9 | 2026-11-11T03:37:38.559218+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 11 | PENGU/USD | 0.006267 | 53.394 | 38.951 | +1.11% | -0.11% | 3.36x | 3.2 | 2026-11-11T03:37:38.559218+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 12 | AVAX/USD | 8.461 | 52.739 | 60.583 | +1.14% | -0.26% | 0.35x | 4.7 | 2026-11-11T03:37:38.559218+00:00 | NOT CALIBRATED / HIGH | WATCH |

**Confidence:** uncalibrated research heuristics, NOT validated probabilities. **BUY:** none authorized. Numerical baseline/challenger scores are uncalibrated paper-only ranking values, not probabilities or validated improvement.

## Learning and coverage

| Forward horizon | Evidence status | Verified matured / hits |
|---|---|---|
| 1h | PER HORIZON NOT INDEPENDENTLY VERIFIED | NOT VERIFIED |
| 6h | PER HORIZON NOT INDEPENDENTLY VERIFIED | NOT VERIFIED |
| 24h | PER HORIZON NOT INDEPENDENTLY VERIFIED | NOT VERIFIED |
| 48h | PER HORIZON NOT INDEPENDENTLY VERIFIED | NOT VERIFIED |

- Persisted scans: 262; predictions: 2421; observations: 157167.
- Matured sampled outcomes across 1/6/24/48h: 1638; gap abstentions: 6595. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 0 (sampled only; not a success-rate estimate).
- False positives / missed movers: NOT VERIFIED without eligible continuous outcome coverage.
- Baseline vs challenger: recorded as-of; unbiased held-out lift NOT MEASURED.
- Online Kraken /USD stablecoin-base pairs excluded: 18 (counted from this scan's online AssetPairs metadata, not inferred from price).
- Stablecoin base exclusions: BRL1, BUSD, DAI, EUR, EURC, EUROP, EURQ, EURR, EURT, FDUSD, FRAX, GUSD, PYUSD, QCAD, RLUSD, TGBP, TUSD, USD, USD1, USDC, USDD, USDE, USDG, USDQ, USDR, USDS, USDT, ZUSD.
- DEX: NOT USED; no DEX freshness gate.
- OHLC screening abstentions: 9; details in immutable scan JSON artifact.
- Storage: checksum-sealed ledger pushed non-force and read back before this report. Independent artifact recovery is NOT VERIFIED by this scan alone.
- Errors: none in successful committed scan; a failed workflow must not publish a SUCCESS report.
