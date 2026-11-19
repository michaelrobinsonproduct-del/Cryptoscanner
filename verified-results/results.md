# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-19T14:20:30.149146+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/44542503442
**Source SHA:** f854bf15990e1aa3564d35bbec4100f929bd3d42
**Previous ledger commit:** 8e1fe56e80da363a17cd6620ce1e82324f28d077 (atomic ledger/results publication)
**Ledger generation:** 791 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 8s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 627; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 609; valid market observations: 594; OHLC screened: 24.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | PUMP/USD | 0.002752 | 100.613 | 83.423 | +6.01% | +0.44% | 5.88x | 7.3 | 2026-11-19T14:20:22.120913+00:00 | Not calibrated | STRONG 100/100 | HIGH 55/100 | Consider small entry | WATCH |
| 2 | VVV/USD | 23.309 | 96.101 | 96.122 | +7.56% | +0.67% | 0.66x | 7.8 | 2026-11-19T14:20:22.120913+00:00 | Not calibrated | STRONG 78/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 3 | TAO/USD | 199.5932 | 92.532 | 79.080 | +3.98% | +0.11% | 2.29x | 7.5 | 2026-11-19T14:20:22.120913+00:00 | Not calibrated | STRONG 91/100 | HIGH 55/100 | Watch | WATCH |
| 4 | PYTH/USD | 0.05709 | 87.575 | 72.775 | +8.21% | +0.90% | 2.03x | 8.8 | 2026-11-19T14:20:22.120913+00:00 | Not calibrated | STRONG 99/100 | HIGH 60/100 | Consider small entry | WATCH |
| 5 | XBT/USD | 63850.1 | 78.890 | 64.612 | +1.37% | -0.14% | 2.62x | 0.0 | 2026-11-19T14:20:22.120913+00:00 | Not calibrated | MODERATE 69/100 | HIGH 61/100 | Watch | WATCH |
| 6 | SOL/USD | 75.07 | 78.827 | 68.897 | +2.08% | -0.04% | 2.01x | 1.3 | 2026-11-19T14:20:22.120913+00:00 | Not calibrated | MODERATE 69/100 | HIGH 61/100 | Watch | WATCH |
| 7 | XDG/USD | 0.0596045 | 76.595 | 62.050 | +1.53% | -0.09% | 5.81x | 0.2 | 2026-11-19T14:20:22.120913+00:00 | Not calibrated | MODERATE 68/100 | HIGH 61/100 | Watch | WATCH |
| 8 | ZEC/USD | 945.77 | 75.154 | 79.320 | +3.71% | -0.06% | 0.61x | 3.3 | 2026-11-19T14:20:22.120913+00:00 | Not calibrated | WEAK 43/100 | VERY_HIGH 76/100 | Watch | WATCH |
| 9 | NEAR/USD | 3.3866 | 71.907 | 72.165 | +2.71% | -0.00% | 0.98x | 3.5 | 2026-11-19T14:20:22.120913+00:00 | Not calibrated | WEAK 41/100 | HIGH 68/100 | Watch | WATCH |
| 10 | ETH/USD | 1807.36 | 71.152 | 67.830 | +1.84% | -0.21% | 1.44x | 0.1 | 2026-11-19T14:20:22.120913+00:00 | Not calibrated | MODERATE 56/100 | HIGH 61/100 | Watch | WATCH |
| 11 | ADA/USD | 0.155246 | 70.746 | 71.832 | +2.64% | -0.07% | 0.92x | 3.3 | 2026-11-19T14:20:22.120913+00:00 | Not calibrated | WEAK 40/100 | HIGH 68/100 | Watch | WATCH |
| 12 | XRP/USD | 0.98982 | 67.355 | 71.683 | +2.43% | -0.26% | 0.70x | 0.6 | 2026-11-19T14:20:22.120913+00:00 | Not calibrated | WEAK 39/100 | VERY_HIGH 76/100 | Watch | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | VVV/USD | 96.122 | 23.309 | +0.67% | 0.66x |
| 2 | PUMP/USD | 83.423 | 0.002752 | +0.44% | 5.88x |
| 3 | ZEC/USD | 79.320 | 945.77 | -0.06% | 0.61x |
| 4 | TAO/USD | 79.080 | 199.5932 | +0.11% | 2.29x |
| 5 | PYTH/USD | 72.775 | 0.05709 | +0.90% | 2.03x |
| 6 | NEAR/USD | 72.165 | 3.3866 | -0.00% | 0.98x |
| 7 | ADA/USD | 71.832 | 0.155246 | -0.07% | 0.92x |
| 8 | XRP/USD | 71.683 | 0.98982 | -0.26% | 0.70x |
| 9 | SOL/USD | 68.897 | 75.07 | -0.04% | 2.01x |
| 10 | ETH/USD | 67.830 | 1807.36 | -0.21% | 1.44x |
| 11 | XBT/USD | 64.612 | 63850.1 | -0.14% | 2.62x |
| 12 | XDG/USD | 62.050 | 0.0596045 | -0.09% | 5.81x |

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

