# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-26T01:46:00.303148+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/45737788712
**Source SHA:** 858c8bc8ec5d7641ddb39cacd8aca91719f855b1
**Previous ledger commit:** f418753aca16a8c4ed004922c9764192027bf02c (atomic ledger/results publication)
**Ledger generation:** 1795 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 9s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 628; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 610; valid market observations: 609; OHLC screened: 24.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | LTC/USD | 43.36 | 80.889 | 64.500 | +1.52% | +0.28% | 3.61x | 2.3 | 2026-11-26T01:45:51.741252+00:00 | Not calibrated | STRONG 95/100 | HIGH 55/100 | Consider small entry | WATCH |
| 2 | ADA/USD | 0.14729 | 75.275 | 59.752 | +1.04% | +0.10% | 5.73x | 5.1 | 2026-11-26T01:45:51.741252+00:00 | Not calibrated | STRONG 83/100 | HIGH 55/100 | Watch | WATCH |
| 3 | VVV/USD | 30.232 | 73.344 | 74.899 | +3.55% | +0.61% | 0.54x | 9.9 | 2026-11-26T01:45:51.741252+00:00 | Not calibrated | MODERATE 67/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 4 | XRP/USD | 0.94662 | 69.162 | 61.991 | +1.07% | +0.29% | 1.57x | 1.1 | 2026-11-26T01:45:51.741252+00:00 | Not calibrated | STRONG 80/100 | HIGH 55/100 | Watch | WATCH |
| 5 | SUI/USD | 0.6743 | 68.903 | 62.663 | +1.20% | +0.46% | 1.39x | 1.5 | 2026-11-26T01:45:51.741252+00:00 | Not calibrated | STRONG 79/100 | HIGH 55/100 | Watch | WATCH |
| 6 | PIEVERSE/USD | 3.7919 | 68.088 | 59.068 | +7.09% | -1.20% | 3.92x | 40.0 | 2026-11-26T01:45:51.741252+00:00 | Not calibrated | MODERATE 49/100 | EXTREME 92/100 | Do nothing | WATCH |
| 7 | TAO/USD | 183.7365 | 66.158 | 59.505 | +1.18% | +0.28% | 1.52x | 7.5 | 2026-11-26T01:45:51.741252+00:00 | Not calibrated | STRONG 78/100 | HIGH 55/100 | Watch | WATCH |
| 8 | INJ/USD | 6.122 | 66.049 | 59.669 | +2.82% | +0.78% | 1.25x | 1.6 | 2026-11-26T01:45:51.741252+00:00 | Not calibrated | MODERATE 68/100 | HIGH 55/100 | Watch | WATCH |
| 9 | XBT/USD | 60673.1 | 59.344 | 58.523 | +0.50% | +0.00% | 1.08x | 0.0 | 2026-11-26T01:45:51.741252+00:00 | Not calibrated | MODERATE 55/100 | HIGH 62/100 | Watch | WATCH |
| 10 | ETH/USD | 1698.7 | 57.819 | 58.404 | +0.49% | -0.05% | 0.96x | 0.1 | 2026-11-26T01:45:51.741252+00:00 | Not calibrated | WEAK 34/100 | HIGH 68/100 | Do nothing | WATCH |
| 11 | NEAR/USD | 3.0965 | 56.367 | 63.758 | +1.53% | +0.12% | 0.20x | 3.9 | 2026-11-26T01:45:51.741252+00:00 | Not calibrated | MODERATE 48/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 12 | SOL/USD | 70.84 | 53.466 | 58.769 | +0.64% | -0.06% | 0.50x | 1.4 | 2026-11-26T01:45:51.741252+00:00 | Not calibrated | WEAK 32/100 | VERY_HIGH 76/100 | Do nothing | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | VVV/USD | 74.899 | 30.232 | +0.61% | 0.54x |
| 2 | LTC/USD | 64.500 | 43.36 | +0.28% | 3.61x |
| 3 | NEAR/USD | 63.758 | 3.0965 | +0.12% | 0.20x |
| 4 | SUI/USD | 62.663 | 0.6743 | +0.46% | 1.39x |
| 5 | XRP/USD | 61.991 | 0.94662 | +0.29% | 1.57x |
| 6 | ADA/USD | 59.752 | 0.14729 | +0.10% | 5.73x |
| 7 | INJ/USD | 59.669 | 6.122 | +0.78% | 1.25x |
| 8 | TAO/USD | 59.505 | 183.7365 | +0.28% | 1.52x |
| 9 | PIEVERSE/USD | 59.068 | 3.7919 | -1.20% | 3.92x |
| 10 | SOL/USD | 58.769 | 70.84 | -0.06% | 0.50x |
| 11 | XBT/USD | 58.523 | 60673.1 | +0.00% | 1.08x |
| 12 | ETH/USD | 58.404 | 1698.7 | -0.05% | 0.96x |

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

