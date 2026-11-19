# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-19T04:50:22.494370+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/44460944609
**Source SHA:** b271b90a2cae9e5307600070ce7d0e510fe68996
**Previous ledger commit:** 6765eef7b8074f21022b1b8608426f9a68eabda8 (atomic ledger/results publication)
**Ledger generation:** 759 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 8s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 627; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 609; valid market observations: 609; OHLC screened: 24.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | VVV/USD | 22.626 | 91.192 | 81.980 | +4.41% | -0.05% | 1.95x | 5.7 | 2026-11-19T04:50:14.552004+00:00 | Not calibrated | MODERATE 66/100 | HIGH 61/100 | Watch | WATCH |
| 2 | HYPE/USD | 67.73 | 76.028 | 63.158 | +1.27% | +0.33% | 2.12x | 1.5 | 2026-11-19T04:50:14.552004+00:00 | Not calibrated | STRONG 93/100 | HIGH 55/100 | Consider small entry | WATCH |
| 3 | NEAR/USD | 3.4008 | 69.296 | 75.333 | +3.14% | -0.25% | 0.52x | 3.2 | 2026-11-19T04:50:14.552004+00:00 | Not calibrated | WEAK 40/100 | VERY_HIGH 76/100 | Watch | WATCH |
| 4 | ZEC/USD | 933.26 | 66.022 | 69.107 | +2.34% | +0.37% | 0.51x | 4.5 | 2026-11-19T04:50:14.552004+00:00 | Not calibrated | MODERATE 63/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 5 | TAO/USD | 195.7713 | 65.937 | 65.169 | +1.99% | +0.26% | 0.95x | 7.5 | 2026-11-19T04:50:14.552004+00:00 | Not calibrated | MODERATE 63/100 | HIGH 62/100 | Watch | WATCH |
| 6 | LUNA/USD | 4.811e-05 | 65.846 | 66.952 | +10.50% | -1.24% | 1.51x | 22.9 | 2026-11-19T04:50:14.552004+00:00 | Not calibrated | WEAK 43/100 | VERY_HIGH 82/100 | Do nothing | WATCH |
| 7 | ADA/USD | 0.153048 | 65.646 | 61.537 | +1.19% | +0.27% | 1.28x | 3.5 | 2026-11-19T04:50:14.552004+00:00 | Not calibrated | MODERATE 68/100 | HIGH 55/100 | Watch | WATCH |
| 8 | SOL/USD | 74.57 | 63.278 | 64.134 | +1.40% | -0.04% | 0.93x | 1.3 | 2026-11-19T04:50:14.552004+00:00 | Not calibrated | WEAK 37/100 | HIGH 68/100 | Watch | WATCH |
| 9 | XBT/USD | 63572.8 | 62.155 | 61.530 | +0.93% | +0.32% | 0.90x | 0.0 | 2026-11-19T04:50:14.552004+00:00 | Not calibrated | MODERATE 61/100 | HIGH 62/100 | Watch | WATCH |
| 10 | ETH/USD | 1799.96 | 59.433 | 64.912 | +1.42% | +0.21% | 0.35x | 0.1 | 2026-11-19T04:50:14.552004+00:00 | Not calibrated | MODERATE 60/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 11 | XRP/USD | 0.97566 | 58.583 | 61.268 | +0.96% | +0.42% | 0.52x | 0.9 | 2026-11-19T04:50:14.552004+00:00 | Not calibrated | MODERATE 59/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 12 | USELESS/USD | 0.10061 | 58.102 | 65.254 | +5.28% | +0.07% | 0.25x | 19.0 | 2026-11-19T04:50:14.552004+00:00 | Not calibrated | WEAK 44/100 | VERY_HIGH 76/100 | Watch | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | VVV/USD | 81.980 | 22.626 | -0.05% | 1.95x |
| 2 | NEAR/USD | 75.333 | 3.4008 | -0.25% | 0.52x |
| 3 | ZEC/USD | 69.107 | 933.26 | +0.37% | 0.51x |
| 4 | LUNA/USD | 66.952 | 4.811e-05 | -1.24% | 1.51x |
| 5 | USELESS/USD | 65.254 | 0.10061 | +0.07% | 0.25x |
| 6 | TAO/USD | 65.169 | 195.7713 | +0.26% | 0.95x |
| 7 | ETH/USD | 64.912 | 1799.96 | +0.21% | 0.35x |
| 8 | SOL/USD | 64.134 | 74.57 | -0.04% | 0.93x |
| 9 | HYPE/USD | 63.158 | 67.73 | +0.33% | 2.12x |
| 10 | ADA/USD | 61.537 | 0.153048 | +0.27% | 1.28x |
| 11 | XBT/USD | 61.530 | 63572.8 | +0.32% | 0.90x |
| 12 | XRP/USD | 61.268 | 0.97566 | +0.42% | 0.52x |

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

- Persisted scans: 759; predictions: 6252; observations: 459237.
- Matured sampled outcomes across 1/6/24/48h: 6236; gap abstentions: 13689. Per-horizon counts require independent audit; do not infer held-out lift.
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

**Writer:** 44460944609 · **Generation:** 759 · **Legacy run:** 44460944609
**Main quote time:** 2026-11-19T04:50:22.494370+00:00 · **Legacy report time:** 2026-11-19T04:50:57.149048+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | VVV/USD | 22.626 | 91.19 | -0.05% | 1.95x | MODERATE 66/100 | HIGH 61/100 | Watch |
| 2 | HYPE/USD ⭐ | 67.73 | 76.03 | +0.33% | 2.12x | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 3 | NEAR/USD | 3.4008 | 69.30 | -0.25% | 0.52x | WEAK 40/100 | VERY_HIGH 76/100 | Watch |
| 4 | ZEC/USD | 933.26 | 66.02 | +0.37% | 0.51x | MODERATE 63/100 | VERY_HIGH 70/100 | Watch |
| 5 | TAO/USD | 195.7713 | 65.94 | +0.26% | 0.95x | MODERATE 63/100 | HIGH 62/100 | Watch |
| 6 | LUNA/USD | 4.811e-05 | 65.85 | -1.24% | 1.51x | WEAK 43/100 | VERY_HIGH 82/100 | Do nothing |
| 7 | ADA/USD | 0.153048 | 65.65 | +0.27% | 1.28x | MODERATE 68/100 | HIGH 55/100 | Watch |
| 8 | SOL/USD | 74.57 | 63.28 | -0.04% | 0.93x | WEAK 37/100 | HIGH 68/100 | Watch |
| 9 | XBT/USD | 63572.8 | 62.15 | +0.32% | 0.90x | MODERATE 61/100 | HIGH 62/100 | Watch |
| 10 | ETH/USD | 1799.96 | 59.43 | +0.21% | 0.35x | MODERATE 60/100 | VERY_HIGH 70/100 | Watch |
| 11 | XRP/USD | 0.97566 | 58.58 | +0.42% | 0.52x | MODERATE 59/100 | VERY_HIGH 70/100 | Watch |
| 12 | USELESS/USD | 0.10061 | 58.10 | +0.07% | 0.25x | WEAK 44/100 | VERY_HIGH 76/100 | Watch |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | HYPE/USD ⭐ | 67.74 | 69.95 | +0.33% | 2.12x | 14607 | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 2 | AKT/USD | 0.5354 | 69.24 | +0.47% | 1.20x | 3471 | STRONG 70/100 | VERY_HIGH 74/100 | Watch |

**Same-run overlap:** HYPE/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
