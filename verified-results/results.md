# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-25T00:22:15.881467+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/45517197419
**Source SHA:** 858c8bc8ec5d7641ddb39cacd8aca91719f855b1
**Previous ledger commit:** 28b3cbc6f57d714abc350cc2d016edbff7d7ced3 (atomic ledger/results publication)
**Ledger generation:** 1645 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 4s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 628; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 610; valid market observations: 609; OHLC screened: 12.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | VVV/USD | 24.607 | 60.136 | 53.717 | +0.28% | -0.35% | 1.82x | 6.5 | 2026-11-25T00:22:11.651650+00:00 | Not calibrated | MODERATE 50/100 | HIGH 61/100 | Watch | WATCH |
| 2 | PEARL/USD | 2.1581 | 37.789 | 35.350 | +0.84% | -0.00% | 1.25x | 18.1 | 2026-11-25T00:22:11.651650+00:00 | Not calibrated | WEAK 24/100 | VERY_HIGH 74/100 | Do nothing | WATCH |
| 3 | SKY/USD | 0.04141 | 34.661 | 33.919 | +1.05% | -0.34% | 1.24x | 14.5 | 2026-11-25T00:22:11.651650+00:00 | Not calibrated | WEAK 22/100 | VERY_HIGH 79/100 | Do nothing | WATCH |
| 4 | DRV/USD | 0.31551 | 20.788 | 26.619 | +0.39% | -1.60% | 1.22x | 20.6 | 2026-11-25T00:22:11.651650+00:00 | Not calibrated | WEAK 10/100 | EXTREME 89/100 | Do nothing | WATCH |
| 5 | BLESS/USD | 0.017707 | 20.592 | 29.032 | +0.66% | -0.66% | 0.49x | 26.1 | 2026-11-25T00:22:11.651650+00:00 | Not calibrated | WEAK 5/100 | EXTREME 88/100 | Do nothing | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | VVV/USD | 53.717 | 24.607 | -0.35% | 1.82x |
| 2 | PEARL/USD | 35.350 | 2.1581 | -0.00% | 1.25x |
| 3 | SKY/USD | 33.919 | 0.04141 | -0.34% | 1.24x |
| 4 | BLESS/USD | 29.032 | 0.017707 | -0.66% | 0.49x |
| 5 | DRV/USD | 26.619 | 0.31551 | -1.60% | 1.22x |

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

- Persisted scans: 1645; predictions: 14071; observations: 996896.
- Matured sampled outcomes across 1/6/24/48h: 29244; gap abstentions: 22370. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 143 (sampled only; not a success-rate estimate).
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

**Writer:** 45517197419 · **Generation:** 1645 · **Legacy run:** 45517197419
**Main quote time:** 2026-11-25T00:22:15.881467+00:00 · **Legacy report time:** 2026-11-25T00:23:09.772057+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | VVV/USD | 24.607 | 60.14 | -0.35% | 1.82x | MODERATE 50/100 | HIGH 61/100 | Watch |
| 2 | PEARL/USD | 2.1581 | 37.79 | -0.00% | 1.25x | WEAK 24/100 | VERY_HIGH 74/100 | Do nothing |
| 3 | SKY/USD | 0.04141 | 34.66 | -0.34% | 1.24x | WEAK 22/100 | VERY_HIGH 79/100 | Do nothing |
| 4 | DRV/USD | 0.31551 | 20.79 | -1.60% | 1.22x | WEAK 10/100 | EXTREME 89/100 | Do nothing |
| 5 | BLESS/USD | 0.017707 | 20.59 | -0.66% | 0.49x | WEAK 5/100 | EXTREME 88/100 | Do nothing |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | SYRUP/USD | 0.06983 | 26.35 | +0.14% | 1.05x | 3338 | WEAK 28/100 | EXTREME 86/100 | Do nothing |

**Same-run overlap:** None
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
