# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-12T06:04:00.378267+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/43165250514
**Source SHA:** 21b4cf643df9f7a7adfddc959660920dd467c70b
**Ledger commit:** 9a5740b61712dcbc55175919c6488ef4fa155601
**Ledger generation:** 316 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 5s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 624; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 606; valid market observations: 606; OHLC screened: 14.

## Top WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | Confidence / risk | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---|---|---|
| 1 | ZEC/USD | 981.57 | 62.789 | 66.933 | +2.03% | -0.19% | 0.68x | 4.6 | 2026-11-12T06:03:55.274579+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 2 | PEPE/USD | 4.55e-06 | 54.819 | 60.423 | +0.93% | -0.20% | 0.54x | 2.2 | 2026-11-12T06:03:55.274579+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 3 | DOT/USD | 0.8411 | 51.558 | 36.676 | +0.30% | -0.02% | 5.47x | 2.4 | 2026-11-12T06:03:55.274579+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 4 | AVAX/USD | 8.563 | 49.801 | 57.443 | +0.60% | -0.26% | 0.36x | 3.5 | 2026-11-12T06:03:55.274579+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 5 | CAP/USD | 0.101091 | 38.233 | 33.839 | +0.62% | +0.27% | 1.30x | 6.0 | 2026-11-12T06:03:55.274579+00:00 | NOT CALIBRATED / HIGH | WATCH |

**Confidence:** uncalibrated research heuristics, NOT validated probabilities. **BUY:** none authorized. Numerical baseline/challenger scores are uncalibrated paper-only ranking values, not probabilities or validated improvement.

## Learning and coverage

| Forward horizon | Evidence status | Verified matured / hits |
|---|---|---|
| 1h | PER HORIZON NOT INDEPENDENTLY VERIFIED | NOT VERIFIED |
| 6h | PER HORIZON NOT INDEPENDENTLY VERIFIED | NOT VERIFIED |
| 24h | PER HORIZON NOT INDEPENDENTLY VERIFIED | NOT VERIFIED |
| 48h | PER HORIZON NOT INDEPENDENTLY VERIFIED | NOT VERIFIED |

- Persisted scans: 316; predictions: 3009; observations: 189813.
- Matured sampled outcomes across 1/6/24/48h: 2467; gap abstentions: 7915. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 0 (sampled only; not a success-rate estimate).
- False positives / missed movers: NOT VERIFIED without eligible continuous outcome coverage.
- Baseline vs challenger: recorded as-of; unbiased held-out lift NOT MEASURED.
- Online Kraken /USD stablecoin-base pairs excluded: 18 (counted from this scan's online AssetPairs metadata, not inferred from price).
- Stablecoin base exclusions: BRL1, BUSD, DAI, EUR, EURC, EUROP, EURQ, EURR, EURT, FDUSD, FRAX, GUSD, PYUSD, QCAD, RLUSD, TGBP, TUSD, USD, USD1, USDC, USDD, USDE, USDG, USDQ, USDR, USDS, USDT, ZUSD.
- DEX: NOT USED; no DEX freshness gate.
- OHLC screening abstentions: 9; details in immutable scan JSON artifact.
- Storage: checksum-sealed ledger pushed non-force and read back before this report. Independent artifact recovery is NOT VERIFIED by this scan alone.
- Errors: none in successful committed scan; a failed workflow must not publish a SUCCESS report.
