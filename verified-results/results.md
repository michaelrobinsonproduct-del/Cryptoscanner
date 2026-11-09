# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-09T23:23:26.507885+00:00
**GitHub trigger:** authenticated issue heartbeat (verified event=issue_comment; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/42719841820
**Source SHA:** 47efb405551d493df87bca8b2583b5611396f1fa
**Ledger commit:** 92b7f84a23a75e87fdd6878361df4ad2fe6148c5
**Ledger generation:** 216 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 7s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 624; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 606; valid market observations: 602; OHLC screened: 24.

## Top WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | Confidence / risk | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---|---|---|
| 1 | AVAX/USD | 8.658 | 103.687 | 97.689 | +9.19% | +0.48% | 1.36x | 4.6 | 2026-11-09T23:23:19.640360+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 2 | PEPE/USD | 5.141e-06 | 99.430 | 80.504 | +3.92% | +0.79% | 3.75x | 3.9 | 2026-11-09T23:23:19.640360+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 3 | ONDO/USD | 0.3721 | 94.569 | 90.609 | +5.84% | -0.26% | 1.53x | 6.2 | 2026-11-09T23:23:19.640360+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 4 | AAVE/USD | 131.97 | 90.316 | 77.017 | +4.78% | -0.34% | 4.42x | 4.6 | 2026-11-09T23:23:19.640360+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 5 | XBT/USD | 75140.1 | 74.348 | 58.718 | +0.53% | +0.13% | 2.65x | 0.0 | 2026-11-09T23:23:19.640360+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 6 | TAO/USD | 222.8315 | 71.065 | 71.439 | +2.80% | +0.04% | 0.94x | 6.3 | 2026-11-09T23:23:19.640360+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 7 | VVV/USD | 21.662 | 70.123 | 77.720 | +7.99% | -0.29% | 0.38x | 8.8 | 2026-11-09T23:23:19.640360+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 8 | SUI/USD | 0.8418 | 69.709 | 72.666 | +2.61% | +0.01% | 0.70x | 1.2 | 2026-11-09T23:23:19.640360+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 9 | XDG/USD | 0.0698506 | 68.702 | 63.671 | +1.41% | +0.15% | 1.43x | 0.5 | 2026-11-09T23:23:19.640360+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 10 | HYPE/USD | 75.2 | 68.119 | 61.197 | +0.98% | +0.08% | 1.65x | 1.3 | 2026-11-09T23:23:19.640360+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 11 | UNI/USD | 6.9988 | 66.695 | 74.460 | +3.17% | -0.05% | 0.25x | 5.4 | 2026-11-09T23:23:19.640360+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 12 | LTC/USD | 51.3 | 60.608 | 61.227 | +2.46% | +0.02% | 0.93x | 1.9 | 2026-11-09T23:23:19.640360+00:00 | NOT CALIBRATED / HIGH | WATCH |

**Confidence:** uncalibrated research heuristics, NOT validated probabilities. **BUY:** none authorized. Numerical baseline/challenger scores are uncalibrated paper-only ranking values, not probabilities or validated improvement.

## Learning and coverage

| Forward horizon | Evidence status | Verified matured / hits |
|---|---|---|
| 1h | PER HORIZON NOT INDEPENDENTLY VERIFIED | NOT VERIFIED |
| 6h | PER HORIZON NOT INDEPENDENTLY VERIFIED | NOT VERIFIED |
| 24h | PER HORIZON NOT INDEPENDENTLY VERIFIED | NOT VERIFIED |
| 48h | PER HORIZON NOT INDEPENDENTLY VERIFIED | NOT VERIFIED |

- Persisted scans: 216; predictions: 1995; observations: 130575.
- Matured sampled outcomes across 1/6/24/48h: 1105; gap abstentions: 5276. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 0 (sampled only; not a success-rate estimate).
- False positives / missed movers: NOT VERIFIED without eligible continuous outcome coverage.
- Baseline vs challenger: recorded as-of; unbiased held-out lift NOT MEASURED.
- Online Kraken /USD stablecoin-base pairs excluded: 18 (counted from this scan's online AssetPairs metadata, not inferred from price).
- Stablecoin base exclusions: BRL1, BUSD, DAI, EUR, EURC, EUROP, EURQ, EURR, EURT, FDUSD, FRAX, GUSD, PYUSD, QCAD, RLUSD, TGBP, TUSD, USD, USD1, USDC, USDD, USDE, USDG, USDQ, USDR, USDS, USDT, ZUSD.
- DEX: NOT USED; no DEX freshness gate.
- OHLC screening abstentions: 7; details in immutable scan JSON artifact.
- Storage: checksum-sealed ledger pushed non-force and read back before this report. Independent artifact recovery is NOT VERIFIED by this scan alone.
- Errors: none in successful committed scan; a failed workflow must not publish a SUCCESS report.
