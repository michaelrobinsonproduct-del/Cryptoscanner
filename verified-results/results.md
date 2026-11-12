# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-12T01:40:37.371657+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/43135836080
**Source SHA:** 21b4cf643df9f7a7adfddc959660920dd467c70b
**Ledger commit:** 9b9b23decc160451f363808f550153fe56f0c34d
**Ledger generation:** 306 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 5s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 624; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 606; valid market observations: 606; OHLC screened: 17.

## Top WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | Confidence / risk | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---|---|---|
| 1 | SC/USD | 0.000671 | 78.377 | 57.136 | +4.84% | +1.36% | 2.44x | 14.9 | 2026-11-12T01:40:32.278391+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 2 | ZEC/USD | 989.41 | 78.081 | 72.044 | +2.85% | +0.54% | 1.34x | 5.8 | 2026-11-12T01:40:32.278391+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 3 | PEPE/USD | 4.542e-06 | 65.295 | 59.178 | +0.75% | +0.62% | 1.30x | 2.2 | 2026-11-12T01:40:32.278391+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 4 | XLM/USD | 0.147411 | 62.850 | 47.934 | +0.29% | -0.02% | 8.89x | 3.3 | 2026-11-12T01:40:32.278391+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 5 | AKE/USD | 0.00268882 | 55.133 | 60.036 | +8.54% | -0.40% | 0.71x | 34.2 | 2026-11-12T01:40:32.278391+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 6 | TON/USD | 1.19 | 51.737 | 50.631 | +1.45% | +0.59% | 0.81x | 8.4 | 2026-11-12T01:40:32.278391+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 7 | PAXG/USD | 3982.54 | 36.556 | 38.556 | +0.32% | -0.09% | 0.84x | 0.0 | 2026-11-12T01:40:32.278391+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 8 | PUMP/USD | 0.003476 | 34.535 | 42.362 | +0.43% | +0.20% | 0.12x | 5.8 | 2026-11-12T01:40:32.278391+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 9 | DOT/USD | 0.8427 | 33.859 | 38.592 | +0.49% | +0.26% | 0.40x | 2.4 | 2026-11-12T01:40:32.278391+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 10 | CAP/USD | 0.100991 | 32.526 | 33.782 | +0.52% | +0.19% | 0.78x | 5.4 | 2026-11-12T01:40:32.278391+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 11 | VVV/USD | 19.776 | 29.948 | 35.241 | +0.45% | +0.66% | 0.14x | 9.1 | 2026-11-12T01:40:32.278391+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 12 | PYTH/USD | 0.06454 | 23.848 | 30.288 | +0.92% | +0.22% | 0.25x | 17.1 | 2026-11-12T01:40:32.278391+00:00 | NOT CALIBRATED / HIGH | WATCH |

**Confidence:** uncalibrated research heuristics, NOT validated probabilities. **BUY:** none authorized. Numerical baseline/challenger scores are uncalibrated paper-only ranking values, not probabilities or validated improvement.

## Learning and coverage

| Forward horizon | Evidence status | Verified matured / hits |
|---|---|---|
| 1h | PER HORIZON NOT INDEPENDENTLY VERIFIED | NOT VERIFIED |
| 6h | PER HORIZON NOT INDEPENDENTLY VERIFIED | NOT VERIFIED |
| 24h | PER HORIZON NOT INDEPENDENTLY VERIFIED | NOT VERIFIED |
| 48h | PER HORIZON NOT INDEPENDENTLY VERIFIED | NOT VERIFIED |

- Persisted scans: 306; predictions: 2934; observations: 183753.
- Matured sampled outcomes across 1/6/24/48h: 2309; gap abstentions: 7744. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 0 (sampled only; not a success-rate estimate).
- False positives / missed movers: NOT VERIFIED without eligible continuous outcome coverage.
- Baseline vs challenger: recorded as-of; unbiased held-out lift NOT MEASURED.
- Online Kraken /USD stablecoin-base pairs excluded: 18 (counted from this scan's online AssetPairs metadata, not inferred from price).
- Stablecoin base exclusions: BRL1, BUSD, DAI, EUR, EURC, EUROP, EURQ, EURR, EURT, FDUSD, FRAX, GUSD, PYUSD, QCAD, RLUSD, TGBP, TUSD, USD, USD1, USDC, USDD, USDE, USDG, USDQ, USDR, USDS, USDT, ZUSD.
- DEX: NOT USED; no DEX freshness gate.
- OHLC screening abstentions: 5; details in immutable scan JSON artifact.
- Storage: checksum-sealed ledger pushed non-force and read back before this report. Independent artifact recovery is NOT VERIFIED by this scan alone.
- Errors: none in successful committed scan; a failed workflow must not publish a SUCCESS report.
