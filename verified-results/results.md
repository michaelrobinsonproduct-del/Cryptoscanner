# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-22T11:41:11.088464+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/45018398669
**Source SHA:** 4066e028afbd46ef7ad268722dcaaaa2ca6a4e7e
**Previous ledger commit:** 5ece8742cc2eac0e7a5f9cea3da1781d8013c8f4 (atomic ledger/results publication)
**Ledger generation:** 1277 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 6s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 628; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 610; valid market observations: 609; OHLC screened: 24.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | CRV/USD | 0.18664 | 89.630 | 72.966 | +4.64% | +0.33% | 4.31x | 9.6 | 2026-11-22T11:41:05.194935+00:00 | Not calibrated | STRONG 100/100 | HIGH 55/100 | Consider small entry | WATCH |
| 2 | NIGHT/USD | 0.04631 | 87.485 | 67.603 | +4.58% | +0.98% | 2.95x | 19.4 | 2026-11-22T11:41:05.194935+00:00 | Not calibrated | STRONG 94/100 | HIGH 61/100 | Consider small entry | WATCH |
| 3 | NEAR/USD | 2.9871 | 86.368 | 76.601 | +3.49% | +0.02% | 1.97x | 5.7 | 2026-11-22T11:41:05.194935+00:00 | Not calibrated | STRONG 78/100 | HIGH 55/100 | Watch | WATCH |
| 4 | ETH/USD | 1705.37 | 79.297 | 64.579 | +1.37% | -0.06% | 2.59x | 0.1 | 2026-11-22T11:41:05.194935+00:00 | Not calibrated | STRONG 70/100 | HIGH 61/100 | Watch | WATCH |
| 5 | ZEC/USD | 798.47 | 69.270 | 70.754 | +2.61% | +0.27% | 0.72x | 5.0 | 2026-11-22T11:41:05.194935+00:00 | Not calibrated | MODERATE 65/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 6 | PUMP/USD | 0.002482 | 66.219 | 77.052 | +5.89% | -0.84% | 0.34x | 12.1 | 2026-11-22T11:41:05.194935+00:00 | Not calibrated | WEAK 33/100 | VERY_HIGH 82/100 | Do nothing | WATCH |
| 7 | INJ/USD | 6.25 | 65.635 | 72.284 | +4.64% | +0.29% | 0.19x | 4.8 | 2026-11-22T11:41:05.194935+00:00 | Not calibrated | MODERATE 63/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 8 | HYPE/USD | 62.44 | 60.824 | 67.115 | +1.96% | +0.10% | 0.32x | 3.2 | 2026-11-22T11:41:05.194935+00:00 | Not calibrated | MODERATE 50/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 9 | TAO/USD | 190.0788 | 60.344 | 67.858 | +2.34% | -0.21% | 0.35x | 5.8 | 2026-11-22T11:41:05.194935+00:00 | Not calibrated | WEAK 35/100 | VERY_HIGH 76/100 | Watch | WATCH |
| 10 | XBT/USD | 60939.1 | 60.277 | 64.884 | +1.41% | +0.16% | 0.46x | 0.0 | 2026-11-22T11:41:05.194935+00:00 | Not calibrated | MODERATE 50/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 11 | AVAX/USD | 6.693 | 60.110 | 55.801 | +1.98% | -0.13% | 1.50x | 3.0 | 2026-11-22T11:41:05.194935+00:00 | Not calibrated | MODERATE 50/100 | HIGH 61/100 | Watch | WATCH |
| 12 | SUI/USD | 0.6601 | 60.105 | 67.327 | +1.98% | +0.00% | 0.28x | 3.0 | 2026-11-22T11:41:05.194935+00:00 | Not calibrated | MODERATE 50/100 | VERY_HIGH 70/100 | Watch | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | PUMP/USD | 77.052 | 0.002482 | -0.84% | 0.34x |
| 2 | NEAR/USD | 76.601 | 2.9871 | +0.02% | 1.97x |
| 3 | CRV/USD | 72.966 | 0.18664 | +0.33% | 4.31x |
| 4 | INJ/USD | 72.284 | 6.25 | +0.29% | 0.19x |
| 5 | ZEC/USD | 70.754 | 798.47 | +0.27% | 0.72x |
| 6 | TAO/USD | 67.858 | 190.0788 | -0.21% | 0.35x |
| 7 | NIGHT/USD | 67.603 | 0.04631 | +0.98% | 2.95x |
| 8 | SUI/USD | 67.327 | 0.6601 | +0.00% | 0.28x |
| 9 | HYPE/USD | 67.115 | 62.44 | +0.10% | 0.32x |
| 10 | XBT/USD | 64.884 | 60939.1 | +0.16% | 0.46x |
| 11 | ETH/USD | 64.579 | 1705.37 | -0.06% | 2.59x |
| 12 | AVAX/USD | 55.801 | 6.693 | -0.13% | 1.50x |

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

