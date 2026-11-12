# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-12T12:38:59.345834+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/43219309953
**Source SHA:** 21b4cf643df9f7a7adfddc959660920dd467c70b
**Ledger commit:** 4735802eab439747ab83242c338059923e981bf5
**Ledger generation:** 329 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 3s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 624; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 606; valid market observations: 606; OHLC screened: 10.

## Top WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | Confidence / risk | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---|---|---|
| 1 | TON/USD | 1.265 | 102.801 | 80.176 | +7.84% | +1.52% | 2.56x | 15.8 | 2026-11-12T12:38:56.404590+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 2 | ZEC/USD | 970.73 | 59.077 | 60.462 | +0.91% | -0.36% | 1.04x | 1.8 | 2026-11-12T12:38:56.404590+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 3 | MON/USD | 0.01691 | 57.402 | 37.029 | +1.50% | +1.07% | 2.55x | 11.8 | 2026-11-12T12:38:56.404590+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 4 | JUP/USD | 0.25823 | 43.185 | 33.473 | +1.20% | -0.82% | 2.38x | 15.9 | 2026-11-12T12:38:56.404590+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 5 | XDC/USD | 0.02962 | 41.109 | 45.621 | +1.93% | +0.17% | 0.46x | 16.9 | 2026-11-12T12:38:56.404590+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 6 | BAT/USD | 0.12075 | 36.536 | 48.301 | +2.57% | -0.53% | 0.09x | 5.0 | 2026-11-12T12:38:56.404590+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 7 | CAP/USD | 0.101003 | 31.327 | 24.582 | +0.53% | -0.14% | 1.74x | 21.0 | 2026-11-12T12:38:56.404590+00:00 | NOT CALIBRATED / HIGH | WATCH |

**Confidence:** uncalibrated research heuristics, NOT validated probabilities. **BUY:** none authorized. Numerical baseline/challenger scores are uncalibrated paper-only ranking values, not probabilities or validated improvement.

## Learning and coverage

| Forward horizon | Evidence status | Verified matured / hits |
|---|---|---|
| 1h | PER HORIZON NOT INDEPENDENTLY VERIFIED | NOT VERIFIED |
| 6h | PER HORIZON NOT INDEPENDENTLY VERIFIED | NOT VERIFIED |
| 24h | PER HORIZON NOT INDEPENDENTLY VERIFIED | NOT VERIFIED |
| 48h | PER HORIZON NOT INDEPENDENTLY VERIFIED | NOT VERIFIED |

- Persisted scans: 329; predictions: 3092; observations: 197690.
- Matured sampled outcomes across 1/6/24/48h: 2676; gap abstentions: 8102. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 0 (sampled only; not a success-rate estimate).
- False positives / missed movers: NOT VERIFIED without eligible continuous outcome coverage.
- Baseline vs challenger: recorded as-of; unbiased held-out lift NOT MEASURED.
- Online Kraken /USD stablecoin-base pairs excluded: 18 (counted from this scan's online AssetPairs metadata, not inferred from price).
- Stablecoin base exclusions: BRL1, BUSD, DAI, EUR, EURC, EUROP, EURQ, EURR, EURT, FDUSD, FRAX, GUSD, PYUSD, QCAD, RLUSD, TGBP, TUSD, USD, USD1, USDC, USDD, USDE, USDG, USDQ, USDR, USDS, USDT, ZUSD.
- DEX: NOT USED; no DEX freshness gate.
- OHLC screening abstentions: 3; details in immutable scan JSON artifact.
- Storage: checksum-sealed ledger pushed non-force and read back before this report. Independent artifact recovery is NOT VERIFIED by this scan alone.
- Errors: none in successful committed scan; a failed workflow must not publish a SUCCESS report.
