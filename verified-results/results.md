# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-24T04:31:31.195593+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/45326763284
**Source SHA:** 858c8bc8ec5d7641ddb39cacd8aca91719f855b1
**Previous ledger commit:** c07f273bc2b304c98c5c00b09513453b23dfb6ef (atomic ledger/results publication)
**Ledger generation:** 1525 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 8s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 628; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 610; valid market observations: 609; OHLC screened: 24.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | MON/USD | 0.0128 | 97.309 | 77.402 | +11.11% | +2.81% | 1.58x | 15.7 | 2026-11-24T04:31:23.437289+00:00 | Not calibrated | STRONG 89/100 | HIGH 61/100 | Consider small entry | WATCH |
| 2 | VVV/USD | 25.069 | 74.670 | 68.592 | +2.54% | +0.80% | 1.21x | 8.4 | 2026-11-24T04:31:23.437289+00:00 | Not calibrated | STRONG 72/100 | HIGH 62/100 | Watch | WATCH |
| 3 | AAVE/USD | 98.24 | 71.022 | 54.439 | +1.23% | +0.32% | 8.62x | 5.1 | 2026-11-24T04:31:23.437289+00:00 | Not calibrated | STRONG 91/100 | HIGH 55/100 | Consider small entry | WATCH |
| 4 | HYPE/USD | 63.8 | 70.233 | 55.976 | +0.25% | +0.41% | 2.22x | 1.6 | 2026-11-24T04:31:23.437289+00:00 | Not calibrated | STRONG 90/100 | HIGH 55/100 | Consider small entry | WATCH |
| 5 | UNI/USD | 4.8651 | 69.594 | 51.932 | +0.56% | +0.53% | 6.11x | 4.7 | 2026-11-24T04:31:23.437289+00:00 | Not calibrated | STRONG 90/100 | HIGH 55/100 | Watch | WATCH |
| 6 | LINK/USD | 9.07468 | 69.411 | 60.416 | +0.77% | +0.29% | 1.76x | 0.0 | 2026-11-24T04:31:23.437289+00:00 | Not calibrated | STRONG 80/100 | HIGH 55/100 | Watch | WATCH |
| 7 | PEPE/USD | 3.502e-06 | 68.254 | 64.847 | +2.34% | +0.43% | 1.13x | 2.9 | 2026-11-24T04:31:23.437289+00:00 | Not calibrated | MODERATE 69/100 | HIGH 62/100 | Watch | WATCH |
| 8 | AI/USD | 0.01616 | 67.484 | 61.596 | +6.11% | -1.82% | 2.66x | 24.6 | 2026-11-24T04:31:23.437289+00:00 | Not calibrated | MODERATE 54/100 | EXTREME 89/100 | Do nothing | WATCH |
| 9 | NEAR/USD | 2.9933 | 65.630 | 56.338 | +0.41% | +0.12% | 1.87x | 3.0 | 2026-11-24T04:31:23.437289+00:00 | Not calibrated | MODERATE 68/100 | HIGH 55/100 | Watch | WATCH |
| 10 | XMR/USD | 491.35 | 65.136 | 58.195 | +1.10% | +0.28% | 1.56x | 9.0 | 2026-11-24T04:31:23.437289+00:00 | Not calibrated | STRONG 78/100 | HIGH 55/100 | Watch | WATCH |
| 11 | BABY/USD | 0.00895 | 65.079 | 56.953 | +5.29% | +1.94% | 0.84x | 22.5 | 2026-11-24T04:31:23.437289+00:00 | Not calibrated | MODERATE 53/100 | EXTREME 86/100 | Do nothing | WATCH |
| 12 | XRP/USD | 0.9529 | 65.038 | 64.595 | +1.44% | +0.39% | 0.85x | 0.9 | 2026-11-24T04:31:23.437289+00:00 | Not calibrated | MODERATE 63/100 | HIGH 62/100 | Watch | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | MON/USD | 77.402 | 0.0128 | +2.81% | 1.58x |
| 2 | VVV/USD | 68.592 | 25.069 | +0.80% | 1.21x |
| 3 | PEPE/USD | 64.847 | 3.502e-06 | +0.43% | 1.13x |
| 4 | XRP/USD | 64.595 | 0.9529 | +0.39% | 0.85x |
| 5 | AI/USD | 61.596 | 0.01616 | -1.82% | 2.66x |
| 6 | LINK/USD | 60.416 | 9.07468 | +0.29% | 1.76x |
| 7 | XMR/USD | 58.195 | 491.35 | +0.28% | 1.56x |
| 8 | BABY/USD | 56.953 | 0.00895 | +1.94% | 0.84x |
| 9 | NEAR/USD | 56.338 | 2.9933 | +0.12% | 1.87x |
| 10 | HYPE/USD | 55.976 | 63.8 | +0.41% | 2.22x |
| 11 | AAVE/USD | 54.439 | 98.24 | +0.32% | 8.62x |
| 12 | UNI/USD | 51.932 | 4.8651 | +0.53% | 6.11x |

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

