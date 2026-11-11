# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-11T17:36:16.964775+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/43069409515
**Source SHA:** 21b4cf643df9f7a7adfddc959660920dd467c70b
**Ledger commit:** 2fcc76bf7337c475206340a3051279e27152ae51
**Ledger generation:** 291 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 7s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 624; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 606; valid market observations: 605; OHLC screened: 24.

## Top WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | Confidence / risk | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---|---|---|
| 1 | CC/USD | 0.09439 | 88.741 | 73.928 | +5.49% | +0.56% | 2.20x | 7.4 | 2026-11-11T17:36:09.751802+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 2 | SUI/USD | 0.8462 | 86.786 | 74.316 | +2.84% | -0.51% | 3.63x | 1.2 | 2026-11-11T17:36:09.751802+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 3 | NEAR/USD | 3.7607 | 84.551 | 88.090 | +4.94% | -0.85% | 1.07x | 2.9 | 2026-11-11T17:36:09.751802+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 4 | TAO/USD | 223.9762 | 81.909 | 70.373 | +2.66% | -0.69% | 8.51x | 6.5 | 2026-11-11T17:36:09.751802+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 5 | TON/USD | 1.209 | 81.484 | 81.023 | +6.15% | -0.90% | 1.50x | 16.6 | 2026-11-11T17:36:09.751802+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 6 | ETH/USD | 2087.59 | 81.279 | 67.586 | +1.80% | -0.26% | 3.40x | 0.0 | 2026-11-11T17:36:09.751802+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 7 | AVAX/USD | 8.683 | 76.485 | 79.796 | +3.79% | -0.18% | 0.76x | 3.5 | 2026-11-11T17:36:09.751802+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 8 | XMR/USD | 593.45 | 75.651 | 86.424 | +5.48% | -0.68% | 0.26x | 13.8 | 2026-11-11T17:36:09.751802+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 9 | SOL/USD | 85.26 | 72.472 | 71.401 | +2.43% | -0.22% | 1.22x | 1.2 | 2026-11-11T17:36:09.751802+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 10 | XLM/USD | 0.150995 | 71.963 | 78.888 | +4.43% | -0.22% | 0.42x | 2.5 | 2026-11-11T17:36:09.751802+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 11 | ADA/USD | 0.179348 | 68.900 | 73.295 | +3.19% | -0.41% | 0.76x | 5.5 | 2026-11-11T17:36:09.751802+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 12 | VVV/USD | 20.463 | 67.467 | 76.153 | +6.01% | -1.29% | 0.78x | 8.3 | 2026-11-11T17:36:09.751802+00:00 | NOT CALIBRATED / HIGH | WATCH |

**Confidence:** uncalibrated research heuristics, NOT validated probabilities. **BUY:** none authorized. Numerical baseline/challenger scores are uncalibrated paper-only ranking values, not probabilities or validated improvement.

## Learning and coverage

| Forward horizon | Evidence status | Verified matured / hits |
|---|---|---|
| 1h | PER HORIZON NOT INDEPENDENTLY VERIFIED | NOT VERIFIED |
| 6h | PER HORIZON NOT INDEPENDENTLY VERIFIED | NOT VERIFIED |
| 24h | PER HORIZON NOT INDEPENDENTLY VERIFIED | NOT VERIFIED |
| 48h | PER HORIZON NOT INDEPENDENTLY VERIFIED | NOT VERIFIED |

- Persisted scans: 291; predictions: 2760; observations: 174668.
- Matured sampled outcomes across 1/6/24/48h: 2099; gap abstentions: 7226. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 0 (sampled only; not a success-rate estimate).
- False positives / missed movers: NOT VERIFIED without eligible continuous outcome coverage.
- Baseline vs challenger: recorded as-of; unbiased held-out lift NOT MEASURED.
- Online Kraken /USD stablecoin-base pairs excluded: 18 (counted from this scan's online AssetPairs metadata, not inferred from price).
- Stablecoin base exclusions: BRL1, BUSD, DAI, EUR, EURC, EUROP, EURQ, EURR, EURT, FDUSD, FRAX, GUSD, PYUSD, QCAD, RLUSD, TGBP, TUSD, USD, USD1, USDC, USDD, USDE, USDG, USDQ, USDR, USDS, USDT, ZUSD.
- DEX: NOT USED; no DEX freshness gate.
- OHLC screening abstentions: 6; details in immutable scan JSON artifact.
- Storage: checksum-sealed ledger pushed non-force and read back before this report. Independent artifact recovery is NOT VERIFIED by this scan alone.
- Errors: none in successful committed scan; a failed workflow must not publish a SUCCESS report.
