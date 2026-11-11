# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-11T04:03:58.323545+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/42956524985
**Source SHA:** 21b4cf643df9f7a7adfddc959660920dd467c70b
**Ledger commit:** 1e30e70e112c4592da68b3f2620fe648aa0009b2
**Ledger generation:** 263 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 9s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 624; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 606; valid market observations: 602; OHLC screened: 24.

## Top WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | Confidence / risk | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---|---|---|
| 1 | INJ/USD | 8.415 | 69.609 | 75.650 | +5.12% | +0.42% | 0.19x | 6.0 | 2026-11-11T04:03:49.410162+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 2 | NEAR/USD | 3.6856 | 68.380 | 72.713 | +2.84% | -0.56% | 0.85x | 4.3 | 2026-11-11T04:03:49.410162+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 3 | XLM/USD | 0.145355 | 66.853 | 52.173 | +0.53% | -0.06% | 8.43x | 0.1 | 2026-11-11T04:03:49.410162+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 4 | LINK/USD | 10.37604 | 66.619 | 53.491 | +0.89% | -0.09% | 2.36x | 3.2 | 2026-11-11T04:03:49.410162+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 5 | AVAX/USD | 8.43 | 64.492 | 58.575 | +0.77% | -0.15% | 1.67x | 3.6 | 2026-11-11T04:03:49.410162+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 6 | TAO/USD | 220.407 | 60.006 | 60.066 | +1.02% | -0.02% | 1.01x | 4.2 | 2026-11-11T04:03:49.410162+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 7 | HBAR/USD | 0.06595 | 58.513 | 43.892 | +0.64% | -0.08% | 4.13x | 1.5 | 2026-11-11T04:03:49.410162+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 8 | AAVE/USD | 125.11 | 56.464 | 57.568 | +1.40% | -0.04% | 0.91x | 6.4 | 2026-11-11T04:03:49.410162+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 9 | BNB/USD | 682.95 | 55.697 | 40.316 | +0.50% | +0.08% | 14.65x | 2.1 | 2026-11-11T04:03:49.410162+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 10 | PYTH/USD | 0.06869 | 55.096 | 59.512 | +4.93% | +0.50% | 0.31x | 14.6 | 2026-11-11T04:03:49.410162+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 11 | VVV/USD | 19.36 | 54.378 | 40.619 | +0.30% | -0.25% | 2.74x | 6.2 | 2026-11-11T04:03:49.410162+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 12 | ETH/USD | 2063.28 | 53.097 | 59.287 | +0.62% | +0.02% | 0.37x | 0.0 | 2026-11-11T04:03:49.410162+00:00 | NOT CALIBRATED / HIGH | WATCH |

**Confidence:** uncalibrated research heuristics, NOT validated probabilities. **BUY:** none authorized. Numerical baseline/challenger scores are uncalibrated paper-only ranking values, not probabilities or validated improvement.

## Learning and coverage

| Forward horizon | Evidence status | Verified matured / hits |
|---|---|---|
| 1h | PER HORIZON NOT INDEPENDENTLY VERIFIED | NOT VERIFIED |
| 6h | PER HORIZON NOT INDEPENDENTLY VERIFIED | NOT VERIFIED |
| 24h | PER HORIZON NOT INDEPENDENTLY VERIFIED | NOT VERIFIED |
| 48h | PER HORIZON NOT INDEPENDENTLY VERIFIED | NOT VERIFIED |

- Persisted scans: 263; predictions: 2433; observations: 157769.
- Matured sampled outcomes across 1/6/24/48h: 1658; gap abstentions: 6611. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 0 (sampled only; not a success-rate estimate).
- False positives / missed movers: NOT VERIFIED without eligible continuous outcome coverage.
- Baseline vs challenger: recorded as-of; unbiased held-out lift NOT MEASURED.
- Online Kraken /USD stablecoin-base pairs excluded: 18 (counted from this scan's online AssetPairs metadata, not inferred from price).
- Stablecoin base exclusions: BRL1, BUSD, DAI, EUR, EURC, EUROP, EURQ, EURR, EURT, FDUSD, FRAX, GUSD, PYUSD, QCAD, RLUSD, TGBP, TUSD, USD, USD1, USDC, USDD, USDE, USDG, USDQ, USDR, USDS, USDT, ZUSD.
- DEX: NOT USED; no DEX freshness gate.
- OHLC screening abstentions: 7; details in immutable scan JSON artifact.
- Storage: checksum-sealed ledger pushed non-force and read back before this report. Independent artifact recovery is NOT VERIFIED by this scan alone.
- Errors: none in successful committed scan; a failed workflow must not publish a SUCCESS report.
