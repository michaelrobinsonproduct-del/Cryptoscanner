# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-17T22:55:14.100103+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/44194541728
**Source SHA:** e9b1b6ee47d56a43a454042547735fcd1cdc45a9
**Previous ledger commit:** df7969e1fec8bef1302ee5638be5ddb9a107c736 (atomic ledger/results publication)
**Ledger generation:** 464 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 9s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 627; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 609; valid market observations: 609; OHLC screened: 24.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | INJ/USD | 7.282 | 108.797 | 91.798 | +5.55% | +0.40% | 4.81x | 4.1 | 2026-11-17T22:55:05.306041+00:00 | Not calibrated | STRONG 100/100 | HIGH 55/100 | Consider small entry | WATCH |
| 2 | NEAR/USD | 3.333 | 99.308 | 92.487 | +5.55% | +0.42% | 1.47x | 2.7 | 2026-11-17T22:55:05.306041+00:00 | Not calibrated | STRONG 95/100 | HIGH 55/100 | Watch | WATCH |
| 3 | ZEC/USD | 951.86 | 95.919 | 92.162 | +5.32% | +0.38% | 1.18x | 0.1 | 2026-11-17T22:55:05.306041+00:00 | Not calibrated | STRONG 83/100 | HIGH 62/100 | Watch | WATCH |
| 4 | SOL/USD | 74.12 | 78.665 | 79.772 | +3.64% | +0.27% | 0.75x | 1.3 | 2026-11-17T22:55:05.306041+00:00 | Not calibrated | MODERATE 69/100 | HIGH 62/100 | Watch | WATCH |
| 5 | VVV/USD | 20.814 | 78.653 | 66.899 | +3.31% | -0.65% | 8.54x | 6.7 | 2026-11-17T22:55:05.306041+00:00 | Not calibrated | MODERATE 69/100 | HIGH 61/100 | Watch | WATCH |
| 6 | XMR/USD | 509.22 | 70.811 | 71.488 | +3.17% | +0.68% | 0.59x | 11.4 | 2026-11-17T22:55:05.306041+00:00 | Not calibrated | MODERATE 60/100 | VERY_HIGH 76/100 | Watch | WATCH |
| 7 | AKT/USD | 0.5046 | 66.409 | 67.423 | +5.48% | +0.44% | 0.68x | 5.9 | 2026-11-17T22:55:05.306041+00:00 | Not calibrated | MODERATE 63/100 | VERY_HIGH 75/100 | Watch | WATCH |
| 8 | SUI/USD | 0.7332 | 63.297 | 67.746 | +1.92% | +0.30% | 0.40x | 1.4 | 2026-11-17T22:55:05.306041+00:00 | Not calibrated | MODERATE 62/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 9 | TRUST/USD | 0.04736 | 62.507 | 66.363 | +10.11% | +0.00% | 0.61x | 23.2 | 2026-11-17T22:55:05.306041+00:00 | Not calibrated | WEAK 41/100 | EXTREME 87/100 | Do nothing | WATCH |
| 10 | XRP/USD | 0.97334 | 61.445 | 68.211 | +1.95% | +0.25% | 0.20x | 0.8 | 2026-11-17T22:55:05.306041+00:00 | Not calibrated | MODERATE 61/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 11 | XDG/USD | 0.0596838 | 56.505 | 63.516 | +1.36% | +0.22% | 0.19x | 0.0 | 2026-11-17T22:55:05.306041+00:00 | Not calibrated | MODERATE 58/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 12 | LTC/USD | 45.04 | 54.452 | 52.528 | +1.28% | +0.31% | 1.04x | 2.2 | 2026-11-17T22:55:05.306041+00:00 | Not calibrated | MODERATE 62/100 | HIGH 62/100 | Watch | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | NEAR/USD | 92.487 | 3.333 | +0.42% | 1.47x |
| 2 | ZEC/USD | 92.162 | 951.86 | +0.38% | 1.18x |
| 3 | INJ/USD | 91.798 | 7.282 | +0.40% | 4.81x |
| 4 | SOL/USD | 79.772 | 74.12 | +0.27% | 0.75x |
| 5 | XMR/USD | 71.488 | 509.22 | +0.68% | 0.59x |
| 6 | XRP/USD | 68.211 | 0.97334 | +0.25% | 0.20x |
| 7 | SUI/USD | 67.746 | 0.7332 | +0.30% | 0.40x |
| 8 | AKT/USD | 67.423 | 0.5046 | +0.44% | 0.68x |
| 9 | VVV/USD | 66.899 | 20.814 | -0.65% | 8.54x |
| 10 | TRUST/USD | 66.363 | 0.04736 | +0.00% | 0.61x |
| 11 | XDG/USD | 63.516 | 0.0596838 | +0.22% | 0.19x |
| 12 | LTC/USD | 52.528 | 45.04 | +0.31% | 1.04x |

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

