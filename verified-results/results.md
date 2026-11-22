# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-22T21:21:09.256919+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/45071463538
**Source SHA:** 193371a597e6dbc5a6a884defbe9e1519a6a183a
**Previous ledger commit:** b8abe21b67a6620dd9b77ef15cad911706dc6a9f (atomic ledger/results publication)
**Ledger generation:** 1337 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 8s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 628; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 610; valid market observations: 609; OHLC screened: 24.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | NIGHT/USD | 0.0487 | 103.308 | 88.000 | +9.98% | +0.06% | 4.25x | 10.3 | 2026-11-22T21:21:01.536559+00:00 | Not calibrated | STRONG 90/100 | HIGH 61/100 | Watch | WATCH |
| 2 | NEAR/USD | 2.9874 | 92.460 | 77.511 | +3.50% | +0.10% | 2.45x | 4.0 | 2026-11-22T21:21:01.536559+00:00 | Not calibrated | STRONG 91/100 | HIGH 55/100 | Watch | WATCH |
| 3 | ETH/USD | 1721.39 | 84.739 | 71.245 | +2.32% | +0.00% | 2.35x | 0.1 | 2026-11-22T21:21:01.536559+00:00 | Not calibrated | STRONG 87/100 | HIGH 55/100 | Watch | WATCH |
| 4 | HYPE/USD | 62.67 | 84.434 | 70.548 | +2.34% | -0.22% | 3.63x | 1.6 | 2026-11-22T21:21:01.536559+00:00 | Not calibrated | STRONG 72/100 | HIGH 61/100 | Watch | WATCH |
| 5 | VVV/USD | 26.129 | 79.579 | 84.956 | +4.94% | -0.23% | 0.58x | 9.2 | 2026-11-22T21:21:01.536559+00:00 | Not calibrated | MODERATE 45/100 | VERY_HIGH 76/100 | Watch | WATCH |
| 6 | DRV/USD | 0.3752 | 77.208 | 83.549 | +11.93% | +0.08% | 0.33x | 11.5 | 2026-11-22T21:21:01.536559+00:00 | Not calibrated | MODERATE 54/100 | VERY_HIGH 76/100 | Watch | WATCH |
| 7 | PUMP/USD | 0.002565 | 74.661 | 84.575 | +9.43% | -0.50% | 0.26x | 3.9 | 2026-11-22T21:21:01.536559+00:00 | Not calibrated | WEAK 42/100 | VERY_HIGH 76/100 | Watch | WATCH |
| 8 | STBL/USD | 0.017127 | 67.361 | 67.226 | +7.02% | +0.50% | 0.76x | 17.5 | 2026-11-22T21:21:01.536559+00:00 | Not calibrated | MODERATE 59/100 | VERY_HIGH 80/100 | Watch | WATCH |
| 9 | ZEC/USD | 794.67 | 67.320 | 68.332 | +2.12% | +0.08% | 0.86x | 3.0 | 2026-11-22T21:21:01.536559+00:00 | Not calibrated | MODERATE 54/100 | HIGH 62/100 | Watch | WATCH |
| 10 | BNB/USD | 557.2 | 63.189 | 48.252 | +1.79% | -0.01% | 3.04x | 2.2 | 2026-11-22T21:21:01.536559+00:00 | Not calibrated | MODERATE 62/100 | HIGH 61/100 | Watch | WATCH |
| 11 | XBT/USD | 60842.3 | 61.568 | 63.757 | +1.25% | -0.16% | 0.86x | 0.0 | 2026-11-22T21:21:01.536559+00:00 | Not calibrated | WEAK 36/100 | HIGH 68/100 | Watch | WATCH |
| 12 | SUI/USD | 0.6563 | 60.620 | 63.654 | +1.39% | -0.05% | 0.72x | 1.5 | 2026-11-22T21:21:01.536559+00:00 | Not calibrated | WEAK 35/100 | VERY_HIGH 76/100 | Watch | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | NIGHT/USD | 88.000 | 0.0487 | +0.06% | 4.25x |
| 2 | VVV/USD | 84.956 | 26.129 | -0.23% | 0.58x |
| 3 | PUMP/USD | 84.575 | 0.002565 | -0.50% | 0.26x |
| 4 | DRV/USD | 83.549 | 0.3752 | +0.08% | 0.33x |
| 5 | NEAR/USD | 77.511 | 2.9874 | +0.10% | 2.45x |
| 6 | ETH/USD | 71.245 | 1721.39 | +0.00% | 2.35x |
| 7 | HYPE/USD | 70.548 | 62.67 | -0.22% | 3.63x |
| 8 | ZEC/USD | 68.332 | 794.67 | +0.08% | 0.86x |
| 9 | STBL/USD | 67.226 | 0.017127 | +0.50% | 0.76x |
| 10 | XBT/USD | 63.757 | 60842.3 | -0.16% | 0.86x |
| 11 | SUI/USD | 63.654 | 0.6563 | -0.05% | 0.72x |
| 12 | BNB/USD | 48.252 | 557.2 | -0.01% | 3.04x |

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

