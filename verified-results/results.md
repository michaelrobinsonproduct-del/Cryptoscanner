# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-18T15:25:12.320272+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/44335297209
**Source SHA:** b271b90a2cae9e5307600070ce7d0e510fe68996
**Previous ledger commit:** d9498fc33b3789bea593dd1bcb7f3a1cdf3494a8 (atomic ledger/results publication)
**Ledger generation:** 600 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 7s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 627; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 609; valid market observations: 609; OHLC screened: 22.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | CT/USD | 0.1236 | 74.381 | 63.889 | +9.38% | +1.23% | 1.44x | 24.3 | 2026-11-18T15:25:04.942714+00:00 | Not calibrated | STRONG 72/100 | VERY_HIGH 79/100 | Watch | WATCH |
| 2 | SENT/USD | 0.01974 | 73.177 | 67.901 | +5.74% | +1.20% | 0.93x | 6.6 | 2026-11-18T15:25:04.942714+00:00 | Not calibrated | MODERATE 67/100 | VERY_HIGH 74/100 | Watch | WATCH |
| 3 | STABLE/USD | 0.02305 | 65.557 | 65.153 | +9.50% | -0.65% | 1.36x | 21.7 | 2026-11-18T15:25:04.942714+00:00 | Not calibrated | WEAK 43/100 | EXTREME 85/100 | Do nothing | WATCH |
| 4 | CAP/USD | 0.102264 | 53.306 | 37.454 | +1.28% | +0.17% | 4.19x | 5.7 | 2026-11-18T15:25:04.942714+00:00 | Not calibrated | STRONG 72/100 | HIGH 67/100 | Watch | WATCH |
| 5 | TRX/USD | 0.310106 | 48.853 | 46.020 | +0.72% | +0.04% | 1.26x | 0.0 | 2026-11-18T15:25:04.942714+00:00 | Not calibrated | MODERATE 49/100 | HIGH 55/100 | Watch | WATCH |
| 6 | NIGHT/USD | 0.04531 | 48.544 | 49.039 | +0.94% | +0.29% | 0.81x | 11.0 | 2026-11-18T15:25:04.942714+00:00 | Not calibrated | MODERATE 49/100 | HIGH 68/100 | Watch | WATCH |
| 7 | AKE/USD | 0.01042827 | 48.175 | 54.538 | +4.45% | -2.23% | 1.48x | 20.3 | 2026-11-18T15:25:04.942714+00:00 | Not calibrated | WEAK 34/100 | VERY_HIGH 82/100 | Do nothing | WATCH |
| 8 | MNT/USD | 0.3856 | 46.401 | 52.153 | +3.29% | +0.10% | 0.37x | 7.8 | 2026-11-18T15:25:04.942714+00:00 | Not calibrated | WEAK 43/100 | VERY_HIGH 75/100 | Watch | WATCH |
| 9 | RE/USD | 0.23881 | 36.615 | 41.143 | +2.78% | +0.34% | 0.38x | 18.0 | 2026-11-18T15:25:04.942714+00:00 | Not calibrated | WEAK 43/100 | EXTREME 88/100 | Do nothing | WATCH |
| 10 | CC/USD | 0.08293 | 33.639 | 40.729 | +0.97% | -0.08% | 0.33x | 3.6 | 2026-11-18T15:25:04.942714+00:00 | Not calibrated | WEAK 22/100 | VERY_HIGH 81/100 | Do nothing | WATCH |
| 11 | AKT/USD | 0.5121 | 28.844 | 28.335 | +0.55% | -0.85% | 1.48x | 15.6 | 2026-11-18T15:25:04.942714+00:00 | Not calibrated | WEAK 29/100 | VERY_HIGH 72/100 | Do nothing | WATCH |
| 12 | FLR/USD | 0.0052 | 27.499 | 33.934 | +1.76% | +0.00% | 0.36x | 19.3 | 2026-11-18T15:25:04.942714+00:00 | Not calibrated | WEAK 29/100 | EXTREME 88/100 | Do nothing | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | SENT/USD | 67.901 | 0.01974 | +1.20% | 0.93x |
| 2 | STABLE/USD | 65.153 | 0.02305 | -0.65% | 1.36x |
| 3 | CT/USD | 63.889 | 0.1236 | +1.23% | 1.44x |
| 4 | AKE/USD | 54.538 | 0.01042827 | -2.23% | 1.48x |
| 5 | MNT/USD | 52.153 | 0.3856 | +0.10% | 0.37x |
| 6 | NIGHT/USD | 49.039 | 0.04531 | +0.29% | 0.81x |
| 7 | TRX/USD | 46.020 | 0.310106 | +0.04% | 1.26x |
| 8 | RE/USD | 41.143 | 0.23881 | +0.34% | 0.38x |
| 9 | CC/USD | 40.729 | 0.08293 | -0.08% | 0.33x |
| 10 | CAP/USD | 37.454 | 0.102264 | +0.17% | 4.19x |
| 11 | FLR/USD | 33.934 | 0.0052 | +0.00% | 0.36x |
| 12 | AKT/USD | 28.335 | 0.5121 | -0.85% | 1.48x |

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

