# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-25T21:45:51.465833+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/45707106340
**Source SHA:** 858c8bc8ec5d7641ddb39cacd8aca91719f855b1
**Previous ledger commit:** 8f8e8f1ca3f55ca01f3aff9a8209142d7042a7b1 (atomic ledger/results publication)
**Ledger generation:** 1771 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 7s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 628; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 610; valid market observations: 609; OHLC screened: 24.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | NEAR/USD | 3.0393 | 102.127 | 91.247 | +5.37% | +1.27% | 1.45x | 2.6 | 2026-11-25T21:45:44.958842+00:00 | Not calibrated | STRONG 95/100 | HIGH 55/100 | Watch | WATCH |
| 2 | ZEC/USD | 764.39 | 80.941 | 76.998 | +3.45% | +0.33% | 1.23x | 4.3 | 2026-11-25T21:45:44.958842+00:00 | Not calibrated | STRONG 75/100 | HIGH 62/100 | Watch | WATCH |
| 3 | LTC/USD | 42.54 | 76.900 | 82.783 | +4.14% | -0.07% | 0.45x | 2.4 | 2026-11-25T21:45:44.958842+00:00 | Not calibrated | WEAK 43/100 | VERY_HIGH 76/100 | Watch | WATCH |
| 4 | HYPE/USD | 61.78 | 72.056 | 75.713 | +3.19% | -0.06% | 0.67x | 3.2 | 2026-11-25T21:45:44.958842+00:00 | Not calibrated | WEAK 41/100 | VERY_HIGH 76/100 | Watch | WATCH |
| 5 | SUI/USD | 0.6636 | 71.615 | 70.897 | +2.49% | -0.08% | 1.11x | 3.0 | 2026-11-25T21:45:44.958842+00:00 | Not calibrated | MODERATE 46/100 | HIGH 68/100 | Watch | WATCH |
| 6 | SOL/USD | 70.72 | 67.802 | 65.557 | +1.61% | +0.24% | 1.10x | 1.4 | 2026-11-25T21:45:44.958842+00:00 | Not calibrated | MODERATE 69/100 | HIGH 62/100 | Watch | WATCH |
| 7 | XRP/USD | 0.94232 | 66.100 | 68.596 | +2.03% | -0.25% | 0.87x | 1.2 | 2026-11-25T21:45:44.958842+00:00 | Not calibrated | WEAK 38/100 | HIGH 68/100 | Watch | WATCH |
| 8 | XMR/USD | 523.68 | 62.344 | 69.179 | +2.76% | +0.26% | 0.19x | 10.3 | 2026-11-25T21:45:44.958842+00:00 | Not calibrated | MODERATE 56/100 | VERY_HIGH 76/100 | Watch | WATCH |
| 9 | PUMP/USD | 0.00254 | 61.620 | 65.799 | +4.14% | +0.08% | 0.54x | 11.8 | 2026-11-25T21:45:44.958842+00:00 | Not calibrated | MODERATE 46/100 | VERY_HIGH 76/100 | Watch | WATCH |
| 10 | ADA/USD | 0.146693 | 59.659 | 65.148 | +1.62% | -0.12% | 0.51x | 2.4 | 2026-11-25T21:45:44.958842+00:00 | Not calibrated | WEAK 35/100 | VERY_HIGH 76/100 | Watch | WATCH |
| 11 | XLM/USD | 0.128129 | 59.588 | 65.344 | +3.28% | -0.04% | 0.44x | 3.2 | 2026-11-25T21:45:44.958842+00:00 | Not calibrated | WEAK 35/100 | VERY_HIGH 76/100 | Watch | WATCH |
| 12 | ETH/USD | 1686.82 | 58.854 | 58.771 | +0.54% | -0.09% | 1.05x | 0.1 | 2026-11-25T21:45:44.958842+00:00 | Not calibrated | WEAK 39/100 | HIGH 68/100 | Watch | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | NEAR/USD | 91.247 | 3.0393 | +1.27% | 1.45x |
| 2 | LTC/USD | 82.783 | 42.54 | -0.07% | 0.45x |
| 3 | ZEC/USD | 76.998 | 764.39 | +0.33% | 1.23x |
| 4 | HYPE/USD | 75.713 | 61.78 | -0.06% | 0.67x |
| 5 | SUI/USD | 70.897 | 0.6636 | -0.08% | 1.11x |
| 6 | XMR/USD | 69.179 | 523.68 | +0.26% | 0.19x |
| 7 | XRP/USD | 68.596 | 0.94232 | -0.25% | 0.87x |
| 8 | PUMP/USD | 65.799 | 0.00254 | +0.08% | 0.54x |
| 9 | SOL/USD | 65.557 | 70.72 | +0.24% | 1.10x |
| 10 | XLM/USD | 65.344 | 0.128129 | -0.04% | 0.44x |
| 11 | ADA/USD | 65.148 | 0.146693 | -0.12% | 0.51x |
| 12 | ETH/USD | 58.771 | 1686.82 | -0.09% | 1.05x |

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

