# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-12T17:05:42.472405+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/43265195853
**Source SHA:** 21b4cf643df9f7a7adfddc959660920dd467c70b
**Ledger commit:** 6be4cf9c143a48bd6f302104b54891fa2fd1c96c
**Ledger generation:** 338 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 3s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 624; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 606; valid market observations: 606; OHLC screened: 10.

## Top WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | Confidence / risk | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---|---|---|
| 1 | TON/USD | 1.25 | 83.489 | 82.098 | +6.56% | -0.48% | 1.38x | 16.0 | 2026-11-12T17:05:39.322919+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 2 | JUP/USD | 0.26302 | 46.319 | 48.977 | +3.08% | -0.35% | 0.91x | 11.8 | 2026-11-12T17:05:39.322919+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 3 | XDC/USD | 0.02935 | 44.780 | 42.403 | +1.00% | +0.10% | 1.19x | 10.2 | 2026-11-12T17:05:39.322919+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 4 | ATOM/USD | 1.4111 | 42.309 | 36.777 | +1.26% | -0.35% | 1.73x | 8.5 | 2026-11-12T17:05:39.322919+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 5 | MEGA/USD | 0.04635 | 32.203 | 40.947 | +3.46% | -0.46% | 0.36x | 30.3 | 2026-11-12T17:05:39.322919+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 6 | CAP/USD | 0.101375 | 23.094 | 29.703 | +0.90% | -0.19% | 0.43x | 15.4 | 2026-11-12T17:05:39.322919+00:00 | NOT CALIBRATED / HIGH | WATCH |

**Confidence:** uncalibrated research heuristics, NOT validated probabilities. **BUY:** none authorized. Numerical baseline/challenger scores are uncalibrated paper-only ranking values, not probabilities or validated improvement.

## Learning and coverage

| Forward horizon | Evidence status | Verified matured / hits |
|---|---|---|
| 1h | PER HORIZON NOT INDEPENDENTLY VERIFIED | NOT VERIFIED |
| 6h | PER HORIZON NOT INDEPENDENTLY VERIFIED | NOT VERIFIED |
| 24h | PER HORIZON NOT INDEPENDENTLY VERIFIED | NOT VERIFIED |
| 48h | PER HORIZON NOT INDEPENDENTLY VERIFIED | NOT VERIFIED |

- Persisted scans: 338; predictions: 3143; observations: 203144.
- Matured sampled outcomes across 1/6/24/48h: 2783; gap abstentions: 8316. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 0 (sampled only; not a success-rate estimate).
- False positives / missed movers: NOT VERIFIED without eligible continuous outcome coverage.
- Baseline vs challenger: recorded as-of; unbiased held-out lift NOT MEASURED.
- Online Kraken /USD stablecoin-base pairs excluded: 18 (counted from this scan's online AssetPairs metadata, not inferred from price).
- Stablecoin base exclusions: BRL1, BUSD, DAI, EUR, EURC, EUROP, EURQ, EURR, EURT, FDUSD, FRAX, GUSD, PYUSD, QCAD, RLUSD, TGBP, TUSD, USD, USD1, USDC, USDD, USDE, USDG, USDQ, USDR, USDS, USDT, ZUSD.
- DEX: NOT USED; no DEX freshness gate.
- OHLC screening abstentions: 4; details in immutable scan JSON artifact.
- Storage: checksum-sealed ledger pushed non-force and read back before this report. Independent artifact recovery is NOT VERIFIED by this scan alone.
- Errors: none in successful committed scan; a failed workflow must not publish a SUCCESS report.
