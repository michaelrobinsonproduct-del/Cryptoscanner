# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-09T23:45:47.164504+00:00
**GitHub trigger:** authenticated issue heartbeat (verified event=issue_comment; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/42722837359
**Source SHA:** 47efb405551d493df87bca8b2583b5611396f1fa
**Ledger commit:** 752126f4a4f6813b17512aa010f3bc362d0d0a3e
**Ledger generation:** 218 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 7s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 624; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 606; valid market observations: 602; OHLC screened: 24.

## Top WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | Confidence / risk | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---|---|---|
| 1 | AVAX/USD | 8.646 | 91.372 | 97.108 | +9.04% | -0.15% | 0.50x | 5.8 | 2026-11-09T23:45:40.342547+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 2 | PEPE/USD | 5.128e-06 | 88.318 | 78.661 | +3.66% | -0.23% | 2.08x | 3.9 | 2026-11-09T23:45:40.342547+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 3 | ONDO/USD | 0.37197 | 80.039 | 89.417 | +5.80% | -0.10% | 0.11x | 7.8 | 2026-11-09T23:45:40.342547+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 4 | UNI/USD | 6.9595 | 71.542 | 71.108 | +2.59% | -0.65% | 1.37x | 4.0 | 2026-11-09T23:45:40.342547+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 5 | VVV/USD | 21.589 | 69.249 | 78.948 | +7.62% | -0.02% | 0.04x | 6.0 | 2026-11-09T23:45:40.342547+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 6 | SUI/USD | 0.8422 | 65.490 | 72.412 | +2.66% | -0.17% | 0.39x | 2.4 | 2026-11-09T23:45:40.342547+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 7 | AAVE/USD | 131.31 | 62.318 | 72.069 | +4.26% | -0.41% | 0.23x | 3.8 | 2026-11-09T23:45:40.342547+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 8 | TAO/USD | 222.2715 | 61.648 | 71.215 | +2.54% | -0.11% | 0.10x | 3.2 | 2026-11-09T23:45:40.342547+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 9 | XDG/USD | 0.0698532 | 60.128 | 63.507 | +1.42% | -0.11% | 0.71x | 0.0 | 2026-11-09T23:45:40.342547+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 10 | HYPE/USD | 75.05 | 56.895 | 59.119 | +0.78% | -0.27% | 0.91x | 2.7 | 2026-11-09T23:45:40.342547+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 11 | GBP/USD | 1.34367 | 54.247 | 59.086 | +0.60% | -0.01% | 0.52x | 0.3 | 2026-11-09T23:45:40.342547+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 12 | AUD/USD | 0.69242 | 52.212 | 41.664 | +0.82% | +0.01% | 2.05x | 1.9 | 2026-11-09T23:45:40.342547+00:00 | NOT CALIBRATED / HIGH | WATCH |

**Confidence:** uncalibrated research heuristics, NOT validated probabilities. **BUY:** none authorized. Numerical baseline/challenger scores are uncalibrated paper-only ranking values, not probabilities or validated improvement.

## Learning and coverage

| Forward horizon | Evidence status | Verified matured / hits |
|---|---|---|
| 1h | PER HORIZON NOT INDEPENDENTLY VERIFIED | NOT VERIFIED |
| 6h | PER HORIZON NOT INDEPENDENTLY VERIFIED | NOT VERIFIED |
| 24h | PER HORIZON NOT INDEPENDENTLY VERIFIED | NOT VERIFIED |
| 48h | PER HORIZON NOT INDEPENDENTLY VERIFIED | NOT VERIFIED |

- Persisted scans: 218; predictions: 2019; observations: 131779.
- Matured sampled outcomes across 1/6/24/48h: 1141; gap abstentions: 5295. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 0 (sampled only; not a success-rate estimate).
- False positives / missed movers: NOT VERIFIED without eligible continuous outcome coverage.
- Baseline vs challenger: recorded as-of; unbiased held-out lift NOT MEASURED.
- Online Kraken /USD stablecoin-base pairs excluded: 18 (counted from this scan's online AssetPairs metadata, not inferred from price).
- Stablecoin base exclusions: BRL1, BUSD, DAI, EUR, EURC, EUROP, EURQ, EURR, EURT, FDUSD, FRAX, GUSD, PYUSD, QCAD, RLUSD, TGBP, TUSD, USD, USD1, USDC, USDD, USDE, USDG, USDQ, USDR, USDS, USDT, ZUSD.
- DEX: NOT USED; no DEX freshness gate.
- OHLC screening abstentions: 9; details in immutable scan JSON artifact.
- Storage: checksum-sealed ledger pushed non-force and read back before this report. Independent artifact recovery is NOT VERIFIED by this scan alone.
- Errors: none in successful committed scan; a failed workflow must not publish a SUCCESS report.
