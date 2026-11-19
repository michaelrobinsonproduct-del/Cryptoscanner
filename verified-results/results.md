# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-19T06:05:23.746954+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/44469523864
**Source SHA:** b271b90a2cae9e5307600070ce7d0e510fe68996
**Previous ledger commit:** 7b62f835d566d0c0bf0a8e49ffe843328b54c0eb (atomic ledger/results publication)
**Ledger generation:** 772 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 6s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 627; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 609; valid market observations: 609; OHLC screened: 24.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | ZEC/USD | 942 | 92.704 | 74.878 | +3.30% | +0.57% | 3.73x | 6.4 | 2026-11-19T06:05:17.737502+00:00 | Not calibrated | STRONG 100/100 | HIGH 55/100 | Consider small entry | WATCH |
| 2 | VVV/USD | 22.937 | 86.411 | 91.826 | +5.84% | +0.29% | 0.31x | 7.4 | 2026-11-19T06:05:17.737502+00:00 | Not calibrated | STRONG 73/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 3 | TAO/USD | 195.743 | 83.185 | 65.628 | +1.97% | +0.51% | 3.19x | 6.3 | 2026-11-19T06:05:17.737502+00:00 | Not calibrated | STRONG 97/100 | HIGH 55/100 | Consider small entry | WATCH |
| 4 | SENT/USD | 0.022419 | 78.952 | 70.537 | +8.80% | +2.19% | 0.74x | 13.4 | 2026-11-19T06:05:17.737502+00:00 | Not calibrated | MODERATE 64/100 | VERY_HIGH 81/100 | Watch | WATCH |
| 5 | NEAR/USD | 3.3983 | 76.463 | 74.062 | +3.06% | +0.82% | 0.83x | 4.7 | 2026-11-19T06:05:17.737502+00:00 | Not calibrated | MODERATE 68/100 | HIGH 62/100 | Watch | WATCH |
| 6 | SOL/USD | 74.71 | 70.158 | 65.468 | +1.59% | +0.39% | 1.27x | 1.3 | 2026-11-19T06:05:17.737502+00:00 | Not calibrated | STRONG 70/100 | HIGH 55/100 | Watch | WATCH |
| 7 | TRX/USD | 0.312592 | 65.486 | 49.141 | +1.07% | +0.27% | 42.16x | 0.0 | 2026-11-19T06:05:17.737502+00:00 | Not calibrated | STRONG 88/100 | HIGH 55/100 | Watch | WATCH |
| 8 | ETH/USD | 1800.36 | 65.289 | 65.069 | +1.44% | +0.29% | 0.87x | 0.1 | 2026-11-19T06:05:17.737502+00:00 | Not calibrated | MODERATE 63/100 | HIGH 62/100 | Watch | WATCH |
| 9 | HYPE/USD | 68.11 | 64.982 | 67.138 | +1.84% | +0.31% | 0.63x | 1.5 | 2026-11-19T06:05:17.737502+00:00 | Not calibrated | MODERATE 62/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 10 | ADA/USD | 0.153025 | 62.391 | 61.464 | +1.17% | +0.26% | 0.96x | 3.5 | 2026-11-19T06:05:17.737502+00:00 | Not calibrated | MODERATE 61/100 | HIGH 62/100 | Watch | WATCH |
| 11 | XBT/USD | 63400.5 | 56.483 | 59.615 | +0.66% | +0.23% | 0.57x | 0.0 | 2026-11-19T06:05:17.737502+00:00 | Not calibrated | MODERATE 58/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 12 | XRP/USD | 0.9751 | 55.819 | 61.272 | +0.90% | +0.38% | 0.26x | 0.1 | 2026-11-19T06:05:17.737502+00:00 | Not calibrated | MODERATE 58/100 | VERY_HIGH 70/100 | Watch | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | VVV/USD | 91.826 | 22.937 | +0.29% | 0.31x |
| 2 | ZEC/USD | 74.878 | 942 | +0.57% | 3.73x |
| 3 | NEAR/USD | 74.062 | 3.3983 | +0.82% | 0.83x |
| 4 | SENT/USD | 70.537 | 0.022419 | +2.19% | 0.74x |
| 5 | HYPE/USD | 67.138 | 68.11 | +0.31% | 0.63x |
| 6 | TAO/USD | 65.628 | 195.743 | +0.51% | 3.19x |
| 7 | SOL/USD | 65.468 | 74.71 | +0.39% | 1.27x |
| 8 | ETH/USD | 65.069 | 1800.36 | +0.29% | 0.87x |
| 9 | ADA/USD | 61.464 | 0.153025 | +0.26% | 0.96x |
| 10 | XRP/USD | 61.272 | 0.9751 | +0.38% | 0.26x |
| 11 | XBT/USD | 59.615 | 63400.5 | +0.23% | 0.57x |
| 12 | TRX/USD | 49.141 | 0.312592 | +0.27% | 42.16x |

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

- Persisted scans: 772; predictions: 6408; observations: 467154.
- Matured sampled outcomes across 1/6/24/48h: 6446; gap abstentions: 13810. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 10 (sampled only; not a success-rate estimate).
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

**Writer:** 44469523864 · **Generation:** 772 · **Legacy run:** 44469523864
**Main quote time:** 2026-11-19T06:05:23.746954+00:00 · **Legacy report time:** 2026-11-19T06:06:10.058267+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | ZEC/USD ⭐ | 942 | 92.70 | +0.57% | 3.73x | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 2 | VVV/USD | 22.937 | 86.41 | +0.29% | 0.31x | STRONG 73/100 | VERY_HIGH 70/100 | Watch |
| 3 | TAO/USD | 195.743 | 83.18 | +0.51% | 3.19x | STRONG 97/100 | HIGH 55/100 | Consider small entry |
| 4 | SENT/USD | 0.022419 | 78.95 | +2.19% | 0.74x | MODERATE 64/100 | VERY_HIGH 81/100 | Watch |
| 5 | NEAR/USD | 3.3983 | 76.46 | +0.82% | 0.83x | MODERATE 68/100 | HIGH 62/100 | Watch |
| 6 | SOL/USD ⭐ | 74.71 | 70.16 | +0.39% | 1.27x | STRONG 80/100 | HIGH 55/100 | Watch |
| 7 | TRX/USD | 0.312592 | 65.49 | +0.27% | 42.16x | STRONG 88/100 | HIGH 55/100 | Watch |
| 8 | ETH/USD | 1800.36 | 65.29 | +0.29% | 0.87x | MODERATE 63/100 | HIGH 62/100 | Watch |
| 9 | HYPE/USD | 68.11 | 64.98 | +0.31% | 0.63x | MODERATE 62/100 | VERY_HIGH 70/100 | Watch |
| 10 | ADA/USD | 0.153025 | 62.39 | +0.26% | 0.96x | MODERATE 61/100 | HIGH 62/100 | Watch |
| 11 | XBT/USD | 63400.5 | 56.48 | +0.23% | 0.57x | MODERATE 58/100 | VERY_HIGH 70/100 | Watch |
| 12 | XRP/USD | 0.9751 | 55.82 | +0.38% | 0.26x | MODERATE 58/100 | VERY_HIGH 70/100 | Watch |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | ZEC/USD ⭐ | 942.96 | 92.74 | +0.57% | 3.73x | 22335 | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 2 | SOL/USD ⭐ | 74.76 | 71.50 | +0.39% | 1.27x | 35186 | STRONG 81/100 | HIGH 55/100 | Watch |

**Same-run overlap:** ZEC/USD, SOL/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
