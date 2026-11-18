# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-18T16:05:23.413108+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/44342960326
**Source SHA:** b271b90a2cae9e5307600070ce7d0e510fe68996
**Previous ledger commit:** e645f53cda938b19508a87c771bc9564430572db (atomic ledger/results publication)
**Ledger generation:** 608 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 5s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 627; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 609; valid market observations: 609; OHLC screened: 14.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | SENT/USD | 0.019529 | 57.776 | 56.631 | +4.61% | -0.03% | 1.13x | 13.3 | 2026-11-18T16:05:18.512210+00:00 | Not calibrated | WEAK 34/100 | EXTREME 86/100 | Do nothing | WATCH |
| 2 | CT/USD | 0.1186 | 55.075 | 57.390 | +4.96% | +0.42% | 0.56x | 16.9 | 2026-11-18T16:05:18.512210+00:00 | Not calibrated | MODERATE 53/100 | EXTREME 88/100 | Do nothing | WATCH |
| 3 | PROS/USD | 0.5766 | 53.968 | 56.913 | +11.55% | -0.14% | 0.78x | 38.0 | 2026-11-18T16:05:18.512210+00:00 | Not calibrated | WEAK 17/100 | EXTREME 92/100 | Do nothing | WATCH |
| 4 | ZAMA/USD | 0.06072 | 52.545 | 35.892 | +1.32% | +0.33% | 6.02x | 9.9 | 2026-11-18T16:05:18.512210+00:00 | Not calibrated | STRONG 81/100 | HIGH 67/100 | Watch | WATCH |
| 5 | MNT/USD | 0.3839 | 51.377 | 48.879 | +2.84% | +0.31% | 1.09x | 7.8 | 2026-11-18T16:05:18.512210+00:00 | Not calibrated | MODERATE 61/100 | HIGH 67/100 | Watch | WATCH |
| 6 | AKE/USD | 0.01044896 | 50.281 | 58.991 | +4.65% | -0.61% | 0.43x | 14.2 | 2026-11-18T16:05:18.512210+00:00 | Not calibrated | WEAK 25/100 | EXTREME 87/100 | Do nothing | WATCH |
| 7 | TRUST/USD | 0.04925 | 48.074 | 54.451 | +4.45% | +0.04% | 0.34x | 18.3 | 2026-11-18T16:05:18.512210+00:00 | Not calibrated | WEAK 39/100 | VERY_HIGH 81/100 | Watch | WATCH |
| 8 | FLR/USD | 0.00516 | 39.735 | 28.380 | +0.98% | +0.19% | 2.04x | 19.4 | 2026-11-18T16:05:18.512210+00:00 | Not calibrated | MODERATE 60/100 | VERY_HIGH 73/100 | Watch | WATCH |
| 9 | TRX/USD | 0.309147 | 34.461 | 42.622 | +0.40% | -0.01% | 0.19x | 1.7 | 2026-11-18T16:05:18.512210+00:00 | Not calibrated | WEAK 22/100 | VERY_HIGH 76/100 | Do nothing | WATCH |
| 10 | MEGA/USD | 0.05262 | 26.502 | 33.968 | +1.90% | +0.32% | 0.09x | 20.9 | 2026-11-18T16:05:18.512210+00:00 | Not calibrated | WEAK 33/100 | EXTREME 94/100 | Do nothing | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | AKE/USD | 58.991 | 0.01044896 | -0.61% | 0.43x |
| 2 | CT/USD | 57.390 | 0.1186 | +0.42% | 0.56x |
| 3 | PROS/USD | 56.913 | 0.5766 | -0.14% | 0.78x |
| 4 | SENT/USD | 56.631 | 0.019529 | -0.03% | 1.13x |
| 5 | TRUST/USD | 54.451 | 0.04925 | +0.04% | 0.34x |
| 6 | MNT/USD | 48.879 | 0.3839 | +0.31% | 1.09x |
| 7 | TRX/USD | 42.622 | 0.309147 | -0.01% | 0.19x |
| 8 | ZAMA/USD | 35.892 | 0.06072 | +0.33% | 6.02x |
| 9 | MEGA/USD | 33.968 | 0.05262 | +0.32% | 0.09x |
| 10 | FLR/USD | 28.380 | 0.00516 | +0.19% | 2.04x |

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

- Persisted scans: 608; predictions: 5219; observations: 367279.
- Matured sampled outcomes across 1/6/24/48h: 4438; gap abstentions: 13125. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 0 (sampled only; not a success-rate estimate).
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

**Writer:** 44342960326 · **Generation:** 608 · **Legacy run:** 44342960326
**Main quote time:** 2026-11-18T16:05:23.413108+00:00 · **Legacy report time:** 2026-11-18T16:05:53.728059+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | SENT/USD | 0.019529 | 57.78 | -0.03% | 1.13x | WEAK 34/100 | EXTREME 86/100 | Do nothing |
| 2 | CT/USD | 0.1186 | 55.07 | +0.42% | 0.56x | MODERATE 53/100 | EXTREME 88/100 | Do nothing |
| 3 | PROS/USD | 0.5766 | 53.97 | -0.14% | 0.78x | WEAK 17/100 | EXTREME 92/100 | Do nothing |
| 4 | ZAMA/USD ⭐ | 0.06072 | 52.55 | +0.33% | 6.02x | STRONG 91/100 | HIGH 67/100 | Consider small entry |
| 5 | MNT/USD ⭐ | 0.3839 | 51.38 | +0.31% | 1.09x | STRONG 71/100 | HIGH 67/100 | Watch |
| 6 | AKE/USD | 0.01044896 | 50.28 | -0.61% | 0.43x | WEAK 25/100 | EXTREME 87/100 | Do nothing |
| 7 | TRUST/USD | 0.04925 | 48.07 | +0.04% | 0.34x | WEAK 39/100 | VERY_HIGH 81/100 | Watch |
| 8 | FLR/USD ⭐ | 0.00516 | 39.73 | +0.19% | 2.04x | STRONG 70/100 | VERY_HIGH 73/100 | Watch |
| 9 | TRX/USD | 0.309147 | 34.46 | -0.01% | 0.19x | WEAK 22/100 | VERY_HIGH 76/100 | Do nothing |
| 10 | MEGA/USD | 0.05262 | 26.50 | +0.32% | 0.09x | WEAK 33/100 | EXTREME 94/100 | Do nothing |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | MNT/USD ⭐ | 0.3839 | 53.73 | +0.31% | 1.09x | 1992 | MODERATE 67/100 | VERY_HIGH 73/100 | Watch |
| 2 | ZAMA/USD ⭐ | 0.06072 | 49.60 | +0.33% | 6.02x | 3474 | STRONG 90/100 | HIGH 67/100 | Consider small entry |
| 3 | FLR/USD ⭐ | 0.00516 | 26.55 | +0.19% | 2.04x | 1120 | MODERATE 63/100 | VERY_HIGH 73/100 | Watch |

**Same-run overlap:** ZAMA/USD, MNT/USD, FLR/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