- Persisted scans: 464; predictions: 4049; observations: 279583.
- Matured sampled outcomes across 1/6/24/48h: 3195; gap abstentions: 12386. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 0 (sampled only; not a success-rate estimate).
- False positives / missed movers: NOT VERIFIED without eligible continuous outcome coverage.
- Baseline vs challenger: recorded as-of; unbiased held-out lift NOT MEASURED.
- Online Kraken /USD stablecoin-base pairs excluded: 18 (counted from this scan's online AssetPairs metadata, not inferred from price).
- Stablecoin base exclusions: BRL1, BUSD, DAI, EUR, EURC, EUROP, EURQ, EURR, EURT, FDUSD, FRAX, GUSD, PYUSD, QCAD, RLUSD, TGBP, TUSD, USD, USD1, USDC, USDD, USDE, USDG, USDQ, USDR, USDS, USDT, ZUSD.
- DEX: NOT USED; no DEX freshness gate.
- OHLC screening abstentions: 5; details in immutable scan JSON artifact.
- Storage: ledger and results published in one non-force Git commit and read back. Independent artifact recovery is NOT VERIFIED by this scan alone.
- Errors: none in successful committed scan; a failed workflow must not publish a SUCCESS report.

# Cryptoscanner — challenger and independent legacy-inspired WATCH

Paper only · risk is high or higher · 30%+ in 48h probability NOT CALIBRATED
Signal confidence 0–100 means setup strength only, NOT a win probability. Actions are research guidance; no trade authorization.

**Writer:** 44194541728 · **Generation:** 464 · **Legacy run:** 44194541728
**Main quote time:** 2026-11-17T22:55:14.100103+00:00 · **Legacy report time:** 2026-11-17T22:55:23.215740+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | INJ/USD ⭐ | 7.282 | 108.80 | +0.40% | 4.81x | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 2 | NEAR/USD ⭐ | 3.333 | 99.31 | +0.42% | 1.47x | STRONG 100/100 | HIGH 55/100 | Watch |
| 3 | ZEC/USD ⭐ | 951.86 | 95.92 | +0.38% | 1.18x | STRONG 93/100 | HIGH 62/100 | Watch |
| 4 | SOL/USD | 74.12 | 78.67 | +0.27% | 0.75x | MODERATE 69/100 | HIGH 62/100 | Watch |
| 5 | VVV/USD | 20.814 | 78.65 | -0.65% | 8.54x | MODERATE 69/100 | HIGH 61/100 | Watch |
| 6 | XMR/USD | 509.22 | 70.81 | +0.68% | 0.59x | MODERATE 60/100 | VERY_HIGH 76/100 | Watch |
| 7 | AKT/USD | 0.5046 | 66.41 | +0.44% | 0.68x | MODERATE 63/100 | VERY_HIGH 75/100 | Watch |
| 8 | SUI/USD | 0.7332 | 63.30 | +0.30% | 0.40x | MODERATE 62/100 | VERY_HIGH 70/100 | Watch |
| 9 | TRUST/USD | 0.04736 | 62.51 | +0.00% | 0.61x | WEAK 41/100 | EXTREME 87/100 | Do nothing |
| 10 | XRP/USD | 0.97334 | 61.44 | +0.25% | 0.20x | MODERATE 61/100 | VERY_HIGH 70/100 | Watch |
| 11 | XDG/USD | 0.0596838 | 56.51 | +0.22% | 0.19x | MODERATE 58/100 | VERY_HIGH 70/100 | Watch |
| 12 | LTC/USD | 45.04 | 54.45 | +0.31% | 1.04x | MODERATE 62/100 | HIGH 62/100 | Watch |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | INJ/USD ⭐ | 7.282 | 100.00 | +0.40% | 4.81x | 9755 | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 2 | NEAR/USD ⭐ | 3.3331 | 98.35 | +0.42% | 1.47x | 14998 | STRONG 100/100 | HIGH 55/100 | Watch |
| 3 | ZEC/USD ⭐ | 951 | 91.36 | +0.38% | 1.18x | 25954 | STRONG 91/100 | HIGH 62/100 | Watch |

**Same-run overlap:** INJ/USD, NEAR/USD, ZEC/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
