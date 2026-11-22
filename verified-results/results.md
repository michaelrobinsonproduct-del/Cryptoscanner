# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-22T15:11:14.208646+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/45036737957
**Source SHA:** 17af11513c515cf2dc9dda8017f091d9b1f13397
**Previous ledger commit:** 66a24bc03e18fcda0425e3d18f1327270148f902 (atomic ledger/results publication)
**Ledger generation:** 1299 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 8s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 628; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 610; valid market observations: 608; OHLC screened: 24.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | NEAR/USD | 3.0207 | 88.832 | 85.939 | +4.66% | -0.45% | 1.51x | 3.3 | 2026-11-22T15:11:06.048765+00:00 | Not calibrated | MODERATE 64/100 | HIGH 61/100 | Watch | WATCH |
| 2 | HYPE/USD | 62.75 | 85.825 | 71.463 | +2.47% | -0.13% | 3.05x | 1.6 | 2026-11-22T15:11:06.048765+00:00 | Not calibrated | STRONG 73/100 | HIGH 61/100 | Watch | WATCH |
| 3 | ZEC/USD | 793.36 | 81.467 | 67.592 | +1.95% | -0.23% | 6.24x | 2.1 | 2026-11-22T15:11:06.048765+00:00 | Not calibrated | STRONG 71/100 | HIGH 61/100 | Watch | WATCH |
| 4 | NIGHT/USD | 0.04795 | 79.280 | 90.427 | +8.29% | -1.62% | 0.70x | 4.2 | 2026-11-22T15:11:06.048765+00:00 | Not calibrated | MODERATE 45/100 | VERY_HIGH 80/100 | Do nothing | WATCH |
| 5 | ETH/USD | 1708.78 | 74.853 | 65.997 | +1.58% | +0.03% | 1.87x | 0.1 | 2026-11-22T15:11:06.048765+00:00 | Not calibrated | STRONG 72/100 | HIGH 55/100 | Watch | WATCH |
| 6 | LINK/USD | 8.77848 | 73.737 | 58.160 | +2.14% | +0.12% | 2.90x | 1.6 | 2026-11-22T15:11:06.048765+00:00 | Not calibrated | STRONG 82/100 | HIGH 55/100 | Watch | WATCH |
| 7 | XBT/USD | 60790.8 | 73.386 | 63.157 | +1.17% | +0.05% | 2.00x | 0.0 | 2026-11-22T15:11:06.048765+00:00 | Not calibrated | STRONG 72/100 | HIGH 55/100 | Watch | WATCH |
| 8 | VVV/USD | 25.627 | 65.878 | 69.579 | +2.92% | +0.47% | 0.40x | 11.7 | 2026-11-22T15:11:06.048765+00:00 | Not calibrated | MODERATE 58/100 | VERY_HIGH 76/100 | Watch | WATCH |
| 9 | AVAX/USD | 6.665 | 65.086 | 50.311 | +1.55% | -0.04% | 27.95x | 4.5 | 2026-11-22T15:11:06.048765+00:00 | Not calibrated | MODERATE 63/100 | HIGH 61/100 | Watch | WATCH |
| 10 | BNB/USD | 556.87 | 62.381 | 48.551 | +1.73% | -0.01% | 2.39x | 1.6 | 2026-11-22T15:11:06.048765+00:00 | Not calibrated | MODERATE 61/100 | HIGH 61/100 | Watch | WATCH |
| 11 | SUI/USD | 0.6567 | 60.612 | 64.404 | +1.45% | -0.06% | 0.65x | 1.5 | 2026-11-22T15:11:06.048765+00:00 | Not calibrated | WEAK 35/100 | VERY_HIGH 76/100 | Watch | WATCH |
| 12 | STBL/USD | 0.016964 | 57.666 | 60.115 | +6.00% | +0.24% | 0.64x | 25.4 | 2026-11-22T15:11:06.048765+00:00 | Not calibrated | MODERATE 49/100 | EXTREME 94/100 | Do nothing | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | NIGHT/USD | 90.427 | 0.04795 | -1.62% | 0.70x |
| 2 | NEAR/USD | 85.939 | 3.0207 | -0.45% | 1.51x |
| 3 | HYPE/USD | 71.463 | 62.75 | -0.13% | 3.05x |
| 4 | VVV/USD | 69.579 | 25.627 | +0.47% | 0.40x |
| 5 | ZEC/USD | 67.592 | 793.36 | -0.23% | 6.24x |
| 6 | ETH/USD | 65.997 | 1708.78 | +0.03% | 1.87x |
| 7 | SUI/USD | 64.404 | 0.6567 | -0.06% | 0.65x |
| 8 | XBT/USD | 63.157 | 60790.8 | +0.05% | 2.00x |
| 9 | STBL/USD | 60.115 | 0.016964 | +0.24% | 0.64x |
| 10 | LINK/USD | 58.160 | 8.77848 | +0.12% | 2.90x |
| 11 | AVAX/USD | 50.311 | 6.665 | -0.04% | 27.95x |
| 12 | BNB/USD | 48.551 | 556.87 | -0.01% | 2.39x |

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

