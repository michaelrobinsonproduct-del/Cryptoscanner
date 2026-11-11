# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-11T06:29:14.103892+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/42972571254
**Source SHA:** 21b4cf643df9f7a7adfddc959660920dd467c70b
**Ledger commit:** cb5d90b059e0a845b46817d79c0f6bc491eea91d
**Ledger generation:** 268 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 9s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 624; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 606; valid market observations: 602; OHLC screened: 24.

## Top WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | Confidence / risk | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---|---|---|
| 1 | ADA/USD | 0.174872 | 71.904 | 58.002 | +0.61% | -0.22% | 2.91x | 2.6 | 2026-11-11T06:29:05.286625+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 2 | NEAR/USD | 3.6179 | 69.273 | 58.895 | +0.95% | -0.26% | 2.17x | 5.5 | 2026-11-11T06:29:05.286625+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 3 | ETH/USD | 2062.25 | 63.793 | 58.693 | +0.57% | -0.14% | 1.58x | 0.5 | 2026-11-11T06:29:05.286625+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 4 | AVAX/USD | 8.478 | 58.943 | 62.602 | +1.34% | -0.01% | 0.64x | 3.5 | 2026-11-11T06:29:05.286625+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 5 | XMR/USD | 567.35 | 56.087 | 57.420 | +0.84% | -0.25% | 0.99x | 6.9 | 2026-11-11T06:29:05.286625+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 6 | NIGHT/USD | 0.04292 | 50.111 | 51.660 | +2.39% | +0.02% | 0.83x | 16.3 | 2026-11-11T06:29:05.286625+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 7 | INJ/USD | 8.151 | 45.504 | 50.664 | +1.82% | -0.07% | 0.52x | 8.6 | 2026-11-11T06:29:05.286625+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 8 | ZRO/USD | 1.545 | 44.155 | 40.970 | +0.72% | -0.52% | 1.58x | 12.9 | 2026-11-11T06:29:05.286625+00:00 | NOT CALIBRATED / HIGH | WATCH |

**Confidence:** uncalibrated research heuristics, NOT validated probabilities. **BUY:** none authorized. Numerical baseline/challenger scores are uncalibrated paper-only ranking values, not probabilities or validated improvement.

## Learning and coverage

| Forward horizon | Evidence status | Verified matured / hits |
|---|---|---|
| 1h | PER HORIZON NOT INDEPENDENTLY VERIFIED | NOT VERIFIED |
| 6h | PER HORIZON NOT INDEPENDENTLY VERIFIED | NOT VERIFIED |
| 24h | PER HORIZON NOT INDEPENDENTLY VERIFIED | NOT VERIFIED |
| 48h | PER HORIZON NOT INDEPENDENTLY VERIFIED | NOT VERIFIED |

- Persisted scans: 268; predictions: 2489; observations: 160779.
- Matured sampled outcomes across 1/6/24/48h: 1767; gap abstentions: 6678. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 0 (sampled only; not a success-rate estimate).
- False positives / missed movers: NOT VERIFIED without eligible continuous outcome coverage.
- Baseline vs challenger: recorded as-of; unbiased held-out lift NOT MEASURED.
- Online Kraken /USD stablecoin-base pairs excluded: 18 (counted from this scan's online AssetPairs metadata, not inferred from price).
- Stablecoin base exclusions: BRL1, BUSD, DAI, EUR, EURC, EUROP, EURQ, EURR, EURT, FDUSD, FRAX, GUSD, PYUSD, QCAD, RLUSD, TGBP, TUSD, USD, USD1, USDC, USDD, USDE, USDG, USDQ, USDR, USDS, USDT, ZUSD.
- DEX: NOT USED; no DEX freshness gate.
- OHLC screening abstentions: 16; details in immutable scan JSON artifact.
- Storage: checksum-sealed ledger pushed non-force and read back before this report. Independent artifact recovery is NOT VERIFIED by this scan alone.
- Errors: none in successful committed scan; a failed workflow must not publish a SUCCESS report.
