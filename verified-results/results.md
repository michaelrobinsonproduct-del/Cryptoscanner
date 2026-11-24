# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-24T01:32:39.277508+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/45305419608
**Source SHA:** 858c8bc8ec5d7641ddb39cacd8aca91719f855b1
**Previous ledger commit:** f97eff2b5b982ca28e98875e7c0a71d2191e6d05 (atomic ledger/results publication)
**Ledger generation:** 1507 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 8s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 628; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 610; valid market observations: 609; OHLC screened: 24.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | XLM/USD | 0.131859 | 81.696 | 64.777 | +1.43% | +0.38% | 6.30x | 0.5 | 2026-11-24T01:32:30.795121+00:00 | Not calibrated | STRONG 96/100 | HIGH 55/100 | Consider small entry | WATCH |
| 2 | LTC/USD | 41.81 | 77.552 | 60.395 | +0.94% | +0.43% | 2.77x | 2.4 | 2026-11-24T01:32:30.795121+00:00 | Not calibrated | STRONG 94/100 | HIGH 55/100 | Consider small entry | WATCH |
| 3 | XRP/USD | 0.95124 | 72.480 | 63.305 | +1.26% | +0.38% | 1.73x | 1.1 | 2026-11-24T01:32:30.795121+00:00 | Not calibrated | STRONG 81/100 | HIGH 55/100 | Consider small entry | WATCH |
| 4 | NIGHT/USD | 0.04905 | 69.233 | 59.992 | +1.87% | +0.55% | 1.65x | 6.1 | 2026-11-24T01:32:30.795121+00:00 | Not calibrated | STRONG 80/100 | HIGH 55/100 | Watch | WATCH |
| 5 | INJ/USD | 6.297 | 68.509 | 54.379 | +0.30% | +0.32% | 2.25x | 3.2 | 2026-11-24T01:32:30.795121+00:00 | Not calibrated | STRONG 89/100 | HIGH 55/100 | Watch | WATCH |
| 6 | VVV/USD | 24.843 | 67.432 | 60.464 | +1.62% | +0.64% | 1.38x | 11.7 | 2026-11-24T01:32:30.795121+00:00 | Not calibrated | STRONG 74/100 | HIGH 61/100 | Watch | WATCH |
| 7 | ZEC/USD | 786.39 | 66.589 | 63.061 | +1.45% | +0.28% | 1.22x | 4.2 | 2026-11-24T01:32:30.795121+00:00 | Not calibrated | MODERATE 68/100 | HIGH 62/100 | Watch | WATCH |
| 8 | SOL/USD | 72.45 | 64.036 | 59.370 | +0.72% | +0.21% | 1.36x | 1.4 | 2026-11-24T01:32:30.795121+00:00 | Not calibrated | STRONG 77/100 | HIGH 55/100 | Watch | WATCH |
| 9 | ETH/USD | 1716.45 | 63.576 | 58.352 | +0.48% | +0.05% | 1.50x | 0.1 | 2026-11-24T01:32:30.795121+00:00 | Not calibrated | MODERATE 67/100 | HIGH 55/100 | Watch | WATCH |
| 10 | HYPE/USD | 64.41 | 62.771 | 62.692 | +1.21% | +0.17% | 0.92x | 1.6 | 2026-11-24T01:32:30.795121+00:00 | Not calibrated | MODERATE 51/100 | HIGH 62/100 | Watch | WATCH |
| 11 | XBT/USD | 61455.3 | 60.796 | 57.920 | +0.42% | +0.04% | 1.27x | 0.0 | 2026-11-24T01:32:30.795121+00:00 | Not calibrated | MODERATE 55/100 | HIGH 55/100 | Watch | WATCH |
| 12 | XDG/USD | 0.0570185 | 59.252 | 63.308 | +1.27% | +0.46% | 0.37x | 1.1 | 2026-11-24T01:32:30.795121+00:00 | Not calibrated | MODERATE 60/100 | VERY_HIGH 70/100 | Watch | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | XLM/USD | 64.777 | 0.131859 | +0.38% | 6.30x |
| 2 | XDG/USD | 63.308 | 0.0570185 | +0.46% | 0.37x |
| 3 | XRP/USD | 63.305 | 0.95124 | +0.38% | 1.73x |
| 4 | ZEC/USD | 63.061 | 786.39 | +0.28% | 1.22x |
| 5 | HYPE/USD | 62.692 | 64.41 | +0.17% | 0.92x |
| 6 | VVV/USD | 60.464 | 24.843 | +0.64% | 1.38x |
| 7 | LTC/USD | 60.395 | 41.81 | +0.43% | 2.77x |
| 8 | NIGHT/USD | 59.992 | 0.04905 | +0.55% | 1.65x |
| 9 | SOL/USD | 59.370 | 72.45 | +0.21% | 1.36x |
| 10 | ETH/USD | 58.352 | 1716.45 | +0.05% | 1.50x |
| 11 | XBT/USD | 57.920 | 61455.3 | +0.04% | 1.27x |
| 12 | INJ/USD | 54.379 | 6.297 | +0.32% | 2.25x |

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

