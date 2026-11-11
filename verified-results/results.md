# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-11T18:38:09.717038+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/43079242993
**Source SHA:** 21b4cf643df9f7a7adfddc959660920dd467c70b
**Ledger commit:** 126f7024b229fb08d1a2db16902912ec78993014
**Ledger generation:** 293 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 7s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 624; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 606; valid market observations: 605; OHLC screened: 24.

## Top WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | Confidence / risk | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---|---|---|
| 1 | TAO/USD | 224.1153 | 87.079 | 71.797 | +2.72% | +0.06% | 3.05x | 4.5 | 2026-11-11T18:38:03.177801+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 2 | VVV/USD | 20.563 | 85.245 | 78.030 | +6.53% | +0.45% | 1.50x | 7.8 | 2026-11-11T18:38:03.177801+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 3 | XMR/USD | 590.75 | 84.934 | 78.009 | +5.00% | +0.25% | 1.57x | 23.9 | 2026-11-11T18:38:03.177801+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 4 | ADA/USD | 0.178127 | 84.621 | 70.419 | +2.49% | -0.16% | 10.60x | 3.9 | 2026-11-11T18:38:03.177801+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 5 | XLM/USD | 0.149853 | 80.925 | 72.843 | +3.64% | -0.35% | 1.99x | 2.2 | 2026-11-11T18:38:03.177801+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 6 | NEAR/USD | 3.7411 | 80.904 | 83.852 | +4.39% | +0.06% | 0.68x | 3.7 | 2026-11-11T18:38:03.177801+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 7 | AVAX/USD | 8.634 | 79.595 | 75.107 | +3.20% | +0.06% | 1.42x | 4.6 | 2026-11-11T18:38:03.177801+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 8 | SOL/USD | 85.25 | 76.762 | 71.316 | +2.41% | +0.02% | 1.53x | 1.2 | 2026-11-11T18:38:03.177801+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 9 | TON/USD | 1.226 | 71.189 | 75.263 | +7.64% | +0.41% | 0.39x | 32.6 | 2026-11-11T18:38:03.177801+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 10 | SUI/USD | 0.8411 | 66.316 | 69.974 | +2.22% | -0.10% | 0.68x | 1.2 | 2026-11-11T18:38:03.177801+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 11 | ETH/USD | 2087.53 | 63.387 | 67.565 | +1.80% | -0.13% | 0.65x | 0.0 | 2026-11-11T18:38:03.177801+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 12 | LTC/USD | 51.15 | 63.267 | 48.267 | +0.89% | +0.00% | 3.19x | 2.0 | 2026-11-11T18:38:03.177801+00:00 | NOT CALIBRATED / HIGH | WATCH |

**Confidence:** uncalibrated research heuristics, NOT validated probabilities. **BUY:** none authorized. Numerical baseline/challenger scores are uncalibrated paper-only ranking values, not probabilities or validated improvement.

## Learning and coverage

| Forward horizon | Evidence status | Verified matured / hits |
|---|---|---|
| 1h | PER HORIZON NOT INDEPENDENTLY VERIFIED | NOT VERIFIED |
| 6h | PER HORIZON NOT INDEPENDENTLY VERIFIED | NOT VERIFIED |
| 24h | PER HORIZON NOT INDEPENDENTLY VERIFIED | NOT VERIFIED |
| 48h | PER HORIZON NOT INDEPENDENTLY VERIFIED | NOT VERIFIED |

- Persisted scans: 293; predictions: 2784; observations: 175878.
- Matured sampled outcomes across 1/6/24/48h: 2147; gap abstentions: 7266. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 0 (sampled only; not a success-rate estimate).
- False positives / missed movers: NOT VERIFIED without eligible continuous outcome coverage.
- Baseline vs challenger: recorded as-of; unbiased held-out lift NOT MEASURED.
- Online Kraken /USD stablecoin-base pairs excluded: 18 (counted from this scan's online AssetPairs metadata, not inferred from price).
- Stablecoin base exclusions: BRL1, BUSD, DAI, EUR, EURC, EUROP, EURQ, EURR, EURT, FDUSD, FRAX, GUSD, PYUSD, QCAD, RLUSD, TGBP, TUSD, USD, USD1, USDC, USDD, USDE, USDG, USDQ, USDR, USDS, USDT, ZUSD.
- DEX: NOT USED; no DEX freshness gate.
- OHLC screening abstentions: 3; details in immutable scan JSON artifact.
- Storage: checksum-sealed ledger pushed non-force and read back before this report. Independent artifact recovery is NOT VERIFIED by this scan alone.
- Errors: none in successful committed scan; a failed workflow must not publish a SUCCESS report.
