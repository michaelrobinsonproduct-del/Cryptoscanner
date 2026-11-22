# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-22T20:31:21.558239+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/45066718657
**Source SHA:** 193371a597e6dbc5a6a884defbe9e1519a6a183a
**Previous ledger commit:** 071f0cb6c96838e0576ba3c22439fcac79be0e69 (atomic ledger/results publication)
**Ledger generation:** 1332 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 8s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 628; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 610; valid market observations: 609; OHLC screened: 24.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | VVV/USD | 26.206 | 97.522 | 90.380 | +5.25% | +0.31% | 1.56x | 2.7 | 2026-11-22T20:31:13.277604+00:00 | Not calibrated | STRONG 94/100 | HIGH 55/100 | Consider small entry | WATCH |
| 2 | PUMP/USD | 0.002542 | 89.285 | 80.314 | +8.45% | -1.21% | 15.16x | 11.8 | 2026-11-22T20:31:13.277604+00:00 | Not calibrated | STRONG 70/100 | VERY_HIGH 71/100 | Do nothing | WATCH |
| 3 | NIGHT/USD | 0.04836 | 85.772 | 89.662 | +9.21% | -0.08% | 0.65x | 6.2 | 2026-11-22T20:31:13.277604+00:00 | Not calibrated | MODERATE 48/100 | VERY_HIGH 76/100 | Watch | WATCH |
| 4 | ETH/USD | 1711.16 | 81.877 | 66.988 | +1.72% | -0.02% | 3.63x | 0.1 | 2026-11-22T20:31:13.277604+00:00 | Not calibrated | STRONG 71/100 | HIGH 61/100 | Watch | WATCH |
| 5 | NEAR/USD | 2.9651 | 74.989 | 72.930 | +2.73% | -0.33% | 1.37x | 2.4 | 2026-11-22T20:31:13.277604+00:00 | Not calibrated | MODERATE 57/100 | HIGH 61/100 | Watch | WATCH |
| 6 | SUI/USD | 0.6532 | 74.621 | 60.615 | +0.91% | -0.20% | 3.31x | 1.5 | 2026-11-22T20:31:13.277604+00:00 | Not calibrated | MODERATE 67/100 | HIGH 61/100 | Watch | WATCH |
| 7 | XBT/USD | 60555.7 | 72.539 | 60.418 | +0.78% | -0.15% | 2.29x | 0.0 | 2026-11-22T20:31:13.277604+00:00 | Not calibrated | MODERATE 66/100 | HIGH 61/100 | Watch | WATCH |
| 8 | PIEVERSE/USD | 3.6127 | 67.827 | 75.059 | +6.16% | -0.66% | 0.61x | 16.9 | 2026-11-22T20:31:13.277604+00:00 | Not calibrated | WEAK 34/100 | VERY_HIGH 82/100 | Do nothing | WATCH |
| 9 | HYPE/USD | 62.45 | 58.409 | 68.030 | +1.98% | -0.02% | 0.05x | 1.6 | 2026-11-22T20:31:13.277604+00:00 | Not calibrated | WEAK 34/100 | VERY_HIGH 76/100 | Do nothing | WATCH |
| 10 | PYTH/USD | 0.05152 | 57.033 | 63.587 | +5.42% | +0.08% | 0.31x | 11.6 | 2026-11-22T20:31:13.277604+00:00 | Not calibrated | WEAK 44/100 | EXTREME 88/100 | Do nothing | WATCH |
| 11 | XMR/USD | 493.58 | 55.812 | 53.783 | +0.36% | -0.15% | 1.28x | 7.5 | 2026-11-22T20:31:13.277604+00:00 | Not calibrated | WEAK 38/100 | HIGH 61/100 | Watch | WATCH |
| 12 | PEARL/USD | 1.9673 | 48.011 | 46.814 | +0.98% | -0.15% | 1.19x | 0.5 | 2026-11-22T20:31:13.277604+00:00 | Not calibrated | WEAK 34/100 | HIGH 68/100 | Do nothing | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | VVV/USD | 90.380 | 26.206 | +0.31% | 1.56x |
| 2 | NIGHT/USD | 89.662 | 0.04836 | -0.08% | 0.65x |
| 3 | PUMP/USD | 80.314 | 0.002542 | -1.21% | 15.16x |
| 4 | PIEVERSE/USD | 75.059 | 3.6127 | -0.66% | 0.61x |
| 5 | NEAR/USD | 72.930 | 2.9651 | -0.33% | 1.37x |
| 6 | HYPE/USD | 68.030 | 62.45 | -0.02% | 0.05x |
| 7 | ETH/USD | 66.988 | 1711.16 | -0.02% | 3.63x |
| 8 | PYTH/USD | 63.587 | 0.05152 | +0.08% | 0.31x |
| 9 | SUI/USD | 60.615 | 0.6532 | -0.20% | 3.31x |
| 10 | XBT/USD | 60.418 | 60555.7 | -0.15% | 2.29x |
| 11 | XMR/USD | 53.783 | 493.58 | -0.15% | 1.28x |
| 12 | PEARL/USD | 46.814 | 1.9673 | -0.15% | 1.19x |

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