- Persisted scans: 1525; predictions: 13033; observations: 923823.
- Matured sampled outcomes across 1/6/24/48h: 24300; gap abstentions: 22370. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 135 (sampled only; not a success-rate estimate).
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

**Writer:** 45326763284 · **Generation:** 1525 · **Legacy run:** 45326763284
**Main quote time:** 2026-11-24T04:31:31.195593+00:00 · **Legacy report time:** 2026-11-24T04:32:29.543679+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | MON/USD ⭐ | 0.0128 | 97.31 | +2.81% | 1.58x | STRONG 99/100 | HIGH 61/100 | Consider small entry |
| 2 | VVV/USD ⭐ | 25.069 | 74.67 | +0.80% | 1.21x | STRONG 82/100 | HIGH 62/100 | Watch |
| 3 | AAVE/USD ⭐ | 98.24 | 71.02 | +0.32% | 8.62x | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 4 | HYPE/USD ⭐ | 63.8 | 70.23 | +0.41% | 2.22x | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 5 | UNI/USD | 4.8651 | 69.59 | +0.53% | 6.11x | STRONG 90/100 | HIGH 55/100 | Watch |
| 6 | LINK/USD ⭐ | 9.07468 | 69.41 | +0.29% | 1.76x | STRONG 90/100 | HIGH 55/100 | Consider small entry |
| 7 | PEPE/USD ⭐ | 3.502e-06 | 68.25 | +0.43% | 1.13x | STRONG 79/100 | HIGH 62/100 | Watch |
| 8 | AI/USD | 0.01616 | 67.48 | -1.82% | 2.66x | MODERATE 54/100 | EXTREME 89/100 | Do nothing |
| 9 | NEAR/USD ⭐ | 2.9933 | 65.63 | +0.12% | 1.87x | STRONG 78/100 | HIGH 55/100 | Watch |
| 10 | XMR/USD ⭐ | 491.35 | 65.14 | +0.28% | 1.56x | STRONG 88/100 | HIGH 55/100 | Consider small entry |
| 11 | BABY/USD | 0.00895 | 65.08 | +1.94% | 0.84x | MODERATE 53/100 | EXTREME 86/100 | Do nothing |
| 12 | XRP/USD | 0.9529 | 65.04 | +0.39% | 0.85x | MODERATE 63/100 | HIGH 62/100 | Watch |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | MON/USD ⭐ | 0.01279 | 86.47 | +2.81% | 1.58x | 8758 | STRONG 93/100 | HIGH 61/100 | Consider small entry |
| 2 | VVV/USD ⭐ | 25.091 | 71.79 | +0.80% | 1.21x | 13557 | STRONG 81/100 | HIGH 62/100 | Watch |
| 3 | PEPE/USD ⭐ | 3.497e-06 | 65.59 | +0.43% | 1.13x | 9348 | STRONG 78/100 | HIGH 62/100 | Watch |
| 4 | AAVE/USD ⭐ | 98.01 | 60.67 | +0.32% | 8.62x | 6602 | STRONG 95/100 | HIGH 55/100 | Consider small entry |
| 5 | LINK/USD ⭐ | 9.07468 | 59.36 | +0.29% | 1.76x | 8854 | STRONG 85/100 | HIGH 55/100 | Consider small entry |
| 6 | XMR/USD ⭐ | 491.84 | 58.85 | +0.28% | 1.56x | 11891 | STRONG 84/100 | HIGH 55/100 | Consider small entry |
| 7 | HYPE/USD ⭐ | 63.81 | 58.18 | +0.41% | 2.22x | 30399 | STRONG 94/100 | HIGH 55/100 | Consider small entry |
| 8 | NEAR/USD ⭐ | 2.9942 | 55.06 | +0.12% | 1.87x | 23683 | STRONG 73/100 | HIGH 55/100 | Watch |

**Same-run overlap:** MON/USD, VVV/USD, AAVE/USD, HYPE/USD, LINK/USD, PEPE/USD, NEAR/USD, XMR/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
