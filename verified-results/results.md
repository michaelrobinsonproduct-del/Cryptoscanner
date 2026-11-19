# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-19T19:50:27.180342+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/44602322318
**Source SHA:** f854bf15990e1aa3564d35bbec4100f929bd3d42
**Previous ledger commit:** b3d943137814df9270b5fcb110adeaa7aa0b3052 (atomic ledger/results publication)
**Ledger generation:** 848 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 9s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 627; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 609; valid market observations: 599; OHLC screened: 24.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | AKT/USD | 0.5563 | 90.115 | 70.031 | +7.39% | +1.02% | 4.26x | 14.4 | 2026-11-19T19:50:18.265094+00:00 | Not calibrated | STRONG 95/100 | HIGH 66/100 | Consider small entry | WATCH |
| 2 | VVV/USD | 22.535 | 74.510 | 80.686 | +3.99% | -0.03% | 0.40x | 4.4 | 2026-11-19T19:50:18.265094+00:00 | Not calibrated | WEAK 42/100 | VERY_HIGH 76/100 | Watch | WATCH |
| 3 | SKR/USD | 0.010108 | 72.259 | 61.701 | +4.93% | -0.47% | 2.29x | 7.9 | 2026-11-19T19:50:18.265094+00:00 | Not calibrated | MODERATE 66/100 | VERY_HIGH 73/100 | Watch | WATCH |
| 4 | ALEO/USD | 0.03114 | 71.538 | 61.530 | +3.87% | +1.95% | 1.02x | 3.2 | 2026-11-19T19:50:18.265094+00:00 | Not calibrated | STRONG 71/100 | HIGH 67/100 | Watch | WATCH |
| 5 | ADA/USD | 0.153234 | 66.747 | 61.615 | +1.31% | +0.06% | 1.48x | 5.1 | 2026-11-19T19:50:18.265094+00:00 | Not calibrated | MODERATE 68/100 | HIGH 55/100 | Watch | WATCH |
| 6 | CT/USD | 0.1299 | 64.985 | 69.191 | +9.90% | -0.15% | 0.66x | 15.4 | 2026-11-19T19:50:18.265094+00:00 | Not calibrated | WEAK 32/100 | EXTREME 87/100 | Do nothing | WATCH |
| 7 | HYPE/USD | 67.77 | 58.634 | 63.577 | +1.33% | +0.00% | 0.51x | 1.5 | 2026-11-19T19:50:18.265094+00:00 | Not calibrated | MODERATE 49/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 8 | SHIB/USD | 3.832e-06 | 51.228 | 35.967 | +1.00% | +0.05% | 4.59x | 7.8 | 2026-11-19T19:50:18.265094+00:00 | Not calibrated | STRONG 71/100 | HIGH 60/100 | Watch | WATCH |
| 9 | SENT/USD | 0.021388 | 50.794 | 57.171 | +3.80% | -0.23% | 0.48x | 7.5 | 2026-11-19T19:50:18.265094+00:00 | Not calibrated | WEAK 30/100 | VERY_HIGH 81/100 | Do nothing | WATCH |
| 10 | TRX/USD | 0.310382 | 50.622 | 42.898 | +0.36% | +0.02% | 1.76x | 1.1 | 2026-11-19T19:50:18.265094+00:00 | Not calibrated | MODERATE 60/100 | HIGH 55/100 | Watch | WATCH |
| 11 | WLD/USD | 0.2613 | 46.522 | 31.139 | +0.35% | +0.08% | 5.22x | 7.7 | 2026-11-19T19:50:18.265094+00:00 | Not calibrated | MODERATE 68/100 | HIGH 60/100 | Watch | WATCH |
| 12 | INJ/USD | 7.082 | 46.268 | 53.038 | +1.45% | +0.13% | 0.26x | 4.2 | 2026-11-19T19:50:18.265094+00:00 | Not calibrated | WEAK 43/100 | VERY_HIGH 70/100 | Watch | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | VVV/USD | 80.686 | 22.535 | -0.03% | 0.40x |
| 2 | AKT/USD | 70.031 | 0.5563 | +1.02% | 4.26x |
| 3 | CT/USD | 69.191 | 0.1299 | -0.15% | 0.66x |
| 4 | HYPE/USD | 63.577 | 67.77 | +0.00% | 0.51x |
| 5 | SKR/USD | 61.701 | 0.010108 | -0.47% | 2.29x |
| 6 | ADA/USD | 61.615 | 0.153234 | +0.06% | 1.48x |
| 7 | ALEO/USD | 61.530 | 0.03114 | +1.95% | 1.02x |
| 8 | SENT/USD | 57.171 | 0.021388 | -0.23% | 0.48x |
| 9 | INJ/USD | 53.038 | 7.082 | +0.13% | 0.26x |
| 10 | TRX/USD | 42.898 | 0.310382 | +0.02% | 1.76x |
| 11 | SHIB/USD | 35.967 | 3.832e-06 | +0.05% | 4.59x |
| 12 | WLD/USD | 31.139 | 0.2613 | +0.08% | 5.22x |

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

