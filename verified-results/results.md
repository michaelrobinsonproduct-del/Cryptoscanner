# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-22T18:41:20.769547+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/45056334346
**Source SHA:** 193371a597e6dbc5a6a884defbe9e1519a6a183a
**Previous ledger commit:** 391eda50186ca493924c98696908693ea413ce10 (atomic ledger/results publication)
**Ledger generation:** 1321 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 6s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 628; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 610; valid market observations: 609; OHLC screened: 24.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | NEAR/USD | 3.0013 | 94.499 | 81.724 | +3.98% | -0.44% | 3.41x | 2.3 | 2026-11-22T18:41:14.462112+00:00 | Not calibrated | STRONG 77/100 | HIGH 61/100 | Watch | WATCH |
| 2 | PUMP/USD | 0.002546 | 92.366 | 80.010 | +8.62% | +0.20% | 2.14x | 11.8 | 2026-11-22T18:41:14.462112+00:00 | Not calibrated | STRONG 86/100 | HIGH 61/100 | Watch | WATCH |
| 3 | VVV/USD | 26.089 | 90.844 | 84.409 | +4.78% | +0.77% | 1.26x | 8.0 | 2026-11-22T18:41:14.462112+00:00 | Not calibrated | STRONG 80/100 | HIGH 55/100 | Watch | WATCH |
| 4 | DRV/USD | 0.36942 | 80.936 | 81.862 | +10.21% | +0.34% | 0.74x | 14.6 | 2026-11-22T18:41:14.462112+00:00 | Not calibrated | MODERATE 65/100 | VERY_HIGH 76/100 | Watch | WATCH |
| 5 | SUI/USD | 0.6569 | 80.307 | 64.620 | +1.48% | +0.14% | 2.98x | 1.5 | 2026-11-22T18:41:14.462112+00:00 | Not calibrated | STRONG 85/100 | HIGH 55/100 | Watch | WATCH |
| 6 | PIEVERSE/USD | 3.6709 | 79.969 | 73.237 | +7.87% | +1.23% | 1.06x | 24.6 | 2026-11-22T18:41:14.462112+00:00 | Not calibrated | MODERATE 65/100 | VERY_HIGH 74/100 | Watch | WATCH |
| 7 | NIGHT/USD | 0.04924 | 79.437 | 84.975 | +11.20% | -0.81% | 0.85x | 16.2 | 2026-11-22T18:41:14.462112+00:00 | Not calibrated | WEAK 40/100 | VERY_HIGH 74/100 | Watch | WATCH |
| 8 | HYPE/USD | 62.54 | 74.307 | 69.060 | +2.12% | +0.11% | 1.47x | 1.6 | 2026-11-22T18:41:14.462112+00:00 | Not calibrated | STRONG 72/100 | HIGH 55/100 | Watch | WATCH |
| 9 | ETH/USD | 1713.04 | 68.248 | 67.303 | +1.83% | +0.14% | 1.02x | 1.0 | 2026-11-22T18:41:14.462112+00:00 | Not calibrated | MODERATE 59/100 | HIGH 62/100 | Watch | WATCH |
| 10 | AVAX/USD | 6.672 | 67.737 | 51.986 | +1.66% | +0.15% | 3.64x | 3.0 | 2026-11-22T18:41:14.462112+00:00 | Not calibrated | STRONG 79/100 | HIGH 55/100 | Watch | WATCH |
| 11 | XBT/USD | 60652.2 | 58.667 | 61.542 | +0.94% | +0.08% | 0.67x | 0.0 | 2026-11-22T18:41:14.462112+00:00 | Not calibrated | MODERATE 49/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 12 | LTC/USD | 39.92 | 58.645 | 43.896 | +0.48% | -0.05% | 4.15x | 5.0 | 2026-11-22T18:41:14.462112+00:00 | Not calibrated | MODERATE 59/100 | HIGH 61/100 | Watch | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | NIGHT/USD | 84.975 | 0.04924 | -0.81% | 0.85x |
| 2 | VVV/USD | 84.409 | 26.089 | +0.77% | 1.26x |
| 3 | DRV/USD | 81.862 | 0.36942 | +0.34% | 0.74x |
| 4 | NEAR/USD | 81.724 | 3.0013 | -0.44% | 3.41x |
| 5 | PUMP/USD | 80.010 | 0.002546 | +0.20% | 2.14x |
| 6 | PIEVERSE/USD | 73.237 | 3.6709 | +1.23% | 1.06x |
| 7 | HYPE/USD | 69.060 | 62.54 | +0.11% | 1.47x |
| 8 | ETH/USD | 67.303 | 1713.04 | +0.14% | 1.02x |
| 9 | SUI/USD | 64.620 | 0.6569 | +0.14% | 2.98x |
| 10 | XBT/USD | 61.542 | 60652.2 | +0.08% | 0.67x |
| 11 | AVAX/USD | 51.986 | 6.672 | +0.15% | 3.64x |
| 12 | LTC/USD | 43.896 | 39.92 | -0.05% | 4.15x |

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

