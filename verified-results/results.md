# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-12T04:39:28.094591+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/43155959954
**Source SHA:** 21b4cf643df9f7a7adfddc959660920dd467c70b
**Ledger commit:** ef733a9748afd1da3a4114cc4746f6bab88015c6
**Ledger generation:** 313 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 5s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 624; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 606; valid market observations: 606; OHLC screened: 19.

## Top WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | Confidence / risk | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---|---|---|
| 1 | PEPE/USD | 4.557e-06 | 63.596 | 59.316 | +1.09% | +0.09% | 1.38x | 6.6 | 2026-11-12T04:39:22.862290+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 2 | ZEC/USD | 978.54 | 55.843 | 64.211 | +1.72% | -0.79% | 0.56x | 5.6 | 2026-11-12T04:39:22.862290+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 3 | INJ/USD | 7.561 | 52.050 | 48.861 | +0.32% | -0.46% | 1.55x | 4.0 | 2026-11-12T04:39:22.862290+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 4 | DOT/USD | 0.8408 | 51.226 | 37.058 | +0.26% | -0.17% | 7.38x | 1.2 | 2026-11-12T04:39:22.862290+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 5 | AVAX/USD | 8.55 | 50.626 | 55.783 | +0.45% | -0.37% | 0.67x | 4.7 | 2026-11-12T04:39:22.862290+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 6 | TON/USD | 1.176 | 37.371 | 42.111 | +0.26% | -0.42% | 0.74x | 8.5 | 2026-11-12T04:39:22.862290+00:00 | NOT CALIBRATED / HIGH | WATCH |

**Confidence:** uncalibrated research heuristics, NOT validated probabilities. **BUY:** none authorized. Numerical baseline/challenger scores are uncalibrated paper-only ranking values, not probabilities or validated improvement.

## Learning and coverage

| Forward horizon | Evidence status | Verified matured / hits |
|---|---|---|
| 1h | PER HORIZON NOT INDEPENDENTLY VERIFIED | NOT VERIFIED |
| 6h | PER HORIZON NOT INDEPENDENTLY VERIFIED | NOT VERIFIED |
| 24h | PER HORIZON NOT INDEPENDENTLY VERIFIED | NOT VERIFIED |
| 48h | PER HORIZON NOT INDEPENDENTLY VERIFIED | NOT VERIFIED |

- Persisted scans: 313; predictions: 2992; observations: 187995.
- Matured sampled outcomes across 1/6/24/48h: 2401; gap abstentions: 7872. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 0 (sampled only; not a success-rate estimate).
- False positives / missed movers: NOT VERIFIED without eligible continuous outcome coverage.
- Baseline vs challenger: recorded as-of; unbiased held-out lift NOT MEASURED.
- Online Kraken /USD stablecoin-base pairs excluded: 18 (counted from this scan's online AssetPairs metadata, not inferred from price).
- Stablecoin base exclusions: BRL1, BUSD, DAI, EUR, EURC, EUROP, EURQ, EURR, EURT, FDUSD, FRAX, GUSD, PYUSD, QCAD, RLUSD, TGBP, TUSD, USD, USD1, USDC, USDD, USDE, USDG, USDQ, USDR, USDS, USDT, ZUSD.
- DEX: NOT USED; no DEX freshness gate.
- OHLC screening abstentions: 13; details in immutable scan JSON artifact.
- Storage: checksum-sealed ledger pushed non-force and read back before this report. Independent artifact recovery is NOT VERIFIED by this scan alone.
- Errors: none in successful committed scan; a failed workflow must not publish a SUCCESS report.
