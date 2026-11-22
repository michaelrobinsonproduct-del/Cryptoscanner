# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-22T14:51:20.892148+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/45034911324
**Source SHA:** 17af11513c515cf2dc9dda8017f091d9b1f13397
**Previous ledger commit:** 12e3cf383dcea6d76e24a732ad46bd6a29ac4aed (atomic ledger/results publication)
**Ledger generation:** 1297 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 7s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 628; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 610; valid market observations: 609; OHLC screened: 24.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | NEAR/USD | 3.0251 | 86.970 | 86.023 | +4.81% | +0.26% | 0.97x | 5.3 | 2026-11-22T14:51:13.917652+00:00 | Not calibrated | STRONG 73/100 | HIGH 62/100 | Watch | WATCH |
| 2 | NIGHT/USD | 0.04856 | 82.471 | 83.948 | +9.67% | -0.84% | 1.27x | 16.4 | 2026-11-22T14:51:13.917652+00:00 | Not calibrated | MODERATE 46/100 | HIGH 67/100 | Watch | WATCH |
| 3 | ZEC/USD | 793.36 | 82.457 | 66.148 | +1.95% | +0.26% | 3.20x | 5.0 | 2026-11-22T14:51:13.917652+00:00 | Not calibrated | STRONG 96/100 | HIGH 55/100 | Consider small entry | WATCH |
| 4 | SUI/USD | 0.6568 | 80.657 | 64.513 | +1.47% | +0.23% | 2.66x | 1.5 | 2026-11-22T14:51:13.917652+00:00 | Not calibrated | STRONG 95/100 | HIGH 55/100 | Consider small entry | WATCH |
| 5 | MNT/USD | 0.3914 | 74.137 | 65.264 | +5.67% | -0.63% | 2.20x | 10.2 | 2026-11-22T14:51:13.917652+00:00 | Not calibrated | MODERATE 62/100 | VERY_HIGH 79/100 | Watch | WATCH |
| 6 | LINK/USD | 8.77295 | 73.966 | 57.381 | +2.07% | +0.32% | 2.68x | 2.0 | 2026-11-22T14:51:13.917652+00:00 | Not calibrated | STRONG 92/100 | HIGH 55/100 | Consider small entry | WATCH |
| 7 | XBT/USD | 60791.9 | 71.487 | 63.169 | +1.17% | +0.34% | 1.66x | 0.0 | 2026-11-22T14:51:13.917652+00:00 | Not calibrated | STRONG 81/100 | HIGH 55/100 | Consider small entry | WATCH |
| 8 | HYPE/USD | 62.61 | 67.307 | 69.063 | +2.24% | +0.10% | 0.78x | 3.2 | 2026-11-22T14:51:13.917652+00:00 | Not calibrated | MODERATE 54/100 | HIGH 62/100 | Watch | WATCH |
| 9 | ETH/USD | 1709.68 | 66.755 | 66.372 | +1.63% | +0.39% | 0.84x | 0.1 | 2026-11-22T14:51:13.917652+00:00 | Not calibrated | MODERATE 63/100 | HIGH 62/100 | Watch | WATCH |
| 10 | TAO/USD | 191.0533 | 63.358 | 66.406 | +2.87% | +0.17% | 0.61x | 6.3 | 2026-11-22T14:51:13.917652+00:00 | Not calibrated | MODERATE 52/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 11 | VVV/USD | 25.519 | 62.016 | 69.856 | +2.49% | -0.15% | 0.29x | 5.1 | 2026-11-22T14:51:13.917652+00:00 | Not calibrated | WEAK 36/100 | VERY_HIGH 76/100 | Watch | WATCH |
| 12 | BNB/USD | 556.69 | 58.198 | 48.339 | +1.70% | +0.38% | 1.80x | 1.6 | 2026-11-22T14:51:13.917652+00:00 | Not calibrated | STRONG 74/100 | HIGH 55/100 | Watch | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | NEAR/USD | 86.023 | 3.0251 | +0.26% | 0.97x |
| 2 | NIGHT/USD | 83.948 | 0.04856 | -0.84% | 1.27x |
| 3 | VVV/USD | 69.856 | 25.519 | -0.15% | 0.29x |
| 4 | HYPE/USD | 69.063 | 62.61 | +0.10% | 0.78x |
| 5 | TAO/USD | 66.406 | 191.0533 | +0.17% | 0.61x |
| 6 | ETH/USD | 66.372 | 1709.68 | +0.39% | 0.84x |
| 7 | ZEC/USD | 66.148 | 793.36 | +0.26% | 3.20x |
| 8 | MNT/USD | 65.264 | 0.3914 | -0.63% | 2.20x |
| 9 | SUI/USD | 64.513 | 0.6568 | +0.23% | 2.66x |
| 10 | XBT/USD | 63.169 | 60791.9 | +0.34% | 1.66x |
| 11 | LINK/USD | 57.381 | 8.77295 | +0.32% | 2.68x |
| 12 | BNB/USD | 48.339 | 556.69 | +0.38% | 1.80x |

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