- Persisted scans: 1299; predictions: 10507; observations: 786199.
- Matured sampled outcomes across 1/6/24/48h: 15368; gap abstentions: 22296. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 61 (sampled only; not a success-rate estimate).
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

**Writer:** 45036737957 · **Generation:** 1299 · **Legacy run:** 45036737957
**Main quote time:** 2026-11-22T15:11:14.208646+00:00 · **Legacy report time:** 2026-11-22T15:12:05.652958+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | NEAR/USD | 3.0207 | 88.83 | -0.45% | 1.51x | MODERATE 64/100 | HIGH 61/100 | Watch |
| 2 | HYPE/USD | 62.75 | 85.83 | -0.13% | 3.05x | STRONG 73/100 | HIGH 61/100 | Watch |
| 3 | ZEC/USD | 793.36 | 81.47 | -0.23% | 6.24x | STRONG 71/100 | HIGH 61/100 | Watch |
| 4 | NIGHT/USD | 0.04795 | 79.28 | -1.62% | 0.70x | MODERATE 45/100 | VERY_HIGH 80/100 | Do nothing |
| 5 | ETH/USD | 1708.78 | 74.85 | +0.03% | 1.87x | STRONG 72/100 | HIGH 55/100 | Watch |
| 6 | LINK/USD ⭐ | 8.77848 | 73.74 | +0.12% | 2.90x | STRONG 92/100 | HIGH 55/100 | Watch |
| 7 | XBT/USD ⭐ | 60790.8 | 73.39 | +0.05% | 2.00x | STRONG 82/100 | HIGH 55/100 | Watch |
| 8 | VVV/USD | 25.627 | 65.88 | +0.47% | 0.40x | MODERATE 58/100 | VERY_HIGH 76/100 | Watch |
| 9 | AVAX/USD | 6.665 | 65.09 | -0.04% | 27.95x | MODERATE 63/100 | HIGH 61/100 | Watch |
| 10 | BNB/USD | 556.87 | 62.38 | -0.01% | 2.39x | MODERATE 61/100 | HIGH 61/100 | Watch |
| 11 | SUI/USD | 0.6567 | 60.61 | -0.06% | 0.65x | WEAK 35/100 | VERY_HIGH 76/100 | Watch |
| 12 | STBL/USD | 0.016964 | 57.67 | +0.24% | 0.64x | MODERATE 49/100 | EXTREME 94/100 | Do nothing |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | LINK/USD ⭐ | 8.77001 | 75.93 | +0.12% | 2.90x | 4894 | STRONG 93/100 | HIGH 55/100 | Watch |
| 2 | XBT/USD ⭐ | 60788.6 | 70.06 | +0.05% | 2.00x | 136171 | STRONG 80/100 | HIGH 55/100 | Watch |

**Same-run overlap:** LINK/USD, XBT/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
