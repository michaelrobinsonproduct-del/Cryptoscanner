# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-22T17:11:12.185907+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/45047846745
**Source SHA:** 17af11513c515cf2dc9dda8017f091d9b1f13397
**Previous ledger commit:** 41aa5e6fcb69e31dbe651d86b93257cf09e9ac93 (atomic ledger/results publication)
**Ledger generation:** 1312 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 6s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 628; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 610; valid market observations: 609; OHLC screened: 24.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | PUMP/USD | 0.002581 | 98.667 | 80.156 | +10.11% | +0.70% | 2.72x | 11.7 | 2026-11-22T17:11:05.866425+00:00 | Not calibrated | STRONG 99/100 | HIGH 61/100 | Consider small entry | WATCH |
| 2 | DRV/USD | 0.35539 | 87.259 | 77.558 | +6.02% | -1.06% | 3.30x | 16.3 | 2026-11-22T17:11:05.866425+00:00 | Not calibrated | MODERATE 69/100 | VERY_HIGH 71/100 | Watch | WATCH |
| 3 | ETH/USD | 1713.05 | 80.812 | 67.774 | +1.83% | -0.39% | 2.94x | 0.1 | 2026-11-22T17:11:05.866425+00:00 | Not calibrated | STRONG 70/100 | HIGH 61/100 | Watch | WATCH |
| 4 | ZBCN/USD | 0.001907 | 80.296 | 66.081 | +10.42% | -0.16% | 5.74x | 26.2 | 2026-11-22T17:11:05.866425+00:00 | Not calibrated | MODERATE 60/100 | VERY_HIGH 78/100 | Watch | WATCH |
| 5 | VVV/USD | 25.581 | 78.100 | 70.818 | +2.73% | +0.32% | 1.57x | 6.7 | 2026-11-22T17:11:05.866425+00:00 | Not calibrated | STRONG 84/100 | HIGH 55/100 | Consider small entry | WATCH |
| 6 | NEAR/USD | 3 | 76.842 | 79.740 | +3.94% | +0.03% | 0.70x | 5.7 | 2026-11-22T17:11:05.866425+00:00 | Not calibrated | MODERATE 58/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 7 | HYPE/USD | 62.9 | 75.359 | 73.179 | +2.71% | -0.33% | 1.38x | 1.6 | 2026-11-22T17:11:05.866425+00:00 | Not calibrated | MODERATE 58/100 | HIGH 61/100 | Watch | WATCH |
| 8 | ZEC/USD | 796.37 | 74.852 | 69.865 | +2.34% | +0.50% | 1.25x | 3.0 | 2026-11-22T17:11:05.866425+00:00 | Not calibrated | STRONG 72/100 | HIGH 62/100 | Watch | WATCH |
| 9 | SUI/USD | 0.6584 | 67.612 | 66.244 | +1.71% | -0.17% | 1.22x | 1.5 | 2026-11-22T17:11:05.866425+00:00 | Not calibrated | WEAK 44/100 | HIGH 68/100 | Watch | WATCH |
| 10 | PEARL/USD | 2.03 | 61.905 | 71.038 | +4.19% | -1.21% | 0.69x | 0.5 | 2026-11-22T17:11:05.866425+00:00 | Not calibrated | WEAK 36/100 | VERY_HIGH 80/100 | Do nothing | WATCH |
| 11 | XBT/USD | 60815.9 | 59.764 | 63.449 | +1.21% | -0.46% | 0.86x | 0.0 | 2026-11-22T17:11:05.866425+00:00 | Not calibrated | WEAK 35/100 | HIGH 68/100 | Watch | WATCH |
| 12 | ONDO/USD | 0.28516 | 55.032 | 43.245 | +1.26% | +0.02% | 2.17x | 0.4 | 2026-11-22T17:11:05.866425+00:00 | Not calibrated | STRONG 73/100 | HIGH 60/100 | Watch | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | PUMP/USD | 80.156 | 0.002581 | +0.70% | 2.72x |
| 2 | NEAR/USD | 79.740 | 3 | +0.03% | 0.70x |
| 3 | DRV/USD | 77.558 | 0.35539 | -1.06% | 3.30x |
| 4 | HYPE/USD | 73.179 | 62.9 | -0.33% | 1.38x |
| 5 | PEARL/USD | 71.038 | 2.03 | -1.21% | 0.69x |
| 6 | VVV/USD | 70.818 | 25.581 | +0.32% | 1.57x |
| 7 | ZEC/USD | 69.865 | 796.37 | +0.50% | 1.25x |
| 8 | ETH/USD | 67.774 | 1713.05 | -0.39% | 2.94x |
| 9 | SUI/USD | 66.244 | 0.6584 | -0.17% | 1.22x |
| 10 | ZBCN/USD | 66.081 | 0.001907 | -0.16% | 5.74x |
| 11 | XBT/USD | 63.449 | 60815.9 | -0.46% | 0.86x |
| 12 | ONDO/USD | 43.245 | 0.28516 | +0.02% | 2.17x |

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

