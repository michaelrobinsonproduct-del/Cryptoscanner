# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-23T07:51:36.889545+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/45133915203
**Source SHA:** 858c8bc8ec5d7641ddb39cacd8aca91719f855b1
**Previous ledger commit:** 41b104d793d1022a2c56d98efac7acad44a0df8e (atomic ledger/results publication)
**Ledger generation:** 1401 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 9s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 628; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 610; valid market observations: 609; OHLC screened: 24.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | SUI/USD | 0.6654 | 80.883 | 64.604 | +1.48% | +0.26% | 5.23x | 1.5 | 2026-11-23T07:51:28.350865+00:00 | Not calibrated | STRONG 95/100 | HIGH 55/100 | Consider small entry | WATCH |
| 2 | XRP/USD | 0.93625 | 75.122 | 61.253 | +0.94% | -0.23% | 3.99x | 0.6 | 2026-11-23T07:51:28.350865+00:00 | Not calibrated | MODERATE 68/100 | HIGH 61/100 | Watch | WATCH |
| 3 | XLM/USD | 0.128933 | 64.480 | 61.435 | +1.10% | +0.05% | 1.28x | 2.1 | 2026-11-23T07:51:28.350865+00:00 | Not calibrated | MODERATE 57/100 | HIGH 55/100 | Watch | WATCH |
| 4 | SOL/USD | 71.93 | 63.582 | 67.189 | +1.84% | -0.11% | 0.69x | 1.4 | 2026-11-23T07:51:28.350865+00:00 | Not calibrated | WEAK 37/100 | VERY_HIGH 76/100 | Watch | WATCH |
| 5 | NIGHT/USD | 0.0504 | 58.229 | 62.547 | +2.50% | +0.00% | 0.57x | 11.9 | 2026-11-23T07:51:28.350865+00:00 | Not calibrated | WEAK 44/100 | VERY_HIGH 76/100 | Watch | WATCH |
| 6 | GBP/USD | 1.3125 | 58.142 | 56.632 | +0.27% | +0.03% | 1.14x | 0.5 | 2026-11-23T07:51:28.350865+00:00 | Not calibrated | MODERATE 54/100 | HIGH 62/100 | Watch | WATCH |
| 7 | XBT/USD | 61416.9 | 56.267 | 57.816 | +0.40% | -0.04% | 0.86x | 0.0 | 2026-11-23T07:51:28.350865+00:00 | Not calibrated | WEAK 33/100 | HIGH 68/100 | Do nothing | WATCH |
| 8 | XAUT/USD | 3611.4 | 55.485 | 41.079 | +1.10% | -0.12% | 10.18x | 0.3 | 2026-11-23T07:51:28.350865+00:00 | Not calibrated | MODERATE 58/100 | HIGH 66/100 | Watch | WATCH |
| 9 | ADA/USD | 0.146207 | 55.274 | 55.573 | +1.11% | -0.07% | 1.01x | 1.8 | 2026-11-23T07:51:28.350865+00:00 | Not calibrated | WEAK 38/100 | HIGH 68/100 | Watch | WATCH |
| 10 | XMR/USD | 499.79 | 55.117 | 61.719 | +1.23% | +0.05% | 0.32x | 3.8 | 2026-11-23T07:51:28.350865+00:00 | Not calibrated | MODERATE 48/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 11 | XDG/USD | 0.0554657 | 53.515 | 49.009 | +0.33% | -0.08% | 1.49x | 0.4 | 2026-11-23T07:51:28.350865+00:00 | Not calibrated | MODERATE 47/100 | HIGH 61/100 | Watch | WATCH |
| 12 | BLESS/USD | 0.017714 | 47.779 | 61.734 | +10.07% | -1.56% | 0.38x | 43.5 | 2026-11-23T07:51:28.350865+00:00 | Not calibrated | WEAK 14/100 | EXTREME 100/100 | Do nothing | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | SOL/USD | 67.189 | 71.93 | -0.11% | 0.69x |
| 2 | SUI/USD | 64.604 | 0.6654 | +0.26% | 5.23x |
| 3 | NIGHT/USD | 62.547 | 0.0504 | +0.00% | 0.57x |
| 4 | BLESS/USD | 61.734 | 0.017714 | -1.56% | 0.38x |
| 5 | XMR/USD | 61.719 | 499.79 | +0.05% | 0.32x |
| 6 | XLM/USD | 61.435 | 0.128933 | +0.05% | 1.28x |
| 7 | XRP/USD | 61.253 | 0.93625 | -0.23% | 3.99x |
| 8 | XBT/USD | 57.816 | 61416.9 | -0.04% | 0.86x |
| 9 | GBP/USD | 56.632 | 1.3125 | +0.03% | 1.14x |
| 10 | ADA/USD | 55.573 | 0.146207 | -0.07% | 1.01x |
| 11 | XDG/USD | 49.009 | 0.0554657 | -0.08% | 1.49x |
| 12 | XAUT/USD | 41.079 | 3611.4 | -0.12% | 10.18x |

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

