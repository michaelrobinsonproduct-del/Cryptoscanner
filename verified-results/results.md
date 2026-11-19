# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-19T22:25:34.347145+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/44628345101
**Source SHA:** f854bf15990e1aa3564d35bbec4100f929bd3d42
**Previous ledger commit:** 003ef92cdf96249864cea3e226e9f4eee123e53d (atomic ledger/results publication)
**Ledger generation:** 870 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 8s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 627; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 609; valid market observations: 602; OHLC screened: 22.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | SENT/USD | 0.021439 | 75.872 | 59.709 | +4.05% | +0.28% | 2.48x | 6.1 | 2026-11-19T22:25:26.618885+00:00 | Not calibrated | STRONG 93/100 | HIGH 60/100 | Consider small entry | WATCH |
| 2 | LUNA/USD | 4.84e-05 | 75.620 | 77.163 | +11.16% | +1.13% | 0.28x | 10.3 | 2026-11-19T22:25:26.618885+00:00 | Not calibrated | MODERATE 63/100 | VERY_HIGH 76/100 | Watch | WATCH |
| 3 | USELESS/USD | 0.09892 | 65.296 | 55.213 | +3.52% | +1.22% | 1.40x | 18.2 | 2026-11-19T22:25:26.618885+00:00 | Not calibrated | STRONG 73/100 | HIGH 61/100 | Watch | WATCH |
| 4 | MEGA/USD | 0.06011 | 62.617 | 68.880 | +7.34% | -0.20% | 0.47x | 16.6 | 2026-11-19T22:25:26.618885+00:00 | Not calibrated | WEAK 31/100 | EXTREME 87/100 | Do nothing | WATCH |
| 5 | VVV/USD | 21.924 | 59.910 | 59.292 | +1.17% | +0.61% | 0.76x | 7.8 | 2026-11-19T22:25:26.618885+00:00 | Not calibrated | MODERATE 60/100 | HIGH 62/100 | Watch | WATCH |
| 6 | SKR/USD | 0.010016 | 58.256 | 55.467 | +3.98% | +0.18% | 1.19x | 7.0 | 2026-11-19T22:25:26.618885+00:00 | Not calibrated | MODERATE 54/100 | VERY_HIGH 74/100 | Watch | WATCH |
| 7 | AKT/USD | 0.5361 | 48.688 | 52.152 | +3.49% | +0.36% | 0.48x | 9.3 | 2026-11-19T22:25:26.618885+00:00 | Not calibrated | MODERATE 54/100 | VERY_HIGH 75/100 | Watch | WATCH |
| 8 | INJ/USD | 7.022 | 47.632 | 47.344 | +0.59% | +0.69% | 0.68x | 4.3 | 2026-11-19T22:25:26.618885+00:00 | Not calibrated | MODERATE 54/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 9 | BLUR/USD | 0.00666 | 21.622 | 24.834 | +1.22% | -0.15% | 0.75x | 29.9 | 2026-11-19T22:25:26.618885+00:00 | Not calibrated | WEAK 6/100 | EXTREME 92/100 | Do nothing | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | LUNA/USD | 77.163 | 4.84e-05 | +1.13% | 0.28x |
| 2 | MEGA/USD | 68.880 | 0.06011 | -0.20% | 0.47x |
| 3 | SENT/USD | 59.709 | 0.021439 | +0.28% | 2.48x |
| 4 | VVV/USD | 59.292 | 21.924 | +0.61% | 0.76x |
| 5 | SKR/USD | 55.467 | 0.010016 | +0.18% | 1.19x |
| 6 | USELESS/USD | 55.213 | 0.09892 | +1.22% | 1.40x |
| 7 | AKT/USD | 52.152 | 0.5361 | +0.36% | 0.48x |
| 8 | INJ/USD | 47.344 | 7.022 | +0.69% | 0.68x |
| 9 | BLUR/USD | 24.834 | 0.00666 | -0.15% | 0.75x |

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

