# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-17T23:10:03.886738+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/44196847213
**Source SHA:** e9b1b6ee47d56a43a454042547735fcd1cdc45a9
**Previous ledger commit:** 6d421c215b65476f8e08ce01e2b8cc303580be21 (atomic ledger/results publication)
**Ledger generation:** 467 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 6s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 627; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 609; valid market observations: 609; OHLC screened: 24.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | NEAR/USD | 3.3646 | 96.192 | 96.728 | +6.55% | +0.51% | 0.69x | 6.5 | 2026-11-17T23:09:57.436814+00:00 | Not calibrated | STRONG 78/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 2 | SOL/USD | 75.35 | 94.820 | 91.822 | +5.36% | +0.50% | 1.05x | 1.3 | 2026-11-17T23:09:57.436814+00:00 | Not calibrated | STRONG 82/100 | HIGH 62/100 | Watch | WATCH |
| 3 | ZEC/USD | 957 | 93.463 | 92.165 | +5.89% | +0.16% | 1.05x | 8.1 | 2026-11-17T23:09:57.436814+00:00 | Not calibrated | STRONG 72/100 | HIGH 62/100 | Watch | WATCH |
| 4 | INJ/USD | 7.361 | 92.961 | 95.920 | +6.70% | +0.25% | 0.58x | 8.2 | 2026-11-17T23:09:57.436814+00:00 | Not calibrated | STRONG 76/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 5 | TAO/USD | 196.9147 | 81.865 | 72.919 | +2.99% | +0.45% | 1.67x | 6.0 | 2026-11-17T23:09:57.436814+00:00 | Not calibrated | STRONG 86/100 | HIGH 55/100 | Consider small entry | WATCH |
| 6 | AAVE/USD | 112.96 | 80.613 | 71.056 | +4.13% | +1.11% | 1.40x | 0.9 | 2026-11-17T23:09:57.436814+00:00 | Not calibrated | STRONG 85/100 | HIGH 55/100 | Watch | WATCH |
| 7 | ETH/USD | 1826.81 | 74.774 | 56.898 | +0.44% | +0.58% | 3.12x | 2.4 | 2026-11-17T23:09:57.436814+00:00 | Not calibrated | STRONG 92/100 | HIGH 55/100 | Consider small entry | WATCH |
| 8 | XDG/USD | 0.0602763 | 73.372 | 70.018 | +2.36% | +0.94% | 0.86x | 1.8 | 2026-11-17T23:09:57.436814+00:00 | Not calibrated | MODERATE 67/100 | HIGH 62/100 | Watch | WATCH |
| 9 | XRP/USD | 0.98713 | 71.458 | 77.314 | +3.39% | +0.47% | 0.18x | 2.8 | 2026-11-17T23:09:57.436814+00:00 | Not calibrated | MODERATE 66/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 10 | VVV/USD | 21.072 | 70.976 | 70.881 | +4.59% | +1.24% | 0.39x | 17.1 | 2026-11-17T23:09:57.436814+00:00 | Not calibrated | MODERATE 60/100 | VERY_HIGH 76/100 | Watch | WATCH |
| 11 | SUI/USD | 0.7398 | 70.089 | 73.498 | +2.84% | +0.31% | 0.50x | 2.7 | 2026-11-17T23:09:57.436814+00:00 | Not calibrated | MODERATE 65/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 12 | XMR/USD | 510.94 | 66.580 | 70.899 | +3.52% | +0.49% | 0.33x | 17.4 | 2026-11-17T23:09:57.436814+00:00 | Not calibrated | MODERATE 58/100 | VERY_HIGH 76/100 | Watch | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | NEAR/USD | 96.728 | 3.3646 | +0.51% | 0.69x |
| 2 | INJ/USD | 95.920 | 7.361 | +0.25% | 0.58x |
| 3 | ZEC/USD | 92.165 | 957 | +0.16% | 1.05x |
| 4 | SOL/USD | 91.822 | 75.35 | +0.50% | 1.05x |
| 5 | XRP/USD | 77.314 | 0.98713 | +0.47% | 0.18x |
| 6 | SUI/USD | 73.498 | 0.7398 | +0.31% | 0.50x |
| 7 | TAO/USD | 72.919 | 196.9147 | +0.45% | 1.67x |
| 8 | AAVE/USD | 71.056 | 112.96 | +1.11% | 1.40x |
| 9 | XMR/USD | 70.899 | 510.94 | +0.49% | 0.33x |
| 10 | VVV/USD | 70.881 | 21.072 | +1.24% | 0.39x |
| 11 | XDG/USD | 70.018 | 0.0602763 | +0.94% | 0.86x |
| 12 | ETH/USD | 56.898 | 1826.81 | +0.58% | 3.12x |

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

