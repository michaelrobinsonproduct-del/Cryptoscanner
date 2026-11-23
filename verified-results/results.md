# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-23T04:51:26.542594+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/45114121959
**Source SHA:** 193371a597e6dbc5a6a884defbe9e1519a6a183a
**Previous ledger commit:** cf14c7d62198dc62833e2d7f32b358d5fd37a88c (atomic ledger/results publication)
**Ledger generation:** 1383 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 7s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 628; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 610; valid market observations: 609; OHLC screened: 24.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | XMR/USD | 501.15 | 78.579 | 63.751 | +1.51% | +0.34% | 2.31x | 3.6 | 2026-11-23T04:51:19.881950+00:00 | Not calibrated | STRONG 94/100 | HIGH 55/100 | Consider small entry | WATCH |
| 2 | NIGHT/USD | 0.04982 | 68.056 | 52.654 | +1.32% | +0.08% | 3.17x | 14.1 | 2026-11-23T04:51:19.881950+00:00 | Not calibrated | STRONG 74/100 | HIGH 61/100 | Watch | WATCH |
| 3 | UNI/USD | 4.7809 | 62.453 | 54.772 | +2.13% | -0.06% | 1.80x | 4.0 | 2026-11-23T04:51:19.881950+00:00 | Not calibrated | MODERATE 51/100 | HIGH 61/100 | Watch | WATCH |
| 4 | LTC/USD | 40.35 | 60.567 | 45.443 | +0.47% | +0.02% | 2.70x | 2.5 | 2026-11-23T04:51:19.881950+00:00 | Not calibrated | STRONG 75/100 | HIGH 55/100 | Watch | WATCH |
| 5 | CC/USD | 0.0759 | 59.706 | 58.183 | +3.59% | +0.01% | 1.15x | 4.0 | 2026-11-23T04:51:19.881950+00:00 | Not calibrated | MODERATE 55/100 | HIGH 67/100 | Watch | WATCH |
| 6 | NEAR/USD | 3.001 | 59.542 | 57.863 | +0.65% | +0.11% | 1.11x | 3.3 | 2026-11-23T04:51:19.881950+00:00 | Not calibrated | MODERATE 55/100 | HIGH 62/100 | Watch | WATCH |
| 7 | VVV/USD | 26.74 | 54.835 | 53.243 | +0.76% | +0.17% | 1.07x | 10.9 | 2026-11-23T04:51:19.881950+00:00 | Not calibrated | MODERATE 47/100 | HIGH 68/100 | Watch | WATCH |
| 8 | XRP/USD | 0.93183 | 54.635 | 57.916 | +0.46% | +0.12% | 0.61x | 0.6 | 2026-11-23T04:51:19.881950+00:00 | Not calibrated | MODERATE 47/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 9 | ICNT/USD | 0.3692 | 54.176 | 53.559 | +4.83% | +1.57% | 0.28x | 27.1 | 2026-11-23T04:51:19.881950+00:00 | Not calibrated | MODERATE 47/100 | EXTREME 87/100 | Do nothing | WATCH |
| 10 | SOL/USD | 71.22 | 53.989 | 59.443 | +0.84% | +0.11% | 0.40x | 2.8 | 2026-11-23T04:51:19.881950+00:00 | Not calibrated | MODERATE 47/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 11 | DOT/USD | 0.6634 | 51.210 | 34.547 | +0.39% | +0.33% | 2.88x | 1.5 | 2026-11-23T04:51:19.881950+00:00 | Not calibrated | STRONG 81/100 | HIGH 60/100 | Watch | WATCH |
| 12 | SUI/USD | 0.6576 | 49.659 | 56.269 | +0.29% | +0.34% | 0.17x | 1.5 | 2026-11-23T04:51:19.881950+00:00 | Not calibrated | MODERATE 55/100 | VERY_HIGH 70/100 | Watch | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | XMR/USD | 63.751 | 501.15 | +0.34% | 2.31x |
| 2 | SOL/USD | 59.443 | 71.22 | +0.11% | 0.40x |
| 3 | CC/USD | 58.183 | 0.0759 | +0.01% | 1.15x |
| 4 | XRP/USD | 57.916 | 0.93183 | +0.12% | 0.61x |
| 5 | NEAR/USD | 57.863 | 3.001 | +0.11% | 1.11x |
| 6 | SUI/USD | 56.269 | 0.6576 | +0.34% | 0.17x |
| 7 | UNI/USD | 54.772 | 4.7809 | -0.06% | 1.80x |
| 8 | ICNT/USD | 53.559 | 0.3692 | +1.57% | 0.28x |
| 9 | VVV/USD | 53.243 | 26.74 | +0.17% | 1.07x |
| 10 | NIGHT/USD | 52.654 | 0.04982 | +0.08% | 3.17x |
| 11 | LTC/USD | 45.443 | 40.35 | +0.02% | 2.70x |
| 12 | DOT/USD | 34.547 | 0.6634 | +0.33% | 2.88x |

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

