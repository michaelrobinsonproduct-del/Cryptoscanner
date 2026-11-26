# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-26T02:44:34.721146+00:00
**GitHub trigger:** scheduled (verified event=schedule; originating cron=2,7,12,17,22,27,32,37,42,47,52,57 * * * *, intended UTC minute=2,7,12,17,22,27,32,37,42,47,52,57; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/45744282117
**Source SHA:** 858c8bc8ec5d7641ddb39cacd8aca91719f855b1
**Previous ledger commit:** 9305d7a8ae7001aee58474b46ef26afb81b67d57 (atomic ledger/results publication)
**Ledger generation:** 1801 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 8s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 628; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 610; valid market observations: 609; OHLC screened: 24.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | TIA/USD | 0.3592 | 91.592 | 75.183 | +6.75% | +0.28% | 16.84x | 2.8 | 2026-11-26T02:44:27.077091+00:00 | Not calibrated | STRONG 100/100 | HIGH 67/100 | Consider small entry | WATCH |
| 2 | TAO/USD | 185.076 | 75.018 | 65.410 | +1.92% | -0.06% | 1.99x | 6.0 | 2026-11-26T02:44:27.077091+00:00 | Not calibrated | MODERATE 58/100 | HIGH 61/100 | Watch | WATCH |
| 3 | XDG/USD | 0.0567532 | 73.170 | 59.720 | +1.42% | -0.31% | 5.60x | 0.7 | 2026-11-26T02:44:27.077091+00:00 | Not calibrated | MODERATE 67/100 | HIGH 61/100 | Watch | WATCH |
| 4 | SOL/USD | 71.25 | 72.817 | 62.851 | +1.22% | -0.31% | 2.15x | 1.4 | 2026-11-26T02:44:27.077091+00:00 | Not calibrated | MODERATE 66/100 | HIGH 61/100 | Watch | WATCH |
| 5 | ETH/USD | 1702.34 | 67.750 | 59.911 | +0.71% | -0.15% | 1.86x | 0.1 | 2026-11-26T02:44:27.077091+00:00 | Not calibrated | MODERATE 54/100 | HIGH 61/100 | Watch | WATCH |
| 6 | INJ/USD | 6.222 | 67.010 | 67.110 | +4.50% | +0.05% | 0.97x | 12.9 | 2026-11-26T02:44:27.077091+00:00 | Not calibrated | MODERATE 49/100 | HIGH 68/100 | Watch | WATCH |
| 7 | XRP/USD | 0.95736 | 65.336 | 70.494 | +2.22% | -0.19% | 0.58x | 0.1 | 2026-11-26T02:44:27.077091+00:00 | Not calibrated | WEAK 38/100 | VERY_HIGH 76/100 | Watch | WATCH |
| 8 | ADA/USD | 0.148531 | 65.209 | 66.846 | +1.89% | -0.30% | 0.98x | 2.8 | 2026-11-26T02:44:27.077091+00:00 | Not calibrated | WEAK 38/100 | HIGH 68/100 | Watch | WATCH |
| 9 | NEAR/USD | 3.0881 | 65.037 | 61.988 | +1.25% | -0.60% | 1.61x | 3.6 | 2026-11-26T02:44:27.077091+00:00 | Not calibrated | MODERATE 53/100 | HIGH 61/100 | Watch | WATCH |
| 10 | SUI/USD | 0.6771 | 63.329 | 65.608 | +1.62% | -0.41% | 0.98x | 1.5 | 2026-11-26T02:44:27.077091+00:00 | Not calibrated | WEAK 37/100 | HIGH 68/100 | Watch | WATCH |
| 11 | ZEC/USD | 782.24 | 62.013 | 64.079 | +1.56% | -0.32% | 0.95x | 3.7 | 2026-11-26T02:44:27.077091+00:00 | Not calibrated | WEAK 36/100 | HIGH 68/100 | Watch | WATCH |
| 12 | XAUT/USD | 3595.5 | 61.653 | 44.864 | +0.74% | +0.36% | 12.51x | 0.8 | 2026-11-26T02:44:27.077091+00:00 | Not calibrated | STRONG 86/100 | HIGH 55/100 | Watch | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | TIA/USD | 75.183 | 0.3592 | +0.28% | 16.84x |
| 2 | XRP/USD | 70.494 | 0.95736 | -0.19% | 0.58x |
| 3 | INJ/USD | 67.110 | 6.222 | +0.05% | 0.97x |
| 4 | ADA/USD | 66.846 | 0.148531 | -0.30% | 0.98x |
| 5 | SUI/USD | 65.608 | 0.6771 | -0.41% | 0.98x |
| 6 | TAO/USD | 65.410 | 185.076 | -0.06% | 1.99x |
| 7 | ZEC/USD | 64.079 | 782.24 | -0.32% | 0.95x |
| 8 | SOL/USD | 62.851 | 71.25 | -0.31% | 2.15x |
| 9 | NEAR/USD | 61.988 | 3.0881 | -0.60% | 1.61x |
| 10 | ETH/USD | 59.911 | 1702.34 | -0.15% | 1.86x |
| 11 | XDG/USD | 59.720 | 0.0567532 | -0.31% | 5.60x |
| 12 | XAUT/USD | 44.864 | 3595.5 | +0.36% | 12.51x |

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

- Persisted scans: 1801; predictions: 15347; observations: 1091853.
- Matured sampled outcomes across 1/6/24/48h: 33335; gap abstentions: 23713. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 146 (sampled only; not a success-rate estimate).
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

**Writer:** 45744282117 · **Generation:** 1801 · **Legacy run:** 45744282117
**Main quote time:** 2026-11-26T02:44:34.721146+00:00 · **Legacy report time:** 2026-11-26T02:45:38.752471+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | TIA/USD | 0.3592 | 91.59 | +0.28% | 16.84x | STRONG 100/100 | HIGH 67/100 | Consider small entry |
| 2 | TAO/USD | 185.076 | 75.02 | -0.06% | 1.99x | MODERATE 58/100 | HIGH 61/100 | Watch |
| 3 | XDG/USD ⭐ | 0.0567532 | 73.17 | -0.31% | 5.60x | STRONG 77/100 | HIGH 61/100 | Watch |
| 4 | SOL/USD ⭐ | 71.25 | 72.82 | -0.31% | 2.15x | STRONG 76/100 | HIGH 61/100 | Watch |
| 5 | ETH/USD | 1702.34 | 67.75 | -0.15% | 1.86x | MODERATE 54/100 | HIGH 61/100 | Watch |
| 6 | INJ/USD | 6.222 | 67.01 | +0.05% | 0.97x | MODERATE 49/100 | HIGH 68/100 | Watch |
| 7 | XRP/USD | 0.95736 | 65.34 | -0.19% | 0.58x | WEAK 38/100 | VERY_HIGH 76/100 | Watch |
| 8 | ADA/USD | 0.148531 | 65.21 | -0.30% | 0.98x | WEAK 38/100 | HIGH 68/100 | Watch |
| 9 | NEAR/USD | 3.0881 | 65.04 | -0.60% | 1.61x | MODERATE 53/100 | HIGH 61/100 | Watch |
| 10 | SUI/USD ⭐ | 0.6771 | 63.33 | -0.41% | 0.98x | MODERATE 47/100 | HIGH 68/100 | Watch |
| 11 | ZEC/USD | 782.24 | 62.01 | -0.32% | 0.95x | WEAK 36/100 | HIGH 68/100 | Watch |
| 12 | XAUT/USD | 3595.5 | 61.65 | +0.36% | 12.51x | STRONG 86/100 | HIGH 55/100 | Watch |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | SUI/USD ⭐ | 0.6773 | 73.97 | +0.37% | 2.00x | 8466 | STRONG 92/100 | HIGH 55/100 | Consider small entry |
| 2 | SOL/USD ⭐ | 71.26 | 66.20 | +0.07% | 1.49x | 46931 | STRONG 78/100 | HIGH 55/100 | Watch |
| 3 | XDG/USD ⭐ | 0.0567272 | 66.16 | +0.12% | 1.07x | 7768 | MODERATE 68/100 | HIGH 62/100 | Watch |

**Same-run overlap:** XDG/USD, SOL/USD, SUI/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
