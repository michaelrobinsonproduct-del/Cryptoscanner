# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-18T16:00:12.560630+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/44341974276
**Source SHA:** b271b90a2cae9e5307600070ce7d0e510fe68996
**Previous ledger commit:** cb407bb9b394df78e7ce4f8b77e780b49d394f29 (atomic ledger/results publication)
**Ledger generation:** 607 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 5s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 627; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 609; valid market observations: 609; OHLC screened: 14.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | SENT/USD | 0.019642 | 78.155 | 62.187 | +5.21% | +0.19% | 2.77x | 10.7 | 2026-11-18T16:00:07.256232+00:00 | Not calibrated | STRONG 79/100 | VERY_HIGH 73/100 | Watch | WATCH |
| 2 | MNT/USD | 0.3844 | 65.648 | 49.866 | +2.97% | +0.16% | 4.58x | 7.8 | 2026-11-18T16:00:07.256232+00:00 | Not calibrated | STRONG 78/100 | HIGH 60/100 | Watch | WATCH |
| 3 | CT/USD | 0.1189 | 61.187 | 59.266 | +5.22% | -1.08% | 1.73x | 16.9 | 2026-11-18T16:00:07.256232+00:00 | Not calibrated | MODERATE 46/100 | VERY_HIGH 83/100 | Watch | WATCH |
| 4 | ZAMA/USD | 0.06057 | 53.866 | 34.116 | +1.07% | +0.95% | 6.23x | 9.9 | 2026-11-18T16:00:07.256232+00:00 | Not calibrated | STRONG 82/100 | HIGH 67/100 | Watch | WATCH |
| 5 | MEGA/USD | 0.05262 | 47.160 | 33.013 | +1.90% | -0.17% | 2.80x | 22.8 | 2026-11-18T16:00:07.256232+00:00 | Not calibrated | WEAK 44/100 | EXTREME 85/100 | Do nothing | WATCH |
| 6 | AKE/USD | 0.01044396 | 44.508 | 53.052 | +4.60% | -0.33% | 0.31x | 25.4 | 2026-11-18T16:00:07.256232+00:00 | Not calibrated | WEAK 17/100 | EXTREME 93/100 | Do nothing | WATCH |
| 7 | FLR/USD | 0.00516 | 34.994 | 28.379 | +0.98% | +0.19% | 1.56x | 19.4 | 2026-11-18T16:00:07.256232+00:00 | Not calibrated | MODERATE 47/100 | VERY_HIGH 73/100 | Watch | WATCH |
| 8 | TRX/USD | 0.309145 | 34.543 | 43.147 | +0.40% | -0.11% | 0.19x | 0.8 | 2026-11-18T16:00:07.256232+00:00 | Not calibrated | WEAK 22/100 | VERY_HIGH 76/100 | Do nothing | WATCH |
| 9 | TRUST/USD | 0.04884 | 31.715 | 40.125 | +3.58% | -0.37% | 0.34x | 34.8 | 2026-11-18T16:00:07.256232+00:00 | Not calibrated | WEAK 11/100 | EXTREME 93/100 | Do nothing | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | SENT/USD | 62.187 | 0.019642 | +0.19% | 2.77x |
| 2 | CT/USD | 59.266 | 0.1189 | -1.08% | 1.73x |
| 3 | AKE/USD | 53.052 | 0.01044396 | -0.33% | 0.31x |
| 4 | MNT/USD | 49.866 | 0.3844 | +0.16% | 4.58x |
| 5 | TRX/USD | 43.147 | 0.309145 | -0.11% | 0.19x |
| 6 | TRUST/USD | 40.125 | 0.04884 | -0.37% | 0.34x |
| 7 | ZAMA/USD | 34.116 | 0.06057 | +0.95% | 6.23x |
| 8 | MEGA/USD | 33.013 | 0.05262 | -0.17% | 2.80x |
| 9 | FLR/USD | 28.379 | 0.00516 | +0.19% | 1.56x |

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

- Persisted scans: 607; predictions: 5209; observations: 366670.
- Matured sampled outcomes across 1/6/24/48h: 4418; gap abstentions: 13125. Per-horizon counts require independent audit; do not infer held-out lift.
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

**Writer:** 44341974276 · **Generation:** 607 · **Legacy run:** 44341974276
**Main quote time:** 2026-11-18T16:00:12.560630+00:00 · **Legacy report time:** 2026-11-18T16:00:42.626830+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | SENT/USD ⭐ | 0.019642 | 78.15 | +0.19% | 2.77x | STRONG 89/100 | VERY_HIGH 73/100 | Watch |
| 2 | MNT/USD ⭐ | 0.3844 | 65.65 | +0.16% | 4.58x | STRONG 88/100 | HIGH 60/100 | Watch |
| 3 | CT/USD | 0.1189 | 61.19 | -1.08% | 1.73x | MODERATE 46/100 | VERY_HIGH 83/100 | Watch |
| 4 | ZAMA/USD ⭐ | 0.06057 | 53.87 | +0.95% | 6.23x | STRONG 92/100 | HIGH 67/100 | Consider small entry |
| 5 | MEGA/USD | 0.05262 | 47.16 | -0.17% | 2.80x | WEAK 44/100 | EXTREME 85/100 | Do nothing |
| 6 | AKE/USD | 0.01044396 | 44.51 | -0.33% | 0.31x | WEAK 17/100 | EXTREME 93/100 | Do nothing |
| 7 | FLR/USD | 0.00516 | 34.99 | +0.19% | 1.56x | MODERATE 47/100 | VERY_HIGH 73/100 | Watch |
| 8 | TRX/USD | 0.309145 | 34.54 | -0.11% | 0.19x | WEAK 22/100 | VERY_HIGH 76/100 | Do nothing |
| 9 | TRUST/USD | 0.04884 | 31.71 | -0.37% | 0.34x | WEAK 11/100 | EXTREME 93/100 | Do nothing |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | SENT/USD ⭐ | 0.019655 | 78.31 | +0.19% | 2.77x | 5873 | STRONG 89/100 | VERY_HIGH 73/100 | Watch |
| 2 | PROS/USD | 0.5826 | 67.88 | +2.18% | 1.16x | 1455 | MODERATE 59/100 | EXTREME 86/100 | Do nothing |
| 3 | MNT/USD ⭐ | 0.3843 | 62.26 | +0.16% | 4.58x | 1999 | STRONG 86/100 | HIGH 60/100 | Watch |
| 4 | ZAMA/USD ⭐ | 0.06057 | 46.62 | +0.95% | 6.23x | 3476 | STRONG 83/100 | VERY_HIGH 73/100 | Watch |
| 5 | CC/USD | 0.08226 | 28.08 | +0.10% | 1.04x | 4866 | WEAK 39/100 | HIGH 67/100 | Watch |

**Same-run overlap:** SENT/USD, MNT/USD, ZAMA/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
