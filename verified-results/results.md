# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-13T16:06:48.011524+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/43459260937
**Source SHA:** e4445ea3884f16a9bdd348d7cfaf75278dcc7858
**Previous ledger commit:** a0fd86f370cd2ea17e7b8a962d86ac5d486643c4 (atomic ledger/results publication)
**Ledger generation:** 362 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 9s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 625; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 607; valid market observations: 606; OHLC screened: 24.

## Top WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | Confidence / risk | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---|---|---|
| 1 | INJ/USD | 8.177 | 103.324 | 96.329 | +9.61% | +1.33% | 1.04x | 7.3 | 2026-11-13T16:06:38.979651+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 2 | ZRO/USD | 1.597 | 78.148 | 57.128 | +2.83% | +1.20% | 2.64x | 6.3 | 2026-11-13T16:06:38.979651+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 3 | UAI/USD | 0.03769 | 74.432 | 51.145 | +4.49% | +1.66% | 3.80x | 24.0 | 2026-11-13T16:06:38.979651+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 4 | NEAR/USD | 3.4996 | 65.808 | 69.313 | +2.33% | +0.13% | 0.59x | 4.0 | 2026-11-13T16:06:38.979651+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 5 | HYPE/USD | 73.16 | 62.675 | 58.353 | +0.67% | +0.47% | 1.20x | 2.7 | 2026-11-13T16:06:38.979651+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 6 | CAP/USD | 0.106615 | 58.910 | 42.425 | +2.94% | +0.30% | 5.43x | 30.1 | 2026-11-13T16:06:38.979651+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 7 | ZBCN/USD | 0.001828 | 52.269 | 54.719 | +7.03% | -0.27% | 0.89x | 43.9 | 2026-11-13T16:06:38.979651+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 8 | TAO/USD | 212.5177 | 50.205 | 54.984 | +0.28% | -0.08% | 0.56x | 4.0 | 2026-11-13T16:06:38.979651+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 9 | ICP/USD | 2.611 | 42.003 | 42.821 | +1.44% | -0.53% | 1.19x | 7.7 | 2026-11-13T16:06:38.979651+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 10 | ICNT/USD | 0.2816 | 39.964 | 42.564 | +2.14% | +0.29% | 0.60x | 7.1 | 2026-11-13T16:06:38.979651+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 11 | STX/USD | 0.2908 | 37.060 | 44.680 | +2.07% | -0.07% | 0.27x | 6.9 | 2026-11-13T16:06:38.979651+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 12 | CT/USD | 0.1107 | 31.693 | 38.917 | +2.41% | -0.72% | 0.64x | 18.0 | 2026-11-13T16:06:38.979651+00:00 | NOT CALIBRATED / HIGH | WATCH |

**Confidence:** uncalibrated research heuristics, NOT validated probabilities. **BUY:** none authorized. Numerical baseline/challenger scores are uncalibrated paper-only ranking values, not probabilities or validated improvement.

## Learning and coverage

| Forward horizon | Evidence status | Verified matured / hits |
|---|---|---|
| 1h | PER HORIZON NOT INDEPENDENTLY VERIFIED | NOT VERIFIED |
| 6h | PER HORIZON NOT INDEPENDENTLY VERIFIED | NOT VERIFIED |
| 24h | PER HORIZON NOT INDEPENDENTLY VERIFIED | NOT VERIFIED |
| 48h | PER HORIZON NOT INDEPENDENTLY VERIFIED | NOT VERIFIED |

- Persisted scans: 362; predictions: 3347; observations: 217690.
- Matured sampled outcomes across 1/6/24/48h: 2926; gap abstentions: 9466. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 0 (sampled only; not a success-rate estimate).
- False positives / missed movers: NOT VERIFIED without eligible continuous outcome coverage.
- Baseline vs challenger: recorded as-of; unbiased held-out lift NOT MEASURED.
- Online Kraken /USD stablecoin-base pairs excluded: 18 (counted from this scan's online AssetPairs metadata, not inferred from price).
- Stablecoin base exclusions: BRL1, BUSD, DAI, EUR, EURC, EUROP, EURQ, EURR, EURT, FDUSD, FRAX, GUSD, PYUSD, QCAD, RLUSD, TGBP, TUSD, USD, USD1, USDC, USDD, USDE, USDG, USDQ, USDR, USDS, USDT, ZUSD.
- DEX: NOT USED; no DEX freshness gate.
- OHLC screening abstentions: 10; details in immutable scan JSON artifact.
- Storage: ledger and results published in one non-force Git commit and read back. Independent artifact recovery is NOT VERIFIED by this scan alone.
- Errors: none in successful committed scan; a failed workflow must not publish a SUCCESS report.
