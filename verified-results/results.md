# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-10T17:35:42.638056+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/42866328616
**Source SHA:** 3774b902ccb4e4fd5507499dc7c96ebbb4185329
**Ledger commit:** 475c7c0937148e836027147de87db6ff9dc4f4d1
**Ledger generation:** 242 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 5s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 624; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 606; valid market observations: 599; OHLC screened: 12.

## Top WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | Confidence / risk | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---|---|---|
| 1 | TON/USD | 1.115 | 76.138 | 65.820 | +7.21% | +1.00% | 1.53x | 26.9 | 2026-11-10T17:35:38.101250+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 2 | CAP/USD | 0.102812 | 70.151 | 63.057 | +4.00% | +2.14% | 0.64x | 6.6 | 2026-11-10T17:35:38.101250+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 3 | PEPE/USD | 5.265e-06 | 69.226 | 68.838 | +2.79% | +0.72% | 0.68x | 11.4 | 2026-11-10T17:35:38.101250+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 4 | LIGHTER/USD | 3.357 | 54.410 | 55.618 | +3.84% | +0.90% | 0.43x | 11.9 | 2026-11-10T17:35:38.101250+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 5 | UAI/USD | 0.04096 | 52.830 | 59.766 | +6.22% | +0.00% | 0.31x | 34.3 | 2026-11-10T17:35:38.101250+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 6 | XDC/USD | 0.03006 | 49.494 | 47.569 | +2.00% | +0.20% | 1.09x | 13.3 | 2026-11-10T17:35:38.101250+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 7 | NIGHT/USD | 0.04116 | 44.393 | 52.341 | +1.68% | -0.10% | 0.25x | 4.9 | 2026-11-10T17:35:38.101250+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 8 | ATOM/USD | 1.3811 | 28.361 | 29.264 | +0.75% | +0.61% | 0.60x | 15.3 | 2026-11-10T17:35:38.101250+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 9 | MEGA/USD | 0.05098 | 27.280 | 36.502 | +2.39% | -0.45% | 0.30x | 25.7 | 2026-11-10T17:35:38.101250+00:00 | NOT CALIBRATED / HIGH | WATCH |

**Confidence:** uncalibrated research heuristics, NOT validated probabilities. **BUY:** none authorized. Numerical baseline/challenger scores are uncalibrated paper-only ranking values, not probabilities or validated improvement.

## Learning and coverage

| Forward horizon | Evidence status | Verified matured / hits |
|---|---|---|
| 1h | PER HORIZON NOT INDEPENDENTLY VERIFIED | NOT VERIFIED |
| 6h | PER HORIZON NOT INDEPENDENTLY VERIFIED | NOT VERIFIED |
| 24h | PER HORIZON NOT INDEPENDENTLY VERIFIED | NOT VERIFIED |
| 48h | PER HORIZON NOT INDEPENDENTLY VERIFIED | NOT VERIFIED |

- Persisted scans: 242; predictions: 2222; observations: 145164.
- Matured sampled outcomes across 1/6/24/48h: 1271; gap abstentions: 6219. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 0 (sampled only; not a success-rate estimate).
- False positives / missed movers: NOT VERIFIED without eligible continuous outcome coverage.
- Baseline vs challenger: recorded as-of; unbiased held-out lift NOT MEASURED.
- Online Kraken /USD stablecoin-base pairs excluded: 18 (counted from this scan's online AssetPairs metadata, not inferred from price).
- Stablecoin base exclusions: BRL1, BUSD, DAI, EUR, EURC, EUROP, EURQ, EURR, EURT, FDUSD, FRAX, GUSD, PYUSD, QCAD, RLUSD, TGBP, TUSD, USD, USD1, USDC, USDD, USDE, USDG, USDQ, USDR, USDS, USDT, ZUSD.
- DEX: NOT USED; no DEX freshness gate.
- OHLC screening abstentions: 3; details in immutable scan JSON artifact.
- Storage: checksum-sealed ledger pushed non-force and read back before this report. Independent artifact recovery is NOT VERIFIED by this scan alone.
- Errors: none in successful committed scan; a failed workflow must not publish a SUCCESS report.
