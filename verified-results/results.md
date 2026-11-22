# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-22T14:41:08.885808+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/45034009725
**Source SHA:** 17af11513c515cf2dc9dda8017f091d9b1f13397
**Previous ledger commit:** 85df56e9c5d69f5fa07120e1b757d19fdafad147 (atomic ledger/results publication)
**Ledger generation:** 1296 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 6s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 628; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 610; valid market observations: 609; OHLC screened: 24.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | NIGHT/USD | 0.04869 | 97.305 | 83.949 | +9.96% | +0.23% | 2.22x | 16.5 | 2026-11-22T14:41:02.418547+00:00 | Not calibrated | STRONG 99/100 | HIGH 61/100 | Consider small entry | WATCH |
| 2 | NEAR/USD | 3.041 | 89.638 | 90.544 | +5.36% | +0.88% | 0.47x | 4.0 | 2026-11-22T14:41:02.418547+00:00 | Not calibrated | STRONG 75/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 3 | ZEC/USD | 792.8 | 77.504 | 65.256 | +1.88% | +0.22% | 2.11x | 5.8 | 2026-11-22T14:41:02.418547+00:00 | Not calibrated | STRONG 94/100 | HIGH 55/100 | Consider small entry | WATCH |
| 4 | SUI/USD | 0.657 | 75.803 | 63.967 | +1.50% | +0.14% | 2.12x | 3.0 | 2026-11-22T14:41:02.418547+00:00 | Not calibrated | STRONG 83/100 | HIGH 55/100 | Watch | WATCH |
| 5 | VVV/USD | 25.55 | 72.849 | 70.139 | +2.61% | +0.16% | 1.19x | 6.3 | 2026-11-22T14:41:02.418547+00:00 | Not calibrated | MODERATE 61/100 | HIGH 62/100 | Watch | WATCH |
| 6 | STBL/USD | 0.017095 | 67.564 | 72.274 | +6.82% | -0.61% | 0.84x | 7.0 | 2026-11-22T14:41:02.418547+00:00 | Not calibrated | WEAK 39/100 | VERY_HIGH 80/100 | Watch | WATCH |
| 7 | HYPE/USD | 62.57 | 65.658 | 69.403 | +2.17% | +0.05% | 0.60x | 1.6 | 2026-11-22T14:41:02.418547+00:00 | Not calibrated | MODERATE 53/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 8 | TAO/USD | 191.1788 | 64.693 | 66.279 | +2.93% | +0.00% | 0.84x | 7.6 | 2026-11-22T14:41:02.418547+00:00 | Not calibrated | MODERATE 52/100 | HIGH 62/100 | Watch | WATCH |
| 9 | MNT/USD | 0.3933 | 62.883 | 67.603 | +6.18% | -0.71% | 0.88x | 12.7 | 2026-11-22T14:41:02.418547+00:00 | Not calibrated | WEAK 31/100 | EXTREME 86/100 | Do nothing | WATCH |
| 10 | XBT/USD | 60637.7 | 62.528 | 61.373 | +0.91% | +0.03% | 1.10x | 0.0 | 2026-11-22T14:41:02.418547+00:00 | Not calibrated | MODERATE 56/100 | HIGH 62/100 | Watch | WATCH |
| 11 | ETH/USD | 1701.74 | 56.742 | 63.068 | +1.16% | -0.05% | 0.39x | 0.1 | 2026-11-22T14:41:02.418547+00:00 | Not calibrated | WEAK 33/100 | VERY_HIGH 76/100 | Do nothing | WATCH |
| 12 | ZAMA/USD | 0.06153 | 54.558 | 42.589 | +1.80% | -0.40% | 2.40x | 3.3 | 2026-11-22T14:41:02.418547+00:00 | Not calibrated | MODERATE 57/100 | VERY_HIGH 73/100 | Watch | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | NEAR/USD | 90.544 | 3.041 | +0.88% | 0.47x |
| 2 | NIGHT/USD | 83.949 | 0.04869 | +0.23% | 2.22x |
| 3 | STBL/USD | 72.274 | 0.017095 | -0.61% | 0.84x |
| 4 | VVV/USD | 70.139 | 25.55 | +0.16% | 1.19x |
| 5 | HYPE/USD | 69.403 | 62.57 | +0.05% | 0.60x |
| 6 | MNT/USD | 67.603 | 0.3933 | -0.71% | 0.88x |
| 7 | TAO/USD | 66.279 | 191.1788 | +0.00% | 0.84x |
| 8 | ZEC/USD | 65.256 | 792.8 | +0.22% | 2.11x |
| 9 | SUI/USD | 63.967 | 0.657 | +0.14% | 2.12x |
| 10 | ETH/USD | 63.068 | 1701.74 | -0.05% | 0.39x |
| 11 | XBT/USD | 61.373 | 60637.7 | +0.03% | 1.10x |
| 12 | ZAMA/USD | 42.589 | 0.06153 | -0.40% | 2.40x |

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

