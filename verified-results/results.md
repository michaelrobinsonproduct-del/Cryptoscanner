# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-18T07:20:12.885727+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/44257988549
**Source SHA:** 394c17eeb7071fba40e02dbbb1ea97cedb3a0a8a
**Previous ledger commit:** 2e7215b954d7f0f2dc2b5a44beba398034eeeaa8 (atomic ledger/results publication)
**Ledger generation:** 565 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 8s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 627; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 609; valid market observations: 609; OHLC screened: 23.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | ICNT/USD | 0.2955 | 80.142 | 68.837 | +7.03% | -0.74% | 2.68x | 20.3 | 2026-11-18T07:20:05.332139+00:00 | Not calibrated | MODERATE 60/100 | VERY_HIGH 78/100 | Watch | WATCH |
| 2 | XRP/USD | 0.99162 | 78.383 | 61.022 | +0.93% | +0.47% | 6.10x | 0.9 | 2026-11-18T07:20:05.332139+00:00 | Not calibrated | STRONG 94/100 | HIGH 55/100 | Consider small entry | WATCH |
| 3 | SENT/USD | 0.019468 | 49.216 | 56.783 | +4.28% | -0.54% | 0.51x | 8.2 | 2026-11-18T07:20:05.332139+00:00 | Not calibrated | WEAK 30/100 | EXTREME 88/100 | Do nothing | WATCH |
| 4 | TRX/USD | 0.309758 | 45.026 | 44.250 | +0.60% | +0.19% | 0.98x | 1.2 | 2026-11-18T07:20:05.332139+00:00 | Not calibrated | WEAK 43/100 | HIGH 62/100 | Watch | WATCH |
| 5 | AKE/USD | 0.01022668 | 39.760 | 42.610 | +2.43% | -1.44% | 1.44x | 17.9 | 2026-11-18T07:20:05.332139+00:00 | Not calibrated | WEAK 35/100 | VERY_HIGH 76/100 | Do nothing | WATCH |
| 6 | AKT/USD | 0.5177 | 37.473 | 37.185 | +1.65% | +0.54% | 0.76x | 13.6 | 2026-11-18T07:20:05.332139+00:00 | Not calibrated | WEAK 44/100 | VERY_HIGH 73/100 | Watch | WATCH |
| 7 | XDC/USD | 0.03092 | 36.090 | 45.853 | +1.98% | -0.03% | 0.04x | 12.9 | 2026-11-18T07:20:05.332139+00:00 | Not calibrated | WEAK 18/100 | VERY_HIGH 82/100 | Do nothing | WATCH |
| 8 | MNT/USD | 0.3794 | 34.503 | 36.381 | +1.63% | +0.48% | 0.57x | 15.8 | 2026-11-18T07:20:05.332139+00:00 | Not calibrated | WEAK 42/100 | VERY_HIGH 81/100 | Watch | WATCH |
| 9 | TRUST/USD | 0.04789 | 30.944 | 35.922 | +1.57% | +0.29% | 0.36x | 16.7 | 2026-11-18T07:20:05.332139+00:00 | Not calibrated | WEAK 40/100 | VERY_HIGH 81/100 | Watch | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | ICNT/USD | 68.837 | 0.2955 | -0.74% | 2.68x |
| 2 | XRP/USD | 61.022 | 0.99162 | +0.47% | 6.10x |
| 3 | SENT/USD | 56.783 | 0.019468 | -0.54% | 0.51x |
| 4 | XDC/USD | 45.853 | 0.03092 | -0.03% | 0.04x |
| 5 | TRX/USD | 44.250 | 0.309758 | +0.19% | 0.98x |
| 6 | AKE/USD | 42.610 | 0.01022668 | -1.44% | 1.44x |
| 7 | AKT/USD | 37.185 | 0.5177 | +0.54% | 0.76x |
| 8 | MNT/USD | 36.381 | 0.3794 | +0.48% | 0.57x |
| 9 | TRUST/USD | 35.922 | 0.04789 | +0.29% | 0.36x |

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

- Persisted scans: 565; predictions: 4765; observations: 341092.
- Matured sampled outcomes across 1/6/24/48h: 4110; gap abstentions: 12463. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 0 (sampled only; not a success-rate estimate).
- False positives / missed movers: NOT VERIFIED without eligible continuous outcome coverage.
- Baseline vs challenger: recorded as-of; unbiased held-out lift NOT MEASURED.
- Online Kraken /USD stablecoin-base pairs excluded: 18 (counted from this scan's online AssetPairs metadata, not inferred from price).
- Stablecoin base exclusions: BRL1, BUSD, DAI, EUR, EURC, EUROP, EURQ, EURR, EURT, FDUSD, FRAX, GUSD, PYUSD, QCAD, RLUSD, TGBP, TUSD, USD, USD1, USDC, USDD, USDE, USDG, USDQ, USDR, USDS, USDT, ZUSD.
- DEX: NOT USED; no DEX freshness gate.
- OHLC screening abstentions: 14; details in immutable scan JSON artifact.
- Storage: ledger and results published in one non-force Git commit and read back. Independent artifact recovery is NOT VERIFIED by this scan alone.
- Errors: none in successful committed scan; a failed workflow must not publish a SUCCESS report.

# Cryptoscanner — challenger and independent legacy-inspired WATCH

Paper only · risk is high or higher · 30%+ in 48h probability NOT CALIBRATED
Signal confidence 0–100 means setup strength only, NOT a win probability. Actions are research guidance; no trade authorization.

**Writer:** 44257988549 · **Generation:** 565 · **Legacy run:** 44257988549
**Main quote time:** 2026-11-18T07:20:12.885727+00:00 · **Legacy report time:** 2026-11-18T07:20:37.536497+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | ICNT/USD | 0.2955 | 80.14 | -0.74% | 2.68x | MODERATE 60/100 | VERY_HIGH 78/100 | Watch |
| 2 | XRP/USD ⭐ | 0.99162 | 78.38 | +0.47% | 6.10x | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 3 | SENT/USD | 0.019468 | 49.22 | -0.54% | 0.51x | WEAK 30/100 | EXTREME 88/100 | Do nothing |
| 4 | TRX/USD | 0.309758 | 45.03 | +0.19% | 0.98x | WEAK 43/100 | HIGH 62/100 | Watch |
| 5 | AKE/USD | 0.01022668 | 39.76 | -1.44% | 1.44x | WEAK 35/100 | VERY_HIGH 76/100 | Do nothing |
| 6 | AKT/USD | 0.5177 | 37.47 | +0.54% | 0.76x | WEAK 44/100 | VERY_HIGH 73/100 | Watch |
| 7 | XDC/USD | 0.03092 | 36.09 | -0.03% | 0.04x | WEAK 18/100 | VERY_HIGH 82/100 | Do nothing |
| 8 | MNT/USD | 0.3794 | 34.50 | +0.48% | 0.57x | WEAK 42/100 | VERY_HIGH 81/100 | Watch |
| 9 | TRUST/USD | 0.04789 | 30.94 | +0.29% | 0.36x | WEAK 40/100 | VERY_HIGH 81/100 | Watch |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | XRP/USD ⭐ | 0.99001 | 68.53 | +0.47% | 6.10x | 32269 | STRONG 99/100 | HIGH 55/100 | Consider small entry |

**Same-run overlap:** XRP/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