- Persisted scans: 1401; predictions: 11579; observations: 848313.
- Matured sampled outcomes across 1/6/24/48h: 18849; gap abstentions: 22370. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 126 (sampled only; not a success-rate estimate).
- False positives / missed movers: NOT VERIFIED without eligible continuous outcome coverage.
- Baseline vs challenger: recorded as-of; unbiased held-out lift NOT MEASURED.
- Online Kraken /USD stablecoin-base pairs excluded: 18 (counted from this scan's online AssetPairs metadata, not inferred from price).
- Stablecoin base exclusions: BRL1, BUSD, DAI, EUR, EURC, EUROP, EURQ, EURR, EURT, FDUSD, FRAX, GUSD, PYUSD, QCAD, RLUSD, TGBP, TUSD, USD, USD1, USDC, USDD, USDE, USDG, USDQ, USDR, USDS, USDT, ZUSD.
- DEX: NOT USED; no DEX freshness gate.
- OHLC screening abstentions: 8; details in immutable scan JSON artifact.
- Storage: ledger and results published in one non-force Git commit and read back. Independent artifact recovery is NOT VERIFIED by this scan alone.
- Errors: none in successful committed scan; a failed workflow must not publish a SUCCESS report.

# Cryptoscanner — challenger and independent legacy-inspired WATCH

Paper only · risk is high or higher · 30%+ in 48h probability NOT CALIBRATED
Signal confidence 0–100 means setup strength only, NOT a win probability. Actions are research guidance; no trade authorization.

**Writer:** 45133915203 · **Generation:** 1401 · **Legacy run:** 45133915203
**Main quote time:** 2026-11-23T07:51:36.889545+00:00 · **Legacy report time:** 2026-11-23T07:52:45.364598+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | SUI/USD ⭐ | 0.6654 | 80.88 | +0.26% | 5.23x | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 2 | XRP/USD | 0.93625 | 75.12 | -0.23% | 3.99x | MODERATE 68/100 | HIGH 61/100 | Watch |
| 3 | XLM/USD ⭐ | 0.128933 | 64.48 | +0.05% | 1.28x | MODERATE 67/100 | HIGH 55/100 | Watch |
| 4 | SOL/USD | 71.93 | 63.58 | -0.11% | 0.69x | WEAK 37/100 | VERY_HIGH 76/100 | Watch |
| 5 | NIGHT/USD | 0.0504 | 58.23 | +0.00% | 0.57x | WEAK 44/100 | VERY_HIGH 76/100 | Watch |
| 6 | GBP/USD | 1.3125 | 58.14 | +0.03% | 1.14x | MODERATE 54/100 | HIGH 62/100 | Watch |
| 7 | XBT/USD | 61416.9 | 56.27 | -0.04% | 0.86x | WEAK 33/100 | HIGH 68/100 | Do nothing |
| 8 | XAUT/USD | 3611.4 | 55.48 | -0.12% | 10.18x | MODERATE 58/100 | HIGH 66/100 | Watch |
| 9 | ADA/USD | 0.146207 | 55.27 | -0.07% | 1.01x | WEAK 38/100 | HIGH 68/100 | Watch |
| 10 | XMR/USD | 499.79 | 55.12 | +0.05% | 0.32x | MODERATE 48/100 | VERY_HIGH 70/100 | Watch |
| 11 | XDG/USD | 0.0554657 | 53.52 | -0.08% | 1.49x | MODERATE 47/100 | HIGH 61/100 | Watch |
| 12 | BLESS/USD | 0.017714 | 47.78 | -1.56% | 0.38x | WEAK 14/100 | EXTREME 100/100 | Do nothing |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | KAS/USD | 0.02706 | 80.94 | +0.45% | 2.85x | 2766 | STRONG 85/100 | VERY_HIGH 72/100 | Watch |
| 2 | SUI/USD ⭐ | 0.6655 | 75.70 | +0.26% | 5.23x | 6657 | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 3 | XLM/USD ⭐ | 0.128933 | 64.49 | +0.05% | 1.28x | 8737 | MODERATE 67/100 | HIGH 55/100 | Watch |

**Same-run overlap:** SUI/USD, XLM/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
