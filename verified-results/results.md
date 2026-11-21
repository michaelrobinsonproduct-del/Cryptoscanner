# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-21T00:30:29.987506+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/44844168137
**Source SHA:** bdc7e68f7fa75fae6636b7738d52f10a65d92038
**Previous ledger commit:** c8a3154384d82dcce71b2734a4405716911682a8 (atomic ledger/results publication)
**Ledger generation:** 1046 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 6s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 628; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 610; valid market observations: 608; OHLC screened: 23.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | SOL/USD | 68.92 | 60.143 | 56.414 | +0.31% | +0.29% | 1.23x | 1.5 | 2026-11-21T00:30:23.827803+00:00 | Not calibrated | MODERATE 65/100 | HIGH 62/100 | Watch | WATCH |
| 2 | PEARL/USD | 1.8468 | 55.204 | 45.392 | +1.01% | +1.91% | 1.03x | 20.6 | 2026-11-21T00:30:23.827803+00:00 | Not calibrated | MODERATE 53/100 | VERY_HIGH 74/100 | Watch | WATCH |
| 3 | AKT/USD | 0.5058 | 50.789 | 31.502 | +0.38% | +0.86% | 3.56x | 7.9 | 2026-11-21T00:30:23.827803+00:00 | Not calibrated | STRONG 80/100 | HIGH 60/100 | Watch | WATCH |
| 4 | CAP/USD | 0.092037 | 46.942 | 31.005 | +0.54% | +0.19% | 3.12x | 11.0 | 2026-11-21T00:30:23.827803+00:00 | Not calibrated | MODERATE 63/100 | HIGH 66/100 | Watch | WATCH |
| 5 | DRV/USD | 0.24684 | 45.017 | 38.435 | +0.53% | +0.36% | 1.48x | 1.2 | 2026-11-21T00:30:23.827803+00:00 | Not calibrated | MODERATE 68/100 | HIGH 60/100 | Watch | WATCH |
| 6 | AKE/USD | 0.0061492 | 40.155 | 45.840 | +0.62% | +0.12% | 0.37x | 27.0 | 2026-11-21T00:30:23.827803+00:00 | Not calibrated | WEAK 30/100 | VERY_HIGH 82/100 | Do nothing | WATCH |
| 7 | DCR/USD | 10.139 | 37.064 | 30.148 | +0.34% | +0.26% | 1.56x | 5.9 | 2026-11-21T00:30:23.827803+00:00 | Not calibrated | MODERATE 64/100 | HIGH 67/100 | Watch | WATCH |
| 8 | PIEVERSE/USD | 3.0078 | 27.631 | 31.609 | +0.30% | +0.16% | 0.52x | 10.6 | 2026-11-21T00:30:23.827803+00:00 | Not calibrated | WEAK 29/100 | VERY_HIGH 81/100 | Do nothing | WATCH |
| 9 | BLUR/USD | 0.00733 | 22.008 | 27.996 | +0.41% | +0.27% | 0.26x | 13.7 | 2026-11-21T00:30:23.827803+00:00 | Not calibrated | WEAK 36/100 | VERY_HIGH 81/100 | Watch | WATCH |
| 10 | ZBCN/USD | 0.001597 | 17.635 | 22.141 | +0.38% | -0.19% | 0.64x | 25.1 | 2026-11-21T00:30:23.827803+00:00 | Not calibrated | WEAK 4/100 | EXTREME 93/100 | Do nothing | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | SOL/USD | 56.414 | 68.92 | +0.29% | 1.23x |
| 2 | AKE/USD | 45.840 | 0.0061492 | +0.12% | 0.37x |
| 3 | PEARL/USD | 45.392 | 1.8468 | +1.91% | 1.03x |
| 4 | DRV/USD | 38.435 | 0.24684 | +0.36% | 1.48x |
| 5 | PIEVERSE/USD | 31.609 | 3.0078 | +0.16% | 0.52x |
| 6 | AKT/USD | 31.502 | 0.5058 | +0.86% | 3.56x |
| 7 | CAP/USD | 31.005 | 0.092037 | +0.19% | 3.12x |
| 8 | DCR/USD | 30.148 | 10.139 | +0.26% | 1.56x |
| 9 | BLUR/USD | 27.996 | 0.00733 | +0.27% | 0.26x |
| 10 | ZBCN/USD | 22.141 | 0.001597 | -0.19% | 0.64x |

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

