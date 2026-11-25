# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-25T14:32:22.190783+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/45634641364
**Source SHA:** 858c8bc8ec5d7641ddb39cacd8aca91719f855b1
**Previous ledger commit:** c64c8cca8fcd1c3ea9805c3111201c2dd9af64cd (atomic ledger/results publication)
**Ledger generation:** 1730 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 4s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 627; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 609; valid market observations: 608; OHLC screened: 12.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | MON/USD | 0.00986 | 55.678 | 64.051 | +4.12% | -0.10% | 0.21x | 20.3 | 2026-11-25T14:32:18.008627+00:00 | Not calibrated | WEAK 23/100 | EXTREME 88/100 | Do nothing | WATCH |
| 2 | VVV/USD | 24.652 | 51.185 | 53.381 | +0.46% | +0.07% | 0.75x | 9.7 | 2026-11-25T14:32:18.008627+00:00 | Not calibrated | MODERATE 46/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 3 | DRV/USD | 0.32292 | 48.626 | 47.716 | +2.75% | -0.32% | 1.25x | 18.6 | 2026-11-25T14:32:18.008627+00:00 | Not calibrated | WEAK 29/100 | HIGH 67/100 | Do nothing | WATCH |
| 4 | MOODENG/USD | 0.02605 | 44.403 | 66.179 | +7.07% | -4.08% | 0.86x | 23.1 | 2026-11-25T14:32:18.008627+00:00 | Not calibrated | WEAK 17/100 | EXTREME 89/100 | Do nothing | WATCH |
| 5 | CT/USD | 0.1296 | 31.852 | 33.922 | +2.61% | -0.08% | 0.83x | 31.0 | 2026-11-25T14:32:18.008627+00:00 | Not calibrated | WEAK 11/100 | EXTREME 92/100 | Do nothing | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | MOODENG/USD | 66.179 | 0.02605 | -4.08% | 0.86x |
| 2 | MON/USD | 64.051 | 0.00986 | -0.10% | 0.21x |
| 3 | VVV/USD | 53.381 | 24.652 | +0.07% | 0.75x |
| 4 | DRV/USD | 47.716 | 0.32292 | -0.32% | 1.25x |
| 5 | CT/USD | 33.922 | 0.1296 | -0.08% | 0.83x |

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

- Persisted scans: 1730; predictions: 14574; observations: 1048625.
- Matured sampled outcomes across 1/6/24/48h: 32120; gap abstentions: 22370. Per-horizon counts require independent audit; do not infer held-out lift.
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

**Writer:** 45634641364 · **Generation:** 1730 · **Legacy run:** 45634641364
**Main quote time:** 2026-11-25T14:32:22.190783+00:00 · **Legacy report time:** 2026-11-25T14:33:12.263656+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | MON/USD | 0.00986 | 55.68 | -0.10% | 0.21x | WEAK 23/100 | EXTREME 88/100 | Do nothing |
| 2 | VVV/USD | 24.652 | 51.18 | +0.07% | 0.75x | MODERATE 46/100 | VERY_HIGH 70/100 | Watch |
| 3 | DRV/USD | 0.32292 | 48.63 | -0.32% | 1.25x | WEAK 29/100 | HIGH 67/100 | Do nothing |
| 4 | MOODENG/USD | 0.02605 | 44.40 | -4.08% | 0.86x | WEAK 17/100 | EXTREME 89/100 | Do nothing |
| 5 | CT/USD | 0.1296 | 31.85 | -0.08% | 0.83x | WEAK 11/100 | EXTREME 92/100 | Do nothing |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| — | No confirmed WATCH signals | — | — | — | — | — | — | — | — |

**Same-run overlap:** None
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
