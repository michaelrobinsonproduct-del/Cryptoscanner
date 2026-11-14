# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-14T00:54:38.514557+00:00
**GitHub trigger:** authenticated on-demand scan request (verified event=push; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/43537215396
**Source SHA:** e6759a3dde010f1fd87f66a1d483a4b8644cd4a4
**Previous ledger commit:** 0b26a7993e8c34fc507e00ac11451b467fdf4660 (atomic ledger/results publication)
**Ledger generation:** 373 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 8s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 625; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 607; valid market observations: 607; OHLC screened: 21.

## Top WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | Confidence / risk | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---|---|---|
| 1 | XMR/USD | 530.99 | 72.063 | 54.210 | +0.39% | +0.57% | 4.80x | 7.0 | 2026-11-14T00:54:30.669313+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 2 | PEPE/USD | 4.42e-06 | 54.966 | 55.118 | +0.34% | +0.34% | 0.82x | 4.5 | 2026-11-14T00:54:30.669313+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 3 | PUMP/USD | 0.003463 | 52.826 | 56.172 | +0.58% | +0.61% | 0.36x | 5.8 | 2026-11-14T00:54:30.669313+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 4 | TAO/USD | 215.8126 | 52.662 | 55.053 | +0.54% | +0.64% | 0.44x | 7.5 | 2026-11-14T00:54:30.669313+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 5 | DASH/USD | 41.228 | 39.167 | 24.623 | +0.26% | +0.89% | 2.01x | 20.6 | 2026-11-14T00:54:30.669313+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 6 | PENGU/USD | 0.006101 | 38.983 | 33.007 | +0.26% | +0.48% | 1.36x | 4.9 | 2026-11-14T00:54:30.669313+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 7 | MON/USD | 0.01686 | 27.196 | 31.175 | +0.66% | +0.60% | 0.30x | 11.9 | 2026-11-14T00:54:30.669313+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 8 | UAI/USD | 0.03901 | 26.775 | 28.500 | +0.57% | +0.05% | 0.80x | 15.4 | 2026-11-14T00:54:30.669313+00:00 | NOT CALIBRATED / HIGH | WATCH |

**Confidence:** uncalibrated research heuristics, NOT validated probabilities. **BUY:** none authorized. Numerical baseline/challenger scores are uncalibrated paper-only ranking values, not probabilities or validated improvement.

## Learning and coverage

| Forward horizon | Evidence status | Verified matured / hits |
|---|---|---|
| 1h | PER HORIZON NOT INDEPENDENTLY VERIFIED | NOT VERIFIED |
| 6h | PER HORIZON NOT INDEPENDENTLY VERIFIED | NOT VERIFIED |
| 24h | PER HORIZON NOT INDEPENDENTLY VERIFIED | NOT VERIFIED |
| 48h | PER HORIZON NOT INDEPENDENTLY VERIFIED | NOT VERIFIED |

- Persisted scans: 373; predictions: 3438; observations: 224366.
- Matured sampled outcomes across 1/6/24/48h: 2942; gap abstentions: 9945. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 0 (sampled only; not a success-rate estimate).
- False positives / missed movers: NOT VERIFIED without eligible continuous outcome coverage.
- Baseline vs challenger: recorded as-of; unbiased held-out lift NOT MEASURED.
- Online Kraken /USD stablecoin-base pairs excluded: 18 (counted from this scan's online AssetPairs metadata, not inferred from price).
- Stablecoin base exclusions: BRL1, BUSD, DAI, EUR, EURC, EUROP, EURQ, EURR, EURT, FDUSD, FRAX, GUSD, PYUSD, QCAD, RLUSD, TGBP, TUSD, USD, USD1, USDC, USDD, USDE, USDG, USDQ, USDR, USDS, USDT, ZUSD.
- DEX: NOT USED; no DEX freshness gate.
- OHLC screening abstentions: 13; details in immutable scan JSON artifact.
- Storage: ledger and results published in one non-force Git commit and read back. Independent artifact recovery is NOT VERIFIED by this scan alone.
- Errors: none in successful committed scan; a failed workflow must not publish a SUCCESS report.
