# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-22T21:11:10.080361+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/45070505211
**Source SHA:** 193371a597e6dbc5a6a884defbe9e1519a6a183a
**Previous ledger commit:** fb1b361906eea0fa2d72e92590f28150ce87372b (atomic ledger/results publication)
**Ledger generation:** 1336 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 7s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 628; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 610; valid market observations: 609; OHLC screened: 24.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | NIGHT/USD | 0.04888 | 108.572 | 89.027 | +10.39% | +0.91% | 3.25x | 8.2 | 2026-11-22T21:11:03.440621+00:00 | Not calibrated | STRONG 100/100 | HIGH 55/100 | Consider small entry | WATCH |
| 2 | HYPE/USD | 62.84 | 86.625 | 71.698 | +2.61% | +0.30% | 2.34x | 3.2 | 2026-11-22T21:11:03.440621+00:00 | Not calibrated | STRONG 98/100 | HIGH 55/100 | Consider small entry | WATCH |
| 3 | ETH/USD | 1719.52 | 85.955 | 70.467 | +2.21% | +0.10% | 2.57x | 0.1 | 2026-11-22T21:11:03.440621+00:00 | Not calibrated | STRONG 88/100 | HIGH 55/100 | Watch | WATCH |
| 4 | NEAR/USD | 2.9811 | 80.808 | 75.980 | +3.28% | +0.46% | 1.25x | 4.0 | 2026-11-22T21:11:03.440621+00:00 | Not calibrated | STRONG 75/100 | HIGH 55/100 | Watch | WATCH |
| 5 | VVV/USD | 26.095 | 79.851 | 84.185 | +4.80% | +0.00% | 0.56x | 8.8 | 2026-11-22T21:11:03.440621+00:00 | Not calibrated | MODERATE 60/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 6 | PUMP/USD | 0.002571 | 79.384 | 82.662 | +9.68% | -0.08% | 0.71x | 7.8 | 2026-11-22T21:11:03.440621+00:00 | Not calibrated | MODERATE 45/100 | VERY_HIGH 76/100 | Watch | WATCH |
| 7 | DRV/USD | 0.37448 | 73.236 | 75.739 | +11.72% | +0.26% | 0.62x | 27.0 | 2026-11-22T21:11:03.440621+00:00 | Not calibrated | MODERATE 57/100 | VERY_HIGH 82/100 | Watch | WATCH |
| 8 | STBL/USD | 0.017109 | 69.507 | 67.215 | +6.90% | -0.09% | 1.27x | 17.6 | 2026-11-22T21:11:03.440621+00:00 | Not calibrated | WEAK 40/100 | VERY_HIGH 79/100 | Watch | WATCH |
| 9 | ZEC/USD | 792.97 | 65.878 | 67.115 | +1.90% | +0.61% | 0.57x | 2.4 | 2026-11-22T21:11:03.440621+00:00 | Not calibrated | MODERATE 63/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 10 | XBT/USD | 60804.6 | 64.281 | 63.318 | +1.19% | -0.03% | 1.11x | 0.0 | 2026-11-22T21:11:03.440621+00:00 | Not calibrated | WEAK 42/100 | HIGH 68/100 | Watch | WATCH |
| 11 | BNB/USD | 556.77 | 58.596 | 47.747 | +1.71% | +0.05% | 2.06x | 2.0 | 2026-11-22T21:11:03.440621+00:00 | Not calibrated | STRONG 74/100 | HIGH 55/100 | Watch | WATCH |
| 12 | KAS/USD | 0.02561 | 49.285 | 32.330 | +0.75% | +0.39% | 4.37x | 11.7 | 2026-11-22T21:11:03.440621+00:00 | Not calibrated | STRONG 75/100 | HIGH 66/100 | Watch | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | NIGHT/USD | 89.027 | 0.04888 | +0.91% | 3.25x |
| 2 | VVV/USD | 84.185 | 26.095 | +0.00% | 0.56x |
| 3 | PUMP/USD | 82.662 | 0.002571 | -0.08% | 0.71x |
| 4 | NEAR/USD | 75.980 | 2.9811 | +0.46% | 1.25x |
| 5 | DRV/USD | 75.739 | 0.37448 | +0.26% | 0.62x |
| 6 | HYPE/USD | 71.698 | 62.84 | +0.30% | 2.34x |
| 7 | ETH/USD | 70.467 | 1719.52 | +0.10% | 2.57x |
| 8 | STBL/USD | 67.215 | 0.017109 | -0.09% | 1.27x |
| 9 | ZEC/USD | 67.115 | 792.97 | +0.61% | 0.57x |
| 10 | XBT/USD | 63.318 | 60804.6 | -0.03% | 1.11x |
| 11 | BNB/USD | 47.747 | 556.77 | +0.05% | 2.06x |
| 12 | KAS/USD | 32.330 | 0.02561 | +0.39% | 4.37x |

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

