# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-25T15:02:38.576156+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/45640101945
**Source SHA:** 858c8bc8ec5d7641ddb39cacd8aca91719f855b1
**Previous ledger commit:** e50d60d75e28324270a6d497b8d58148545cb5be (atomic ledger/results publication)
**Ledger generation:** 1733 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 5s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 627; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 609; valid market observations: 608; OHLC screened: 14.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | VVV/USD | 25.296 | 98.045 | 70.670 | +3.09% | +3.57% | 1.95x | 11.9 | 2026-11-25T15:02:34.011417+00:00 | Not calibrated | STRONG 89/100 | VERY_HIGH 71/100 | Watch | WATCH |
| 2 | MON/USD | 0.00999 | 89.154 | 72.756 | +5.49% | +1.22% | 2.03x | 20.1 | 2026-11-25T15:02:34.011417+00:00 | Not calibrated | STRONG 90/100 | HIGH 67/100 | Consider small entry | WATCH |
| 3 | DRV/USD | 0.3277 | 78.306 | 63.123 | +4.27% | +1.08% | 1.98x | 9.5 | 2026-11-25T15:02:34.011417+00:00 | Not calibrated | STRONG 84/100 | HIGH 55/100 | Consider small entry | WATCH |
| 4 | XPL/USD | 0.0457 | 76.619 | 51.484 | +3.86% | +2.03% | 3.90x | 21.9 | 2026-11-25T15:02:34.011417+00:00 | Not calibrated | STRONG 83/100 | VERY_HIGH 72/100 | Watch | WATCH |
| 5 | CT/USD | 0.1315 | 67.564 | 44.739 | +4.12% | +2.74% | 1.91x | 30.4 | 2026-11-25T15:02:34.011417+00:00 | Not calibrated | MODERATE 69/100 | VERY_HIGH 79/100 | Watch | WATCH |
| 6 | PIEVERSE/USD | 3.2862 | 51.552 | 60.752 | +6.68% | -4.84% | 14.25x | 31.4 | 2026-11-25T15:02:34.011417+00:00 | Not calibrated | MODERATE 46/100 | EXTREME 89/100 | Do nothing | WATCH |
| 7 | ASTER/USD | 0.48385 | 44.866 | 33.887 | +0.63% | +1.10% | 1.55x | 5.6 | 2026-11-25T15:02:34.011417+00:00 | Not calibrated | MODERATE 67/100 | HIGH 60/100 | Watch | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | MON/USD | 72.756 | 0.00999 | +1.22% | 2.03x |
| 2 | VVV/USD | 70.670 | 25.296 | +3.57% | 1.95x |
| 3 | DRV/USD | 63.123 | 0.3277 | +1.08% | 1.98x |
| 4 | PIEVERSE/USD | 60.752 | 3.2862 | -4.84% | 14.25x |
| 5 | XPL/USD | 51.484 | 0.0457 | +2.03% | 3.90x |
| 6 | CT/USD | 44.739 | 0.1315 | +2.74% | 1.91x |
| 7 | ASTER/USD | 33.887 | 0.48385 | +1.10% | 1.55x |

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

- Persisted scans: 1733; predictions: 14594; observations: 1050449.
- Matured sampled outcomes across 1/6/24/48h: 32226; gap abstentions: 22370. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 146 (sampled only; not a success-rate estimate).
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

**Writer:** 45640101945 · **Generation:** 1733 · **Legacy run:** 45640101945
**Main quote time:** 2026-11-25T15:02:38.576156+00:00 · **Legacy report time:** 2026-11-25T15:03:55.519947+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | VVV/USD ⭐ | 25.296 | 98.05 | +3.57% | 1.95x | STRONG 99/100 | VERY_HIGH 71/100 | Watch |
| 2 | MON/USD ⭐ | 0.00999 | 89.15 | +1.22% | 2.03x | STRONG 100/100 | HIGH 67/100 | Consider small entry |
| 3 | DRV/USD ⭐ | 0.3277 | 78.31 | +1.08% | 1.98x | STRONG 94/100 | HIGH 55/100 | Consider small entry |
| 4 | XPL/USD ⭐ | 0.0457 | 76.62 | +2.03% | 3.90x | STRONG 93/100 | VERY_HIGH 72/100 | Watch |
| 5 | CT/USD ⭐ | 0.1315 | 67.56 | +2.74% | 1.91x | STRONG 79/100 | VERY_HIGH 79/100 | Watch |
| 6 | PIEVERSE/USD | 3.2862 | 51.55 | -4.84% | 14.25x | MODERATE 46/100 | EXTREME 89/100 | Do nothing |
| 7 | ASTER/USD ⭐ | 0.48385 | 44.87 | +1.10% | 1.55x | STRONG 77/100 | HIGH 60/100 | Consider small entry |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | MON/USD ⭐ | 0.01001 | 86.36 | +1.22% | 2.03x | 15370 | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 2 | VVV/USD ⭐ | 25.301 | 86.13 | +3.57% | 1.95x | 12739 | STRONG 93/100 | VERY_HIGH 71/100 | Watch |
| 3 | DRV/USD ⭐ | 0.32662 | 81.04 | +1.08% | 1.98x | 10674 | STRONG 91/100 | HIGH 61/100 | Consider small entry |
| 4 | XPL/USD ⭐ | 0.0456 | 75.54 | +2.03% | 3.90x | 1748 | STRONG 93/100 | VERY_HIGH 72/100 | Watch |
| 5 | MOODENG/USD | 0.02655 | 74.37 | +1.75% | 2.10x | 1794 | STRONG 77/100 | VERY_HIGH 72/100 | Watch |
| 6 | CT/USD ⭐ | 0.1315 | 73.29 | +2.74% | 1.91x | 1556 | STRONG 82/100 | VERY_HIGH 79/100 | Watch |
| 7 | ASTER/USD ⭐ | 0.48337 | 40.69 | +1.10% | 1.55x | 2696 | STRONG 75/100 | HIGH 60/100 | Consider small entry |

**Same-run overlap:** VVV/USD, MON/USD, DRV/USD, XPL/USD, CT/USD, ASTER/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
