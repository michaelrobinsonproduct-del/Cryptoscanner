# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-10T16:39:09.216825+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/42856359134
**Source SHA:** 3774b902ccb4e4fd5507499dc7c96ebbb4185329
**Ledger commit:** b9d003df0ddb5219aab7b184b8dec5e093669581
**Ledger generation:** 240 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 5s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 624; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 606; valid market observations: 595; OHLC screened: 12.

## Top WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | Confidence / risk | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---|---|---|
| 1 | TON/USD | 1.102 | 54.800 | 62.337 | +5.96% | -0.72% | 0.61x | 27.3 | 2026-11-10T16:39:04.682278+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 2 | XDC/USD | 0.03022 | 53.050 | 54.429 | +2.54% | +0.20% | 0.76x | 6.6 | 2026-11-10T16:39:04.682278+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 3 | PEPE/USD | 5.164e-06 | 46.730 | 58.802 | +0.82% | -2.57% | 1.08x | 3.9 | 2026-11-10T16:39:04.682278+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 4 | NIGHT/USD | 0.04143 | 46.167 | 54.827 | +2.35% | -0.65% | 0.46x | 9.7 | 2026-11-10T16:39:04.682278+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 5 | UAI/USD | 0.04096 | 45.808 | 61.112 | +6.22% | -2.06% | 0.50x | 31.8 | 2026-11-10T16:39:04.682278+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 6 | TRX/USD | 0.318354 | 41.334 | 40.986 | +0.31% | -0.18% | 1.12x | 1.4 | 2026-11-10T16:39:04.682278+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 7 | PLAY/USD | 0.008519 | 28.863 | 41.879 | +3.73% | -0.73% | 0.06x | 30.5 | 2026-11-10T16:39:04.682278+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 8 | CAP/USD | 0.101243 | 28.608 | 36.171 | +2.41% | -0.07% | 0.28x | 37.2 | 2026-11-10T16:39:04.682278+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 9 | PLUME/USD | 0.0129 | 23.642 | 28.449 | +0.78% | -0.92% | 0.98x | 15.5 | 2026-11-10T16:39:04.682278+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 10 | LIGHTER/USD | 3.301 | 21.143 | 41.836 | +2.10% | -2.74% | 0.30x | 15.2 | 2026-11-10T16:39:04.682278+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 11 | Q/USD | 0.024815 | 15.697 | 15.898 | +0.69% | -0.83% | 1.39x | 40.0 | 2026-11-10T16:39:04.682278+00:00 | NOT CALIBRATED / HIGH | WATCH |

**Confidence:** uncalibrated research heuristics, NOT validated probabilities. **BUY:** none authorized. Numerical baseline/challenger scores are uncalibrated paper-only ranking values, not probabilities or validated improvement.

## Learning and coverage

| Forward horizon | Evidence status | Verified matured / hits |
|---|---|---|
| 1h | PER HORIZON NOT INDEPENDENTLY VERIFIED | NOT VERIFIED |
| 6h | PER HORIZON NOT INDEPENDENTLY VERIFIED | NOT VERIFIED |
| 24h | PER HORIZON NOT INDEPENDENTLY VERIFIED | NOT VERIFIED |
| 48h | PER HORIZON NOT INDEPENDENTLY VERIFIED | NOT VERIFIED |

- Persisted scans: 240; predictions: 2206; observations: 143968.
- Matured sampled outcomes across 1/6/24/48h: 1247; gap abstentions: 6181. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 0 (sampled only; not a success-rate estimate).
- False positives / missed movers: NOT VERIFIED without eligible continuous outcome coverage.
- Baseline vs challenger: recorded as-of; unbiased held-out lift NOT MEASURED.
- Online Kraken /USD stablecoin-base pairs excluded: 18 (counted from this scan's online AssetPairs metadata, not inferred from price).
- Stablecoin base exclusions: BRL1, BUSD, DAI, EUR, EURC, EUROP, EURQ, EURR, EURT, FDUSD, FRAX, GUSD, PYUSD, QCAD, RLUSD, TGBP, TUSD, USD, USD1, USDC, USDD, USDE, USDG, USDQ, USDR, USDS, USDT, ZUSD.
- DEX: NOT USED; no DEX freshness gate.
- OHLC screening abstentions: 1; details in immutable scan JSON artifact.
- Storage: checksum-sealed ledger pushed non-force and read back before this report. Independent artifact recovery is NOT VERIFIED by this scan alone.
- Errors: none in successful committed scan; a failed workflow must not publish a SUCCESS report.
