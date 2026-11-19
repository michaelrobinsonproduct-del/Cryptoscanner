# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-19T17:07:41.155487+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/44573184994
**Source SHA:** f854bf15990e1aa3564d35bbec4100f929bd3d42
**Previous ledger commit:** f3201c713d587abea9f28ab83ce2f8b70961a4c7 (atomic ledger/results publication)
**Ledger generation:** 821 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 9s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 627; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 609; valid market observations: 598; OHLC screened: 24.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | LUNA/USD | 4.777e-05 | 87.599 | 61.614 | +9.72% | +2.20% | 3.97x | 40.1 | 2026-11-19T17:07:32.388559+00:00 | Not calibrated | STRONG 84/100 | VERY_HIGH 82/100 | Watch | WATCH |
| 2 | TRUST/USD | 0.05496 | 81.158 | 75.348 | +11.71% | +0.53% | 1.32x | 1.8 | 2026-11-19T17:07:32.388559+00:00 | Not calibrated | STRONG 86/100 | HIGH 67/100 | Watch | WATCH |
| 3 | SENT/USD | 0.021667 | 63.020 | 68.644 | +5.15% | -0.65% | 0.76x | 3.7 | 2026-11-19T17:07:32.388559+00:00 | Not calibrated | WEAK 37/100 | VERY_HIGH 73/100 | Watch | WATCH |
| 4 | VVV/USD | 22.257 | 62.757 | 69.660 | +2.70% | -2.36% | 1.49x | 8.5 | 2026-11-19T17:07:32.388559+00:00 | Not calibrated | MODERATE 51/100 | HIGH 65/100 | Do nothing | WATCH |
| 5 | ALEO/USD | 0.03117 | 57.852 | 58.935 | +3.97% | +0.39% | 0.70x | 3.2 | 2026-11-19T17:07:32.388559+00:00 | Not calibrated | MODERATE 59/100 | VERY_HIGH 75/100 | Watch | WATCH |
| 6 | BMT/USD | 0.02037 | 56.264 | 68.821 | +7.89% | -0.68% | 0.09x | 14.7 | 2026-11-19T17:07:32.388559+00:00 | Not calibrated | WEAK 28/100 | EXTREME 94/100 | Do nothing | WATCH |
| 7 | PYTH/USD | 0.05538 | 53.258 | 57.008 | +4.97% | -1.21% | 1.23x | 19.8 | 2026-11-19T17:07:32.388559+00:00 | Not calibrated | WEAK 32/100 | VERY_HIGH 83/100 | Do nothing | WATCH |
| 8 | HYPE/USD | 67.11 | 52.005 | 55.917 | +0.34% | -1.10% | 1.16x | 3.0 | 2026-11-19T17:07:32.388559+00:00 | Not calibrated | WEAK 36/100 | VERY_HIGH 72/100 | Watch | WATCH |
| 9 | AKT/USD | 0.5327 | 47.691 | 43.953 | +2.84% | -2.25% | 3.20x | 15.0 | 2026-11-19T17:07:32.388559+00:00 | Not calibrated | MODERATE 49/100 | VERY_HIGH 83/100 | Do nothing | WATCH |
| 10 | USELESS/USD | 0.0979 | 46.442 | 47.379 | +2.45% | -3.19% | 6.39x | 14.3 | 2026-11-19T17:07:32.388559+00:00 | Not calibrated | MODERATE 48/100 | VERY_HIGH 71/100 | Do nothing | WATCH |
| 11 | SKR/USD | 0.01014 | 46.334 | 61.498 | +5.26% | -2.23% | 0.60x | 12.8 | 2026-11-19T17:07:32.388559+00:00 | Not calibrated | WEAK 23/100 | EXTREME 98/100 | Do nothing | WATCH |
| 12 | INJ/USD | 7.054 | 36.531 | 48.427 | +1.05% | -1.88% | 0.75x | 4.3 | 2026-11-19T17:07:32.388559+00:00 | Not calibrated | WEAK 23/100 | VERY_HIGH 72/100 | Do nothing | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | TRUST/USD | 75.348 | 0.05496 | +0.53% | 1.32x |
| 2 | VVV/USD | 69.660 | 22.257 | -2.36% | 1.49x |
| 3 | BMT/USD | 68.821 | 0.02037 | -0.68% | 0.09x |
| 4 | SENT/USD | 68.644 | 0.021667 | -0.65% | 0.76x |
| 5 | LUNA/USD | 61.614 | 4.777e-05 | +2.20% | 3.97x |
| 6 | SKR/USD | 61.498 | 0.01014 | -2.23% | 0.60x |
| 7 | ALEO/USD | 58.935 | 0.03117 | +0.39% | 0.70x |
| 8 | PYTH/USD | 57.008 | 0.05538 | -1.21% | 1.23x |
| 9 | HYPE/USD | 55.917 | 67.11 | -1.10% | 1.16x |
| 10 | INJ/USD | 48.427 | 7.054 | -1.88% | 0.75x |
| 11 | USELESS/USD | 47.379 | 0.0979 | -3.19% | 6.39x |
| 12 | AKT/USD | 43.953 | 0.5327 | -2.25% | 3.20x |

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

