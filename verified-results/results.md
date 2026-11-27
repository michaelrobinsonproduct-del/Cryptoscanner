# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-27T17:32:25.442111+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/46042246175
**Source SHA:** 858c8bc8ec5d7641ddb39cacd8aca91719f855b1
**Previous ledger commit:** 6f06a4a8078dbc7d596005816ba400f788562d98 (atomic ledger/results publication)
**Ledger generation:** 2038 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 9s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 628; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 610; valid market observations: 605; OHLC screened: 24.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | ZEC/USD | 730.25 | 82.437 | 94.654 | +7.13% | -1.24% | 0.40x | 10.7 | 2026-11-27T17:32:16.712098+00:00 | Not calibrated | WEAK 41/100 | EXTREME 86/100 | Do nothing | WATCH |
| 2 | SPACE/USD | 0.004177 | 69.554 | 70.974 | +7.88% | +0.43% | 0.64x | 9.6 | 2026-11-27T17:32:16.712098+00:00 | Not calibrated | MODERATE 65/100 | VERY_HIGH 82/100 | Watch | WATCH |
| 3 | XDG/USD | 0.0575779 | 65.504 | 68.117 | +2.13% | -0.04% | 0.76x | 3.7 | 2026-11-27T17:32:16.712098+00:00 | Not calibrated | WEAK 38/100 | HIGH 68/100 | Watch | WATCH |
| 4 | SOL/USD | 71.7 | 64.173 | 61.802 | +1.07% | -0.28% | 1.38x | 1.4 | 2026-11-27T17:32:16.712098+00:00 | Not calibrated | MODERATE 52/100 | HIGH 61/100 | Watch | WATCH |
| 5 | NIGHT/USD | 0.04957 | 63.181 | 68.405 | +2.27% | -0.40% | 0.68x | 4.0 | 2026-11-27T17:32:16.712098+00:00 | Not calibrated | WEAK 37/100 | VERY_HIGH 76/100 | Watch | WATCH |
| 6 | HYPE/USD | 63.78 | 62.138 | 70.982 | +2.51% | -0.75% | 0.49x | 3.1 | 2026-11-27T17:32:16.712098+00:00 | Not calibrated | WEAK 36/100 | VERY_HIGH 76/100 | Watch | WATCH |
| 7 | FET/USD | 0.1259 | 62.087 | 57.185 | +4.57% | +0.16% | 1.41x | 23.9 | 2026-11-27T17:32:16.712098+00:00 | Not calibrated | MODERATE 56/100 | HIGH 67/100 | Watch | WATCH |
| 8 | UNI/USD | 4.7523 | 59.621 | 66.068 | +2.20% | -0.52% | 0.62x | 3.4 | 2026-11-27T17:32:16.712098+00:00 | Not calibrated | WEAK 35/100 | VERY_HIGH 76/100 | Watch | WATCH |
| 9 | XRP/USD | 0.94672 | 53.832 | 57.895 | +0.42% | -0.21% | 0.70x | 0.1 | 2026-11-27T17:32:16.712098+00:00 | Not calibrated | WEAK 32/100 | VERY_HIGH 76/100 | Do nothing | WATCH |
| 10 | LINK/USD | 9.31332 | 52.072 | 56.305 | +0.48% | -0.10% | 0.63x | 4.2 | 2026-11-27T17:32:16.712098+00:00 | Not calibrated | WEAK 31/100 | VERY_HIGH 76/100 | Do nothing | WATCH |
| 11 | PAXG/USD | 3624.01 | 46.248 | 55.196 | +1.89% | +0.17% | 0.02x | 2.4 | 2026-11-27T17:32:16.712098+00:00 | Not calibrated | WEAK 43/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 12 | XAUT/USD | 3626.2 | 43.583 | 50.195 | +1.87% | +0.14% | 0.27x | 0.6 | 2026-11-27T17:32:16.712098+00:00 | Not calibrated | WEAK 42/100 | VERY_HIGH 70/100 | Watch | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | ZEC/USD | 94.654 | 730.25 | -1.24% | 0.40x |
| 2 | HYPE/USD | 70.982 | 63.78 | -0.75% | 0.49x |
| 3 | SPACE/USD | 70.974 | 0.004177 | +0.43% | 0.64x |
| 4 | NIGHT/USD | 68.405 | 0.04957 | -0.40% | 0.68x |
| 5 | XDG/USD | 68.117 | 0.0575779 | -0.04% | 0.76x |
| 6 | UNI/USD | 66.068 | 4.7523 | -0.52% | 0.62x |
| 7 | SOL/USD | 61.802 | 71.7 | -0.28% | 1.38x |
| 8 | XRP/USD | 57.895 | 0.94672 | -0.21% | 0.70x |
| 9 | FET/USD | 57.185 | 0.1259 | +0.16% | 1.41x |
| 10 | LINK/USD | 56.305 | 9.31332 | -0.10% | 0.63x |
| 11 | PAXG/USD | 55.196 | 3624.01 | +0.17% | 0.02x |
| 12 | XAUT/USD | 50.195 | 3626.2 | +0.14% | 0.27x |

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