- Persisted scans: 1296; predictions: 10471; observations: 784373.
- Matured sampled outcomes across 1/6/24/48h: 15269; gap abstentions: 22281. Per-horizon counts require independent audit; do not infer held-out lift.
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

**Writer:** 45034009725 · **Generation:** 1296 · **Legacy run:** 45034009725
**Main quote time:** 2026-11-22T14:41:08.885808+00:00 · **Legacy report time:** 2026-11-22T14:41:59.815044+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | NIGHT/USD ⭐ | 0.04869 | 97.31 | +0.23% | 2.22x | STRONG 100/100 | HIGH 61/100 | Consider small entry |
| 2 | NEAR/USD | 3.041 | 89.64 | +0.88% | 0.47x | STRONG 75/100 | VERY_HIGH 70/100 | Watch |
| 3 | ZEC/USD ⭐ | 792.8 | 77.50 | +0.22% | 2.11x | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 4 | SUI/USD ⭐ | 0.657 | 75.80 | +0.14% | 2.12x | STRONG 93/100 | HIGH 55/100 | Watch |
| 5 | VVV/USD ⭐ | 25.55 | 72.85 | +0.16% | 1.19x | STRONG 71/100 | HIGH 62/100 | Watch |
| 6 | STBL/USD | 0.017095 | 67.56 | -0.61% | 0.84x | WEAK 39/100 | VERY_HIGH 80/100 | Watch |
| 7 | HYPE/USD | 62.57 | 65.66 | +0.05% | 0.60x | MODERATE 53/100 | VERY_HIGH 70/100 | Watch |
| 8 | TAO/USD | 191.1788 | 64.69 | +0.00% | 0.84x | MODERATE 52/100 | HIGH 62/100 | Watch |
| 9 | MNT/USD | 0.3933 | 62.88 | -0.71% | 0.88x | WEAK 31/100 | EXTREME 86/100 | Do nothing |
| 10 | XBT/USD | 60637.7 | 62.53 | +0.03% | 1.10x | MODERATE 56/100 | HIGH 62/100 | Watch |
| 11 | ETH/USD | 1701.74 | 56.74 | -0.05% | 0.39x | WEAK 33/100 | VERY_HIGH 76/100 | Do nothing |
| 12 | ZAMA/USD | 0.06153 | 54.56 | -0.40% | 2.40x | MODERATE 57/100 | VERY_HIGH 73/100 | Watch |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | PIEVERSE/USD | 3.66 | 87.99 | +5.53% | 1.88x | 6128 | STRONG 74/100 | EXTREME 87/100 | Do nothing |
| 2 | NIGHT/USD ⭐ | 0.04856 | 85.85 | +0.23% | 2.22x | 9769 | STRONG 100/100 | HIGH 61/100 | Consider small entry |
| 3 | ZEC/USD ⭐ | 793.01 | 75.97 | +0.22% | 2.11x | 23085 | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 4 | SUI/USD ⭐ | 0.657 | 71.81 | +0.14% | 2.12x | 6516 | STRONG 91/100 | HIGH 55/100 | Watch |
| 5 | VVV/USD ⭐ | 25.509 | 69.25 | +0.16% | 1.19x | 13322 | STRONG 70/100 | HIGH 62/100 | Watch |

**Same-run overlap:** NIGHT/USD, ZEC/USD, SUI/USD, VVV/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
