# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-14T01:00:37.654797+00:00
**GitHub trigger:** authenticated on-demand scan request (verified event=push; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/43537815748
**Source SHA:** d68328b2c0a55df9b3bdf614249d4207261093eb
**Previous ledger commit:** ecce6d00ac4c9d7dd32126c54958d0935c3685fe (atomic ledger/results publication)
**Ledger generation:** 374 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 5s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 625; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 607; valid market observations: 607; OHLC screened: 16.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | Confidence / risk | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---|---|---|
| 1 | BERA/USD | 0.1244 | 58.321 | 55.845 | +8.46% | -0.88% | 1.69x | 40.2 | 2026-11-14T01:00:32.265955+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 2 | PEPE/USD | 4.421e-06 | 52.573 | 56.411 | +0.36% | -0.47% | 0.85x | 2.3 | 2026-11-14T01:00:32.265955+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 3 | TAO/USD | 216.4195 | 51.636 | 56.437 | +0.83% | +0.68% | 0.18x | 8.7 | 2026-11-14T01:00:32.265955+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 4 | RENDER/USD | 1.538 | 47.901 | 30.615 | +0.33% | +0.46% | 3.39x | 13.0 | 2026-11-14T01:00:32.265955+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 5 | MON/USD | 0.01684 | 24.744 | 30.324 | +0.54% | +0.54% | 0.17x | 11.9 | 2026-11-14T01:00:32.265955+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 6 | DASH/USD | 41.298 | 24.017 | 29.238 | +0.43% | +0.38% | 0.29x | 13.8 | 2026-11-14T01:00:32.265955+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 7 | AERO/USD | 0.4709 | 16.996 | 26.497 | +0.36% | -0.34% | 0.22x | 23.4 | 2026-11-14T01:00:32.265955+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 8 | A/USD | 0.0707 | 16.262 | 18.687 | +0.28% | +0.00% | 0.76x | 28.4 | 2026-11-14T01:00:32.265955+00:00 | NOT CALIBRATED / HIGH | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | TAO/USD | 56.437 | 216.4195 | +0.68% | 0.18x |
| 2 | PEPE/USD | 56.411 | 4.421e-06 | -0.47% | 0.85x |
| 3 | BERA/USD | 55.845 | 0.1244 | -0.88% | 1.69x |
| 4 | RENDER/USD | 30.615 | 1.538 | +0.46% | 3.39x |
| 5 | MON/USD | 30.324 | 0.01684 | +0.54% | 0.17x |
| 6 | DASH/USD | 29.238 | 41.298 | +0.38% | 0.29x |
| 7 | AERO/USD | 26.497 | 0.4709 | -0.34% | 0.22x |
| 8 | A/USD | 18.687 | 0.0707 | +0.00% | 0.76x |

The baseline ordering is over this same confirmed WATCH pool, not an independent full-market baseline scan.
The separate legacy-inspired scanner publishes its own WATCH signals in a later, read-only GitHub artifact linked by this paper run ID.

**Confidence:** uncalibrated research heuristics, NOT validated probabilities. **BUY:** none authorized. Numerical baseline/challenger scores are uncalibrated paper-only ranking values, not probabilities or validated improvement.

## Learning and coverage

| Forward horizon | Evidence status | Verified matured / hits |
|---|---|---|
| 1h | PER HORIZON NOT INDEPENDENTLY VERIFIED | NOT VERIFIED |
| 6h | PER HORIZON NOT INDEPENDENTLY VERIFIED | NOT VERIFIED |
| 24h | PER HORIZON NOT INDEPENDENTLY VERIFIED | NOT VERIFIED |
| 48h | PER HORIZON NOT INDEPENDENTLY VERIFIED | NOT VERIFIED |

- Persisted scans: 374; predictions: 3446; observations: 224973.
- Matured sampled outcomes across 1/6/24/48h: 2946; gap abstentions: 9945. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 0 (sampled only; not a success-rate estimate).
- False positives / missed movers: NOT VERIFIED without eligible continuous outcome coverage.
- Baseline vs challenger: recorded as-of; unbiased held-out lift NOT MEASURED.
- Online Kraken /USD stablecoin-base pairs excluded: 18 (counted from this scan's online AssetPairs metadata, not inferred from price).
- Stablecoin base exclusions: BRL1, BUSD, DAI, EUR, EURC, EUROP, EURQ, EURR, EURT, FDUSD, FRAX, GUSD, PYUSD, QCAD, RLUSD, TGBP, TUSD, USD, USD1, USDC, USDD, USDE, USDG, USDQ, USDR, USDS, USDT, ZUSD.
- DEX: NOT USED; no DEX freshness gate.
- OHLC screening abstentions: 8; details in immutable scan JSON artifact.
- Storage: ledger and results published in one non-force Git commit and read back. Independent artifact recovery is NOT VERIFIED by this scan alone.
- Errors: none in successful committed scan; a failed workflow must not publish a SUCCESS report.