- Persisted scans: 1337; predictions: 10963; observations: 809341.
- Matured sampled outcomes across 1/6/24/48h: 16737; gap abstentions: 22363. Per-horizon counts require independent audit; do not infer held-out lift.
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

**Writer:** 45071463538 · **Generation:** 1337 · **Legacy run:** 45071463538
**Main quote time:** 2026-11-22T21:21:09.256919+00:00 · **Legacy report time:** 2026-11-22T21:22:03.223364+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | NIGHT/USD ⭐ | 0.0487 | 103.31 | +0.06% | 4.25x | STRONG 100/100 | HIGH 61/100 | Watch |
| 2 | NEAR/USD ⭐ | 2.9874 | 92.46 | +0.10% | 2.45x | STRONG 100/100 | HIGH 55/100 | Watch |
| 3 | ETH/USD | 1721.39 | 84.74 | +0.00% | 2.35x | STRONG 87/100 | HIGH 55/100 | Watch |
| 4 | HYPE/USD | 62.67 | 84.43 | -0.22% | 3.63x | STRONG 72/100 | HIGH 61/100 | Watch |
| 5 | VVV/USD | 26.129 | 79.58 | -0.23% | 0.58x | MODERATE 45/100 | VERY_HIGH 76/100 | Watch |
| 6 | DRV/USD | 0.3752 | 77.21 | +0.08% | 0.33x | MODERATE 54/100 | VERY_HIGH 76/100 | Watch |
| 7 | PUMP/USD | 0.002565 | 74.66 | -0.50% | 0.26x | WEAK 42/100 | VERY_HIGH 76/100 | Watch |
| 8 | STBL/USD | 0.017127 | 67.36 | +0.50% | 0.76x | MODERATE 59/100 | VERY_HIGH 80/100 | Watch |
| 9 | ZEC/USD | 794.67 | 67.32 | +0.08% | 0.86x | MODERATE 54/100 | HIGH 62/100 | Watch |
| 10 | BNB/USD | 557.2 | 63.19 | -0.01% | 3.04x | MODERATE 62/100 | HIGH 61/100 | Watch |
| 11 | XBT/USD | 60842.3 | 61.57 | -0.16% | 0.86x | WEAK 36/100 | HIGH 68/100 | Watch |
| 12 | SUI/USD | 0.6563 | 60.62 | -0.05% | 0.72x | WEAK 35/100 | VERY_HIGH 76/100 | Watch |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | NEAR/USD ⭐ | 2.9864 | 92.99 | +0.10% | 2.45x | 12665 | STRONG 100/100 | HIGH 55/100 | Watch |
| 2 | NIGHT/USD ⭐ | 0.04878 | 89.08 | +0.06% | 4.25x | 9953 | STRONG 95/100 | HIGH 61/100 | Watch |

**Same-run overlap:** NIGHT/USD, NEAR/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
