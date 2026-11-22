# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-22T16:11:14.099202+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/45042243764
**Source SHA:** 17af11513c515cf2dc9dda8017f091d9b1f13397
**Previous ledger commit:** 84d2fac2e6e8f7d8ba0ebb1b98791eef443feb96 (atomic ledger/results publication)
**Ledger generation:** 1305 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 8s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 628; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 610; valid market observations: 609; OHLC screened: 24.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | NIGHT/USD | 0.04837 | 87.977 | 85.092 | +9.24% | -0.19% | 1.38x | 14.5 | 2026-11-22T16:11:06.338534+00:00 | Not calibrated | MODERATE 59/100 | HIGH 67/100 | Watch | WATCH |
| 2 | SUI/USD | 0.6584 | 82.081 | 66.244 | +1.71% | +0.17% | 2.82x | 1.5 | 2026-11-22T16:11:06.338534+00:00 | Not calibrated | STRONG 86/100 | HIGH 55/100 | Watch | WATCH |
| 3 | NEAR/USD | 2.9908 | 77.714 | 78.840 | +3.62% | -0.67% | 1.22x | 3.0 | 2026-11-22T16:11:06.338534+00:00 | Not calibrated | MODERATE 49/100 | HIGH 68/100 | Watch | WATCH |
| 4 | PUMP/USD | 0.002538 | 73.004 | 80.047 | +8.28% | -0.63% | 0.61x | 11.8 | 2026-11-22T16:11:06.338534+00:00 | Not calibrated | WEAK 37/100 | VERY_HIGH 82/100 | Watch | WATCH |
| 5 | DRV/USD | 0.36284 | 70.299 | 80.390 | +8.25% | -0.54% | 0.26x | 16.8 | 2026-11-22T16:11:06.338534+00:00 | Not calibrated | WEAK 35/100 | VERY_HIGH 82/100 | Watch | WATCH |
| 6 | STBL/USD | 0.017265 | 70.143 | 68.294 | +7.88% | +0.48% | 0.94x | 15.1 | 2026-11-22T16:11:06.338534+00:00 | Not calibrated | MODERATE 60/100 | VERY_HIGH 80/100 | Watch | WATCH |
| 7 | AVAX/USD | 6.687 | 69.422 | 53.222 | +1.89% | +0.24% | 5.37x | 3.0 | 2026-11-22T16:11:06.338534+00:00 | Not calibrated | STRONG 90/100 | HIGH 55/100 | Watch | WATCH |
| 8 | HYPE/USD | 62.9 | 69.387 | 73.180 | +2.71% | -0.10% | 0.67x | 1.6 | 2026-11-22T16:11:06.338534+00:00 | Not calibrated | WEAK 40/100 | VERY_HIGH 76/100 | Watch | WATCH |
| 9 | ETH/USD | 1717.95 | 66.377 | 69.813 | +2.12% | -0.02% | 0.67x | 0.1 | 2026-11-22T16:11:06.338534+00:00 | Not calibrated | WEAK 38/100 | VERY_HIGH 76/100 | Watch | WATCH |
| 10 | ZEC/USD | 793.23 | 64.307 | 66.782 | +1.94% | -0.11% | 0.81x | 3.5 | 2026-11-22T16:11:06.338534+00:00 | Not calibrated | WEAK 37/100 | HIGH 68/100 | Watch | WATCH |
| 11 | XBT/USD | 60941.4 | 63.479 | 64.911 | +1.42% | +0.12% | 0.80x | 0.0 | 2026-11-22T16:11:06.338534+00:00 | Not calibrated | MODERATE 52/100 | HIGH 62/100 | Watch | WATCH |
| 12 | BNB/USD | 557.77 | 60.664 | 49.500 | +1.89% | +0.11% | 2.06x | 1.8 | 2026-11-22T16:11:06.338534+00:00 | Not calibrated | STRONG 75/100 | HIGH 55/100 | Watch | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | NIGHT/USD | 85.092 | 0.04837 | -0.19% | 1.38x |
| 2 | DRV/USD | 80.390 | 0.36284 | -0.54% | 0.26x |
| 3 | PUMP/USD | 80.047 | 0.002538 | -0.63% | 0.61x |
| 4 | NEAR/USD | 78.840 | 2.9908 | -0.67% | 1.22x |
| 5 | HYPE/USD | 73.180 | 62.9 | -0.10% | 0.67x |
| 6 | ETH/USD | 69.813 | 1717.95 | -0.02% | 0.67x |
| 7 | STBL/USD | 68.294 | 0.017265 | +0.48% | 0.94x |
| 8 | ZEC/USD | 66.782 | 793.23 | -0.11% | 0.81x |
| 9 | SUI/USD | 66.244 | 0.6584 | +0.17% | 2.82x |
| 10 | XBT/USD | 64.911 | 60941.4 | +0.12% | 0.80x |
| 11 | AVAX/USD | 53.222 | 6.687 | +0.24% | 5.37x |
| 12 | BNB/USD | 49.500 | 557.77 | +0.11% | 2.06x |

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

- Persisted scans: 1305; predictions: 10579; observations: 789853.
- Matured sampled outcomes across 1/6/24/48h: 15588; gap abstentions: 22318. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 61 (sampled only; not a success-rate estimate).
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

**Writer:** 45042243764 · **Generation:** 1305 · **Legacy run:** 45042243764
**Main quote time:** 2026-11-22T16:11:14.099202+00:00 · **Legacy report time:** 2026-11-22T16:12:04.477756+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | NIGHT/USD | 0.04837 | 87.98 | -0.19% | 1.38x | MODERATE 59/100 | HIGH 67/100 | Watch |
| 2 | SUI/USD ⭐ | 0.6584 | 82.08 | +0.17% | 2.82x | STRONG 96/100 | HIGH 55/100 | Watch |
| 3 | NEAR/USD | 2.9908 | 77.71 | -0.67% | 1.22x | MODERATE 49/100 | HIGH 68/100 | Watch |
| 4 | PUMP/USD | 0.002538 | 73.00 | -0.63% | 0.61x | WEAK 37/100 | VERY_HIGH 82/100 | Watch |
| 5 | DRV/USD | 0.36284 | 70.30 | -0.54% | 0.26x | WEAK 35/100 | VERY_HIGH 82/100 | Watch |
| 6 | STBL/USD | 0.017265 | 70.14 | +0.48% | 0.94x | MODERATE 60/100 | VERY_HIGH 80/100 | Watch |
| 7 | AVAX/USD | 6.687 | 69.42 | +0.24% | 5.37x | STRONG 90/100 | HIGH 55/100 | Watch |
| 8 | HYPE/USD | 62.9 | 69.39 | -0.10% | 0.67x | WEAK 40/100 | VERY_HIGH 76/100 | Watch |
| 9 | ETH/USD | 1717.95 | 66.38 | -0.02% | 0.67x | WEAK 38/100 | VERY_HIGH 76/100 | Watch |
| 10 | ZEC/USD | 793.23 | 64.31 | -0.11% | 0.81x | WEAK 37/100 | HIGH 68/100 | Watch |
| 11 | XBT/USD | 60941.4 | 63.48 | +0.12% | 0.80x | MODERATE 52/100 | HIGH 62/100 | Watch |
| 12 | BNB/USD | 557.77 | 60.66 | +0.11% | 2.06x | STRONG 75/100 | HIGH 55/100 | Watch |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | SUI/USD ⭐ | 0.6587 | 77.86 | +0.17% | 2.82x | 6274 | STRONG 94/100 | HIGH 55/100 | Watch |

**Same-run overlap:** SUI/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
