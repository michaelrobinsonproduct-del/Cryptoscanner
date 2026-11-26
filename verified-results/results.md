# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-26T01:56:00.697340+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/45738880050
**Source SHA:** 858c8bc8ec5d7641ddb39cacd8aca91719f855b1
**Previous ledger commit:** 26591441750cf496d14d348a38900eed8b98dca9 (atomic ledger/results publication)
**Ledger generation:** 1796 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 9s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 628; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 610; valid market observations: 609; OHLC screened: 24.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | LTC/USD | 43.43 | 81.229 | 64.496 | +1.69% | +0.35% | 3.99x | 4.6 | 2026-11-26T01:55:52.169985+00:00 | Not calibrated | STRONG 96/100 | HIGH 55/100 | Consider small entry | WATCH |
| 2 | INJ/USD | 6.121 | 77.950 | 58.340 | +2.80% | +0.92% | 4.30x | 4.9 | 2026-11-26T01:55:52.169985+00:00 | Not calibrated | STRONG 94/100 | HIGH 55/100 | Consider small entry | WATCH |
| 3 | TAO/USD | 184.5063 | 73.207 | 62.995 | +1.60% | +0.18% | 1.93x | 6.5 | 2026-11-26T01:55:52.169985+00:00 | Not calibrated | STRONG 72/100 | HIGH 55/100 | Watch | WATCH |
| 4 | PEARL/USD | 2.0416 | 72.908 | 56.154 | +2.32% | +1.60% | 1.87x | 0.5 | 2026-11-26T01:55:52.169985+00:00 | Not calibrated | STRONG 81/100 | HIGH 55/100 | Consider small entry | WATCH |
| 5 | XBT/USD | 60849.6 | 72.898 | 60.569 | +0.80% | +0.37% | 2.05x | 0.0 | 2026-11-26T01:55:52.169985+00:00 | Not calibrated | STRONG 91/100 | HIGH 55/100 | Consider small entry | WATCH |
| 6 | VVV/USD | 30.076 | 68.749 | 70.639 | +3.02% | -0.05% | 0.83x | 11.0 | 2026-11-26T01:55:52.169985+00:00 | Not calibrated | WEAK 34/100 | VERY_HIGH 74/100 | Do nothing | WATCH |
| 7 | XRP/USD | 0.95027 | 67.142 | 64.721 | +1.46% | +0.57% | 0.95x | 1.1 | 2026-11-26T01:55:52.169985+00:00 | Not calibrated | MODERATE 64/100 | HIGH 62/100 | Watch | WATCH |
| 8 | ZEC/USD | 778.71 | 62.491 | 60.862 | +1.10% | +1.12% | 0.60x | 3.7 | 2026-11-26T01:55:52.169985+00:00 | Not calibrated | MODERATE 61/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 9 | SUI/USD | 0.6756 | 60.565 | 64.030 | +1.40% | +0.22% | 0.54x | 1.5 | 2026-11-26T01:55:52.169985+00:00 | Not calibrated | MODERATE 60/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 10 | ETH/USD | 1701.96 | 59.842 | 59.754 | +0.68% | +0.21% | 0.90x | 0.1 | 2026-11-26T01:55:52.169985+00:00 | Not calibrated | MODERATE 60/100 | HIGH 62/100 | Watch | WATCH |
| 11 | ADA/USD | 0.147469 | 59.691 | 60.854 | +1.17% | +0.22% | 0.77x | 4.6 | 2026-11-26T01:55:52.169985+00:00 | Not calibrated | MODERATE 60/100 | HIGH 62/100 | Watch | WATCH |
| 12 | NEAR/USD | 3.1053 | 59.486 | 64.492 | +1.82% | +0.62% | 0.19x | 6.4 | 2026-11-26T01:55:52.169985+00:00 | Not calibrated | MODERATE 60/100 | VERY_HIGH 70/100 | Watch | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | VVV/USD | 70.639 | 30.076 | -0.05% | 0.83x |
| 2 | XRP/USD | 64.721 | 0.95027 | +0.57% | 0.95x |
| 3 | LTC/USD | 64.496 | 43.43 | +0.35% | 3.99x |
| 4 | NEAR/USD | 64.492 | 3.1053 | +0.62% | 0.19x |
| 5 | SUI/USD | 64.030 | 0.6756 | +0.22% | 0.54x |
| 6 | TAO/USD | 62.995 | 184.5063 | +0.18% | 1.93x |
| 7 | ZEC/USD | 60.862 | 778.71 | +1.12% | 0.60x |
| 8 | ADA/USD | 60.854 | 0.147469 | +0.22% | 0.77x |
| 9 | XBT/USD | 60.569 | 60849.6 | +0.37% | 2.05x |
| 10 | ETH/USD | 59.754 | 1701.96 | +0.21% | 0.90x |
| 11 | INJ/USD | 58.340 | 6.121 | +0.92% | 4.30x |
| 12 | PEARL/USD | 56.154 | 2.0416 | +1.60% | 1.87x |

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