- Persisted scans: 467; predictions: 4085; observations: 281410.
- Matured sampled outcomes across 1/6/24/48h: 3195; gap abstentions: 12398. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 0 (sampled only; not a success-rate estimate).
- False positives / missed movers: NOT VERIFIED without eligible continuous outcome coverage.
- Baseline vs challenger: recorded as-of; unbiased held-out lift NOT MEASURED.
- Online Kraken /USD stablecoin-base pairs excluded: 18 (counted from this scan's online AssetPairs metadata, not inferred from price).
- Stablecoin base exclusions: BRL1, BUSD, DAI, EUR, EURC, EUROP, EURQ, EURR, EURT, FDUSD, FRAX, GUSD, PYUSD, QCAD, RLUSD, TGBP, TUSD, USD, USD1, USDC, USDD, USDE, USDG, USDQ, USDR, USDS, USDT, ZUSD.
- DEX: NOT USED; no DEX freshness gate.
- OHLC screening abstentions: 5; details in immutable scan JSON artifact.
- Storage: ledger and results published in one non-force Git commit and read back. Independent artifact recovery is NOT VERIFIED by this scan alone.
- Errors: none in successful committed scan; a failed workflow must not publish a SUCCESS report.

# Cryptoscanner — challenger and independent legacy-inspired WATCH

Paper only · risk is high or higher · 30%+ in 48h probability NOT CALIBRATED
Signal confidence 0–100 means setup strength only, NOT a win probability. Actions are research guidance; no trade authorization.

**Writer:** 44196847213 · **Generation:** 467 · **Legacy run:** 44196847213
**Main quote time:** 2026-11-17T23:10:03.886738+00:00 · **Legacy report time:** 2026-11-17T23:10:14.881957+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | NEAR/USD | 3.3646 | 96.19 | +0.51% | 0.69x | STRONG 78/100 | VERY_HIGH 70/100 | Watch |
| 2 | SOL/USD ⭐ | 75.35 | 94.82 | +0.50% | 1.05x | STRONG 92/100 | HIGH 62/100 | Watch |
| 3 | ZEC/USD ⭐ | 957 | 93.46 | +0.16% | 1.05x | STRONG 82/100 | HIGH 62/100 | Watch |
| 4 | INJ/USD | 7.361 | 92.96 | +0.25% | 0.58x | STRONG 76/100 | VERY_HIGH 70/100 | Watch |
| 5 | TAO/USD ⭐ | 196.9147 | 81.86 | +0.45% | 1.67x | STRONG 96/100 | HIGH 55/100 | Consider small entry |
| 6 | AAVE/USD ⭐ | 112.96 | 80.61 | +1.11% | 1.40x | STRONG 95/100 | HIGH 55/100 | Watch |
| 7 | ETH/USD | 1826.81 | 74.77 | +0.58% | 3.12x | STRONG 92/100 | HIGH 55/100 | Consider small entry |
| 8 | XDG/USD | 0.0602763 | 73.37 | +0.94% | 0.86x | MODERATE 67/100 | HIGH 62/100 | Watch |
| 9 | XRP/USD ⭐ | 0.98713 | 71.46 | +0.47% | 0.18x | STRONG 76/100 | VERY_HIGH 70/100 | Watch |
| 10 | VVV/USD | 21.072 | 70.98 | +1.24% | 0.39x | MODERATE 60/100 | VERY_HIGH 76/100 | Watch |
| 11 | SUI/USD ⭐ | 0.7398 | 70.09 | +0.31% | 0.50x | STRONG 75/100 | VERY_HIGH 70/100 | Watch |
| 12 | XMR/USD | 510.94 | 66.58 | +0.49% | 0.33x | MODERATE 58/100 | VERY_HIGH 76/100 | Watch |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | SOL/USD ⭐ | 75.41 | 100.00 | +1.67% | 6.16x | 36001 | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 2 | SUI/USD ⭐ | 0.7397 | 93.86 | +0.90% | 8.28x | 8242 | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 3 | XRP/USD ⭐ | 0.98616 | 91.64 | +1.34% | 1.71x | 30256 | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 4 | ZEC/USD ⭐ | 955.68 | 88.70 | +0.54% | 1.07x | 25816 | STRONG 89/100 | HIGH 62/100 | Watch |
| 5 | AAVE/USD ⭐ | 112.91 | 88.63 | +1.11% | 1.40x | 4140 | STRONG 99/100 | HIGH 55/100 | Watch |
| 6 | ENA/USD | 0.1184 | 84.87 | +1.11% | 4.48x | 5225 | STRONG 97/100 | HIGH 55/100 | Consider small entry |
| 7 | LINK/USD | 9.35098 | 84.62 | +1.01% | 3.75x | 6109 | STRONG 97/100 | HIGH 55/100 | Consider small entry |
| 8 | UNI/USD | 5.3017 | 78.06 | +1.04% | 1.56x | 7060 | STRONG 84/100 | HIGH 55/100 | Consider small entry |
| 9 | TAO/USD ⭐ | 196.6058 | 77.43 | +0.86% | 1.22x | 5113 | STRONG 84/100 | HIGH 62/100 | Watch |

**Same-run overlap:** SOL/USD, ZEC/USD, TAO/USD, AAVE/USD, XRP/USD, SUI/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
