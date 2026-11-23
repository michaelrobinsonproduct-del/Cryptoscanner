# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-23T07:41:26.202635+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/45132707591
**Source SHA:** 858c8bc8ec5d7641ddb39cacd8aca91719f855b1
**Previous ledger commit:** 37b6ce57f9683ca79d2d401284d07e87cb15cca3 (atomic ledger/results publication)
**Ledger generation:** 1400 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 8s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 628; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 610; valid market observations: 609; OHLC screened: 24.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | SUI/USD | 0.6658 | 78.905 | 64.280 | +1.54% | -0.07% | 3.44x | 3.0 | 2026-11-23T07:41:18.562476+00:00 | Not calibrated | MODERATE 69/100 | HIGH 61/100 | Watch | WATCH |
| 2 | XRP/USD | 0.93808 | 76.392 | 62.901 | +1.14% | -0.30% | 3.81x | 0.1 | 2026-11-23T07:41:18.562476+00:00 | Not calibrated | MODERATE 68/100 | HIGH 61/100 | Watch | WATCH |
| 3 | SOL/USD | 72.01 | 73.619 | 67.983 | +1.95% | -0.12% | 1.63x | 1.4 | 2026-11-23T07:41:18.562476+00:00 | Not calibrated | MODERATE 57/100 | HIGH 61/100 | Watch | WATCH |
| 4 | PEARL/USD | 2.1591 | 68.952 | 68.381 | +5.10% | +0.52% | 0.80x | 17.6 | 2026-11-23T07:41:18.562476+00:00 | Not calibrated | MODERATE 59/100 | HIGH 68/100 | Watch | WATCH |
| 5 | NIGHT/USD | 0.05047 | 65.512 | 64.574 | +2.64% | +0.26% | 0.96x | 9.9 | 2026-11-23T07:41:18.562476+00:00 | Not calibrated | MODERATE 63/100 | HIGH 62/100 | Watch | WATCH |
| 6 | XLM/USD | 0.128909 | 64.719 | 61.764 | +1.08% | +0.08% | 1.26x | 1.1 | 2026-11-23T07:41:18.562476+00:00 | Not calibrated | MODERATE 57/100 | HIGH 55/100 | Watch | WATCH |
| 7 | XMR/USD | 499.76 | 62.472 | 62.277 | +1.23% | -0.16% | 1.10x | 2.6 | 2026-11-23T07:41:18.562476+00:00 | Not calibrated | WEAK 41/100 | HIGH 68/100 | Watch | WATCH |
| 8 | XBT/USD | 61414.9 | 55.604 | 57.793 | +0.40% | -0.03% | 0.80x | 0.0 | 2026-11-23T07:41:18.562476+00:00 | Not calibrated | WEAK 33/100 | HIGH 68/100 | Do nothing | WATCH |
| 9 | XAUT/USD | 3613.4 | 55.221 | 41.477 | +1.16% | -0.25% | 27.56x | 0.3 | 2026-11-23T07:41:18.562476+00:00 | Not calibrated | MODERATE 58/100 | HIGH 66/100 | Watch | WATCH |
| 10 | XDG/USD | 0.0554621 | 54.592 | 48.782 | +0.32% | -0.27% | 1.71x | 0.7 | 2026-11-23T07:41:18.562476+00:00 | Not calibrated | MODERATE 47/100 | HIGH 61/100 | Watch | WATCH |
| 11 | LINK/USD | 8.91098 | 52.311 | 51.735 | +1.13% | -0.00% | 1.06x | 0.0 | 2026-11-23T07:41:18.562476+00:00 | Not calibrated | WEAK 36/100 | HIGH 68/100 | Watch | WATCH |
| 12 | PAXG/USD | 3613.53 | 46.761 | 52.254 | +1.16% | -0.23% | 0.57x | 1.1 | 2026-11-23T07:41:18.562476+00:00 | Not calibrated | WEAK 28/100 | VERY_HIGH 76/100 | Do nothing | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | PEARL/USD | 68.381 | 2.1591 | +0.52% | 0.80x |
| 2 | SOL/USD | 67.983 | 72.01 | -0.12% | 1.63x |
| 3 | NIGHT/USD | 64.574 | 0.05047 | +0.26% | 0.96x |
| 4 | SUI/USD | 64.280 | 0.6658 | -0.07% | 3.44x |
| 5 | XRP/USD | 62.901 | 0.93808 | -0.30% | 3.81x |
| 6 | XMR/USD | 62.277 | 499.76 | -0.16% | 1.10x |
| 7 | XLM/USD | 61.764 | 0.128909 | +0.08% | 1.26x |
| 8 | XBT/USD | 57.793 | 61414.9 | -0.03% | 0.80x |
| 9 | PAXG/USD | 52.254 | 3613.53 | -0.23% | 0.57x |
| 10 | LINK/USD | 51.735 | 8.91098 | -0.00% | 1.06x |
| 11 | XDG/USD | 48.782 | 0.0554621 | -0.27% | 1.71x |
| 12 | XAUT/USD | 41.477 | 3613.4 | -0.25% | 27.56x |

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

