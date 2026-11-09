# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-09T17:18:25.322698+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/42663138095
**Source SHA:** 69b32fce88f9296ad7d9292e14e64b61178763c7
**Ledger commit:** 1316fef197f7da768442a77146c9ad35102767b5
**Ledger generation:** 203 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 8s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 624; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 606; valid market observations: 606; OHLC screened: 24.

## Top WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | Confidence / risk | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---|---|---|
| 1 | AAVE/USD | 133.53 | 104.680 | 89.943 | +6.02% | -0.05% | 4.00x | 6.7 | 2026-11-09T17:18:16.843955+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 2 | AVAX/USD | 8.727 | 99.715 | 97.708 | +10.06% | +0.05% | 1.18x | 4.6 | 2026-11-09T17:18:16.843955+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 3 | ENA/USD | 0.1545 | 94.719 | 80.042 | +4.04% | -0.06% | 3.57x | 6.5 | 2026-11-09T17:18:16.843955+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 4 | PEPE/USD | 5.245e-06 | 90.380 | 93.351 | +6.02% | -0.27% | 0.84x | 7.6 | 2026-11-09T17:18:16.843955+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 5 | USELESS/USD | 0.13423 | 89.722 | 76.782 | +9.01% | -0.19% | 2.39x | 16.4 | 2026-11-09T17:18:16.843955+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 6 | ONDO/USD | 0.37353 | 88.331 | 96.536 | +6.24% | -0.71% | 0.53x | 2.4 | 2026-11-09T17:18:16.843955+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 7 | VVV/USD | 21.282 | 87.940 | 74.603 | +6.09% | -0.33% | 2.50x | 7.1 | 2026-11-09T17:18:16.843955+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 8 | JUP/USD | 0.25 | 83.409 | 85.183 | +7.84% | -0.30% | 0.97x | 0.4 | 2026-11-09T17:18:16.843955+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 9 | ARB/USD | 0.1793 | 74.186 | 82.195 | +8.08% | -0.44% | 0.42x | 11.2 | 2026-11-09T17:18:16.843955+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 10 | SUI/USD | 0.8497 | 68.797 | 79.411 | +3.57% | -0.48% | 0.18x | 1.2 | 2026-11-09T17:18:16.843955+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 11 | BCH/USD | 243.22 | 63.584 | 47.118 | +1.79% | +0.29% | 4.42x | 0.4 | 2026-11-09T17:18:16.843955+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 12 | HYPE/USD | 75.34 | 59.816 | 62.514 | +1.17% | +0.16% | 0.65x | 1.3 | 2026-11-09T17:18:16.843955+00:00 | NOT CALIBRATED / HIGH | WATCH |

**Confidence:** uncalibrated research heuristics, NOT validated probabilities. **BUY:** none authorized. Numerical baseline/challenger scores are uncalibrated paper-only ranking values, not probabilities or validated improvement.

## Learning and coverage

| Forward horizon | Evidence status | Verified matured / hits |
|---|---|---|
| 1h | PER HORIZON NOT INDEPENDENTLY VERIFIED | NOT VERIFIED |
| 6h | PER HORIZON NOT INDEPENDENTLY VERIFIED | NOT VERIFIED |
| 24h | PER HORIZON NOT INDEPENDENTLY VERIFIED | NOT VERIFIED |
| 48h | PER HORIZON NOT INDEPENDENTLY VERIFIED | NOT VERIFIED |

- Persisted scans: 203; predictions: 1839; observations: 122725.
- Matured sampled outcomes across 1/6/24/48h: 1045; gap abstentions: 4950. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 0 (sampled only; not a success-rate estimate).
- False positives / missed movers: NOT VERIFIED without eligible continuous outcome coverage.
- Baseline vs challenger: recorded as-of; unbiased held-out lift NOT MEASURED.
- Online Kraken /USD stablecoin-base pairs excluded: 18 (counted from this scan's online AssetPairs metadata, not inferred from price).
- Stablecoin base exclusions: BRL1, BUSD, DAI, EUR, EURC, EUROP, EURQ, EURR, EURT, FDUSD, FRAX, GUSD, PYUSD, QCAD, RLUSD, TGBP, TUSD, USD, USD1, USDC, USDD, USDE, USDG, USDQ, USDR, USDS, USDT, ZUSD.
- DEX: NOT USED; no DEX freshness gate.
- OHLC screening abstentions: 6; details in immutable scan JSON artifact.
- Storage: checksum-sealed ledger pushed non-force and read back before this report. Independent artifact recovery is NOT VERIFIED by this scan alone.
- Errors: none in successful committed scan; a failed workflow must not publish a SUCCESS report.
