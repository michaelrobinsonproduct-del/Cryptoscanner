# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-12T09:40:59.756428+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/43193075597
**Source SHA:** 21b4cf643df9f7a7adfddc959660920dd467c70b
**Ledger commit:** f046d683b030d7f742d72b781de95e4d0d9361ee
**Ledger generation:** 323 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 6s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 624; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 606; valid market observations: 606; OHLC screened: 18.

## Top WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | Confidence / risk | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---|---|---|
| 1 | AVAX/USD | 8.67 | 84.404 | 65.685 | +1.86% | +0.74% | 3.33x | 4.6 | 2026-11-12T09:40:53.910730+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 2 | ZEC/USD | 988.44 | 84.134 | 71.949 | +2.75% | +0.29% | 2.07x | 4.5 | 2026-11-12T09:40:53.910730+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 3 | TON/USD | 1.232 | 72.567 | 76.656 | +5.03% | +0.41% | 0.39x | 8.1 | 2026-11-12T09:40:53.910730+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 4 | AKE/USD | 0.00277277 | 41.251 | 61.078 | +11.92% | -2.24% | 0.14x | 35.1 | 2026-11-12T09:40:53.910730+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 5 | HBAR/USD | 0.06589 | 39.117 | 38.027 | +0.80% | +0.49% | 0.87x | 6.1 | 2026-11-12T09:40:53.910730+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 6 | DOT/USD | 0.8414 | 29.530 | 36.291 | +0.33% | +0.21% | 0.22x | 2.4 | 2026-11-12T09:40:53.910730+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 7 | ATOM/USD | 1.3978 | 23.572 | 30.288 | +0.31% | +0.28% | 0.19x | 7.2 | 2026-11-12T09:40:53.910730+00:00 | NOT CALIBRATED / HIGH | WATCH |

**Confidence:** uncalibrated research heuristics, NOT validated probabilities. **BUY:** none authorized. Numerical baseline/challenger scores are uncalibrated paper-only ranking values, not probabilities or validated improvement.

## Learning and coverage

| Forward horizon | Evidence status | Verified matured / hits |
|---|---|---|
| 1h | PER HORIZON NOT INDEPENDENTLY VERIFIED | NOT VERIFIED |
| 6h | PER HORIZON NOT INDEPENDENTLY VERIFIED | NOT VERIFIED |
| 24h | PER HORIZON NOT INDEPENDENTLY VERIFIED | NOT VERIFIED |
| 48h | PER HORIZON NOT INDEPENDENTLY VERIFIED | NOT VERIFIED |

- Persisted scans: 323; predictions: 3054; observations: 194055.
- Matured sampled outcomes across 1/6/24/48h: 2584; gap abstentions: 8023. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 0 (sampled only; not a success-rate estimate).
- False positives / missed movers: NOT VERIFIED without eligible continuous outcome coverage.
- Baseline vs challenger: recorded as-of; unbiased held-out lift NOT MEASURED.
- Online Kraken /USD stablecoin-base pairs excluded: 18 (counted from this scan's online AssetPairs metadata, not inferred from price).
- Stablecoin base exclusions: BRL1, BUSD, DAI, EUR, EURC, EUROP, EURQ, EURR, EURT, FDUSD, FRAX, GUSD, PYUSD, QCAD, RLUSD, TGBP, TUSD, USD, USD1, USDC, USDD, USDE, USDG, USDQ, USDR, USDS, USDT, ZUSD.
- DEX: NOT USED; no DEX freshness gate.
- OHLC screening abstentions: 11; details in immutable scan JSON artifact.
- Storage: checksum-sealed ledger pushed non-force and read back before this report. Independent artifact recovery is NOT VERIFIED by this scan alone.
- Errors: none in successful committed scan; a failed workflow must not publish a SUCCESS report.
