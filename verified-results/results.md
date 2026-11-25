# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-25T19:46:19.034581+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/45688176632
**Source SHA:** 858c8bc8ec5d7641ddb39cacd8aca91719f855b1
**Previous ledger commit:** 0aaecbfa8ade6fb9f1cd2329216aaf69c86d72d0 (atomic ledger/results publication)
**Ledger generation:** 1758 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 9s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 628; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 610; valid market observations: 609; OHLC screened: 24.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | LTC/USD | 42.33 | 89.612 | 79.180 | +3.62% | -0.54% | 2.31x | 2.4 | 2026-11-25T19:46:10.440835+00:00 | Not calibrated | STRONG 75/100 | HIGH 61/100 | Watch | WATCH |
| 2 | XRP/USD | 0.93928 | 78.388 | 66.237 | +1.70% | -0.39% | 2.41x | 1.3 | 2026-11-25T19:46:10.440835+00:00 | Not calibrated | MODERATE 69/100 | HIGH 61/100 | Watch | WATCH |
| 3 | XLM/USD | 0.127459 | 74.300 | 60.841 | +2.74% | -0.31% | 3.20x | 5.7 | 2026-11-25T19:46:10.440835+00:00 | Not calibrated | MODERATE 67/100 | HIGH 61/100 | Watch | WATCH |
| 4 | HYPE/USD | 61.24 | 71.955 | 70.201 | +2.29% | -0.99% | 1.67x | 1.6 | 2026-11-25T19:46:10.440835+00:00 | Not calibrated | MODERATE 56/100 | HIGH 61/100 | Watch | WATCH |
| 5 | XPL/USD | 0.048 | 71.259 | 71.925 | +9.09% | -1.44% | 1.65x | 20.8 | 2026-11-25T19:46:10.440835+00:00 | Not calibrated | MODERATE 46/100 | VERY_HIGH 77/100 | Do nothing | WATCH |
| 6 | SOL/USD | 70.37 | 69.733 | 61.323 | +1.11% | -0.47% | 2.07x | 2.8 | 2026-11-25T19:46:10.440835+00:00 | Not calibrated | MODERATE 65/100 | HIGH 61/100 | Watch | WATCH |
| 7 | XDG/USD | 0.0557914 | 64.486 | 51.002 | +1.00% | -0.30% | 6.24x | 1.9 | 2026-11-25T19:46:10.440835+00:00 | Not calibrated | MODERATE 62/100 | HIGH 61/100 | Watch | WATCH |
| 8 | SUI/USD | 0.6615 | 64.085 | 68.623 | +2.16% | -0.63% | 0.86x | 3.0 | 2026-11-25T19:46:10.440835+00:00 | Not calibrated | WEAK 37/100 | HIGH 68/100 | Watch | WATCH |
| 9 | ETH/USD | 1683.16 | 62.349 | 55.878 | +0.32% | -0.43% | 1.86x | 2.8 | 2026-11-25T19:46:10.440835+00:00 | Not calibrated | MODERATE 51/100 | HIGH 61/100 | Watch | WATCH |
| 10 | XMR/USD | 517.41 | 61.123 | 59.912 | +1.53% | -0.60% | 1.42x | 11.6 | 2026-11-25T19:46:10.440835+00:00 | Not calibrated | MODERATE 46/100 | HIGH 67/100 | Watch | WATCH |
| 11 | PEPE/USD | 3.47e-06 | 60.865 | 47.730 | +0.49% | -0.37% | 4.23x | 2.9 | 2026-11-25T19:46:10.440835+00:00 | Not calibrated | MODERATE 60/100 | HIGH 61/100 | Watch | WATCH |
| 12 | TIA/USD | 0.3296 | 57.506 | 44.771 | +2.20% | -0.45% | 6.68x | 3.1 | 2026-11-25T19:46:10.440835+00:00 | Not calibrated | MODERATE 59/100 | VERY_HIGH 73/100 | Watch | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | LTC/USD | 79.180 | 42.33 | -0.54% | 2.31x |
| 2 | XPL/USD | 71.925 | 0.048 | -1.44% | 1.65x |
| 3 | HYPE/USD | 70.201 | 61.24 | -0.99% | 1.67x |
| 4 | SUI/USD | 68.623 | 0.6615 | -0.63% | 0.86x |
| 5 | XRP/USD | 66.237 | 0.93928 | -0.39% | 2.41x |
| 6 | SOL/USD | 61.323 | 70.37 | -0.47% | 2.07x |
| 7 | XLM/USD | 60.841 | 0.127459 | -0.31% | 3.20x |
| 8 | XMR/USD | 59.912 | 517.41 | -0.60% | 1.42x |
| 9 | ETH/USD | 55.878 | 1683.16 | -0.43% | 1.86x |
| 10 | XDG/USD | 51.002 | 0.0557914 | -0.30% | 6.24x |
| 11 | PEPE/USD | 47.730 | 3.47e-06 | -0.37% | 4.23x |
| 12 | TIA/USD | 44.771 | 0.3296 | -0.45% | 6.68x |

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

