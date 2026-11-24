# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-24T05:21:22.432220+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/45332518331
**Source SHA:** 858c8bc8ec5d7641ddb39cacd8aca91719f855b1
**Previous ledger commit:** 2e772bb6b407f375877d56d378207aaeb91b812a (atomic ledger/results publication)
**Ledger generation:** 1530 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 8s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 628; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 610; valid market observations: 609; OHLC screened: 24.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | LINK/USD | 9.10726 | 77.773 | 61.147 | +1.14% | +0.33% | 5.80x | 3.6 | 2026-11-24T05:21:14.797158+00:00 | Not calibrated | STRONG 94/100 | HIGH 55/100 | Consider small entry | WATCH |
| 2 | PEPE/USD | 3.575e-06 | 77.645 | 77.432 | +4.47% | +1.14% | 0.45x | 8.4 | 2026-11-24T05:21:14.797158+00:00 | Not calibrated | MODERATE 69/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 3 | UNI/USD | 4.9221 | 76.169 | 59.558 | +1.74% | +0.45% | 2.43x | 6.1 | 2026-11-24T05:21:14.797158+00:00 | Not calibrated | STRONG 93/100 | HIGH 55/100 | Consider small entry | WATCH |
| 4 | LTC/USD | 41.78 | 74.775 | 57.493 | +0.87% | +0.46% | 3.61x | 7.2 | 2026-11-24T05:21:14.797158+00:00 | Not calibrated | STRONG 92/100 | HIGH 55/100 | Consider small entry | WATCH |
| 5 | XMR/USD | 494 | 72.124 | 66.392 | +1.64% | +0.54% | 1.30x | 0.2 | 2026-11-24T05:21:14.797158+00:00 | Not calibrated | STRONG 81/100 | HIGH 55/100 | Watch | WATCH |
| 6 | VVV/USD | 25.25 | 70.565 | 71.818 | +3.28% | +0.18% | 0.78x | 12.3 | 2026-11-24T05:21:14.797158+00:00 | Not calibrated | MODERATE 50/100 | HIGH 68/100 | Watch | WATCH |
| 7 | AI/USD | 0.01623 | 65.124 | 70.086 | +6.57% | +0.43% | 0.29x | 12.2 | 2026-11-24T05:21:14.797158+00:00 | Not calibrated | MODERATE 58/100 | EXTREME 88/100 | Do nothing | WATCH |
| 8 | ADA/USD | 0.149232 | 63.728 | 56.958 | +0.53% | +0.44% | 1.46x | 3.5 | 2026-11-24T05:21:14.797158+00:00 | Not calibrated | STRONG 77/100 | HIGH 55/100 | Watch | WATCH |
| 9 | DOT/USD | 0.6866 | 62.869 | 45.894 | +1.64% | +0.40% | 7.77x | 1.5 | 2026-11-24T05:21:14.797158+00:00 | Not calibrated | STRONG 86/100 | HIGH 60/100 | Watch | WATCH |
| 10 | XDG/USD | 0.0567037 | 60.732 | 59.285 | +0.71% | +0.37% | 0.96x | 1.3 | 2026-11-24T05:21:14.797158+00:00 | Not calibrated | MODERATE 60/100 | HIGH 62/100 | Watch | WATCH |
| 11 | XRP/USD | 0.9533 | 57.112 | 64.631 | +1.48% | +0.10% | 0.20x | 1.5 | 2026-11-24T05:21:14.797158+00:00 | Not calibrated | MODERATE 49/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 12 | NEAR/USD | 3.0203 | 53.885 | 62.194 | +1.31% | +0.19% | 0.07x | 4.0 | 2026-11-24T05:21:14.797158+00:00 | Not calibrated | MODERATE 47/100 | VERY_HIGH 70/100 | Watch | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | PEPE/USD | 77.432 | 3.575e-06 | +1.14% | 0.45x |
| 2 | VVV/USD | 71.818 | 25.25 | +0.18% | 0.78x |
| 3 | AI/USD | 70.086 | 0.01623 | +0.43% | 0.29x |
| 4 | XMR/USD | 66.392 | 494 | +0.54% | 1.30x |
| 5 | XRP/USD | 64.631 | 0.9533 | +0.10% | 0.20x |
| 6 | NEAR/USD | 62.194 | 3.0203 | +0.19% | 0.07x |
| 7 | LINK/USD | 61.147 | 9.10726 | +0.33% | 5.80x |
| 8 | UNI/USD | 59.558 | 4.9221 | +0.45% | 2.43x |
| 9 | XDG/USD | 59.285 | 0.0567037 | +0.37% | 0.96x |
| 10 | LTC/USD | 57.493 | 41.78 | +0.46% | 3.61x |
| 11 | ADA/USD | 56.958 | 0.149232 | +0.44% | 1.46x |
| 12 | DOT/USD | 45.894 | 0.6866 | +0.40% | 7.77x |

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