- Persisted scans: 870; predictions: 7561; observations: 525742.
- Matured sampled outcomes across 1/6/24/48h: 7962; gap abstentions: 15741. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 10 (sampled only; not a success-rate estimate).
- False positives / missed movers: NOT VERIFIED without eligible continuous outcome coverage.
- Baseline vs challenger: recorded as-of; unbiased held-out lift NOT MEASURED.
- Online Kraken /USD stablecoin-base pairs excluded: 18 (counted from this scan's online AssetPairs metadata, not inferred from price).
- Stablecoin base exclusions: BRL1, BUSD, DAI, EUR, EURC, EUROP, EURQ, EURR, EURT, FDUSD, FRAX, GUSD, PYUSD, QCAD, RLUSD, TGBP, TUSD, USD, USD1, USDC, USDD, USDE, USDG, USDQ, USDR, USDS, USDT, ZUSD.
- DEX: NOT USED; no DEX freshness gate.
- OHLC screening abstentions: 13; details in immutable scan JSON artifact.
- Storage: ledger and results published in one non-force Git commit and read back. Independent artifact recovery is NOT VERIFIED by this scan alone.
- Errors: none in successful committed scan; a failed workflow must not publish a SUCCESS report.

# Cryptoscanner — challenger and independent legacy-inspired WATCH

Paper only · risk is high or higher · 30%+ in 48h probability NOT CALIBRATED
Signal confidence 0–100 means setup strength only, NOT a win probability. Actions are research guidance; no trade authorization.

**Writer:** 44628345101 · **Generation:** 870 · **Legacy run:** 44628345101
**Main quote time:** 2026-11-19T22:25:34.347145+00:00 · **Legacy report time:** 2026-11-19T22:26:27.475468+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | SENT/USD ⭐ | 0.021439 | 75.87 | +0.28% | 2.48x | STRONG 100/100 | HIGH 60/100 | Consider small entry |
| 2 | LUNA/USD | 4.84e-05 | 75.62 | +1.13% | 0.28x | MODERATE 63/100 | VERY_HIGH 76/100 | Watch |
| 3 | USELESS/USD ⭐ | 0.09892 | 65.30 | +1.22% | 1.40x | STRONG 83/100 | HIGH 61/100 | Watch |
| 4 | MEGA/USD | 0.06011 | 62.62 | -0.20% | 0.47x | WEAK 31/100 | EXTREME 87/100 | Do nothing |
| 5 | VVV/USD | 21.924 | 59.91 | +0.61% | 0.76x | MODERATE 60/100 | HIGH 62/100 | Watch |
| 6 | SKR/USD ⭐ | 0.010016 | 58.26 | +0.18% | 1.19x | MODERATE 64/100 | VERY_HIGH 74/100 | Watch |
| 7 | AKT/USD | 0.5361 | 48.69 | +0.36% | 0.48x | MODERATE 54/100 | VERY_HIGH 75/100 | Watch |
| 8 | INJ/USD | 7.022 | 47.63 | +0.69% | 0.68x | MODERATE 54/100 | VERY_HIGH 70/100 | Watch |
| 9 | BLUR/USD | 0.00666 | 21.62 | -0.15% | 0.75x | WEAK 6/100 | EXTREME 92/100 | Do nothing |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | SENT/USD ⭐ | 0.021439 | 86.93 | +0.28% | 2.48x | 14777 | STRONG 100/100 | HIGH 60/100 | Consider small entry |
| 2 | USELESS/USD ⭐ | 0.09919 | 78.69 | +1.22% | 1.40x | 4934 | STRONG 89/100 | HIGH 61/100 | Watch |
| 3 | SKR/USD ⭐ | 0.010016 | 64.19 | +0.18% | 1.19x | 1378 | MODERATE 67/100 | VERY_HIGH 74/100 | Watch |

**Same-run overlap:** SENT/USD, USELESS/USD, SKR/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
