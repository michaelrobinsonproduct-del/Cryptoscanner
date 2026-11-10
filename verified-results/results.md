# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-10T18:01:51.369116+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/42870668151
**Source SHA:** a401ca9b3fa5588c6780befb93e5eb91f2431f0f
**Ledger commit:** af9a50500b86d89d817f788366431ef3e95193f9
**Ledger generation:** 243 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 4s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 624; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 606; valid market observations: 599; OHLC screened: 14.

## Top WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | Confidence / risk | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---|---|---|
| 1 | TON/USD | 1.115 | 88.760 | 70.613 | +7.21% | +0.63% | 8.39x | 18.0 | 2026-11-10T18:01:47.276558+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 2 | PEPE/USD | 5.266e-06 | 88.162 | 71.831 | +2.81% | +0.27% | 3.87x | 5.7 | 2026-11-10T18:01:47.276558+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 3 | NIGHT/USD | 0.04171 | 80.752 | 63.577 | +3.04% | +1.26% | 2.09x | 2.4 | 2026-11-10T18:01:47.276558+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 4 | LIGHTER/USD | 3.355 | 66.448 | 52.339 | +3.77% | -0.18% | 3.49x | 17.9 | 2026-11-10T18:01:47.276558+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 5 | UAI/USD | 0.04055 | 66.011 | 54.642 | +5.16% | +0.82% | 1.73x | 29.6 | 2026-11-10T18:01:47.276558+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 6 | CAP/USD | 0.103656 | 62.567 | 65.999 | +4.85% | +0.64% | 0.34x | 13.0 | 2026-11-10T18:01:47.276558+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 7 | TRUMP/USD | 1.129 | 47.903 | 34.700 | +0.80% | +1.16% | 1.74x | 8.9 | 2026-11-10T18:01:47.276558+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 8 | XDC/USD | 0.03009 | 36.377 | 44.926 | +2.10% | +0.13% | 0.08x | 20.0 | 2026-11-10T18:01:47.276558+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 9 | JUP/USD | 0.25342 | 34.869 | 33.015 | +0.30% | +0.62% | 0.87x | 12.2 | 2026-11-10T18:01:47.276558+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 10 | MEGA/USD | 0.05082 | 32.595 | 38.214 | +2.07% | +0.69% | 0.09x | 17.8 | 2026-11-10T18:01:47.276558+00:00 | NOT CALIBRATED / HIGH | WATCH |

**Confidence:** uncalibrated research heuristics, NOT validated probabilities. **BUY:** none authorized. Numerical baseline/challenger scores are uncalibrated paper-only ranking values, not probabilities or validated improvement.

## Learning and coverage

| Forward horizon | Evidence status | Verified matured / hits |
|---|---|---|
| 1h | PER HORIZON NOT INDEPENDENTLY VERIFIED | NOT VERIFIED |
| 6h | PER HORIZON NOT INDEPENDENTLY VERIFIED | NOT VERIFIED |
| 24h | PER HORIZON NOT INDEPENDENTLY VERIFIED | NOT VERIFIED |
| 48h | PER HORIZON NOT INDEPENDENTLY VERIFIED | NOT VERIFIED |

- Persisted scans: 243; predictions: 2232; observations: 145763.
- Matured sampled outcomes across 1/6/24/48h: 1283; gap abstentions: 6231. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 0 (sampled only; not a success-rate estimate).
- False positives / missed movers: NOT VERIFIED without eligible continuous outcome coverage.
- Baseline vs challenger: recorded as-of; unbiased held-out lift NOT MEASURED.
- Online Kraken /USD stablecoin-base pairs excluded: 18 (counted from this scan's online AssetPairs metadata, not inferred from price).
- Stablecoin base exclusions: BRL1, BUSD, DAI, EUR, EURC, EUROP, EURQ, EURR, EURT, FDUSD, FRAX, GUSD, PYUSD, QCAD, RLUSD, TGBP, TUSD, USD, USD1, USDC, USDD, USDE, USDG, USDQ, USDR, USDS, USDT, ZUSD.
- DEX: NOT USED; no DEX freshness gate.
- OHLC screening abstentions: 4; details in immutable scan JSON artifact.
- Storage: checksum-sealed ledger pushed non-force and read back before this report. Independent artifact recovery is NOT VERIFIED by this scan alone.
- Errors: none in successful committed scan; a failed workflow must not publish a SUCCESS report.
