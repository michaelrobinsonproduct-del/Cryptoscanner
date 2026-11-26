# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-26T22:10:52.695158+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/45902942438
**Source SHA:** 858c8bc8ec5d7641ddb39cacd8aca91719f855b1
**Previous ledger commit:** 193407f902ee0ff3058217db1b29691b4b4b1929 (atomic ledger/results publication)
**Ledger generation:** 1920 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 7s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 628; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 610; valid market observations: 599; OHLC screened: 24.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | ZRO/USD | 1.142 | 74.217 | 71.927 | +11.52% | +0.53% | 0.96x | 17.5 | 2026-11-26T22:10:45.809818+00:00 | Not calibrated | MODERATE 62/100 | VERY_HIGH 73/100 | Watch | WATCH |
| 2 | LTC/USD | 44.03 | 72.052 | 74.363 | +3.09% | -0.11% | 0.83x | 4.5 | 2026-11-26T22:10:45.809818+00:00 | Not calibrated | WEAK 41/100 | HIGH 68/100 | Watch | WATCH |
| 3 | DRV/USD | 0.39089 | 69.477 | 73.339 | +9.25% | -0.70% | 0.96x | 18.7 | 2026-11-26T22:10:45.809818+00:00 | Not calibrated | WEAK 35/100 | VERY_HIGH 74/100 | Watch | WATCH |
| 4 | LINK/USD | 9.345 | 69.331 | 76.361 | +3.32% | -0.47% | 0.53x | 3.8 | 2026-11-26T22:10:45.809818+00:00 | Not calibrated | WEAK 40/100 | VERY_HIGH 76/100 | Watch | WATCH |
| 5 | NEAR/USD | 3.063 | 67.554 | 56.211 | +0.43% | -0.73% | 3.48x | 3.6 | 2026-11-26T22:10:45.809818+00:00 | Not calibrated | MODERATE 64/100 | HIGH 61/100 | Watch | WATCH |
| 6 | W/USD | 0.00885 | 65.007 | 71.600 | +6.63% | -0.45% | 0.57x | 11.3 | 2026-11-26T22:10:45.809818+00:00 | Not calibrated | WEAK 33/100 | EXTREME 87/100 | Do nothing | WATCH |
| 7 | XDG/USD | 0.0566195 | 63.637 | 51.233 | +1.18% | -0.52% | 5.80x | 0.7 | 2026-11-26T22:10:45.809818+00:00 | Not calibrated | MODERATE 62/100 | HIGH 61/100 | Watch | WATCH |
| 8 | SOL/USD | 71.09 | 62.210 | 61.258 | +0.99% | -0.59% | 1.39x | 1.4 | 2026-11-26T22:10:45.809818+00:00 | Not calibrated | MODERATE 51/100 | HIGH 61/100 | Watch | WATCH |
| 9 | ADA/USD | 0.149485 | 61.436 | 71.602 | +2.55% | -0.51% | 0.24x | 2.5 | 2026-11-26T22:10:45.809818+00:00 | Not calibrated | WEAK 36/100 | VERY_HIGH 76/100 | Watch | WATCH |
| 10 | XRP/USD | 0.94889 | 53.780 | 64.058 | +1.32% | -0.40% | 0.17x | 0.3 | 2026-11-26T22:10:45.809818+00:00 | Not calibrated | WEAK 32/100 | VERY_HIGH 76/100 | Do nothing | WATCH |
| 11 | ETH/USD | 1696.35 | 51.184 | 57.430 | +0.35% | -0.45% | 0.60x | 0.1 | 2026-11-26T22:10:45.809818+00:00 | Not calibrated | WEAK 31/100 | VERY_HIGH 76/100 | Do nothing | WATCH |
| 12 | XBT/USD | 60520.2 | 49.482 | 56.750 | +0.25% | -0.43% | 0.49x | 0.0 | 2026-11-26T22:10:45.809818+00:00 | Not calibrated | WEAK 30/100 | VERY_HIGH 76/100 | Do nothing | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | LINK/USD | 76.361 | 9.345 | -0.47% | 0.53x |
| 2 | LTC/USD | 74.363 | 44.03 | -0.11% | 0.83x |
| 3 | DRV/USD | 73.339 | 0.39089 | -0.70% | 0.96x |
| 4 | ZRO/USD | 71.927 | 1.142 | +0.53% | 0.96x |
| 5 | ADA/USD | 71.602 | 0.149485 | -0.51% | 0.24x |
| 6 | W/USD | 71.600 | 0.00885 | -0.45% | 0.57x |
| 7 | XRP/USD | 64.058 | 0.94889 | -0.40% | 0.17x |
| 8 | SOL/USD | 61.258 | 71.09 | -0.59% | 1.39x |
| 9 | ETH/USD | 57.430 | 1696.35 | -0.45% | 0.60x |
| 10 | XBT/USD | 56.750 | 60520.2 | -0.43% | 0.49x |
| 11 | NEAR/USD | 56.211 | 3.063 | -0.73% | 3.48x |
| 12 | XDG/USD | 51.233 | 0.0566195 | -0.52% | 5.80x |

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

- Persisted scans: 1920; predictions: 16775; observations: 1163014.
- Matured sampled outcomes across 1/6/24/48h: 36524; gap abstentions: 25299. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 146 (sampled only; not a success-rate estimate).
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

**Writer:** 45902942438 · **Generation:** 1920 · **Legacy run:** 45902942438
**Main quote time:** 2026-11-26T22:10:52.695158+00:00 · **Legacy report time:** 2026-11-26T22:11:26.085354+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | ZRO/USD | 1.142 | 74.22 | +0.53% | 0.96x | MODERATE 62/100 | VERY_HIGH 73/100 | Watch |
| 2 | LTC/USD | 44.03 | 72.05 | -0.11% | 0.83x | WEAK 41/100 | HIGH 68/100 | Watch |
| 3 | DRV/USD | 0.39089 | 69.48 | -0.70% | 0.96x | WEAK 35/100 | VERY_HIGH 74/100 | Watch |
| 4 | LINK/USD | 9.345 | 69.33 | -0.47% | 0.53x | WEAK 40/100 | VERY_HIGH 76/100 | Watch |
| 5 | NEAR/USD | 3.063 | 67.55 | -0.73% | 3.48x | MODERATE 64/100 | HIGH 61/100 | Watch |
| 6 | W/USD | 0.00885 | 65.01 | -0.45% | 0.57x | WEAK 33/100 | EXTREME 87/100 | Do nothing |
| 7 | XDG/USD | 0.0566195 | 63.64 | -0.52% | 5.80x | MODERATE 62/100 | HIGH 61/100 | Watch |
| 8 | SOL/USD | 71.09 | 62.21 | -0.59% | 1.39x | MODERATE 51/100 | HIGH 61/100 | Watch |
| 9 | ADA/USD | 0.149485 | 61.44 | -0.51% | 0.24x | WEAK 36/100 | VERY_HIGH 76/100 | Watch |
| 10 | XRP/USD | 0.94889 | 53.78 | -0.40% | 0.17x | WEAK 32/100 | VERY_HIGH 76/100 | Do nothing |
| 11 | ETH/USD | 1696.35 | 51.18 | -0.45% | 0.60x | WEAK 31/100 | VERY_HIGH 76/100 | Do nothing |
| 12 | XBT/USD | 60520.2 | 49.48 | -0.43% | 0.49x | WEAK 30/100 | VERY_HIGH 76/100 | Do nothing |

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
