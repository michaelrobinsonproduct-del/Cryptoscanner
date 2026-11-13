# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-13T11:03:54.198592+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/43413938299
**Source SHA:** bf81d0ba655dbff12bc9c9251ee2fcaf50d54acc
**Previous ledger commit:** 95c0661a0c76065e4e07a264edf1852aebf528ef (atomic ledger/results publication)
**Ledger generation:** 357 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 7s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 624; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 606; valid market observations: 606; OHLC screened: 24.

## Top WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | Confidence / risk | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---|---|---|
| 1 | HYPE/USD | 73.05 | 74.835 | 57.975 | +0.52% | +0.37% | 4.52x | 1.4 | 2026-11-13T11:03:47.216023+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 2 | ICNT/USD | 0.285 | 72.485 | 49.495 | +3.37% | +1.60% | 4.86x | 10.5 | 2026-11-13T11:03:47.216023+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 3 | NEAR/USD | 3.5172 | 70.357 | 72.214 | +2.85% | +0.41% | 0.61x | 5.4 | 2026-11-13T11:03:47.216023+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 4 | ZRO/USD | 1.586 | 68.343 | 48.244 | +2.12% | +1.02% | 8.31x | 12.6 | 2026-11-13T11:03:47.216023+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 5 | INJ/USD | 7.676 | 60.488 | 66.702 | +2.90% | +0.66% | 0.05x | 6.5 | 2026-11-13T11:03:47.216023+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 6 | UAI/USD | 0.03897 | 59.650 | 68.826 | +8.04% | -1.71% | 0.94x | 15.4 | 2026-11-13T11:03:47.216023+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 7 | AVAX/USD | 8.422 | 54.764 | 59.338 | +0.87% | +0.08% | 0.50x | 3.6 | 2026-11-13T11:03:47.216023+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 8 | TON/USD | 1.147 | 40.375 | 46.733 | +0.61% | +0.26% | 0.23x | 8.7 | 2026-11-13T11:03:47.216023+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 9 | PONS/USD | 0.1546 | 34.462 | 36.735 | +2.25% | +0.26% | 0.64x | 19.4 | 2026-11-13T11:03:47.216023+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 10 | STX/USD | 0.2898 | 32.132 | 42.499 | +1.72% | -0.34% | 0.14x | 6.9 | 2026-11-13T11:03:47.216023+00:00 | NOT CALIBRATED / HIGH | WATCH |

**Confidence:** uncalibrated research heuristics, NOT validated probabilities. **BUY:** none authorized. Numerical baseline/challenger scores are uncalibrated paper-only ranking values, not probabilities or validated improvement.

## Learning and coverage

| Forward horizon | Evidence status | Verified matured / hits |
|---|---|---|
| 1h | PER HORIZON NOT INDEPENDENTLY VERIFIED | NOT VERIFIED |
| 6h | PER HORIZON NOT INDEPENDENTLY VERIFIED | NOT VERIFIED |
| 24h | PER HORIZON NOT INDEPENDENTLY VERIFIED | NOT VERIFIED |
| 48h | PER HORIZON NOT INDEPENDENTLY VERIFIED | NOT VERIFIED |

- Persisted scans: 357; predictions: 3290; observations: 214658.
- Matured sampled outcomes across 1/6/24/48h: 2926; gap abstentions: 9204. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 0 (sampled only; not a success-rate estimate).
- False positives / missed movers: NOT VERIFIED without eligible continuous outcome coverage.
- Baseline vs challenger: recorded as-of; unbiased held-out lift NOT MEASURED.
- Online Kraken /USD stablecoin-base pairs excluded: 18 (counted from this scan's online AssetPairs metadata, not inferred from price).
- Stablecoin base exclusions: BRL1, BUSD, DAI, EUR, EURC, EUROP, EURQ, EURR, EURT, FDUSD, FRAX, GUSD, PYUSD, QCAD, RLUSD, TGBP, TUSD, USD, USD1, USDC, USDD, USDE, USDG, USDQ, USDR, USDS, USDT, ZUSD.
- DEX: NOT USED; no DEX freshness gate.
- OHLC screening abstentions: 14; details in immutable scan JSON artifact.
- Storage: ledger and results published in one non-force Git commit and read back. Independent artifact recovery is NOT VERIFIED by this scan alone.
- Errors: none in successful committed scan; a failed workflow must not publish a SUCCESS report.
