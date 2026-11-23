# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-23T10:51:40.584043+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/45159598541
**Source SHA:** 858c8bc8ec5d7641ddb39cacd8aca91719f855b1
**Previous ledger commit:** 3b21c92ff87a67684a2c4c733fd567cefcb9ec17 (atomic ledger/results publication)
**Ledger generation:** 1419 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 9s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 628; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 610; valid market observations: 609; OHLC screened: 24.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | QNT/USD | 153.41 | 85.891 | 85.084 | +6.95% | +1.75% | 0.21x | 13.7 | 2026-11-23T10:51:31.761740+00:00 | Not calibrated | MODERATE 68/100 | VERY_HIGH 76/100 | Watch | WATCH |
| 2 | XMR/USD | 503.84 | 79.080 | 64.695 | +2.05% | -0.12% | 4.95x | 9.3 | 2026-11-23T10:51:31.761740+00:00 | Not calibrated | STRONG 70/100 | HIGH 61/100 | Watch | WATCH |
| 3 | SOL/USD | 72.38 | 77.978 | 71.653 | +2.48% | +0.19% | 1.54x | 1.4 | 2026-11-23T10:51:31.761740+00:00 | Not calibrated | STRONG 74/100 | HIGH 55/100 | Watch | WATCH |
| 4 | ALGO/USD | 0.08084 | 68.479 | 75.892 | +7.17% | -0.17% | 0.35x | 6.2 | 2026-11-23T10:51:31.761740+00:00 | Not calibrated | WEAK 39/100 | VERY_HIGH 81/100 | Watch | WATCH |
| 5 | XRP/USD | 0.94026 | 68.146 | 64.546 | +1.37% | +0.13% | 1.30x | 0.1 | 2026-11-23T10:51:31.761740+00:00 | Not calibrated | MODERATE 59/100 | HIGH 55/100 | Watch | WATCH |
| 6 | JUP/USD | 0.24059 | 67.304 | 73.331 | +7.13% | -0.18% | 0.49x | 13.7 | 2026-11-23T10:51:31.761740+00:00 | Not calibrated | WEAK 34/100 | EXTREME 87/100 | Do nothing | WATCH |
| 7 | XDG/USD | 0.0555533 | 65.917 | 49.618 | +0.49% | +0.26% | 2.77x | 0.5 | 2026-11-23T10:51:31.761740+00:00 | Not calibrated | STRONG 88/100 | HIGH 55/100 | Watch | WATCH |
| 8 | XLM/USD | 0.128938 | 64.689 | 62.112 | +1.11% | +0.30% | 1.11x | 0.1 | 2026-11-23T10:51:31.761740+00:00 | Not calibrated | MODERATE 67/100 | HIGH 62/100 | Watch | WATCH |
| 9 | SUI/USD | 0.67 | 62.343 | 69.520 | +2.18% | +0.39% | 0.09x | 1.5 | 2026-11-23T10:51:31.761740+00:00 | Not calibrated | MODERATE 61/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 10 | PENGU/USD | 0.00435 | 61.674 | 45.177 | +2.02% | +0.30% | 2.59x | 2.3 | 2026-11-23T10:51:31.761740+00:00 | Not calibrated | STRONG 86/100 | HIGH 60/100 | Watch | WATCH |
| 11 | HYPE/USD | 64.17 | 61.294 | 66.542 | +1.76% | +0.28% | 0.33x | 1.6 | 2026-11-23T10:51:31.761740+00:00 | Not calibrated | MODERATE 61/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 12 | INJ/USD | 6.467 | 60.532 | 61.051 | +3.84% | +0.55% | 0.68x | 12.4 | 2026-11-23T10:51:31.761740+00:00 | Not calibrated | MODERATE 55/100 | VERY_HIGH 76/100 | Watch | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | QNT/USD | 85.084 | 153.41 | +1.75% | 0.21x |
| 2 | ALGO/USD | 75.892 | 0.08084 | -0.17% | 0.35x |
| 3 | JUP/USD | 73.331 | 0.24059 | -0.18% | 0.49x |
| 4 | SOL/USD | 71.653 | 72.38 | +0.19% | 1.54x |
| 5 | SUI/USD | 69.520 | 0.67 | +0.39% | 0.09x |
| 6 | HYPE/USD | 66.542 | 64.17 | +0.28% | 0.33x |
| 7 | XMR/USD | 64.695 | 503.84 | -0.12% | 4.95x |
| 8 | XRP/USD | 64.546 | 0.94026 | +0.13% | 1.30x |
| 9 | XLM/USD | 62.112 | 0.128938 | +0.30% | 1.11x |
| 10 | INJ/USD | 61.051 | 6.467 | +0.55% | 0.68x |
| 11 | XDG/USD | 49.618 | 0.0555533 | +0.26% | 2.77x |
| 12 | PENGU/USD | 45.177 | 0.00435 | +0.30% | 2.59x |

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

