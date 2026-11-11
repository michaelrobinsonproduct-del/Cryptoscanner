# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-11T08:37:17.033032+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/42988194644
**Source SHA:** 21b4cf643df9f7a7adfddc959660920dd467c70b
**Ledger commit:** fbd06cfe76d277f1fef261cc82e027f47664a08d
**Ledger generation:** 272 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 6s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 624; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 606; valid market observations: 603; OHLC screened: 24.

## Top WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | Confidence / risk | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---|---|---|
| 1 | NIGHT/USD | 0.04353 | 77.808 | 67.018 | +3.84% | -0.84% | 2.64x | 6.9 | 2026-11-11T08:37:10.549693+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 2 | ADA/USD | 0.174725 | 71.242 | 56.493 | +0.53% | -0.05% | 3.71x | 4.4 | 2026-11-11T08:37:10.549693+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 3 | AVAX/USD | 8.58 | 64.428 | 70.577 | +2.56% | -0.21% | 0.49x | 4.7 | 2026-11-11T08:37:10.549693+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 4 | TAO/USD | 219.2582 | 60.127 | 56.023 | +0.50% | -0.25% | 1.53x | 4.9 | 2026-11-11T08:37:10.549693+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 5 | NEAR/USD | 3.6057 | 59.603 | 57.613 | +0.61% | -0.78% | 1.59x | 3.3 | 2026-11-11T08:37:10.549693+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 6 | SUI/USD | 0.8252 | 56.326 | 56.436 | +0.29% | -0.06% | 1.02x | 1.2 | 2026-11-11T08:37:10.549693+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 7 | XLM/USD | 0.145769 | 48.465 | 52.398 | +0.82% | -0.12% | 0.67x | 3.3 | 2026-11-11T08:37:10.549693+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 8 | ONDO/USD | 0.3704 | 43.048 | 44.955 | +1.01% | -0.52% | 1.07x | 3.2 | 2026-11-11T08:37:10.549693+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 9 | TIA/USD | 0.4291 | 42.477 | 31.521 | +0.56% | -0.81% | 4.40x | 7.0 | 2026-11-11T08:37:10.549693+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 10 | INJ/USD | 8.143 | 41.115 | 50.030 | +1.72% | -0.77% | 0.49x | 7.4 | 2026-11-11T08:37:10.549693+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 11 | LINK/USD | 10.32165 | 39.362 | 51.120 | +0.37% | -0.46% | 0.05x | 3.9 | 2026-11-11T08:37:10.549693+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 12 | TON/USD | 1.142 | 19.100 | 30.165 | +0.26% | -0.78% | 0.28x | 17.5 | 2026-11-11T08:37:10.549693+00:00 | NOT CALIBRATED / HIGH | WATCH |

**Confidence:** uncalibrated research heuristics, NOT validated probabilities. **BUY:** none authorized. Numerical baseline/challenger scores are uncalibrated paper-only ranking values, not probabilities or validated improvement.

## Learning and coverage

| Forward horizon | Evidence status | Verified matured / hits |
|---|---|---|
| 1h | PER HORIZON NOT INDEPENDENTLY VERIFIED | NOT VERIFIED |
| 6h | PER HORIZON NOT INDEPENDENTLY VERIFIED | NOT VERIFIED |
| 24h | PER HORIZON NOT INDEPENDENTLY VERIFIED | NOT VERIFIED |
| 48h | PER HORIZON NOT INDEPENDENTLY VERIFIED | NOT VERIFIED |

- Persisted scans: 272; predictions: 2533; observations: 163189.
- Matured sampled outcomes across 1/6/24/48h: 1849; gap abstentions: 6733. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 0 (sampled only; not a success-rate estimate).
- False positives / missed movers: NOT VERIFIED without eligible continuous outcome coverage.
- Baseline vs challenger: recorded as-of; unbiased held-out lift NOT MEASURED.
- Online Kraken /USD stablecoin-base pairs excluded: 18 (counted from this scan's online AssetPairs metadata, not inferred from price).
- Stablecoin base exclusions: BRL1, BUSD, DAI, EUR, EURC, EUROP, EURQ, EURR, EURT, FDUSD, FRAX, GUSD, PYUSD, QCAD, RLUSD, TGBP, TUSD, USD, USD1, USDC, USDD, USDE, USDG, USDQ, USDR, USDS, USDT, ZUSD.
- DEX: NOT USED; no DEX freshness gate.
- OHLC screening abstentions: 12; details in immutable scan JSON artifact.
- Storage: checksum-sealed ledger pushed non-force and read back before this report. Independent artifact recovery is NOT VERIFIED by this scan alone.
- Errors: none in successful committed scan; a failed workflow must not publish a SUCCESS report.
