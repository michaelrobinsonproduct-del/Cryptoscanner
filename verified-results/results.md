# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-18T18:50:15.927855+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/44373888542
**Source SHA:** b271b90a2cae9e5307600070ce7d0e510fe68996
**Previous ledger commit:** d76e93eeec66e1236267a12144c4362469eddd40 (atomic ledger/results publication)
**Ledger generation:** 640 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 5s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 627; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 609; valid market observations: 609; OHLC screened: 17.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | SENT/USD | 0.019858 | 80.913 | 69.171 | +6.37% | -0.65% | 2.82x | 13.1 | 2026-11-18T18:50:10.968208+00:00 | Not calibrated | MODERATE 65/100 | VERY_HIGH 79/100 | Watch | WATCH |
| 2 | STABLE/USD | 0.02341 | 57.987 | 63.154 | +11.21% | +0.60% | 0.18x | 25.7 | 2026-11-18T18:50:10.968208+00:00 | Not calibrated | MODERATE 49/100 | EXTREME 94/100 | Do nothing | WATCH |
| 3 | AKT/USD | 0.5118 | 53.400 | 34.462 | +0.49% | +0.79% | 4.31x | 2.0 | 2026-11-18T18:50:10.968208+00:00 | Not calibrated | STRONG 82/100 | HIGH 60/100 | Watch | WATCH |
| 4 | NIGHT/USD | 0.04516 | 47.346 | 49.970 | +0.60% | -0.13% | 0.80x | 4.4 | 2026-11-18T18:50:10.968208+00:00 | Not calibrated | WEAK 29/100 | HIGH 68/100 | Do nothing | WATCH |
| 5 | MNT/USD | 0.3852 | 40.769 | 48.990 | +3.19% | -0.05% | 0.20x | 10.4 | 2026-11-18T18:50:10.968208+00:00 | Not calibrated | WEAK 20/100 | EXTREME 87/100 | Do nothing | WATCH |
| 6 | W/USD | 0.00898 | 36.816 | 29.663 | +0.56% | +0.90% | 1.27x | 11.1 | 2026-11-18T18:50:10.968208+00:00 | Not calibrated | MODERATE 48/100 | VERY_HIGH 73/100 | Watch | WATCH |
| 7 | UAI/USD | 0.03353 | 25.677 | 25.088 | +0.45% | +0.48% | 0.82x | 17.9 | 2026-11-18T18:50:10.968208+00:00 | Not calibrated | WEAK 38/100 | VERY_HIGH 80/100 | Watch | WATCH |
| 8 | SPACE/USD | 0.00337 | 17.010 | 23.052 | +0.81% | +0.45% | 0.17x | 26.7 | 2026-11-18T18:50:10.968208+00:00 | Not calibrated | WEAK 29/100 | EXTREME 94/100 | Do nothing | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | SENT/USD | 69.171 | 0.019858 | -0.65% | 2.82x |
| 2 | STABLE/USD | 63.154 | 0.02341 | +0.60% | 0.18x |
| 3 | NIGHT/USD | 49.970 | 0.04516 | -0.13% | 0.80x |
| 4 | MNT/USD | 48.990 | 0.3852 | -0.05% | 0.20x |
| 5 | AKT/USD | 34.462 | 0.5118 | +0.79% | 4.31x |
| 6 | W/USD | 29.663 | 0.00898 | +0.90% | 1.27x |
| 7 | UAI/USD | 25.088 | 0.03353 | +0.48% | 0.82x |
| 8 | SPACE/USD | 23.052 | 0.00337 | +0.45% | 0.17x |

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

- Persisted scans: 640; predictions: 5434; observations: 386767.
- Matured sampled outcomes across 1/6/24/48h: 4725; gap abstentions: 13125. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 0 (sampled only; not a success-rate estimate).
- False positives / missed movers: NOT VERIFIED without eligible continuous outcome coverage.
- Baseline vs challenger: recorded as-of; unbiased held-out lift NOT MEASURED.
- Online Kraken /USD stablecoin-base pairs excluded: 18 (counted from this scan's online AssetPairs metadata, not inferred from price).
- Stablecoin base exclusions: BRL1, BUSD, DAI, EUR, EURC, EUROP, EURQ, EURR, EURT, FDUSD, FRAX, GUSD, PYUSD, QCAD, RLUSD, TGBP, TUSD, USD, USD1, USDC, USDD, USDE, USDG, USDQ, USDR, USDS, USDT, ZUSD.
- DEX: NOT USED; no DEX freshness gate.
- OHLC screening abstentions: 9; details in immutable scan JSON artifact.
- Storage: ledger and results published in one non-force Git commit and read back. Independent artifact recovery is NOT VERIFIED by this scan alone.
- Errors: none in successful committed scan; a failed workflow must not publish a SUCCESS report.

# Cryptoscanner — challenger and independent legacy-inspired WATCH

Paper only · risk is high or higher · 30%+ in 48h probability NOT CALIBRATED
Signal confidence 0–100 means setup strength only, NOT a win probability. Actions are research guidance; no trade authorization.

**Writer:** 44373888542 · **Generation:** 640 · **Legacy run:** 44373888542
**Main quote time:** 2026-11-18T18:50:15.927855+00:00 · **Legacy report time:** 2026-11-18T18:50:50.022366+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | SENT/USD | 0.019858 | 80.91 | -0.65% | 2.82x | MODERATE 65/100 | VERY_HIGH 79/100 | Watch |
| 2 | STABLE/USD | 0.02341 | 57.99 | +0.60% | 0.18x | MODERATE 49/100 | EXTREME 94/100 | Do nothing |
| 3 | AKT/USD ⭐ | 0.5118 | 53.40 | +0.79% | 4.31x | STRONG 92/100 | HIGH 60/100 | Consider small entry |
| 4 | NIGHT/USD | 0.04516 | 47.35 | -0.13% | 0.80x | WEAK 29/100 | HIGH 68/100 | Do nothing |
| 5 | MNT/USD | 0.3852 | 40.77 | -0.05% | 0.20x | WEAK 20/100 | EXTREME 87/100 | Do nothing |
| 6 | W/USD | 0.00898 | 36.82 | +0.90% | 1.27x | MODERATE 48/100 | VERY_HIGH 73/100 | Watch |
| 7 | UAI/USD | 0.03353 | 25.68 | +0.48% | 0.82x | WEAK 38/100 | VERY_HIGH 80/100 | Watch |
| 8 | SPACE/USD | 0.00337 | 17.01 | +0.45% | 0.17x | WEAK 29/100 | EXTREME 94/100 | Do nothing |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | INFI/USD | 0.1341 | 86.69 | +7.58% | 3.69x | 3677 | STRONG 88/100 | EXTREME 89/100 | Do nothing |
| 2 | TRX/USD | 0.308359 | 45.40 | +0.07% | 1.05x | 4156 | MODERATE 48/100 | HIGH 62/100 | Watch |
| 3 | AKT/USD ⭐ | 0.5116 | 38.99 | +0.79% | 4.31x | 4484 | STRONG 79/100 | HIGH 66/100 | Consider small entry |
| 4 | CC/USD | 0.08225 | 28.37 | +0.16% | 1.16x | 4953 | WEAK 39/100 | HIGH 67/100 | Watch |

**Same-run overlap:** AKT/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
