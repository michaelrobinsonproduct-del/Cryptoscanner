# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-25T12:52:35.589507+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/45617483706
**Source SHA:** 858c8bc8ec5d7641ddb39cacd8aca91719f855b1
**Previous ledger commit:** a2056e1e27be0ca6dab0c05a155000670b7e1c8f (atomic ledger/results publication)
**Ledger generation:** 1720 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 6s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 627; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 609; valid market observations: 608; OHLC screened: 18.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | VVV/USD | 25.151 | 84.388 | 68.112 | +2.50% | +0.26% | 3.06x | 8.8 | 2026-11-25T12:52:29.615644+00:00 | Not calibrated | STRONG 97/100 | HIGH 55/100 | Consider small entry | WATCH |
| 2 | MOODENG/USD | 0.02662 | 79.886 | 66.052 | +9.41% | -0.07% | 2.42x | 22.6 | 2026-11-25T12:52:29.615644+00:00 | Not calibrated | MODERATE 60/100 | VERY_HIGH 78/100 | Watch | WATCH |
| 3 | MON/USD | 0.00982 | 73.362 | 63.714 | +3.70% | -0.81% | 2.37x | 20.4 | 2026-11-25T12:52:29.615644+00:00 | Not calibrated | MODERATE 57/100 | VERY_HIGH 73/100 | Watch | WATCH |
| 4 | BABY/USD | 0.00889 | 65.219 | 65.307 | +7.63% | +1.02% | 0.48x | 22.5 | 2026-11-25T12:52:29.615644+00:00 | Not calibrated | MODERATE 53/100 | EXTREME 94/100 | Do nothing | WATCH |
| 5 | INX/USD | 0.003955 | 50.128 | 44.481 | +3.24% | +0.41% | 1.36x | 17.7 | 2026-11-25T12:52:29.615644+00:00 | Not calibrated | MODERATE 65/100 | VERY_HIGH 73/100 | Watch | WATCH |
| 6 | XPL/USD | 0.0446 | 37.655 | 33.508 | +1.36% | -0.89% | 1.86x | 22.4 | 2026-11-25T12:52:29.615644+00:00 | Not calibrated | WEAK 29/100 | VERY_HIGH 78/100 | Do nothing | WATCH |
| 7 | CAP/USD | 0.092994 | 28.691 | 33.042 | +0.62% | +0.00% | 0.56x | 6.1 | 2026-11-25T12:52:29.615644+00:00 | Not calibrated | WEAK 34/100 | VERY_HIGH 75/100 | Do nothing | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | VVV/USD | 68.112 | 25.151 | +0.26% | 3.06x |
| 2 | MOODENG/USD | 66.052 | 0.02662 | -0.07% | 2.42x |
| 3 | BABY/USD | 65.307 | 0.00889 | +1.02% | 0.48x |
| 4 | MON/USD | 63.714 | 0.00982 | -0.81% | 2.37x |
| 5 | INX/USD | 44.481 | 0.003955 | +0.41% | 1.36x |
| 6 | XPL/USD | 33.508 | 0.0446 | -0.89% | 1.86x |
| 7 | CAP/USD | 33.042 | 0.092994 | +0.00% | 0.56x |

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

- Persisted scans: 1720; predictions: 14522; observations: 1042545.
- Matured sampled outcomes across 1/6/24/48h: 31788; gap abstentions: 22370. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 146 (sampled only; not a success-rate estimate).
- False positives / missed movers: NOT VERIFIED without eligible continuous outcome coverage.
- Baseline vs challenger: recorded as-of; unbiased held-out lift NOT MEASURED.
- Online Kraken /USD stablecoin-base pairs excluded: 18 (counted from this scan's online AssetPairs metadata, not inferred from price).
- Stablecoin base exclusions: BRL1, BUSD, DAI, EUR, EURC, EUROP, EURQ, EURR, EURT, FDUSD, FRAX, GUSD, PYUSD, QCAD, RLUSD, TGBP, TUSD, USD, USD1, USDC, USDD, USDE, USDG, USDQ, USDR, USDS, USDT, ZUSD.
- DEX: NOT USED; no DEX freshness gate.
- OHLC screening abstentions: 11; details in immutable scan JSON artifact.
- Storage: ledger and results published in one non-force Git commit and read back. Independent artifact recovery is NOT VERIFIED by this scan alone.
- Errors: none in successful committed scan; a failed workflow must not publish a SUCCESS report.

# Cryptoscanner — challenger and independent legacy-inspired WATCH

Paper only · risk is high or higher · 30%+ in 48h probability NOT CALIBRATED
Signal confidence 0–100 means setup strength only, NOT a win probability. Actions are research guidance; no trade authorization.

**Writer:** 45617483706 · **Generation:** 1720 · **Legacy run:** 45617483706
**Main quote time:** 2026-11-25T12:52:35.589507+00:00 · **Legacy report time:** 2026-11-25T12:53:52.932806+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | VVV/USD ⭐ | 25.151 | 84.39 | +0.26% | 3.06x | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 2 | MOODENG/USD | 0.02662 | 79.89 | -0.07% | 2.42x | MODERATE 60/100 | VERY_HIGH 78/100 | Watch |
| 3 | MON/USD | 0.00982 | 73.36 | -0.81% | 2.37x | MODERATE 57/100 | VERY_HIGH 73/100 | Watch |
| 4 | BABY/USD | 0.00889 | 65.22 | +1.02% | 0.48x | MODERATE 53/100 | EXTREME 94/100 | Do nothing |
| 5 | INX/USD ⭐ | 0.003955 | 50.13 | +0.41% | 1.36x | STRONG 75/100 | VERY_HIGH 73/100 | Watch |
| 6 | XPL/USD | 0.0446 | 37.66 | -0.89% | 1.86x | WEAK 29/100 | VERY_HIGH 78/100 | Do nothing |
| 7 | CAP/USD | 0.092994 | 28.69 | +0.00% | 0.56x | WEAK 34/100 | VERY_HIGH 75/100 | Do nothing |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | VVV/USD ⭐ | 25.206 | 78.43 | +0.26% | 3.06x | 12458 | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 2 | INX/USD ⭐ | 0.003974 | 60.56 | +0.41% | 1.36x | 1523 | STRONG 80/100 | VERY_HIGH 73/100 | Watch |

**Same-run overlap:** VVV/USD, INX/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
