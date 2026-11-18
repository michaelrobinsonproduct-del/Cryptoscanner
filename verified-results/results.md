# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-18T17:50:17.176820+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/44362940837
**Source SHA:** b271b90a2cae9e5307600070ce7d0e510fe68996
**Previous ledger commit:** c9cc132ab5ab04eacc23dcbf9129c932863046e0 (atomic ledger/results publication)
**Ledger generation:** 628 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 4s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 627; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 609; valid market observations: 609; OHLC screened: 17.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | SENT/USD | 0.019861 | 82.158 | 73.005 | +6.38% | -1.17% | 2.77x | 5.5 | 2026-11-18T17:50:12.676962+00:00 | Not calibrated | STRONG 71/100 | VERY_HIGH 77/100 | Watch | WATCH |
| 2 | TRUST/USD | 0.04995 | 71.169 | 72.840 | +5.94% | +0.00% | 0.83x | 2.0 | 2026-11-18T17:50:12.676962+00:00 | Not calibrated | MODERATE 56/100 | HIGH 67/100 | Watch | WATCH |
| 3 | MEGA/USD | 0.05391 | 59.775 | 53.545 | +4.40% | +0.17% | 1.54x | 16.7 | 2026-11-18T17:50:12.676962+00:00 | Not calibrated | MODERATE 60/100 | VERY_HIGH 73/100 | Watch | WATCH |
| 4 | NIGHT/USD | 0.04519 | 54.933 | 49.022 | +0.67% | -0.46% | 1.82x | 8.9 | 2026-11-18T17:50:12.676962+00:00 | Not calibrated | MODERATE 47/100 | HIGH 61/100 | Watch | WATCH |
| 5 | MNT/USD | 0.3821 | 52.121 | 41.788 | +2.36% | -0.93% | 2.77x | 13.1 | 2026-11-18T17:50:12.676962+00:00 | Not calibrated | MODERATE 51/100 | VERY_HIGH 72/100 | Watch | WATCH |
| 6 | CC/USD | 0.0824 | 33.319 | 34.712 | +0.33% | -1.64% | 1.68x | 6.1 | 2026-11-18T17:50:12.676962+00:00 | Not calibrated | WEAK 37/100 | VERY_HIGH 70/100 | Do nothing | WATCH |
| 7 | ZAMA/USD | 0.0607 | 25.286 | 34.742 | +1.28% | -0.26% | 0.19x | 11.6 | 2026-11-18T17:50:12.676962+00:00 | Not calibrated | WEAK 13/100 | EXTREME 94/100 | Do nothing | WATCH |
| 8 | AKT/USD | 0.5113 | 22.521 | 26.939 | +0.39% | -0.25% | 0.69x | 15.7 | 2026-11-18T17:50:12.676962+00:00 | Not calibrated | WEAK 11/100 | EXTREME 87/100 | Do nothing | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | SENT/USD | 73.005 | 0.019861 | -1.17% | 2.77x |
| 2 | TRUST/USD | 72.840 | 0.04995 | +0.00% | 0.83x |
| 3 | MEGA/USD | 53.545 | 0.05391 | +0.17% | 1.54x |
| 4 | NIGHT/USD | 49.022 | 0.04519 | -0.46% | 1.82x |
| 5 | MNT/USD | 41.788 | 0.3821 | -0.93% | 2.77x |
| 6 | ZAMA/USD | 34.742 | 0.0607 | -0.26% | 0.19x |
| 7 | CC/USD | 34.712 | 0.0824 | -1.64% | 1.68x |
| 8 | AKT/USD | 26.939 | 0.5113 | -0.25% | 0.69x |

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

- Persisted scans: 628; predictions: 5362; observations: 379459.
- Matured sampled outcomes across 1/6/24/48h: 4653; gap abstentions: 13125. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 0 (sampled only; not a success-rate estimate).
- False positives / missed movers: NOT VERIFIED without eligible continuous outcome coverage.
- Baseline vs challenger: recorded as-of; unbiased held-out lift NOT MEASURED.
- Online Kraken /USD stablecoin-base pairs excluded: 18 (counted from this scan's online AssetPairs metadata, not inferred from price).
- Stablecoin base exclusions: BRL1, BUSD, DAI, EUR, EURC, EUROP, EURQ, EURR, EURT, FDUSD, FRAX, GUSD, PYUSD, QCAD, RLUSD, TGBP, TUSD, USD, USD1, USDC, USDD, USDE, USDG, USDQ, USDR, USDS, USDT, ZUSD.
- DEX: NOT USED; no DEX freshness gate.
- OHLC screening abstentions: 9; details in immutable scan JSON artifact.
- Storage: ledger and results published in one non-force Git commit and read back. Independent artifact recovery is NOT VERIFIED by this scan alone.
- Errors: none in successful committed scan; a failed workflow must not publish a SUCCESS report.

# Cryptoscanner — challenger and independent legacy-inspired WATCH

Paper only · risk is high or higher · 30%+ in 48h probability NOT CALIBRATED
Signal confidence 0–100 means setup strength only, NOT a win probability. Actions are research guidance; no trade authorization.

**Writer:** 44362940837 · **Generation:** 628 · **Legacy run:** 44362940837
**Main quote time:** 2026-11-18T17:50:17.176820+00:00 · **Legacy report time:** 2026-11-18T17:50:40.287887+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | SENT/USD | 0.019861 | 82.16 | -1.17% | 2.77x | STRONG 71/100 | VERY_HIGH 77/100 | Watch |
| 2 | TRUST/USD | 0.04995 | 71.17 | +0.00% | 0.83x | MODERATE 56/100 | HIGH 67/100 | Watch |
| 3 | MEGA/USD ⭐ | 0.05391 | 59.77 | +0.17% | 1.54x | STRONG 70/100 | VERY_HIGH 73/100 | Watch |
| 4 | NIGHT/USD | 0.04519 | 54.93 | -0.46% | 1.82x | MODERATE 47/100 | HIGH 61/100 | Watch |
| 5 | MNT/USD | 0.3821 | 52.12 | -0.93% | 2.77x | MODERATE 51/100 | VERY_HIGH 72/100 | Watch |
| 6 | CC/USD | 0.0824 | 33.32 | -1.64% | 1.68x | WEAK 37/100 | VERY_HIGH 70/100 | Do nothing |
| 7 | ZAMA/USD | 0.0607 | 25.29 | -0.26% | 0.19x | WEAK 13/100 | EXTREME 94/100 | Do nothing |
| 8 | AKT/USD | 0.5113 | 22.52 | -0.25% | 0.69x | WEAK 11/100 | EXTREME 87/100 | Do nothing |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | MEGA/USD ⭐ | 0.05391 | 61.35 | +0.17% | 1.54x | 1200 | STRONG 71/100 | VERY_HIGH 73/100 | Watch |

**Same-run overlap:** MEGA/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
