# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-17T23:40:07.800568+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/44201292528
**Source SHA:** 113db7a045b71125e52affc5c74a39ca3094a032
**Previous ledger commit:** e9835346ef9f1cb39810402eca37afac7faedd46 (atomic ledger/results publication)
**Ledger generation:** 473 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 8s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 627; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 609; valid market observations: 609; OHLC screened: 24.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | ZEC/USD | 966.01 | 115.646 | 99.120 | +6.88% | +0.31% | 3.54x | 1.8 | 2026-11-17T23:40:00.241365+00:00 | Not calibrated | STRONG 100/100 | HIGH 55/100 | Consider small entry | WATCH |
| 2 | INJ/USD | 7.405 | 110.757 | 97.974 | +7.33% | +1.13% | 1.71x | 4.1 | 2026-11-17T23:40:00.241365+00:00 | Not calibrated | STRONG 95/100 | HIGH 55/100 | Consider small entry | WATCH |
| 3 | NEAR/USD | 3.3818 | 94.907 | 96.893 | +7.09% | +0.33% | 0.64x | 6.2 | 2026-11-17T23:40:00.241365+00:00 | Not calibrated | STRONG 77/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 4 | XRP/USD | 0.98566 | 92.356 | 77.148 | +3.24% | +0.04% | 2.78x | 1.0 | 2026-11-17T23:40:00.241365+00:00 | Not calibrated | STRONG 91/100 | HIGH 55/100 | Watch | WATCH |
| 5 | TAO/USD | 197.4232 | 89.912 | 73.743 | +3.25% | +0.23% | 3.34x | 8.1 | 2026-11-17T23:40:00.241365+00:00 | Not calibrated | STRONG 100/100 | HIGH 55/100 | Consider small entry | WATCH |
| 6 | VVV/USD | 21.168 | 88.953 | 79.707 | +5.06% | +0.29% | 1.78x | 7.1 | 2026-11-17T23:40:00.241365+00:00 | Not calibrated | STRONG 89/100 | HIGH 55/100 | Consider small entry | WATCH |
| 7 | SOL/USD | 75.12 | 87.999 | 89.569 | +5.03% | +0.01% | 0.84x | 1.3 | 2026-11-17T23:40:00.241365+00:00 | Not calibrated | MODERATE 64/100 | HIGH 62/100 | Watch | WATCH |
| 8 | HYPE/USD | 70.03 | 74.572 | 56.483 | +0.42% | +0.62% | 3.46x | 2.9 | 2026-11-17T23:40:00.241365+00:00 | Not calibrated | STRONG 92/100 | HIGH 55/100 | Consider small entry | WATCH |
| 9 | XMR/USD | 511.33 | 74.009 | 77.140 | +3.60% | +0.35% | 0.51x | 6.1 | 2026-11-17T23:40:00.241365+00:00 | Not calibrated | MODERATE 67/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 10 | XBT/USD | 65029.1 | 73.557 | 57.319 | +0.33% | +0.25% | 2.55x | 0.0 | 2026-11-17T23:40:00.241365+00:00 | Not calibrated | STRONG 92/100 | HIGH 55/100 | Consider small entry | WATCH |
| 11 | LTC/USD | 45.31 | 73.383 | 57.056 | +1.89% | +0.27% | 2.55x | 2.2 | 2026-11-17T23:40:00.241365+00:00 | Not calibrated | STRONG 92/100 | HIGH 55/100 | Consider small entry | WATCH |
| 12 | SUI/USD | 0.7376 | 69.448 | 72.033 | +2.53% | -0.03% | 0.76x | 1.4 | 2026-11-17T23:40:00.241365+00:00 | Not calibrated | WEAK 40/100 | HIGH 68/100 | Watch | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | ZEC/USD | 99.120 | 966.01 | +0.31% | 3.54x |
| 2 | INJ/USD | 97.974 | 7.405 | +1.13% | 1.71x |
| 3 | NEAR/USD | 96.893 | 3.3818 | +0.33% | 0.64x |
| 4 | SOL/USD | 89.569 | 75.12 | +0.01% | 0.84x |
| 5 | VVV/USD | 79.707 | 21.168 | +0.29% | 1.78x |
| 6 | XRP/USD | 77.148 | 0.98566 | +0.04% | 2.78x |
| 7 | XMR/USD | 77.140 | 511.33 | +0.35% | 0.51x |
| 8 | TAO/USD | 73.743 | 197.4232 | +0.23% | 3.34x |
| 9 | SUI/USD | 72.033 | 0.7376 | -0.03% | 0.76x |
| 10 | XBT/USD | 57.319 | 65029.1 | +0.25% | 2.55x |
| 11 | LTC/USD | 57.056 | 45.31 | +0.27% | 2.55x |
| 12 | HYPE/USD | 56.483 | 70.03 | +0.62% | 3.46x |

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

