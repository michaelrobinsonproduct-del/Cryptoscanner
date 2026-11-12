# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-12T10:06:58.582137+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/43196954975
**Source SHA:** 21b4cf643df9f7a7adfddc959660920dd467c70b
**Ledger commit:** 86ba4b2fb803c935ab8c3ffe77afefa85f90a752
**Ledger generation:** 324 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 5s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 624; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 606; valid market observations: 606; OHLC screened: 19.

## Top WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | Confidence / risk | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---|---|---|
| 1 | TON/USD | 1.238 | 89.448 | 80.287 | +5.54% | -0.24% | 2.04x | 8.1 | 2026-11-12T10:06:53.254071+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 2 | BAT/USD | 0.12399 | 82.695 | 68.138 | +5.32% | -0.09% | 11.87x | 4.0 | 2026-11-12T10:06:53.254071+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 3 | AVAX/USD | 8.685 | 61.837 | 65.772 | +2.03% | +0.35% | 0.43x | 6.9 | 2026-11-12T10:06:53.254071+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 4 | ZEC/USD | 979.94 | 56.129 | 65.794 | +1.86% | -1.01% | 0.54x | 4.5 | 2026-11-12T10:06:53.254071+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 5 | AKE/USD | 0.00265952 | 35.341 | 58.828 | +7.35% | -3.56% | 0.43x | 39.4 | 2026-11-12T10:06:53.254071+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 6 | DOT/USD | 0.8434 | 33.967 | 37.285 | +0.57% | +0.36% | 0.49x | 3.6 | 2026-11-12T10:06:53.254071+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 7 | HBAR/USD | 0.06604 | 33.954 | 40.418 | +1.02% | +0.03% | 0.34x | 4.5 | 2026-11-12T10:06:53.254071+00:00 | NOT CALIBRATED / HIGH | WATCH |

**Confidence:** uncalibrated research heuristics, NOT validated probabilities. **BUY:** none authorized. Numerical baseline/challenger scores are uncalibrated paper-only ranking values, not probabilities or validated improvement.

## Learning and coverage

| Forward horizon | Evidence status | Verified matured / hits |
|---|---|---|
| 1h | PER HORIZON NOT INDEPENDENTLY VERIFIED | NOT VERIFIED |
| 6h | PER HORIZON NOT INDEPENDENTLY VERIFIED | NOT VERIFIED |
| 24h | PER HORIZON NOT INDEPENDENTLY VERIFIED | NOT VERIFIED |
| 48h | PER HORIZON NOT INDEPENDENTLY VERIFIED | NOT VERIFIED |

- Persisted scans: 324; predictions: 3061; observations: 194661.
- Matured sampled outcomes across 1/6/24/48h: 2606; gap abstentions: 8035. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 0 (sampled only; not a success-rate estimate).
- False positives / missed movers: NOT VERIFIED without eligible continuous outcome coverage.
- Baseline vs challenger: recorded as-of; unbiased held-out lift NOT MEASURED.
- Online Kraken /USD stablecoin-base pairs excluded: 18 (counted from this scan's online AssetPairs metadata, not inferred from price).
- Stablecoin base exclusions: BRL1, BUSD, DAI, EUR, EURC, EUROP, EURQ, EURR, EURT, FDUSD, FRAX, GUSD, PYUSD, QCAD, RLUSD, TGBP, TUSD, USD, USD1, USDC, USDD, USDE, USDG, USDQ, USDR, USDS, USDT, ZUSD.
- DEX: NOT USED; no DEX freshness gate.
- OHLC screening abstentions: 12; details in immutable scan JSON artifact.
- Storage: checksum-sealed ledger pushed non-force and read back before this report. Independent artifact recovery is NOT VERIFIED by this scan alone.
- Errors: none in successful committed scan; a failed workflow must not publish a SUCCESS report.
