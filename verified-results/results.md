# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-11T16:39:44.196889+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/43060132791
**Source SHA:** 21b4cf643df9f7a7adfddc959660920dd467c70b
**Ledger commit:** 465f19757bed6e74c2c140f0548e661bd055f7d9
**Ledger generation:** 289 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 7s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 624; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 606; valid market observations: 605; OHLC screened: 24.

## Top WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | Confidence / risk | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---|---|---|
| 1 | VVV/USD | 20.425 | 101.044 | 77.389 | +5.81% | +1.73% | 2.83x | 7.8 | 2026-11-11T16:39:36.954851+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 2 | NEAR/USD | 3.7757 | 99.586 | 90.097 | +5.35% | +0.26% | 1.82x | 4.8 | 2026-11-11T16:39:36.954851+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 3 | HYPE/USD | 73.83 | 78.972 | 69.928 | +2.23% | +0.39% | 1.71x | 1.4 | 2026-11-11T16:39:36.954851+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 4 | XMR/USD | 590.98 | 77.267 | 80.937 | +5.04% | +0.39% | 0.44x | 18.6 | 2026-11-11T16:39:36.954851+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 5 | ADA/USD | 0.178409 | 76.197 | 70.138 | +2.65% | +0.23% | 1.49x | 5.3 | 2026-11-11T16:39:36.954851+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 6 | XLM/USD | 0.150665 | 72.966 | 77.915 | +4.20% | -0.15% | 0.58x | 2.5 | 2026-11-11T16:39:36.954851+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 7 | TON/USD | 1.195 | 72.397 | 72.015 | +4.92% | +0.42% | 0.83x | 16.7 | 2026-11-11T16:39:36.954851+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 8 | SOL/USD | 84.71 | 70.727 | 66.772 | +1.77% | +0.17% | 1.31x | 1.2 | 2026-11-11T16:39:36.954851+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 9 | SUI/USD | 0.8438 | 69.649 | 71.680 | +2.55% | +0.18% | 0.71x | 2.4 | 2026-11-11T16:39:36.954851+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 10 | AVAX/USD | 8.6 | 66.017 | 72.253 | +2.80% | +0.22% | 0.27x | 4.7 | 2026-11-11T16:39:36.954851+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 11 | XDG/USD | 0.0688058 | 65.949 | 59.264 | +1.27% | +0.01% | 1.66x | 2.3 | 2026-11-11T16:39:36.954851+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 12 | XRP/USD | 1.07066 | 64.954 | 65.270 | +1.47% | +0.24% | 0.85x | 0.1 | 2026-11-11T16:39:36.954851+00:00 | NOT CALIBRATED / HIGH | WATCH |

**Confidence:** uncalibrated research heuristics, NOT validated probabilities. **BUY:** none authorized. Numerical baseline/challenger scores are uncalibrated paper-only ranking values, not probabilities or validated improvement.

## Learning and coverage

| Forward horizon | Evidence status | Verified matured / hits |
|---|---|---|
| 1h | PER HORIZON NOT INDEPENDENTLY VERIFIED | NOT VERIFIED |
| 6h | PER HORIZON NOT INDEPENDENTLY VERIFIED | NOT VERIFIED |
| 24h | PER HORIZON NOT INDEPENDENTLY VERIFIED | NOT VERIFIED |
| 48h | PER HORIZON NOT INDEPENDENTLY VERIFIED | NOT VERIFIED |

- Persisted scans: 289; predictions: 2736; observations: 173458.
- Matured sampled outcomes across 1/6/24/48h: 2039; gap abstentions: 7179. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 0 (sampled only; not a success-rate estimate).
- False positives / missed movers: NOT VERIFIED without eligible continuous outcome coverage.
- Baseline vs challenger: recorded as-of; unbiased held-out lift NOT MEASURED.
- Online Kraken /USD stablecoin-base pairs excluded: 18 (counted from this scan's online AssetPairs metadata, not inferred from price).
- Stablecoin base exclusions: BRL1, BUSD, DAI, EUR, EURC, EUROP, EURQ, EURR, EURT, FDUSD, FRAX, GUSD, PYUSD, QCAD, RLUSD, TGBP, TUSD, USD, USD1, USDC, USDD, USDE, USDG, USDQ, USDR, USDS, USDT, ZUSD.
- DEX: NOT USED; no DEX freshness gate.
- OHLC screening abstentions: 2; details in immutable scan JSON artifact.
- Storage: checksum-sealed ledger pushed non-force and read back before this report. Independent artifact recovery is NOT VERIFIED by this scan alone.
- Errors: none in successful committed scan; a failed workflow must not publish a SUCCESS report.
