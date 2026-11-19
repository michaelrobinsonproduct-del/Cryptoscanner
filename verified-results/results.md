# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-19T02:00:26.123878+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/44440988898
**Source SHA:** b271b90a2cae9e5307600070ce7d0e510fe68996
**Previous ledger commit:** 5b85b17cfa6b9ce8cb57ad2af9ef78b3c280ed55 (atomic ledger/results publication)
**Ledger generation:** 725 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 8s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 627; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 609; valid market observations: 609; OHLC screened: 24.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | CFG/USD | 0.0705 | 76.858 | 68.683 | +9.47% | +2.47% | 0.58x | 14.2 | 2026-11-19T02:00:17.737158+00:00 | Not calibrated | MODERATE 63/100 | EXTREME 88/100 | Do nothing | WATCH |
| 2 | SENT/USD | 0.021739 | 62.549 | 68.408 | +5.50% | +0.04% | 0.39x | 3.2 | 2026-11-19T02:00:17.737158+00:00 | Not calibrated | MODERATE 51/100 | VERY_HIGH 82/100 | Watch | WATCH |
| 3 | LUNA/USD | 4.544e-05 | 60.956 | 61.572 | +4.36% | +1.14% | 0.37x | 2.2 | 2026-11-19T02:00:17.737158+00:00 | Not calibrated | MODERATE 60/100 | VERY_HIGH 75/100 | Watch | WATCH |
| 4 | TRX/USD | 0.310211 | 56.465 | 41.580 | +0.30% | -0.02% | 10.52x | 1.1 | 2026-11-19T02:00:17.737158+00:00 | Not calibrated | MODERATE 58/100 | HIGH 61/100 | Watch | WATCH |
| 5 | DRV/USD | 0.26641 | 48.152 | 32.777 | +0.65% | +0.08% | 3.77x | 10.1 | 2026-11-19T02:00:17.737158+00:00 | Not calibrated | MODERATE 64/100 | HIGH 66/100 | Watch | WATCH |
| 6 | FIL/USD | 0.569 | 38.959 | 25.658 | +0.35% | +0.18% | 2.24x | 17.6 | 2026-11-19T02:00:17.737158+00:00 | Not calibrated | MODERATE 59/100 | HIGH 66/100 | Watch | WATCH |
| 7 | MEGA/USD | 0.05768 | 38.315 | 40.931 | +3.00% | +0.26% | 0.61x | 22.6 | 2026-11-19T02:00:17.737158+00:00 | Not calibrated | WEAK 39/100 | EXTREME 94/100 | Do nothing | WATCH |
| 8 | PAXG/USD | 3745.57 | 34.671 | 43.827 | +0.39% | +0.04% | 0.06x | 2.3 | 2026-11-19T02:00:17.737158+00:00 | Not calibrated | WEAK 37/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 9 | BONK/USD | 2.348e-06 | 27.595 | 27.893 | +0.34% | -0.04% | 0.99x | 12.8 | 2026-11-19T02:00:17.737158+00:00 | Not calibrated | WEAK 14/100 | VERY_HIGH 79/100 | Do nothing | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | CFG/USD | 68.683 | 0.0705 | +2.47% | 0.58x |
| 2 | SENT/USD | 68.408 | 0.021739 | +0.04% | 0.39x |
| 3 | LUNA/USD | 61.572 | 4.544e-05 | +1.14% | 0.37x |
| 4 | PAXG/USD | 43.827 | 3745.57 | +0.04% | 0.06x |
| 5 | TRX/USD | 41.580 | 0.310211 | -0.02% | 10.52x |
| 6 | MEGA/USD | 40.931 | 0.05768 | +0.26% | 0.61x |
| 7 | DRV/USD | 32.777 | 0.26641 | +0.08% | 3.77x |
| 8 | BONK/USD | 27.893 | 2.348e-06 | -0.04% | 0.99x |
| 9 | FIL/USD | 25.658 | 0.569 | +0.18% | 2.24x |

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

- Persisted scans: 725; predictions: 5880; observations: 438532.
- Matured sampled outcomes across 1/6/24/48h: 5808; gap abstentions: 13469. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 10 (sampled only; not a success-rate estimate).
- False positives / missed movers: NOT VERIFIED without eligible continuous outcome coverage.
- Baseline vs challenger: recorded as-of; unbiased held-out lift NOT MEASURED.
- Online Kraken /USD stablecoin-base pairs excluded: 18 (counted from this scan's online AssetPairs metadata, not inferred from price).
- Stablecoin base exclusions: BRL1, BUSD, DAI, EUR, EURC, EUROP, EURQ, EURR, EURT, FDUSD, FRAX, GUSD, PYUSD, QCAD, RLUSD, TGBP, TUSD, USD, USD1, USDC, USDD, USDE, USDG, USDQ, USDR, USDS, USDT, ZUSD.
- DEX: NOT USED; no DEX freshness gate.
- OHLC screening abstentions: 15; details in immutable scan JSON artifact.
- Storage: ledger and results published in one non-force Git commit and read back. Independent artifact recovery is NOT VERIFIED by this scan alone.
- Errors: none in successful committed scan; a failed workflow must not publish a SUCCESS report.

# Cryptoscanner — challenger and independent legacy-inspired WATCH

Paper only · risk is high or higher · 30%+ in 48h probability NOT CALIBRATED
Signal confidence 0–100 means setup strength only, NOT a win probability. Actions are research guidance; no trade authorization.

**Writer:** 44440988898 · **Generation:** 725 · **Legacy run:** 44440988898
**Main quote time:** 2026-11-19T02:00:26.123878+00:00 · **Legacy report time:** 2026-11-19T02:01:41.513999+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | CFG/USD | 0.0705 | 76.86 | +2.47% | 0.58x | MODERATE 63/100 | EXTREME 88/100 | Do nothing |
| 2 | SENT/USD | 0.021739 | 62.55 | +0.04% | 0.39x | MODERATE 51/100 | VERY_HIGH 82/100 | Watch |
| 3 | LUNA/USD | 4.544e-05 | 60.96 | +1.14% | 0.37x | MODERATE 60/100 | VERY_HIGH 75/100 | Watch |
| 4 | TRX/USD | 0.310211 | 56.47 | -0.02% | 10.52x | MODERATE 58/100 | HIGH 61/100 | Watch |
| 5 | DRV/USD | 0.26641 | 48.15 | +0.08% | 3.77x | MODERATE 64/100 | HIGH 66/100 | Watch |
| 6 | FIL/USD | 0.569 | 38.96 | +0.18% | 2.24x | MODERATE 59/100 | HIGH 66/100 | Watch |
| 7 | MEGA/USD | 0.05768 | 38.31 | +0.26% | 0.61x | WEAK 39/100 | EXTREME 94/100 | Do nothing |
| 8 | PAXG/USD | 3745.57 | 34.67 | +0.04% | 0.06x | WEAK 37/100 | VERY_HIGH 70/100 | Watch |
| 9 | BONK/USD | 2.348e-06 | 27.60 | -0.04% | 0.99x | WEAK 14/100 | VERY_HIGH 79/100 | Do nothing |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | LIGHTER/USD | 2.736 | 45.45 | +0.77% | 10.94x | 3844 | STRONG 73/100 | HIGH 66/100 | Watch |

**Same-run overlap:** None
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
