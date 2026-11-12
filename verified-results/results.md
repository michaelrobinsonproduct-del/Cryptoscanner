# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-12T18:34:52.527027+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/43280858996
**Source SHA:** 21b4cf643df9f7a7adfddc959660920dd467c70b
**Ledger commit:** 4f26fb610dae3019ae936bb7655f13604217d173
**Ledger generation:** 341 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 6s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 624; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 606; valid market observations: 606; OHLC screened: 16.

## Top WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | Confidence / risk | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---|---|---|
| 1 | JUP/USD | 0.2648 | 63.944 | 51.797 | +3.77% | +0.34% | 2.04x | 15.5 | 2026-11-12T18:34:46.315798+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 2 | XDC/USD | 0.0295 | 63.332 | 47.823 | +1.51% | +0.10% | 3.05x | 6.8 | 2026-11-12T18:34:46.315798+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 3 | TON/USD | 1.186 | 59.231 | 48.788 | +1.11% | -0.91% | 3.42x | 8.4 | 2026-11-12T18:34:46.315798+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 4 | TIA/USD | 0.4176 | 54.679 | 40.882 | +0.77% | -0.24% | 3.18x | 2.4 | 2026-11-12T18:34:46.315798+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 5 | MEGA/USD | 0.04602 | 52.047 | 34.654 | +2.72% | +0.48% | 3.54x | 32.5 | 2026-11-12T18:34:46.315798+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 6 | BAT/USD | 0.12239 | 50.678 | 58.477 | +3.96% | +0.21% | 0.12x | 4.9 | 2026-11-12T18:34:46.315798+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 7 | MON/USD | 0.01726 | 40.274 | 53.121 | +3.60% | -0.86% | 0.15x | 11.6 | 2026-11-12T18:34:46.315798+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 8 | ATOM/USD | 1.4169 | 38.498 | 38.124 | +1.68% | +0.21% | 0.93x | 12.0 | 2026-11-12T18:34:46.315798+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 9 | CAP/USD | 0.101784 | 29.543 | 27.151 | +1.30% | -0.03% | 1.25x | 26.2 | 2026-11-12T18:34:46.315798+00:00 | NOT CALIBRATED / HIGH | WATCH |

**Confidence:** uncalibrated research heuristics, NOT validated probabilities. **BUY:** none authorized. Numerical baseline/challenger scores are uncalibrated paper-only ranking values, not probabilities or validated improvement.

## Learning and coverage

| Forward horizon | Evidence status | Verified matured / hits |
|---|---|---|
| 1h | PER HORIZON NOT INDEPENDENTLY VERIFIED | NOT VERIFIED |
| 6h | PER HORIZON NOT INDEPENDENTLY VERIFIED | NOT VERIFIED |
| 24h | PER HORIZON NOT INDEPENDENTLY VERIFIED | NOT VERIFIED |
| 48h | PER HORIZON NOT INDEPENDENTLY VERIFIED | NOT VERIFIED |

- Persisted scans: 341; predictions: 3166; observations: 204962.
- Matured sampled outcomes across 1/6/24/48h: 2820; gap abstentions: 8379. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 0 (sampled only; not a success-rate estimate).
- False positives / missed movers: NOT VERIFIED without eligible continuous outcome coverage.
- Baseline vs challenger: recorded as-of; unbiased held-out lift NOT MEASURED.
- Online Kraken /USD stablecoin-base pairs excluded: 18 (counted from this scan's online AssetPairs metadata, not inferred from price).
- Stablecoin base exclusions: BRL1, BUSD, DAI, EUR, EURC, EUROP, EURQ, EURR, EURT, FDUSD, FRAX, GUSD, PYUSD, QCAD, RLUSD, TGBP, TUSD, USD, USD1, USDC, USDD, USDE, USDG, USDQ, USDR, USDS, USDT, ZUSD.
- DEX: NOT USED; no DEX freshness gate.
- OHLC screening abstentions: 7; details in immutable scan JSON artifact.
- Storage: checksum-sealed ledger pushed non-force and read back before this report. Independent artifact recovery is NOT VERIFIED by this scan alone.
- Errors: none in successful committed scan; a failed workflow must not publish a SUCCESS report.
