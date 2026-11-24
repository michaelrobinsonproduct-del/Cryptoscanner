# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-24T15:11:59.294795+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/45422224616
**Source SHA:** 858c8bc8ec5d7641ddb39cacd8aca91719f855b1
**Previous ledger commit:** 7ef5bd1b92a3718a68458cb42ff8a80326d56e7c (atomic ledger/results publication)
**Ledger generation:** 1590 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 5s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 628; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 610; valid market observations: 608; OHLC screened: 13.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | VVV/USD | 25.167 | 80.064 | 70.822 | +2.94% | -1.15% | 7.37x | 9.5 | 2026-11-24T15:11:54.634160+00:00 | Not calibrated | STRONG 70/100 | HIGH 65/100 | Watch | WATCH |
| 2 | GBP/USD | 1.31062 | 68.422 | 58.844 | +0.57% | -0.02% | 1.97x | 0.2 | 2026-11-24T15:11:54.634160+00:00 | Not calibrated | MODERATE 54/100 | HIGH 61/100 | Watch | WATCH |
| 3 | XMR/USD | 495.4 | 51.596 | 59.819 | +1.93% | -0.56% | 0.46x | 17.4 | 2026-11-24T15:11:54.634160+00:00 | Not calibrated | WEAK 26/100 | VERY_HIGH 82/100 | Do nothing | WATCH |
| 4 | NIGHT/USD | 0.0484 | 43.117 | 41.762 | +0.52% | -0.43% | 1.35x | 8.3 | 2026-11-24T15:11:54.634160+00:00 | Not calibrated | WEAK 42/100 | HIGH 61/100 | Watch | WATCH |
| 5 | AUD/USD | 0.6647 | 40.315 | 42.879 | +0.32% | -0.08% | 0.78x | 1.2 | 2026-11-24T15:11:54.634160+00:00 | Not calibrated | WEAK 25/100 | HIGH 68/100 | Do nothing | WATCH |
| 6 | 2Z/USD | 0.01615 | 37.614 | 50.007 | +3.19% | -1.46% | 0.49x | 6.2 | 2026-11-24T15:11:54.634160+00:00 | Not calibrated | WEAK 24/100 | EXTREME 92/100 | Do nothing | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | VVV/USD | 70.822 | 25.167 | -1.15% | 7.37x |
| 2 | XMR/USD | 59.819 | 495.4 | -0.56% | 0.46x |
| 3 | GBP/USD | 58.844 | 1.31062 | -0.02% | 1.97x |
| 4 | 2Z/USD | 50.007 | 0.01615 | -1.46% | 0.49x |
| 5 | AUD/USD | 42.879 | 0.6647 | -0.08% | 0.78x |
| 6 | NIGHT/USD | 41.762 | 0.0484 | -0.43% | 1.35x |

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

- Persisted scans: 1590; predictions: 13704; observations: 963403.
- Matured sampled outcomes across 1/6/24/48h: 27075; gap abstentions: 22370. Per-horizon counts require independent audit; do not infer held-out lift.
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

**Writer:** 45422224616 · **Generation:** 1590 · **Legacy run:** 45422224616
**Main quote time:** 2026-11-24T15:11:59.294795+00:00 · **Legacy report time:** 2026-11-24T15:12:56.003010+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | VVV/USD | 25.167 | 80.06 | -1.15% | 7.37x | STRONG 70/100 | HIGH 65/100 | Watch |
| 2 | GBP/USD | 1.31062 | 68.42 | -0.02% | 1.97x | MODERATE 54/100 | HIGH 61/100 | Watch |
| 3 | XMR/USD | 495.4 | 51.60 | -0.56% | 0.46x | WEAK 26/100 | VERY_HIGH 82/100 | Do nothing |
| 4 | NIGHT/USD | 0.0484 | 43.12 | -0.43% | 1.35x | WEAK 42/100 | HIGH 61/100 | Watch |
| 5 | AUD/USD | 0.6647 | 40.32 | -0.08% | 0.78x | WEAK 25/100 | HIGH 68/100 | Do nothing |
| 6 | 2Z/USD | 0.01615 | 37.61 | -1.46% | 0.49x | WEAK 24/100 | EXTREME 92/100 | Do nothing |

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
