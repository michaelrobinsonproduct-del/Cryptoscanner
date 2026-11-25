# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-25T16:57:58.784850+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/45659007435
**Source SHA:** 858c8bc8ec5d7641ddb39cacd8aca91719f855b1
**Previous ledger commit:** 10cf10c247c40bc626517e06f58dc7325b6c1d3e (atomic ledger/results publication)
**Ledger generation:** 1741 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 3s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 627; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 609; valid market observations: 608; OHLC screened: 11.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | XPL/USD | 0.0461 | 58.737 | 58.379 | +4.77% | +0.44% | 0.82x | 21.7 | 2026-11-25T16:57:55.753797+00:00 | Not calibrated | MODERATE 49/100 | VERY_HIGH 79/100 | Watch | WATCH |
| 2 | VVV/USD | 25.052 | 57.911 | 65.231 | +2.09% | +0.27% | 0.14x | 6.8 | 2026-11-25T16:57:55.753797+00:00 | Not calibrated | MODERATE 59/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 3 | PIEVERSE/USD | 3.3277 | 56.515 | 54.392 | +8.03% | +1.31% | 0.56x | 44.9 | 2026-11-25T16:57:55.753797+00:00 | Not calibrated | WEAK 43/100 | EXTREME 97/100 | Do nothing | WATCH |
| 4 | DRV/USD | 0.32866 | 55.241 | 60.543 | +4.58% | +0.49% | 0.23x | 18.9 | 2026-11-25T16:57:55.753797+00:00 | Not calibrated | MODERATE 53/100 | VERY_HIGH 76/100 | Watch | WATCH |
| 5 | CAP/USD | 0.092674 | 16.546 | 24.893 | +0.28% | -0.93% | 0.63x | 17.0 | 2026-11-25T16:57:55.753797+00:00 | Not calibrated | WEAK 8/100 | EXTREME 94/100 | Do nothing | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | VVV/USD | 65.231 | 25.052 | +0.27% | 0.14x |
| 2 | DRV/USD | 60.543 | 0.32866 | +0.49% | 0.23x |
| 3 | XPL/USD | 58.379 | 0.0461 | +0.44% | 0.82x |
| 4 | PIEVERSE/USD | 54.392 | 3.3277 | +1.31% | 0.56x |
| 5 | CAP/USD | 24.893 | 0.092674 | -0.93% | 0.63x |

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

- Persisted scans: 1741; predictions: 14640; observations: 1055313.
- Matured sampled outcomes across 1/6/24/48h: 32504; gap abstentions: 22458. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 146 (sampled only; not a success-rate estimate).
- False positives / missed movers: NOT VERIFIED without eligible continuous outcome coverage.
- Baseline vs challenger: recorded as-of; unbiased held-out lift NOT MEASURED.
- Online Kraken /USD stablecoin-base pairs excluded: 18 (counted from this scan's online AssetPairs metadata, not inferred from price).
- Stablecoin base exclusions: BRL1, BUSD, DAI, EUR, EURC, EUROP, EURQ, EURR, EURT, FDUSD, FRAX, GUSD, PYUSD, QCAD, RLUSD, TGBP, TUSD, USD, USD1, USDC, USDD, USDE, USDG, USDQ, USDR, USDS, USDT, ZUSD.
- DEX: NOT USED; no DEX freshness gate.
- OHLC screening abstentions: 6; details in immutable scan JSON artifact.
- Storage: ledger and results published in one non-force Git commit and read back. Independent artifact recovery is NOT VERIFIED by this scan alone.
- Errors: none in successful committed scan; a failed workflow must not publish a SUCCESS report.

# Cryptoscanner — challenger and independent legacy-inspired WATCH

Paper only · risk is high or higher · 30%+ in 48h probability NOT CALIBRATED
Signal confidence 0–100 means setup strength only, NOT a win probability. Actions are research guidance; no trade authorization.

**Writer:** 45659007435 · **Generation:** 1741 · **Legacy run:** 45659007435
**Main quote time:** 2026-11-25T16:57:58.784850+00:00 · **Legacy report time:** 2026-11-25T16:59:14.339033+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | XPL/USD | 0.0461 | 58.74 | +0.44% | 0.82x | MODERATE 49/100 | VERY_HIGH 79/100 | Watch |
| 2 | VVV/USD | 25.052 | 57.91 | +0.27% | 0.14x | MODERATE 59/100 | VERY_HIGH 70/100 | Watch |
| 3 | PIEVERSE/USD | 3.3277 | 56.52 | +1.31% | 0.56x | WEAK 43/100 | EXTREME 97/100 | Do nothing |
| 4 | DRV/USD | 0.32866 | 55.24 | +0.49% | 0.23x | MODERATE 53/100 | VERY_HIGH 76/100 | Watch |
| 5 | CAP/USD | 0.092674 | 16.55 | -0.93% | 0.63x | WEAK 8/100 | EXTREME 94/100 | Do nothing |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | MON/USD | 0.01086 | 87.73 | +2.35% | 1.64x | 14098 | STRONG 74/100 | HIGH 67/100 | Watch |
| 2 | ASTER/USD | 0.48208 | 37.50 | +0.42% | 1.31x | 2911 | MODERATE 64/100 | HIGH 60/100 | Watch |

**Same-run overlap:** None
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
