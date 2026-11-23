# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-23T22:32:06.220274+00:00
**GitHub trigger:** scheduled (verified event=schedule; originating cron=2,7,12,17,22,27,32,37,42,47,52,57 * * * *, intended UTC minute=2,7,12,17,22,27,32,37,42,47,52,57; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/45279953167
**Source SHA:** 858c8bc8ec5d7641ddb39cacd8aca91719f855b1
**Previous ledger commit:** 35c5c61f3d60308e8a87535d844993bb3d67d7cc (atomic ledger/results publication)
**Ledger generation:** 1490 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 9s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 628; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 610; valid market observations: 609; OHLC screened: 24.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | QNT/USD | 155.69 | 108.383 | 97.112 | +8.54% | -0.75% | 3.78x | 5.8 | 2026-11-23T22:31:57.545286+00:00 | Not calibrated | STRONG 80/100 | HIGH 61/100 | Watch | WATCH |
| 2 | SHX/USD | 0.003613 | 86.788 | 74.961 | +7.05% | -0.63% | 3.07x | 2.8 | 2026-11-23T22:31:57.545286+00:00 | Not calibrated | STRONG 73/100 | VERY_HIGH 73/100 | Watch | WATCH |
| 3 | ALGO/USD | 0.08084 | 83.933 | 91.092 | +7.17% | -0.55% | 0.56x | 7.4 | 2026-11-23T22:31:57.545286+00:00 | Not calibrated | MODERATE 47/100 | VERY_HIGH 76/100 | Watch | WATCH |
| 4 | CAP/USD | 0.101894 | 82.356 | 76.152 | +8.89% | -1.76% | 3.56x | 6.1 | 2026-11-23T22:31:57.545286+00:00 | Not calibrated | STRONG 71/100 | VERY_HIGH 70/100 | Do nothing | WATCH |
| 5 | LTC/USD | 41.14 | 73.625 | 70.866 | +2.44% | -0.29% | 1.42x | 2.4 | 2026-11-23T22:31:57.545286+00:00 | Not calibrated | MODERATE 57/100 | HIGH 61/100 | Watch | WATCH |
| 6 | XDG/USD | 0.0562504 | 72.636 | 67.230 | +1.75% | -0.32% | 1.70x | 0.0 | 2026-11-23T22:31:57.545286+00:00 | Not calibrated | MODERATE 56/100 | HIGH 61/100 | Watch | WATCH |
| 7 | ATOM/USD | 1.2505 | 71.494 | 71.658 | +6.70% | -0.21% | 1.09x | 12.8 | 2026-11-23T22:31:57.545286+00:00 | Not calibrated | WEAK 41/100 | VERY_HIGH 79/100 | Watch | WATCH |
| 8 | XRP/USD | 0.9378 | 70.710 | 62.636 | +1.11% | -0.22% | 1.92x | 0.2 | 2026-11-23T22:31:57.545286+00:00 | Not calibrated | MODERATE 55/100 | HIGH 61/100 | Watch | WATCH |
| 9 | WINGS/USD | 0.002061 | 66.077 | 72.496 | +7.96% | -0.39% | 0.55x | 9.6 | 2026-11-23T22:31:57.545286+00:00 | Not calibrated | WEAK 38/100 | VERY_HIGH 81/100 | Watch | WATCH |
| 10 | SOL/USD | 72.16 | 63.874 | 69.470 | +2.17% | -0.06% | 0.47x | 1.4 | 2026-11-23T22:31:57.545286+00:00 | Not calibrated | WEAK 37/100 | VERY_HIGH 76/100 | Watch | WATCH |
| 11 | SUI/USD | 0.6693 | 62.394 | 68.772 | +2.07% | -0.45% | 0.59x | 1.5 | 2026-11-23T22:31:57.545286+00:00 | Not calibrated | WEAK 36/100 | VERY_HIGH 76/100 | Watch | WATCH |
| 12 | CC/USD | 0.07697 | 61.106 | 69.728 | +5.05% | -0.40% | 0.34x | 3.9 | 2026-11-23T22:31:57.545286+00:00 | Not calibrated | WEAK 36/100 | VERY_HIGH 81/100 | Watch | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | QNT/USD | 97.112 | 155.69 | -0.75% | 3.78x |
| 2 | ALGO/USD | 91.092 | 0.08084 | -0.55% | 0.56x |
| 3 | CAP/USD | 76.152 | 0.101894 | -1.76% | 3.56x |
| 4 | SHX/USD | 74.961 | 0.003613 | -0.63% | 3.07x |
| 5 | WINGS/USD | 72.496 | 0.002061 | -0.39% | 0.55x |
| 6 | ATOM/USD | 71.658 | 1.2505 | -0.21% | 1.09x |
| 7 | LTC/USD | 70.866 | 41.14 | -0.29% | 1.42x |
| 8 | CC/USD | 69.728 | 0.07697 | -0.40% | 0.34x |
| 9 | SOL/USD | 69.470 | 72.16 | -0.06% | 0.47x |
| 10 | SUI/USD | 68.772 | 0.6693 | -0.45% | 0.59x |
| 11 | XDG/USD | 67.230 | 0.0562504 | -0.32% | 1.70x |
| 12 | XRP/USD | 62.636 | 0.9378 | -0.22% | 1.92x |

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

- Persisted scans: 1490; predictions: 12647; observations: 902512.
- Matured sampled outcomes across 1/6/24/48h: 22876; gap abstentions: 22370. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 131 (sampled only; not a success-rate estimate).
- False positives / missed movers: NOT VERIFIED without eligible continuous outcome coverage.
- Baseline vs challenger: recorded as-of; unbiased held-out lift NOT MEASURED.
- Online Kraken /USD stablecoin-base pairs excluded: 18 (counted from this scan's online AssetPairs metadata, not inferred from price).
- Stablecoin base exclusions: BRL1, BUSD, DAI, EUR, EURC, EUROP, EURQ, EURR, EURT, FDUSD, FRAX, GUSD, PYUSD, QCAD, RLUSD, TGBP, TUSD, USD, USD1, USDC, USDD, USDE, USDG, USDQ, USDR, USDS, USDT, ZUSD.
- DEX: NOT USED; no DEX freshness gate.
- OHLC screening abstentions: 7; details in immutable scan JSON artifact.
- Storage: ledger and results published in one non-force Git commit and read back. Independent artifact recovery is NOT VERIFIED by this scan alone.
- Errors: none in successful committed scan; a failed workflow must not publish a SUCCESS report.

# Cryptoscanner — challenger and independent legacy-inspired WATCH

Paper only · risk is high or higher · 30%+ in 48h probability NOT CALIBRATED
Signal confidence 0–100 means setup strength only, NOT a win probability. Actions are research guidance; no trade authorization.

**Writer:** 45279953167 · **Generation:** 1490 · **Legacy run:** 45279953167
**Main quote time:** 2026-11-23T22:32:06.220274+00:00 · **Legacy report time:** 2026-11-23T22:33:17.259232+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | QNT/USD | 155.69 | 108.38 | -0.75% | 3.78x | STRONG 80/100 | HIGH 61/100 | Watch |
| 2 | SHX/USD | 0.003613 | 86.79 | -0.63% | 3.07x | STRONG 73/100 | VERY_HIGH 73/100 | Watch |
| 3 | ALGO/USD | 0.08084 | 83.93 | -0.55% | 0.56x | MODERATE 47/100 | VERY_HIGH 76/100 | Watch |
| 4 | CAP/USD | 0.101894 | 82.36 | -1.76% | 3.56x | STRONG 71/100 | VERY_HIGH 70/100 | Do nothing |
| 5 | LTC/USD | 41.14 | 73.62 | -0.29% | 1.42x | MODERATE 57/100 | HIGH 61/100 | Watch |
| 6 | XDG/USD | 0.0562504 | 72.64 | -0.32% | 1.70x | MODERATE 56/100 | HIGH 61/100 | Watch |
| 7 | ATOM/USD | 1.2505 | 71.49 | -0.21% | 1.09x | WEAK 41/100 | VERY_HIGH 79/100 | Watch |
| 8 | XRP/USD | 0.9378 | 70.71 | -0.22% | 1.92x | MODERATE 55/100 | HIGH 61/100 | Watch |
| 9 | WINGS/USD | 0.002061 | 66.08 | -0.39% | 0.55x | WEAK 38/100 | VERY_HIGH 81/100 | Watch |
| 10 | SOL/USD | 72.16 | 63.87 | -0.06% | 0.47x | WEAK 37/100 | VERY_HIGH 76/100 | Watch |
| 11 | SUI/USD | 0.6693 | 62.39 | -0.45% | 0.59x | WEAK 36/100 | VERY_HIGH 76/100 | Watch |
| 12 | CC/USD | 0.07697 | 61.11 | -0.40% | 0.34x | WEAK 36/100 | VERY_HIGH 81/100 | Watch |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| — | No confirmed WATCH signals | — | — | — | — | — | — | — | — |

**Same-run overlap:** None
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
