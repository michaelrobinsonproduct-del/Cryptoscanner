# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-25T01:32:18.929306+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/45526128537
**Source SHA:** 858c8bc8ec5d7641ddb39cacd8aca91719f855b1
**Previous ledger commit:** 246868b2d74fd3faf26931dc332f692ee22852ee (atomic ledger/results publication)
**Ledger generation:** 1651 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 5s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 628; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 610; valid market observations: 609; OHLC screened: 14.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | PEARL/USD | 2.1908 | 52.457 | 51.773 | +2.37% | -0.09% | 1.11x | 7.3 | 2026-11-25T01:32:13.436470+00:00 | Not calibrated | WEAK 36/100 | HIGH 68/100 | Watch | WATCH |
| 2 | DRV/USD | 0.32003 | 50.292 | 47.108 | +1.83% | +0.86% | 0.89x | 0.3 | 2026-11-25T01:32:13.436470+00:00 | Not calibrated | MODERATE 55/100 | HIGH 67/100 | Watch | WATCH |
| 3 | SKY/USD | 0.0414 | 33.365 | 36.256 | +1.02% | -0.81% | 1.12x | 9.7 | 2026-11-25T01:32:13.436470+00:00 | Not calibrated | WEAK 27/100 | VERY_HIGH 73/100 | Do nothing | WATCH |
| 4 | GWEI/USD | 0.010423 | 33.252 | 27.784 | +1.15% | +1.14% | 0.98x | 21.9 | 2026-11-25T01:32:13.436470+00:00 | Not calibrated | WEAK 37/100 | EXTREME 86/100 | Do nothing | WATCH |
| 5 | SYRUP/USD | 0.07077 | 30.371 | 25.696 | +1.58% | +0.53% | 1.20x | 34.0 | 2026-11-25T01:32:13.436470+00:00 | Not calibrated | WEAK 40/100 | EXTREME 86/100 | Do nothing | WATCH |
| 6 | LUNA/USD | 4.594e-05 | 20.565 | 21.073 | +0.35% | +0.24% | 0.83x | 26.2 | 2026-11-25T01:32:13.436470+00:00 | Not calibrated | WEAK 30/100 | VERY_HIGH 79/100 | Do nothing | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | PEARL/USD | 51.773 | 2.1908 | -0.09% | 1.11x |
| 2 | DRV/USD | 47.108 | 0.32003 | +0.86% | 0.89x |
| 3 | SKY/USD | 36.256 | 0.0414 | -0.81% | 1.12x |
| 4 | GWEI/USD | 27.784 | 0.010423 | +1.14% | 0.98x |
| 5 | SYRUP/USD | 25.696 | 0.07077 | +0.53% | 1.20x |
| 6 | LUNA/USD | 21.073 | 4.594e-05 | +0.24% | 0.83x |

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

- Persisted scans: 1651; predictions: 14105; observations: 1000550.
- Matured sampled outcomes across 1/6/24/48h: 29459; gap abstentions: 22370. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 143 (sampled only; not a success-rate estimate).
- False positives / missed movers: NOT VERIFIED without eligible continuous outcome coverage.
- Baseline vs challenger: recorded as-of; unbiased held-out lift NOT MEASURED.
- Online Kraken /USD stablecoin-base pairs excluded: 18 (counted from this scan's online AssetPairs metadata, not inferred from price).
- Stablecoin base exclusions: BRL1, BUSD, DAI, EUR, EURC, EUROP, EURQ, EURR, EURT, FDUSD, FRAX, GUSD, PYUSD, QCAD, RLUSD, TGBP, TUSD, USD, USD1, USDC, USDD, USDE, USDG, USDQ, USDR, USDS, USDT, ZUSD.
- DEX: NOT USED; no DEX freshness gate.
- OHLC screening abstentions: 8; details in immutable scan JSON artifact.
- Storage: ledger and results published in one non-force Git commit and read back. Independent artifact recovery is NOT VERIFIED by this scan alone.
- Errors: none in successful committed scan; a failed workflow must not publish a SUCCESS report.

# Cryptoscanner — challenger and independent legacy-inspired WATCH

Paper only · risk is high or higher · 30%+ in 48h probability NOT CALIBRATED
Signal confidence 0–100 means setup strength only, NOT a win probability. Actions are research guidance; no trade authorization.

**Writer:** 45526128537 · **Generation:** 1651 · **Legacy run:** 45526128537
**Main quote time:** 2026-11-25T01:32:18.929306+00:00 · **Legacy report time:** 2026-11-25T01:33:27.989665+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | PEARL/USD | 2.1908 | 52.46 | -0.09% | 1.11x | WEAK 36/100 | HIGH 68/100 | Watch |
| 2 | DRV/USD | 0.32003 | 50.29 | +0.86% | 0.89x | MODERATE 55/100 | HIGH 67/100 | Watch |
| 3 | SKY/USD | 0.0414 | 33.36 | -0.81% | 1.12x | WEAK 27/100 | VERY_HIGH 73/100 | Do nothing |
| 4 | GWEI/USD | 0.010423 | 33.25 | +1.14% | 0.98x | WEAK 37/100 | EXTREME 86/100 | Do nothing |
| 5 | SYRUP/USD ⭐ | 0.07077 | 30.37 | +0.53% | 1.20x | MODERATE 50/100 | EXTREME 86/100 | Do nothing |
| 6 | LUNA/USD | 4.594e-05 | 20.57 | +0.24% | 0.83x | WEAK 30/100 | VERY_HIGH 79/100 | Do nothing |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | SYRUP/USD ⭐ | 0.07061 | 41.56 | +0.53% | 1.20x | 3320 | MODERATE 56/100 | EXTREME 86/100 | Do nothing |

**Same-run overlap:** SYRUP/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
