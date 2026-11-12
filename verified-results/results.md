# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-12T13:37:48.005641+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/43228631924
**Source SHA:** 21b4cf643df9f7a7adfddc959660920dd467c70b
**Ledger commit:** d3aa0c84bd3b5bc4e8e8eff32669798e1211a173
**Ledger generation:** 331 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 3s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 624; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 606; valid market observations: 606; OHLC screened: 8.

## Top WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | Confidence / risk | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---|---|---|
| 1 | TON/USD | 1.266 | 93.737 | 84.099 | +7.93% | +0.24% | 1.85x | 7.9 | 2026-11-12T13:37:45.016486+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 2 | AKE/USD | 0.00270643 | 71.862 | 57.286 | +9.25% | -0.08% | 6.90x | 43.1 | 2026-11-12T13:37:45.016486+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 3 | MON/USD | 0.01683 | 53.737 | 33.924 | +1.02% | +0.96% | 13.63x | 11.9 | 2026-11-12T13:37:45.016486+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 4 | JUP/USD | 0.25598 | 38.340 | 28.294 | +0.32% | +0.68% | 1.66x | 14.5 | 2026-11-12T13:37:45.016486+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 5 | XDC/USD | 0.02946 | 33.747 | 42.099 | +1.38% | -0.51% | 0.42x | 17.0 | 2026-11-12T13:37:45.016486+00:00 | NOT CALIBRATED / HIGH | WATCH |

**Confidence:** uncalibrated research heuristics, NOT validated probabilities. **BUY:** none authorized. Numerical baseline/challenger scores are uncalibrated paper-only ranking values, not probabilities or validated improvement.

## Learning and coverage

| Forward horizon | Evidence status | Verified matured / hits |
|---|---|---|
| 1h | PER HORIZON NOT INDEPENDENTLY VERIFIED | NOT VERIFIED |
| 6h | PER HORIZON NOT INDEPENDENTLY VERIFIED | NOT VERIFIED |
| 24h | PER HORIZON NOT INDEPENDENTLY VERIFIED | NOT VERIFIED |
| 48h | PER HORIZON NOT INDEPENDENTLY VERIFIED | NOT VERIFIED |

- Persisted scans: 331; predictions: 3099; observations: 198902.
- Matured sampled outcomes across 1/6/24/48h: 2699; gap abstentions: 8146. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 0 (sampled only; not a success-rate estimate).
- False positives / missed movers: NOT VERIFIED without eligible continuous outcome coverage.
- Baseline vs challenger: recorded as-of; unbiased held-out lift NOT MEASURED.
- Online Kraken /USD stablecoin-base pairs excluded: 18 (counted from this scan's online AssetPairs metadata, not inferred from price).
- Stablecoin base exclusions: BRL1, BUSD, DAI, EUR, EURC, EUROP, EURQ, EURR, EURT, FDUSD, FRAX, GUSD, PYUSD, QCAD, RLUSD, TGBP, TUSD, USD, USD1, USDC, USDD, USDE, USDG, USDQ, USDR, USDS, USDT, ZUSD.
- DEX: NOT USED; no DEX freshness gate.
- OHLC screening abstentions: 3; details in immutable scan JSON artifact.
- Storage: checksum-sealed ledger pushed non-force and read back before this report. Independent artifact recovery is NOT VERIFIED by this scan alone.
- Errors: none in successful committed scan; a failed workflow must not publish a SUCCESS report.
