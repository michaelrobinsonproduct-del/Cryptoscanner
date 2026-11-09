# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-09T18:43:37.869844+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/42676331420
**Source SHA:** 69b32fce88f9296ad7d9292e14e64b61178763c7
**Ledger commit:** d33273da2b952ba2ce6bffc0d3145cc4183aa8e8
**Ledger generation:** 205 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 6s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 624; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 606; valid market observations: 606; OHLC screened: 24.

## Top WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | Confidence / risk | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---|---|---|
| 1 | ONDO/USD | 0.37802 | 111.593 | 95.369 | +7.52% | +1.24% | 2.00x | 9.3 | 2026-11-09T18:43:31.707706+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 2 | RENDER/USD | 1.62 | 93.641 | 73.645 | +6.23% | +1.00% | 8.59x | 12.4 | 2026-11-09T18:43:31.707706+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 3 | AVAX/USD | 8.592 | 89.416 | 96.508 | +8.36% | +0.23% | 0.17x | 7.0 | 2026-11-09T18:43:31.707706+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 4 | SUI/USD | 0.8498 | 85.945 | 78.908 | +3.58% | +0.89% | 1.26x | 2.4 | 2026-11-09T18:43:31.707706+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 5 | TAO/USD | 224.9229 | 83.459 | 77.490 | +3.77% | +0.82% | 1.19x | 7.7 | 2026-11-09T18:43:31.707706+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 6 | AAVE/USD | 133.43 | 82.745 | 89.428 | +5.94% | +0.40% | 0.13x | 6.0 | 2026-11-09T18:43:31.707706+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 7 | PEPE/USD | 5.151e-06 | 82.213 | 82.895 | +4.12% | +0.02% | 0.92x | 1.9 | 2026-11-09T18:43:31.707706+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 8 | ENA/USD | 0.1549 | 79.194 | 78.704 | +4.31% | +1.44% | 0.33x | 12.9 | 2026-11-09T18:43:31.707706+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 9 | PAXG/USD | 4087.68 | 76.928 | 61.842 | +1.01% | +0.02% | 452.77x | 0.4 | 2026-11-09T18:43:31.707706+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 10 | ARB/USD | 0.1769 | 76.305 | 82.354 | +6.63% | -0.28% | 0.54x | 11.3 | 2026-11-09T18:43:31.707706+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 11 | UNI/USD | 7.035 | 73.492 | 77.640 | +3.70% | +0.86% | 0.15x | 6.5 | 2026-11-09T18:43:31.707706+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 12 | XDG/USD | 0.0699276 | 73.461 | 65.296 | +1.53% | +0.55% | 1.54x | 0.8 | 2026-11-09T18:43:31.707706+00:00 | NOT CALIBRATED / HIGH | WATCH |

**Confidence:** uncalibrated research heuristics, NOT validated probabilities. **BUY:** none authorized. Numerical baseline/challenger scores are uncalibrated paper-only ranking values, not probabilities or validated improvement.

## Learning and coverage

| Forward horizon | Evidence status | Verified matured / hits |
|---|---|---|
| 1h | PER HORIZON NOT INDEPENDENTLY VERIFIED | NOT VERIFIED |
| 6h | PER HORIZON NOT INDEPENDENTLY VERIFIED | NOT VERIFIED |
| 24h | PER HORIZON NOT INDEPENDENTLY VERIFIED | NOT VERIFIED |
| 48h | PER HORIZON NOT INDEPENDENTLY VERIFIED | NOT VERIFIED |

- Persisted scans: 205; predictions: 1863; observations: 123937.
- Matured sampled outcomes across 1/6/24/48h: 1081; gap abstentions: 5012. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 0 (sampled only; not a success-rate estimate).
- False positives / missed movers: NOT VERIFIED without eligible continuous outcome coverage.
- Baseline vs challenger: recorded as-of; unbiased held-out lift NOT MEASURED.
- Online Kraken /USD stablecoin-base pairs excluded: 18 (counted from this scan's online AssetPairs metadata, not inferred from price).
- Stablecoin base exclusions: BRL1, BUSD, DAI, EUR, EURC, EUROP, EURQ, EURR, EURT, FDUSD, FRAX, GUSD, PYUSD, QCAD, RLUSD, TGBP, TUSD, USD, USD1, USDC, USDD, USDE, USDG, USDQ, USDR, USDS, USDT, ZUSD.
- DEX: NOT USED; no DEX freshness gate.
- OHLC screening abstentions: 5; details in immutable scan JSON artifact.
- Storage: checksum-sealed ledger pushed non-force and read back before this report. Independent artifact recovery is NOT VERIFIED by this scan alone.
- Errors: none in successful committed scan; a failed workflow must not publish a SUCCESS report.
