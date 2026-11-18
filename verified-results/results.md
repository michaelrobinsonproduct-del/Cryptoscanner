# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-18T05:40:07.070061+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/44245771932
**Source SHA:** 394c17eeb7071fba40e02dbbb1ea97cedb3a0a8a
**Previous ledger commit:** cd76508ea66b65ebd0b30db2049bccf9e806b72e (atomic ledger/results publication)
**Ledger generation:** 545 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 6s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 627; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 609; valid market observations: 609; OHLC screened: 22.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | NEAR/USD | 3.4054 | 75.377 | 56.739 | +0.37% | +0.73% | 17.17x | 1.8 | 2026-11-18T05:40:00.697896+00:00 | Not calibrated | STRONG 93/100 | HIGH 55/100 | Consider small entry | WATCH |
| 2 | XRP/USD | 0.98675 | 73.347 | 57.550 | +0.43% | +0.16% | 3.71x | 0.9 | 2026-11-18T05:40:00.697896+00:00 | Not calibrated | STRONG 82/100 | HIGH 55/100 | Watch | WATCH |
| 3 | SENT/USD | 0.01987 | 72.103 | 71.966 | +6.43% | +0.88% | 0.57x | 8.1 | 2026-11-18T05:40:00.697896+00:00 | Not calibrated | MODERATE 66/100 | VERY_HIGH 82/100 | Watch | WATCH |
| 4 | CC/USD | 0.08434 | 48.245 | 52.034 | +2.69% | +0.34% | 0.45x | 4.7 | 2026-11-18T05:40:00.697896+00:00 | Not calibrated | MODERATE 54/100 | VERY_HIGH 75/100 | Watch | WATCH |
| 5 | UP/USD | 0.05504 | 46.944 | 53.003 | +3.87% | -0.60% | 0.69x | 12.7 | 2026-11-18T05:40:00.697896+00:00 | Not calibrated | WEAK 23/100 | EXTREME 87/100 | Do nothing | WATCH |
| 6 | XDC/USD | 0.03101 | 46.471 | 49.083 | +2.28% | +0.68% | 0.40x | 9.7 | 2026-11-18T05:40:00.697896+00:00 | Not calibrated | MODERATE 53/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 7 | MNT/USD | 0.3779 | 33.561 | 37.514 | +1.23% | +0.59% | 0.31x | 7.9 | 2026-11-18T05:40:00.697896+00:00 | Not calibrated | MODERATE 47/100 | VERY_HIGH 75/100 | Watch | WATCH |
| 8 | PEARL/USD | 1.8449 | 32.480 | 38.036 | +1.90% | +0.36% | 0.26x | 20.1 | 2026-11-18T05:40:00.697896+00:00 | Not calibrated | WEAK 36/100 | EXTREME 87/100 | Do nothing | WATCH |
| 9 | MELANIA/USD | 0.0497 | 20.648 | 25.064 | +2.05% | +0.20% | 0.46x | 40.2 | 2026-11-18T05:40:00.697896+00:00 | Not calibrated | WEAK 25/100 | EXTREME 100/100 | Do nothing | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | SENT/USD | 71.966 | 0.01987 | +0.88% | 0.57x |
| 2 | XRP/USD | 57.550 | 0.98675 | +0.16% | 3.71x |
| 3 | NEAR/USD | 56.739 | 3.4054 | +0.73% | 17.17x |
| 4 | UP/USD | 53.003 | 0.05504 | -0.60% | 0.69x |
| 5 | CC/USD | 52.034 | 0.08434 | +0.34% | 0.45x |
| 6 | XDC/USD | 49.083 | 0.03101 | +0.68% | 0.40x |
| 7 | PEARL/USD | 38.036 | 1.8449 | +0.36% | 0.26x |
| 8 | MNT/USD | 37.514 | 0.3779 | +0.59% | 0.31x |
| 9 | MELANIA/USD | 25.064 | 0.0497 | +0.20% | 0.46x |

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

- Persisted scans: 545; predictions: 4604; observations: 328912.
- Matured sampled outcomes across 1/6/24/48h: 3746; gap abstentions: 12463. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 0 (sampled only; not a success-rate estimate).
- False positives / missed movers: NOT VERIFIED without eligible continuous outcome coverage.
- Baseline vs challenger: recorded as-of; unbiased held-out lift NOT MEASURED.
- Online Kraken /USD stablecoin-base pairs excluded: 18 (counted from this scan's online AssetPairs metadata, not inferred from price).
- Stablecoin base exclusions: BRL1, BUSD, DAI, EUR, EURC, EUROP, EURQ, EURR, EURT, FDUSD, FRAX, GUSD, PYUSD, QCAD, RLUSD, TGBP, TUSD, USD, USD1, USDC, USDD, USDE, USDG, USDQ, USDR, USDS, USDT, ZUSD.
- DEX: NOT USED; no DEX freshness gate.
- OHLC screening abstentions: 13; details in immutable scan JSON artifact.
- Storage: ledger and results published in one non-force Git commit and read back. Independent artifact recovery is NOT VERIFIED by this scan alone.
- Errors: none in successful committed scan; a failed workflow must not publish a SUCCESS report.

# Cryptoscanner — challenger and independent legacy-inspired WATCH

Paper only · risk is high or higher · 30%+ in 48h probability NOT CALIBRATED
Signal confidence 0–100 means setup strength only, NOT a win probability. Actions are research guidance; no trade authorization.

**Writer:** 44245771932 · **Generation:** 545 · **Legacy run:** 44245771932
**Main quote time:** 2026-11-18T05:40:07.070061+00:00 · **Legacy report time:** 2026-11-18T05:40:26.188680+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | NEAR/USD ⭐ | 3.4054 | 75.38 | +0.73% | 17.17x | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 2 | XRP/USD ⭐ | 0.98675 | 73.35 | +0.16% | 3.71x | STRONG 92/100 | HIGH 55/100 | Watch |
| 3 | SENT/USD | 0.01987 | 72.10 | +0.88% | 0.57x | MODERATE 66/100 | VERY_HIGH 82/100 | Watch |
| 4 | CC/USD | 0.08434 | 48.24 | +0.34% | 0.45x | MODERATE 54/100 | VERY_HIGH 75/100 | Watch |
| 5 | UP/USD | 0.05504 | 46.94 | -0.60% | 0.69x | WEAK 23/100 | EXTREME 87/100 | Do nothing |
| 6 | XDC/USD | 0.03101 | 46.47 | +0.68% | 0.40x | MODERATE 53/100 | VERY_HIGH 70/100 | Watch |
| 7 | MNT/USD | 0.3779 | 33.56 | +0.59% | 0.31x | MODERATE 47/100 | VERY_HIGH 75/100 | Watch |
| 8 | PEARL/USD | 1.8449 | 32.48 | +0.36% | 0.26x | WEAK 36/100 | EXTREME 87/100 | Do nothing |
| 9 | MELANIA/USD | 0.0497 | 20.65 | +0.20% | 0.46x | WEAK 25/100 | EXTREME 100/100 | Do nothing |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | XRP/USD ⭐ | 0.98744 | 64.85 | +0.16% | 3.71x | 32120 | STRONG 87/100 | HIGH 55/100 | Watch |
| 2 | NEAR/USD ⭐ | 3.4085 | 63.66 | +0.73% | 17.17x | 16127 | STRONG 97/100 | HIGH 55/100 | Consider small entry |
| 3 | QNT/USD | 156.15 | 48.02 | +0.79% | 9.68x | 4861 | STRONG 79/100 | HIGH 55/100 | Watch |

**Same-run overlap:** NEAR/USD, XRP/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
