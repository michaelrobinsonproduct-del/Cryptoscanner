# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-21T17:41:08.951894+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/44931247413
**Source SHA:** 7ac7b40f8385b7b363a3015feba153e001ac4fc4
**Previous ledger commit:** 9d00b599bd1f1cd0e9d176cc3c46fcb826d85d30 (atomic ledger/results publication)
**Ledger generation:** 1165 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 8s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 628; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 610; valid market observations: 608; OHLC screened: 24.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | XMR/USD | 481.57 | 105.751 | 91.706 | +5.54% | -0.19% | 2.62x | 4.2 | 2026-11-21T17:41:00.541271+00:00 | Not calibrated | STRONG 80/100 | HIGH 61/100 | Watch | WATCH |
| 2 | UNI/USD | 4.716 | 91.201 | 91.864 | +5.57% | -0.70% | 1.28x | 4.2 | 2026-11-21T17:41:00.541271+00:00 | Not calibrated | MODERATE 56/100 | HIGH 61/100 | Watch | WATCH |
| 3 | NIGHT/USD | 0.04533 | 89.213 | 89.646 | +7.37% | +0.29% | 0.81x | 4.4 | 2026-11-21T17:41:00.541271+00:00 | Not calibrated | STRONG 75/100 | HIGH 62/100 | Watch | WATCH |
| 4 | XRP/USD | 0.93215 | 87.796 | 72.574 | +2.58% | +0.07% | 2.49x | 1.0 | 2026-11-21T17:41:00.541271+00:00 | Not calibrated | STRONG 89/100 | HIGH 55/100 | Watch | WATCH |
| 5 | ETH/USD | 1675.35 | 73.694 | 79.191 | +3.46% | -0.36% | 0.63x | 0.1 | 2026-11-21T17:41:00.541271+00:00 | Not calibrated | WEAK 42/100 | VERY_HIGH 76/100 | Watch | WATCH |
| 6 | BEAM/USD | 0.003475 | 71.644 | 69.706 | +6.01% | -0.86% | 1.62x | 8.6 | 2026-11-21T17:41:00.541271+00:00 | Not calibrated | MODERATE 56/100 | HIGH 66/100 | Watch | WATCH |
| 7 | SOL/USD | 70.44 | 71.194 | 71.205 | +2.52% | -0.33% | 1.16x | 2.8 | 2026-11-21T17:41:00.541271+00:00 | Not calibrated | MODERATE 46/100 | HIGH 68/100 | Watch | WATCH |
| 8 | ZEC/USD | 780.85 | 69.820 | 74.714 | +3.03% | -0.81% | 0.92x | 2.9 | 2026-11-21T17:41:00.541271+00:00 | Not calibrated | WEAK 40/100 | HIGH 68/100 | Watch | WATCH |
| 9 | TRX/USD | 0.304736 | 68.857 | 54.110 | +1.07% | -0.05% | 7.84x | 0.7 | 2026-11-21T17:41:00.541271+00:00 | Not calibrated | MODERATE 64/100 | HIGH 61/100 | Watch | WATCH |
| 10 | TAO/USD | 185.7833 | 66.004 | 71.183 | +2.92% | -0.17% | 0.57x | 8.5 | 2026-11-21T17:41:00.541271+00:00 | Not calibrated | WEAK 38/100 | VERY_HIGH 76/100 | Watch | WATCH |
| 11 | XDG/USD | 0.0551242 | 64.876 | 65.744 | +1.56% | -0.16% | 0.99x | 0.4 | 2026-11-21T17:41:00.541271+00:00 | Not calibrated | WEAK 37/100 | HIGH 68/100 | Watch | WATCH |
| 12 | BNB/USD | 546.57 | 64.655 | 57.132 | +1.28% | -0.16% | 1.83x | 0.2 | 2026-11-21T17:41:00.541271+00:00 | Not calibrated | MODERATE 52/100 | HIGH 61/100 | Watch | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | UNI/USD | 91.864 | 4.716 | -0.70% | 1.28x |
| 2 | XMR/USD | 91.706 | 481.57 | -0.19% | 2.62x |
| 3 | NIGHT/USD | 89.646 | 0.04533 | +0.29% | 0.81x |
| 4 | ETH/USD | 79.191 | 1675.35 | -0.36% | 0.63x |
| 5 | ZEC/USD | 74.714 | 780.85 | -0.81% | 0.92x |
| 6 | XRP/USD | 72.574 | 0.93215 | +0.07% | 2.49x |
| 7 | SOL/USD | 71.205 | 70.44 | -0.33% | 1.16x |
| 8 | TAO/USD | 71.183 | 185.7833 | -0.17% | 0.57x |
| 9 | BEAM/USD | 69.706 | 0.003475 | -0.86% | 1.62x |
| 10 | XDG/USD | 65.744 | 0.0551242 | -0.16% | 0.99x |
| 11 | BNB/USD | 57.132 | 546.57 | -0.16% | 1.83x |
| 12 | TRX/USD | 54.110 | 0.304736 | -0.05% | 7.84x |

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

