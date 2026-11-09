# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-09T12:45:52.194390+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/42619545244
**Source SHA:** bba6177fd9f7dcbc32e4a40002747091c0abb5e2
**Ledger commit:** b7df94543c72a4ad59f778c5e7c6f950f066f7c1
**Ledger generation:** 195 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 9s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 624; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 606; valid market observations: 605; OHLC screened: 24.

## Top WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | Confidence / risk | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---|---|---|
| 1 | AVAX/USD | 8.362 | 112.258 | 81.890 | +5.46% | +3.07% | 10.93x | 6.0 | 2026-11-09T12:45:43.021609+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 2 | AAVE/USD | 133.35 | 102.617 | 86.189 | +5.88% | +0.29% | 10.32x | 7.5 | 2026-11-09T12:45:43.021609+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 3 | ENA/USD | 0.1533 | 92.978 | 74.365 | +3.23% | +0.72% | 4.45x | 6.5 | 2026-11-09T12:45:43.021609+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 4 | SUI/USD | 0.8391 | 87.214 | 70.359 | +2.28% | +0.37% | 3.16x | 1.2 | 2026-11-09T12:45:43.021609+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 5 | USELESS/USD | 0.13628 | 85.495 | 70.934 | +10.68% | -0.09% | 3.33x | 26.5 | 2026-11-09T12:45:43.021609+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 6 | CHIP/USD | 0.03504 | 81.290 | 68.859 | +6.41% | +0.81% | 1.84x | 14.3 | 2026-11-09T12:45:43.021609+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 7 | PUMP/USD | 0.00368 | 73.672 | 77.379 | +4.81% | -0.41% | 0.83x | 5.4 | 2026-11-09T12:45:43.021609+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 8 | LINK/USD | 10.6252 | 73.015 | 68.557 | +2.15% | -0.14% | 1.52x | 3.0 | 2026-11-09T12:45:43.021609+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 9 | GBP/USD | 1.34141 | 72.916 | 57.827 | +0.44% | +0.02% | 3.11x | 0.4 | 2026-11-09T12:45:43.021609+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 10 | LTC/USD | 51.26 | 70.754 | 63.651 | +2.38% | +0.31% | 1.55x | 2.0 | 2026-11-09T12:45:43.021609+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 11 | RENDER/USD | 1.614 | 70.713 | 73.390 | +5.84% | +0.25% | 0.61x | 6.2 | 2026-11-09T12:45:43.021609+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 12 | PEPE/USD | 5.089e-06 | 70.408 | 72.146 | +2.87% | -0.06% | 0.86x | 5.9 | 2026-11-09T12:45:43.021609+00:00 | NOT CALIBRATED / HIGH | WATCH |

**Confidence:** uncalibrated research heuristics, NOT validated probabilities. **BUY:** none authorized. Numerical baseline/challenger scores are uncalibrated paper-only ranking values, not probabilities or validated improvement.

## Learning and coverage

| Forward horizon | Evidence status | Verified matured / hits |
|---|---|---|
| 1h | PER HORIZON NOT INDEPENDENTLY VERIFIED | NOT VERIFIED |
| 6h | PER HORIZON NOT INDEPENDENTLY VERIFIED | NOT VERIFIED |
| 24h | PER HORIZON NOT INDEPENDENTLY VERIFIED | NOT VERIFIED |
| 48h | PER HORIZON NOT INDEPENDENTLY VERIFIED | NOT VERIFIED |

- Persisted scans: 195; predictions: 1743; observations: 117877.
- Matured sampled outcomes across 1/6/24/48h: 973; gap abstentions: 4764. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 0 (sampled only; not a success-rate estimate).
- False positives / missed movers: NOT VERIFIED without eligible continuous outcome coverage.
- Baseline vs challenger: recorded as-of; unbiased held-out lift NOT MEASURED.
- Online Kraken /USD stablecoin-base pairs excluded: 18 (counted from this scan's online AssetPairs metadata, not inferred from price).
- Stablecoin base exclusions: BRL1, BUSD, DAI, EUR, EURC, EUROP, EURQ, EURR, EURT, FDUSD, FRAX, GUSD, PYUSD, QCAD, RLUSD, TGBP, TUSD, USD, USD1, USDC, USDD, USDE, USDG, USDQ, USDR, USDS, USDT, ZUSD.
- DEX: NOT USED; no DEX freshness gate.
- OHLC screening abstentions: 5; details in immutable scan JSON artifact.
- Storage: checksum-sealed ledger pushed non-force and read back before this report. Independent artifact recovery is NOT VERIFIED by this scan alone.
- Errors: none in successful committed scan; a failed workflow must not publish a SUCCESS report.