- Persisted scans: 1758; predictions: 14840; observations: 1065666.
- Matured sampled outcomes across 1/6/24/48h: 32594; gap abstentions: 22870. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 146 (sampled only; not a success-rate estimate).
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

**Writer:** 45688176632 · **Generation:** 1758 · **Legacy run:** 45688176632
**Main quote time:** 2026-11-25T19:46:19.034581+00:00 · **Legacy report time:** 2026-11-25T19:47:34.958148+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | LTC/USD | 42.33 | 89.61 | -0.54% | 2.31x | STRONG 75/100 | HIGH 61/100 | Watch |
| 2 | XRP/USD | 0.93928 | 78.39 | -0.39% | 2.41x | MODERATE 69/100 | HIGH 61/100 | Watch |
| 3 | XLM/USD | 0.127459 | 74.30 | -0.31% | 3.20x | MODERATE 67/100 | HIGH 61/100 | Watch |
| 4 | HYPE/USD | 61.24 | 71.95 | -0.99% | 1.67x | MODERATE 56/100 | HIGH 61/100 | Watch |
| 5 | XPL/USD | 0.048 | 71.26 | -1.44% | 1.65x | MODERATE 46/100 | VERY_HIGH 77/100 | Do nothing |
| 6 | SOL/USD | 70.37 | 69.73 | -0.47% | 2.07x | MODERATE 65/100 | HIGH 61/100 | Watch |
| 7 | XDG/USD | 0.0557914 | 64.49 | -0.30% | 6.24x | MODERATE 62/100 | HIGH 61/100 | Watch |
| 8 | SUI/USD | 0.6615 | 64.09 | -0.63% | 0.86x | WEAK 37/100 | HIGH 68/100 | Watch |
| 9 | ETH/USD | 1683.16 | 62.35 | -0.43% | 1.86x | MODERATE 51/100 | HIGH 61/100 | Watch |
| 10 | XMR/USD | 517.41 | 61.12 | -0.60% | 1.42x | MODERATE 46/100 | HIGH 67/100 | Watch |
| 11 | PEPE/USD | 3.47e-06 | 60.87 | -0.37% | 4.23x | MODERATE 60/100 | HIGH 61/100 | Watch |
| 12 | TIA/USD | 0.3296 | 57.51 | -0.45% | 6.68x | MODERATE 59/100 | VERY_HIGH 73/100 | Watch |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | VVV/USD | 27.472 | 92.35 | +0.96% | 1.64x | 11756 | STRONG 91/100 | HIGH 55/100 | Consider small entry |
| 2 | CC/USD | 0.07783 | 80.74 | +0.31% | 1.05x | 5373 | STRONG 75/100 | HIGH 67/100 | Watch |

**Same-run overlap:** None
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