- Persisted scans: 1165; predictions: 9289; observations: 704679.
- Matured sampled outcomes across 1/6/24/48h: 12234; gap abstentions: 20968. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 16 (sampled only; not a success-rate estimate).
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

**Writer:** 44931247413 · **Generation:** 1165 · **Legacy run:** 44931247413
**Main quote time:** 2026-11-21T17:41:08.951894+00:00 · **Legacy report time:** 2026-11-21T17:42:02.117648+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | XMR/USD | 481.57 | 105.75 | -0.19% | 2.62x | STRONG 80/100 | HIGH 61/100 | Watch |
| 2 | UNI/USD | 4.716 | 91.20 | -0.70% | 1.28x | MODERATE 56/100 | HIGH 61/100 | Watch |
| 3 | NIGHT/USD | 0.04533 | 89.21 | +0.29% | 0.81x | STRONG 75/100 | HIGH 62/100 | Watch |
| 4 | XRP/USD ⭐ | 0.93215 | 87.80 | +0.07% | 2.49x | STRONG 99/100 | HIGH 55/100 | Watch |
| 5 | ETH/USD | 1675.35 | 73.69 | -0.36% | 0.63x | WEAK 42/100 | VERY_HIGH 76/100 | Watch |
| 6 | BEAM/USD | 0.003475 | 71.64 | -0.86% | 1.62x | MODERATE 56/100 | HIGH 66/100 | Watch |
| 7 | SOL/USD | 70.44 | 71.19 | -0.33% | 1.16x | MODERATE 46/100 | HIGH 68/100 | Watch |
| 8 | ZEC/USD | 780.85 | 69.82 | -0.81% | 0.92x | WEAK 40/100 | HIGH 68/100 | Watch |
| 9 | TRX/USD | 0.304736 | 68.86 | -0.05% | 7.84x | MODERATE 64/100 | HIGH 61/100 | Watch |
| 10 | TAO/USD | 185.7833 | 66.00 | -0.17% | 0.57x | WEAK 38/100 | VERY_HIGH 76/100 | Watch |
| 11 | XDG/USD | 0.0551242 | 64.88 | -0.16% | 0.99x | WEAK 37/100 | HIGH 68/100 | Watch |
| 12 | BNB/USD | 546.57 | 64.65 | -0.16% | 1.83x | MODERATE 52/100 | HIGH 61/100 | Watch |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | XRP/USD ⭐ | 0.93244 | 86.27 | +0.07% | 2.49x | 61656 | STRONG 98/100 | HIGH 55/100 | Watch |
| 2 | PIEVERSE/USD | 3.3837 | 80.59 | +1.24% | 2.85x | 2288 | STRONG 80/100 | VERY_HIGH 82/100 | Watch |

**Same-run overlap:** XRP/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
