# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-28T01:52:22.090391+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/46095039147
**Source SHA:** 858c8bc8ec5d7641ddb39cacd8aca91719f855b1
**Previous ledger commit:** e9f8cea71f3ee1338ceb4d6777071bcfc9a84acc (atomic ledger/results publication)
**Ledger generation:** 2089 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 7s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 628; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 610; valid market observations: 606; OHLC screened: 24.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | HYPE/USD | 64.6 | 72.692 | 66.464 | +1.75% | +0.33% | 1.46x | 1.5 | 2026-11-28T01:52:14.603134+00:00 | Not calibrated | STRONG 81/100 | HIGH 55/100 | Watch | WATCH |
| 2 | XMR/USD | 408.51 | 69.989 | 54.070 | +0.30% | +0.18% | 3.17x | 6.1 | 2026-11-28T01:52:14.603134+00:00 | Not calibrated | STRONG 80/100 | HIGH 55/100 | Watch | WATCH |
| 3 | NEAR/USD | 3.0526 | 67.820 | 60.686 | +1.14% | +0.06% | 1.69x | 4.6 | 2026-11-28T01:52:14.603134+00:00 | Not calibrated | MODERATE 69/100 | HIGH 55/100 | Watch | WATCH |
| 4 | ZEC/USD | 754.17 | 66.758 | 71.033 | +2.67% | -0.29% | 0.72x | 5.3 | 2026-11-28T01:52:14.603134+00:00 | Not calibrated | WEAK 38/100 | VERY_HIGH 76/100 | Watch | WATCH |
| 5 | PUMP/USD | 0.002635 | 62.453 | 47.263 | +1.39% | +0.04% | 15.34x | 3.8 | 2026-11-28T01:52:14.603134+00:00 | Not calibrated | STRONG 76/100 | HIGH 55/100 | Watch | WATCH |
| 6 | XRP/USD | 0.95377 | 60.065 | 59.171 | +0.60% | +0.00% | 1.09x | 0.1 | 2026-11-28T01:52:14.603134+00:00 | Not calibrated | MODERATE 55/100 | HIGH 62/100 | Watch | WATCH |
| 7 | SUI/USD | 0.6765 | 59.116 | 58.320 | +0.58% | +0.12% | 1.02x | 1.5 | 2026-11-28T01:52:14.603134+00:00 | Not calibrated | MODERATE 55/100 | HIGH 62/100 | Watch | WATCH |
| 8 | ETH/USD | 1668.28 | 58.243 | 58.076 | +0.44% | -0.06% | 1.05x | 0.1 | 2026-11-28T01:52:14.603134+00:00 | Not calibrated | WEAK 39/100 | HIGH 68/100 | Watch | WATCH |
| 9 | SOL/USD | 72.16 | 54.552 | 59.782 | +0.78% | +0.00% | 0.48x | 1.4 | 2026-11-28T01:52:14.603134+00:00 | Not calibrated | MODERATE 47/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 10 | XDG/USD | 0.0579995 | 54.233 | 58.971 | +0.57% | -0.04% | 0.55x | 0.0 | 2026-11-28T01:52:14.603134+00:00 | Not calibrated | WEAK 32/100 | VERY_HIGH 76/100 | Do nothing | WATCH |
| 11 | XBT/USD | 60138.2 | 54.012 | 58.200 | +0.46% | -0.05% | 0.61x | 0.0 | 2026-11-28T01:52:14.603134+00:00 | Not calibrated | WEAK 32/100 | VERY_HIGH 76/100 | Do nothing | WATCH |
| 12 | TAO/USD | 189.3252 | 52.585 | 59.985 | +1.27% | +0.12% | 0.20x | 7.8 | 2026-11-28T01:52:14.603134+00:00 | Not calibrated | MODERATE 46/100 | VERY_HIGH 70/100 | Watch | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | ZEC/USD | 71.033 | 754.17 | -0.29% | 0.72x |
| 2 | HYPE/USD | 66.464 | 64.6 | +0.33% | 1.46x |
| 3 | NEAR/USD | 60.686 | 3.0526 | +0.06% | 1.69x |
| 4 | TAO/USD | 59.985 | 189.3252 | +0.12% | 0.20x |
| 5 | SOL/USD | 59.782 | 72.16 | +0.00% | 0.48x |
| 6 | XRP/USD | 59.171 | 0.95377 | +0.00% | 1.09x |
| 7 | XDG/USD | 58.971 | 0.0579995 | -0.04% | 0.55x |
| 8 | SUI/USD | 58.320 | 0.6765 | +0.12% | 1.02x |
| 9 | XBT/USD | 58.200 | 60138.2 | -0.05% | 0.61x |
| 10 | ETH/USD | 58.076 | 1668.28 | -0.06% | 1.05x |
| 11 | XMR/USD | 54.070 | 408.51 | +0.18% | 3.17x |
| 12 | PUMP/USD | 47.263 | 0.002635 | +0.04% | 15.34x |

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

