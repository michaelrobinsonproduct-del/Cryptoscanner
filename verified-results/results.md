# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-26T17:20:59.932826+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/45866763791
**Source SHA:** 858c8bc8ec5d7641ddb39cacd8aca91719f855b1
**Previous ledger commit:** cb583955950a08ac17151e06c8f50cd668f04d68 (atomic ledger/results publication)
**Ledger generation:** 1890 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 8s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 628; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 610; valid market observations: 595; OHLC screened: 24.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | WIF/USD | 0.1357 | 79.471 | 72.805 | +6.60% | -1.24% | 2.29x | 7.4 | 2026-11-26T17:20:52.094180+00:00 | Not calibrated | STRONG 70/100 | VERY_HIGH 77/100 | Do nothing | WATCH |
| 2 | LINK/USD | 9.19544 | 79.290 | 65.310 | +1.67% | -0.20% | 6.66x | 2.7 | 2026-11-26T17:20:52.094180+00:00 | Not calibrated | STRONG 70/100 | HIGH 61/100 | Watch | WATCH |
| 3 | SKY/USD | 0.04627 | 71.481 | 74.330 | +10.48% | +1.00% | 0.21x | 10.8 | 2026-11-26T17:20:52.094180+00:00 | Not calibrated | MODERATE 61/100 | VERY_HIGH 81/100 | Watch | WATCH |
| 4 | ADA/USD | 0.14892 | 65.752 | 68.481 | +2.16% | -0.26% | 0.86x | 3.3 | 2026-11-26T17:20:52.094180+00:00 | Not calibrated | WEAK 38/100 | HIGH 68/100 | Watch | WATCH |
| 5 | LTC/USD | 43.42 | 64.764 | 65.486 | +1.66% | -0.34% | 1.10x | 2.3 | 2026-11-26T17:20:52.094180+00:00 | Not calibrated | WEAK 42/100 | HIGH 68/100 | Watch | WATCH |
| 6 | FET/USD | 0.116 | 64.570 | 74.108 | +6.91% | -0.34% | 0.22x | 8.6 | 2026-11-26T17:20:52.094180+00:00 | Not calibrated | WEAK 37/100 | VERY_HIGH 81/100 | Watch | WATCH |
| 7 | SOL/USD | 70.99 | 63.978 | 60.262 | +0.85% | -0.14% | 1.44x | 1.4 | 2026-11-26T17:20:52.094180+00:00 | Not calibrated | MODERATE 52/100 | HIGH 61/100 | Watch | WATCH |
| 8 | XRP/USD | 0.95031 | 63.476 | 65.014 | +1.47% | -0.15% | 0.92x | 0.5 | 2026-11-26T17:20:52.094180+00:00 | Not calibrated | WEAK 37/100 | HIGH 68/100 | Watch | WATCH |
| 9 | QNT/USD | 149.56 | 62.207 | 65.208 | +3.29% | -0.73% | 1.07x | 4.0 | 2026-11-26T17:20:52.094180+00:00 | Not calibrated | WEAK 41/100 | HIGH 68/100 | Watch | WATCH |
| 10 | HBAR/USD | 0.05388 | 58.802 | 58.787 | +3.42% | +0.07% | 0.96x | 1.9 | 2026-11-26T17:20:52.094180+00:00 | Not calibrated | MODERATE 49/100 | HIGH 67/100 | Watch | WATCH |
| 11 | XDG/USD | 0.0566564 | 51.555 | 54.031 | +1.25% | -0.21% | 0.86x | 0.1 | 2026-11-26T17:20:52.094180+00:00 | Not calibrated | WEAK 31/100 | HIGH 68/100 | Do nothing | WATCH |
| 12 | NEAR/USD | 3.0579 | 50.970 | 55.202 | +0.26% | -0.58% | 0.86x | 3.3 | 2026-11-26T17:20:52.094180+00:00 | Not calibrated | WEAK 30/100 | HIGH 68/100 | Do nothing | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | SKY/USD | 74.330 | 0.04627 | +1.00% | 0.21x |
| 2 | FET/USD | 74.108 | 0.116 | -0.34% | 0.22x |
| 3 | WIF/USD | 72.805 | 0.1357 | -1.24% | 2.29x |
| 4 | ADA/USD | 68.481 | 0.14892 | -0.26% | 0.86x |
| 5 | LTC/USD | 65.486 | 43.42 | -0.34% | 1.10x |
| 6 | LINK/USD | 65.310 | 9.19544 | -0.20% | 6.66x |
| 7 | QNT/USD | 65.208 | 149.56 | -0.73% | 1.07x |
| 8 | XRP/USD | 65.014 | 0.95031 | -0.15% | 0.92x |
| 9 | SOL/USD | 60.262 | 70.99 | -0.14% | 1.44x |
| 10 | HBAR/USD | 58.787 | 0.05388 | +0.07% | 0.96x |
| 11 | NEAR/USD | 55.202 | 3.0579 | -0.58% | 0.86x |
| 12 | XDG/USD | 54.031 | 0.0566564 | -0.21% | 0.86x |

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

- Persisted scans: 1890; predictions: 16415; observations: 1145082.
- Matured sampled outcomes across 1/6/24/48h: 35468; gap abstentions: 25093. Per-horizon counts require independent audit; do not infer held-out lift.
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

**Writer:** 45866763791 · **Generation:** 1890 · **Legacy run:** 45866763791
**Main quote time:** 2026-11-26T17:20:59.932826+00:00 · **Legacy report time:** 2026-11-26T17:21:36.371653+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | WIF/USD | 0.1357 | 79.47 | -1.24% | 2.29x | STRONG 70/100 | VERY_HIGH 77/100 | Do nothing |
| 2 | LINK/USD | 9.19544 | 79.29 | -0.20% | 6.66x | STRONG 70/100 | HIGH 61/100 | Watch |
| 3 | SKY/USD | 0.04627 | 71.48 | +1.00% | 0.21x | MODERATE 61/100 | VERY_HIGH 81/100 | Watch |
| 4 | ADA/USD | 0.14892 | 65.75 | -0.26% | 0.86x | WEAK 38/100 | HIGH 68/100 | Watch |
| 5 | LTC/USD | 43.42 | 64.76 | -0.34% | 1.10x | WEAK 42/100 | HIGH 68/100 | Watch |
| 6 | FET/USD | 0.116 | 64.57 | -0.34% | 0.22x | WEAK 37/100 | VERY_HIGH 81/100 | Watch |
| 7 | SOL/USD | 70.99 | 63.98 | -0.14% | 1.44x | MODERATE 52/100 | HIGH 61/100 | Watch |
| 8 | XRP/USD | 0.95031 | 63.48 | -0.15% | 0.92x | WEAK 37/100 | HIGH 68/100 | Watch |
| 9 | QNT/USD | 149.56 | 62.21 | -0.73% | 1.07x | WEAK 41/100 | HIGH 68/100 | Watch |
| 10 | HBAR/USD | 0.05388 | 58.80 | +0.07% | 0.96x | MODERATE 49/100 | HIGH 67/100 | Watch |
| 11 | XDG/USD | 0.0566564 | 51.55 | -0.21% | 0.86x | WEAK 31/100 | HIGH 68/100 | Do nothing |
| 12 | NEAR/USD | 3.0579 | 50.97 | -0.58% | 0.86x | WEAK 30/100 | HIGH 68/100 | Do nothing |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | DRV/USD | 0.3714 | 73.75 | +0.62% | 1.16x | 7603 | MODERATE 67/100 | VERY_HIGH 73/100 | Watch |

**Same-run overlap:** None
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
