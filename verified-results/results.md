# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-24T14:22:07.326127+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/45412821790
**Source SHA:** 858c8bc8ec5d7641ddb39cacd8aca91719f855b1
**Previous ledger commit:** 2aea05b85f5fbcf3cef1446fdc05c2759d947889 (atomic ledger/results publication)
**Ledger generation:** 1585 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 5s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 628; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 610; valid market observations: 608; OHLC screened: 13.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | XMR/USD | 496.41 | 80.804 | 64.827 | +2.14% | +0.20% | 4.50x | 10.3 | 2026-11-24T14:22:02.190247+00:00 | Not calibrated | STRONG 80/100 | HIGH 61/100 | Watch | WATCH |
| 2 | 2Z/USD | 0.01631 | 76.534 | 57.208 | +4.22% | +0.87% | 2.75x | 6.1 | 2026-11-24T14:22:02.190247+00:00 | Not calibrated | STRONG 93/100 | HIGH 67/100 | Consider small entry | WATCH |
| 3 | VVV/USD | 25.436 | 73.036 | 78.963 | +4.04% | +0.13% | 0.34x | 8.7 | 2026-11-24T14:22:02.190247+00:00 | Not calibrated | MODERATE 57/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 4 | GBP/USD | 1.31031 | 64.236 | 58.639 | +0.54% | -0.00% | 1.56x | 0.3 | 2026-11-24T14:22:02.190247+00:00 | Not calibrated | MODERATE 52/100 | HIGH 61/100 | Watch | WATCH |
| 5 | NIGHT/USD | 0.04835 | 61.665 | 46.148 | +0.42% | +0.10% | 2.72x | 2.1 | 2026-11-24T14:22:02.190247+00:00 | Not calibrated | STRONG 76/100 | HIGH 55/100 | Watch | WATCH |
| 6 | DBR/USD | 0.01424 | 59.930 | 60.140 | +6.11% | +0.35% | 0.80x | 28.2 | 2026-11-24T14:22:02.190247+00:00 | Not calibrated | MODERATE 50/100 | EXTREME 86/100 | Do nothing | WATCH |
| 7 | Q/USD | 0.027096 | 54.882 | 47.623 | +4.74% | +1.01% | 1.22x | 32.6 | 2026-11-24T14:22:02.190247+00:00 | Not calibrated | MODERATE 52/100 | EXTREME 86/100 | Do nothing | WATCH |
| 8 | LUNA/USD | 4.589e-05 | 53.718 | 60.910 | +5.57% | -0.13% | 0.35x | 19.7 | 2026-11-24T14:22:02.190247+00:00 | Not calibrated | WEAK 27/100 | EXTREME 87/100 | Do nothing | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | VVV/USD | 78.963 | 25.436 | +0.13% | 0.34x |
| 2 | XMR/USD | 64.827 | 496.41 | +0.20% | 4.50x |
| 3 | LUNA/USD | 60.910 | 4.589e-05 | -0.13% | 0.35x |
| 4 | DBR/USD | 60.140 | 0.01424 | +0.35% | 0.80x |
| 5 | GBP/USD | 58.639 | 1.31031 | -0.00% | 1.56x |
| 6 | 2Z/USD | 57.208 | 0.01631 | +0.87% | 2.75x |
| 7 | Q/USD | 47.623 | 0.027096 | +1.01% | 1.22x |
| 8 | NIGHT/USD | 46.148 | 0.04835 | +0.10% | 2.72x |

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

- Persisted scans: 1585; predictions: 13668; observations: 960361.
- Matured sampled outcomes across 1/6/24/48h: 26856; gap abstentions: 22370. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 143 (sampled only; not a success-rate estimate).
- False positives / missed movers: NOT VERIFIED without eligible continuous outcome coverage.
- Baseline vs challenger: recorded as-of; unbiased held-out lift NOT MEASURED.
- Online Kraken /USD stablecoin-base pairs excluded: 18 (counted from this scan's online AssetPairs metadata, not inferred from price).
- Stablecoin base exclusions: BRL1, BUSD, DAI, EUR, EURC, EUROP, EURQ, EURR, EURT, FDUSD, FRAX, GUSD, PYUSD, QCAD, RLUSD, TGBP, TUSD, USD, USD1, USDC, USDD, USDE, USDG, USDQ, USDR, USDS, USDT, ZUSD.
- DEX: NOT USED; no DEX freshness gate.
- OHLC screening abstentions: 5; details in immutable scan JSON artifact.
- Storage: ledger and results published in one non-force Git commit and read back. Independent artifact recovery is NOT VERIFIED by this scan alone.
- Errors: none in successful committed scan; a failed workflow must not publish a SUCCESS report.

# Cryptoscanner — challenger and independent legacy-inspired WATCH

Paper only · risk is high or higher · 30%+ in 48h probability NOT CALIBRATED
Signal confidence 0–100 means setup strength only, NOT a win probability. Actions are research guidance; no trade authorization.

**Writer:** 45412821790 · **Generation:** 1585 · **Legacy run:** 45412821790
**Main quote time:** 2026-11-24T14:22:07.326127+00:00 · **Legacy report time:** 2026-11-24T14:23:01.549479+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | XMR/USD ⭐ | 496.41 | 80.80 | +0.20% | 4.50x | STRONG 90/100 | HIGH 61/100 | Watch |
| 2 | 2Z/USD ⭐ | 0.01631 | 76.53 | +0.87% | 2.75x | STRONG 100/100 | HIGH 67/100 | Consider small entry |
| 3 | VVV/USD | 25.436 | 73.04 | +0.13% | 0.34x | MODERATE 57/100 | VERY_HIGH 70/100 | Watch |
| 4 | GBP/USD | 1.31031 | 64.24 | -0.00% | 1.56x | MODERATE 52/100 | HIGH 61/100 | Watch |
| 5 | NIGHT/USD ⭐ | 0.04835 | 61.67 | +0.10% | 2.72x | STRONG 86/100 | HIGH 55/100 | Watch |
| 6 | DBR/USD | 0.01424 | 59.93 | +0.35% | 0.80x | MODERATE 50/100 | EXTREME 86/100 | Do nothing |
| 7 | Q/USD ⭐ | 0.027096 | 54.88 | +1.01% | 1.22x | MODERATE 62/100 | EXTREME 86/100 | Do nothing |
| 8 | LUNA/USD | 4.589e-05 | 53.72 | -0.13% | 0.35x | WEAK 27/100 | EXTREME 87/100 | Do nothing |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | XMR/USD ⭐ | 497.09 | 72.92 | +0.20% | 4.50x | 10278 | STRONG 91/100 | HIGH 55/100 | Watch |
| 2 | 2Z/USD ⭐ | 0.01631 | 71.84 | +0.87% | 2.75x | 1326 | STRONG 100/100 | HIGH 67/100 | Consider small entry |
| 3 | Q/USD ⭐ | 0.027096 | 58.20 | +1.01% | 1.22x | 703 | MODERATE 59/100 | EXTREME 86/100 | Do nothing |
| 4 | NIGHT/USD ⭐ | 0.04835 | 53.59 | +0.10% | 2.72x | 10901 | STRONG 82/100 | HIGH 55/100 | Watch |

**Same-run overlap:** XMR/USD, 2Z/USD, NIGHT/USD, Q/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
