# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-25T05:07:26.584757+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/45551049941
**Source SHA:** 858c8bc8ec5d7641ddb39cacd8aca91719f855b1
**Previous ledger commit:** 5b09f3a2a303d7605af30a2f76d19d1df5a999ab (atomic ledger/results publication)
**Ledger generation:** 1673 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 8s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 628; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 610; valid market observations: 609; OHLC screened: 23.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | VVV/USD | 25.002 | 65.511 | 63.839 | +1.89% | +0.51% | 0.91x | 8.8 | 2026-11-25T05:07:18.267936+00:00 | Not calibrated | MODERATE 63/100 | HIGH 62/100 | Watch | WATCH |
| 2 | XMR/USD | 512.72 | 61.671 | 56.429 | +0.61% | +0.29% | 1.38x | 3.1 | 2026-11-25T05:07:18.267936+00:00 | Not calibrated | STRONG 76/100 | HIGH 55/100 | Watch | WATCH |
| 3 | DRV/USD | 0.3319 | 57.607 | 67.182 | +5.61% | -0.52% | 0.30x | 17.5 | 2026-11-25T05:07:18.267936+00:00 | Not calibrated | WEAK 29/100 | VERY_HIGH 82/100 | Do nothing | WATCH |
| 4 | MON/USD | 0.00981 | 57.232 | 68.085 | +3.59% | -1.41% | 0.62x | 10.2 | 2026-11-25T05:07:18.267936+00:00 | Not calibrated | WEAK 29/100 | EXTREME 86/100 | Do nothing | WATCH |
| 5 | CAP/USD | 0.092684 | 46.795 | 31.423 | +0.29% | +0.07% | 3.05x | 5.7 | 2026-11-25T05:07:18.267936+00:00 | Not calibrated | MODERATE 68/100 | HIGH 60/100 | Watch | WATCH |
| 6 | KAS/USD | 0.02621 | 43.907 | 26.607 | +0.34% | +0.46% | 3.05x | 19.1 | 2026-11-25T05:07:18.267936+00:00 | Not calibrated | STRONG 72/100 | HIGH 66/100 | Watch | WATCH |
| 7 | BLESS/USD | 0.017837 | 31.748 | 26.157 | +1.40% | +0.57% | 1.28x | 41.6 | 2026-11-25T05:07:18.267936+00:00 | Not calibrated | WEAK 36/100 | VERY_HIGH 77/100 | Watch | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | MON/USD | 68.085 | 0.00981 | -1.41% | 0.62x |
| 2 | DRV/USD | 67.182 | 0.3319 | -0.52% | 0.30x |
| 3 | VVV/USD | 63.839 | 25.002 | +0.51% | 0.91x |
| 4 | XMR/USD | 56.429 | 512.72 | +0.29% | 1.38x |
| 5 | CAP/USD | 31.423 | 0.092684 | +0.07% | 3.05x |
| 6 | KAS/USD | 26.607 | 0.02621 | +0.46% | 3.05x |
| 7 | BLESS/USD | 26.157 | 0.017837 | +0.57% | 1.28x |

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

- Persisted scans: 1673; predictions: 14210; observations: 1013948.
- Matured sampled outcomes across 1/6/24/48h: 30111; gap abstentions: 22370. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 146 (sampled only; not a success-rate estimate).
- False positives / missed movers: NOT VERIFIED without eligible continuous outcome coverage.
- Baseline vs challenger: recorded as-of; unbiased held-out lift NOT MEASURED.
- Online Kraken /USD stablecoin-base pairs excluded: 18 (counted from this scan's online AssetPairs metadata, not inferred from price).
- Stablecoin base exclusions: BRL1, BUSD, DAI, EUR, EURC, EUROP, EURQ, EURR, EURT, FDUSD, FRAX, GUSD, PYUSD, QCAD, RLUSD, TGBP, TUSD, USD, USD1, USDC, USDD, USDE, USDG, USDQ, USDR, USDS, USDT, ZUSD.
- DEX: NOT USED; no DEX freshness gate.
- OHLC screening abstentions: 16; details in immutable scan JSON artifact.
- Storage: ledger and results published in one non-force Git commit and read back. Independent artifact recovery is NOT VERIFIED by this scan alone.
- Errors: none in successful committed scan; a failed workflow must not publish a SUCCESS report.

# Cryptoscanner — challenger and independent legacy-inspired WATCH

Paper only · risk is high or higher · 30%+ in 48h probability NOT CALIBRATED
Signal confidence 0–100 means setup strength only, NOT a win probability. Actions are research guidance; no trade authorization.

**Writer:** 45551049941 · **Generation:** 1673 · **Legacy run:** 45551049941
**Main quote time:** 2026-11-25T05:07:26.584757+00:00 · **Legacy report time:** 2026-11-25T05:08:28.886154+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | VVV/USD | 25.002 | 65.51 | +0.51% | 0.91x | MODERATE 63/100 | HIGH 62/100 | Watch |
| 2 | XMR/USD ⭐ | 512.72 | 61.67 | +0.29% | 1.38x | STRONG 86/100 | HIGH 55/100 | Watch |
| 3 | DRV/USD | 0.3319 | 57.61 | -0.52% | 0.30x | WEAK 29/100 | VERY_HIGH 82/100 | Do nothing |
| 4 | MON/USD | 0.00981 | 57.23 | -1.41% | 0.62x | WEAK 29/100 | EXTREME 86/100 | Do nothing |
| 5 | CAP/USD ⭐ | 0.092684 | 46.80 | +0.07% | 3.05x | STRONG 78/100 | HIGH 60/100 | Watch |
| 6 | KAS/USD | 0.02621 | 43.91 | +0.46% | 3.05x | STRONG 72/100 | HIGH 66/100 | Watch |
| 7 | BLESS/USD ⭐ | 0.017837 | 31.75 | +0.57% | 1.28x | MODERATE 46/100 | VERY_HIGH 77/100 | Watch |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | XMR/USD ⭐ | 513.42 | 53.65 | +0.29% | 1.38x | 6928 | STRONG 82/100 | HIGH 55/100 | Watch |
| 2 | TRX/USD | 0.308219 | 53.43 | +0.10% | 37.90x | 3495 | STRONG 72/100 | HIGH 55/100 | Watch |
| 3 | BLESS/USD ⭐ | 0.017769 | 41.24 | +0.57% | 1.28x | 3498 | MODERATE 51/100 | VERY_HIGH 77/100 | Watch |
| 4 | CAP/USD ⭐ | 0.092684 | 35.04 | +0.07% | 3.05x | 5320 | MODERATE 68/100 | HIGH 66/100 | Watch |

**Same-run overlap:** XMR/USD, CAP/USD, BLESS/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