- Persisted scans: 600; predictions: 5136; observations: 362407.
- Matured sampled outcomes across 1/6/24/48h: 4336; gap abstentions: 13125. Per-horizon counts require independent audit; do not infer held-out lift.
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

**Writer:** 44335297209 · **Generation:** 600 · **Legacy run:** 44335297209
**Main quote time:** 2026-11-18T15:25:12.320272+00:00 · **Legacy report time:** 2026-11-18T15:25:32.814389+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | CT/USD ⭐ | 0.1236 | 74.38 | +1.23% | 1.44x | STRONG 82/100 | VERY_HIGH 79/100 | Watch |
| 2 | SENT/USD | 0.01974 | 73.18 | +1.20% | 0.93x | MODERATE 67/100 | VERY_HIGH 74/100 | Watch |
| 3 | STABLE/USD | 0.02305 | 65.56 | -0.65% | 1.36x | WEAK 43/100 | EXTREME 85/100 | Do nothing |
| 4 | CAP/USD ⭐ | 0.102264 | 53.31 | +0.17% | 4.19x | STRONG 82/100 | HIGH 67/100 | Watch |
| 5 | TRX/USD | 0.310106 | 48.85 | +0.04% | 1.26x | MODERATE 49/100 | HIGH 55/100 | Watch |
| 6 | NIGHT/USD | 0.04531 | 48.54 | +0.29% | 0.81x | MODERATE 49/100 | HIGH 68/100 | Watch |
| 7 | AKE/USD | 0.01042827 | 48.18 | -2.23% | 1.48x | WEAK 34/100 | VERY_HIGH 82/100 | Do nothing |
| 8 | MNT/USD | 0.3856 | 46.40 | +0.10% | 0.37x | WEAK 43/100 | VERY_HIGH 75/100 | Watch |
| 9 | RE/USD | 0.23881 | 36.62 | +0.34% | 0.38x | WEAK 43/100 | EXTREME 88/100 | Do nothing |
| 10 | CC/USD | 0.08293 | 33.64 | -0.08% | 0.33x | WEAK 22/100 | VERY_HIGH 81/100 | Do nothing |
| 11 | AKT/USD | 0.5121 | 28.84 | -0.85% | 1.48x | WEAK 29/100 | VERY_HIGH 72/100 | Do nothing |
| 12 | FLR/USD | 0.0052 | 27.50 | +0.00% | 0.36x | WEAK 29/100 | EXTREME 88/100 | Do nothing |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | CT/USD ⭐ | 0.1236 | 64.49 | +1.23% | 1.44x | 1252 | STRONG 87/100 | HIGH 67/100 | Watch |
| 2 | CAP/USD ⭐ | 0.102264 | 45.68 | +0.17% | 4.19x | 2524 | STRONG 78/100 | HIGH 67/100 | Watch |

**Same-run overlap:** CT/USD, CAP/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
