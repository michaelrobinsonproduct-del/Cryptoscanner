# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-12T16:05:15.113302+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/43254219005
**Source SHA:** 21b4cf643df9f7a7adfddc959660920dd467c70b
**Ledger commit:** e67435399d3a064bb3ad659ac785ba57922b23b0
**Ledger generation:** 336 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 4s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 624; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 606; valid market observations: 606; OHLC screened: 10.

## Top WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | Confidence / risk | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---|---|---|
| 1 | TON/USD | 1.282 | 109.658 | 85.928 | +9.29% | +1.75% | 3.34x | 7.8 | 2026-11-12T16:05:11.480851+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 2 | TIA/USD | 0.4202 | 54.467 | 42.548 | +1.40% | +1.67% | 1.36x | 7.1 | 2026-11-12T16:05:11.480851+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 3 | XDC/USD | 0.02937 | 52.403 | 39.606 | +1.07% | -0.44% | 5.91x | 17.0 | 2026-11-12T16:05:11.480851+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 4 | CAP/USD | 0.102199 | 49.079 | 34.660 | +1.72% | -0.12% | 2.70x | 17.2 | 2026-11-12T16:05:11.480851+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 5 | ATOM/USD | 1.413 | 46.966 | 35.551 | +1.40% | +1.24% | 1.52x | 12.7 | 2026-11-12T16:05:11.480851+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 6 | MON/USD | 0.01699 | 45.745 | 41.181 | +1.98% | +1.07% | 0.92x | 11.8 | 2026-11-12T16:05:11.480851+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 7 | MEGA/USD | 0.04589 | 34.253 | 40.175 | +2.43% | +0.46% | 0.18x | 17.4 | 2026-11-12T16:05:11.480851+00:00 | NOT CALIBRATED / HIGH | WATCH |

**Confidence:** uncalibrated research heuristics, NOT validated probabilities. **BUY:** none authorized. Numerical baseline/challenger scores are uncalibrated paper-only ranking values, not probabilities or validated improvement.

## Learning and coverage

| Forward horizon | Evidence status | Verified matured / hits |
|---|---|---|
| 1h | PER HORIZON NOT INDEPENDENTLY VERIFIED | NOT VERIFIED |
| 6h | PER HORIZON NOT INDEPENDENTLY VERIFIED | NOT VERIFIED |
| 24h | PER HORIZON NOT INDEPENDENTLY VERIFIED | NOT VERIFIED |
| 48h | PER HORIZON NOT INDEPENDENTLY VERIFIED | NOT VERIFIED |

- Persisted scans: 336; predictions: 3131; observations: 201932.
- Matured sampled outcomes across 1/6/24/48h: 2754; gap abstentions: 8256. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 0 (sampled only; not a success-rate estimate).
- False positives / missed movers: NOT VERIFIED without eligible continuous outcome coverage.
- Baseline vs challenger: recorded as-of; unbiased held-out lift NOT MEASURED.
- Online Kraken /USD stablecoin-base pairs excluded: 18 (counted from this scan's online AssetPairs metadata, not inferred from price).
- Stablecoin base exclusions: BRL1, BUSD, DAI, EUR, EURC, EUROP, EURQ, EURR, EURT, FDUSD, FRAX, GUSD, PYUSD, QCAD, RLUSD, TGBP, TUSD, USD, USD1, USDC, USDD, USDE, USDG, USDQ, USDR, USDS, USDT, ZUSD.
- DEX: NOT USED; no DEX freshness gate.
- OHLC screening abstentions: 3; details in immutable scan JSON artifact.
- Storage: checksum-sealed ledger pushed non-force and read back before this report. Independent artifact recovery is NOT VERIFIED by this scan alone.
- Errors: none in successful committed scan; a failed workflow must not publish a SUCCESS report.
