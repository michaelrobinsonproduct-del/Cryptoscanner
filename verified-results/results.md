# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-11T11:33:58.814224+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/43012719107
**Source SHA:** 21b4cf643df9f7a7adfddc959660920dd467c70b
**Ledger commit:** 15e3ea07ffb80fe757d449ac5d790c878c35834b
**Ledger generation:** 278 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 6s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 624; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 606; valid market observations: 603; OHLC screened: 24.

## Top WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | Confidence / risk | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---|---|---|
| 1 | XMR/USD | 577.97 | 88.303 | 72.861 | +2.72% | +0.09% | 2.91x | 2.4 | 2026-11-11T11:33:52.436362+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 2 | NEAR/USD | 3.6541 | 80.349 | 65.444 | +1.96% | -0.02% | 3.41x | 6.6 | 2026-11-11T11:33:52.436362+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 3 | SHX/USD | 0.004341 | 70.299 | 65.069 | +5.24% | -0.23% | 1.64x | 4.6 | 2026-11-11T11:33:52.436362+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 4 | NIGHT/USD | 0.04403 | 65.259 | 76.260 | +5.03% | -0.59% | 0.19x | 6.8 | 2026-11-11T11:33:52.436362+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 5 | AVAX/USD | 8.595 | 63.942 | 71.833 | +2.74% | -0.88% | 0.65x | 4.7 | 2026-11-11T11:33:52.436362+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 6 | TON/USD | 1.192 | 60.890 | 69.427 | +4.65% | -0.34% | 0.31x | 8.4 | 2026-11-11T11:33:52.436362+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 7 | ETH/USD | 2056.16 | 57.290 | 56.856 | +0.27% | -0.17% | 1.13x | 0.0 | 2026-11-11T11:33:52.436362+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 8 | PUMP/USD | 0.003589 | 56.828 | 64.591 | +2.19% | -0.06% | 0.25x | 5.6 | 2026-11-11T11:33:52.436362+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 9 | HYPE/USD | 72.41 | 54.540 | 56.151 | +0.26% | -0.29% | 0.98x | 1.4 | 2026-11-11T11:33:52.436362+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 10 | LINK/USD | 10.37575 | 54.464 | 54.091 | +0.89% | -0.04% | 1.06x | 4.8 | 2026-11-11T11:33:52.436362+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 11 | SUI/USD | 0.8297 | 53.797 | 59.665 | +0.84% | -0.13% | 0.48x | 2.4 | 2026-11-11T11:33:52.436362+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 12 | XLM/USD | 0.147555 | 53.648 | 63.341 | +2.05% | -0.16% | 0.11x | 0.8 | 2026-11-11T11:33:52.436362+00:00 | NOT CALIBRATED / HIGH | WATCH |

**Confidence:** uncalibrated research heuristics, NOT validated probabilities. **BUY:** none authorized. Numerical baseline/challenger scores are uncalibrated paper-only ranking values, not probabilities or validated improvement.

## Learning and coverage

| Forward horizon | Evidence status | Verified matured / hits |
|---|---|---|
| 1h | PER HORIZON NOT INDEPENDENTLY VERIFIED | NOT VERIFIED |
| 6h | PER HORIZON NOT INDEPENDENTLY VERIFIED | NOT VERIFIED |
| 24h | PER HORIZON NOT INDEPENDENTLY VERIFIED | NOT VERIFIED |
| 48h | PER HORIZON NOT INDEPENDENTLY VERIFIED | NOT VERIFIED |

- Persisted scans: 278; predictions: 2604; observations: 166807.
- Matured sampled outcomes across 1/6/24/48h: 1884; gap abstentions: 6905. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 0 (sampled only; not a success-rate estimate).
- False positives / missed movers: NOT VERIFIED without eligible continuous outcome coverage.
- Baseline vs challenger: recorded as-of; unbiased held-out lift NOT MEASURED.
- Online Kraken /USD stablecoin-base pairs excluded: 18 (counted from this scan's online AssetPairs metadata, not inferred from price).
- Stablecoin base exclusions: BRL1, BUSD, DAI, EUR, EURC, EUROP, EURQ, EURR, EURT, FDUSD, FRAX, GUSD, PYUSD, QCAD, RLUSD, TGBP, TUSD, USD, USD1, USDC, USDD, USDE, USDG, USDQ, USDR, USDS, USDT, ZUSD.
- DEX: NOT USED; no DEX freshness gate.
- OHLC screening abstentions: 5; details in immutable scan JSON artifact.
- Storage: checksum-sealed ledger pushed non-force and read back before this report. Independent artifact recovery is NOT VERIFIED by this scan alone.
- Errors: none in successful committed scan; a failed workflow must not publish a SUCCESS report.
