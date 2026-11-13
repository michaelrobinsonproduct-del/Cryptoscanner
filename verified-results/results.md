# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-13T07:25:33.627834+00:00
**GitHub trigger:** scheduled (verified event=schedule; originating cron=20,50 * * * *, intended UTC minute=20,50; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/43385610853
**Source SHA:** f243866652b61a450371de4732d7a048b93e9c0a
**Previous ledger commit:** d942c5a13e1e03b42f34e62036b32f3e7d2566d0 (atomic ledger/results publication)
**Ledger generation:** 353 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 9s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 624; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 606; valid market observations: 606; OHLC screened: 23.

## Top WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | Confidence / risk | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---|---|---|
| 1 | NEAR/USD | 3.5383 | 96.472 | 78.386 | +3.46% | +0.62% | 8.00x | 1.7 | 2026-11-13T07:25:24.877461+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 2 | ICNT/USD | 0.2913 | 77.848 | 63.877 | +5.66% | -0.21% | 3.91x | 13.7 | 2026-11-13T07:25:24.877461+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 3 | PEPE/USD | 4.611e-06 | 76.236 | 67.062 | +1.88% | +0.63% | 1.60x | 2.2 | 2026-11-13T07:25:24.877461+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 4 | USELESS/USD | 0.13636 | 71.031 | 55.885 | +3.30% | +0.03% | 4.23x | 14.0 | 2026-11-13T07:25:24.877461+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 5 | UAI/USD | 0.03744 | 63.456 | 49.831 | +3.80% | +1.46% | 1.63x | 16.0 | 2026-11-13T07:25:24.877461+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 6 | BAT/USD | 0.12468 | 59.265 | 39.033 | +1.42% | +1.05% | 5.48x | 5.6 | 2026-11-13T07:25:24.877461+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 7 | TON/USD | 1.156 | 57.255 | 53.126 | +1.40% | -0.17% | 1.50x | 8.7 | 2026-11-13T07:25:24.877461+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 8 | ZRO/USD | 1.589 | 46.444 | 48.864 | +2.32% | -1.61% | 1.56x | 12.6 | 2026-11-13T07:25:24.877461+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 9 | JUP/USD | 0.26624 | 40.834 | 32.933 | +0.40% | -0.67% | 2.13x | 9.0 | 2026-11-13T07:25:24.877461+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 10 | KAS/USD | 0.02895 | 40.385 | 33.603 | +0.56% | -0.55% | 1.95x | 10.4 | 2026-11-13T07:25:24.877461+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 11 | ICP/USD | 2.611 | 38.440 | 44.164 | +1.44% | +0.08% | 0.39x | 3.8 | 2026-11-13T07:25:24.877461+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 12 | PYTH/USD | 0.06718 | 35.671 | 27.621 | +0.27% | +0.19% | 1.71x | 13.4 | 2026-11-13T07:25:24.877461+00:00 | NOT CALIBRATED / HIGH | WATCH |

**Confidence:** uncalibrated research heuristics, NOT validated probabilities. **BUY:** none authorized. Numerical baseline/challenger scores are uncalibrated paper-only ranking values, not probabilities or validated improvement.

## Learning and coverage

| Forward horizon | Evidence status | Verified matured / hits |
|---|---|---|
| 1h | PER HORIZON NOT INDEPENDENTLY VERIFIED | NOT VERIFIED |
| 6h | PER HORIZON NOT INDEPENDENTLY VERIFIED | NOT VERIFIED |
| 24h | PER HORIZON NOT INDEPENDENTLY VERIFIED | NOT VERIFIED |
| 48h | PER HORIZON NOT INDEPENDENTLY VERIFIED | NOT VERIFIED |

- Persisted scans: 353; predictions: 3251; observations: 212234.
- Matured sampled outcomes across 1/6/24/48h: 2926; gap abstentions: 9037. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 0 (sampled only; not a success-rate estimate).
- False positives / missed movers: NOT VERIFIED without eligible continuous outcome coverage.
- Baseline vs challenger: recorded as-of; unbiased held-out lift NOT MEASURED.
- Online Kraken /USD stablecoin-base pairs excluded: 18 (counted from this scan's online AssetPairs metadata, not inferred from price).
- Stablecoin base exclusions: BRL1, BUSD, DAI, EUR, EURC, EUROP, EURQ, EURR, EURT, FDUSD, FRAX, GUSD, PYUSD, QCAD, RLUSD, TGBP, TUSD, USD, USD1, USDC, USDD, USDE, USDG, USDQ, USDR, USDS, USDT, ZUSD.
- DEX: NOT USED; no DEX freshness gate.
- OHLC screening abstentions: 10; details in immutable scan JSON artifact.
- Storage: ledger and results published in one non-force Git commit and read back. Independent artifact recovery is NOT VERIFIED by this scan alone.
- Errors: none in successful committed scan; a failed workflow must not publish a SUCCESS report.
