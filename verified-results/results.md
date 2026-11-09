# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-09T06:50:15.090336+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/42575405798
**Source SHA:** bba6177fd9f7dcbc32e4a40002747091c0abb5e2
**Ledger commit:** f78e0ce28434ff83b7bb0b330d423f155dd9a1b8
**Ledger generation:** 185 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 7s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 624; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 606; valid market observations: 606; OHLC screened: 24.

## Top WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | Confidence / risk | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---|---|---|
| 1 | ENA/USD | 0.1499 | 74.933 | 58.259 | +0.94% | +0.33% | 4.85x | 6.7 | 2026-11-09T06:50:08.277334+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 2 | WLD/USD | 0.3177 | 65.674 | 50.070 | +1.89% | +0.16% | 2.48x | 3.1 | 2026-11-09T06:50:08.277334+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 3 | PEPE/USD | 5.064e-06 | 64.082 | 68.590 | +2.37% | +0.32% | 0.39x | 5.9 | 2026-11-09T06:50:08.277334+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 4 | PUMP/USD | 0.003548 | 63.898 | 46.490 | +1.05% | +0.48% | 6.75x | 8.5 | 2026-11-09T06:50:08.277334+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 5 | PIEVERSE/USD | 1.596 | 57.344 | 63.502 | +11.03% | -0.09% | 0.43x | 25.1 | 2026-11-09T06:50:08.277334+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 6 | LTC/USD | 50.25 | 54.523 | 46.208 | +0.36% | -0.12% | 1.89x | 4.0 | 2026-11-09T06:50:08.277334+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 7 | HBAR/USD | 0.06583 | 54.258 | 40.199 | +0.37% | -0.15% | 2.48x | 3.0 | 2026-11-09T06:50:08.277334+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 8 | XAUT/USD | 4093.9 | 54.069 | 39.166 | +1.09% | -0.02% | 16.01x | 0.2 | 2026-11-09T06:50:08.277334+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 9 | ZEC/USD | 1216.04 | 52.631 | 54.467 | +0.30% | -0.35% | 0.99x | 5.3 | 2026-11-09T06:50:08.277334+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 10 | QNT/USD | 199.12 | 52.070 | 55.537 | +2.19% | +0.73% | 0.29x | 7.0 | 2026-11-09T06:50:08.277334+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 11 | LIGHTER/USD | 3.071 | 50.708 | 34.239 | +0.43% | +0.29% | 12.12x | 6.5 | 2026-11-09T06:50:08.277334+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 12 | AUD/USD | 0.6893 | 43.388 | 40.979 | +0.37% | +0.03% | 1.23x | 2.0 | 2026-11-09T06:50:08.277334+00:00 | NOT CALIBRATED / HIGH | WATCH |

**Confidence:** uncalibrated research heuristics, NOT validated probabilities. **BUY:** none authorized. Numerical baseline/challenger scores are uncalibrated paper-only ranking values, not probabilities or validated improvement.

## Learning and coverage

| Forward horizon | Evidence status | Verified matured / hits |
|---|---|---|
| 1h | PER HORIZON NOT INDEPENDENTLY VERIFIED | NOT VERIFIED |
| 6h | PER HORIZON NOT INDEPENDENTLY VERIFIED | NOT VERIFIED |
| 24h | PER HORIZON NOT INDEPENDENTLY VERIFIED | NOT VERIFIED |
| 48h | PER HORIZON NOT INDEPENDENTLY VERIFIED | NOT VERIFIED |

- Persisted scans: 185; predictions: 1628; observations: 111818.
- Matured sampled outcomes across 1/6/24/48h: 927; gap abstentions: 4486. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 0 (sampled only; not a success-rate estimate).
- False positives / missed movers: NOT VERIFIED without eligible continuous outcome coverage.
- Baseline vs challenger: recorded as-of; unbiased held-out lift NOT MEASURED.
- Online Kraken /USD stablecoin-base pairs excluded: 18 (counted from this scan's online AssetPairs metadata, not inferred from price).
- Stablecoin base exclusions: BRL1, BUSD, DAI, EUR, EURC, EUROP, EURQ, EURR, EURT, FDUSD, FRAX, GUSD, PYUSD, QCAD, RLUSD, TGBP, TUSD, USD, USD1, USDC, USDD, USDE, USDG, USDQ, USDR, USDS, USDT, ZUSD.
- DEX: NOT USED; no DEX freshness gate.
- OHLC screening abstentions: 10; details in immutable scan JSON artifact.
- Storage: checksum-sealed ledger pushed non-force and read back before this report. Independent artifact recovery is NOT VERIFIED by this scan alone.
- Errors: none in successful committed scan; a failed workflow must not publish a SUCCESS report.
