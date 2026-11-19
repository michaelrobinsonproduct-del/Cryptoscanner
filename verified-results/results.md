# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-19T03:50:22.281908+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/44454114133
**Source SHA:** b271b90a2cae9e5307600070ce7d0e510fe68996
**Previous ledger commit:** 19dfa2b6e0fdb8b22ee92e322f5f315fa72fac69 (atomic ledger/results publication)
**Ledger generation:** 747 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 7s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 627; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 609; valid market observations: 609; OHLC screened: 24.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | VVV/USD | 22.34 | 85.589 | 63.714 | +3.09% | +1.38% | 2.71x | 16.5 | 2026-11-19T03:50:15.100246+00:00 | Not calibrated | STRONG 93/100 | HIGH 61/100 | Consider small entry | WATCH |
| 2 | NEAR/USD | 3.3871 | 84.531 | 70.352 | +2.72% | +0.56% | 2.14x | 7.4 | 2026-11-19T03:50:15.100246+00:00 | Not calibrated | STRONG 97/100 | HIGH 55/100 | Consider small entry | WATCH |
| 3 | SUI/USD | 0.7249 | 78.765 | 60.153 | +0.83% | +0.72% | 7.39x | 1.4 | 2026-11-19T03:50:15.100246+00:00 | Not calibrated | STRONG 94/100 | HIGH 55/100 | Consider small entry | WATCH |
| 4 | SENT/USD | 0.022246 | 77.695 | 73.354 | +7.96% | -1.43% | 2.15x | 6.7 | 2026-11-19T03:50:15.100246+00:00 | Not calibrated | MODERATE 69/100 | VERY_HIGH 70/100 | Do nothing | WATCH |
| 5 | ETH/USD | 1787.54 | 76.345 | 59.565 | +0.72% | +0.36% | 2.81x | 1.0 | 2026-11-19T03:50:15.100246+00:00 | Not calibrated | STRONG 93/100 | HIGH 55/100 | Consider small entry | WATCH |
| 6 | TAO/USD | 194.0351 | 72.952 | 58.514 | +1.08% | +0.84% | 2.02x | 8.1 | 2026-11-19T03:50:15.100246+00:00 | Not calibrated | STRONG 91/100 | HIGH 55/100 | Consider small entry | WATCH |
| 7 | LINK/USD | 9.09723 | 71.173 | 54.669 | +0.27% | +0.30% | 4.45x | 4.4 | 2026-11-19T03:50:15.100246+00:00 | Not calibrated | STRONG 91/100 | HIGH 55/100 | Consider small entry | WATCH |
| 8 | XDG/USD | 0.0589168 | 68.402 | 51.296 | +0.36% | +0.42% | 2.96x | 0.6 | 2026-11-19T03:50:15.100246+00:00 | Not calibrated | STRONG 89/100 | HIGH 55/100 | Watch | WATCH |
| 9 | SOL/USD | 74.12 | 67.670 | 59.846 | +0.79% | +0.49% | 1.54x | 1.3 | 2026-11-19T03:50:15.100246+00:00 | Not calibrated | STRONG 79/100 | HIGH 55/100 | Watch | WATCH |
| 10 | ZEC/USD | 918.56 | 66.071 | 57.459 | +0.72% | +0.96% | 1.38x | 5.2 | 2026-11-19T03:50:15.100246+00:00 | Not calibrated | STRONG 78/100 | HIGH 55/100 | Watch | WATCH |
| 11 | HYPE/USD | 67.21 | 63.373 | 57.710 | +0.49% | +0.72% | 1.21x | 1.5 | 2026-11-19T03:50:15.100246+00:00 | Not calibrated | MODERATE 67/100 | HIGH 62/100 | Watch | WATCH |
| 12 | ONDO/USD | 0.30062 | 59.697 | 41.635 | +1.00% | +0.61% | 8.77x | 0.3 | 2026-11-19T03:50:15.100246+00:00 | Not calibrated | STRONG 85/100 | HIGH 60/100 | Watch | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | SENT/USD | 73.354 | 0.022246 | -1.43% | 2.15x |
| 2 | NEAR/USD | 70.352 | 3.3871 | +0.56% | 2.14x |
| 3 | VVV/USD | 63.714 | 22.34 | +1.38% | 2.71x |
| 4 | SUI/USD | 60.153 | 0.7249 | +0.72% | 7.39x |
| 5 | SOL/USD | 59.846 | 74.12 | +0.49% | 1.54x |
| 6 | ETH/USD | 59.565 | 1787.54 | +0.36% | 2.81x |
| 7 | TAO/USD | 58.514 | 194.0351 | +0.84% | 2.02x |
| 8 | HYPE/USD | 57.710 | 67.21 | +0.72% | 1.21x |
| 9 | ZEC/USD | 57.459 | 918.56 | +0.96% | 1.38x |
| 10 | LINK/USD | 54.669 | 9.09723 | +0.30% | 4.45x |
| 11 | XDG/USD | 51.296 | 0.0589168 | +0.42% | 2.96x |
| 12 | ONDO/USD | 41.635 | 0.30062 | +0.61% | 8.77x |

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