- Persisted scans: 1046; predictions: 8363; observations: 632328.
- Matured sampled outcomes across 1/6/24/48h: 10928; gap abstentions: 19015. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 10 (sampled only; not a success-rate estimate).
- False positives / missed movers: NOT VERIFIED without eligible continuous outcome coverage.
- Baseline vs challenger: recorded as-of; unbiased held-out lift NOT MEASURED.
- Online Kraken /USD stablecoin-base pairs excluded: 18 (counted from this scan's online AssetPairs metadata, not inferred from price).
- Stablecoin base exclusions: BRL1, BUSD, DAI, EUR, EURC, EUROP, EURQ, EURR, EURT, FDUSD, FRAX, GUSD, PYUSD, QCAD, RLUSD, TGBP, TUSD, USD, USD1, USDC, USDD, USDE, USDG, USDQ, USDR, USDS, USDT, ZUSD.
- DEX: NOT USED; no DEX freshness gate.
- OHLC screening abstentions: 13; details in immutable scan JSON artifact.
- Storage: ledger and results published in one non-force Git commit and read back. Independent artifact recovery is NOT VERIFIED by this scan alone.
- Errors: none in successful committed scan; a failed workflow must not publish a SUCCESS report.

# Cryptoscanner — challenger and independent legacy-inspired WATCH

Paper only · risk is high or higher · 30%+ in 48h probability NOT CALIBRATED
Signal confidence 0–100 means setup strength only, NOT a win probability. Actions are research guidance; no trade authorization.

**Writer:** 44844168137 · **Generation:** 1046 · **Legacy run:** 44844168137
**Main quote time:** 2026-11-21T00:30:29.987506+00:00 · **Legacy report time:** 2026-11-21T00:31:31.083497+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | SOL/USD ⭐ | 68.92 | 60.14 | +0.29% | 1.23x | STRONG 75/100 | HIGH 62/100 | Watch |
| 2 | PEARL/USD ⭐ | 1.8468 | 55.20 | +1.91% | 1.03x | MODERATE 63/100 | VERY_HIGH 74/100 | Watch |
| 3 | AKT/USD ⭐ | 0.5058 | 50.79 | +0.86% | 3.56x | STRONG 90/100 | HIGH 60/100 | Consider small entry |
| 4 | CAP/USD ⭐ | 0.092037 | 46.94 | +0.19% | 3.12x | STRONG 73/100 | HIGH 66/100 | Watch |
| 5 | DRV/USD ⭐ | 0.24684 | 45.02 | +0.36% | 1.48x | STRONG 78/100 | HIGH 60/100 | Watch |
| 6 | AKE/USD | 0.0061492 | 40.16 | +0.12% | 0.37x | WEAK 30/100 | VERY_HIGH 82/100 | Do nothing |
| 7 | DCR/USD | 10.139 | 37.06 | +0.26% | 1.56x | MODERATE 64/100 | HIGH 67/100 | Watch |
| 8 | PIEVERSE/USD | 3.0078 | 27.63 | +0.16% | 0.52x | WEAK 29/100 | VERY_HIGH 81/100 | Do nothing |
| 9 | BLUR/USD | 0.00733 | 22.01 | +0.27% | 0.26x | WEAK 36/100 | VERY_HIGH 81/100 | Watch |
| 10 | ZBCN/USD | 0.001597 | 17.63 | -0.19% | 0.64x | WEAK 4/100 | EXTREME 93/100 | Do nothing |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | PEARL/USD ⭐ | 1.8547 | 56.37 | +1.91% | 1.03x | 22081 | MODERATE 68/100 | HIGH 68/100 | Watch |
| 2 | SOL/USD ⭐ | 68.93 | 54.72 | +0.29% | 1.23x | 43583 | STRONG 72/100 | HIGH 62/100 | Watch |
| 3 | CAP/USD ⭐ | 0.092037 | 45.41 | +0.19% | 3.12x | 3837 | STRONG 78/100 | HIGH 60/100 | Watch |
| 4 | AKT/USD ⭐ | 0.5062 | 39.74 | +0.86% | 3.56x | 4589 | STRONG 80/100 | HIGH 66/100 | Consider small entry |
| 5 | DRV/USD ⭐ | 0.2472 | 38.36 | +0.36% | 1.48x | 5958 | STRONG 74/100 | HIGH 60/100 | Watch |

**Same-run overlap:** SOL/USD, PEARL/USD, AKT/USD, CAP/USD, DRV/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
