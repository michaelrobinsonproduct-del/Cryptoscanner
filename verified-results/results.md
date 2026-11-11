# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-11T22:22:02.901036+00:00
**GitHub trigger:** scheduled (verified event=schedule; originating cron=20,50 * * * *, intended UTC minute=20,50; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/43110778835
**Source SHA:** 21b4cf643df9f7a7adfddc959660920dd467c70b
**Ledger commit:** 74de17ae6f38fd9edab510a5ad317b44706f7637
**Ledger generation:** 300 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 6s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 624; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 606; valid market observations: 606; OHLC screened: 24.

## Top WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | Confidence / risk | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---|---|---|
| 1 | XLM/USD | 0.149565 | 87.845 | 71.240 | +3.44% | +0.32% | 7.60x | 1.5 | 2026-11-11T22:21:56.696802+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 2 | NEAR/USD | 3.6892 | 85.034 | 73.823 | +2.94% | +0.23% | 2.01x | 3.5 | 2026-11-11T22:21:56.696802+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 3 | XMR/USD | 587.52 | 81.715 | 84.677 | +4.42% | +0.32% | 0.54x | 2.6 | 2026-11-11T22:21:56.696802+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 4 | AVAX/USD | 8.597 | 76.742 | 72.002 | +2.76% | -0.07% | 1.51x | 4.7 | 2026-11-11T22:21:56.696802+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 5 | ADA/USD | 0.177356 | 67.938 | 67.799 | +2.04% | +0.26% | 0.89x | 3.0 | 2026-11-11T22:21:56.696802+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 6 | SUI/USD | 0.8361 | 66.902 | 65.717 | +1.62% | +0.22% | 1.01x | 1.2 | 2026-11-11T22:21:56.696802+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 7 | ETH/USD | 2075.14 | 65.097 | 63.336 | +1.19% | +0.42% | 0.97x | 0.0 | 2026-11-11T22:21:56.696802+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 8 | SOL/USD | 84.66 | 63.954 | 66.351 | +1.71% | +0.31% | 0.61x | 1.2 | 2026-11-11T22:21:56.696802+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 9 | DOT/USD | 0.8531 | 59.666 | 43.198 | +1.26% | +0.29% | 2.80x | 1.2 | 2026-11-11T22:21:56.696802+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 10 | HYPE/USD | 72.84 | 59.291 | 60.323 | +0.86% | +0.15% | 0.82x | 1.4 | 2026-11-11T22:21:56.696802+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 11 | ICP/USD | 2.632 | 56.972 | 61.177 | +3.83% | +0.46% | 0.35x | 7.6 | 2026-11-11T22:21:56.696802+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 12 | XRP/USD | 1.06102 | 55.995 | 58.874 | +0.56% | +0.05% | 0.69x | 0.1 | 2026-11-11T22:21:56.696802+00:00 | NOT CALIBRATED / HIGH | WATCH |

**Confidence:** uncalibrated research heuristics, NOT validated probabilities. **BUY:** none authorized. Numerical baseline/challenger scores are uncalibrated paper-only ranking values, not probabilities or validated improvement.

## Learning and coverage

| Forward horizon | Evidence status | Verified matured / hits |
|---|---|---|
| 1h | PER HORIZON NOT INDEPENDENTLY VERIFIED | NOT VERIFIED |
| 6h | PER HORIZON NOT INDEPENDENTLY VERIFIED | NOT VERIFIED |
| 24h | PER HORIZON NOT INDEPENDENTLY VERIFIED | NOT VERIFIED |
| 48h | PER HORIZON NOT INDEPENDENTLY VERIFIED | NOT VERIFIED |

- Persisted scans: 300; predictions: 2868; observations: 180117.
- Matured sampled outcomes across 1/6/24/48h: 2243; gap abstentions: 7484. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 0 (sampled only; not a success-rate estimate).
- False positives / missed movers: NOT VERIFIED without eligible continuous outcome coverage.
- Baseline vs challenger: recorded as-of; unbiased held-out lift NOT MEASURED.
- Online Kraken /USD stablecoin-base pairs excluded: 18 (counted from this scan's online AssetPairs metadata, not inferred from price).
- Stablecoin base exclusions: BRL1, BUSD, DAI, EUR, EURC, EUROP, EURQ, EURR, EURT, FDUSD, FRAX, GUSD, PYUSD, QCAD, RLUSD, TGBP, TUSD, USD, USD1, USDC, USDD, USDE, USDG, USDQ, USDR, USDS, USDT, ZUSD.
- DEX: NOT USED; no DEX freshness gate.
- OHLC screening abstentions: 7; details in immutable scan JSON artifact.
- Storage: checksum-sealed ledger pushed non-force and read back before this report. Independent artifact recovery is NOT VERIFIED by this scan alone.
- Errors: none in successful committed scan; a failed workflow must not publish a SUCCESS report.
