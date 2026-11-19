# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-19T18:40:24.619617+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/44590143095
**Source SHA:** f854bf15990e1aa3564d35bbec4100f929bd3d42
**Previous ledger commit:** 714e28be24963a415b35761ab9285d1c1e848b07 (atomic ledger/results publication)
**Ledger generation:** 836 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 6s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 627; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 609; valid market observations: 599; OHLC screened: 24.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | VVV/USD | 22.797 | 100.503 | 87.412 | +5.20% | +1.29% | 1.66x | 7.9 | 2026-11-19T18:40:18.424206+00:00 | Not calibrated | STRONG 95/100 | HIGH 55/100 | Consider small entry | WATCH |
| 2 | HYPE/USD | 69.95 | 90.565 | 85.701 | +4.59% | +0.52% | 1.23x | 2.9 | 2026-11-19T18:40:18.424206+00:00 | Not calibrated | STRONG 80/100 | HIGH 62/100 | Watch | WATCH |
| 3 | TAO/USD | 196.8408 | 88.053 | 68.673 | +2.54% | +0.88% | 3.08x | 6.2 | 2026-11-19T18:40:18.424206+00:00 | Not calibrated | STRONG 99/100 | HIGH 55/100 | Consider small entry | WATCH |
| 4 | INJ/USD | 7.242 | 87.461 | 66.027 | +3.74% | +1.29% | 2.92x | 9.7 | 2026-11-19T18:40:18.424206+00:00 | Not calibrated | STRONG 99/100 | HIGH 55/100 | Consider small entry | WATCH |
| 5 | SUI/USD | 0.7222 | 75.832 | 57.519 | +0.46% | +0.67% | 2.50x | 1.4 | 2026-11-19T18:40:18.424206+00:00 | Not calibrated | STRONG 93/100 | HIGH 55/100 | Consider small entry | WATCH |
| 6 | AKT/USD | 0.555 | 75.498 | 73.494 | +7.14% | +0.89% | 0.76x | 7.2 | 2026-11-19T18:40:18.424206+00:00 | Not calibrated | MODERATE 68/100 | HIGH 67/100 | Watch | WATCH |
| 7 | LIGHTER/USD | 2.871 | 72.357 | 68.242 | +5.78% | +1.02% | 0.90x | 13.9 | 2026-11-19T18:40:18.424206+00:00 | Not calibrated | MODERATE 61/100 | VERY_HIGH 73/100 | Watch | WATCH |
| 8 | ADA/USD | 0.154251 | 68.214 | 67.702 | +1.98% | +0.61% | 0.75x | 2.3 | 2026-11-19T18:40:18.424206+00:00 | Not calibrated | MODERATE 64/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 9 | PUMP/USD | 0.002725 | 66.660 | 71.607 | +4.97% | +0.70% | 0.15x | 11.0 | 2026-11-19T18:40:18.424206+00:00 | Not calibrated | MODERATE 58/100 | VERY_HIGH 76/100 | Watch | WATCH |
| 10 | ETH/USD | 1785.31 | 65.457 | 59.133 | +0.59% | +0.39% | 1.44x | 0.1 | 2026-11-19T18:40:18.424206+00:00 | Not calibrated | STRONG 78/100 | HIGH 55/100 | Watch | WATCH |
| 11 | SKR/USD | 0.01019 | 61.004 | 66.684 | +5.78% | -0.22% | 0.54x | 9.8 | 2026-11-19T18:40:18.424206+00:00 | Not calibrated | WEAK 36/100 | EXTREME 88/100 | Do nothing | WATCH |
| 12 | XRP/USD | 0.97662 | 59.057 | 61.913 | +1.06% | +0.47% | 0.48x | 1.0 | 2026-11-19T18:40:18.424206+00:00 | Not calibrated | MODERATE 60/100 | VERY_HIGH 70/100 | Watch | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | VVV/USD | 87.412 | 22.797 | +1.29% | 1.66x |
| 2 | HYPE/USD | 85.701 | 69.95 | +0.52% | 1.23x |
| 3 | AKT/USD | 73.494 | 0.555 | +0.89% | 0.76x |
| 4 | PUMP/USD | 71.607 | 0.002725 | +0.70% | 0.15x |
| 5 | TAO/USD | 68.673 | 196.8408 | +0.88% | 3.08x |
| 6 | LIGHTER/USD | 68.242 | 2.871 | +1.02% | 0.90x |
| 7 | ADA/USD | 67.702 | 0.154251 | +0.61% | 0.75x |
| 8 | SKR/USD | 66.684 | 0.01019 | -0.22% | 0.54x |
| 9 | INJ/USD | 66.027 | 7.242 | +1.29% | 2.92x |
| 10 | XRP/USD | 61.913 | 0.97662 | +0.47% | 0.48x |
| 11 | ETH/USD | 59.133 | 1785.31 | +0.39% | 1.44x |
| 12 | SUI/USD | 57.519 | 0.7222 | +0.67% | 2.50x |

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

