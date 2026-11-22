# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-22T19:31:35.715693+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/45061042795
**Source SHA:** 193371a597e6dbc5a6a884defbe9e1519a6a183a
**Previous ledger commit:** 736b23282f9273e700ddb8a5bc67fb9a4b175533 (atomic ledger/results publication)
**Ledger generation:** 1326 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 9s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 628; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 610; valid market observations: 609; OHLC screened: 24.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | DRV/USD | 0.37323 | 99.238 | 82.868 | +11.35% | +0.27% | 7.80x | 13.1 | 2026-11-22T19:31:27.053489+00:00 | Not calibrated | STRONG 100/100 | HIGH 61/100 | Consider small entry | WATCH |
| 2 | NIGHT/USD | 0.04836 | 87.776 | 87.820 | +9.21% | -0.78% | 1.39x | 10.3 | 2026-11-22T19:31:27.053489+00:00 | Not calibrated | MODERATE 59/100 | HIGH 67/100 | Watch | WATCH |
| 3 | ETH/USD | 1711.84 | 82.355 | 67.212 | +1.76% | +0.03% | 2.68x | 0.2 | 2026-11-22T19:31:27.053489+00:00 | Not calibrated | STRONG 86/100 | HIGH 55/100 | Watch | WATCH |
| 4 | PUMP/USD | 0.002561 | 75.970 | 79.918 | +9.26% | +0.27% | 0.47x | 11.7 | 2026-11-22T19:31:27.053489+00:00 | Not calibrated | MODERATE 63/100 | VERY_HIGH 76/100 | Watch | WATCH |
| 5 | NEAR/USD | 2.9991 | 75.486 | 80.520 | +3.91% | -0.41% | 0.70x | 3.7 | 2026-11-22T19:31:27.053489+00:00 | Not calibrated | WEAK 43/100 | VERY_HIGH 76/100 | Watch | WATCH |
| 6 | VVV/USD | 25.912 | 72.209 | 80.939 | +4.06% | -0.59% | 0.42x | 5.0 | 2026-11-22T19:31:27.053489+00:00 | Not calibrated | WEAK 41/100 | VERY_HIGH 76/100 | Watch | WATCH |
| 7 | PYTH/USD | 0.05224 | 69.078 | 66.849 | +6.90% | +0.73% | 0.86x | 19.2 | 2026-11-22T19:31:27.053489+00:00 | Not calibrated | MODERATE 60/100 | VERY_HIGH 80/100 | Watch | WATCH |
| 8 | XBT/USD | 60639.5 | 62.599 | 61.394 | +0.91% | +0.08% | 1.08x | 0.0 | 2026-11-22T19:31:27.053489+00:00 | Not calibrated | MODERATE 56/100 | HIGH 62/100 | Watch | WATCH |
| 9 | HYPE/USD | 62.39 | 61.284 | 67.343 | +1.88% | +0.02% | 0.39x | 1.6 | 2026-11-22T19:31:27.053489+00:00 | Not calibrated | MODERATE 51/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 10 | ZEC/USD | 789.8 | 60.891 | 63.497 | +1.49% | +0.20% | 0.64x | 3.9 | 2026-11-22T19:31:27.053489+00:00 | Not calibrated | MODERATE 60/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 11 | DOT/USD | 0.6603 | 53.443 | 39.953 | +1.12% | -0.30% | 2.84x | 1.5 | 2026-11-22T19:31:27.053489+00:00 | Not calibrated | MODERATE 57/100 | HIGH 66/100 | Watch | WATCH |
| 12 | BNB/USD | 555.82 | 53.436 | 46.446 | +1.54% | -0.05% | 1.73x | 2.0 | 2026-11-22T19:31:27.053489+00:00 | Not calibrated | MODERATE 47/100 | HIGH 61/100 | Watch | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | NIGHT/USD | 87.820 | 0.04836 | -0.78% | 1.39x |
| 2 | DRV/USD | 82.868 | 0.37323 | +0.27% | 7.80x |
| 3 | VVV/USD | 80.939 | 25.912 | -0.59% | 0.42x |
| 4 | NEAR/USD | 80.520 | 2.9991 | -0.41% | 0.70x |
| 5 | PUMP/USD | 79.918 | 0.002561 | +0.27% | 0.47x |
| 6 | HYPE/USD | 67.343 | 62.39 | +0.02% | 0.39x |
| 7 | ETH/USD | 67.212 | 1711.84 | +0.03% | 2.68x |
| 8 | PYTH/USD | 66.849 | 0.05224 | +0.73% | 0.86x |
| 9 | ZEC/USD | 63.497 | 789.8 | +0.20% | 0.64x |
| 10 | XBT/USD | 61.394 | 60639.5 | +0.08% | 1.08x |
| 11 | BNB/USD | 46.446 | 555.82 | -0.05% | 1.73x |
| 12 | DOT/USD | 39.953 | 0.6603 | -0.30% | 2.84x |

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

