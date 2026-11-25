# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-25T09:57:23.792702+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/45589871629
**Source SHA:** 858c8bc8ec5d7641ddb39cacd8aca91719f855b1
**Previous ledger commit:** 8b7eb42d5cd6ad04f7a0ef1baaebaa0b512dc052 (atomic ledger/results publication)
**Ledger generation:** 1702 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 10s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 628; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 610; valid market observations: 609; OHLC screened: 20.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | MON/USD | 0.01019 | 78.662 | 85.054 | +7.60% | +0.00% | 0.36x | 19.6 | 2026-11-25T09:57:14.246983+00:00 | Not calibrated | MODERATE 54/100 | VERY_HIGH 76/100 | Watch | WATCH |
| 2 | VVV/USD | 24.77 | 58.830 | 57.372 | +0.95% | +0.85% | 0.72x | 8.5 | 2026-11-25T09:57:14.246983+00:00 | Not calibrated | MODERATE 59/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 3 | 2Z/USD | 0.01671 | 37.885 | 38.673 | +1.95% | -1.89% | 1.87x | 12.0 | 2026-11-25T09:57:14.246983+00:00 | Not calibrated | WEAK 34/100 | VERY_HIGH 83/100 | Do nothing | WATCH |
| 4 | BABY/USD | 0.00859 | 31.462 | 42.014 | +4.00% | -0.58% | 0.23x | 35.0 | 2026-11-25T09:57:14.246983+00:00 | Not calibrated | WEAK 6/100 | EXTREME 100/100 | Do nothing | WATCH |
| 5 | SYRUP/USD | 0.06994 | 28.872 | 23.495 | +0.39% | -0.48% | 1.78x | 21.5 | 2026-11-25T09:57:14.246983+00:00 | Not calibrated | WEAK 24/100 | EXTREME 85/100 | Do nothing | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | MON/USD | 85.054 | 0.01019 | +0.00% | 0.36x |
| 2 | VVV/USD | 57.372 | 24.77 | +0.85% | 0.72x |
| 3 | BABY/USD | 42.014 | 0.00859 | -0.58% | 0.23x |
| 4 | 2Z/USD | 38.673 | 0.01671 | -1.89% | 1.87x |
| 5 | SYRUP/USD | 23.495 | 0.06994 | -0.48% | 1.78x |

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

- Persisted scans: 1702; predictions: 14435; observations: 1031600.
- Matured sampled outcomes across 1/6/24/48h: 31177; gap abstentions: 22370. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 146 (sampled only; not a success-rate estimate).
- False positives / missed movers: NOT VERIFIED without eligible continuous outcome coverage.
- Baseline vs challenger: recorded as-of; unbiased held-out lift NOT MEASURED.
- Online Kraken /USD stablecoin-base pairs excluded: 18 (counted from this scan's online AssetPairs metadata, not inferred from price).
- Stablecoin base exclusions: BRL1, BUSD, DAI, EUR, EURC, EUROP, EURQ, EURR, EURT, FDUSD, FRAX, GUSD, PYUSD, QCAD, RLUSD, TGBP, TUSD, USD, USD1, USDC, USDD, USDE, USDG, USDQ, USDR, USDS, USDT, ZUSD.
- DEX: NOT USED; no DEX freshness gate.
- OHLC screening abstentions: 15; details in immutable scan JSON artifact.
- Storage: ledger and results published in one non-force Git commit and read back. Independent artifact recovery is NOT VERIFIED by this scan alone.
- Errors: none in successful committed scan; a failed workflow must not publish a SUCCESS report.

# Cryptoscanner — challenger and independent legacy-inspired WATCH

Paper only · risk is high or higher · 30%+ in 48h probability NOT CALIBRATED
Signal confidence 0–100 means setup strength only, NOT a win probability. Actions are research guidance; no trade authorization.

**Writer:** 45589871629 · **Generation:** 1702 · **Legacy run:** 45589871629
**Main quote time:** 2026-11-25T09:57:23.792702+00:00 · **Legacy report time:** 2026-11-25T09:58:24.695795+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | MON/USD | 0.01019 | 78.66 | +0.00% | 0.36x | MODERATE 54/100 | VERY_HIGH 76/100 | Watch |
| 2 | VVV/USD | 24.77 | 58.83 | +0.85% | 0.72x | MODERATE 59/100 | VERY_HIGH 70/100 | Watch |
| 3 | 2Z/USD | 0.01671 | 37.88 | -1.89% | 1.87x | WEAK 34/100 | VERY_HIGH 83/100 | Do nothing |
| 4 | BABY/USD | 0.00859 | 31.46 | -0.58% | 0.23x | WEAK 6/100 | EXTREME 100/100 | Do nothing |
| 5 | SYRUP/USD | 0.06994 | 28.87 | -0.48% | 1.78x | WEAK 24/100 | EXTREME 85/100 | Do nothing |

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
