# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-25T22:56:43.479594+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/45717132725
**Source SHA:** 858c8bc8ec5d7641ddb39cacd8aca91719f855b1
**Previous ledger commit:** 10a453c2732ee28ec64b7a928f30cb88b5391503 (atomic ledger/results publication)
**Ledger generation:** 1778 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 8s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 628; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 610; valid market observations: 609; OHLC screened: 24.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | LTC/USD | 42.53 | 81.882 | 82.612 | +4.11% | +0.24% | 0.81x | 2.4 | 2026-11-25T22:56:35.378529+00:00 | Not calibrated | STRONG 71/100 | HIGH 62/100 | Watch | WATCH |
| 2 | NEAR/USD | 3.0243 | 77.148 | 87.438 | +4.85% | -0.47% | 0.21x | 3.0 | 2026-11-25T22:56:35.378529+00:00 | Not calibrated | WEAK 44/100 | VERY_HIGH 76/100 | Watch | WATCH |
| 3 | PUMP/USD | 0.002549 | 69.950 | 73.090 | +4.51% | -0.04% | 0.71x | 3.9 | 2026-11-25T22:56:35.378529+00:00 | Not calibrated | WEAK 40/100 | VERY_HIGH 76/100 | Watch | WATCH |
| 4 | HYPE/USD | 61.46 | 65.235 | 72.777 | +2.66% | +0.00% | 0.25x | 1.6 | 2026-11-25T22:56:35.378529+00:00 | Not calibrated | MODERATE 53/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 5 | SUI/USD | 0.6635 | 64.701 | 71.544 | +2.47% | +0.08% | 0.28x | 1.5 | 2026-11-25T22:56:35.378529+00:00 | Not calibrated | MODERATE 52/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 6 | XBT/USD | 60056.2 | 63.041 | 58.681 | +0.53% | -0.16% | 1.52x | 0.0 | 2026-11-25T22:56:35.378529+00:00 | Not calibrated | MODERATE 52/100 | HIGH 61/100 | Watch | WATCH |
| 7 | ZEC/USD | 754.2 | 61.342 | 68.179 | +2.07% | -0.30% | 0.47x | 2.7 | 2026-11-25T22:56:35.378529+00:00 | Not calibrated | WEAK 36/100 | VERY_HIGH 76/100 | Watch | WATCH |
| 8 | PAXG/USD | 3579.51 | 60.380 | 62.212 | +1.06% | -0.00% | 0.82x | 0.5 | 2026-11-25T22:56:35.378529+00:00 | Not calibrated | WEAK 35/100 | HIGH 68/100 | Watch | WATCH |
| 9 | XMR/USD | 520.95 | 60.285 | 68.094 | +2.23% | +0.05% | 0.19x | 5.0 | 2026-11-25T22:56:35.378529+00:00 | Not calibrated | MODERATE 50/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 10 | XRP/USD | 0.93602 | 59.828 | 64.352 | +1.34% | -0.13% | 0.61x | 0.1 | 2026-11-25T22:56:35.378529+00:00 | Not calibrated | WEAK 35/100 | VERY_HIGH 76/100 | Watch | WATCH |
| 11 | XLM/USD | 0.12769 | 58.095 | 63.122 | +2.93% | -0.03% | 0.51x | 2.7 | 2026-11-25T22:56:35.378529+00:00 | Not calibrated | WEAK 34/100 | VERY_HIGH 76/100 | Do nothing | WATCH |
| 12 | SOL/USD | 70.47 | 57.511 | 63.041 | +1.25% | +0.04% | 0.43x | 1.4 | 2026-11-25T22:56:35.378529+00:00 | Not calibrated | MODERATE 49/100 | VERY_HIGH 70/100 | Watch | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | NEAR/USD | 87.438 | 3.0243 | -0.47% | 0.21x |
| 2 | LTC/USD | 82.612 | 42.53 | +0.24% | 0.81x |
| 3 | PUMP/USD | 73.090 | 0.002549 | -0.04% | 0.71x |
| 4 | HYPE/USD | 72.777 | 61.46 | +0.00% | 0.25x |
| 5 | SUI/USD | 71.544 | 0.6635 | +0.08% | 0.28x |
| 6 | ZEC/USD | 68.179 | 754.2 | -0.30% | 0.47x |
| 7 | XMR/USD | 68.094 | 520.95 | +0.05% | 0.19x |
| 8 | XRP/USD | 64.352 | 0.93602 | -0.13% | 0.61x |
| 9 | XLM/USD | 63.122 | 0.12769 | -0.03% | 0.51x |
| 10 | SOL/USD | 63.041 | 70.47 | +0.04% | 0.43x |
| 11 | PAXG/USD | 62.212 | 3579.51 | -0.00% | 0.82x |
| 12 | XBT/USD | 58.681 | 60056.2 | -0.16% | 1.52x |

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

- Persisted scans: 1778; predictions: 15080; observations: 1077846.
- Matured sampled outcomes across 1/6/24/48h: 32834; gap abstentions: 23317. Per-horizon counts require independent audit; do not infer held-out lift.
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

**Writer:** 45717132725 · **Generation:** 1778 · **Legacy run:** 45717132725
**Main quote time:** 2026-11-25T22:56:43.479594+00:00 · **Legacy report time:** 2026-11-25T22:57:39.595139+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | LTC/USD | 42.53 | 81.88 | +0.24% | 0.81x | STRONG 71/100 | HIGH 62/100 | Watch |
| 2 | NEAR/USD | 3.0243 | 77.15 | -0.47% | 0.21x | WEAK 44/100 | VERY_HIGH 76/100 | Watch |
| 3 | PUMP/USD | 0.002549 | 69.95 | -0.04% | 0.71x | WEAK 40/100 | VERY_HIGH 76/100 | Watch |
| 4 | HYPE/USD | 61.46 | 65.23 | +0.00% | 0.25x | MODERATE 53/100 | VERY_HIGH 70/100 | Watch |
| 5 | SUI/USD | 0.6635 | 64.70 | +0.08% | 0.28x | MODERATE 52/100 | VERY_HIGH 70/100 | Watch |
| 6 | XBT/USD | 60056.2 | 63.04 | -0.16% | 1.52x | MODERATE 52/100 | HIGH 61/100 | Watch |
| 7 | ZEC/USD | 754.2 | 61.34 | -0.30% | 0.47x | WEAK 36/100 | VERY_HIGH 76/100 | Watch |
| 8 | PAXG/USD | 3579.51 | 60.38 | -0.00% | 0.82x | WEAK 35/100 | HIGH 68/100 | Watch |
| 9 | XMR/USD | 520.95 | 60.28 | +0.05% | 0.19x | MODERATE 50/100 | VERY_HIGH 70/100 | Watch |
| 10 | XRP/USD | 0.93602 | 59.83 | -0.13% | 0.61x | WEAK 35/100 | VERY_HIGH 76/100 | Watch |
| 11 | XLM/USD | 0.12769 | 58.10 | -0.03% | 0.51x | WEAK 34/100 | VERY_HIGH 76/100 | Do nothing |
| 12 | SOL/USD | 70.47 | 57.51 | +0.04% | 0.43x | MODERATE 49/100 | VERY_HIGH 70/100 | Watch |

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
