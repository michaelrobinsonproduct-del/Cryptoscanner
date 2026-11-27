# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-27T18:02:29.281731+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/46046040484
**Source SHA:** 858c8bc8ec5d7641ddb39cacd8aca91719f855b1
**Previous ledger commit:** 8011bc06a1abe3ac876baaa00fea4d28110b1294 (atomic ledger/results publication)
**Ledger generation:** 2041 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 8s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 628; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 610; valid market observations: 605; OHLC screened: 24.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | ZEC/USD | 746.11 | 102.964 | 96.848 | +9.45% | +2.18% | 0.52x | 6.3 | 2026-11-27T18:02:21.126742+00:00 | Not calibrated | STRONG 80/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 2 | HYPE/USD | 63.82 | 93.013 | 71.433 | +2.57% | +1.32% | 5.65x | 3.1 | 2026-11-27T18:02:21.126742+00:00 | Not calibrated | STRONG 100/100 | HIGH 55/100 | Consider small entry | WATCH |
| 3 | XDG/USD | 0.0577294 | 89.647 | 71.001 | +2.40% | +0.97% | 2.38x | 1.6 | 2026-11-27T18:02:21.126742+00:00 | Not calibrated | STRONG 100/100 | HIGH 55/100 | Consider small entry | WATCH |
| 4 | NIGHT/USD | 0.04959 | 87.868 | 70.029 | +2.31% | +0.57% | 2.99x | 2.0 | 2026-11-27T18:02:21.126742+00:00 | Not calibrated | STRONG 99/100 | HIGH 55/100 | Consider small entry | WATCH |
| 5 | FET/USD | 0.1269 | 84.494 | 67.259 | +5.40% | +1.12% | 2.16x | 15.8 | 2026-11-27T18:02:21.126742+00:00 | Not calibrated | STRONG 92/100 | HIGH 61/100 | Consider small entry | WATCH |
| 6 | UNI/USD | 4.8031 | 73.191 | 73.029 | +3.29% | +1.52% | 0.26x | 5.0 | 2026-11-27T18:02:21.126742+00:00 | Not calibrated | MODERATE 67/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 7 | SENT/USD | 0.022945 | 72.105 | 69.506 | +6.33% | +1.74% | 0.39x | 10.9 | 2026-11-27T18:02:21.126742+00:00 | Not calibrated | MODERATE 61/100 | EXTREME 88/100 | Do nothing | WATCH |
| 8 | SPACE/USD | 0.004201 | 69.886 | 71.031 | +8.50% | +0.96% | 0.41x | 9.5 | 2026-11-27T18:02:21.126742+00:00 | Not calibrated | MODERATE 65/100 | VERY_HIGH 82/100 | Watch | WATCH |
| 9 | LTC/USD | 43.87 | 68.313 | 54.800 | +0.30% | +1.06% | 1.82x | 4.6 | 2026-11-27T18:02:21.126742+00:00 | Not calibrated | STRONG 79/100 | HIGH 55/100 | Watch | WATCH |
| 10 | XRP/USD | 0.94696 | 64.585 | 57.809 | +0.45% | +0.65% | 1.35x | 0.6 | 2026-11-27T18:02:21.126742+00:00 | Not calibrated | STRONG 77/100 | HIGH 55/100 | Watch | WATCH |
| 11 | PAXG/USD | 3634.1 | 63.324 | 57.954 | +2.18% | +0.43% | 1.32x | 0.0 | 2026-11-27T18:02:21.126742+00:00 | Not calibrated | STRONG 77/100 | HIGH 55/100 | Watch | WATCH |
| 12 | SUI/USD | 0.674 | 63.293 | 60.862 | +0.94% | +1.28% | 0.60x | 1.5 | 2026-11-27T18:02:21.126742+00:00 | Not calibrated | MODERATE 62/100 | VERY_HIGH 70/100 | Watch | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | ZEC/USD | 96.848 | 746.11 | +2.18% | 0.52x |
| 2 | UNI/USD | 73.029 | 4.8031 | +1.52% | 0.26x |
| 3 | HYPE/USD | 71.433 | 63.82 | +1.32% | 5.65x |
| 4 | SPACE/USD | 71.031 | 0.004201 | +0.96% | 0.41x |
| 5 | XDG/USD | 71.001 | 0.0577294 | +0.97% | 2.38x |
| 6 | NIGHT/USD | 70.029 | 0.04959 | +0.57% | 2.99x |
| 7 | SENT/USD | 69.506 | 0.022945 | +1.74% | 0.39x |
| 8 | FET/USD | 67.259 | 0.1269 | +1.12% | 2.16x |
| 9 | SUI/USD | 60.862 | 0.674 | +1.28% | 0.60x |
| 10 | PAXG/USD | 57.954 | 3634.1 | +0.43% | 1.32x |
| 11 | XRP/USD | 57.809 | 0.94696 | +0.65% | 1.35x |
| 12 | LTC/USD | 54.800 | 43.87 | +1.06% | 1.82x |

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

