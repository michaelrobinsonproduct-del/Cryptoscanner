# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-11T12:04:22.446938+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/43016835456
**Source SHA:** 21b4cf643df9f7a7adfddc959660920dd467c70b
**Ledger commit:** 39c8c6b73c1d9d4734e5d4460d62d837a568217f
**Ledger generation:** 279 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 7s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 624; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 606; valid market observations: 603; OHLC screened: 24.

## Top WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | Confidence / risk | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---|---|---|
| 1 | NEAR/USD | 3.7845 | 121.260 | 88.779 | +5.60% | +3.50% | 9.89x | 10.8 | 2026-11-11T12:04:14.978678+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 2 | ADA/USD | 0.176588 | 79.789 | 63.793 | +1.60% | +0.20% | 2.60x | 4.8 | 2026-11-11T12:04:14.978678+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 3 | CC/USD | 0.09349 | 76.757 | 65.846 | +4.48% | +0.79% | 1.69x | 9.6 | 2026-11-11T12:04:14.978678+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 4 | SUI/USD | 0.8329 | 71.783 | 62.392 | +1.23% | +0.40% | 1.74x | 2.4 | 2026-11-11T12:04:14.978678+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 5 | AVAX/USD | 8.566 | 68.995 | 68.815 | +2.39% | -0.21% | 1.12x | 5.8 | 2026-11-11T12:04:14.978678+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 6 | XLM/USD | 0.147935 | 68.333 | 63.733 | +2.31% | +0.18% | 1.37x | 3.9 | 2026-11-11T12:04:14.978678+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 7 | LINK/USD | 10.37352 | 66.475 | 53.738 | +0.87% | +0.22% | 2.16x | 5.3 | 2026-11-11T12:04:14.978678+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 8 | NIGHT/USD | 0.0444 | 65.667 | 68.166 | +5.92% | -0.09% | 0.80x | 36.1 | 2026-11-11T12:04:14.978678+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 9 | TIA/USD | 0.4362 | 63.791 | 45.674 | +2.23% | +0.62% | 38.16x | 2.3 | 2026-11-11T12:04:14.978678+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 10 | XMR/USD | 579.53 | 60.600 | 69.278 | +3.00% | +0.04% | 0.11x | 13.5 | 2026-11-11T12:04:14.978678+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 11 | TON/USD | 1.183 | 60.178 | 59.929 | +3.86% | -0.08% | 1.07x | 16.9 | 2026-11-11T12:04:14.978678+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 12 | HBAR/USD | 0.06604 | 59.827 | 43.234 | +0.78% | +0.32% | 3.56x | 4.5 | 2026-11-11T12:04:14.978678+00:00 | NOT CALIBRATED / HIGH | WATCH |

**Confidence:** uncalibrated research heuristics, NOT validated probabilities. **BUY:** none authorized. Numerical baseline/challenger scores are uncalibrated paper-only ranking values, not probabilities or validated improvement.

## Learning and coverage

| Forward horizon | Evidence status | Verified matured / hits |
|---|---|---|
| 1h | PER HORIZON NOT INDEPENDENTLY VERIFIED | NOT VERIFIED |
| 6h | PER HORIZON NOT INDEPENDENTLY VERIFIED | NOT VERIFIED |
| 24h | PER HORIZON NOT INDEPENDENTLY VERIFIED | NOT VERIFIED |
| 48h | PER HORIZON NOT INDEPENDENTLY VERIFIED | NOT VERIFIED |

- Persisted scans: 279; predictions: 2616; observations: 167410.
- Matured sampled outcomes across 1/6/24/48h: 1896; gap abstentions: 6937. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 0 (sampled only; not a success-rate estimate).
- False positives / missed movers: NOT VERIFIED without eligible continuous outcome coverage.
- Baseline vs challenger: recorded as-of; unbiased held-out lift NOT MEASURED.
- Online Kraken /USD stablecoin-base pairs excluded: 18 (counted from this scan's online AssetPairs metadata, not inferred from price).
- Stablecoin base exclusions: BRL1, BUSD, DAI, EUR, EURC, EUROP, EURQ, EURR, EURT, FDUSD, FRAX, GUSD, PYUSD, QCAD, RLUSD, TGBP, TUSD, USD, USD1, USDC, USDD, USDE, USDG, USDQ, USDR, USDS, USDT, ZUSD.
- DEX: NOT USED; no DEX freshness gate.
- OHLC screening abstentions: 7; details in immutable scan JSON artifact.
- Storage: checksum-sealed ledger pushed non-force and read back before this report. Independent artifact recovery is NOT VERIFIED by this scan alone.
- Errors: none in successful committed scan; a failed workflow must not publish a SUCCESS report.