- Persisted scans: 1297; predictions: 10483; observations: 784982.
- Matured sampled outcomes across 1/6/24/48h: 15300; gap abstentions: 22285. Per-horizon counts require independent audit; do not infer held-out lift.
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

**Writer:** 45034911324 · **Generation:** 1297 · **Legacy run:** 45034911324
**Main quote time:** 2026-11-22T14:51:20.892148+00:00 · **Legacy report time:** 2026-11-22T14:52:17.986021+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | NEAR/USD | 3.0251 | 86.97 | +0.26% | 0.97x | STRONG 73/100 | HIGH 62/100 | Watch |
| 2 | NIGHT/USD | 0.04856 | 82.47 | -0.84% | 1.27x | MODERATE 46/100 | HIGH 67/100 | Watch |
| 3 | ZEC/USD ⭐ | 793.36 | 82.46 | +0.26% | 3.20x | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 4 | SUI/USD ⭐ | 0.6568 | 80.66 | +0.23% | 2.66x | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 5 | MNT/USD | 0.3914 | 74.14 | -0.63% | 2.20x | MODERATE 62/100 | VERY_HIGH 79/100 | Watch |
| 6 | LINK/USD | 8.77295 | 73.97 | +0.32% | 2.68x | STRONG 92/100 | HIGH 55/100 | Consider small entry |
| 7 | XBT/USD ⭐ | 60791.9 | 71.49 | +0.34% | 1.66x | STRONG 91/100 | HIGH 55/100 | Consider small entry |
| 8 | HYPE/USD | 62.61 | 67.31 | +0.10% | 0.78x | MODERATE 54/100 | HIGH 62/100 | Watch |
| 9 | ETH/USD | 1709.68 | 66.76 | +0.39% | 0.84x | MODERATE 63/100 | HIGH 62/100 | Watch |
| 10 | TAO/USD | 191.0533 | 63.36 | +0.17% | 0.61x | MODERATE 52/100 | VERY_HIGH 70/100 | Watch |
| 11 | VVV/USD | 25.519 | 62.02 | -0.15% | 0.29x | WEAK 36/100 | VERY_HIGH 76/100 | Watch |
| 12 | BNB/USD | 556.69 | 58.20 | +0.38% | 1.80x | STRONG 74/100 | HIGH 55/100 | Watch |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | ZBCN/USD | 0.001935 | 84.20 | +1.36% | 5.32x | 4758 | STRONG 82/100 | VERY_HIGH 72/100 | Watch |
| 2 | SUI/USD ⭐ | 0.6574 | 75.00 | +0.23% | 2.66x | 6502 | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 3 | ZEC/USD ⭐ | 793.36 | 74.88 | +0.26% | 3.20x | 23065 | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 4 | XBT/USD ⭐ | 60763.1 | 69.08 | +0.34% | 1.66x | 136435 | STRONG 90/100 | HIGH 55/100 | Consider small entry |

**Same-run overlap:** ZEC/USD, SUI/USD, XBT/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
