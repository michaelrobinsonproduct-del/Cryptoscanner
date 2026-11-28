# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-28T08:47:43.751362+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/46127217293
**Source SHA:** 858c8bc8ec5d7641ddb39cacd8aca91719f855b1
**Previous ledger commit:** 57735d7f4474bb45f2043a6e950477668820b0bb (atomic ledger/results publication)
**Ledger generation:** 2131 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 5s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 628; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 610; valid market observations: 606; OHLC screened: 13.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | XMR/USD | 428.88 | 86.263 | 70.008 | +5.31% | +0.25% | 4.37x | 44.3 | 2026-11-28T08:47:39.104987+00:00 | Not calibrated | STRONG 83/100 | VERY_HIGH 77/100 | Watch | WATCH |
| 2 | NIGHT/USD | 0.0512 | 80.628 | 66.422 | +1.91% | +0.18% | 2.33x | 3.9 | 2026-11-28T08:47:39.104987+00:00 | Not calibrated | STRONG 85/100 | HIGH 55/100 | Watch | WATCH |
| 3 | VVV/USD | 26.366 | 49.770 | 57.842 | +2.40% | -1.22% | 0.80x | 6.8 | 2026-11-28T08:47:39.104987+00:00 | Not calibrated | WEAK 30/100 | VERY_HIGH 72/100 | Do nothing | WATCH |
| 4 | SPACE/USD | 0.004387 | 46.780 | 61.164 | +5.00% | -1.48% | 0.30x | 9.1 | 2026-11-28T08:47:39.104987+00:00 | Not calibrated | WEAK 28/100 | EXTREME 92/100 | Do nothing | WATCH |
| 5 | AKE/USD | 0.00110693 | 35.001 | 34.396 | +1.88% | +0.65% | 0.74x | 29.7 | 2026-11-28T08:47:39.104987+00:00 | Not calibrated | WEAK 38/100 | EXTREME 87/100 | Do nothing | WATCH |
| 6 | KAVA/USD | 0.0277 | 7.016 | 24.007 | +1.47% | -1.79% | 0.19x | 36.1 | 2026-11-28T08:47:39.104987+00:00 | Not calibrated | WEAK 0/100 | EXTREME 97/100 | Do nothing | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | XMR/USD | 70.008 | 428.88 | +0.25% | 4.37x |
| 2 | NIGHT/USD | 66.422 | 0.0512 | +0.18% | 2.33x |
| 3 | SPACE/USD | 61.164 | 0.004387 | -1.48% | 0.30x |
| 4 | VVV/USD | 57.842 | 26.366 | -1.22% | 0.80x |
| 5 | AKE/USD | 34.396 | 0.00110693 | +0.65% | 0.74x |
| 6 | KAVA/USD | 24.007 | 0.0277 | -1.79% | 0.19x |

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

- Persisted scans: 2131; predictions: 19067; observations: 1290432.
- Matured sampled outcomes across 1/6/24/48h: 44970; gap abstentions: 25968. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 155 (sampled only; not a success-rate estimate).
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

**Writer:** 46127217293 · **Generation:** 2131 · **Legacy run:** 46127217293
**Main quote time:** 2026-11-28T08:47:43.751362+00:00 · **Legacy report time:** 2026-11-28T08:48:31.979179+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | XMR/USD ⭐ | 428.88 | 86.26 | +0.25% | 4.37x | STRONG 93/100 | VERY_HIGH 77/100 | Watch |
| 2 | NIGHT/USD ⭐ | 0.0512 | 80.63 | +0.18% | 2.33x | STRONG 95/100 | HIGH 55/100 | Watch |
| 3 | VVV/USD | 26.366 | 49.77 | -1.22% | 0.80x | WEAK 30/100 | VERY_HIGH 72/100 | Do nothing |
| 4 | SPACE/USD | 0.004387 | 46.78 | -1.48% | 0.30x | WEAK 28/100 | EXTREME 92/100 | Do nothing |
| 5 | AKE/USD | 0.00110693 | 35.00 | +0.65% | 0.74x | WEAK 38/100 | EXTREME 87/100 | Do nothing |
| 6 | KAVA/USD | 0.0277 | 7.02 | -1.79% | 0.19x | WEAK 0/100 | EXTREME 97/100 | Do nothing |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | XMR/USD ⭐ | 429.47 | 93.75 | +0.25% | 4.37x | 15106 | STRONG 100/100 | HIGH 67/100 | Consider small entry |
| 2 | NIGHT/USD ⭐ | 0.05117 | 65.07 | +0.18% | 2.33x | 19187 | STRONG 88/100 | HIGH 55/100 | Watch |

**Same-run overlap:** XMR/USD, NIGHT/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
