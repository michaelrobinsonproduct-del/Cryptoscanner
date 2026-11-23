# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-23T10:11:37.051739+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/45153499878
**Source SHA:** 858c8bc8ec5d7641ddb39cacd8aca91719f855b1
**Previous ledger commit:** eb13cd0eb52c3a4e8fd4fc069e15a364f50424ad (atomic ledger/results publication)
**Ledger generation:** 1415 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 6s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 628; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 610; valid market observations: 609; OHLC screened: 24.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | QNT/USD | 151.27 | 97.670 | 81.742 | +5.46% | +0.19% | 3.24x | 6.0 | 2026-11-23T10:11:30.647843+00:00 | Not calibrated | STRONG 94/100 | HIGH 55/100 | Watch | WATCH |
| 2 | KAS/USD | 0.02728 | 93.051 | 72.304 | +5.70% | +1.15% | 5.18x | 3.7 | 2026-11-23T10:11:30.647843+00:00 | Not calibrated | STRONG 100/100 | HIGH 60/100 | Consider small entry | WATCH |
| 3 | ALGO/USD | 0.08028 | 90.440 | 75.751 | +6.43% | -0.06% | 6.62x | 6.2 | 2026-11-23T10:11:30.647843+00:00 | Not calibrated | STRONG 75/100 | HIGH 66/100 | Watch | WATCH |
| 4 | SUI/USD | 0.6705 | 75.218 | 70.054 | +2.26% | +0.51% | 1.26x | 1.5 | 2026-11-23T10:11:30.647843+00:00 | Not calibrated | STRONG 73/100 | HIGH 55/100 | Watch | WATCH |
| 5 | XRP/USD | 0.93873 | 68.370 | 62.913 | +1.21% | +0.46% | 1.31x | 1.1 | 2026-11-23T10:11:30.647843+00:00 | Not calibrated | STRONG 79/100 | HIGH 55/100 | Watch | WATCH |
| 6 | JUP/USD | 0.24349 | 66.736 | 72.637 | +8.43% | +0.28% | 0.27x | 15.2 | 2026-11-23T10:11:30.647843+00:00 | Not calibrated | MODERATE 58/100 | VERY_HIGH 81/100 | Watch | WATCH |
| 7 | SOL/USD | 72.3 | 65.429 | 70.859 | +2.36% | +0.29% | 0.31x | 1.4 | 2026-11-23T10:11:30.647843+00:00 | Not calibrated | MODERATE 63/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 8 | XLM/USD | 0.128623 | 65.301 | 60.120 | +0.86% | +0.24% | 1.40x | 1.1 | 2026-11-23T10:11:30.647843+00:00 | Not calibrated | STRONG 78/100 | HIGH 55/100 | Watch | WATCH |
| 9 | PAXG/USD | 3609.53 | 59.339 | 52.006 | +1.04% | +0.13% | 1.67x | 0.4 | 2026-11-23T10:11:30.647843+00:00 | Not calibrated | MODERATE 65/100 | HIGH 55/100 | Watch | WATCH |
| 10 | XMR/USD | 503.53 | 57.191 | 64.653 | +1.99% | -0.13% | 0.32x | 8.5 | 2026-11-23T10:11:30.647843+00:00 | Not calibrated | WEAK 34/100 | VERY_HIGH 76/100 | Do nothing | WATCH |
| 11 | XBT/USD | 61325.9 | 56.370 | 56.775 | +0.25% | +0.14% | 0.89x | 0.0 | 2026-11-23T10:11:30.647843+00:00 | Not calibrated | MODERATE 48/100 | HIGH 62/100 | Watch | WATCH |
| 12 | TAO/USD | 191.5687 | 51.807 | 45.261 | +0.38% | +0.45% | 1.43x | 4.1 | 2026-11-23T10:11:30.647843+00:00 | Not calibrated | STRONG 71/100 | HIGH 55/100 | Watch | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | QNT/USD | 81.742 | 151.27 | +0.19% | 3.24x |
| 2 | ALGO/USD | 75.751 | 0.08028 | -0.06% | 6.62x |
| 3 | JUP/USD | 72.637 | 0.24349 | +0.28% | 0.27x |
| 4 | KAS/USD | 72.304 | 0.02728 | +1.15% | 5.18x |
| 5 | SOL/USD | 70.859 | 72.3 | +0.29% | 0.31x |
| 6 | SUI/USD | 70.054 | 0.6705 | +0.51% | 1.26x |
| 7 | XMR/USD | 64.653 | 503.53 | -0.13% | 0.32x |
| 8 | XRP/USD | 62.913 | 0.93873 | +0.46% | 1.31x |
| 9 | XLM/USD | 60.120 | 0.128623 | +0.24% | 1.40x |
| 10 | XBT/USD | 56.775 | 61325.9 | +0.14% | 0.89x |
| 11 | PAXG/USD | 52.006 | 3609.53 | +0.13% | 1.67x |
| 12 | TAO/USD | 45.261 | 191.5687 | +0.45% | 1.43x |

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

