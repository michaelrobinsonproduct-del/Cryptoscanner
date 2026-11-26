# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-26T02:16:15.517151+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/45741091131
**Source SHA:** 858c8bc8ec5d7641ddb39cacd8aca91719f855b1
**Previous ledger commit:** e4574737c30ea98ff747b45ab87de8035cc5dce7 (atomic ledger/results publication)
**Ledger generation:** 1798 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 7s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 628; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 610; valid market observations: 609; OHLC screened: 24.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | TIA/USD | 0.3525 | 86.373 | 60.510 | +4.75% | +2.17% | 14.89x | 8.5 | 2026-11-26T02:16:08.836286+00:00 | Not calibrated | STRONG 98/100 | HIGH 67/100 | Consider small entry | WATCH |
| 2 | XRP/USD | 0.95496 | 84.743 | 68.229 | +1.96% | +0.30% | 4.26x | 1.0 | 2026-11-26T02:16:08.836286+00:00 | Not calibrated | STRONG 97/100 | HIGH 55/100 | Consider small entry | WATCH |
| 3 | TAO/USD | 185.106 | 82.485 | 66.138 | +1.93% | +0.27% | 2.72x | 4.8 | 2026-11-26T02:16:08.836286+00:00 | Not calibrated | STRONG 96/100 | HIGH 55/100 | Consider small entry | WATCH |
| 4 | ADA/USD | 0.148505 | 80.379 | 65.946 | +1.88% | +0.57% | 2.16x | 4.4 | 2026-11-26T02:16:08.836286+00:00 | Not calibrated | STRONG 95/100 | HIGH 55/100 | Consider small entry | WATCH |
| 5 | NEAR/USD | 3.0979 | 79.891 | 63.272 | +1.57% | +0.32% | 2.50x | 5.5 | 2026-11-26T02:16:08.836286+00:00 | Not calibrated | STRONG 95/100 | HIGH 55/100 | Consider small entry | WATCH |
| 6 | LTC/USD | 43.83 | 77.372 | 72.216 | +2.62% | +0.85% | 1.09x | 2.3 | 2026-11-26T02:16:08.836286+00:00 | Not calibrated | STRONG 74/100 | HIGH 62/100 | Watch | WATCH |
| 7 | XDG/USD | 0.0568111 | 77.013 | 60.437 | +1.52% | +0.32% | 3.04x | 0.3 | 2026-11-26T02:16:08.836286+00:00 | Not calibrated | STRONG 94/100 | HIGH 55/100 | Consider small entry | WATCH |
| 8 | VVV/USD | 30.148 | 69.775 | 73.697 | +3.26% | -0.08% | 0.65x | 8.3 | 2026-11-26T02:16:08.836286+00:00 | Not calibrated | WEAK 40/100 | VERY_HIGH 76/100 | Watch | WATCH |
| 9 | ZEC/USD | 780.73 | 68.923 | 62.639 | +1.37% | +0.34% | 1.46x | 3.8 | 2026-11-26T02:16:08.836286+00:00 | Not calibrated | STRONG 79/100 | HIGH 55/100 | Watch | WATCH |
| 10 | XLM/USD | 0.129137 | 65.438 | 50.201 | +1.03% | +0.05% | 4.41x | 2.8 | 2026-11-26T02:16:08.836286+00:00 | Not calibrated | STRONG 78/100 | HIGH 55/100 | Watch | WATCH |
| 11 | SOL/USD | 71.29 | 63.833 | 63.249 | +1.28% | +0.27% | 0.92x | 1.4 | 2026-11-26T02:16:08.836286+00:00 | Not calibrated | MODERATE 62/100 | HIGH 62/100 | Watch | WATCH |
| 12 | SUI/USD | 0.6795 | 63.273 | 67.396 | +1.98% | +0.61% | 0.28x | 2.9 | 2026-11-26T02:16:08.836286+00:00 | Not calibrated | MODERATE 62/100 | VERY_HIGH 70/100 | Watch | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | VVV/USD | 73.697 | 30.148 | -0.08% | 0.65x |
| 2 | LTC/USD | 72.216 | 43.83 | +0.85% | 1.09x |
| 3 | XRP/USD | 68.229 | 0.95496 | +0.30% | 4.26x |
| 4 | SUI/USD | 67.396 | 0.6795 | +0.61% | 0.28x |
| 5 | TAO/USD | 66.138 | 185.106 | +0.27% | 2.72x |
| 6 | ADA/USD | 65.946 | 0.148505 | +0.57% | 2.16x |
| 7 | NEAR/USD | 63.272 | 3.0979 | +0.32% | 2.50x |
| 8 | SOL/USD | 63.249 | 71.29 | +0.27% | 0.92x |
| 9 | ZEC/USD | 62.639 | 780.73 | +0.34% | 1.46x |
| 10 | TIA/USD | 60.510 | 0.3525 | +2.17% | 14.89x |
| 11 | XDG/USD | 60.437 | 0.0568111 | +0.32% | 3.04x |
| 12 | XLM/USD | 50.201 | 0.129137 | +0.05% | 4.41x |

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

