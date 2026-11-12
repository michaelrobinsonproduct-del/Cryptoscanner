# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-12T17:36:16.487681+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/43270614182
**Source SHA:** 21b4cf643df9f7a7adfddc959660920dd467c70b
**Ledger commit:** bb6e835cdc63e8931636174c82c54e69a24fb591
**Ledger generation:** 339 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 4s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 624; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 606; valid market observations: 606; OHLC screened: 13.

## Top WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | Confidence / risk | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---|---|---|
| 1 | TON/USD | 1.23 | 69.093 | 75.030 | +4.86% | -0.32% | 0.57x | 8.1 | 2026-11-12T17:36:12.030168+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 2 | MON/USD | 0.01722 | 67.672 | 48.286 | +3.36% | +0.88% | 5.42x | 17.4 | 2026-11-12T17:36:12.030168+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 3 | MEGA/USD | 0.04585 | 41.845 | 33.007 | +2.34% | -1.23% | 3.56x | 30.6 | 2026-11-12T17:36:12.030168+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 4 | ATOM/USD | 1.4107 | 41.591 | 35.941 | +1.23% | +0.32% | 1.41x | 9.9 | 2026-11-12T17:36:12.030168+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 5 | XDC/USD | 0.02947 | 39.840 | 41.937 | +1.41% | +0.41% | 0.59x | 17.0 | 2026-11-12T17:36:12.030168+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 6 | JUP/USD | 0.2607 | 34.679 | 41.849 | +2.17% | -0.84% | 0.70x | 13.1 | 2026-11-12T17:36:12.030168+00:00 | NOT CALIBRATED / HIGH | WATCH |

**Confidence:** uncalibrated research heuristics, NOT validated probabilities. **BUY:** none authorized. Numerical baseline/challenger scores are uncalibrated paper-only ranking values, not probabilities or validated improvement.

## Learning and coverage

| Forward horizon | Evidence status | Verified matured / hits |
|---|---|---|
| 1h | PER HORIZON NOT INDEPENDENTLY VERIFIED | NOT VERIFIED |
| 6h | PER HORIZON NOT INDEPENDENTLY VERIFIED | NOT VERIFIED |
| 24h | PER HORIZON NOT INDEPENDENTLY VERIFIED | NOT VERIFIED |
| 48h | PER HORIZON NOT INDEPENDENTLY VERIFIED | NOT VERIFIED |

- Persisted scans: 339; predictions: 3149; observations: 203750.
- Matured sampled outcomes across 1/6/24/48h: 2796; gap abstentions: 8339. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 0 (sampled only; not a success-rate estimate).
- False positives / missed movers: NOT VERIFIED without eligible continuous outcome coverage.
- Baseline vs challenger: recorded as-of; unbiased held-out lift NOT MEASURED.
- Online Kraken /USD stablecoin-base pairs excluded: 18 (counted from this scan's online AssetPairs metadata, not inferred from price).
- Stablecoin base exclusions: BRL1, BUSD, DAI, EUR, EURC, EUROP, EURQ, EURR, EURT, FDUSD, FRAX, GUSD, PYUSD, QCAD, RLUSD, TGBP, TUSD, USD, USD1, USDC, USDD, USDE, USDG, USDQ, USDR, USDS, USDT, ZUSD.
- DEX: NOT USED; no DEX freshness gate.
- OHLC screening abstentions: 7; details in immutable scan JSON artifact.
- Storage: checksum-sealed ledger pushed non-force and read back before this report. Independent artifact recovery is NOT VERIFIED by this scan alone.
- Errors: none in successful committed scan; a failed workflow must not publish a SUCCESS report.
