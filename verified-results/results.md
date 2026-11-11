# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-11T15:31:16.813196+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/43048750989
**Source SHA:** 21b4cf643df9f7a7adfddc959660920dd467c70b
**Ledger commit:** 10e4ee0b03bb464566cde7b1143870549acec44a
**Ledger generation:** 286 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 7s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 624; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 606; valid market observations: 605; OHLC screened: 24.

## Top WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | Confidence / risk | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---|---|---|
| 1 | XMR/USD | 585.47 | 91.405 | 78.619 | +4.06% | +0.63% | 1.96x | 9.6 | 2026-11-11T15:31:09.421033+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 2 | XLM/USD | 0.150285 | 87.663 | 74.994 | +3.94% | -0.47% | 6.82x | 4.4 | 2026-11-11T15:31:09.421033+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 3 | NIGHT/USD | 0.0458 | 84.027 | 78.985 | +9.26% | +0.77% | 1.12x | 19.7 | 2026-11-11T15:31:09.421033+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 4 | PUMP/USD | 0.003619 | 76.104 | 70.165 | +3.05% | +0.78% | 1.20x | 5.5 | 2026-11-11T15:31:09.421033+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 5 | SUI/USD | 0.8323 | 76.103 | 62.481 | +1.15% | -0.28% | 2.90x | 1.2 | 2026-11-11T15:31:09.421033+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 6 | NEAR/USD | 3.7146 | 71.466 | 77.583 | +3.65% | -0.24% | 0.51x | 5.9 | 2026-11-11T15:31:09.421033+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 7 | HYPE/USD | 72.78 | 67.143 | 59.740 | +0.78% | -0.21% | 1.84x | 1.4 | 2026-11-11T15:31:09.421033+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 8 | TAO/USD | 223.0158 | 66.394 | 68.341 | +2.22% | -0.22% | 0.92x | 4.4 | 2026-11-11T15:31:09.421033+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 9 | SOL/USD | 83.98 | 63.139 | 60.627 | +0.89% | +0.05% | 1.23x | 1.2 | 2026-11-11T15:31:09.421033+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 10 | XRP/USD | 1.05975 | 61.694 | 57.606 | +0.44% | -0.06% | 1.44x | 0.9 | 2026-11-11T15:31:09.421033+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 11 | ADA/USD | 0.176724 | 61.596 | 64.315 | +1.68% | -0.41% | 0.93x | 4.9 | 2026-11-11T15:31:09.421033+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 12 | TON/USD | 1.186 | 60.359 | 65.405 | +4.13% | -0.83% | 0.91x | 16.9 | 2026-11-11T15:31:09.421033+00:00 | NOT CALIBRATED / HIGH | WATCH |

**Confidence:** uncalibrated research heuristics, NOT validated probabilities. **BUY:** none authorized. Numerical baseline/challenger scores are uncalibrated paper-only ranking values, not probabilities or validated improvement.

## Learning and coverage

| Forward horizon | Evidence status | Verified matured / hits |
|---|---|---|
| 1h | PER HORIZON NOT INDEPENDENTLY VERIFIED | NOT VERIFIED |
| 6h | PER HORIZON NOT INDEPENDENTLY VERIFIED | NOT VERIFIED |
| 24h | PER HORIZON NOT INDEPENDENTLY VERIFIED | NOT VERIFIED |
| 48h | PER HORIZON NOT INDEPENDENTLY VERIFIED | NOT VERIFIED |

- Persisted scans: 286; predictions: 2700; observations: 171643.
- Matured sampled outcomes across 1/6/24/48h: 1992; gap abstentions: 7131. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 0 (sampled only; not a success-rate estimate).
- False positives / missed movers: NOT VERIFIED without eligible continuous outcome coverage.
- Baseline vs challenger: recorded as-of; unbiased held-out lift NOT MEASURED.
- Online Kraken /USD stablecoin-base pairs excluded: 18 (counted from this scan's online AssetPairs metadata, not inferred from price).
- Stablecoin base exclusions: BRL1, BUSD, DAI, EUR, EURC, EUROP, EURQ, EURR, EURT, FDUSD, FRAX, GUSD, PYUSD, QCAD, RLUSD, TGBP, TUSD, USD, USD1, USDC, USDD, USDE, USDG, USDQ, USDR, USDS, USDT, ZUSD.
- DEX: NOT USED; no DEX freshness gate.
- OHLC screening abstentions: 5; details in immutable scan JSON artifact.
- Storage: checksum-sealed ledger pushed non-force and read back before this report. Independent artifact recovery is NOT VERIFIED by this scan alone.
- Errors: none in successful committed scan; a failed workflow must not publish a SUCCESS report.