- Persisted scans: 1419; predictions: 11795; observations: 859274.
- Matured sampled outcomes across 1/6/24/48h: 19495; gap abstentions: 22370. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 131 (sampled only; not a success-rate estimate).
- False positives / missed movers: NOT VERIFIED without eligible continuous outcome coverage.
- Baseline vs challenger: recorded as-of; unbiased held-out lift NOT MEASURED.
- Online Kraken /USD stablecoin-base pairs excluded: 18 (counted from this scan's online AssetPairs metadata, not inferred from price).
- Stablecoin base exclusions: BRL1, BUSD, DAI, EUR, EURC, EUROP, EURQ, EURR, EURT, FDUSD, FRAX, GUSD, PYUSD, QCAD, RLUSD, TGBP, TUSD, USD, USD1, USDC, USDD, USDE, USDG, USDQ, USDR, USDS, USDT, ZUSD.
- DEX: NOT USED; no DEX freshness gate.
- OHLC screening abstentions: 4; details in immutable scan JSON artifact.
- Storage: ledger and results published in one non-force Git commit and read back. Independent artifact recovery is NOT VERIFIED by this scan alone.
- Errors: none in successful committed scan; a failed workflow must not publish a SUCCESS report.

# Cryptoscanner — challenger and independent legacy-inspired WATCH

Paper only · risk is high or higher · 30%+ in 48h probability NOT CALIBRATED
Signal confidence 0–100 means setup strength only, NOT a win probability. Actions are research guidance; no trade authorization.

**Writer:** 45159598541 · **Generation:** 1419 · **Legacy run:** 45159598541
**Main quote time:** 2026-11-23T10:51:40.584043+00:00 · **Legacy report time:** 2026-11-23T10:52:38.448277+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | QNT/USD | 153.41 | 85.89 | +1.75% | 0.21x | MODERATE 68/100 | VERY_HIGH 76/100 | Watch |
| 2 | XMR/USD | 503.84 | 79.08 | -0.12% | 4.95x | STRONG 70/100 | HIGH 61/100 | Watch |
| 3 | SOL/USD ⭐ | 72.38 | 77.98 | +0.19% | 1.54x | STRONG 84/100 | HIGH 55/100 | Watch |
| 4 | ALGO/USD | 0.08084 | 68.48 | -0.17% | 0.35x | WEAK 39/100 | VERY_HIGH 81/100 | Watch |
| 5 | XRP/USD ⭐ | 0.94026 | 68.15 | +0.13% | 1.30x | MODERATE 69/100 | HIGH 55/100 | Watch |
| 6 | JUP/USD | 0.24059 | 67.30 | -0.18% | 0.49x | WEAK 34/100 | EXTREME 87/100 | Do nothing |
| 7 | XDG/USD | 0.0555533 | 65.92 | +0.26% | 2.77x | STRONG 88/100 | HIGH 55/100 | Watch |
| 8 | XLM/USD ⭐ | 0.128938 | 64.69 | +0.30% | 1.11x | STRONG 77/100 | HIGH 62/100 | Watch |
| 9 | SUI/USD | 0.67 | 62.34 | +0.39% | 0.09x | MODERATE 61/100 | VERY_HIGH 70/100 | Watch |
| 10 | PENGU/USD | 0.00435 | 61.67 | +0.30% | 2.59x | STRONG 86/100 | HIGH 60/100 | Watch |
| 11 | HYPE/USD | 64.17 | 61.29 | +0.28% | 0.33x | MODERATE 61/100 | VERY_HIGH 70/100 | Watch |
| 12 | INJ/USD | 6.467 | 60.53 | +0.55% | 0.68x | MODERATE 55/100 | VERY_HIGH 76/100 | Watch |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | SOL/USD ⭐ | 72.39 | 81.86 | +0.19% | 1.54x | 29645 | STRONG 86/100 | HIGH 55/100 | Watch |
| 2 | XRP/USD ⭐ | 0.93989 | 67.42 | +0.13% | 1.30x | 20548 | MODERATE 69/100 | HIGH 55/100 | Watch |
| 3 | XLM/USD ⭐ | 0.128923 | 65.96 | +0.30% | 1.11x | 11453 | STRONG 78/100 | HIGH 62/100 | Watch |

**Same-run overlap:** SOL/USD, XRP/USD, XLM/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
