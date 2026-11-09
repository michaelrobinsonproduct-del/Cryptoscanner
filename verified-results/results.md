# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-09T05:44:50.453136+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/42568979343
**Source SHA:** bba6177fd9f7dcbc32e4a40002747091c0abb5e2
**Ledger commit:** 90d0eb4389c6a40d264f9b8a822e5bdfa8a408b5
**Ledger generation:** 183 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 8s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 624; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 606; valid market observations: 606; OHLC screened: 24.

## Top WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | Confidence / risk | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---|---|---|
| 1 | ZEC/USD | 1227.54 | 77.281 | 61.984 | +1.25% | +0.06% | 2.57x | 3.5 | 2026-11-09T05:44:42.508515+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 2 | ENA/USD | 0.151 | 75.828 | 63.467 | +1.68% | -0.53% | 2.66x | 6.6 | 2026-11-09T05:44:42.508515+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 3 | PEPE/USD | 5.055e-06 | 75.025 | 68.303 | +2.18% | +0.02% | 1.66x | 4.0 | 2026-11-09T05:44:42.508515+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 4 | SOL/USD | 86.69 | 64.178 | 56.367 | +0.28% | -0.31% | 1.94x | 1.2 | 2026-11-09T05:44:42.508515+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 5 | PAXG/USD | 4106.34 | 56.172 | 45.239 | +1.47% | -0.03% | 2.11x | 1.0 | 2026-11-09T05:44:42.508515+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 6 | SUI/USD | 0.8249 | 55.227 | 58.234 | +0.55% | -0.01% | 0.71x | 1.2 | 2026-11-09T05:44:42.508515+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 7 | HBAR/USD | 0.06628 | 55.223 | 45.034 | +1.05% | -0.09% | 2.06x | 3.0 | 2026-11-09T05:44:42.508515+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 8 | ARB/USD | 0.1734 | 53.255 | 62.974 | +4.52% | -0.40% | 0.23x | 11.5 | 2026-11-09T05:44:42.508515+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 9 | XDG/USD | 0.0691563 | 51.439 | 57.836 | +0.41% | -0.33% | 0.53x | 0.0 | 2026-11-09T05:44:42.508515+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 10 | RSR/USD | 0.001743 | 48.766 | 57.651 | +5.38% | -0.52% | 0.37x | 23.0 | 2026-11-09T05:44:42.508515+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 11 | LINK/USD | 10.46523 | 47.709 | 52.524 | +0.61% | -0.33% | 0.68x | 5.5 | 2026-11-09T05:44:42.508515+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 12 | AUD/USD | 0.68904 | 34.761 | 40.703 | +0.33% | +0.03% | 0.39x | 1.9 | 2026-11-09T05:44:42.508515+00:00 | NOT CALIBRATED / HIGH | WATCH |

**Confidence:** uncalibrated research heuristics, NOT validated probabilities. **BUY:** none authorized. Numerical baseline/challenger scores are uncalibrated paper-only ranking values, not probabilities or validated improvement.

## Learning and coverage

| Forward horizon | Evidence status | Verified matured / hits |
|---|---|---|
| 1h | PER HORIZON NOT INDEPENDENTLY VERIFIED | NOT VERIFIED |
| 6h | PER HORIZON NOT INDEPENDENTLY VERIFIED | NOT VERIFIED |
| 24h | PER HORIZON NOT INDEPENDENTLY VERIFIED | NOT VERIFIED |
| 48h | PER HORIZON NOT INDEPENDENTLY VERIFIED | NOT VERIFIED |

- Persisted scans: 183; predictions: 1604; observations: 110606.
- Matured sampled outcomes across 1/6/24/48h: 903; gap abstentions: 4478. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 0 (sampled only; not a success-rate estimate).
- False positives / missed movers: NOT VERIFIED without eligible continuous outcome coverage.
- Baseline vs challenger: recorded as-of; unbiased held-out lift NOT MEASURED.
- Online Kraken /USD stablecoin-base pairs excluded: 18 (counted from this scan's online AssetPairs metadata, not inferred from price).
- Stablecoin base exclusions: BRL1, BUSD, DAI, EUR, EURC, EUROP, EURQ, EURR, EURT, FDUSD, FRAX, GUSD, PYUSD, QCAD, RLUSD, TGBP, TUSD, USD, USD1, USDC, USDD, USDE, USDG, USDQ, USDR, USDS, USDT, ZUSD.
- DEX: NOT USED; no DEX freshness gate.
- OHLC screening abstentions: 11; details in immutable scan JSON artifact.
- Storage: checksum-sealed ledger pushed non-force and read back before this report. Independent artifact recovery is NOT VERIFIED by this scan alone.
- Errors: none in successful committed scan; a failed workflow must not publish a SUCCESS report.