- Persisted scans: 1530; predictions: 13093; observations: 926868.
- Matured sampled outcomes across 1/6/24/48h: 24484; gap abstentions: 22370. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 136 (sampled only; not a success-rate estimate).
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

**Writer:** 45332518331 · **Generation:** 1530 · **Legacy run:** 45332518331
**Main quote time:** 2026-11-24T05:21:22.432220+00:00 · **Legacy report time:** 2026-11-24T05:22:08.414279+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | LINK/USD ⭐ | 9.10726 | 77.77 | +0.33% | 5.80x | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 2 | PEPE/USD | 3.575e-06 | 77.64 | +1.14% | 0.45x | MODERATE 69/100 | VERY_HIGH 70/100 | Watch |
| 3 | UNI/USD ⭐ | 4.9221 | 76.17 | +0.45% | 2.43x | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 4 | LTC/USD ⭐ | 41.78 | 74.77 | +0.46% | 3.61x | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 5 | XMR/USD ⭐ | 494 | 72.12 | +0.54% | 1.30x | STRONG 91/100 | HIGH 55/100 | Watch |
| 6 | VVV/USD | 25.25 | 70.57 | +0.18% | 0.78x | MODERATE 50/100 | HIGH 68/100 | Watch |
| 7 | AI/USD | 0.01623 | 65.12 | +0.43% | 0.29x | MODERATE 58/100 | EXTREME 88/100 | Do nothing |
| 8 | ADA/USD | 0.149232 | 63.73 | +0.44% | 1.46x | STRONG 77/100 | HIGH 55/100 | Watch |
| 9 | DOT/USD | 0.6866 | 62.87 | +0.40% | 7.77x | STRONG 86/100 | HIGH 60/100 | Watch |
| 10 | XDG/USD | 0.0567037 | 60.73 | +0.37% | 0.96x | MODERATE 60/100 | HIGH 62/100 | Watch |
| 11 | XRP/USD | 0.9533 | 57.11 | +0.10% | 0.20x | MODERATE 49/100 | VERY_HIGH 70/100 | Watch |
| 12 | NEAR/USD | 3.0203 | 53.89 | +0.19% | 0.07x | MODERATE 47/100 | VERY_HIGH 70/100 | Watch |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | BAT/USD | 0.07994 | 68.52 | +0.73% | 1.04x | 3103 | MODERATE 64/100 | VERY_HIGH 73/100 | Watch |
| 2 | LTC/USD ⭐ | 41.79 | 67.31 | +0.46% | 3.61x | 13086 | STRONG 99/100 | HIGH 55/100 | Consider small entry |
| 3 | LINK/USD ⭐ | 9.10104 | 66.22 | +0.33% | 5.80x | 8863 | STRONG 98/100 | HIGH 55/100 | Consider small entry |
| 4 | UNI/USD ⭐ | 4.9221 | 65.01 | +0.45% | 2.43x | 9292 | STRONG 98/100 | HIGH 55/100 | Consider small entry |
| 5 | XMR/USD ⭐ | 493.78 | 58.99 | +0.54% | 1.30x | 11794 | STRONG 79/100 | HIGH 61/100 | Watch |

**Same-run overlap:** LINK/USD, UNI/USD, LTC/USD, XMR/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