- Persisted scans: 1415; predictions: 11747; observations: 856838.
- Matured sampled outcomes across 1/6/24/48h: 19323; gap abstentions: 22370. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 130 (sampled only; not a success-rate estimate).
- False positives / missed movers: NOT VERIFIED without eligible continuous outcome coverage.
- Baseline vs challenger: recorded as-of; unbiased held-out lift NOT MEASURED.
- Online Kraken /USD stablecoin-base pairs excluded: 18 (counted from this scan's online AssetPairs metadata, not inferred from price).
- Stablecoin base exclusions: BRL1, BUSD, DAI, EUR, EURC, EUROP, EURQ, EURR, EURT, FDUSD, FRAX, GUSD, PYUSD, QCAD, RLUSD, TGBP, TUSD, USD, USD1, USDC, USDD, USDE, USDG, USDQ, USDR, USDS, USDT, ZUSD.
- DEX: NOT USED; no DEX freshness gate.
- OHLC screening abstentions: 6; details in immutable scan JSON artifact.
- Storage: ledger and results published in one non-force Git commit and read back. Independent artifact recovery is NOT VERIFIED by this scan alone.
- Errors: none in successful committed scan; a failed workflow must not publish a SUCCESS report.

# Cryptoscanner — challenger and independent legacy-inspired WATCH

Paper only · risk is high or higher · 30%+ in 48h probability NOT CALIBRATED
Signal confidence 0–100 means setup strength only, NOT a win probability. Actions are research guidance; no trade authorization.

**Writer:** 45153499878 · **Generation:** 1415 · **Legacy run:** 45153499878
**Main quote time:** 2026-11-23T10:11:37.051739+00:00 · **Legacy report time:** 2026-11-23T10:12:45.018623+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | QNT/USD ⭐ | 151.27 | 97.67 | +0.19% | 3.24x | STRONG 100/100 | HIGH 55/100 | Watch |
| 2 | KAS/USD ⭐ | 0.02728 | 93.05 | +1.15% | 5.18x | STRONG 100/100 | HIGH 60/100 | Consider small entry |
| 3 | ALGO/USD | 0.08028 | 90.44 | -0.06% | 6.62x | STRONG 75/100 | HIGH 66/100 | Watch |
| 4 | SUI/USD ⭐ | 0.6705 | 75.22 | +0.51% | 1.26x | STRONG 83/100 | HIGH 55/100 | Watch |
| 5 | XRP/USD ⭐ | 0.93873 | 68.37 | +0.46% | 1.31x | STRONG 89/100 | HIGH 55/100 | Watch |
| 6 | JUP/USD | 0.24349 | 66.74 | +0.28% | 0.27x | MODERATE 58/100 | VERY_HIGH 81/100 | Watch |
| 7 | SOL/USD | 72.3 | 65.43 | +0.29% | 0.31x | MODERATE 63/100 | VERY_HIGH 70/100 | Watch |
| 8 | XLM/USD | 0.128623 | 65.30 | +0.24% | 1.40x | STRONG 78/100 | HIGH 55/100 | Watch |
| 9 | PAXG/USD | 3609.53 | 59.34 | +0.13% | 1.67x | MODERATE 65/100 | HIGH 55/100 | Watch |
| 10 | XMR/USD | 503.53 | 57.19 | -0.13% | 0.32x | WEAK 34/100 | VERY_HIGH 76/100 | Do nothing |
| 11 | XBT/USD | 61325.9 | 56.37 | +0.14% | 0.89x | MODERATE 48/100 | HIGH 62/100 | Watch |
| 12 | TAO/USD | 191.5687 | 51.81 | +0.45% | 1.43x | STRONG 71/100 | HIGH 55/100 | Watch |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | QNT/USD ⭐ | 151.12 | 88.93 | +0.19% | 3.24x | 5035 | STRONG 99/100 | HIGH 55/100 | Watch |
| 2 | KAS/USD ⭐ | 0.02724 | 84.33 | +1.15% | 5.18x | 3157 | STRONG 100/100 | HIGH 60/100 | Consider small entry |
| 3 | SUI/USD ⭐ | 0.6705 | 78.68 | +0.51% | 1.26x | 5984 | STRONG 84/100 | HIGH 55/100 | Watch |
| 4 | XRP/USD ⭐ | 0.93999 | 69.48 | +0.46% | 1.31x | 20579 | STRONG 90/100 | HIGH 55/100 | Watch |

**Same-run overlap:** QNT/USD, KAS/USD, SUI/USD, XRP/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
