# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-18T17:15:14.430366+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/44356447535
**Source SHA:** b271b90a2cae9e5307600070ce7d0e510fe68996
**Previous ledger commit:** d9365a73cc76f81bf159775770f11971996d3432 (atomic ledger/results publication)
**Ledger generation:** 621 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 4s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 627; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 609; valid market observations: 609; OHLC screened: 11.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | SENT/USD | 0.019626 | 58.623 | 63.111 | +5.13% | -0.60% | 0.85x | 7.6 | 2026-11-18T17:15:10.265517+00:00 | Not calibrated | WEAK 34/100 | VERY_HIGH 80/100 | Do nothing | WATCH |
| 2 | TRUST/USD | 0.04915 | 56.813 | 49.701 | +4.24% | -0.28% | 1.85x | 24.5 | 2026-11-18T17:15:10.265517+00:00 | Not calibrated | WEAK 38/100 | VERY_HIGH 78/100 | Watch | WATCH |
| 3 | MNT/USD | 0.3857 | 45.973 | 48.596 | +3.32% | +0.44% | 0.52x | 13.0 | 2026-11-18T17:15:10.265517+00:00 | Not calibrated | MODERATE 48/100 | VERY_HIGH 81/100 | Watch | WATCH |
| 4 | MEGA/USD | 0.05317 | 42.696 | 40.574 | +2.96% | +0.40% | 1.01x | 22.6 | 2026-11-18T17:15:10.265517+00:00 | Not calibrated | MODERATE 46/100 | EXTREME 86/100 | Do nothing | WATCH |
| 5 | CC/USD | 0.08251 | 37.522 | 35.163 | +0.46% | +0.27% | 1.10x | 7.3 | 2026-11-18T17:15:10.265517+00:00 | Not calibrated | MODERATE 54/100 | HIGH 67/100 | Watch | WATCH |
| 6 | INFI/USD | 0.1303 | 21.466 | 45.637 | +2.60% | -3.34% | 0.25x | 7.7 | 2026-11-18T17:15:10.265517+00:00 | Not calibrated | WEAK 16/100 | EXTREME 92/100 | Do nothing | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | SENT/USD | 63.111 | 0.019626 | -0.60% | 0.85x |
| 2 | TRUST/USD | 49.701 | 0.04915 | -0.28% | 1.85x |
| 3 | MNT/USD | 48.596 | 0.3857 | +0.44% | 0.52x |
| 4 | INFI/USD | 45.637 | 0.1303 | -3.34% | 0.25x |
| 5 | MEGA/USD | 40.574 | 0.05317 | +0.40% | 1.01x |
| 6 | CC/USD | 35.163 | 0.08251 | +0.27% | 1.10x |

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

- Persisted scans: 621; predictions: 5298; observations: 375196.
- Matured sampled outcomes across 1/6/24/48h: 4580; gap abstentions: 13125. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 0 (sampled only; not a success-rate estimate).
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

**Writer:** 44356447535 · **Generation:** 621 · **Legacy run:** 44356447535
**Main quote time:** 2026-11-18T17:15:14.430366+00:00 · **Legacy report time:** 2026-11-18T17:15:41.008162+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | SENT/USD | 0.019626 | 58.62 | -0.60% | 0.85x | WEAK 34/100 | VERY_HIGH 80/100 | Do nothing |
| 2 | TRUST/USD | 0.04915 | 56.81 | -0.28% | 1.85x | WEAK 38/100 | VERY_HIGH 78/100 | Watch |
| 3 | MNT/USD | 0.3857 | 45.97 | +0.44% | 0.52x | MODERATE 48/100 | VERY_HIGH 81/100 | Watch |
| 4 | MEGA/USD ⭐ | 0.05317 | 42.70 | +0.40% | 1.01x | MODERATE 56/100 | EXTREME 86/100 | Do nothing |
| 5 | CC/USD ⭐ | 0.08251 | 37.52 | +0.27% | 1.10x | MODERATE 64/100 | HIGH 67/100 | Watch |
| 6 | INFI/USD | 0.1303 | 21.47 | -3.34% | 0.25x | WEAK 16/100 | EXTREME 92/100 | Do nothing |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | MEGA/USD ⭐ | 0.05317 | 47.40 | +0.40% | 1.01x | 1191 | MODERATE 59/100 | EXTREME 86/100 | Do nothing |
| 2 | AKE/USD | 0.01003127 | 36.44 | +1.58% | 1.48x | 2864 | MODERATE 53/100 | VERY_HIGH 72/100 | Watch |
| 3 | CC/USD ⭐ | 0.08243 | 33.80 | +0.27% | 1.10x | 4961 | MODERATE 62/100 | HIGH 67/100 | Watch |

**Same-run overlap:** MEGA/USD, CC/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
