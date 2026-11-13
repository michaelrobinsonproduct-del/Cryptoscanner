# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-13T18:30:53.260799+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/43483232621
**Source SHA:** 1de7f34577ba42db35171277708cbe2c8de3e8f1
**Previous ledger commit:** ed73ba6c26ac89920cf56ae1515ac8dfb2a47de4 (atomic ledger/results publication)
**Ledger generation:** 364 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 8s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 625; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 607; valid market observations: 607; OHLC screened: 23.

## Top WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | Confidence / risk | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---|---|---|
| 1 | INJ/USD | 8.085 | 96.943 | 96.906 | +8.38% | +0.05% | 0.98x | 6.2 | 2026-11-13T18:30:45.219553+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 2 | UAI/USD | 0.04028 | 71.737 | 65.941 | +11.67% | -1.84% | 8.99x | 22.4 | 2026-11-13T18:30:45.219553+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 3 | NIGHT/USD | 0.04627 | 67.272 | 53.596 | +0.83% | +0.87% | 1.93x | 8.7 | 2026-11-13T18:30:45.219553+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 4 | VVV/USD | 19.192 | 62.800 | 45.580 | +1.05% | +1.00% | 2.22x | 5.2 | 2026-11-13T18:30:45.219553+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 5 | NEAR/USD | 3.4881 | 62.477 | 68.529 | +1.99% | +0.09% | 0.35x | 0.9 | 2026-11-13T18:30:45.219553+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 6 | Q/USD | 0.030436 | 61.376 | 59.799 | +5.70% | +0.02% | 1.15x | 27.3 | 2026-11-13T18:30:45.219553+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 7 | AVAX/USD | 8.409 | 60.246 | 59.436 | +0.72% | +0.29% | 0.94x | 1.2 | 2026-11-13T18:30:45.219553+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 8 | ZBCN/USD | 0.00188 | 53.572 | 58.246 | +10.07% | +0.80% | 0.13x | 37.3 | 2026-11-13T18:30:45.219553+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 9 | TAO/USD | 214.1885 | 52.719 | 58.403 | +1.07% | +0.30% | 0.28x | 8.2 | 2026-11-13T18:30:45.219553+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 10 | CAP/USD | 0.108551 | 50.016 | 51.323 | +4.81% | -0.10% | 0.92x | 40.1 | 2026-11-13T18:30:45.219553+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 11 | XLM/USD | 0.148751 | 46.303 | 53.886 | +0.30% | +0.02% | 0.23x | 1.1 | 2026-11-13T18:30:45.219553+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 12 | STX/USD | 0.289 | 45.388 | 40.202 | +1.44% | -0.14% | 1.59x | 6.9 | 2026-11-13T18:30:45.219553+00:00 | NOT CALIBRATED / HIGH | WATCH |

**Confidence:** uncalibrated research heuristics, NOT validated probabilities. **BUY:** none authorized. Numerical baseline/challenger scores are uncalibrated paper-only ranking values, not probabilities or validated improvement.

## Learning and coverage

| Forward horizon | Evidence status | Verified matured / hits |
|---|---|---|
| 1h | PER HORIZON NOT INDEPENDENTLY VERIFIED | NOT VERIFIED |
| 6h | PER HORIZON NOT INDEPENDENTLY VERIFIED | NOT VERIFIED |
| 24h | PER HORIZON NOT INDEPENDENTLY VERIFIED | NOT VERIFIED |
| 48h | PER HORIZON NOT INDEPENDENTLY VERIFIED | NOT VERIFIED |

- Persisted scans: 364; predictions: 3370; observations: 218904.
- Matured sampled outcomes across 1/6/24/48h: 2938; gap abstentions: 9608. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 0 (sampled only; not a success-rate estimate).
- False positives / missed movers: NOT VERIFIED without eligible continuous outcome coverage.
- Baseline vs challenger: recorded as-of; unbiased held-out lift NOT MEASURED.
- Online Kraken /USD stablecoin-base pairs excluded: 18 (counted from this scan's online AssetPairs metadata, not inferred from price).
- Stablecoin base exclusions: BRL1, BUSD, DAI, EUR, EURC, EUROP, EURQ, EURR, EURT, FDUSD, FRAX, GUSD, PYUSD, QCAD, RLUSD, TGBP, TUSD, USD, USD1, USDC, USDD, USDE, USDG, USDQ, USDR, USDS, USDT, ZUSD.
- DEX: NOT USED; no DEX freshness gate.
- OHLC screening abstentions: 10; details in immutable scan JSON artifact.
- Storage: ledger and results published in one non-force Git commit and read back. Independent artifact recovery is NOT VERIFIED by this scan alone.
- Errors: none in successful committed scan; a failed workflow must not publish a SUCCESS report.
