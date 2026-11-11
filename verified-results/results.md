# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-11T21:06:09.671359+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/43099803536
**Source SHA:** 21b4cf643df9f7a7adfddc959660920dd467c70b
**Ledger commit:** b5332aa1a75e3e7b450b909413a753a124911922
**Ledger generation:** 297 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 7s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 624; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 606; valid market observations: 606; OHLC screened: 24.

## Top WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | Confidence / risk | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---|---|---|
| 1 | SOL/USD | 84.86 | 82.328 | 68.034 | +1.95% | -0.14% | 2.57x | 1.2 | 2026-11-11T21:06:02.795454+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 2 | XLM/USD | 0.14968 | 77.738 | 71.490 | +3.52% | +0.18% | 1.53x | 1.9 | 2026-11-11T21:06:02.795454+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 3 | TON/USD | 1.181 | 75.377 | 63.311 | +3.69% | -0.59% | 4.00x | 16.9 | 2026-11-11T21:06:02.795454+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 4 | SUI/USD | 0.8383 | 74.967 | 67.590 | +1.88% | +0.05% | 1.71x | 1.2 | 2026-11-11T21:06:02.795454+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 5 | NEAR/USD | 3.7076 | 74.578 | 77.425 | +3.45% | -0.17% | 0.80x | 3.5 | 2026-11-11T21:06:02.795454+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 6 | AVAX/USD | 8.614 | 68.400 | 74.590 | +2.96% | -0.01% | 0.39x | 2.3 | 2026-11-11T21:06:02.795454+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 7 | XBT/USD | 74559.3 | 67.533 | 63.161 | +1.17% | -0.08% | 1.48x | 0.0 | 2026-11-11T21:06:02.795454+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 8 | XMR/USD | 584.03 | 67.208 | 77.160 | +3.80% | -0.48% | 0.25x | 8.9 | 2026-11-11T21:06:02.795454+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 9 | ETH/USD | 2076.08 | 63.418 | 63.657 | +1.24% | -0.16% | 1.05x | 0.0 | 2026-11-11T21:06:02.795454+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 10 | ADA/USD | 0.177515 | 61.840 | 67.651 | +2.13% | +0.04% | 0.40x | 4.6 | 2026-11-11T21:06:02.795454+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 11 | XRP/USD | 1.06479 | 59.056 | 61.140 | +0.92% | +0.11% | 0.73x | 0.6 | 2026-11-11T21:06:02.795454+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 12 | BNB/USD | 685.86 | 57.651 | 43.575 | +0.93% | -0.18% | 4.41x | 0.1 | 2026-11-11T21:06:02.795454+00:00 | NOT CALIBRATED / HIGH | WATCH |

**Confidence:** uncalibrated research heuristics, NOT validated probabilities. **BUY:** none authorized. Numerical baseline/challenger scores are uncalibrated paper-only ranking values, not probabilities or validated improvement.

## Learning and coverage

| Forward horizon | Evidence status | Verified matured / hits |
|---|---|---|
| 1h | PER HORIZON NOT INDEPENDENTLY VERIFIED | NOT VERIFIED |
| 6h | PER HORIZON NOT INDEPENDENTLY VERIFIED | NOT VERIFIED |
| 24h | PER HORIZON NOT INDEPENDENTLY VERIFIED | NOT VERIFIED |
| 48h | PER HORIZON NOT INDEPENDENTLY VERIFIED | NOT VERIFIED |

- Persisted scans: 297; predictions: 2832; observations: 178299.
- Matured sampled outcomes across 1/6/24/48h: 2243; gap abstentions: 7373. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 0 (sampled only; not a success-rate estimate).
- False positives / missed movers: NOT VERIFIED without eligible continuous outcome coverage.
- Baseline vs challenger: recorded as-of; unbiased held-out lift NOT MEASURED.
- Online Kraken /USD stablecoin-base pairs excluded: 18 (counted from this scan's online AssetPairs metadata, not inferred from price).
- Stablecoin base exclusions: BRL1, BUSD, DAI, EUR, EURC, EUROP, EURQ, EURR, EURT, FDUSD, FRAX, GUSD, PYUSD, QCAD, RLUSD, TGBP, TUSD, USD, USD1, USDC, USDD, USDE, USDG, USDQ, USDR, USDS, USDT, ZUSD.
- DEX: NOT USED; no DEX freshness gate.
- OHLC screening abstentions: 8; details in immutable scan JSON artifact.
- Storage: checksum-sealed ledger pushed non-force and read back before this report. Independent artifact recovery is NOT VERIFIED by this scan alone.
- Errors: none in successful committed scan; a failed workflow must not publish a SUCCESS report.