- Persisted scans: 1771; predictions: 14996; observations: 1073583.
- Matured sampled outcomes across 1/6/24/48h: 32738; gap abstentions: 23158. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 146 (sampled only; not a success-rate estimate).
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

**Writer:** 45707106340 · **Generation:** 1771 · **Legacy run:** 45707106340
**Main quote time:** 2026-11-25T21:45:51.465833+00:00 · **Legacy report time:** 2026-11-25T21:46:53.128358+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | NEAR/USD ⭐ | 3.0393 | 102.13 | +1.27% | 1.45x | STRONG 100/100 | HIGH 55/100 | Watch |
| 2 | ZEC/USD ⭐ | 764.39 | 80.94 | +0.33% | 1.23x | STRONG 85/100 | HIGH 62/100 | Watch |
| 3 | LTC/USD | 42.54 | 76.90 | -0.07% | 0.45x | WEAK 43/100 | VERY_HIGH 76/100 | Watch |
| 4 | HYPE/USD | 61.78 | 72.06 | -0.06% | 0.67x | WEAK 41/100 | VERY_HIGH 76/100 | Watch |
| 5 | SUI/USD | 0.6636 | 71.61 | -0.08% | 1.11x | MODERATE 46/100 | HIGH 68/100 | Watch |
| 6 | SOL/USD | 70.72 | 67.80 | +0.24% | 1.10x | MODERATE 69/100 | HIGH 62/100 | Watch |
| 7 | XRP/USD | 0.94232 | 66.10 | -0.25% | 0.87x | WEAK 38/100 | HIGH 68/100 | Watch |
| 8 | XMR/USD | 523.68 | 62.34 | +0.26% | 0.19x | MODERATE 56/100 | VERY_HIGH 76/100 | Watch |
| 9 | PUMP/USD | 0.00254 | 61.62 | +0.08% | 0.54x | MODERATE 46/100 | VERY_HIGH 76/100 | Watch |
| 10 | ADA/USD | 0.146693 | 59.66 | -0.12% | 0.51x | WEAK 35/100 | VERY_HIGH 76/100 | Watch |
| 11 | XLM/USD | 0.128129 | 59.59 | -0.04% | 0.44x | WEAK 35/100 | VERY_HIGH 76/100 | Watch |
| 12 | ETH/USD | 1686.82 | 58.85 | -0.09% | 1.05x | WEAK 39/100 | HIGH 68/100 | Watch |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | NEAR/USD ⭐ | 3.028 | 100.00 | +1.27% | 1.45x | 16705 | STRONG 100/100 | HIGH 55/100 | Watch |
| 2 | ZEC/USD ⭐ | 763.76 | 86.18 | +0.33% | 1.23x | 42749 | STRONG 88/100 | HIGH 62/100 | Watch |
| 3 | PENGU/USD | 0.004344 | 75.03 | +0.12% | 1.95x | 3299 | STRONG 73/100 | HIGH 60/100 | Watch |
| 4 | TIA/USD | 0.3326 | 74.81 | +0.42% | 2.09x | 2919 | STRONG 92/100 | HIGH 67/100 | Consider small entry |

**Same-run overlap:** NEAR/USD, ZEC/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
