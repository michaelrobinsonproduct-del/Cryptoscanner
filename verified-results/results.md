# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-18T13:10:13.368569+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/44310866289
**Source SHA:** b271b90a2cae9e5307600070ce7d0e510fe68996
**Previous ledger commit:** ae0bf8fa6138d9588146639c6d99d8623878ccc8 (atomic ledger/results publication)
**Ledger generation:** 573 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 6s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 627; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 609; valid market observations: 609; OHLC screened: 19.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | NIGHT/USD | 0.0463 | 76.705 | 64.176 | +3.14% | -0.49% | 7.11x | 13.0 | 2026-11-18T13:10:07.204349+00:00 | Not calibrated | MODERATE 63/100 | HIGH 67/100 | Watch | WATCH |
| 2 | STABLE/USD | 0.02338 | 66.076 | 69.561 | +11.07% | +0.86% | 0.22x | 12.8 | 2026-11-18T13:10:07.204349+00:00 | Not calibrated | MODERATE 58/100 | EXTREME 88/100 | Do nothing | WATCH |
| 3 | MNT/USD | 0.3843 | 60.678 | 49.789 | +2.95% | -0.13% | 2.15x | 7.8 | 2026-11-18T13:10:07.204349+00:00 | Not calibrated | MODERATE 60/100 | HIGH 66/100 | Watch | WATCH |
| 4 | USELESS/USD | 0.10044 | 56.092 | 53.529 | +2.93% | +0.16% | 1.18x | 17.9 | 2026-11-18T13:10:07.204349+00:00 | Not calibrated | MODERATE 48/100 | HIGH 68/100 | Watch | WATCH |
| 5 | SENT/USD | 0.019415 | 49.854 | 55.146 | +4.00% | -0.39% | 0.67x | 7.7 | 2026-11-18T13:10:07.204349+00:00 | Not calibrated | WEAK 30/100 | EXTREME 88/100 | Do nothing | WATCH |
| 6 | CC/USD | 0.08335 | 48.794 | 43.824 | +1.49% | +0.35% | 1.32x | 4.8 | 2026-11-18T13:10:07.204349+00:00 | Not calibrated | MODERATE 69/100 | HIGH 60/100 | Watch | WATCH |
| 7 | ME/USD | 0.0402 | 48.514 | 48.082 | +4.15% | -0.25% | 1.17x | 24.9 | 2026-11-18T13:10:07.204349+00:00 | Not calibrated | WEAK 24/100 | EXTREME 92/100 | Do nothing | WATCH |
| 8 | TRX/USD | 0.309162 | 36.064 | 43.889 | +0.41% | -0.16% | 0.30x | 0.8 | 2026-11-18T13:10:07.204349+00:00 | Not calibrated | WEAK 23/100 | VERY_HIGH 76/100 | Do nothing | WATCH |
| 9 | AKT/USD | 0.5191 | 35.650 | 37.274 | +1.92% | +0.15% | 0.76x | 17.3 | 2026-11-18T13:10:07.204349+00:00 | Not calibrated | WEAK 33/100 | VERY_HIGH 73/100 | Do nothing | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | STABLE/USD | 69.561 | 0.02338 | +0.86% | 0.22x |
| 2 | NIGHT/USD | 64.176 | 0.0463 | -0.49% | 7.11x |
| 3 | SENT/USD | 55.146 | 0.019415 | -0.39% | 0.67x |
| 4 | USELESS/USD | 53.529 | 0.10044 | +0.16% | 1.18x |
| 5 | MNT/USD | 49.789 | 0.3843 | -0.13% | 2.15x |
| 6 | ME/USD | 48.082 | 0.0402 | -0.25% | 1.17x |
| 7 | TRX/USD | 43.889 | 0.309162 | -0.16% | 0.30x |
| 8 | CC/USD | 43.824 | 0.08335 | +0.35% | 1.32x |
| 9 | AKT/USD | 37.274 | 0.5191 | +0.15% | 0.76x |

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

