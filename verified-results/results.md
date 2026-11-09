# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-09T23:51:27.879121+00:00
**GitHub trigger:** authenticated issue heartbeat (verified event=issue_comment; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/42723597855
**Source SHA:** 47efb405551d493df87bca8b2583b5611396f1fa
**Ledger commit:** a21f656c1253e81d0b6b7178f01140d8624cdd22
**Ledger generation:** 219 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 7s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 624; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 606; valid market observations: 602; OHLC screened: 24.

## Top WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | Confidence / risk | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---|---|---|
| 1 | AVAX/USD | 8.638 | 90.798 | 98.263 | +8.94% | -0.35% | 0.43x | 3.5 | 2026-11-09T23:51:21.266017+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 2 | UNI/USD | 6.97 | 87.850 | 74.131 | +2.74% | -0.26% | 3.15x | 0.1 | 2026-11-09T23:51:21.266017+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 3 | ONDO/USD | 0.3727 | 83.605 | 91.565 | +6.01% | +0.11% | 0.15x | 6.4 | 2026-11-09T23:51:21.266017+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 4 | VVV/USD | 21.659 | 74.433 | 81.323 | +7.97% | +0.20% | 0.21x | 1.4 | 2026-11-09T23:51:21.266017+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 5 | PEPE/USD | 5.137e-06 | 71.460 | 79.936 | +3.84% | +0.02% | 0.14x | 3.9 | 2026-11-09T23:51:21.266017+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 6 | SUI/USD | 0.842 | 69.450 | 71.651 | +2.63% | -0.07% | 0.82x | 3.6 | 2026-11-09T23:51:21.266017+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 7 | TAO/USD | 222.323 | 63.219 | 71.876 | +2.57% | +0.03% | 0.12x | 2.2 | 2026-11-09T23:51:21.266017+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 8 | AAVE/USD | 131.42 | 61.681 | 72.267 | +4.34% | -0.47% | 0.18x | 4.6 | 2026-11-09T23:51:21.266017+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 9 | XDG/USD | 0.0699271 | 57.574 | 64.355 | +1.53% | +0.07% | 0.29x | 0.0 | 2026-11-09T23:51:21.266017+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 10 | GBP/USD | 1.34366 | 56.352 | 59.044 | +0.60% | +0.00% | 0.73x | 0.4 | 2026-11-09T23:51:21.266017+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 11 | HYPE/USD | 75.1 | 54.913 | 60.256 | +0.85% | -0.07% | 0.50x | 1.3 | 2026-11-09T23:51:21.266017+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 12 | XLM/USD | 0.147227 | 52.784 | 58.776 | +0.71% | -0.01% | 0.41x | 2.4 | 2026-11-09T23:51:21.266017+00:00 | NOT CALIBRATED / HIGH | WATCH |

**Confidence:** uncalibrated research heuristics, NOT validated probabilities. **BUY:** none authorized. Numerical baseline/challenger scores are uncalibrated paper-only ranking values, not probabilities or validated improvement.

## Learning and coverage

| Forward horizon | Evidence status | Verified matured / hits |
|---|---|---|
| 1h | PER HORIZON NOT INDEPENDENTLY VERIFIED | NOT VERIFIED |
| 6h | PER HORIZON NOT INDEPENDENTLY VERIFIED | NOT VERIFIED |
| 24h | PER HORIZON NOT INDEPENDENTLY VERIFIED | NOT VERIFIED |
| 48h | PER HORIZON NOT INDEPENDENTLY VERIFIED | NOT VERIFIED |

- Persisted scans: 219; predictions: 2031; observations: 132381.
- Matured sampled outcomes across 1/6/24/48h: 1141; gap abstentions: 5295. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 0 (sampled only; not a success-rate estimate).
- False positives / missed movers: NOT VERIFIED without eligible continuous outcome coverage.
- Baseline vs challenger: recorded as-of; unbiased held-out lift NOT MEASURED.
- Online Kraken /USD stablecoin-base pairs excluded: 18 (counted from this scan's online AssetPairs metadata, not inferred from price).
- Stablecoin base exclusions: BRL1, BUSD, DAI, EUR, EURC, EUROP, EURQ, EURR, EURT, FDUSD, FRAX, GUSD, PYUSD, QCAD, RLUSD, TGBP, TUSD, USD, USD1, USDC, USDD, USDE, USDG, USDQ, USDR, USDS, USDT, ZUSD.
- DEX: NOT USED; no DEX freshness gate.
- OHLC screening abstentions: 8; details in immutable scan JSON artifact.
- Storage: checksum-sealed ledger pushed non-force and read back before this report. Independent artifact recovery is NOT VERIFIED by this scan alone.
- Errors: none in successful committed scan; a failed workflow must not publish a SUCCESS report.