- Persisted scans: 1277; predictions: 10244; observations: 772802.
- Matured sampled outcomes across 1/6/24/48h: 14790; gap abstentions: 22219. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 60 (sampled only; not a success-rate estimate).
- False positives / missed movers: NOT VERIFIED without eligible continuous outcome coverage.
- Baseline vs challenger: recorded as-of; unbiased held-out lift NOT MEASURED.
- Online Kraken /USD stablecoin-base pairs excluded: 18 (counted from this scan's online AssetPairs metadata, not inferred from price).
- Stablecoin base exclusions: BRL1, BUSD, DAI, EUR, EURC, EUROP, EURQ, EURR, EURT, FDUSD, FRAX, GUSD, PYUSD, QCAD, RLUSD, TGBP, TUSD, USD, USD1, USDC, USDD, USDE, USDG, USDQ, USDR, USDS, USDT, ZUSD.
- DEX: NOT USED; no DEX freshness gate.
- OHLC screening abstentions: 4; details in immutable scan JSON artifact.
- Storage: ledger and results published in one non-force Git commit and read back. Independent artifact recovery is NOT VERIFIED by this scan alone.
- Errors: none in successful committed scan; a failed workflow must not publish a SUCCESS report.

# Cryptoscanner — challenger and independent legacy-inspired WATCH

Paper only · risk is high or higher · 30%+ in 48h probability NOT CALIBRATED
Signal confidence 0–100 means setup strength only, NOT a win probability. Actions are research guidance; no trade authorization.

**Writer:** 45018398669 · **Generation:** 1277 · **Legacy run:** 45018398669
**Main quote time:** 2026-11-22T11:41:11.088464+00:00 · **Legacy report time:** 2026-11-22T11:42:14.110639+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | CRV/USD ⭐ | 0.18664 | 89.63 | +0.33% | 4.31x | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 2 | NIGHT/USD ⭐ | 0.04631 | 87.48 | +0.98% | 2.95x | STRONG 100/100 | HIGH 61/100 | Consider small entry |
| 3 | NEAR/USD | 2.9871 | 86.37 | +0.02% | 1.97x | STRONG 78/100 | HIGH 55/100 | Watch |
| 4 | ETH/USD | 1705.37 | 79.30 | -0.06% | 2.59x | STRONG 70/100 | HIGH 61/100 | Watch |
| 5 | ZEC/USD | 798.47 | 69.27 | +0.27% | 0.72x | MODERATE 65/100 | VERY_HIGH 70/100 | Watch |
| 6 | PUMP/USD | 0.002482 | 66.22 | -0.84% | 0.34x | WEAK 33/100 | VERY_HIGH 82/100 | Do nothing |
| 7 | INJ/USD | 6.25 | 65.64 | +0.29% | 0.19x | MODERATE 63/100 | VERY_HIGH 70/100 | Watch |
| 8 | HYPE/USD | 62.44 | 60.82 | +0.10% | 0.32x | MODERATE 50/100 | VERY_HIGH 70/100 | Watch |
| 9 | TAO/USD | 190.0788 | 60.34 | -0.21% | 0.35x | WEAK 35/100 | VERY_HIGH 76/100 | Watch |
| 10 | XBT/USD | 60939.1 | 60.28 | +0.16% | 0.46x | MODERATE 50/100 | VERY_HIGH 70/100 | Watch |
| 11 | AVAX/USD | 6.693 | 60.11 | -0.13% | 1.50x | MODERATE 50/100 | HIGH 61/100 | Watch |
| 12 | SUI/USD | 0.6601 | 60.11 | +0.00% | 0.28x | MODERATE 50/100 | VERY_HIGH 70/100 | Watch |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | NIGHT/USD ⭐ | 0.0464 | 89.88 | +0.98% | 2.95x | 8802 | STRONG 100/100 | HIGH 61/100 | Consider small entry |
| 2 | CRV/USD ⭐ | 0.18649 | 88.17 | +0.33% | 4.31x | 6759 | STRONG 100/100 | HIGH 61/100 | Consider small entry |

**Same-run overlap:** CRV/USD, NIGHT/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
