# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-11T10:03:33.507214+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/43000146698
**Source SHA:** 21b4cf643df9f7a7adfddc959660920dd467c70b
**Ledger commit:** b4d50a4f366c770162f73a1267a5dfca3d21bde3
**Ledger generation:** 275 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 8s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 624; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 606; valid market observations: 603; OHLC screened: 24.

## Top WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | Confidence / risk | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---|---|---|
| 1 | TON/USD | 1.192 | 79.283 | 62.395 | +4.65% | +1.45% | 1.96x | 16.8 | 2026-11-11T10:03:25.037156+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 2 | SUI/USD | 0.8274 | 75.743 | 57.705 | +0.56% | +0.61% | 2.71x | 2.4 | 2026-11-11T10:03:25.037156+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 3 | NIGHT/USD | 0.0441 | 74.407 | 77.639 | +5.20% | +0.52% | 0.41x | 4.5 | 2026-11-11T10:03:25.037156+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 4 | TAO/USD | 218.8012 | 70.287 | 53.890 | +0.29% | +0.28% | 4.29x | 6.3 | 2026-11-11T10:03:25.037156+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 5 | AVAX/USD | 8.607 | 66.608 | 72.841 | +2.88% | +0.29% | 0.23x | 4.6 | 2026-11-11T10:03:25.037156+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 6 | XMR/USD | 572.83 | 64.733 | 63.489 | +1.81% | +0.18% | 1.04x | 8.4 | 2026-11-11T10:03:25.037156+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 7 | ADA/USD | 0.17598 | 59.657 | 60.878 | +1.25% | +0.60% | 0.58x | 5.7 | 2026-11-11T10:03:25.037156+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 8 | DOT/USD | 0.8475 | 58.896 | 40.564 | +0.59% | +0.67% | 5.55x | 2.4 | 2026-11-11T10:03:25.037156+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 9 | AAVE/USD | 124.04 | 56.432 | 49.902 | +0.53% | +0.55% | 1.38x | 3.2 | 2026-11-11T10:03:25.037156+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 10 | NEAR/USD | 3.6057 | 54.198 | 55.396 | +0.61% | +0.95% | 0.41x | 7.8 | 2026-11-11T10:03:25.037156+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 11 | LINK/USD | 10.35678 | 53.453 | 52.795 | +0.71% | +0.32% | 0.90x | 5.8 | 2026-11-11T10:03:25.037156+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 12 | ZRO/USD | 1.571 | 52.724 | 52.551 | +2.41% | +1.75% | 0.14x | 19.1 | 2026-11-11T10:03:25.037156+00:00 | NOT CALIBRATED / HIGH | WATCH |

**Confidence:** uncalibrated research heuristics, NOT validated probabilities. **BUY:** none authorized. Numerical baseline/challenger scores are uncalibrated paper-only ranking values, not probabilities or validated improvement.

## Learning and coverage

| Forward horizon | Evidence status | Verified matured / hits |
|---|---|---|
| 1h | PER HORIZON NOT INDEPENDENTLY VERIFIED | NOT VERIFIED |
| 6h | PER HORIZON NOT INDEPENDENTLY VERIFIED | NOT VERIFIED |
| 24h | PER HORIZON NOT INDEPENDENTLY VERIFIED | NOT VERIFIED |
| 48h | PER HORIZON NOT INDEPENDENTLY VERIFIED | NOT VERIFIED |

- Persisted scans: 275; predictions: 2568; observations: 164998.
- Matured sampled outcomes across 1/6/24/48h: 1849; gap abstentions: 6823. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 0 (sampled only; not a success-rate estimate).
- False positives / missed movers: NOT VERIFIED without eligible continuous outcome coverage.
- Baseline vs challenger: recorded as-of; unbiased held-out lift NOT MEASURED.
- Online Kraken /USD stablecoin-base pairs excluded: 18 (counted from this scan's online AssetPairs metadata, not inferred from price).
- Stablecoin base exclusions: BRL1, BUSD, DAI, EUR, EURC, EUROP, EURQ, EURR, EURT, FDUSD, FRAX, GUSD, PYUSD, QCAD, RLUSD, TGBP, TUSD, USD, USD1, USDC, USDD, USDE, USDG, USDQ, USDR, USDS, USDT, ZUSD.
- DEX: NOT USED; no DEX freshness gate.
- OHLC screening abstentions: 8; details in immutable scan JSON artifact.
- Storage: checksum-sealed ledger pushed non-force and read back before this report. Independent artifact recovery is NOT VERIFIED by this scan alone.
- Errors: none in successful committed scan; a failed workflow must not publish a SUCCESS report.
