# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-18T04:35:03.417091+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/44238272903
**Source SHA:** 394c17eeb7071fba40e02dbbb1ea97cedb3a0a8a
**Previous ledger commit:** dfd4061052d84258a03e9497480cf6480e66dd79 (atomic ledger/results publication)
**Ledger generation:** 532 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 4s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 627; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 609; valid market observations: 609; OHLC screened: 15.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | SENT/USD | 0.019193 | 62.461 | 46.652 | +2.81% | +0.16% | 4.75x | 7.8 | 2026-11-18T04:34:59.269320+00:00 | Not calibrated | STRONG 76/100 | HIGH 67/100 | Watch | WATCH |
| 2 | XDC/USD | 0.03115 | 52.633 | 55.094 | +2.74% | +0.71% | 0.40x | 3.2 | 2026-11-18T04:34:59.269320+00:00 | Not calibrated | MODERATE 56/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 3 | PEARL/USD | 1.8445 | 52.556 | 43.519 | +1.88% | +0.70% | 1.55x | 9.3 | 2026-11-18T04:34:59.269320+00:00 | Not calibrated | STRONG 71/100 | HIGH 60/100 | Watch | WATCH |
| 4 | UAI/USD | 0.03367 | 51.395 | 31.143 | +0.87% | +1.05% | 3.06x | 11.9 | 2026-11-18T04:34:59.269320+00:00 | Not calibrated | STRONG 76/100 | VERY_HIGH 73/100 | Watch | WATCH |
| 5 | CC/USD | 0.08315 | 35.459 | 41.202 | +1.24% | -0.75% | 0.80x | 6.0 | 2026-11-18T04:34:59.269320+00:00 | Not calibrated | WEAK 23/100 | VERY_HIGH 73/100 | Do nothing | WATCH |
| 6 | ZAMA/USD | 0.06055 | 26.543 | 33.082 | +1.03% | -0.66% | 0.67x | 14.9 | 2026-11-18T04:34:59.269320+00:00 | Not calibrated | WEAK 13/100 | EXTREME 87/100 | Do nothing | WATCH |
| 7 | AKT/USD | 0.5138 | 18.646 | 30.703 | +0.88% | -0.81% | 0.20x | 15.6 | 2026-11-18T04:34:59.269320+00:00 | Not calibrated | WEAK 9/100 | EXTREME 87/100 | Do nothing | WATCH |
| 8 | MELANIA/USD | 0.0499 | 11.381 | 27.893 | +2.46% | -2.16% | 0.43x | 40.2 | 2026-11-18T04:34:59.269320+00:00 | Not calibrated | WEAK 0/100 | EXTREME 100/100 | Do nothing | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | XDC/USD | 55.094 | 0.03115 | +0.71% | 0.40x |
| 2 | SENT/USD | 46.652 | 0.019193 | +0.16% | 4.75x |
| 3 | PEARL/USD | 43.519 | 1.8445 | +0.70% | 1.55x |
| 4 | CC/USD | 41.202 | 0.08315 | -0.75% | 0.80x |
| 5 | ZAMA/USD | 33.082 | 0.06055 | -0.66% | 0.67x |
| 6 | UAI/USD | 31.143 | 0.03367 | +1.05% | 3.06x |
| 7 | AKT/USD | 30.703 | 0.5138 | -0.81% | 0.20x |
| 8 | MELANIA/USD | 27.893 | 0.0499 | -2.16% | 0.43x |

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

- Persisted scans: 532; predictions: 4496; observations: 320995.
- Matured sampled outcomes across 1/6/24/48h: 3572; gap abstentions: 12463. Per-horizon counts require independent audit; do not infer held-out lift.
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

**Writer:** 44238272903 · **Generation:** 532 · **Legacy run:** 44238272903
**Main quote time:** 2026-11-18T04:35:03.417091+00:00 · **Legacy report time:** 2026-11-18T04:35:19.783155+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | SENT/USD ⭐ | 0.019193 | 62.46 | +0.16% | 4.75x | STRONG 86/100 | HIGH 67/100 | Watch |
| 2 | XDC/USD | 0.03115 | 52.63 | +0.71% | 0.40x | MODERATE 56/100 | VERY_HIGH 70/100 | Watch |
| 3 | PEARL/USD ⭐ | 1.8445 | 52.56 | +0.70% | 1.55x | STRONG 81/100 | HIGH 60/100 | Consider small entry |
| 4 | UAI/USD ⭐ | 0.03367 | 51.39 | +1.05% | 3.06x | STRONG 86/100 | VERY_HIGH 73/100 | Watch |
| 5 | CC/USD | 0.08315 | 35.46 | -0.75% | 0.80x | WEAK 23/100 | VERY_HIGH 73/100 | Do nothing |
| 6 | ZAMA/USD | 0.06055 | 26.54 | -0.66% | 0.67x | WEAK 13/100 | EXTREME 87/100 | Do nothing |
| 7 | AKT/USD | 0.5138 | 18.65 | -0.81% | 0.20x | WEAK 9/100 | EXTREME 87/100 | Do nothing |
| 8 | MELANIA/USD | 0.0499 | 11.38 | -2.16% | 0.43x | WEAK 0/100 | EXTREME 100/100 | Do nothing |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | ICNT/USD | 0.2881 | 82.66 | +1.09% | 5.25x | 3782 | STRONG 86/100 | VERY_HIGH 72/100 | Watch |
| 2 | SENT/USD ⭐ | 0.019193 | 64.71 | +0.16% | 4.75x | 4012 | STRONG 87/100 | HIGH 67/100 | Watch |
| 3 | PEARL/USD ⭐ | 1.8445 | 51.85 | +0.70% | 1.55x | 4043 | STRONG 81/100 | HIGH 60/100 | Consider small entry |
| 4 | UAI/USD ⭐ | 0.03367 | 39.64 | +1.05% | 3.06x | 2095 | STRONG 80/100 | VERY_HIGH 73/100 | Watch |

**Same-run overlap:** SENT/USD, PEARL/USD, UAI/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