- Persisted scans: 573; predictions: 4842; observations: 345964.
- Matured sampled outcomes across 1/6/24/48h: 4226; gap abstentions: 13019. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 0 (sampled only; not a success-rate estimate).
- False positives / missed movers: NOT VERIFIED without eligible continuous outcome coverage.
- Baseline vs challenger: recorded as-of; unbiased held-out lift NOT MEASURED.
- Online Kraken /USD stablecoin-base pairs excluded: 18 (counted from this scan's online AssetPairs metadata, not inferred from price).
- Stablecoin base exclusions: BRL1, BUSD, DAI, EUR, EURC, EUROP, EURQ, EURR, EURT, FDUSD, FRAX, GUSD, PYUSD, QCAD, RLUSD, TGBP, TUSD, USD, USD1, USDC, USDD, USDE, USDG, USDQ, USDR, USDS, USDT, ZUSD.
- DEX: NOT USED; no DEX freshness gate.
- OHLC screening abstentions: 10; details in immutable scan JSON artifact.
- Storage: ledger and results published in one non-force Git commit and read back. Independent artifact recovery is NOT VERIFIED by this scan alone.
- Errors: none in successful committed scan; a failed workflow must not publish a SUCCESS report.

# Cryptoscanner — challenger and independent legacy-inspired WATCH

Paper only · risk is high or higher · 30%+ in 48h probability NOT CALIBRATED
Signal confidence 0–100 means setup strength only, NOT a win probability. Actions are research guidance; no trade authorization.

**Writer:** 44310866289 · **Generation:** 573 · **Legacy run:** 44310866289
**Main quote time:** 2026-11-18T13:10:13.368569+00:00 · **Legacy report time:** 2026-11-18T13:10:38.448000+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | NIGHT/USD | 0.0463 | 76.70 | -0.49% | 7.11x | MODERATE 63/100 | HIGH 67/100 | Watch |
| 2 | STABLE/USD | 0.02338 | 66.08 | +0.86% | 0.22x | MODERATE 58/100 | EXTREME 88/100 | Do nothing |
| 3 | MNT/USD | 0.3843 | 60.68 | -0.13% | 2.15x | MODERATE 60/100 | HIGH 66/100 | Watch |
| 4 | USELESS/USD ⭐ | 0.10044 | 56.09 | +0.16% | 1.18x | MODERATE 58/100 | HIGH 68/100 | Watch |
| 5 | SENT/USD | 0.019415 | 49.85 | -0.39% | 0.67x | WEAK 30/100 | EXTREME 88/100 | Do nothing |
| 6 | CC/USD ⭐ | 0.08335 | 48.79 | +0.35% | 1.32x | STRONG 79/100 | HIGH 60/100 | Watch |
| 7 | ME/USD | 0.0402 | 48.51 | -0.25% | 1.17x | WEAK 24/100 | EXTREME 92/100 | Do nothing |
| 8 | TRX/USD | 0.309162 | 36.06 | -0.16% | 0.30x | WEAK 23/100 | VERY_HIGH 76/100 | Do nothing |
| 9 | AKT/USD | 0.5191 | 35.65 | +0.15% | 0.76x | WEAK 33/100 | VERY_HIGH 73/100 | Do nothing |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | USELESS/USD ⭐ | 0.1009 | 71.21 | +0.16% | 1.18x | 5315 | MODERATE 66/100 | HIGH 68/100 | Watch |
| 2 | XRP/USD | 0.98523 | 63.97 | +0.29% | 3.59x | 35626 | STRONG 87/100 | HIGH 55/100 | Watch |
| 3 | CC/USD ⭐ | 0.08335 | 53.44 | +0.35% | 1.32x | 4829 | STRONG 82/100 | HIGH 60/100 | Watch |

**Same-run overlap:** USELESS/USD, CC/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