- Persisted scans: 1336; predictions: 10951; observations: 808732.
- Matured sampled outcomes across 1/6/24/48h: 16701; gap abstentions: 22360. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 61 (sampled only; not a success-rate estimate).
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

**Writer:** 45070505211 · **Generation:** 1336 · **Legacy run:** 45070505211
**Main quote time:** 2026-11-22T21:11:10.080361+00:00 · **Legacy report time:** 2026-11-22T21:12:05.194491+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | NIGHT/USD ⭐ | 0.04888 | 108.57 | +0.91% | 3.25x | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 2 | HYPE/USD ⭐ | 62.84 | 86.62 | +0.30% | 2.34x | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 3 | ETH/USD ⭐ | 1719.52 | 85.96 | +0.10% | 2.57x | STRONG 98/100 | HIGH 55/100 | Watch |
| 4 | NEAR/USD ⭐ | 2.9811 | 80.81 | +0.46% | 1.25x | STRONG 85/100 | HIGH 55/100 | Watch |
| 5 | VVV/USD | 26.095 | 79.85 | +0.00% | 0.56x | MODERATE 60/100 | VERY_HIGH 70/100 | Watch |
| 6 | PUMP/USD | 0.002571 | 79.38 | -0.08% | 0.71x | MODERATE 45/100 | VERY_HIGH 76/100 | Watch |
| 7 | DRV/USD | 0.37448 | 73.24 | +0.26% | 0.62x | MODERATE 57/100 | VERY_HIGH 82/100 | Watch |
| 8 | STBL/USD | 0.017109 | 69.51 | -0.09% | 1.27x | WEAK 40/100 | VERY_HIGH 79/100 | Watch |
| 9 | ZEC/USD | 792.97 | 65.88 | +0.61% | 0.57x | MODERATE 63/100 | VERY_HIGH 70/100 | Watch |
| 10 | XBT/USD | 60804.6 | 64.28 | -0.03% | 1.11x | WEAK 42/100 | HIGH 68/100 | Watch |
| 11 | BNB/USD | 556.77 | 58.60 | +0.05% | 2.06x | STRONG 74/100 | HIGH 55/100 | Watch |
| 12 | KAS/USD | 0.02561 | 49.28 | +0.39% | 4.37x | STRONG 75/100 | HIGH 66/100 | Watch |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | NIGHT/USD ⭐ | 0.04888 | 94.30 | +0.91% | 3.25x | 9950 | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 2 | NEAR/USD ⭐ | 2.9882 | 90.73 | +0.46% | 1.25x | 12675 | STRONG 90/100 | HIGH 55/100 | Watch |
| 3 | HYPE/USD ⭐ | 62.84 | 86.45 | +0.30% | 2.34x | 9884 | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 4 | ETH/USD ⭐ | 1721.48 | 86.40 | +0.10% | 2.57x | 38495 | STRONG 98/100 | HIGH 55/100 | Watch |
| 5 | ZBCN/USD | 0.00183 | 76.12 | +0.82% | 1.21x | 6152 | MODERATE 58/100 | VERY_HIGH 79/100 | Watch |

**Same-run overlap:** NIGHT/USD, HYPE/USD, ETH/USD, NEAR/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
