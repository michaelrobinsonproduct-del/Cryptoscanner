# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-26T07:56:06.998892+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/45778829830
**Source SHA:** 858c8bc8ec5d7641ddb39cacd8aca91719f855b1
**Previous ledger commit:** 905c217dfbf9e8e8f7b141d185a230467de3ad9c (atomic ledger/results publication)
**Ledger generation:** 1833 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 8s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 628; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 610; valid market observations: 609; OHLC screened: 24.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | SYRUP/USD | 0.07207 | 85.815 | 68.937 | +8.75% | +0.38% | 6.41x | 16.7 | 2026-11-26T07:55:59.458762+00:00 | Not calibrated | STRONG 93/100 | HIGH 66/100 | Consider small entry | WATCH |
| 2 | LINK/USD | 9.14837 | 69.882 | 61.126 | +1.15% | -0.07% | 1.91x | 2.4 | 2026-11-26T07:55:59.458762+00:00 | Not calibrated | MODERATE 55/100 | HIGH 61/100 | Watch | WATCH |
| 3 | LTC/USD | 43.45 | 63.590 | 65.977 | +1.73% | +0.12% | 0.70x | 2.3 | 2026-11-26T07:55:59.458762+00:00 | Not calibrated | MODERATE 52/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 4 | INJ/USD | 6.129 | 60.635 | 60.533 | +2.94% | +0.10% | 0.96x | 4.9 | 2026-11-26T07:55:59.458762+00:00 | Not calibrated | MODERATE 50/100 | HIGH 62/100 | Watch | WATCH |
| 5 | XDG/USD | 0.0564472 | 59.798 | 56.212 | +0.87% | -0.10% | 1.41x | 0.0 | 2026-11-26T07:55:59.458762+00:00 | Not calibrated | MODERATE 50/100 | HIGH 61/100 | Watch | WATCH |
| 6 | XRP/USD | 0.95238 | 59.580 | 66.772 | +1.69% | +0.05% | 0.25x | 0.1 | 2026-11-26T07:55:59.458762+00:00 | Not calibrated | MODERATE 50/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 7 | ADA/USD | 0.147747 | 58.788 | 62.362 | +1.36% | -0.06% | 0.67x | 4.3 | 2026-11-26T07:55:59.458762+00:00 | Not calibrated | WEAK 34/100 | VERY_HIGH 76/100 | Do nothing | WATCH |
| 8 | SOL/USD | 70.79 | 58.273 | 58.272 | +0.57% | -0.16% | 1.08x | 1.4 | 2026-11-26T07:55:59.458762+00:00 | Not calibrated | WEAK 39/100 | HIGH 68/100 | Watch | WATCH |
| 9 | PEPE/USD | 3.498e-06 | 56.589 | 44.133 | +0.40% | +0.17% | 2.16x | 5.7 | 2026-11-26T07:55:59.458762+00:00 | Not calibrated | STRONG 73/100 | HIGH 55/100 | Watch | WATCH |
| 10 | ZRO/USD | 1.069 | 54.370 | 61.565 | +4.39% | -0.83% | 0.70x | 18.7 | 2026-11-26T07:55:59.458762+00:00 | Not calibrated | WEAK 27/100 | VERY_HIGH 82/100 | Do nothing | WATCH |
| 11 | SUI/USD | 0.6691 | 50.562 | 57.194 | +0.42% | +0.06% | 0.31x | 1.5 | 2026-11-26T07:55:59.458762+00:00 | Not calibrated | MODERATE 45/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 12 | DCR/USD | 10.518 | 45.756 | 31.041 | +0.27% | -0.06% | 3.01x | 3.8 | 2026-11-26T07:55:59.458762+00:00 | Not calibrated | MODERATE 53/100 | VERY_HIGH 73/100 | Watch | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | SYRUP/USD | 68.937 | 0.07207 | +0.38% | 6.41x |
| 2 | XRP/USD | 66.772 | 0.95238 | +0.05% | 0.25x |
| 3 | LTC/USD | 65.977 | 43.45 | +0.12% | 0.70x |
| 4 | ADA/USD | 62.362 | 0.147747 | -0.06% | 0.67x |
| 5 | ZRO/USD | 61.565 | 1.069 | -0.83% | 0.70x |
| 6 | LINK/USD | 61.126 | 9.14837 | -0.07% | 1.91x |
| 7 | INJ/USD | 60.533 | 6.129 | +0.10% | 0.96x |
| 8 | SOL/USD | 58.272 | 70.79 | -0.16% | 1.08x |
| 9 | SUI/USD | 57.194 | 0.6691 | +0.06% | 0.31x |
| 10 | XDG/USD | 56.212 | 0.0564472 | -0.10% | 1.41x |
| 11 | PEPE/USD | 44.133 | 3.498e-06 | +0.17% | 2.16x |
| 12 | DCR/USD | 31.041 | 10.518 | -0.06% | 3.01x |

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

- Persisted scans: 1833; predictions: 15731; observations: 1111341.
- Matured sampled outcomes across 1/6/24/48h: 34094; gap abstentions: 24266. Per-horizon counts require independent audit; do not infer held-out lift.
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

**Writer:** 45778829830 · **Generation:** 1833 · **Legacy run:** 45778829830
**Main quote time:** 2026-11-26T07:56:06.998892+00:00 · **Legacy report time:** 2026-11-26T07:57:11.306094+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | SYRUP/USD ⭐ | 0.07207 | 85.82 | +0.38% | 6.41x | STRONG 100/100 | HIGH 66/100 | Consider small entry |
| 2 | LINK/USD | 9.14837 | 69.88 | -0.07% | 1.91x | MODERATE 55/100 | HIGH 61/100 | Watch |
| 3 | LTC/USD | 43.45 | 63.59 | +0.12% | 0.70x | MODERATE 52/100 | VERY_HIGH 70/100 | Watch |
| 4 | INJ/USD | 6.129 | 60.63 | +0.10% | 0.96x | MODERATE 50/100 | HIGH 62/100 | Watch |
| 5 | XDG/USD | 0.0564472 | 59.80 | -0.10% | 1.41x | MODERATE 50/100 | HIGH 61/100 | Watch |
| 6 | XRP/USD | 0.95238 | 59.58 | +0.05% | 0.25x | MODERATE 50/100 | VERY_HIGH 70/100 | Watch |
| 7 | ADA/USD | 0.147747 | 58.79 | -0.06% | 0.67x | WEAK 34/100 | VERY_HIGH 76/100 | Do nothing |
| 8 | SOL/USD | 70.79 | 58.27 | -0.16% | 1.08x | WEAK 39/100 | HIGH 68/100 | Watch |
| 9 | PEPE/USD | 3.498e-06 | 56.59 | +0.17% | 2.16x | STRONG 73/100 | HIGH 55/100 | Watch |
| 10 | ZRO/USD | 1.069 | 54.37 | -0.83% | 0.70x | WEAK 27/100 | VERY_HIGH 82/100 | Do nothing |
| 11 | SUI/USD | 0.6691 | 50.56 | +0.06% | 0.31x | MODERATE 45/100 | VERY_HIGH 70/100 | Watch |
| 12 | DCR/USD | 10.518 | 45.76 | -0.06% | 3.01x | MODERATE 53/100 | VERY_HIGH 73/100 | Watch |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | SYRUP/USD ⭐ | 0.07207 | 80.49 | +0.38% | 6.41x | 3780 | STRONG 100/100 | HIGH 66/100 | Consider small entry |

**Same-run overlap:** SYRUP/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
