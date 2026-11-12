# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-12T01:01:32.597140+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/43131228169
**Source SHA:** 21b4cf643df9f7a7adfddc959660920dd467c70b
**Ledger commit:** 9df60594db6ca19cf14ad419cc4c8cda102cb3c0
**Ledger generation:** 305 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 7s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 624; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 606; valid market observations: 606; OHLC screened: 24.

## Top WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | Confidence / risk | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---|---|---|
| 1 | ETH/USD | 2059.76 | 71.749 | 57.038 | +0.29% | -0.06% | 3.02x | 0.0 | 2026-11-12T01:01:25.221742+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 2 | ZEC/USD | 989.26 | 67.751 | 71.334 | +2.83% | -0.71% | 1.00x | 7.0 | 2026-11-12T01:01:25.221742+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 3 | AVAX/USD | 8.558 | 65.138 | 57.032 | +0.54% | -0.33% | 1.97x | 3.5 | 2026-11-12T01:01:25.221742+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 4 | XRP/USD | 1.05685 | 64.006 | 57.970 | +0.55% | -0.15% | 1.68x | 1.8 | 2026-11-12T01:01:25.221742+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 5 | SOL/USD | 83.58 | 60.566 | 57.768 | +0.48% | -0.18% | 1.37x | 1.2 | 2026-11-12T01:01:25.221742+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 6 | PEPE/USD | 4.561e-06 | 55.545 | 61.038 | +1.18% | -0.13% | 0.52x | 4.4 | 2026-11-12T01:01:25.221742+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 7 | NEAR/USD | 3.6193 | 52.693 | 58.124 | +1.00% | -0.15% | 0.53x | 7.7 | 2026-11-12T01:01:25.221742+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 8 | TON/USD | 1.181 | 49.401 | 41.178 | +0.68% | +0.43% | 1.61x | 16.9 | 2026-11-12T01:01:25.221742+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 9 | TAO/USD | 216.6177 | 47.878 | 54.440 | +0.38% | -0.32% | 0.51x | 6.4 | 2026-11-12T01:01:25.221742+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 10 | XLM/USD | 0.148056 | 45.150 | 50.953 | +0.73% | +0.05% | 0.40x | 2.4 | 2026-11-12T01:01:25.221742+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 11 | ALGO/USD | 0.08942 | 43.251 | 29.868 | +0.26% | -0.32% | 5.16x | 7.8 | 2026-11-12T01:01:25.221742+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 12 | INJ/USD | 7.556 | 40.980 | 45.825 | +0.25% | +0.27% | 0.38x | 7.9 | 2026-11-12T01:01:25.221742+00:00 | NOT CALIBRATED / HIGH | WATCH |

**Confidence:** uncalibrated research heuristics, NOT validated probabilities. **BUY:** none authorized. Numerical baseline/challenger scores are uncalibrated paper-only ranking values, not probabilities or validated improvement.

## Learning and coverage

| Forward horizon | Evidence status | Verified matured / hits |
|---|---|---|
| 1h | PER HORIZON NOT INDEPENDENTLY VERIFIED | NOT VERIFIED |
| 6h | PER HORIZON NOT INDEPENDENTLY VERIFIED | NOT VERIFIED |
| 24h | PER HORIZON NOT INDEPENDENTLY VERIFIED | NOT VERIFIED |
| 48h | PER HORIZON NOT INDEPENDENTLY VERIFIED | NOT VERIFIED |

- Persisted scans: 305; predictions: 2922; observations: 183147.
- Matured sampled outcomes across 1/6/24/48h: 2301; gap abstentions: 7717. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 0 (sampled only; not a success-rate estimate).
- False positives / missed movers: NOT VERIFIED without eligible continuous outcome coverage.
- Baseline vs challenger: recorded as-of; unbiased held-out lift NOT MEASURED.
- Online Kraken /USD stablecoin-base pairs excluded: 18 (counted from this scan's online AssetPairs metadata, not inferred from price).
- Stablecoin base exclusions: BRL1, BUSD, DAI, EUR, EURC, EUROP, EURQ, EURR, EURT, FDUSD, FRAX, GUSD, PYUSD, QCAD, RLUSD, TGBP, TUSD, USD, USD1, USDC, USDD, USDE, USDG, USDQ, USDR, USDS, USDT, ZUSD.
- DEX: NOT USED; no DEX freshness gate.
- OHLC screening abstentions: 6; details in immutable scan JSON artifact.
- Storage: checksum-sealed ledger pushed non-force and read back before this report. Independent artifact recovery is NOT VERIFIED by this scan alone.
- Errors: none in successful committed scan; a failed workflow must not publish a SUCCESS report.
