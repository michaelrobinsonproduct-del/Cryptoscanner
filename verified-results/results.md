# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-12T05:34:47.545262+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/43161979654
**Source SHA:** 21b4cf643df9f7a7adfddc959660920dd467c70b
**Ledger commit:** 9dd17241bab501855e65a90294519abd3c4ed2d5
**Ledger generation:** 315 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 6s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 624; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 606; valid market observations: 606; OHLC screened: 17.

## Top WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | Confidence / risk | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---|---|---|
| 1 | ZEC/USD | 978.83 | 63.094 | 65.647 | +1.75% | +0.20% | 0.64x | 3.2 | 2026-11-12T05:34:41.603163+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 2 | PEPE/USD | 4.557e-06 | 61.345 | 59.316 | +1.09% | +0.11% | 1.15x | 6.6 | 2026-11-12T05:34:41.603163+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 3 | AVAX/USD | 8.578 | 61.281 | 59.261 | +0.78% | +0.53% | 0.94x | 2.3 | 2026-11-12T05:34:41.603163+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 4 | DOT/USD | 0.8423 | 39.766 | 38.269 | +0.44% | -0.06% | 1.18x | 1.2 | 2026-11-12T05:34:41.603163+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 5 | CAP/USD | 0.101636 | 30.782 | 33.006 | +1.16% | +0.73% | 0.41x | 15.4 | 2026-11-12T05:34:41.603163+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 6 | AKE/USD | 0.00254048 | 29.307 | 31.370 | +2.55% | +1.45% | 0.07x | 37.3 | 2026-11-12T05:34:41.603163+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 7 | KAS/USD | 0.02919 | 28.330 | 34.607 | +0.41% | +0.10% | 0.32x | 13.7 | 2026-11-12T05:34:41.603163+00:00 | NOT CALIBRATED / HIGH | WATCH |

**Confidence:** uncalibrated research heuristics, NOT validated probabilities. **BUY:** none authorized. Numerical baseline/challenger scores are uncalibrated paper-only ranking values, not probabilities or validated improvement.

## Learning and coverage

| Forward horizon | Evidence status | Verified matured / hits |
|---|---|---|
| 1h | PER HORIZON NOT INDEPENDENTLY VERIFIED | NOT VERIFIED |
| 6h | PER HORIZON NOT INDEPENDENTLY VERIFIED | NOT VERIFIED |
| 24h | PER HORIZON NOT INDEPENDENTLY VERIFIED | NOT VERIFIED |
| 48h | PER HORIZON NOT INDEPENDENTLY VERIFIED | NOT VERIFIED |

- Persisted scans: 315; predictions: 3004; observations: 189207.
- Matured sampled outcomes across 1/6/24/48h: 2447; gap abstentions: 7903. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 0 (sampled only; not a success-rate estimate).
- False positives / missed movers: NOT VERIFIED without eligible continuous outcome coverage.
- Baseline vs challenger: recorded as-of; unbiased held-out lift NOT MEASURED.
- Online Kraken /USD stablecoin-base pairs excluded: 18 (counted from this scan's online AssetPairs metadata, not inferred from price).
- Stablecoin base exclusions: BRL1, BUSD, DAI, EUR, EURC, EUROP, EURQ, EURR, EURT, FDUSD, FRAX, GUSD, PYUSD, QCAD, RLUSD, TGBP, TUSD, USD, USD1, USDC, USDD, USDE, USDG, USDQ, USDR, USDS, USDT, ZUSD.
- DEX: NOT USED; no DEX freshness gate.
- OHLC screening abstentions: 10; details in immutable scan JSON artifact.
- Storage: checksum-sealed ledger pushed non-force and read back before this report. Independent artifact recovery is NOT VERIFIED by this scan alone.
- Errors: none in successful committed scan; a failed workflow must not publish a SUCCESS report.
