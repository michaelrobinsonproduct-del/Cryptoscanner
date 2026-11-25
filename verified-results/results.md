# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-25T11:32:32.483448+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/45604922843
**Source SHA:** 858c8bc8ec5d7641ddb39cacd8aca91719f855b1
**Previous ledger commit:** 59b285b62292bf51a16175821863e41f348c21d2 (atomic ledger/results publication)
**Ledger generation:** 1712 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 5s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 627; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 609; valid market observations: 608; OHLC screened: 14.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | MON/USD | 0.00991 | 73.805 | 76.297 | +4.65% | +0.30% | 0.60x | 10.1 | 2026-11-25T11:32:27.360551+00:00 | Not calibrated | MODERATE 62/100 | VERY_HIGH 76/100 | Watch | WATCH |
| 2 | DRV/USD | 0.33705 | 72.926 | 77.521 | +7.25% | -0.86% | 0.97x | 11.0 | 2026-11-25T11:32:27.360551+00:00 | Not calibrated | WEAK 36/100 | VERY_HIGH 74/100 | Watch | WATCH |
| 3 | VVV/USD | 24.845 | 45.742 | 55.712 | +1.25% | -0.65% | 0.33x | 16.1 | 2026-11-25T11:32:27.360551+00:00 | Not calibrated | WEAK 23/100 | VERY_HIGH 82/100 | Do nothing | WATCH |
| 4 | BABY/USD | 0.00853 | 40.497 | 36.747 | +3.27% | -0.12% | 1.43x | 35.2 | 2026-11-25T11:32:27.360551+00:00 | Not calibrated | WEAK 25/100 | EXTREME 85/100 | Do nothing | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | DRV/USD | 77.521 | 0.33705 | -0.86% | 0.97x |
| 2 | MON/USD | 76.297 | 0.00991 | +0.30% | 0.60x |
| 3 | VVV/USD | 55.712 | 24.845 | -0.65% | 0.33x |
| 4 | BABY/USD | 36.747 | 0.00853 | -0.12% | 1.43x |

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

- Persisted scans: 1712; predictions: 14477; observations: 1037681.
- Matured sampled outcomes across 1/6/24/48h: 31507; gap abstentions: 22370. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 146 (sampled only; not a success-rate estimate).
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

**Writer:** 45604922843 · **Generation:** 1712 · **Legacy run:** 45604922843
**Main quote time:** 2026-11-25T11:32:32.483448+00:00 · **Legacy report time:** 2026-11-25T11:33:48.430232+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | MON/USD | 0.00991 | 73.80 | +0.30% | 0.60x | MODERATE 62/100 | VERY_HIGH 76/100 | Watch |
| 2 | DRV/USD | 0.33705 | 72.93 | -0.86% | 0.97x | WEAK 36/100 | VERY_HIGH 74/100 | Watch |
| 3 | VVV/USD | 24.845 | 45.74 | -0.65% | 0.33x | WEAK 23/100 | VERY_HIGH 82/100 | Do nothing |
| 4 | BABY/USD | 0.00853 | 40.50 | -0.12% | 1.43x | WEAK 25/100 | EXTREME 85/100 | Do nothing |

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