- Persisted scans: 836; predictions: 7176; observations: 505341.
- Matured sampled outcomes across 1/6/24/48h: 7163; gap abstentions: 15532. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 10 (sampled only; not a success-rate estimate).
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

**Writer:** 44590143095 · **Generation:** 836 · **Legacy run:** 44590143095
**Main quote time:** 2026-11-19T18:40:24.619617+00:00 · **Legacy report time:** 2026-11-19T18:41:11.365515+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | VVV/USD ⭐ | 22.797 | 100.50 | +1.29% | 1.66x | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 2 | HYPE/USD ⭐ | 69.95 | 90.56 | +0.52% | 1.23x | STRONG 90/100 | HIGH 62/100 | Watch |
| 3 | TAO/USD | 196.8408 | 88.05 | +0.88% | 3.08x | STRONG 99/100 | HIGH 55/100 | Consider small entry |
| 4 | INJ/USD ⭐ | 7.242 | 87.46 | +1.29% | 2.92x | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 5 | SUI/USD | 0.7222 | 75.83 | +0.67% | 2.50x | STRONG 93/100 | HIGH 55/100 | Consider small entry |
| 6 | AKT/USD | 0.555 | 75.50 | +0.89% | 0.76x | MODERATE 68/100 | HIGH 67/100 | Watch |
| 7 | LIGHTER/USD | 2.871 | 72.36 | +1.02% | 0.90x | MODERATE 61/100 | VERY_HIGH 73/100 | Watch |
| 8 | ADA/USD | 0.154251 | 68.21 | +0.61% | 0.75x | MODERATE 64/100 | VERY_HIGH 70/100 | Watch |
| 9 | PUMP/USD | 0.002725 | 66.66 | +0.70% | 0.15x | MODERATE 58/100 | VERY_HIGH 76/100 | Watch |
| 10 | ETH/USD | 1785.31 | 65.46 | +0.39% | 1.44x | STRONG 78/100 | HIGH 55/100 | Watch |
| 11 | SKR/USD | 0.01019 | 61.00 | -0.22% | 0.54x | WEAK 36/100 | EXTREME 88/100 | Do nothing |
| 12 | XRP/USD | 0.97662 | 59.06 | +0.47% | 0.48x | MODERATE 60/100 | VERY_HIGH 70/100 | Watch |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | HYPE/USD ⭐ | 69.84 | 99.60 | +0.52% | 1.23x | 13785 | STRONG 95/100 | HIGH 62/100 | Watch |
| 2 | VVV/USD ⭐ | 22.76 | 91.53 | +1.29% | 1.66x | 12561 | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 3 | INJ/USD ⭐ | 7.192 | 82.67 | +1.29% | 2.92x | 7134 | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 4 | LUNA/USD | 4.967e-05 | 79.14 | +1.30% | 1.20x | 6512 | STRONG 70/100 | HIGH 68/100 | Watch |

**Same-run overlap:** VVV/USD, HYPE/USD, INJ/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
