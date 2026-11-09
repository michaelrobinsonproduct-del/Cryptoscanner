# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-09T22:54:33.477840+00:00
**GitHub trigger:** authenticated issue heartbeat (verified event=issue_comment; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/42715828260
**Source SHA:** 47efb405551d493df87bca8b2583b5611396f1fa
**Ledger commit:** b43779ab62c4ebd1b9d23827aa32bea6cf5021e6
**Ledger generation:** 215 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 8s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 624; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 606; valid market observations: 602; OHLC screened: 24.

## Top WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | Confidence / risk | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---|---|---|
| 1 | ONDO/USD | 0.37701 | 111.511 | 94.779 | +7.23% | +0.35% | 4.37x | 6.4 | 2026-11-09T22:54:25.293316+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 2 | AVAX/USD | 8.643 | 101.973 | 97.685 | +9.00% | +0.30% | 1.28x | 4.6 | 2026-11-09T22:54:25.293316+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 3 | VVV/USD | 21.825 | 92.882 | 79.246 | +8.80% | -0.27% | 4.25x | 6.0 | 2026-11-09T22:54:25.293316+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 4 | TAO/USD | 223.6912 | 92.797 | 77.266 | +3.20% | +0.11% | 3.96x | 0.2 | 2026-11-09T22:54:25.293316+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 5 | UNI/USD | 7.0543 | 80.484 | 80.702 | +3.99% | +0.34% | 0.81x | 4.4 | 2026-11-09T22:54:25.293316+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 6 | LINK/USD | 10.69058 | 77.825 | 74.464 | +2.78% | +0.13% | 1.27x | 0.0 | 2026-11-09T22:54:25.293316+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 7 | PEPE/USD | 5.134e-06 | 77.050 | 79.512 | +3.78% | +0.41% | 0.55x | 3.9 | 2026-11-09T22:54:25.293316+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 8 | SUI/USD | 0.8476 | 74.827 | 77.618 | +3.32% | -0.02% | 0.73x | 1.2 | 2026-11-09T22:54:25.293316+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 9 | SOL/USD | 86.88 | 72.205 | 57.906 | +0.50% | +0.24% | 2.31x | 1.2 | 2026-11-09T22:54:25.293316+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 10 | ENA/USD | 0.1546 | 69.188 | 76.488 | +4.11% | -0.06% | 0.30x | 6.5 | 2026-11-09T22:54:25.293316+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 11 | XDG/USD | 0.0700665 | 65.597 | 67.087 | +1.73% | +0.10% | 0.80x | 0.0 | 2026-11-09T22:54:25.293316+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 12 | XBT/USD | 75185.3 | 63.139 | 59.141 | +0.59% | +0.14% | 1.33x | 0.0 | 2026-11-09T22:54:25.293316+00:00 | NOT CALIBRATED / HIGH | WATCH |

**Confidence:** uncalibrated research heuristics, NOT validated probabilities. **BUY:** none authorized. Numerical baseline/challenger scores are uncalibrated paper-only ranking values, not probabilities or validated improvement.

## Learning and coverage

| Forward horizon | Evidence status | Verified matured / hits |
|---|---|---|
| 1h | PER HORIZON NOT INDEPENDENTLY VERIFIED | NOT VERIFIED |
| 6h | PER HORIZON NOT INDEPENDENTLY VERIFIED | NOT VERIFIED |
| 24h | PER HORIZON NOT INDEPENDENTLY VERIFIED | NOT VERIFIED |
| 48h | PER HORIZON NOT INDEPENDENTLY VERIFIED | NOT VERIFIED |

- Persisted scans: 215; predictions: 1983; observations: 129973.
- Matured sampled outcomes across 1/6/24/48h: 1105; gap abstentions: 5253. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 0 (sampled only; not a success-rate estimate).
- False positives / missed movers: NOT VERIFIED without eligible continuous outcome coverage.
- Baseline vs challenger: recorded as-of; unbiased held-out lift NOT MEASURED.
- Online Kraken /USD stablecoin-base pairs excluded: 18 (counted from this scan's online AssetPairs metadata, not inferred from price).
- Stablecoin base exclusions: BRL1, BUSD, DAI, EUR, EURC, EUROP, EURQ, EURR, EURT, FDUSD, FRAX, GUSD, PYUSD, QCAD, RLUSD, TGBP, TUSD, USD, USD1, USDC, USDD, USDE, USDG, USDQ, USDR, USDS, USDT, ZUSD.
- DEX: NOT USED; no DEX freshness gate.
- OHLC screening abstentions: 7; details in immutable scan JSON artifact.
- Storage: checksum-sealed ledger pushed non-force and read back before this report. Independent artifact recovery is NOT VERIFIED by this scan alone.
- Errors: none in successful committed scan; a failed workflow must not publish a SUCCESS report.