- Persisted scans: 821; predictions: 6996; observations: 496369.
- Matured sampled outcomes across 1/6/24/48h: 6959; gap abstentions: 15416. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 10 (sampled only; not a success-rate estimate).
- False positives / missed movers: NOT VERIFIED without eligible continuous outcome coverage.
- Baseline vs challenger: recorded as-of; unbiased held-out lift NOT MEASURED.
- Online Kraken /USD stablecoin-base pairs excluded: 18 (counted from this scan's online AssetPairs metadata, not inferred from price).
- Stablecoin base exclusions: BRL1, BUSD, DAI, EUR, EURC, EUROP, EURQ, EURR, EURT, FDUSD, FRAX, GUSD, PYUSD, QCAD, RLUSD, TGBP, TUSD, USD, USD1, USDC, USDD, USDE, USDG, USDQ, USDR, USDS, USDT, ZUSD.
- DEX: NOT USED; no DEX freshness gate.
- OHLC screening abstentions: 11; details in immutable scan JSON artifact.
- Storage: ledger and results published in one non-force Git commit and read back. Independent artifact recovery is NOT VERIFIED by this scan alone.
- Errors: none in successful committed scan; a failed workflow must not publish a SUCCESS report.

# Cryptoscanner — challenger and independent legacy-inspired WATCH

Paper only · risk is high or higher · 30%+ in 48h probability NOT CALIBRATED
Signal confidence 0–100 means setup strength only, NOT a win probability. Actions are research guidance; no trade authorization.

**Writer:** 44573184994 · **Generation:** 821 · **Legacy run:** 44573184994
**Main quote time:** 2026-11-19T17:07:41.155487+00:00 · **Legacy report time:** 2026-11-19T17:08:27.596518+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | LUNA/USD ⭐ | 4.777e-05 | 87.60 | +2.20% | 3.97x | STRONG 94/100 | VERY_HIGH 82/100 | Watch |
| 2 | TRUST/USD ⭐ | 0.05496 | 81.16 | +0.53% | 1.32x | STRONG 96/100 | HIGH 67/100 | Watch |
| 3 | SENT/USD | 0.021667 | 63.02 | -0.65% | 0.76x | WEAK 37/100 | VERY_HIGH 73/100 | Watch |
| 4 | VVV/USD | 22.257 | 62.76 | -2.36% | 1.49x | MODERATE 51/100 | HIGH 65/100 | Do nothing |
| 5 | ALEO/USD | 0.03117 | 57.85 | +0.39% | 0.70x | MODERATE 59/100 | VERY_HIGH 75/100 | Watch |
| 6 | BMT/USD | 0.02037 | 56.26 | -0.68% | 0.09x | WEAK 28/100 | EXTREME 94/100 | Do nothing |
| 7 | PYTH/USD | 0.05538 | 53.26 | -1.21% | 1.23x | WEAK 32/100 | VERY_HIGH 83/100 | Do nothing |
| 8 | HYPE/USD | 67.11 | 52.01 | -1.10% | 1.16x | WEAK 36/100 | VERY_HIGH 72/100 | Watch |
| 9 | AKT/USD | 0.5327 | 47.69 | -2.25% | 3.20x | MODERATE 49/100 | VERY_HIGH 83/100 | Do nothing |
| 10 | USELESS/USD | 0.0979 | 46.44 | -3.19% | 6.39x | MODERATE 48/100 | VERY_HIGH 71/100 | Do nothing |
| 11 | SKR/USD | 0.01014 | 46.33 | -2.23% | 0.60x | WEAK 23/100 | EXTREME 98/100 | Do nothing |
| 12 | INJ/USD | 7.054 | 36.53 | -1.88% | 0.75x | WEAK 23/100 | VERY_HIGH 72/100 | Do nothing |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | LUNA/USD ⭐ | 4.781e-05 | 88.59 | +2.20% | 3.97x | 6019 | STRONG 94/100 | VERY_HIGH 72/100 | Watch |
| 2 | TRUST/USD ⭐ | 0.05522 | 68.96 | +0.53% | 1.32x | 2081 | STRONG 79/100 | VERY_HIGH 79/100 | Watch |

**Same-run overlap:** LUNA/USD, TRUST/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
