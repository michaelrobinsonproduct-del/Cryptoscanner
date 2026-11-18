# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-18T03:20:02.485955+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/44229616016
**Source SHA:** 394c17eeb7071fba40e02dbbb1ea97cedb3a0a8a
**Previous ledger commit:** 6d9cd7bb3f225526627c9b8db009e26f1bfcebff (atomic ledger/results publication)
**Ledger generation:** 517 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 3s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 627; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 609; valid market observations: 609; OHLC screened: 10.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | ICNT/USD | 0.2832 | 60.790 | 43.221 | +2.57% | +1.54% | 1.99x | 14.2 | 2026-11-18T03:19:59.422257+00:00 | Not calibrated | STRONG 70/100 | HIGH 66/100 | Watch | WATCH |
| 2 | PIEVERSE/USD | 2.1675 | 57.853 | 60.001 | +5.80% | +0.41% | 0.58x | 24.9 | 2026-11-18T03:19:59.422257+00:00 | Not calibrated | MODERATE 49/100 | EXTREME 87/100 | Do nothing | WATCH |
| 3 | CC/USD | 0.08348 | 54.689 | 43.630 | +1.64% | +0.59% | 1.81x | 6.0 | 2026-11-18T03:19:59.422257+00:00 | Not calibrated | STRONG 72/100 | HIGH 60/100 | Watch | WATCH |
| 4 | ZAMA/USD | 0.06025 | 48.077 | 31.328 | +0.53% | +0.35% | 5.86x | 11.6 | 2026-11-18T03:19:59.422257+00:00 | Not calibrated | STRONG 74/100 | HIGH 66/100 | Watch | WATCH |
| 5 | SENT/USD | 0.018803 | 37.416 | 33.744 | +0.72% | +0.34% | 1.20x | 4.3 | 2026-11-18T03:19:59.422257+00:00 | Not calibrated | MODERATE 54/100 | VERY_HIGH 74/100 | Watch | WATCH |
| 6 | PEARL/USD | 1.8199 | 28.802 | 29.483 | +0.52% | +0.44% | 0.71x | 18.7 | 2026-11-18T03:19:59.422257+00:00 | Not calibrated | WEAK 39/100 | VERY_HIGH 81/100 | Watch | WATCH |
| 7 | AKT/USD | 0.5156 | 20.943 | 33.266 | +1.24% | -1.00% | 0.27x | 15.5 | 2026-11-18T03:19:59.422257+00:00 | Not calibrated | WEAK 10/100 | EXTREME 87/100 | Do nothing | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | PIEVERSE/USD | 60.001 | 2.1675 | +0.41% | 0.58x |
| 2 | CC/USD | 43.630 | 0.08348 | +0.59% | 1.81x |
| 3 | ICNT/USD | 43.221 | 0.2832 | +1.54% | 1.99x |
| 4 | SENT/USD | 33.744 | 0.018803 | +0.34% | 1.20x |
| 5 | AKT/USD | 33.266 | 0.5156 | -1.00% | 0.27x |
| 6 | ZAMA/USD | 31.328 | 0.06025 | +0.35% | 5.86x |
| 7 | PEARL/USD | 29.483 | 1.8199 | +0.44% | 0.71x |

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

- Persisted scans: 517; predictions: 4372; observations: 311860.
- Matured sampled outcomes across 1/6/24/48h: 3510; gap abstentions: 12424. Per-horizon counts require independent audit; do not infer held-out lift.
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

**Writer:** 44229616016 · **Generation:** 517 · **Legacy run:** 44229616016
**Main quote time:** 2026-11-18T03:20:02.485955+00:00 · **Legacy report time:** 2026-11-18T03:20:17.548427+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | ICNT/USD ⭐ | 0.2832 | 60.79 | +1.54% | 1.99x | STRONG 80/100 | HIGH 66/100 | Consider small entry |
| 2 | PIEVERSE/USD | 2.1675 | 57.85 | +0.41% | 0.58x | MODERATE 49/100 | EXTREME 87/100 | Do nothing |
| 3 | CC/USD ⭐ | 0.08348 | 54.69 | +0.59% | 1.81x | STRONG 82/100 | HIGH 60/100 | Consider small entry |
| 4 | ZAMA/USD ⭐ | 0.06025 | 48.08 | +0.35% | 5.86x | STRONG 84/100 | HIGH 66/100 | Consider small entry |
| 5 | SENT/USD ⭐ | 0.018803 | 37.42 | +0.34% | 1.20x | MODERATE 64/100 | VERY_HIGH 74/100 | Watch |
| 6 | PEARL/USD | 1.8199 | 28.80 | +0.44% | 0.71x | WEAK 39/100 | VERY_HIGH 81/100 | Watch |
| 7 | AKT/USD | 0.5156 | 20.94 | -1.00% | 0.27x | WEAK 10/100 | EXTREME 87/100 | Do nothing |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | ICNT/USD ⭐ | 0.2832 | 60.01 | +0.53% | 1.83x | 3770 | STRONG 85/100 | HIGH 60/100 | Consider small entry |
| 2 | CC/USD ⭐ | 0.08348 | 57.03 | +0.41% | 4.27x | 3972 | STRONG 94/100 | HIGH 60/100 | Consider small entry |
| 3 | XMR/USD | 510.17 | 49.77 | +0.58% | 7.22x | 12755 | STRONG 75/100 | HIGH 61/100 | Watch |
| 4 | ZAMA/USD ⭐ | 0.06025 | 39.51 | +0.35% | 5.86x | 4483 | STRONG 80/100 | HIGH 66/100 | Consider small entry |
| 5 | SENT/USD ⭐ | 0.018803 | 39.41 | +0.34% | 1.20x | 3769 | MODERATE 65/100 | VERY_HIGH 74/100 | Watch |

**Same-run overlap:** ICNT/USD, CC/USD, ZAMA/USD, SENT/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