- Persisted scans: 2041; predictions: 18194; observations: 1235914.
- Matured sampled outcomes across 1/6/24/48h: 40836; gap abstentions: 25968. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 153 (sampled only; not a success-rate estimate).
- False positives / missed movers: NOT VERIFIED without eligible continuous outcome coverage.
- Baseline vs challenger: recorded as-of; unbiased held-out lift NOT MEASURED.
- Online Kraken /USD stablecoin-base pairs excluded: 18 (counted from this scan's online AssetPairs metadata, not inferred from price).
- Stablecoin base exclusions: BRL1, BUSD, DAI, EUR, EURC, EUROP, EURQ, EURR, EURT, FDUSD, FRAX, GUSD, PYUSD, QCAD, RLUSD, TGBP, TUSD, USD, USD1, USDC, USDD, USDE, USDG, USDQ, USDR, USDS, USDT, ZUSD.
- DEX: NOT USED; no DEX freshness gate.
- OHLC screening abstentions: 3; details in immutable scan JSON artifact.
- Storage: ledger and results published in one non-force Git commit and read back. Independent artifact recovery is NOT VERIFIED by this scan alone.
- Errors: none in successful committed scan; a failed workflow must not publish a SUCCESS report.

# Cryptoscanner — challenger and independent legacy-inspired WATCH

Paper only · risk is high or higher · 30%+ in 48h probability NOT CALIBRATED
Signal confidence 0–100 means setup strength only, NOT a win probability. Actions are research guidance; no trade authorization.

**Writer:** 46046040484 · **Generation:** 2041 · **Legacy run:** 46046040484
**Main quote time:** 2026-11-27T18:02:29.281731+00:00 · **Legacy report time:** 2026-11-27T18:03:26.109173+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | ZEC/USD | 746.11 | 102.96 | +2.18% | 0.52x | STRONG 80/100 | VERY_HIGH 70/100 | Watch |
| 2 | HYPE/USD ⭐ | 63.82 | 93.01 | +1.32% | 5.65x | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 3 | XDG/USD ⭐ | 0.0577294 | 89.65 | +0.97% | 2.38x | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 4 | NIGHT/USD ⭐ | 0.04959 | 87.87 | +0.57% | 2.99x | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 5 | FET/USD ⭐ | 0.1269 | 84.49 | +1.12% | 2.16x | STRONG 100/100 | HIGH 61/100 | Consider small entry |
| 6 | UNI/USD | 4.8031 | 73.19 | +1.52% | 0.26x | MODERATE 67/100 | VERY_HIGH 70/100 | Watch |
| 7 | SENT/USD | 0.022945 | 72.10 | +1.74% | 0.39x | MODERATE 61/100 | EXTREME 88/100 | Do nothing |
| 8 | SPACE/USD | 0.004201 | 69.89 | +0.96% | 0.41x | MODERATE 65/100 | VERY_HIGH 82/100 | Watch |
| 9 | LTC/USD | 43.87 | 68.31 | +1.06% | 1.82x | STRONG 79/100 | HIGH 55/100 | Watch |
| 10 | XRP/USD | 0.94696 | 64.59 | +0.65% | 1.35x | STRONG 77/100 | HIGH 55/100 | Watch |
| 11 | PAXG/USD ⭐ | 3634.1 | 63.32 | +0.43% | 1.32x | STRONG 87/100 | HIGH 55/100 | Watch |
| 12 | SUI/USD | 0.674 | 63.29 | +1.28% | 0.60x | MODERATE 62/100 | VERY_HIGH 70/100 | Watch |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | HYPE/USD ⭐ | 63.79 | 91.09 | +1.32% | 5.65x | 21044 | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 2 | XDG/USD ⭐ | 0.0576723 | 88.02 | +0.97% | 2.38x | 13061 | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 3 | NIGHT/USD ⭐ | 0.04959 | 85.27 | +0.57% | 2.99x | 16589 | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 4 | FET/USD ⭐ | 0.1267 | 82.42 | +1.12% | 2.16x | 3823 | STRONG 96/100 | HIGH 67/100 | Consider small entry |
| 5 | W/USD | 0.00921 | 74.24 | +0.99% | 1.13x | 2465 | MODERATE 62/100 | VERY_HIGH 79/100 | Watch |
| 6 | PONS/USD | 0.1004 | 73.15 | +0.59% | 1.11x | 4663 | MODERATE 67/100 | VERY_HIGH 80/100 | Watch |
| 7 | PAXG/USD ⭐ | 3636.14 | 71.16 | +0.43% | 1.32x | 4448 | STRONG 91/100 | HIGH 55/100 | Watch |
| 8 | LIGHTER/USD | 2.591 | 68.42 | +0.50% | 1.26x | 1929 | MODERATE 64/100 | HIGH 66/100 | Watch |

**Same-run overlap:** HYPE/USD, XDG/USD, NIGHT/USD, FET/USD, PAXG/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