- Persisted scans: 1795; predictions: 15275; observations: 1088199.
- Matured sampled outcomes across 1/6/24/48h: 33200; gap abstentions: 23612. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 146 (sampled only; not a success-rate estimate).
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

**Writer:** 45737788712 · **Generation:** 1795 · **Legacy run:** 45737788712
**Main quote time:** 2026-11-26T01:46:00.303148+00:00 · **Legacy report time:** 2026-11-26T01:46:51.063052+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | LTC/USD ⭐ | 43.36 | 80.89 | +0.28% | 3.61x | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 2 | ADA/USD | 0.14729 | 75.28 | +0.10% | 5.73x | STRONG 83/100 | HIGH 55/100 | Watch |
| 3 | VVV/USD | 30.232 | 73.34 | +0.61% | 0.54x | MODERATE 67/100 | VERY_HIGH 70/100 | Watch |
| 4 | XRP/USD ⭐ | 0.94662 | 69.16 | +0.29% | 1.57x | STRONG 90/100 | HIGH 55/100 | Consider small entry |
| 5 | SUI/USD ⭐ | 0.6743 | 68.90 | +0.46% | 1.39x | STRONG 89/100 | HIGH 55/100 | Watch |
| 6 | PIEVERSE/USD | 3.7919 | 68.09 | -1.20% | 3.92x | MODERATE 49/100 | EXTREME 92/100 | Do nothing |
| 7 | TAO/USD | 183.7365 | 66.16 | +0.28% | 1.52x | STRONG 78/100 | HIGH 55/100 | Watch |
| 8 | INJ/USD ⭐ | 6.122 | 66.05 | +0.78% | 1.25x | STRONG 78/100 | HIGH 55/100 | Watch |
| 9 | XBT/USD | 60673.1 | 59.34 | +0.00% | 1.08x | MODERATE 55/100 | HIGH 62/100 | Watch |
| 10 | ETH/USD | 1698.7 | 57.82 | -0.05% | 0.96x | WEAK 34/100 | HIGH 68/100 | Do nothing |
| 11 | NEAR/USD | 3.0965 | 56.37 | +0.12% | 0.20x | MODERATE 48/100 | VERY_HIGH 70/100 | Watch |
| 12 | SOL/USD | 70.84 | 53.47 | -0.06% | 0.50x | WEAK 32/100 | VERY_HIGH 76/100 | Do nothing |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | INJ/USD ⭐ | 6.122 | 77.36 | +0.78% | 1.25x | 6794 | STRONG 84/100 | HIGH 55/100 | Watch |
| 2 | LTC/USD ⭐ | 43.39 | 75.33 | +0.28% | 3.61x | 14683 | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 3 | ZRO/USD | 1.058 | 72.03 | +0.77% | 1.42x | 3725 | MODERATE 66/100 | HIGH 67/100 | Watch |
| 4 | BABY/USD | 0.00898 | 69.07 | +0.79% | 14.48x | 2528 | STRONG 85/100 | VERY_HIGH 73/100 | Watch |
| 5 | XRP/USD ⭐ | 0.9467 | 65.83 | +0.29% | 1.57x | 42366 | STRONG 88/100 | HIGH 55/100 | Consider small entry |
| 6 | SUI/USD ⭐ | 0.6743 | 63.43 | +0.46% | 1.39x | 8296 | STRONG 87/100 | HIGH 55/100 | Watch |

**Same-run overlap:** LTC/USD, XRP/USD, SUI/USD, INJ/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