- Persisted scans: 1796; predictions: 15287; observations: 1088808.
- Matured sampled outcomes across 1/6/24/48h: 33215; gap abstentions: 23630. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 146 (sampled only; not a success-rate estimate).
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

**Writer:** 45738880050 · **Generation:** 1796 · **Legacy run:** 45738880050
**Main quote time:** 2026-11-26T01:56:00.697340+00:00 · **Legacy report time:** 2026-11-26T01:57:05.347845+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | LTC/USD ⭐ | 43.43 | 81.23 | +0.35% | 3.99x | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 2 | INJ/USD | 6.121 | 77.95 | +0.92% | 4.30x | STRONG 94/100 | HIGH 55/100 | Consider small entry |
| 3 | TAO/USD | 184.5063 | 73.21 | +0.18% | 1.93x | STRONG 72/100 | HIGH 55/100 | Watch |
| 4 | PEARL/USD | 2.0416 | 72.91 | +1.60% | 1.87x | STRONG 81/100 | HIGH 55/100 | Consider small entry |
| 5 | XBT/USD | 60849.6 | 72.90 | +0.37% | 2.05x | STRONG 91/100 | HIGH 55/100 | Consider small entry |
| 6 | VVV/USD | 30.076 | 68.75 | -0.05% | 0.83x | WEAK 34/100 | VERY_HIGH 74/100 | Do nothing |
| 7 | XRP/USD | 0.95027 | 67.14 | +0.57% | 0.95x | MODERATE 64/100 | HIGH 62/100 | Watch |
| 8 | ZEC/USD | 778.71 | 62.49 | +1.12% | 0.60x | MODERATE 61/100 | VERY_HIGH 70/100 | Watch |
| 9 | SUI/USD | 0.6756 | 60.56 | +0.22% | 0.54x | MODERATE 60/100 | VERY_HIGH 70/100 | Watch |
| 10 | ETH/USD | 1701.96 | 59.84 | +0.21% | 0.90x | MODERATE 60/100 | HIGH 62/100 | Watch |
| 11 | ADA/USD | 0.147469 | 59.69 | +0.22% | 0.77x | MODERATE 60/100 | HIGH 62/100 | Watch |
| 12 | NEAR/USD | 3.1053 | 59.49 | +0.62% | 0.19x | MODERATE 60/100 | VERY_HIGH 70/100 | Watch |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | PIEVERSE/USD | 3.8623 | 81.43 | +2.04% | 3.14x | 1990 | STRONG 86/100 | VERY_HIGH 72/100 | Watch |
| 2 | ME/USD | 0.0401 | 77.08 | +1.51% | 2.84x | 1947 | STRONG 79/100 | EXTREME 89/100 | Do nothing |
| 3 | ZRO/USD | 1.055 | 75.18 | +0.86% | 3.14x | 3754 | STRONG 88/100 | HIGH 61/100 | Consider small entry |
| 4 | LTC/USD ⭐ | 43.37 | 74.97 | +0.35% | 3.99x | 14711 | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 5 | LUNA/USD | 4.798e-05 | 71.14 | +0.17% | 2.30x | 1938 | MODERATE 66/100 | VERY_HIGH 82/100 | Watch |
| 6 | PEPE/USD | 3.545e-06 | 63.89 | +0.57% | 1.19x | 7064 | MODERATE 67/100 | HIGH 62/100 | Watch |

**Same-run overlap:** LTC/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
