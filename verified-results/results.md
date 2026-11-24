# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-24T19:26:58.663900+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/45469895155
**Source SHA:** 858c8bc8ec5d7641ddb39cacd8aca91719f855b1
**Previous ledger commit:** 6d6f0e416059c572301d7f15c339ac853433e53f (atomic ledger/results publication)
**Ledger generation:** 1616 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 4s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 628; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 610; valid market observations: 609; OHLC screened: 13.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | LUNA/USD | 4.621e-05 | 85.393 | 72.762 | +6.30% | -0.47% | 9.37x | 6.5 | 2026-11-24T19:26:55.052817+00:00 | Not calibrated | STRONG 73/100 | HIGH 66/100 | Watch | WATCH |
| 2 | VVV/USD | 24.85 | 66.202 | 66.108 | +1.64% | -0.15% | 1.08x | 0.8 | 2026-11-24T19:26:55.052817+00:00 | Not calibrated | WEAK 43/100 | HIGH 68/100 | Watch | WATCH |
| 3 | XMR/USD | 500.65 | 62.467 | 70.278 | +3.01% | -0.47% | 0.45x | 11.6 | 2026-11-24T19:26:55.052817+00:00 | Not calibrated | WEAK 31/100 | VERY_HIGH 82/100 | Do nothing | WATCH |
| 4 | PEPE/USD | 3.466e-06 | 54.591 | 49.986 | +1.29% | +0.64% | 1.14x | 5.8 | 2026-11-24T19:26:55.052817+00:00 | Not calibrated | MODERATE 62/100 | HIGH 62/100 | Watch | WATCH |
| 5 | GBP/USD | 1.311 | 50.060 | 59.086 | +0.59% | -0.02% | 0.11x | 0.2 | 2026-11-24T19:26:55.052817+00:00 | Not calibrated | WEAK 30/100 | VERY_HIGH 76/100 | Do nothing | WATCH |
| 6 | NIGHT/USD | 0.04881 | 41.872 | 47.407 | +1.37% | +0.66% | 0.12x | 6.1 | 2026-11-24T19:26:55.052817+00:00 | Not calibrated | MODERATE 51/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 7 | AUD/USD | 0.66438 | 37.607 | 44.016 | +0.27% | -0.01% | 0.36x | 1.7 | 2026-11-24T19:26:55.052817+00:00 | Not calibrated | WEAK 24/100 | VERY_HIGH 76/100 | Do nothing | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | LUNA/USD | 72.762 | 4.621e-05 | -0.47% | 9.37x |
| 2 | XMR/USD | 70.278 | 500.65 | -0.47% | 0.45x |
| 3 | VVV/USD | 66.108 | 24.85 | -0.15% | 1.08x |
| 4 | GBP/USD | 59.086 | 1.311 | -0.02% | 0.11x |
| 5 | PEPE/USD | 49.986 | 3.466e-06 | +0.64% | 1.14x |
| 6 | NIGHT/USD | 47.407 | 0.04881 | +0.66% | 0.12x |
| 7 | AUD/USD | 44.016 | 0.66438 | -0.01% | 0.36x |

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

- Persisted scans: 1616; predictions: 13873; observations: 979236.
- Matured sampled outcomes across 1/6/24/48h: 28132; gap abstentions: 22370. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 143 (sampled only; not a success-rate estimate).
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

**Writer:** 45469895155 · **Generation:** 1616 · **Legacy run:** 45469895155
**Main quote time:** 2026-11-24T19:26:58.663900+00:00 · **Legacy report time:** 2026-11-24T19:28:11.740905+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | LUNA/USD | 4.621e-05 | 85.39 | -0.47% | 9.37x | STRONG 73/100 | HIGH 66/100 | Watch |
| 2 | VVV/USD | 24.85 | 66.20 | -0.15% | 1.08x | WEAK 43/100 | HIGH 68/100 | Watch |
| 3 | XMR/USD | 500.65 | 62.47 | -0.47% | 0.45x | WEAK 31/100 | VERY_HIGH 82/100 | Do nothing |
| 4 | PEPE/USD ⭐ | 3.466e-06 | 54.59 | +0.64% | 1.14x | STRONG 72/100 | HIGH 62/100 | Watch |
| 5 | GBP/USD | 1.311 | 50.06 | -0.02% | 0.11x | WEAK 30/100 | VERY_HIGH 76/100 | Do nothing |
| 6 | NIGHT/USD | 0.04881 | 41.87 | +0.66% | 0.12x | MODERATE 51/100 | VERY_HIGH 70/100 | Watch |
| 7 | AUD/USD | 0.66438 | 37.61 | -0.01% | 0.36x | WEAK 24/100 | VERY_HIGH 76/100 | Do nothing |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | PEPE/USD ⭐ | 3.474e-06 | 54.54 | +0.64% | 1.14x | 6640 | STRONG 72/100 | HIGH 62/100 | Watch |

**Same-run overlap:** PEPE/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