- Persisted scans: 1321; predictions: 10771; observations: 799597.
- Matured sampled outcomes across 1/6/24/48h: 16162; gap abstentions: 22341. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 61 (sampled only; not a success-rate estimate).
- False positives / missed movers: NOT VERIFIED without eligible continuous outcome coverage.
- Baseline vs challenger: recorded as-of; unbiased held-out lift NOT MEASURED.
- Online Kraken /USD stablecoin-base pairs excluded: 18 (counted from this scan's online AssetPairs metadata, not inferred from price).
- Stablecoin base exclusions: BRL1, BUSD, DAI, EUR, EURC, EUROP, EURQ, EURR, EURT, FDUSD, FRAX, GUSD, PYUSD, QCAD, RLUSD, TGBP, TUSD, USD, USD1, USDC, USDD, USDE, USDG, USDQ, USDR, USDS, USDT, ZUSD.
- DEX: NOT USED; no DEX freshness gate.
- OHLC screening abstentions: 8; details in immutable scan JSON artifact.
- Storage: ledger and results published in one non-force Git commit and read back. Independent artifact recovery is NOT VERIFIED by this scan alone.
- Errors: none in successful committed scan; a failed workflow must not publish a SUCCESS report.

# Cryptoscanner — challenger and independent legacy-inspired WATCH

Paper only · risk is high or higher · 30%+ in 48h probability NOT CALIBRATED
Signal confidence 0–100 means setup strength only, NOT a win probability. Actions are research guidance; no trade authorization.

**Writer:** 45056334346 · **Generation:** 1321 · **Legacy run:** 45056334346
**Main quote time:** 2026-11-22T18:41:20.769547+00:00 · **Legacy report time:** 2026-11-22T18:42:24.485643+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | NEAR/USD | 3.0013 | 94.50 | -0.44% | 3.41x | STRONG 77/100 | HIGH 61/100 | Watch |
| 2 | PUMP/USD ⭐ | 0.002546 | 92.37 | +0.20% | 2.14x | STRONG 96/100 | HIGH 61/100 | Watch |
| 3 | VVV/USD ⭐ | 26.089 | 90.84 | +0.77% | 1.26x | STRONG 90/100 | HIGH 55/100 | Watch |
| 4 | DRV/USD | 0.36942 | 80.94 | +0.34% | 0.74x | MODERATE 65/100 | VERY_HIGH 76/100 | Watch |
| 5 | SUI/USD ⭐ | 0.6569 | 80.31 | +0.14% | 2.98x | STRONG 95/100 | HIGH 55/100 | Watch |
| 6 | PIEVERSE/USD ⭐ | 3.6709 | 79.97 | +1.23% | 1.06x | STRONG 75/100 | VERY_HIGH 74/100 | Watch |
| 7 | NIGHT/USD | 0.04924 | 79.44 | -0.81% | 0.85x | WEAK 40/100 | VERY_HIGH 74/100 | Watch |
| 8 | HYPE/USD ⭐ | 62.54 | 74.31 | +0.11% | 1.47x | STRONG 82/100 | HIGH 55/100 | Watch |
| 9 | ETH/USD ⭐ | 1713.04 | 68.25 | +0.14% | 1.02x | MODERATE 69/100 | HIGH 62/100 | Watch |
| 10 | AVAX/USD | 6.672 | 67.74 | +0.15% | 3.64x | STRONG 79/100 | HIGH 55/100 | Watch |
| 11 | XBT/USD | 60652.2 | 58.67 | +0.08% | 0.67x | MODERATE 49/100 | VERY_HIGH 70/100 | Watch |
| 12 | LTC/USD | 39.92 | 58.65 | -0.05% | 4.15x | MODERATE 59/100 | HIGH 61/100 | Watch |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | VVV/USD ⭐ | 26.069 | 91.84 | +0.77% | 1.26x | 12151 | STRONG 91/100 | HIGH 55/100 | Watch |
| 2 | PUMP/USD ⭐ | 0.002546 | 81.68 | +0.20% | 2.14x | 4075 | STRONG 96/100 | HIGH 55/100 | Watch |
| 3 | PIEVERSE/USD ⭐ | 3.6709 | 80.24 | +1.23% | 1.06x | 5943 | STRONG 80/100 | HIGH 68/100 | Watch |
| 4 | WLD/USD | 0.2369 | 79.31 | +0.51% | 4.10x | 2390 | STRONG 90/100 | HIGH 66/100 | Consider small entry |
| 5 | HYPE/USD ⭐ | 62.57 | 77.08 | +0.11% | 1.47x | 10274 | STRONG 84/100 | HIGH 55/100 | Watch |
| 6 | SUI/USD ⭐ | 0.6566 | 74.51 | +0.14% | 2.98x | 6026 | STRONG 92/100 | HIGH 55/100 | Watch |
| 7 | ETH/USD ⭐ | 1712.75 | 74.14 | +0.14% | 1.02x | 38241 | STRONG 72/100 | HIGH 62/100 | Watch |

**Same-run overlap:** PUMP/USD, VVV/USD, SUI/USD, PIEVERSE/USD, HYPE/USD, ETH/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