- Persisted scans: 1507; predictions: 12841; observations: 912864.
- Matured sampled outcomes across 1/6/24/48h: 23665; gap abstentions: 22370. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 133 (sampled only; not a success-rate estimate).
- False positives / missed movers: NOT VERIFIED without eligible continuous outcome coverage.
- Baseline vs challenger: recorded as-of; unbiased held-out lift NOT MEASURED.
- Online Kraken /USD stablecoin-base pairs excluded: 18 (counted from this scan's online AssetPairs metadata, not inferred from price).
- Stablecoin base exclusions: BRL1, BUSD, DAI, EUR, EURC, EUROP, EURQ, EURR, EURT, FDUSD, FRAX, GUSD, PYUSD, QCAD, RLUSD, TGBP, TUSD, USD, USD1, USDC, USDD, USDE, USDG, USDQ, USDR, USDS, USDT, ZUSD.
- DEX: NOT USED; no DEX freshness gate.
- OHLC screening abstentions: 4; details in immutable scan JSON artifact.
- Storage: ledger and results published in one non-force Git commit and read back. Independent artifact recovery is NOT VERIFIED by this scan alone.
- Errors: none in successful committed scan; a failed workflow must not publish a SUCCESS report.

# Cryptoscanner — challenger and independent legacy-inspired WATCH

Paper only · risk is high or higher · 30%+ in 48h probability NOT CALIBRATED
Signal confidence 0–100 means setup strength only, NOT a win probability. Actions are research guidance; no trade authorization.

**Writer:** 45305419608 · **Generation:** 1507 · **Legacy run:** 45305419608
**Main quote time:** 2026-11-24T01:32:39.277508+00:00 · **Legacy report time:** 2026-11-24T01:33:32.554107+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | XLM/USD ⭐ | 0.131859 | 81.70 | +0.38% | 6.30x | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 2 | LTC/USD ⭐ | 41.81 | 77.55 | +0.43% | 2.77x | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 3 | XRP/USD ⭐ | 0.95124 | 72.48 | +0.38% | 1.73x | STRONG 91/100 | HIGH 55/100 | Consider small entry |
| 4 | NIGHT/USD ⭐ | 0.04905 | 69.23 | +0.55% | 1.65x | STRONG 90/100 | HIGH 55/100 | Consider small entry |
| 5 | INJ/USD | 6.297 | 68.51 | +0.32% | 2.25x | STRONG 89/100 | HIGH 55/100 | Watch |
| 6 | VVV/USD | 24.843 | 67.43 | +0.64% | 1.38x | STRONG 74/100 | HIGH 61/100 | Watch |
| 7 | ZEC/USD ⭐ | 786.39 | 66.59 | +0.28% | 1.22x | STRONG 78/100 | HIGH 62/100 | Watch |
| 8 | SOL/USD ⭐ | 72.45 | 64.04 | +0.21% | 1.36x | STRONG 87/100 | HIGH 55/100 | Watch |
| 9 | ETH/USD ⭐ | 1716.45 | 63.58 | +0.05% | 1.50x | STRONG 77/100 | HIGH 55/100 | Watch |
| 10 | HYPE/USD | 64.41 | 62.77 | +0.17% | 0.92x | MODERATE 51/100 | HIGH 62/100 | Watch |
| 11 | XBT/USD | 61455.3 | 60.80 | +0.04% | 1.27x | MODERATE 55/100 | HIGH 55/100 | Watch |
| 12 | XDG/USD | 0.0570185 | 59.25 | +0.46% | 0.37x | MODERATE 60/100 | VERY_HIGH 70/100 | Watch |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | PEPE/USD | 3.491e-06 | 73.11 | +0.40% | 2.41x | 8957 | STRONG 92/100 | HIGH 55/100 | Consider small entry |
| 2 | XRP/USD ⭐ | 0.95121 | 70.94 | +0.38% | 1.73x | 44956 | STRONG 90/100 | HIGH 55/100 | Consider small entry |
| 3 | XLM/USD ⭐ | 0.13188 | 69.00 | +0.38% | 6.30x | 18230 | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 4 | LTC/USD ⭐ | 41.79 | 66.31 | +0.43% | 2.77x | 12980 | STRONG 98/100 | HIGH 55/100 | Consider small entry |
| 5 | NIGHT/USD ⭐ | 0.04915 | 65.96 | +0.55% | 1.65x | 12151 | STRONG 88/100 | HIGH 55/100 | Consider small entry |
| 6 | SOL/USD ⭐ | 72.45 | 59.99 | +0.21% | 1.36x | 45798 | STRONG 85/100 | HIGH 55/100 | Watch |
| 7 | ETH/USD ⭐ | 1715.41 | 59.09 | +0.05% | 1.50x | 56880 | STRONG 75/100 | HIGH 55/100 | Watch |
| 8 | ZEC/USD ⭐ | 784.79 | 58.69 | +0.28% | 1.22x | 40274 | STRONG 74/100 | HIGH 62/100 | Watch |

**Same-run overlap:** XLM/USD, LTC/USD, XRP/USD, NIGHT/USD, ZEC/USD, SOL/USD, ETH/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