- Persisted scans: 1312; predictions: 10663; observations: 794116.
- Matured sampled outcomes across 1/6/24/48h: 15802; gap abstentions: 22327. Per-horizon counts require independent audit; do not infer held-out lift.
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

**Writer:** 45047846745 · **Generation:** 1312 · **Legacy run:** 45047846745
**Main quote time:** 2026-11-22T17:11:12.185907+00:00 · **Legacy report time:** 2026-11-22T17:12:03.306476+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | PUMP/USD ⭐ | 0.002581 | 98.67 | +0.70% | 2.72x | STRONG 100/100 | HIGH 61/100 | Consider small entry |
| 2 | DRV/USD | 0.35539 | 87.26 | -1.06% | 3.30x | MODERATE 69/100 | VERY_HIGH 71/100 | Watch |
| 3 | ETH/USD | 1713.05 | 80.81 | -0.39% | 2.94x | STRONG 70/100 | HIGH 61/100 | Watch |
| 4 | ZBCN/USD | 0.001907 | 80.30 | -0.16% | 5.74x | MODERATE 60/100 | VERY_HIGH 78/100 | Watch |
| 5 | VVV/USD ⭐ | 25.581 | 78.10 | +0.32% | 1.57x | STRONG 94/100 | HIGH 55/100 | Consider small entry |
| 6 | NEAR/USD | 3 | 76.84 | +0.03% | 0.70x | MODERATE 58/100 | VERY_HIGH 70/100 | Watch |
| 7 | HYPE/USD | 62.9 | 75.36 | -0.33% | 1.38x | MODERATE 58/100 | HIGH 61/100 | Watch |
| 8 | ZEC/USD ⭐ | 796.37 | 74.85 | +0.50% | 1.25x | STRONG 82/100 | HIGH 62/100 | Watch |
| 9 | SUI/USD | 0.6584 | 67.61 | -0.17% | 1.22x | WEAK 44/100 | HIGH 68/100 | Watch |
| 10 | PEARL/USD | 2.03 | 61.91 | -1.21% | 0.69x | WEAK 36/100 | VERY_HIGH 80/100 | Do nothing |
| 11 | XBT/USD | 60815.9 | 59.76 | -0.46% | 0.86x | WEAK 35/100 | HIGH 68/100 | Watch |
| 12 | ONDO/USD | 0.28516 | 55.03 | +0.02% | 2.17x | STRONG 73/100 | HIGH 60/100 | Watch |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | PUMP/USD ⭐ | 0.002574 | 85.58 | +0.70% | 2.72x | 4050 | STRONG 100/100 | HIGH 61/100 | Consider small entry |
| 2 | ZEC/USD ⭐ | 796.69 | 75.78 | +0.50% | 1.25x | 20955 | STRONG 83/100 | HIGH 62/100 | Watch |
| 3 | VVV/USD ⭐ | 25.562 | 75.39 | +0.32% | 1.57x | 12550 | STRONG 93/100 | HIGH 55/100 | Consider small entry |

**Same-run overlap:** PUMP/USD, VVV/USD, ZEC/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
