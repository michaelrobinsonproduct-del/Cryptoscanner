# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-10T16:04:16.701132+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/42850556701
**Source SHA:** 3774b902ccb4e4fd5507499dc7c96ebbb4185329
**Ledger commit:** c1255f969af68293b463ede3d6e051101f0595a4
**Ledger generation:** 239 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 5s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 624; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 606; valid market observations: 593; OHLC screened: 16.

## Top WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | Confidence / risk | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---|---|---|
| 1 | UAI/USD | 0.04097 | 73.547 | 58.982 | +6.25% | +2.44% | 1.24x | 36.6 | 2026-11-10T16:04:12.015505+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 2 | PEPE/USD | 5.234e-06 | 71.759 | 68.394 | +2.19% | +0.46% | 1.11x | 3.8 | 2026-11-10T16:04:12.015505+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 3 | PLAY/USD | 0.008609 | 69.943 | 49.139 | +4.82% | +1.16% | 31.54x | 31.4 | 2026-11-10T16:04:12.015505+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 4 | NIGHT/USD | 0.04128 | 64.388 | 52.222 | +1.98% | +0.44% | 2.00x | 7.3 | 2026-11-10T16:04:12.015505+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 5 | TON/USD | 1.103 | 63.114 | 63.069 | +6.06% | +1.57% | 0.22x | 27.2 | 2026-11-10T16:04:12.015505+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 6 | CAP/USD | 0.101064 | 61.453 | 39.775 | +2.23% | +1.34% | 7.28x | 26.4 | 2026-11-10T16:04:12.015505+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 7 | XDC/USD | 0.03021 | 59.237 | 49.200 | +2.51% | -0.46% | 2.23x | 16.6 | 2026-11-10T16:04:12.015505+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 8 | XPL/USD | 0.0526 | 59.171 | 34.462 | +1.54% | +1.94% | 31.65x | 19.0 | 2026-11-10T16:04:12.015505+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 9 | ZRO/USD | 1.49 | 58.319 | 38.580 | +0.95% | +0.95% | 5.48x | 20.1 | 2026-11-10T16:04:12.015505+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 10 | JUP/USD | 0.25347 | 57.812 | 36.413 | +0.32% | +1.28% | 53.51x | 18.9 | 2026-11-10T16:04:12.015505+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 11 | LIGHTER/USD | 3.326 | 51.055 | 45.864 | +2.88% | +1.74% | 0.65x | 18.0 | 2026-11-10T16:04:12.015505+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 12 | ATOM/USD | 1.3812 | 44.896 | 30.535 | +0.76% | +1.14% | 1.87x | 12.3 | 2026-11-10T16:04:12.015505+00:00 | NOT CALIBRATED / HIGH | WATCH |

**Confidence:** uncalibrated research heuristics, NOT validated probabilities. **BUY:** none authorized. Numerical baseline/challenger scores are uncalibrated paper-only ranking values, not probabilities or validated improvement.

## Learning and coverage

| Forward horizon | Evidence status | Verified matured / hits |
|---|---|---|
| 1h | PER HORIZON NOT INDEPENDENTLY VERIFIED | NOT VERIFIED |
| 6h | PER HORIZON NOT INDEPENDENTLY VERIFIED | NOT VERIFIED |
| 24h | PER HORIZON NOT INDEPENDENTLY VERIFIED | NOT VERIFIED |
| 48h | PER HORIZON NOT INDEPENDENTLY VERIFIED | NOT VERIFIED |

- Persisted scans: 239; predictions: 2195; observations: 143373.
- Matured sampled outcomes across 1/6/24/48h: 1235; gap abstentions: 6145. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 0 (sampled only; not a success-rate estimate).
- False positives / missed movers: NOT VERIFIED without eligible continuous outcome coverage.
- Baseline vs challenger: recorded as-of; unbiased held-out lift NOT MEASURED.
- Online Kraken /USD stablecoin-base pairs excluded: 18 (counted from this scan's online AssetPairs metadata, not inferred from price).
- Stablecoin base exclusions: BRL1, BUSD, DAI, EUR, EURC, EUROP, EURQ, EURR, EURT, FDUSD, FRAX, GUSD, PYUSD, QCAD, RLUSD, TGBP, TUSD, USD, USD1, USDC, USDD, USDE, USDG, USDQ, USDR, USDS, USDT, ZUSD.
- DEX: NOT USED; no DEX freshness gate.
- OHLC screening abstentions: 1; details in immutable scan JSON artifact.
- Storage: checksum-sealed ledger pushed non-force and read back before this report. Independent artifact recovery is NOT VERIFIED by this scan alone.
- Errors: none in successful committed scan; a failed workflow must not publish a SUCCESS report.
