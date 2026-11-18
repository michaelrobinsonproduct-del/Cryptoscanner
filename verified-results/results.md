# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-18T02:25:00.258870+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/44223030066
**Source SHA:** 394c17eeb7071fba40e02dbbb1ea97cedb3a0a8a
**Previous ledger commit:** 1421d2070fcbcafd386e68794878dfbaea511897 (atomic ledger/results publication)
**Ledger generation:** 506 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 2s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 627; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 609; valid market observations: 609; OHLC screened: 8.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | AKT/USD | 0.5221 | 62.132 | 44.231 | +2.51% | +0.58% | 4.39x | 11.5 | 2026-11-18T02:24:57.762844+00:00 | Not calibrated | STRONG 81/100 | HIGH 66/100 | Watch | WATCH |
| 2 | UP/USD | 0.05527 | 61.867 | 58.932 | +4.30% | +1.06% | 0.77x | 5.4 | 2026-11-18T02:24:57.762844+00:00 | Not calibrated | MODERATE 61/100 | VERY_HIGH 74/100 | Watch | WATCH |
| 3 | PEARL/USD | 1.8245 | 61.132 | 40.542 | +0.77% | +1.12% | 5.51x | 0.5 | 2026-11-18T02:24:57.762844+00:00 | Not calibrated | STRONG 86/100 | HIGH 60/100 | Watch | WATCH |
| 4 | CAP/USD | 0.101373 | 43.067 | 32.223 | +0.40% | -0.83% | 3.46x | 5.4 | 2026-11-18T02:24:57.762844+00:00 | Not calibrated | MODERATE 52/100 | HIGH 66/100 | Watch | WATCH |
| 5 | TON/USD | 1.085 | 38.438 | 39.589 | +0.74% | -0.46% | 1.11x | 9.2 | 2026-11-18T02:24:57.762844+00:00 | Not calibrated | WEAK 29/100 | HIGH 68/100 | Do nothing | WATCH |
| 6 | SENT/USD | 0.018759 | 35.701 | 30.225 | +0.48% | +0.43% | 1.33x | 8.0 | 2026-11-18T02:24:57.762844+00:00 | Not calibrated | MODERATE 63/100 | HIGH 67/100 | Watch | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | UP/USD | 58.932 | 0.05527 | +1.06% | 0.77x |
| 2 | AKT/USD | 44.231 | 0.5221 | +0.58% | 4.39x |
| 3 | PEARL/USD | 40.542 | 1.8245 | +1.12% | 5.51x |
| 4 | TON/USD | 39.589 | 1.085 | -0.46% | 1.11x |
| 5 | CAP/USD | 32.223 | 0.101373 | -0.83% | 3.46x |
| 6 | SENT/USD | 30.225 | 0.018759 | +0.43% | 1.33x |

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

- Persisted scans: 506; predictions: 4310; observations: 305161.
- Matured sampled outcomes across 1/6/24/48h: 3468; gap abstentions: 12412. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 0 (sampled only; not a success-rate estimate).
- False positives / missed movers: NOT VERIFIED without eligible continuous outcome coverage.
- Baseline vs challenger: recorded as-of; unbiased held-out lift NOT MEASURED.
- Online Kraken /USD stablecoin-base pairs excluded: 18 (counted from this scan's online AssetPairs metadata, not inferred from price).
- Stablecoin base exclusions: BRL1, BUSD, DAI, EUR, EURC, EUROP, EURQ, EURR, EURT, FDUSD, FRAX, GUSD, PYUSD, QCAD, RLUSD, TGBP, TUSD, USD, USD1, USDC, USDD, USDE, USDG, USDQ, USDR, USDS, USDT, ZUSD.
- DEX: NOT USED; no DEX freshness gate.
- OHLC screening abstentions: 2; details in immutable scan JSON artifact.
- Storage: ledger and results published in one non-force Git commit and read back. Independent artifact recovery is NOT VERIFIED by this scan alone.
- Errors: none in successful committed scan; a failed workflow must not publish a SUCCESS report.

# Cryptoscanner — challenger and independent legacy-inspired WATCH

Paper only · risk is high or higher · 30%+ in 48h probability NOT CALIBRATED
Signal confidence 0–100 means setup strength only, NOT a win probability. Actions are research guidance; no trade authorization.

**Writer:** 44223030066 · **Generation:** 506 · **Legacy run:** 44223030066
**Main quote time:** 2026-11-18T02:25:00.258870+00:00 · **Legacy report time:** 2026-11-18T02:25:13.162261+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | AKT/USD ⭐ | 0.5221 | 62.13 | +0.58% | 4.39x | STRONG 91/100 | HIGH 66/100 | Consider small entry |
| 2 | UP/USD | 0.05527 | 61.87 | +1.06% | 0.77x | MODERATE 61/100 | VERY_HIGH 74/100 | Watch |
| 3 | PEARL/USD | 1.8245 | 61.13 | +1.12% | 5.51x | STRONG 86/100 | HIGH 60/100 | Watch |
| 4 | CAP/USD | 0.101373 | 43.07 | -0.83% | 3.46x | MODERATE 52/100 | HIGH 66/100 | Watch |
| 5 | TON/USD | 1.085 | 38.44 | -0.46% | 1.11x | WEAK 29/100 | HIGH 68/100 | Do nothing |
| 6 | SENT/USD ⭐ | 0.018759 | 35.70 | +0.43% | 1.33x | STRONG 73/100 | HIGH 67/100 | Watch |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | AKT/USD ⭐ | 0.5221 | 64.14 | +0.85% | 6.56x | 3681 | STRONG 97/100 | HIGH 60/100 | Consider small entry |
| 2 | SENT/USD ⭐ | 0.018759 | 31.06 | +0.21% | 1.53x | 3815 | STRONG 71/100 | HIGH 67/100 | Watch |

**Same-run overlap:** AKT/USD, SENT/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
