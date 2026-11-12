# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-12T15:07:00.090754+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/43243741781
**Source SHA:** 21b4cf643df9f7a7adfddc959660920dd467c70b
**Ledger commit:** 099e10770acf2f3db1821849a5d5d95fee013362
**Ledger generation:** 334 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 2s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 624; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 606; valid market observations: 606; OHLC screened: 7.

## Top WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | Confidence / risk | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---|---|---|
| 1 | TON/USD | 1.245 | 86.418 | 83.602 | +6.14% | -0.56% | 1.56x | 8.0 | 2026-11-12T15:06:57.614680+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 2 | CAP/USD | 0.101455 | 49.974 | 35.082 | +0.98% | -0.02% | 2.90x | 6.1 | 2026-11-12T15:06:57.614680+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 3 | JUP/USD | 0.25839 | 44.055 | 37.180 | +1.26% | -0.35% | 1.86x | 10.1 | 2026-11-12T15:06:57.614680+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 4 | BAT/USD | 0.12046 | 38.153 | 46.703 | +2.32% | -1.09% | 0.69x | 5.0 | 2026-11-12T15:06:57.614680+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 5 | XDC/USD | 0.02928 | 30.008 | 37.267 | +0.76% | -0.03% | 0.29x | 17.1 | 2026-11-12T15:06:57.614680+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 6 | MON/USD | 0.01681 | 25.959 | 33.258 | +0.90% | -0.71% | 0.62x | 11.9 | 2026-11-12T15:06:57.614680+00:00 | NOT CALIBRATED / HIGH | WATCH |

**Confidence:** uncalibrated research heuristics, NOT validated probabilities. **BUY:** none authorized. Numerical baseline/challenger scores are uncalibrated paper-only ranking values, not probabilities or validated improvement.

## Learning and coverage

| Forward horizon | Evidence status | Verified matured / hits |
|---|---|---|
| 1h | PER HORIZON NOT INDEPENDENTLY VERIFIED | NOT VERIFIED |
| 6h | PER HORIZON NOT INDEPENDENTLY VERIFIED | NOT VERIFIED |
| 24h | PER HORIZON NOT INDEPENDENTLY VERIFIED | NOT VERIFIED |
| 48h | PER HORIZON NOT INDEPENDENTLY VERIFIED | NOT VERIFIED |

- Persisted scans: 334; predictions: 3119; observations: 200720.
- Matured sampled outcomes across 1/6/24/48h: 2731; gap abstentions: 8208. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 0 (sampled only; not a success-rate estimate).
- False positives / missed movers: NOT VERIFIED without eligible continuous outcome coverage.
- Baseline vs challenger: recorded as-of; unbiased held-out lift NOT MEASURED.
- Online Kraken /USD stablecoin-base pairs excluded: 18 (counted from this scan's online AssetPairs metadata, not inferred from price).
- Stablecoin base exclusions: BRL1, BUSD, DAI, EUR, EURC, EUROP, EURQ, EURR, EURT, FDUSD, FRAX, GUSD, PYUSD, QCAD, RLUSD, TGBP, TUSD, USD, USD1, USDC, USDD, USDE, USDG, USDQ, USDR, USDS, USDT, ZUSD.
- DEX: NOT USED; no DEX freshness gate.
- OHLC screening abstentions: 1; details in immutable scan JSON artifact.
- Storage: checksum-sealed ledger pushed non-force and read back before this report. Independent artifact recovery is NOT VERIFIED by this scan alone.
- Errors: none in successful committed scan; a failed workflow must not publish a SUCCESS report.
