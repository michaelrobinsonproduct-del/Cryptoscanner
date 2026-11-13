# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-13T09:36:09.587820+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/43402630328
**Source SHA:** af3b2f47bee5eef0f7fdea2d2d8c22c286a92662
**Previous ledger commit:** 6b1f5c4ae906af8716f614aaa910266ce25ff36c (atomic ledger/results publication)
**Ledger generation:** 356 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 6s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 624; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 606; valid market observations: 606; OHLC screened: 18.

## Top WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | Confidence / risk | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---|---|---|
| 1 | NEAR/USD | 3.5038 | 65.713 | 71.317 | +2.45% | -0.31% | 0.59x | 1.7 | 2026-11-13T09:36:03.590696+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 2 | ICNT/USD | 0.2876 | 64.995 | 56.174 | +4.32% | +0.88% | 1.44x | 10.4 | 2026-11-13T09:36:03.590696+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 3 | TON/USD | 1.146 | 63.183 | 46.432 | +0.53% | +0.35% | 2.85x | 8.7 | 2026-11-13T09:36:03.590696+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 4 | INJ/USD | 7.64 | 53.992 | 58.705 | +2.41% | -0.21% | 0.63x | 7.9 | 2026-11-13T09:36:03.590696+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 5 | ICP/USD | 2.613 | 48.975 | 42.515 | +1.52% | +0.19% | 1.55x | 7.6 | 2026-11-13T09:36:03.590696+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 6 | ZRO/USD | 1.564 | 45.994 | 38.020 | +0.71% | -0.64% | 2.12x | 12.8 | 2026-11-13T09:36:03.590696+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 7 | PONS/USD | 0.1551 | 45.501 | 42.309 | +2.58% | -0.32% | 1.48x | 12.9 | 2026-11-13T09:36:03.590696+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 8 | KAS/USD | 0.0293 | 45.475 | 40.605 | +1.77% | +0.48% | 1.25x | 13.7 | 2026-11-13T09:36:03.590696+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 9 | USELESS/USD | 0.13464 | 34.758 | 42.065 | +2.00% | +0.26% | 0.14x | 23.1 | 2026-11-13T09:36:03.590696+00:00 | NOT CALIBRATED / HIGH | WATCH |

**Confidence:** uncalibrated research heuristics, NOT validated probabilities. **BUY:** none authorized. Numerical baseline/challenger scores are uncalibrated paper-only ranking values, not probabilities or validated improvement.

## Learning and coverage

| Forward horizon | Evidence status | Verified matured / hits |
|---|---|---|
| 1h | PER HORIZON NOT INDEPENDENTLY VERIFIED | NOT VERIFIED |
| 6h | PER HORIZON NOT INDEPENDENTLY VERIFIED | NOT VERIFIED |
| 24h | PER HORIZON NOT INDEPENDENTLY VERIFIED | NOT VERIFIED |
| 48h | PER HORIZON NOT INDEPENDENTLY VERIFIED | NOT VERIFIED |

- Persisted scans: 356; predictions: 3280; observations: 214052.
- Matured sampled outcomes across 1/6/24/48h: 2926; gap abstentions: 9126. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 0 (sampled only; not a success-rate estimate).
- False positives / missed movers: NOT VERIFIED without eligible continuous outcome coverage.
- Baseline vs challenger: recorded as-of; unbiased held-out lift NOT MEASURED.
- Online Kraken /USD stablecoin-base pairs excluded: 18 (counted from this scan's online AssetPairs metadata, not inferred from price).
- Stablecoin base exclusions: BRL1, BUSD, DAI, EUR, EURC, EUROP, EURQ, EURR, EURT, FDUSD, FRAX, GUSD, PYUSD, QCAD, RLUSD, TGBP, TUSD, USD, USD1, USDC, USDD, USDE, USDG, USDQ, USDR, USDS, USDT, ZUSD.
- DEX: NOT USED; no DEX freshness gate.
- OHLC screening abstentions: 9; details in immutable scan JSON artifact.
- Storage: ledger and results published in one non-force Git commit and read back. Independent artifact recovery is NOT VERIFIED by this scan alone.
- Errors: none in successful committed scan; a failed workflow must not publish a SUCCESS report.
