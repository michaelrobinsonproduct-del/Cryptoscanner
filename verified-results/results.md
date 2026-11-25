# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-25T18:35:47.846272+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/45676550526
**Source SHA:** 858c8bc8ec5d7641ddb39cacd8aca91719f855b1
**Previous ledger commit:** 14606c84d4f995c68c356998f5c9d4e68d57f9fc (atomic ledger/results publication)
**Ledger generation:** 1751 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 9s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 628; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 610; valid market observations: 609; OHLC screened: 24.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | VVV/USD | 26.49 | 88.294 | 95.658 | +7.96% | -0.31% | 0.42x | 8.7 | 2026-11-25T18:35:39.275943+00:00 | Not calibrated | MODERATE 49/100 | VERY_HIGH 76/100 | Watch | WATCH |
| 2 | DRV/USD | 0.3499 | 82.034 | 82.548 | +11.33% | -0.09% | 0.99x | 3.1 | 2026-11-25T18:35:39.275943+00:00 | Not calibrated | MODERATE 46/100 | HIGH 68/100 | Watch | WATCH |
| 3 | XPL/USD | 0.0477 | 65.027 | 71.168 | +8.41% | -1.66% | 1.22x | 21.0 | 2026-11-25T18:35:39.275943+00:00 | Not calibrated | WEAK 33/100 | EXTREME 89/100 | Do nothing | WATCH |
| 4 | HYPE/USD | 60.24 | 60.891 | 57.666 | +0.62% | -0.94% | 1.79x | 3.3 | 2026-11-25T18:35:39.275943+00:00 | Not calibrated | MODERATE 50/100 | HIGH 61/100 | Watch | WATCH |
| 5 | LTC/USD | 41.63 | 56.297 | 65.964 | +1.91% | -0.91% | 0.49x | 4.8 | 2026-11-25T18:35:39.275943+00:00 | Not calibrated | WEAK 33/100 | VERY_HIGH 76/100 | Do nothing | WATCH |
| 6 | LINK/USD | 8.8911 | 55.316 | 47.462 | +0.56% | -0.70% | 2.13x | 3.5 | 2026-11-25T18:35:39.275943+00:00 | Not calibrated | MODERATE 58/100 | HIGH 61/100 | Watch | WATCH |
| 7 | XMR/USD | 514.41 | 52.562 | 56.358 | +0.94% | -0.08% | 0.66x | 10.5 | 2026-11-25T18:35:39.275943+00:00 | Not calibrated | WEAK 26/100 | VERY_HIGH 82/100 | Do nothing | WATCH |
| 8 | SUI/USD | 0.6508 | 52.477 | 57.031 | +0.51% | -0.99% | 1.04x | 3.1 | 2026-11-25T18:35:39.275943+00:00 | Not calibrated | WEAK 36/100 | HIGH 68/100 | Watch | WATCH |
| 9 | ASTER/USD | 0.49018 | 48.453 | 44.223 | +1.95% | -0.70% | 1.78x | 4.3 | 2026-11-25T18:35:39.275943+00:00 | Not calibrated | WEAK 44/100 | HIGH 66/100 | Watch | WATCH |
| 10 | BCH/USD | 199.48 | 43.234 | 39.756 | +1.17% | -0.65% | 1.67x | 4.5 | 2026-11-25T18:35:39.275943+00:00 | Not calibrated | WEAK 42/100 | HIGH 66/100 | Watch | WATCH |
| 11 | XLM/USD | 0.12547 | 40.314 | 48.819 | +1.14% | -0.78% | 0.54x | 5.1 | 2026-11-25T18:35:39.275943+00:00 | Not calibrated | WEAK 25/100 | VERY_HIGH 76/100 | Do nothing | WATCH |
| 12 | CC/USD | 0.07573 | 39.351 | 38.140 | +0.91% | -0.72% | 1.48x | 5.3 | 2026-11-25T18:35:39.275943+00:00 | Not calibrated | WEAK 40/100 | HIGH 66/100 | Watch | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | VVV/USD | 95.658 | 26.49 | -0.31% | 0.42x |
| 2 | DRV/USD | 82.548 | 0.3499 | -0.09% | 0.99x |
| 3 | XPL/USD | 71.168 | 0.0477 | -1.66% | 1.22x |
| 4 | LTC/USD | 65.964 | 41.63 | -0.91% | 0.49x |
| 5 | HYPE/USD | 57.666 | 60.24 | -0.94% | 1.79x |
| 6 | SUI/USD | 57.031 | 0.6508 | -0.99% | 1.04x |
| 7 | XMR/USD | 56.358 | 514.41 | -0.08% | 0.66x |
| 8 | XLM/USD | 48.819 | 0.12547 | -0.78% | 0.54x |
| 9 | LINK/USD | 47.462 | 8.8911 | -0.70% | 2.13x |
| 10 | ASTER/USD | 44.223 | 0.49018 | -0.70% | 1.78x |
| 11 | BCH/USD | 39.756 | 199.48 | -0.65% | 1.67x |
| 12 | CC/USD | 38.140 | 0.07573 | -0.72% | 1.48x |

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

- Persisted scans: 1751; predictions: 14756; observations: 1061403.
- Matured sampled outcomes across 1/6/24/48h: 32521; gap abstentions: 22693. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 146 (sampled only; not a success-rate estimate).
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

**Writer:** 45676550526 · **Generation:** 1751 · **Legacy run:** 45676550526
**Main quote time:** 2026-11-25T18:35:47.846272+00:00 · **Legacy report time:** 2026-11-25T18:36:37.643110+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | VVV/USD | 26.49 | 88.29 | -0.31% | 0.42x | MODERATE 49/100 | VERY_HIGH 76/100 | Watch |
| 2 | DRV/USD | 0.3499 | 82.03 | -0.09% | 0.99x | MODERATE 46/100 | HIGH 68/100 | Watch |
| 3 | XPL/USD | 0.0477 | 65.03 | -1.66% | 1.22x | WEAK 33/100 | EXTREME 89/100 | Do nothing |
| 4 | HYPE/USD | 60.24 | 60.89 | -0.94% | 1.79x | MODERATE 50/100 | HIGH 61/100 | Watch |
| 5 | LTC/USD | 41.63 | 56.30 | -0.91% | 0.49x | WEAK 33/100 | VERY_HIGH 76/100 | Do nothing |
| 6 | LINK/USD | 8.8911 | 55.32 | -0.70% | 2.13x | MODERATE 58/100 | HIGH 61/100 | Watch |
| 7 | XMR/USD | 514.41 | 52.56 | -0.08% | 0.66x | WEAK 26/100 | VERY_HIGH 82/100 | Do nothing |
| 8 | SUI/USD | 0.6508 | 52.48 | -0.99% | 1.04x | WEAK 36/100 | HIGH 68/100 | Watch |
| 9 | ASTER/USD | 0.49018 | 48.45 | -0.70% | 1.78x | WEAK 44/100 | HIGH 66/100 | Watch |
| 10 | BCH/USD | 199.48 | 43.23 | -0.65% | 1.67x | WEAK 42/100 | HIGH 66/100 | Watch |
| 11 | XLM/USD | 0.12547 | 40.31 | -0.78% | 0.54x | WEAK 25/100 | VERY_HIGH 76/100 | Do nothing |
| 12 | CC/USD | 0.07573 | 39.35 | -0.72% | 1.48x | WEAK 40/100 | HIGH 66/100 | Watch |

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