- Persisted scans: 1332; predictions: 10903; observations: 806296.
- Matured sampled outcomes across 1/6/24/48h: 16558; gap abstentions: 22350. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 61 (sampled only; not a success-rate estimate).
- False positives / missed movers: NOT VERIFIED without eligible continuous outcome coverage.
- Baseline vs challenger: recorded as-of; unbiased held-out lift NOT MEASURED.
- Online Kraken /USD stablecoin-base pairs excluded: 18 (counted from this scan's online AssetPairs metadata, not inferred from price).
- Stablecoin base exclusions: BRL1, BUSD, DAI, EUR, EURC, EUROP, EURQ, EURR, EURT, FDUSD, FRAX, GUSD, PYUSD, QCAD, RLUSD, TGBP, TUSD, USD, USD1, USDC, USDD, USDE, USDG, USDQ, USDR, USDS, USDT, ZUSD.
- DEX: NOT USED; no DEX freshness gate.
- OHLC screening abstentions: 11; details in immutable scan JSON artifact.
- Storage: ledger and results published in one non-force Git commit and read back. Independent artifact recovery is NOT VERIFIED by this scan alone.
- Errors: none in successful committed scan; a failed workflow must not publish a SUCCESS report.

# Cryptoscanner — challenger and independent legacy-inspired WATCH

Paper only · risk is high or higher · 30%+ in 48h probability NOT CALIBRATED
Signal confidence 0–100 means setup strength only, NOT a win probability. Actions are research guidance; no trade authorization.

**Writer:** 45066718657 · **Generation:** 1332 · **Legacy run:** 45066718657
**Main quote time:** 2026-11-22T20:31:21.558239+00:00 · **Legacy report time:** 2026-11-22T20:32:27.503078+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | VVV/USD ⭐ | 26.206 | 97.52 | +0.31% | 1.56x | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 2 | PUMP/USD | 0.002542 | 89.29 | -1.21% | 15.16x | STRONG 70/100 | VERY_HIGH 71/100 | Do nothing |
| 3 | NIGHT/USD | 0.04836 | 85.77 | -0.08% | 0.65x | MODERATE 48/100 | VERY_HIGH 76/100 | Watch |
| 4 | ETH/USD | 1711.16 | 81.88 | -0.02% | 3.63x | STRONG 71/100 | HIGH 61/100 | Watch |
| 5 | NEAR/USD | 2.9651 | 74.99 | -0.33% | 1.37x | MODERATE 57/100 | HIGH 61/100 | Watch |
| 6 | SUI/USD | 0.6532 | 74.62 | -0.20% | 3.31x | MODERATE 67/100 | HIGH 61/100 | Watch |
| 7 | XBT/USD | 60555.7 | 72.54 | -0.15% | 2.29x | MODERATE 66/100 | HIGH 61/100 | Watch |
| 8 | PIEVERSE/USD | 3.6127 | 67.83 | -0.66% | 0.61x | WEAK 34/100 | VERY_HIGH 82/100 | Do nothing |
| 9 | HYPE/USD | 62.45 | 58.41 | -0.02% | 0.05x | WEAK 34/100 | VERY_HIGH 76/100 | Do nothing |
| 10 | PYTH/USD | 0.05152 | 57.03 | +0.08% | 0.31x | WEAK 44/100 | EXTREME 88/100 | Do nothing |
| 11 | XMR/USD | 493.58 | 55.81 | -0.15% | 1.28x | WEAK 38/100 | HIGH 61/100 | Watch |
| 12 | PEARL/USD | 1.9673 | 48.01 | -0.15% | 1.19x | WEAK 34/100 | HIGH 68/100 | Do nothing |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | VVV/USD ⭐ | 26.215 | 88.17 | +0.31% | 1.56x | 12046 | STRONG 99/100 | HIGH 55/100 | Consider small entry |

**Same-run overlap:** VVV/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