- Persisted scans: 747; predictions: 6108; observations: 451930.
- Matured sampled outcomes across 1/6/24/48h: 6079; gap abstentions: 13570. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 10 (sampled only; not a success-rate estimate).
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

**Writer:** 44454114133 · **Generation:** 747 · **Legacy run:** 44454114133
**Main quote time:** 2026-11-19T03:50:22.281908+00:00 · **Legacy report time:** 2026-11-19T03:51:12.472198+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | VVV/USD ⭐ | 22.34 | 85.59 | +1.38% | 2.71x | STRONG 100/100 | HIGH 61/100 | Consider small entry |
| 2 | NEAR/USD ⭐ | 3.3871 | 84.53 | +0.56% | 2.14x | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 3 | SUI/USD ⭐ | 0.7249 | 78.77 | +0.72% | 7.39x | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 4 | SENT/USD | 0.022246 | 77.69 | -1.43% | 2.15x | MODERATE 69/100 | VERY_HIGH 70/100 | Do nothing |
| 5 | ETH/USD ⭐ | 1787.54 | 76.35 | +0.36% | 2.81x | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 6 | TAO/USD | 194.0351 | 72.95 | +0.84% | 2.02x | STRONG 91/100 | HIGH 55/100 | Consider small entry |
| 7 | LINK/USD ⭐ | 9.09723 | 71.17 | +0.30% | 4.45x | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 8 | XDG/USD | 0.0589168 | 68.40 | +0.42% | 2.96x | STRONG 89/100 | HIGH 55/100 | Watch |
| 9 | SOL/USD ⭐ | 74.12 | 67.67 | +0.49% | 1.54x | STRONG 89/100 | HIGH 55/100 | Consider small entry |
| 10 | ZEC/USD | 918.56 | 66.07 | +0.96% | 1.38x | STRONG 78/100 | HIGH 55/100 | Watch |
| 11 | HYPE/USD | 67.21 | 63.37 | +0.72% | 1.21x | MODERATE 67/100 | HIGH 62/100 | Watch |
| 12 | ONDO/USD | 0.30062 | 59.70 | +0.61% | 8.77x | STRONG 85/100 | HIGH 60/100 | Watch |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | VVV/USD ⭐ | 22.362 | 83.46 | +1.38% | 2.71x | 8631 | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 2 | NEAR/USD ⭐ | 3.3864 | 81.17 | +0.56% | 2.14x | 13813 | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 3 | SUI/USD ⭐ | 0.725 | 69.59 | +0.72% | 7.39x | 6702 | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 4 | ETH/USD ⭐ | 1785.8 | 66.78 | +0.36% | 2.81x | 58161 | STRONG 98/100 | HIGH 55/100 | Consider small entry |
| 5 | LINK/USD ⭐ | 9.09192 | 63.42 | +0.30% | 4.45x | 5750 | STRONG 97/100 | HIGH 55/100 | Consider small entry |
| 6 | SOL/USD ⭐ | 74.02 | 60.75 | +0.49% | 1.54x | 35195 | STRONG 85/100 | HIGH 55/100 | Consider small entry |
| 7 | XBT/USD | 63063.3 | 59.58 | +0.18% | 2.39x | 148603 | STRONG 75/100 | HIGH 55/100 | Watch |

**Same-run overlap:** VVV/USD, NEAR/USD, SUI/USD, ETH/USD, LINK/USD, SOL/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