- Persisted scans: 1400; predictions: 11567; observations: 847704.
- Matured sampled outcomes across 1/6/24/48h: 18818; gap abstentions: 22370. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 125 (sampled only; not a success-rate estimate).
- False positives / missed movers: NOT VERIFIED without eligible continuous outcome coverage.
- Baseline vs challenger: recorded as-of; unbiased held-out lift NOT MEASURED.
- Online Kraken /USD stablecoin-base pairs excluded: 18 (counted from this scan's online AssetPairs metadata, not inferred from price).
- Stablecoin base exclusions: BRL1, BUSD, DAI, EUR, EURC, EUROP, EURQ, EURR, EURT, FDUSD, FRAX, GUSD, PYUSD, QCAD, RLUSD, TGBP, TUSD, USD, USD1, USDC, USDD, USDE, USDG, USDQ, USDR, USDS, USDT, ZUSD.
- DEX: NOT USED; no DEX freshness gate.
- OHLC screening abstentions: 9; details in immutable scan JSON artifact.
- Storage: ledger and results published in one non-force Git commit and read back. Independent artifact recovery is NOT VERIFIED by this scan alone.
- Errors: none in successful committed scan; a failed workflow must not publish a SUCCESS report.

# Cryptoscanner — challenger and independent legacy-inspired WATCH

Paper only · risk is high or higher · 30%+ in 48h probability NOT CALIBRATED
Signal confidence 0–100 means setup strength only, NOT a win probability. Actions are research guidance; no trade authorization.

**Writer:** 45132707591 · **Generation:** 1400 · **Legacy run:** 45132707591
**Main quote time:** 2026-11-23T07:41:26.202635+00:00 · **Legacy report time:** 2026-11-23T07:42:14.026687+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | SUI/USD | 0.6658 | 78.91 | -0.07% | 3.44x | MODERATE 69/100 | HIGH 61/100 | Watch |
| 2 | XRP/USD | 0.93808 | 76.39 | -0.30% | 3.81x | MODERATE 68/100 | HIGH 61/100 | Watch |
| 3 | SOL/USD | 72.01 | 73.62 | -0.12% | 1.63x | MODERATE 57/100 | HIGH 61/100 | Watch |
| 4 | PEARL/USD | 2.1591 | 68.95 | +0.52% | 0.80x | MODERATE 59/100 | HIGH 68/100 | Watch |
| 5 | NIGHT/USD | 0.05047 | 65.51 | +0.26% | 0.96x | MODERATE 63/100 | HIGH 62/100 | Watch |
| 6 | XLM/USD ⭐ | 0.128909 | 64.72 | +0.08% | 1.26x | MODERATE 67/100 | HIGH 55/100 | Watch |
| 7 | XMR/USD | 499.76 | 62.47 | -0.16% | 1.10x | WEAK 41/100 | HIGH 68/100 | Watch |
| 8 | XBT/USD | 61414.9 | 55.60 | -0.03% | 0.80x | WEAK 33/100 | HIGH 68/100 | Do nothing |
| 9 | XAUT/USD | 3613.4 | 55.22 | -0.25% | 27.56x | MODERATE 58/100 | HIGH 66/100 | Watch |
| 10 | XDG/USD | 0.0554621 | 54.59 | -0.27% | 1.71x | MODERATE 47/100 | HIGH 61/100 | Watch |
| 11 | LINK/USD | 8.91098 | 52.31 | -0.00% | 1.06x | WEAK 36/100 | HIGH 68/100 | Watch |
| 12 | PAXG/USD | 3613.53 | 46.76 | -0.23% | 0.57x | WEAK 28/100 | VERY_HIGH 76/100 | Do nothing |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | NEAR/USD | 3.0121 | 69.17 | +0.31% | 9.11x | 14338 | STRONG 90/100 | HIGH 55/100 | Watch |
| 2 | XLM/USD ⭐ | 0.128911 | 64.72 | +0.08% | 1.26x | 8753 | MODERATE 67/100 | HIGH 55/100 | Watch |

**Same-run overlap:** XLM/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
