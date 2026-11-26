# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-26T03:05:57.144121+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/45746552917
**Source SHA:** 858c8bc8ec5d7641ddb39cacd8aca91719f855b1
**Previous ledger commit:** cdb9697f72f4eafb937db28e686d11b6284aaa1a (atomic ledger/results publication)
**Ledger generation:** 1804 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 5s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 628; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 610; valid market observations: 609; OHLC screened: 24.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | SYRUP/USD | 0.07108 | 71.323 | 70.745 | +7.26% | +0.37% | 0.87x | 12.7 | 2026-11-26T03:05:51.822673+00:00 | Not calibrated | MODERATE 61/100 | VERY_HIGH 73/100 | Watch | WATCH |
| 2 | XBT/USD | 60608.4 | 70.188 | 57.772 | +0.40% | -0.52% | 2.51x | 0.0 | 2026-11-26T03:05:51.822673+00:00 | Not calibrated | MODERATE 65/100 | HIGH 61/100 | Watch | WATCH |
| 3 | XRP/USD | 0.95393 | 65.192 | 67.930 | +1.85% | -0.42% | 0.94x | 0.1 | 2026-11-26T03:05:51.822673+00:00 | Not calibrated | WEAK 38/100 | HIGH 68/100 | Watch | WATCH |
| 4 | LTC/USD | 43.41 | 58.345 | 64.169 | +1.64% | -0.37% | 0.60x | 4.6 | 2026-11-26T03:05:51.822673+00:00 | Not calibrated | WEAK 34/100 | VERY_HIGH 76/100 | Do nothing | WATCH |
| 5 | LINK/USD | 9.14813 | 57.546 | 59.570 | +1.15% | -0.53% | 1.06x | 2.2 | 2026-11-26T03:05:51.822673+00:00 | Not calibrated | WEAK 39/100 | HIGH 68/100 | Watch | WATCH |
| 6 | TAO/USD | 184.3457 | 57.269 | 62.251 | +1.52% | -0.79% | 0.90x | 6.7 | 2026-11-26T03:05:51.822673+00:00 | Not calibrated | WEAK 34/100 | HIGH 68/100 | Do nothing | WATCH |
| 7 | ETH/USD | 1694.81 | 57.114 | 56.792 | +0.26% | -0.35% | 1.21x | 0.1 | 2026-11-26T03:05:51.822673+00:00 | Not calibrated | WEAK 39/100 | HIGH 68/100 | Watch | WATCH |
| 8 | SUI/USD | 0.6716 | 56.635 | 59.824 | +0.80% | -0.81% | 1.09x | 1.5 | 2026-11-26T03:05:51.822673+00:00 | Not calibrated | WEAK 38/100 | HIGH 68/100 | Watch | WATCH |
| 9 | INJ/USD | 6.111 | 55.348 | 57.368 | +2.64% | -1.23% | 1.41x | 6.5 | 2026-11-26T03:05:51.822673+00:00 | Not calibrated | MODERATE 48/100 | HIGH 65/100 | Do nothing | WATCH |
| 10 | XLM/USD | 0.128882 | 54.175 | 48.624 | +0.83% | -0.46% | 1.78x | 3.6 | 2026-11-26T03:05:51.822673+00:00 | Not calibrated | MODERATE 47/100 | HIGH 61/100 | Watch | WATCH |
| 11 | ADA/USD | 0.147989 | 54.016 | 64.204 | +1.52% | -0.31% | 0.14x | 2.9 | 2026-11-26T03:05:51.822673+00:00 | Not calibrated | WEAK 32/100 | VERY_HIGH 76/100 | Do nothing | WATCH |
| 12 | SOL/USD | 71.06 | 53.386 | 60.959 | +0.95% | -0.39% | 0.44x | 1.4 | 2026-11-26T03:05:51.822673+00:00 | Not calibrated | WEAK 32/100 | VERY_HIGH 76/100 | Do nothing | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | SYRUP/USD | 70.745 | 0.07108 | +0.37% | 0.87x |
| 2 | XRP/USD | 67.930 | 0.95393 | -0.42% | 0.94x |
| 3 | ADA/USD | 64.204 | 0.147989 | -0.31% | 0.14x |
| 4 | LTC/USD | 64.169 | 43.41 | -0.37% | 0.60x |
| 5 | TAO/USD | 62.251 | 184.3457 | -0.79% | 0.90x |
| 6 | SOL/USD | 60.959 | 71.06 | -0.39% | 0.44x |
| 7 | SUI/USD | 59.824 | 0.6716 | -0.81% | 1.09x |
| 8 | LINK/USD | 59.570 | 9.14813 | -0.53% | 1.06x |
| 9 | XBT/USD | 57.772 | 60608.4 | -0.52% | 2.51x |
| 10 | INJ/USD | 57.368 | 6.111 | -1.23% | 1.41x |
| 11 | ETH/USD | 56.792 | 1694.81 | -0.35% | 1.21x |
| 12 | XLM/USD | 48.624 | 0.128882 | -0.46% | 1.78x |

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

- Persisted scans: 1804; predictions: 15383; observations: 1093680.
- Matured sampled outcomes across 1/6/24/48h: 33395; gap abstentions: 23743. Per-horizon counts require independent audit; do not infer held-out lift.
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

**Writer:** 45746552917 · **Generation:** 1804 · **Legacy run:** 45746552917
**Main quote time:** 2026-11-26T03:05:57.144121+00:00 · **Legacy report time:** 2026-11-26T03:06:51.162451+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | SYRUP/USD | 0.07108 | 71.32 | +0.37% | 0.87x | MODERATE 61/100 | VERY_HIGH 73/100 | Watch |
| 2 | XBT/USD | 60608.4 | 70.19 | -0.52% | 2.51x | MODERATE 65/100 | HIGH 61/100 | Watch |
| 3 | XRP/USD | 0.95393 | 65.19 | -0.42% | 0.94x | WEAK 38/100 | HIGH 68/100 | Watch |
| 4 | LTC/USD | 43.41 | 58.35 | -0.37% | 0.60x | WEAK 34/100 | VERY_HIGH 76/100 | Do nothing |
| 5 | LINK/USD | 9.14813 | 57.55 | -0.53% | 1.06x | WEAK 39/100 | HIGH 68/100 | Watch |
| 6 | TAO/USD | 184.3457 | 57.27 | -0.79% | 0.90x | WEAK 34/100 | HIGH 68/100 | Do nothing |
| 7 | ETH/USD | 1694.81 | 57.11 | -0.35% | 1.21x | WEAK 39/100 | HIGH 68/100 | Watch |
| 8 | SUI/USD | 0.6716 | 56.64 | -0.81% | 1.09x | WEAK 38/100 | HIGH 68/100 | Watch |
| 9 | INJ/USD | 6.111 | 55.35 | -1.23% | 1.41x | MODERATE 48/100 | HIGH 65/100 | Do nothing |
| 10 | XLM/USD | 0.128882 | 54.17 | -0.46% | 1.78x | MODERATE 47/100 | HIGH 61/100 | Watch |
| 11 | ADA/USD | 0.147989 | 54.02 | -0.31% | 0.14x | WEAK 32/100 | VERY_HIGH 76/100 | Do nothing |
| 12 | SOL/USD | 71.06 | 53.39 | -0.39% | 0.44x | WEAK 32/100 | VERY_HIGH 76/100 | Do nothing |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| — | No confirmed WATCH signals | — | — | — | — | — | — | — | — |

**Same-run overlap:** None
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