- Persisted scans: 848; predictions: 7320; observations: 512529.
- Matured sampled outcomes across 1/6/24/48h: 7355; gap abstentions: 15625. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 10 (sampled only; not a success-rate estimate).
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

**Writer:** 44602322318 · **Generation:** 848 · **Legacy run:** 44602322318
**Main quote time:** 2026-11-19T19:50:27.180342+00:00 · **Legacy report time:** 2026-11-19T19:51:18.315303+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | AKT/USD ⭐ | 0.5563 | 90.12 | +1.02% | 4.26x | STRONG 100/100 | HIGH 66/100 | Consider small entry |
| 2 | VVV/USD | 22.535 | 74.51 | -0.03% | 0.40x | WEAK 42/100 | VERY_HIGH 76/100 | Watch |
| 3 | SKR/USD | 0.010108 | 72.26 | -0.47% | 2.29x | MODERATE 66/100 | VERY_HIGH 73/100 | Watch |
| 4 | ALEO/USD ⭐ | 0.03114 | 71.54 | +1.95% | 1.02x | STRONG 81/100 | HIGH 67/100 | Watch |
| 5 | ADA/USD ⭐ | 0.153234 | 66.75 | +0.06% | 1.48x | STRONG 78/100 | HIGH 55/100 | Watch |
| 6 | CT/USD | 0.1299 | 64.98 | -0.15% | 0.66x | WEAK 32/100 | EXTREME 87/100 | Do nothing |
| 7 | HYPE/USD | 67.77 | 58.63 | +0.00% | 0.51x | MODERATE 49/100 | VERY_HIGH 70/100 | Watch |
| 8 | SHIB/USD | 3.832e-06 | 51.23 | +0.05% | 4.59x | STRONG 71/100 | HIGH 60/100 | Watch |
| 9 | SENT/USD | 0.021388 | 50.79 | -0.23% | 0.48x | WEAK 30/100 | VERY_HIGH 81/100 | Do nothing |
| 10 | TRX/USD | 0.310382 | 50.62 | +0.02% | 1.76x | MODERATE 60/100 | HIGH 55/100 | Watch |
| 11 | WLD/USD | 0.2613 | 46.52 | +0.08% | 5.22x | MODERATE 68/100 | HIGH 60/100 | Watch |
| 12 | INJ/USD | 7.082 | 46.27 | +0.13% | 0.26x | WEAK 43/100 | VERY_HIGH 70/100 | Watch |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | ALEO/USD ⭐ | 0.03106 | 83.36 | +1.95% | 1.02x | 6823 | STRONG 87/100 | HIGH 67/100 | Watch |
| 2 | AKT/USD ⭐ | 0.5564 | 82.39 | +1.02% | 4.26x | 3375 | STRONG 100/100 | HIGH 66/100 | Consider small entry |
| 3 | ADA/USD ⭐ | 0.152863 | 60.21 | +0.06% | 1.48x | 11844 | STRONG 75/100 | HIGH 55/100 | Watch |

**Same-run overlap:** AKT/USD, ALEO/USD, ADA/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
