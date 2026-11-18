# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-18T03:05:01.810489+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/44227808850
**Source SHA:** 394c17eeb7071fba40e02dbbb1ea97cedb3a0a8a
**Previous ledger commit:** 41252a6c3fd759788cef164539fd1abc10fee06a (atomic ledger/results publication)
**Ledger generation:** 514 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 3s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 627; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 609; valid market observations: 609; OHLC screened: 10.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | CC/USD | 0.08314 | 47.916 | 40.104 | +1.23% | +0.74% | 1.41x | 7.2 | 2026-11-18T03:04:58.366175+00:00 | Not calibrated | MODERATE 69/100 | HIGH 60/100 | Watch | WATCH |
| 2 | AKT/USD | 0.5208 | 39.723 | 44.358 | +2.26% | -0.76% | 0.92x | 7.7 | 2026-11-18T03:04:58.366175+00:00 | Not calibrated | WEAK 25/100 | VERY_HIGH 73/100 | Do nothing | WATCH |
| 3 | SENT/USD | 0.01874 | 39.426 | 31.644 | +0.38% | +0.73% | 1.42x | 3.7 | 2026-11-18T03:04:58.366175+00:00 | Not calibrated | MODERATE 65/100 | HIGH 67/100 | Watch | WATCH |
| 4 | ICNT/USD | 0.2817 | 37.821 | 35.787 | +2.03% | -0.96% | 1.68x | 21.4 | 2026-11-18T03:04:58.366175+00:00 | Not calibrated | WEAK 29/100 | VERY_HIGH 78/100 | Do nothing | WATCH |
| 5 | AKE/USD | 0.01003 | 35.068 | 25.715 | +0.46% | +0.44% | 1.72x | 24.6 | 2026-11-18T03:04:58.366175+00:00 | Not calibrated | MODERATE 53/100 | VERY_HIGH 72/100 | Watch | WATCH |
| 6 | CAP/USD | 0.101272 | 23.853 | 31.086 | +0.30% | +0.21% | 0.17x | 6.1 | 2026-11-18T03:04:58.366175+00:00 | Not calibrated | WEAK 42/100 | VERY_HIGH 75/100 | Watch | WATCH |
| 7 | TON/USD | 1.081 | 22.163 | 32.232 | +0.37% | -0.46% | 0.22x | 18.6 | 2026-11-18T03:04:58.366175+00:00 | Not calibrated | WEAK 11/100 | VERY_HIGH 82/100 | Do nothing | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | AKT/USD | 44.358 | 0.5208 | -0.76% | 0.92x |
| 2 | CC/USD | 40.104 | 0.08314 | +0.74% | 1.41x |
| 3 | ICNT/USD | 35.787 | 0.2817 | -0.96% | 1.68x |
| 4 | TON/USD | 32.232 | 1.081 | -0.46% | 0.22x |
| 5 | SENT/USD | 31.644 | 0.01874 | +0.73% | 1.42x |
| 6 | CAP/USD | 31.086 | 0.101272 | +0.21% | 0.17x |
| 7 | AKE/USD | 25.715 | 0.01003 | +0.44% | 1.72x |

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

- Persisted scans: 514; predictions: 4351; observations: 310033.
- Matured sampled outcomes across 1/6/24/48h: 3499; gap abstentions: 12424. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 0 (sampled only; not a success-rate estimate).
- False positives / missed movers: NOT VERIFIED without eligible continuous outcome coverage.
- Baseline vs challenger: recorded as-of; unbiased held-out lift NOT MEASURED.
- Online Kraken /USD stablecoin-base pairs excluded: 18 (counted from this scan's online AssetPairs metadata, not inferred from price).
- Stablecoin base exclusions: BRL1, BUSD, DAI, EUR, EURC, EUROP, EURQ, EURR, EURT, FDUSD, FRAX, GUSD, PYUSD, QCAD, RLUSD, TGBP, TUSD, USD, USD1, USDC, USDD, USDE, USDG, USDQ, USDR, USDS, USDT, ZUSD.
- DEX: NOT USED; no DEX freshness gate.
- OHLC screening abstentions: 3; details in immutable scan JSON artifact.
- Storage: ledger and results published in one non-force Git commit and read back. Independent artifact recovery is NOT VERIFIED by this scan alone.
- Errors: none in successful committed scan; a failed workflow must not publish a SUCCESS report.

# Cryptoscanner — challenger and independent legacy-inspired WATCH

Paper only · risk is high or higher · 30%+ in 48h probability NOT CALIBRATED
Signal confidence 0–100 means setup strength only, NOT a win probability. Actions are research guidance; no trade authorization.

**Writer:** 44227808850 · **Generation:** 514 · **Legacy run:** 44227808850
**Main quote time:** 2026-11-18T03:05:01.810489+00:00 · **Legacy report time:** 2026-11-18T03:05:15.328838+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | CC/USD ⭐ | 0.08314 | 47.92 | +0.74% | 1.41x | STRONG 79/100 | HIGH 60/100 | Watch |
| 2 | AKT/USD | 0.5208 | 39.72 | -0.76% | 0.92x | WEAK 25/100 | VERY_HIGH 73/100 | Do nothing |
| 3 | SENT/USD ⭐ | 0.01874 | 39.43 | +0.73% | 1.42x | STRONG 75/100 | HIGH 67/100 | Watch |
| 4 | ICNT/USD ⭐ | 0.2817 | 37.82 | -0.96% | 1.68x | WEAK 39/100 | VERY_HIGH 78/100 | Watch |
| 5 | AKE/USD ⭐ | 0.01003 | 35.07 | +0.44% | 1.72x | MODERATE 63/100 | VERY_HIGH 72/100 | Watch |
| 6 | CAP/USD | 0.101272 | 23.85 | +0.21% | 0.17x | WEAK 42/100 | VERY_HIGH 75/100 | Watch |
| 7 | TON/USD | 1.081 | 22.16 | -0.46% | 0.22x | WEAK 11/100 | VERY_HIGH 82/100 | Do nothing |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | CC/USD ⭐ | 0.08314 | 50.29 | +1.06% | 1.48x | 3980 | STRONG 80/100 | HIGH 60/100 | Watch |
| 2 | ICNT/USD ⭐ | 0.2799 | 49.50 | +1.62% | 2.19x | 3707 | STRONG 85/100 | HIGH 66/100 | Consider small entry |
| 3 | SENT/USD ⭐ | 0.01874 | 38.67 | +0.90% | 1.34x | 3801 | STRONG 74/100 | HIGH 67/100 | Watch |
| 4 | ZAMA/USD | 0.06004 | 38.41 | +1.45% | 2.95x | 4489 | MODERATE 69/100 | HIGH 66/100 | Watch |
| 5 | AKE/USD ⭐ | 0.01004179 | 35.94 | +0.44% | 1.72x | 5475 | MODERATE 63/100 | VERY_HIGH 72/100 | Watch |

**Same-run overlap:** CC/USD, SENT/USD, ICNT/USD, AKE/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