- Persisted scans: 2089; predictions: 18731; observations: 1264980.
- Matured sampled outcomes across 1/6/24/48h: 43100; gap abstentions: 25968. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 155 (sampled only; not a success-rate estimate).
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

**Writer:** 46095039147 · **Generation:** 2089 · **Legacy run:** 46095039147
**Main quote time:** 2026-11-28T01:52:22.090391+00:00 · **Legacy report time:** 2026-11-28T01:53:00.521301+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | HYPE/USD ⭐ | 64.6 | 72.69 | +0.33% | 1.46x | STRONG 91/100 | HIGH 55/100 | Watch |
| 2 | XMR/USD | 408.51 | 69.99 | +0.18% | 3.17x | STRONG 80/100 | HIGH 55/100 | Watch |
| 3 | NEAR/USD ⭐ | 3.0526 | 67.82 | +0.06% | 1.69x | STRONG 79/100 | HIGH 55/100 | Watch |
| 4 | ZEC/USD | 754.17 | 66.76 | -0.29% | 0.72x | WEAK 38/100 | VERY_HIGH 76/100 | Watch |
| 5 | PUMP/USD | 0.002635 | 62.45 | +0.04% | 15.34x | STRONG 76/100 | HIGH 55/100 | Watch |
| 6 | XRP/USD | 0.95377 | 60.06 | +0.00% | 1.09x | MODERATE 55/100 | HIGH 62/100 | Watch |
| 7 | SUI/USD ⭐ | 0.6765 | 59.12 | +0.12% | 1.02x | MODERATE 65/100 | HIGH 62/100 | Watch |
| 8 | ETH/USD | 1668.28 | 58.24 | -0.06% | 1.05x | WEAK 39/100 | HIGH 68/100 | Watch |
| 9 | SOL/USD | 72.16 | 54.55 | +0.00% | 0.48x | MODERATE 47/100 | VERY_HIGH 70/100 | Watch |
| 10 | XDG/USD | 0.0579995 | 54.23 | -0.04% | 0.55x | WEAK 32/100 | VERY_HIGH 76/100 | Do nothing |
| 11 | XBT/USD | 60138.2 | 54.01 | -0.05% | 0.61x | WEAK 32/100 | VERY_HIGH 76/100 | Do nothing |
| 12 | TAO/USD | 189.3252 | 52.59 | +0.12% | 0.20x | MODERATE 46/100 | VERY_HIGH 70/100 | Watch |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | CFG/USD | 0.0633 | 82.97 | +2.58% | 3.44x | 2135 | STRONG 81/100 | VERY_HIGH 82/100 | Watch |
| 2 | HYPE/USD ⭐ | 64.64 | 73.46 | +0.33% | 1.46x | 20022 | STRONG 92/100 | HIGH 55/100 | Watch |
| 3 | NEAR/USD ⭐ | 3.0526 | 62.69 | +0.06% | 1.69x | 14283 | STRONG 76/100 | HIGH 55/100 | Watch |
| 4 | SUI/USD ⭐ | 0.6768 | 56.97 | +0.12% | 1.02x | 8053 | MODERATE 63/100 | HIGH 62/100 | Watch |

**Same-run overlap:** HYPE/USD, NEAR/USD, SUI/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
