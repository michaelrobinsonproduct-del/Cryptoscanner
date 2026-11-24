# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-24T17:55:24.588678+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/45452810083
**Source SHA:** 858c8bc8ec5d7641ddb39cacd8aca91719f855b1
**Previous ledger commit:** f5fba88111ad89874ad03332fec97ba2ab3b838a (atomic ledger/results publication)
**Ledger generation:** 1607 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 5s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 628; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 610; valid market observations: 609; OHLC screened: 12.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | XMR/USD | 501.62 | 91.572 | 76.173 | +3.21% | +0.08% | 5.70x | 2.6 | 2026-11-24T17:55:19.765911+00:00 | Not calibrated | STRONG 91/100 | HIGH 55/100 | Watch | WATCH |
| 2 | VVV/USD | 25.295 | 77.552 | 75.879 | +3.46% | -0.07% | 1.20x | 6.7 | 2026-11-24T17:55:19.765911+00:00 | Not calibrated | MODERATE 49/100 | HIGH 68/100 | Watch | WATCH |
| 3 | GBP/USD | 1.31172 | 74.397 | 59.321 | +0.65% | +0.02% | 2.90x | 0.5 | 2026-11-24T17:55:19.765911+00:00 | Not calibrated | STRONG 82/100 | HIGH 55/100 | Watch | WATCH |
| 4 | LUNA/USD | 4.818e-05 | 71.371 | 55.952 | +10.84% | +0.08% | 16.06x | 41.7 | 2026-11-24T17:55:19.765911+00:00 | Not calibrated | MODERATE 66/100 | VERY_HIGH 82/100 | Watch | WATCH |
| 5 | 2Z/USD | 0.01628 | 68.155 | 49.754 | +4.03% | +0.68% | 3.79x | 18.4 | 2026-11-24T17:55:19.765911+00:00 | Not calibrated | STRONG 84/100 | VERY_HIGH 73/100 | Watch | WATCH |
| 6 | AUD/USD | 0.66441 | 54.086 | 43.518 | +0.27% | +0.03% | 2.04x | 2.7 | 2026-11-24T17:55:19.765911+00:00 | Not calibrated | STRONG 72/100 | HIGH 55/100 | Watch | WATCH |
| 7 | ZEUS/USD | 0.00466 | 53.888 | 54.603 | +6.39% | -0.21% | 1.04x | 43.0 | 2026-11-24T17:55:19.765911+00:00 | Not calibrated | WEAK 22/100 | EXTREME 100/100 | Do nothing | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | XMR/USD | 76.173 | 501.62 | +0.08% | 5.70x |
| 2 | VVV/USD | 75.879 | 25.295 | -0.07% | 1.20x |
| 3 | GBP/USD | 59.321 | 1.31172 | +0.02% | 2.90x |
| 4 | LUNA/USD | 55.952 | 4.818e-05 | +0.08% | 16.06x |
| 5 | ZEUS/USD | 54.603 | 0.00466 | -0.21% | 1.04x |
| 6 | 2Z/USD | 49.754 | 0.01628 | +0.68% | 3.79x |
| 7 | AUD/USD | 43.518 | 0.66441 | +0.03% | 2.04x |

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

- Persisted scans: 1607; predictions: 13804; observations: 973755.
- Matured sampled outcomes across 1/6/24/48h: 27745; gap abstentions: 22370. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 143 (sampled only; not a success-rate estimate).
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

**Writer:** 45452810083 · **Generation:** 1607 · **Legacy run:** 45452810083
**Main quote time:** 2026-11-24T17:55:24.588678+00:00 · **Legacy report time:** 2026-11-24T17:56:26.054987+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | XMR/USD ⭐ | 501.62 | 91.57 | +0.08% | 5.70x | STRONG 100/100 | HIGH 55/100 | Watch |
| 2 | VVV/USD | 25.295 | 77.55 | -0.07% | 1.20x | MODERATE 49/100 | HIGH 68/100 | Watch |
| 3 | GBP/USD | 1.31172 | 74.40 | +0.02% | 2.90x | STRONG 82/100 | HIGH 55/100 | Watch |
| 4 | LUNA/USD ⭐ | 4.818e-05 | 71.37 | +0.08% | 16.06x | STRONG 76/100 | VERY_HIGH 82/100 | Watch |
| 5 | 2Z/USD ⭐ | 0.01628 | 68.16 | +0.68% | 3.79x | STRONG 94/100 | VERY_HIGH 73/100 | Watch |
| 6 | AUD/USD | 0.66441 | 54.09 | +0.03% | 2.04x | STRONG 72/100 | HIGH 55/100 | Watch |
| 7 | ZEUS/USD | 0.00466 | 53.89 | -0.21% | 1.04x | WEAK 22/100 | EXTREME 100/100 | Do nothing |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | XMR/USD ⭐ | 502.82 | 94.96 | +0.08% | 5.70x | 8965 | STRONG 100/100 | HIGH 55/100 | Watch |
| 2 | LUNA/USD ⭐ | 4.812e-05 | 71.84 | +0.08% | 16.06x | 1741 | STRONG 81/100 | VERY_HIGH 72/100 | Watch |
| 3 | 2Z/USD ⭐ | 0.01632 | 70.45 | +0.68% | 3.79x | 1432 | STRONG 95/100 | VERY_HIGH 73/100 | Watch |

**Same-run overlap:** XMR/USD, LUNA/USD, 2Z/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
