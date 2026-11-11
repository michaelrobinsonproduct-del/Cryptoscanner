# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-11T23:39:38.694694+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/43121195308
**Source SHA:** 21b4cf643df9f7a7adfddc959660920dd467c70b
**Ledger commit:** 93ed9ae8c221e532837abb847aa84888b5abe572
**Ledger generation:** 302 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 5s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 624; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 606; valid market observations: 606; OHLC screened: 18.

## Top WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | Confidence / risk | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---|---|---|
| 1 | XMR/USD | 583.41 | 75.414 | 74.235 | +3.69% | +0.40% | 0.92x | 13.2 | 2026-11-11T23:39:33.495272+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 2 | AVAX/USD | 8.48 | 62.486 | 62.180 | +1.36% | +0.49% | 0.79x | 4.7 | 2026-11-11T23:39:33.495272+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 3 | ICP/USD | 2.585 | 61.142 | 46.335 | +1.97% | -0.04% | 2.66x | 7.7 | 2026-11-11T23:39:33.495272+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 4 | TON/USD | 1.174 | 58.142 | 62.378 | +3.07% | +0.17% | 0.49x | 8.5 | 2026-11-11T23:39:33.495272+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 5 | XLM/USD | 0.146748 | 55.862 | 58.674 | +1.49% | +0.41% | 0.51x | 0.3 | 2026-11-11T23:39:33.495272+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 6 | FET/USD | 0.1475 | 41.430 | 38.572 | +1.72% | +0.41% | 1.08x | 13.6 | 2026-11-11T23:39:33.495272+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 7 | VVV/USD | 19.581 | 39.428 | 42.661 | +1.44% | +0.23% | 0.56x | 8.2 | 2026-11-11T23:39:33.495272+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 8 | PEAQ/USD | 0.02674 | 26.474 | 36.563 | +1.63% | -1.19% | 0.58x | 11.2 | 2026-11-11T23:39:33.495272+00:00 | NOT CALIBRATED / HIGH | WATCH |

**Confidence:** uncalibrated research heuristics, NOT validated probabilities. **BUY:** none authorized. Numerical baseline/challenger scores are uncalibrated paper-only ranking values, not probabilities or validated improvement.

## Learning and coverage

| Forward horizon | Evidence status | Verified matured / hits |
|---|---|---|
| 1h | PER HORIZON NOT INDEPENDENTLY VERIFIED | NOT VERIFIED |
| 6h | PER HORIZON NOT INDEPENDENTLY VERIFIED | NOT VERIFIED |
| 24h | PER HORIZON NOT INDEPENDENTLY VERIFIED | NOT VERIFIED |
| 48h | PER HORIZON NOT INDEPENDENTLY VERIFIED | NOT VERIFIED |

- Persisted scans: 302; predictions: 2886; observations: 181329.
- Matured sampled outcomes across 1/6/24/48h: 2267; gap abstentions: 7615. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 0 (sampled only; not a success-rate estimate).
- False positives / missed movers: NOT VERIFIED without eligible continuous outcome coverage.
- Baseline vs challenger: recorded as-of; unbiased held-out lift NOT MEASURED.
- Online Kraken /USD stablecoin-base pairs excluded: 18 (counted from this scan's online AssetPairs metadata, not inferred from price).
- Stablecoin base exclusions: BRL1, BUSD, DAI, EUR, EURC, EUROP, EURQ, EURR, EURT, FDUSD, FRAX, GUSD, PYUSD, QCAD, RLUSD, TGBP, TUSD, USD, USD1, USDC, USDD, USDE, USDG, USDQ, USDR, USDS, USDT, ZUSD.
- DEX: NOT USED; no DEX freshness gate.
- OHLC screening abstentions: 10; details in immutable scan JSON artifact.
- Storage: checksum-sealed ledger pushed non-force and read back before this report. Independent artifact recovery is NOT VERIFIED by this scan alone.
- Errors: none in successful committed scan; a failed workflow must not publish a SUCCESS report.
