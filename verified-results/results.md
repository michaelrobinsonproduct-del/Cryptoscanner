# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-18T03:15:07.150125+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/44229012698
**Source SHA:** 394c17eeb7071fba40e02dbbb1ea97cedb3a0a8a
**Previous ledger commit:** 2c556e77b9a3861f98268a4c156ccd00df815be1 (atomic ledger/results publication)
**Ledger generation:** 516 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 4s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 627; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 609; valid market observations: 609; OHLC screened: 10.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | ICNT/USD | 0.2835 | 58.012 | 40.442 | +2.68% | +1.54% | 1.99x | 21.2 | 2026-11-18T03:15:03.610062+00:00 | Not calibrated | MODERATE 64/100 | VERY_HIGH 72/100 | Watch | WATCH |
| 2 | PIEVERSE/USD | 2.1576 | 53.928 | 56.076 | +5.32% | +0.41% | 0.58x | 26.0 | 2026-11-18T03:15:03.610062+00:00 | Not calibrated | MODERATE 47/100 | EXTREME 87/100 | Do nothing | WATCH |
| 3 | CC/USD | 0.08344 | 53.146 | 42.088 | +1.59% | +0.59% | 1.81x | 8.4 | 2026-11-18T03:15:03.610062+00:00 | Not calibrated | STRONG 72/100 | HIGH 60/100 | Watch | WATCH |
| 4 | ZAMA/USD | 0.0602 | 49.020 | 30.760 | +0.45% | +0.65% | 4.67x | 11.6 | 2026-11-18T03:15:03.610062+00:00 | Not calibrated | STRONG 75/100 | HIGH 66/100 | Watch | WATCH |
| 5 | AKE/USD | 0.01003308 | 36.275 | 28.565 | +0.49% | -1.46% | 4.05x | 19.1 | 2026-11-18T03:15:03.610062+00:00 | Not calibrated | WEAK 43/100 | VERY_HIGH 76/100 | Do nothing | WATCH |
| 6 | AKT/USD | 0.521 | 34.692 | 42.708 | +2.30% | -0.38% | 0.39x | 11.5 | 2026-11-18T03:15:03.610062+00:00 | Not calibrated | WEAK 17/100 | EXTREME 87/100 | Do nothing | WATCH |
| 7 | SENT/USD | 0.018748 | 31.116 | 30.607 | +0.42% | +0.13% | 0.98x | 6.4 | 2026-11-18T03:15:03.610062+00:00 | Not calibrated | WEAK 36/100 | VERY_HIGH 74/100 | Watch | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | PIEVERSE/USD | 56.076 | 2.1576 | +0.41% | 0.58x |
| 2 | AKT/USD | 42.708 | 0.521 | -0.38% | 0.39x |
| 3 | CC/USD | 42.088 | 0.08344 | +0.59% | 1.81x |
| 4 | ICNT/USD | 40.442 | 0.2835 | +1.54% | 1.99x |
| 5 | ZAMA/USD | 30.760 | 0.0602 | +0.65% | 4.67x |
| 6 | SENT/USD | 30.607 | 0.018748 | +0.13% | 0.98x |
| 7 | AKE/USD | 28.565 | 0.01003308 | -1.46% | 4.05x |

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

- Persisted scans: 516; predictions: 4365; observations: 311251.
- Matured sampled outcomes across 1/6/24/48h: 3507; gap abstentions: 12424. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 0 (sampled only; not a success-rate estimate).
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

**Writer:** 44229012698 · **Generation:** 516 · **Legacy run:** 44229012698
**Main quote time:** 2026-11-18T03:15:07.150125+00:00 · **Legacy report time:** 2026-11-18T03:15:22.744616+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | ICNT/USD ⭐ | 0.2835 | 58.01 | +1.54% | 1.99x | STRONG 74/100 | VERY_HIGH 72/100 | Watch |
| 2 | PIEVERSE/USD | 2.1576 | 53.93 | +0.41% | 0.58x | MODERATE 47/100 | EXTREME 87/100 | Do nothing |
| 3 | CC/USD ⭐ | 0.08344 | 53.15 | +0.59% | 1.81x | STRONG 82/100 | HIGH 60/100 | Consider small entry |
| 4 | ZAMA/USD ⭐ | 0.0602 | 49.02 | +0.65% | 4.67x | STRONG 85/100 | HIGH 66/100 | Consider small entry |
| 5 | AKE/USD | 0.01003308 | 36.27 | -1.46% | 4.05x | WEAK 43/100 | VERY_HIGH 76/100 | Do nothing |
| 6 | AKT/USD | 0.521 | 34.69 | -0.38% | 0.39x | WEAK 17/100 | EXTREME 87/100 | Do nothing |
| 7 | SENT/USD | 0.018748 | 31.12 | +0.13% | 0.98x | WEAK 36/100 | VERY_HIGH 74/100 | Watch |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | ICNT/USD ⭐ | 0.2835 | 64.11 | +1.54% | 1.99x | 3758 | STRONG 72/100 | VERY_HIGH 72/100 | Watch |
| 2 | CC/USD ⭐ | 0.08344 | 52.24 | +0.59% | 1.81x | 3977 | STRONG 81/100 | HIGH 60/100 | Consider small entry |
| 3 | ZAMA/USD ⭐ | 0.06025 | 40.41 | +0.65% | 4.67x | 4487 | STRONG 80/100 | HIGH 66/100 | Consider small entry |

**Same-run overlap:** ICNT/USD, CC/USD, ZAMA/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
