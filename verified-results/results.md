# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-18T04:15:17.334286+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/44235950004
**Source SHA:** 394c17eeb7071fba40e02dbbb1ea97cedb3a0a8a
**Previous ledger commit:** 03bb5676c1dc7079a408f69a4a46d1398396f129 (atomic ledger/results publication)
**Ledger generation:** 528 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 6s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 627; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 609; valid market observations: 609; OHLC screened: 16.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | CC/USD | 0.08412 | 58.518 | 49.480 | +2.42% | +0.07% | 1.87x | 5.9 | 2026-11-18T04:15:11.556235+00:00 | Not calibrated | MODERATE 64/100 | HIGH 60/100 | Watch | WATCH |
| 2 | SENT/USD | 0.019101 | 56.590 | 42.663 | +2.31% | +0.07% | 2.36x | 8.9 | 2026-11-18T04:15:11.556235+00:00 | Not calibrated | STRONG 73/100 | HIGH 67/100 | Watch | WATCH |
| 3 | ICNT/USD | 0.2847 | 48.255 | 41.841 | +3.11% | +1.90% | 0.69x | 24.6 | 2026-11-18T04:15:11.556235+00:00 | Not calibrated | WEAK 44/100 | EXTREME 87/100 | Do nothing | WATCH |
| 4 | NIGHT/USD | 0.04501 | 45.696 | 44.015 | +0.27% | -0.16% | 1.25x | 8.9 | 2026-11-18T04:15:11.556235+00:00 | Not calibrated | WEAK 33/100 | HIGH 68/100 | Do nothing | WATCH |
| 5 | PEARL/USD | 1.8359 | 42.992 | 37.840 | +1.40% | +0.04% | 1.49x | 14.2 | 2026-11-18T04:15:11.556235+00:00 | Not calibrated | MODERATE 51/100 | HIGH 66/100 | Watch | WATCH |
| 6 | ZAMA/USD | 0.06119 | 40.101 | 43.159 | +2.10% | +0.36% | 0.51x | 9.8 | 2026-11-18T04:15:11.556235+00:00 | Not calibrated | MODERATE 50/100 | VERY_HIGH 75/100 | Watch | WATCH |
| 7 | XDC/USD | 0.03079 | 38.452 | 43.362 | +1.55% | +0.59% | 0.21x | 9.8 | 2026-11-18T04:15:11.556235+00:00 | Not calibrated | MODERATE 49/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 8 | MELANIA/USD | 0.051 | 36.178 | 44.177 | +4.72% | -0.39% | 0.40x | 39.2 | 2026-11-18T04:15:11.556235+00:00 | Not calibrated | WEAK 8/100 | EXTREME 100/100 | Do nothing | WATCH |
| 9 | AKT/USD | 0.5159 | 26.177 | 35.608 | +1.30% | -0.39% | 0.25x | 11.6 | 2026-11-18T04:15:11.556235+00:00 | Not calibrated | WEAK 13/100 | EXTREME 87/100 | Do nothing | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | CC/USD | 49.480 | 0.08412 | +0.07% | 1.87x |
| 2 | MELANIA/USD | 44.177 | 0.051 | -0.39% | 0.40x |
| 3 | NIGHT/USD | 44.015 | 0.04501 | -0.16% | 1.25x |
| 4 | XDC/USD | 43.362 | 0.03079 | +0.59% | 0.21x |
| 5 | ZAMA/USD | 43.159 | 0.06119 | +0.36% | 0.51x |
| 6 | SENT/USD | 42.663 | 0.019101 | +0.07% | 2.36x |
| 7 | ICNT/USD | 41.841 | 0.2847 | +1.90% | 0.69x |
| 8 | PEARL/USD | 37.840 | 1.8359 | +0.04% | 1.49x |
| 9 | AKT/USD | 35.608 | 0.5159 | -0.39% | 0.25x |

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

- Persisted scans: 528; predictions: 4464; observations: 318559.
- Matured sampled outcomes across 1/6/24/48h: 3558; gap abstentions: 12463. Per-horizon counts require independent audit; do not infer held-out lift.
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

**Writer:** 44235950004 · **Generation:** 528 · **Legacy run:** 44235950004
**Main quote time:** 2026-11-18T04:15:17.334286+00:00 · **Legacy report time:** 2026-11-18T04:15:33.070880+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | CC/USD ⭐ | 0.08412 | 58.52 | +0.07% | 1.87x | STRONG 74/100 | HIGH 60/100 | Watch |
| 2 | SENT/USD ⭐ | 0.019101 | 56.59 | +0.07% | 2.36x | STRONG 83/100 | HIGH 67/100 | Watch |
| 3 | ICNT/USD | 0.2847 | 48.25 | +1.90% | 0.69x | WEAK 44/100 | EXTREME 87/100 | Do nothing |
| 4 | NIGHT/USD | 0.04501 | 45.70 | -0.16% | 1.25x | WEAK 33/100 | HIGH 68/100 | Do nothing |
| 5 | PEARL/USD | 1.8359 | 42.99 | +0.04% | 1.49x | MODERATE 51/100 | HIGH 66/100 | Watch |
| 6 | ZAMA/USD | 0.06119 | 40.10 | +0.36% | 0.51x | MODERATE 50/100 | VERY_HIGH 75/100 | Watch |
| 7 | XDC/USD | 0.03079 | 38.45 | +0.59% | 0.21x | MODERATE 49/100 | VERY_HIGH 70/100 | Watch |
| 8 | MELANIA/USD | 0.051 | 36.18 | -0.39% | 0.40x | WEAK 8/100 | EXTREME 100/100 | Do nothing |
| 9 | AKT/USD | 0.5159 | 26.18 | -0.39% | 0.25x | WEAK 13/100 | EXTREME 87/100 | Do nothing |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | CC/USD ⭐ | 0.08412 | 61.18 | +0.07% | 1.87x | 4161 | STRONG 76/100 | HIGH 60/100 | Watch |
| 2 | SENT/USD ⭐ | 0.019097 | 55.70 | +0.07% | 2.36x | 3945 | STRONG 83/100 | HIGH 67/100 | Watch |

**Same-run overlap:** CC/USD, SENT/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
