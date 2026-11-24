# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-24T17:11:56.663746+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/45445402767
**Source SHA:** 858c8bc8ec5d7641ddb39cacd8aca91719f855b1
**Previous ledger commit:** 32fdd20a98a7b35e816f0adf6004e524f925e67a (atomic ledger/results publication)
**Ledger generation:** 1602 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 3s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 628; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 610; valid market observations: 609; OHLC screened: 9.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | LUNA/USD | 4.651e-05 | 72.010 | 66.756 | +6.99% | -0.21% | 1.63x | 19.3 | 2026-11-24T17:11:53.805574+00:00 | Not calibrated | MODERATE 51/100 | VERY_HIGH 79/100 | Watch | WATCH |
| 2 | VVV/USD | 25.102 | 69.288 | 63.548 | +2.68% | +1.11% | 1.02x | 20.4 | 2026-11-24T17:11:53.805574+00:00 | Not calibrated | MODERATE 60/100 | VERY_HIGH 74/100 | Watch | WATCH |
| 3 | XMR/USD | 498.01 | 62.777 | 68.052 | +2.47% | +0.31% | 0.32x | 8.4 | 2026-11-24T17:11:53.805574+00:00 | Not calibrated | MODERATE 61/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 4 | 2Z/USD | 0.01625 | 57.834 | 54.511 | +3.83% | +0.56% | 1.05x | 6.1 | 2026-11-24T17:11:53.805574+00:00 | Not calibrated | MODERATE 64/100 | VERY_HIGH 74/100 | Watch | WATCH |
| 5 | ZEUS/USD | 0.00469 | 52.495 | 54.984 | +7.08% | -3.50% | 3.04x | 42.6 | 2026-11-24T17:11:53.805574+00:00 | Not calibrated | WEAK 41/100 | EXTREME 99/100 | Do nothing | WATCH |
| 6 | GBP/USD | 1.31088 | 50.802 | 58.793 | +0.59% | +0.04% | 0.18x | 0.6 | 2026-11-24T17:11:53.805574+00:00 | Not calibrated | MODERATE 45/100 | VERY_HIGH 70/100 | Watch | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | XMR/USD | 68.052 | 498.01 | +0.31% | 0.32x |
| 2 | LUNA/USD | 66.756 | 4.651e-05 | -0.21% | 1.63x |
| 3 | VVV/USD | 63.548 | 25.102 | +1.11% | 1.02x |
| 4 | GBP/USD | 58.793 | 1.31088 | +0.04% | 0.18x |
| 5 | ZEUS/USD | 54.984 | 0.00469 | -3.50% | 3.04x |
| 6 | 2Z/USD | 54.511 | 0.01625 | +0.56% | 1.05x |

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

- Persisted scans: 1602; predictions: 13768; observations: 970710.
- Matured sampled outcomes across 1/6/24/48h: 27580; gap abstentions: 22370. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 143 (sampled only; not a success-rate estimate).
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

**Writer:** 45445402767 · **Generation:** 1602 · **Legacy run:** 45445402767
**Main quote time:** 2026-11-24T17:11:56.663746+00:00 · **Legacy report time:** 2026-11-24T17:13:01.086370+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | LUNA/USD | 4.651e-05 | 72.01 | -0.21% | 1.63x | MODERATE 51/100 | VERY_HIGH 79/100 | Watch |
| 2 | VVV/USD ⭐ | 25.102 | 69.29 | +1.11% | 1.02x | STRONG 70/100 | VERY_HIGH 74/100 | Watch |
| 3 | XMR/USD | 498.01 | 62.78 | +0.31% | 0.32x | MODERATE 61/100 | VERY_HIGH 70/100 | Watch |
| 4 | 2Z/USD ⭐ | 0.01625 | 57.83 | +0.56% | 1.05x | STRONG 74/100 | VERY_HIGH 74/100 | Watch |
| 5 | ZEUS/USD | 0.00469 | 52.49 | -3.50% | 3.04x | WEAK 41/100 | EXTREME 99/100 | Do nothing |
| 6 | GBP/USD | 1.31088 | 50.80 | +0.04% | 0.18x | MODERATE 45/100 | VERY_HIGH 70/100 | Watch |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | VVV/USD ⭐ | 24.99 | 72.41 | +1.11% | 1.02x | 15432 | STRONG 81/100 | HIGH 62/100 | Watch |
| 2 | 2Z/USD ⭐ | 0.01627 | 61.65 | +0.56% | 1.05x | 1413 | STRONG 71/100 | VERY_HIGH 80/100 | Watch |

**Same-run overlap:** VVV/USD, 2Z/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