- Persisted scans: 1798; predictions: 15311; observations: 1090026.
- Matured sampled outcomes across 1/6/24/48h: 33263; gap abstentions: 23660. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 146 (sampled only; not a success-rate estimate).
- False positives / missed movers: NOT VERIFIED without eligible continuous outcome coverage.
- Baseline vs challenger: recorded as-of; unbiased held-out lift NOT MEASURED.
- Online Kraken /USD stablecoin-base pairs excluded: 18 (counted from this scan's online AssetPairs metadata, not inferred from price).
- Stablecoin base exclusions: BRL1, BUSD, DAI, EUR, EURC, EUROP, EURQ, EURR, EURT, FDUSD, FRAX, GUSD, PYUSD, QCAD, RLUSD, TGBP, TUSD, USD, USD1, USDC, USDD, USDE, USDG, USDQ, USDR, USDS, USDT, ZUSD.
- DEX: NOT USED; no DEX freshness gate.
- OHLC screening abstentions: 4; details in immutable scan JSON artifact.
- Storage: ledger and results published in one non-force Git commit and read back. Independent artifact recovery is NOT VERIFIED by this scan alone.
- Errors: none in successful committed scan; a failed workflow must not publish a SUCCESS report.

# Cryptoscanner — challenger and independent legacy-inspired WATCH

Paper only · risk is high or higher · 30%+ in 48h probability NOT CALIBRATED
Signal confidence 0–100 means setup strength only, NOT a win probability. Actions are research guidance; no trade authorization.

**Writer:** 45741091131 · **Generation:** 1798 · **Legacy run:** 45741091131
**Main quote time:** 2026-11-26T02:16:15.517151+00:00 · **Legacy report time:** 2026-11-26T02:17:26.607154+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | TIA/USD ⭐ | 0.3525 | 86.37 | +2.17% | 14.89x | STRONG 100/100 | HIGH 67/100 | Consider small entry |
| 2 | XRP/USD ⭐ | 0.95496 | 84.74 | +0.30% | 4.26x | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 3 | TAO/USD | 185.106 | 82.49 | +0.27% | 2.72x | STRONG 96/100 | HIGH 55/100 | Consider small entry |
| 4 | ADA/USD | 0.148505 | 80.38 | +0.57% | 2.16x | STRONG 95/100 | HIGH 55/100 | Consider small entry |
| 5 | NEAR/USD ⭐ | 3.0979 | 79.89 | +0.32% | 2.50x | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 6 | LTC/USD ⭐ | 43.83 | 77.37 | +0.85% | 1.09x | STRONG 84/100 | HIGH 62/100 | Watch |
| 7 | XDG/USD ⭐ | 0.0568111 | 77.01 | +0.32% | 3.04x | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 8 | VVV/USD | 30.148 | 69.78 | -0.08% | 0.65x | WEAK 40/100 | VERY_HIGH 76/100 | Watch |
| 9 | ZEC/USD | 780.73 | 68.92 | +0.34% | 1.46x | STRONG 79/100 | HIGH 55/100 | Watch |
| 10 | XLM/USD | 0.129137 | 65.44 | +0.05% | 4.41x | STRONG 78/100 | HIGH 55/100 | Watch |
| 11 | SOL/USD | 71.29 | 63.83 | +0.27% | 0.92x | MODERATE 62/100 | HIGH 62/100 | Watch |
| 12 | SUI/USD | 0.6795 | 63.27 | +0.61% | 0.28x | MODERATE 62/100 | VERY_HIGH 70/100 | Watch |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | TIA/USD ⭐ | 0.3525 | 89.05 | +2.17% | 14.89x | 3585 | STRONG 100/100 | HIGH 67/100 | Consider small entry |
| 2 | PEPE/USD | 3.581e-06 | 84.23 | +0.71% | 3.47x | 7130 | STRONG 97/100 | HIGH 55/100 | Consider small entry |
| 3 | XRP/USD ⭐ | 0.95551 | 83.72 | +0.30% | 4.26x | 42391 | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 4 | LTC/USD ⭐ | 43.87 | 82.95 | +0.85% | 1.09x | 14858 | STRONG 86/100 | HIGH 62/100 | Watch |
| 5 | XDG/USD ⭐ | 0.056832 | 73.24 | +0.32% | 3.04x | 7711 | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 6 | JUP/USD | 0.23434 | 71.10 | +0.86% | 2.20x | 2493 | STRONG 86/100 | HIGH 66/100 | Consider small entry |
| 7 | NEAR/USD ⭐ | 3.0991 | 69.95 | +0.32% | 2.50x | 19168 | STRONG 100/100 | HIGH 55/100 | Consider small entry |

**Same-run overlap:** TIA/USD, XRP/USD, NEAR/USD, LTC/USD, XDG/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