- Persisted scans: 1383; predictions: 11363; observations: 837352.
- Matured sampled outcomes across 1/6/24/48h: 18366; gap abstentions: 22370. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 101 (sampled only; not a success-rate estimate).
- False positives / missed movers: NOT VERIFIED without eligible continuous outcome coverage.
- Baseline vs challenger: recorded as-of; unbiased held-out lift NOT MEASURED.
- Online Kraken /USD stablecoin-base pairs excluded: 18 (counted from this scan's online AssetPairs metadata, not inferred from price).
- Stablecoin base exclusions: BRL1, BUSD, DAI, EUR, EURC, EUROP, EURQ, EURR, EURT, FDUSD, FRAX, GUSD, PYUSD, QCAD, RLUSD, TGBP, TUSD, USD, USD1, USDC, USDD, USDE, USDG, USDQ, USDR, USDS, USDT, ZUSD.
- DEX: NOT USED; no DEX freshness gate.
- OHLC screening abstentions: 7; details in immutable scan JSON artifact.
- Storage: ledger and results published in one non-force Git commit and read back. Independent artifact recovery is NOT VERIFIED by this scan alone.
- Errors: none in successful committed scan; a failed workflow must not publish a SUCCESS report.

# Cryptoscanner — challenger and independent legacy-inspired WATCH

Paper only · risk is high or higher · 30%+ in 48h probability NOT CALIBRATED
Signal confidence 0–100 means setup strength only, NOT a win probability. Actions are research guidance; no trade authorization.

**Writer:** 45114121959 · **Generation:** 1383 · **Legacy run:** 45114121959
**Main quote time:** 2026-11-23T04:51:26.542594+00:00 · **Legacy report time:** 2026-11-23T04:52:21.284740+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | XMR/USD ⭐ | 501.15 | 78.58 | +0.34% | 2.31x | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 2 | NIGHT/USD ⭐ | 0.04982 | 68.06 | +0.08% | 3.17x | STRONG 84/100 | HIGH 61/100 | Watch |
| 3 | UNI/USD | 4.7809 | 62.45 | -0.06% | 1.80x | MODERATE 51/100 | HIGH 61/100 | Watch |
| 4 | LTC/USD | 40.35 | 60.57 | +0.02% | 2.70x | STRONG 75/100 | HIGH 55/100 | Watch |
| 5 | CC/USD | 0.0759 | 59.71 | +0.01% | 1.15x | MODERATE 55/100 | HIGH 67/100 | Watch |
| 6 | NEAR/USD ⭐ | 3.001 | 59.54 | +0.11% | 1.11x | MODERATE 65/100 | HIGH 62/100 | Watch |
| 7 | VVV/USD | 26.74 | 54.83 | +0.17% | 1.07x | MODERATE 47/100 | HIGH 68/100 | Watch |
| 8 | XRP/USD | 0.93183 | 54.63 | +0.12% | 0.61x | MODERATE 47/100 | VERY_HIGH 70/100 | Watch |
| 9 | ICNT/USD | 0.3692 | 54.18 | +1.57% | 0.28x | MODERATE 47/100 | EXTREME 87/100 | Do nothing |
| 10 | SOL/USD | 71.22 | 53.99 | +0.11% | 0.40x | MODERATE 47/100 | VERY_HIGH 70/100 | Watch |
| 11 | DOT/USD | 0.6634 | 51.21 | +0.33% | 2.88x | STRONG 81/100 | HIGH 60/100 | Watch |
| 12 | SUI/USD | 0.6576 | 49.66 | +0.34% | 0.17x | MODERATE 55/100 | VERY_HIGH 70/100 | Watch |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | NIGHT/USD ⭐ | 0.04988 | 62.81 | +0.08% | 3.17x | 10701 | STRONG 86/100 | HIGH 55/100 | Watch |
| 2 | XMR/USD ⭐ | 501.51 | 62.23 | +0.34% | 2.31x | 8436 | STRONG 96/100 | HIGH 55/100 | Consider small entry |
| 3 | NEAR/USD ⭐ | 3.001 | 57.88 | +0.11% | 1.11x | 13136 | MODERATE 64/100 | HIGH 62/100 | Watch |

**Same-run overlap:** XMR/USD, NIGHT/USD, NEAR/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
