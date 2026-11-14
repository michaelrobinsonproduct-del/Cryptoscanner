# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-14T01:31:32.032025+00:00
**GitHub trigger:** authenticated on-demand scan request (verified event=push; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/43541053044
**Source SHA:** e7462a31b5b0cb5b8afacce793c41be26d1db48d
**Previous ledger commit:** 268494c0b008a1707c968e2f9143f2ddc62622d8 (atomic ledger/results publication)
**Ledger generation:** 376 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 7s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 625; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 607; valid market observations: 607; OHLC screened: 19.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | NIGHT/USD | 0.04734 | 77.326 | 54.821 | +0.98% | +1.50% | 5.86x | 6.3 | 2026-11-14T01:31:25.199114+00:00 | Not calibrated | STRONG 94/100 | HIGH 55/100 | Consider small entry | WATCH |
| 2 | TAO/USD | 216.1862 | 56.165 | 56.356 | +0.72% | +0.22% | 0.87x | 7.3 | 2026-11-14T01:31:25.199114+00:00 | Not calibrated | MODERATE 58/100 | HIGH 62/100 | Watch | WATCH |
| 3 | RENDER/USD | 1.539 | 51.575 | 34.623 | +0.39% | +0.39% | 4.37x | 6.5 | 2026-11-14T01:31:25.199114+00:00 | Not calibrated | STRONG 81/100 | HIGH 60/100 | Watch | WATCH |
| 4 | MON/USD | 0.01688 | 51.296 | 35.106 | +0.78% | +0.24% | 9.30x | 5.9 | 2026-11-14T01:31:25.199114+00:00 | Not calibrated | STRONG 81/100 | HIGH 60/100 | Watch | WATCH |
| 5 | AERO/USD | 0.471 | 29.368 | 28.770 | +0.38% | +0.32% | 0.90x | 19.1 | 2026-11-14T01:31:25.199114+00:00 | Not calibrated | WEAK 40/100 | VERY_HIGH 73/100 | Watch | WATCH |
| 6 | PYTH/USD | 0.06431 | 22.157 | 28.895 | +0.30% | +0.33% | 0.16x | 10.9 | 2026-11-14T01:31:25.199114+00:00 | Not calibrated | WEAK 36/100 | VERY_HIGH 81/100 | Watch | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | TAO/USD | 56.356 | 216.1862 | +0.22% | 0.87x |
| 2 | NIGHT/USD | 54.821 | 0.04734 | +1.50% | 5.86x |
| 3 | MON/USD | 35.106 | 0.01688 | +0.24% | 9.30x |
| 4 | RENDER/USD | 34.623 | 1.539 | +0.39% | 4.37x |
| 5 | PYTH/USD | 28.895 | 0.06431 | +0.33% | 0.16x |
| 6 | AERO/USD | 28.770 | 0.471 | +0.32% | 0.90x |

The baseline ordering is over this same confirmed WATCH pool, not an independent full-market baseline scan.
The separate legacy-inspired scanner publishes its own WATCH signals in a later, read-only GitHub artifact linked by this paper run ID.

**30%+ in 48h probability:** NOT CALIBRATED. The separate signal-confidence index (0–100) expresses current setup strength, NOT odds of a gain. Risk varies by spread, momentum and volume; every candidate remains speculative. The action is a research consideration, not an executed or authorized trade. A more substantial entry requires independently qualified held-out calibration.

## Learning and coverage

| Forward horizon | Evidence status | Verified matured / hits |
|---|---|---|
| 1h | PER HORIZON NOT INDEPENDENTLY VERIFIED | NOT VERIFIED |
| 6h | PER HORIZON NOT INDEPENDENTLY VERIFIED | NOT VERIFIED |
| 24h | PER HORIZON NOT INDEPENDENTLY VERIFIED | NOT VERIFIED |
| 48h | PER HORIZON NOT INDEPENDENTLY VERIFIED | NOT VERIFIED |

- Persisted scans: 376; predictions: 3457; observations: 226187.
- Matured sampled outcomes across 1/6/24/48h: 2951; gap abstentions: 9973. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 0 (sampled only; not a success-rate estimate).
- False positives / missed movers: NOT VERIFIED without eligible continuous outcome coverage.
- Baseline vs challenger: recorded as-of; unbiased held-out lift NOT MEASURED.
- Online Kraken /USD stablecoin-base pairs excluded: 18 (counted from this scan's online AssetPairs metadata, not inferred from price).
- Stablecoin base exclusions: BRL1, BUSD, DAI, EUR, EURC, EUROP, EURQ, EURR, EURT, FDUSD, FRAX, GUSD, PYUSD, QCAD, RLUSD, TGBP, TUSD, USD, USD1, USDC, USDD, USDE, USDG, USDQ, USDR, USDS, USDT, ZUSD.
- DEX: NOT USED; no DEX freshness gate.
- OHLC screening abstentions: 13; details in immutable scan JSON artifact.
- Storage: ledger and results published in one non-force Git commit and read back. Independent artifact recovery is NOT VERIFIED by this scan alone.
- Errors: none in successful committed scan; a failed workflow must not publish a SUCCESS report.