- Persisted scans: 473; predictions: 4157; observations: 285064.
- Matured sampled outcomes across 1/6/24/48h: 3195; gap abstentions: 12398. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 0 (sampled only; not a success-rate estimate).
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

**Writer:** 44201292528 · **Generation:** 473 · **Legacy run:** 44201292528
**Main quote time:** 2026-11-17T23:40:07.800568+00:00 · **Legacy report time:** 2026-11-17T23:40:20.019126+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | ZEC/USD ⭐ | 966.01 | 115.65 | +0.31% | 3.54x | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 2 | INJ/USD ⭐ | 7.405 | 110.76 | +1.13% | 1.71x | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 3 | NEAR/USD ⭐ | 3.3818 | 94.91 | +0.33% | 0.64x | STRONG 87/100 | VERY_HIGH 70/100 | Watch |
| 4 | XRP/USD | 0.98566 | 92.36 | +0.04% | 2.78x | STRONG 91/100 | HIGH 55/100 | Watch |
| 5 | TAO/USD ⭐ | 197.4232 | 89.91 | +0.23% | 3.34x | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 6 | VVV/USD ⭐ | 21.168 | 88.95 | +0.29% | 1.78x | STRONG 99/100 | HIGH 55/100 | Consider small entry |
| 7 | SOL/USD | 75.12 | 88.00 | +0.01% | 0.84x | MODERATE 64/100 | HIGH 62/100 | Watch |
| 8 | HYPE/USD | 70.03 | 74.57 | +0.62% | 3.46x | STRONG 92/100 | HIGH 55/100 | Consider small entry |
| 9 | XMR/USD | 511.33 | 74.01 | +0.35% | 0.51x | MODERATE 67/100 | VERY_HIGH 70/100 | Watch |
| 10 | XBT/USD | 65029.1 | 73.56 | +0.25% | 2.55x | STRONG 92/100 | HIGH 55/100 | Consider small entry |
| 11 | LTC/USD | 45.31 | 73.38 | +0.27% | 2.55x | STRONG 92/100 | HIGH 55/100 | Consider small entry |
| 12 | SUI/USD | 0.7376 | 69.45 | -0.03% | 0.76x | WEAK 40/100 | HIGH 68/100 | Watch |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | ZEC/USD ⭐ | 966.69 | 100.00 | +0.66% | 3.46x | 26698 | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 2 | INJ/USD ⭐ | 7.407 | 95.44 | +1.13% | 1.71x | 9918 | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 3 | NEAR/USD ⭐ | 3.3807 | 93.41 | +0.50% | 1.34x | 15327 | STRONG 100/100 | HIGH 55/100 | Watch |
| 4 | USELESS/USD | 0.0989 | 89.11 | +1.72% | 5.42x | 4406 | STRONG 90/100 | HIGH 67/100 | Consider small entry |
| 5 | VVV/USD ⭐ | 21.168 | 87.41 | +0.29% | 1.78x | 7324 | STRONG 99/100 | HIGH 55/100 | Consider small entry |
| 6 | TAO/USD ⭐ | 197.4232 | 84.75 | +0.23% | 3.34x | 5574 | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 7 | LINK/USD | 9.33408 | 78.57 | +0.15% | 2.29x | 6413 | STRONG 84/100 | HIGH 55/100 | Watch |

**Same-run overlap:** ZEC/USD, INJ/USD, NEAR/USD, TAO/USD, VVV/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
