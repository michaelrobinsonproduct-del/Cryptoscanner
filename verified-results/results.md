# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-11T06:03:57.891115+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/42969592975
**Source SHA:** 21b4cf643df9f7a7adfddc959660920dd467c70b
**Ledger commit:** 0715310635a220fecdef39954a3c1fcfe16dcdc8
**Ledger generation:** 267 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 9s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 624; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 606; valid market observations: 602; OHLC screened: 24.

## Top WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | Confidence / risk | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---|---|---|
| 1 | AVAX/USD | 8.492 | 79.792 | 63.188 | +1.51% | +0.60% | 2.36x | 4.7 | 2026-11-11T06:03:48.394797+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 2 | ETH/USD | 2066.66 | 68.995 | 59.957 | +0.78% | +0.07% | 1.87x | 1.0 | 2026-11-11T06:03:48.394797+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 3 | NIGHT/USD | 0.04305 | 68.928 | 59.801 | +2.70% | +0.51% | 1.66x | 4.7 | 2026-11-11T06:03:48.394797+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 4 | XMR/USD | 570.21 | 68.822 | 62.048 | +1.35% | -0.08% | 1.72x | 4.7 | 2026-11-11T06:03:48.394797+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 5 | NEAR/USD | 3.6461 | 67.802 | 65.660 | +1.74% | +0.17% | 1.13x | 3.0 | 2026-11-11T06:03:48.394797+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 6 | ADA/USD | 0.175373 | 64.103 | 59.539 | +0.90% | +0.17% | 1.37x | 3.5 | 2026-11-11T06:03:48.394797+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 7 | DASH/USD | 45.006 | 61.305 | 64.224 | +4.76% | -0.02% | 0.72x | 14.1 | 2026-11-11T06:03:48.394797+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 8 | ONDO/USD | 0.36946 | 61.280 | 43.052 | +0.75% | +0.65% | 7.75x | 3.2 | 2026-11-11T06:03:48.394797+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 9 | INJ/USD | 8.248 | 59.187 | 60.629 | +3.04% | -0.07% | 0.89x | 6.1 | 2026-11-11T06:03:48.394797+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 10 | SUI/USD | 0.8281 | 57.820 | 58.905 | +0.64% | +0.25% | 0.76x | 1.2 | 2026-11-11T06:03:48.394797+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 11 | XRP/USD | 1.06156 | 52.301 | 58.902 | +0.61% | +0.17% | 0.25x | 0.8 | 2026-11-11T06:03:48.394797+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 12 | XDG/USD | 0.0682607 | 49.956 | 57.282 | +0.47% | +0.10% | 0.22x | 2.1 | 2026-11-11T06:03:48.394797+00:00 | NOT CALIBRATED / HIGH | WATCH |

**Confidence:** uncalibrated research heuristics, NOT validated probabilities. **BUY:** none authorized. Numerical baseline/challenger scores are uncalibrated paper-only ranking values, not probabilities or validated improvement.

## Learning and coverage

| Forward horizon | Evidence status | Verified matured / hits |
|---|---|---|
| 1h | PER HORIZON NOT INDEPENDENTLY VERIFIED | NOT VERIFIED |
| 6h | PER HORIZON NOT INDEPENDENTLY VERIFIED | NOT VERIFIED |
| 24h | PER HORIZON NOT INDEPENDENTLY VERIFIED | NOT VERIFIED |
| 48h | PER HORIZON NOT INDEPENDENTLY VERIFIED | NOT VERIFIED |

- Persisted scans: 267; predictions: 2481; observations: 160177.
- Matured sampled outcomes across 1/6/24/48h: 1748; gap abstentions: 6666. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 0 (sampled only; not a success-rate estimate).
- False positives / missed movers: NOT VERIFIED without eligible continuous outcome coverage.
- Baseline vs challenger: recorded as-of; unbiased held-out lift NOT MEASURED.
- Online Kraken /USD stablecoin-base pairs excluded: 18 (counted from this scan's online AssetPairs metadata, not inferred from price).
- Stablecoin base exclusions: BRL1, BUSD, DAI, EUR, EURC, EUROP, EURQ, EURR, EURT, FDUSD, FRAX, GUSD, PYUSD, QCAD, RLUSD, TGBP, TUSD, USD, USD1, USDC, USDD, USDE, USDG, USDQ, USDR, USDS, USDT, ZUSD.
- DEX: NOT USED; no DEX freshness gate.
- OHLC screening abstentions: 11; details in immutable scan JSON artifact.
- Storage: checksum-sealed ledger pushed non-force and read back before this report. Independent artifact recovery is NOT VERIFIED by this scan alone.
- Errors: none in successful committed scan; a failed workflow must not publish a SUCCESS report.
