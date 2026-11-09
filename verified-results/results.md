# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-09T20:26:20.344508+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/42692775534
**Source SHA:** 69b32fce88f9296ad7d9292e14e64b61178763c7
**Ledger commit:** 32e0f4055f87811976267e1730f53f576e364bdf
**Ledger generation:** 208 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 8s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 624; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 606; valid market observations: 606; OHLC screened: 24.

## Top WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | Confidence / risk | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---|---|---|
| 1 | AVAX/USD | 8.709 | 120.654 | 96.556 | +9.84% | +1.82% | 2.51x | 6.9 | 2026-11-09T20:26:11.959450+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 2 | VVV/USD | 21.76 | 96.929 | 78.342 | +8.47% | +0.72% | 2.62x | 6.9 | 2026-11-09T20:26:11.959450+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 3 | AAVE/USD | 132.57 | 92.429 | 83.424 | +5.26% | +0.03% | 1.89x | 7.5 | 2026-11-09T20:26:11.959450+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 4 | TAO/USD | 223.8623 | 90.511 | 75.910 | +3.28% | -0.08% | 3.54x | 4.0 | 2026-11-09T20:26:11.959450+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 5 | ONDO/USD | 0.37589 | 90.198 | 94.419 | +6.91% | +0.30% | 0.43x | 11.2 | 2026-11-09T20:26:11.959450+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 6 | ENA/USD | 0.1559 | 82.388 | 86.673 | +4.98% | +0.26% | 0.44x | 6.4 | 2026-11-09T20:26:11.959450+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 7 | UNI/USD | 7.0457 | 78.048 | 79.530 | +3.86% | +0.68% | 0.51x | 5.0 | 2026-11-09T20:26:11.959450+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 8 | PEPE/USD | 5.141e-06 | 76.409 | 80.507 | +3.92% | +0.72% | 0.23x | 3.9 | 2026-11-09T20:26:11.959450+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 9 | SUI/USD | 0.8514 | 75.833 | 80.276 | +3.78% | +0.35% | 0.38x | 2.3 | 2026-11-09T20:26:11.959450+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 10 | ARB/USD | 0.1759 | 73.348 | 80.024 | +6.03% | +0.06% | 0.30x | 11.4 | 2026-11-09T20:26:11.959450+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 11 | PAXG/USD | 4126.34 | 67.745 | 68.422 | +1.96% | +0.13% | 0.87x | 0.6 | 2026-11-09T20:26:11.959450+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 12 | GBP/USD | 1.34351 | 65.893 | 58.928 | +0.59% | -0.01% | 1.70x | 0.4 | 2026-11-09T20:26:11.959450+00:00 | NOT CALIBRATED / HIGH | WATCH |

**Confidence:** uncalibrated research heuristics, NOT validated probabilities. **BUY:** none authorized. Numerical baseline/challenger scores are uncalibrated paper-only ranking values, not probabilities or validated improvement.

## Learning and coverage

| Forward horizon | Evidence status | Verified matured / hits |
|---|---|---|
| 1h | PER HORIZON NOT INDEPENDENTLY VERIFIED | NOT VERIFIED |
| 6h | PER HORIZON NOT INDEPENDENTLY VERIFIED | NOT VERIFIED |
| 24h | PER HORIZON NOT INDEPENDENTLY VERIFIED | NOT VERIFIED |
| 48h | PER HORIZON NOT INDEPENDENTLY VERIFIED | NOT VERIFIED |

- Persisted scans: 208; predictions: 1899; observations: 125755.
- Matured sampled outcomes across 1/6/24/48h: 1081; gap abstentions: 5111. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 0 (sampled only; not a success-rate estimate).
- False positives / missed movers: NOT VERIFIED without eligible continuous outcome coverage.
- Baseline vs challenger: recorded as-of; unbiased held-out lift NOT MEASURED.
- Online Kraken /USD stablecoin-base pairs excluded: 18 (counted from this scan's online AssetPairs metadata, not inferred from price).
- Stablecoin base exclusions: BRL1, BUSD, DAI, EUR, EURC, EUROP, EURQ, EURR, EURT, FDUSD, FRAX, GUSD, PYUSD, QCAD, RLUSD, TGBP, TUSD, USD, USD1, USDC, USDD, USDE, USDG, USDQ, USDR, USDS, USDT, ZUSD.
- DEX: NOT USED; no DEX freshness gate.
- OHLC screening abstentions: 7; details in immutable scan JSON artifact.
- Storage: checksum-sealed ledger pushed non-force and read back before this report. Independent artifact recovery is NOT VERIFIED by this scan alone.
- Errors: none in successful committed scan; a failed workflow must not publish a SUCCESS report.