- Persisted scans: 791; predictions: 6636; observations: 478482.
- Matured sampled outcomes across 1/6/24/48h: 6671; gap abstentions: 15062. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 10 (sampled only; not a success-rate estimate).
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

**Writer:** 44542503442 · **Generation:** 791 · **Legacy run:** 44542503442
**Main quote time:** 2026-11-19T14:20:30.149146+00:00 · **Legacy report time:** 2026-11-19T14:21:12.869789+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | PUMP/USD ⭐ | 0.002752 | 100.61 | +0.44% | 5.88x | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 2 | VVV/USD | 23.309 | 96.10 | +0.67% | 0.66x | STRONG 78/100 | VERY_HIGH 70/100 | Watch |
| 3 | TAO/USD ⭐ | 199.5932 | 92.53 | +0.11% | 2.29x | STRONG 100/100 | HIGH 55/100 | Watch |
| 4 | PYTH/USD | 0.05709 | 87.58 | +0.90% | 2.03x | STRONG 99/100 | HIGH 60/100 | Consider small entry |
| 5 | XBT/USD | 63850.1 | 78.89 | -0.14% | 2.62x | MODERATE 69/100 | HIGH 61/100 | Watch |
| 6 | SOL/USD | 75.07 | 78.83 | -0.04% | 2.01x | MODERATE 69/100 | HIGH 61/100 | Watch |
| 7 | XDG/USD | 0.0596045 | 76.60 | -0.09% | 5.81x | MODERATE 68/100 | HIGH 61/100 | Watch |
| 8 | ZEC/USD | 945.77 | 75.15 | -0.06% | 0.61x | WEAK 43/100 | VERY_HIGH 76/100 | Watch |
| 9 | NEAR/USD | 3.3866 | 71.91 | -0.00% | 0.98x | WEAK 41/100 | HIGH 68/100 | Watch |
| 10 | ETH/USD | 1807.36 | 71.15 | -0.21% | 1.44x | MODERATE 56/100 | HIGH 61/100 | Watch |
| 11 | ADA/USD | 0.155246 | 70.75 | -0.07% | 0.92x | WEAK 40/100 | HIGH 68/100 | Watch |
| 12 | XRP/USD | 0.98982 | 67.35 | -0.26% | 0.70x | WEAK 39/100 | VERY_HIGH 76/100 | Watch |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | TAO/USD ⭐ | 199.5203 | 93.77 | +0.11% | 2.29x | 6121 | STRONG 100/100 | HIGH 55/100 | Watch |
| 2 | PUMP/USD ⭐ | 0.002752 | 88.75 | +0.44% | 5.88x | 4891 | STRONG 100/100 | HIGH 55/100 | Consider small entry |

**Same-run overlap:** PUMP/USD, TAO/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