- Persisted scans: 2038; predictions: 18158; observations: 1234099.
- Matured sampled outcomes across 1/6/24/48h: 40710; gap abstentions: 25968. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 153 (sampled only; not a success-rate estimate).
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

**Writer:** 46042246175 · **Generation:** 2038 · **Legacy run:** 46042246175
**Main quote time:** 2026-11-27T17:32:25.442111+00:00 · **Legacy report time:** 2026-11-27T17:33:10.305200+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | ZEC/USD | 730.25 | 82.44 | -1.24% | 0.40x | WEAK 41/100 | EXTREME 86/100 | Do nothing |
| 2 | SPACE/USD | 0.004177 | 69.55 | +0.43% | 0.64x | MODERATE 65/100 | VERY_HIGH 82/100 | Watch |
| 3 | XDG/USD | 0.0575779 | 65.50 | -0.04% | 0.76x | WEAK 38/100 | HIGH 68/100 | Watch |
| 4 | SOL/USD | 71.7 | 64.17 | -0.28% | 1.38x | MODERATE 52/100 | HIGH 61/100 | Watch |
| 5 | NIGHT/USD | 0.04957 | 63.18 | -0.40% | 0.68x | WEAK 37/100 | VERY_HIGH 76/100 | Watch |
| 6 | HYPE/USD | 63.78 | 62.14 | -0.75% | 0.49x | WEAK 36/100 | VERY_HIGH 76/100 | Watch |
| 7 | FET/USD ⭐ | 0.1259 | 62.09 | +0.16% | 1.41x | MODERATE 66/100 | HIGH 67/100 | Watch |
| 8 | UNI/USD | 4.7523 | 59.62 | -0.52% | 0.62x | WEAK 35/100 | VERY_HIGH 76/100 | Watch |
| 9 | XRP/USD | 0.94672 | 53.83 | -0.21% | 0.70x | WEAK 32/100 | VERY_HIGH 76/100 | Do nothing |
| 10 | LINK/USD | 9.31332 | 52.07 | -0.10% | 0.63x | WEAK 31/100 | VERY_HIGH 76/100 | Do nothing |
| 11 | PAXG/USD | 3624.01 | 46.25 | +0.17% | 0.02x | WEAK 43/100 | VERY_HIGH 70/100 | Watch |
| 12 | XAUT/USD | 3626.2 | 43.58 | +0.14% | 0.27x | WEAK 42/100 | VERY_HIGH 70/100 | Watch |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | FET/USD ⭐ | 0.1258 | 76.41 | +0.16% | 1.41x | 3785 | STRONG 73/100 | HIGH 67/100 | Watch |

**Same-run overlap:** FET/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