- Persisted scans: 1326; predictions: 10831; observations: 802642.
- Matured sampled outcomes across 1/6/24/48h: 16342; gap abstentions: 22342. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 61 (sampled only; not a success-rate estimate).
- False positives / missed movers: NOT VERIFIED without eligible continuous outcome coverage.
- Baseline vs challenger: recorded as-of; unbiased held-out lift NOT MEASURED.
- Online Kraken /USD stablecoin-base pairs excluded: 18 (counted from this scan's online AssetPairs metadata, not inferred from price).
- Stablecoin base exclusions: BRL1, BUSD, DAI, EUR, EURC, EUROP, EURQ, EURR, EURT, FDUSD, FRAX, GUSD, PYUSD, QCAD, RLUSD, TGBP, TUSD, USD, USD1, USDC, USDD, USDE, USDG, USDQ, USDR, USDS, USDT, ZUSD.
- DEX: NOT USED; no DEX freshness gate.
- OHLC screening abstentions: 10; details in immutable scan JSON artifact.
- Storage: ledger and results published in one non-force Git commit and read back. Independent artifact recovery is NOT VERIFIED by this scan alone.
- Errors: none in successful committed scan; a failed workflow must not publish a SUCCESS report.

# Cryptoscanner — challenger and independent legacy-inspired WATCH

Paper only · risk is high or higher · 30%+ in 48h probability NOT CALIBRATED
Signal confidence 0–100 means setup strength only, NOT a win probability. Actions are research guidance; no trade authorization.

**Writer:** 45061042795 · **Generation:** 1326 · **Legacy run:** 45061042795
**Main quote time:** 2026-11-22T19:31:35.715693+00:00 · **Legacy report time:** 2026-11-22T19:32:36.740959+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | DRV/USD ⭐ | 0.37323 | 99.24 | +0.27% | 7.80x | STRONG 100/100 | HIGH 61/100 | Consider small entry |
| 2 | NIGHT/USD | 0.04836 | 87.78 | -0.78% | 1.39x | MODERATE 59/100 | HIGH 67/100 | Watch |
| 3 | ETH/USD | 1711.84 | 82.36 | +0.03% | 2.68x | STRONG 86/100 | HIGH 55/100 | Watch |
| 4 | PUMP/USD | 0.002561 | 75.97 | +0.27% | 0.47x | MODERATE 63/100 | VERY_HIGH 76/100 | Watch |
| 5 | NEAR/USD | 2.9991 | 75.49 | -0.41% | 0.70x | WEAK 43/100 | VERY_HIGH 76/100 | Watch |
| 6 | VVV/USD | 25.912 | 72.21 | -0.59% | 0.42x | WEAK 41/100 | VERY_HIGH 76/100 | Watch |
| 7 | PYTH/USD | 0.05224 | 69.08 | +0.73% | 0.86x | MODERATE 60/100 | VERY_HIGH 80/100 | Watch |
| 8 | XBT/USD | 60639.5 | 62.60 | +0.08% | 1.08x | MODERATE 56/100 | HIGH 62/100 | Watch |
| 9 | HYPE/USD | 62.39 | 61.28 | +0.02% | 0.39x | MODERATE 51/100 | VERY_HIGH 70/100 | Watch |
| 10 | ZEC/USD | 789.8 | 60.89 | +0.20% | 0.64x | MODERATE 60/100 | VERY_HIGH 70/100 | Watch |
| 11 | DOT/USD | 0.6603 | 53.44 | -0.30% | 2.84x | MODERATE 57/100 | HIGH 66/100 | Watch |
| 12 | BNB/USD | 555.82 | 53.44 | -0.05% | 1.73x | MODERATE 47/100 | HIGH 61/100 | Watch |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | DRV/USD ⭐ | 0.37382 | 89.64 | +0.27% | 7.80x | 18397 | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 2 | PIEVERSE/USD | 3.6107 | 84.97 | +0.24% | 18.60x | 5947 | STRONG 82/100 | VERY_HIGH 77/100 | Watch |
| 3 | INJ/USD | 6.202 | 77.42 | +0.13% | 1.69x | 5429 | STRONG 74/100 | HIGH 55/100 | Watch |
| 4 | LINK/USD | 8.78529 | 72.79 | +0.05% | 2.88x | 4641 | STRONG 81/100 | HIGH 55/100 | Watch |

**Same-run overlap:** DRV/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
