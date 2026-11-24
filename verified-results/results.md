# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-24T15:01:45.350942+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/45420279049
**Source SHA:** 858c8bc8ec5d7641ddb39cacd8aca91719f855b1
**Previous ledger commit:** 403ff8437468a340a3d6ff91e224599b7c7d7771 (atomic ledger/results publication)
**Ledger generation:** 1589 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 7s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 628; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 610; valid market observations: 608; OHLC screened: 15.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | VVV/USD | 25.335 | 88.046 | 74.278 | +3.63% | -0.25% | 6.67x | 12.2 | 2026-11-24T15:01:38.634826+00:00 | Not calibrated | MODERATE 69/100 | HIGH 67/100 | Watch | WATCH |
| 2 | ICNT/USD | 0.331 | 63.101 | 64.353 | +7.09% | +0.03% | 0.86x | 27.2 | 2026-11-24T15:01:38.634826+00:00 | Not calibrated | WEAK 42/100 | VERY_HIGH 79/100 | Watch | WATCH |
| 3 | 2Z/USD | 0.01644 | 62.823 | 63.044 | +5.05% | +0.92% | 0.52x | 6.1 | 2026-11-24T15:01:38.634826+00:00 | Not calibrated | MODERATE 61/100 | VERY_HIGH 82/100 | Watch | WATCH |
| 4 | NIGHT/USD | 0.04873 | 62.607 | 45.861 | +1.20% | +0.35% | 6.22x | 10.3 | 2026-11-24T15:01:38.634826+00:00 | Not calibrated | STRONG 81/100 | HIGH 61/100 | Watch | WATCH |
| 5 | GBP/USD | 1.31093 | 59.204 | 59.011 | +0.59% | +0.01% | 1.02x | 0.2 | 2026-11-24T15:01:38.634826+00:00 | Not calibrated | MODERATE 55/100 | HIGH 62/100 | Watch | WATCH |
| 6 | XMR/USD | 495.64 | 53.536 | 63.102 | +1.98% | -0.29% | 0.19x | 11.5 | 2026-11-24T15:01:38.634826+00:00 | Not calibrated | WEAK 27/100 | VERY_HIGH 82/100 | Do nothing | WATCH |
| 7 | BAT/USD | 0.07756 | 38.848 | 35.425 | +0.51% | +0.57% | 1.06x | 1.3 | 2026-11-24T15:01:38.634826+00:00 | Not calibrated | MODERATE 54/100 | HIGH 67/100 | Watch | WATCH |
| 8 | AUD/USD | 0.66528 | 37.510 | 43.700 | +0.41% | -0.01% | 0.39x | 1.4 | 2026-11-24T15:01:38.634826+00:00 | Not calibrated | WEAK 24/100 | VERY_HIGH 76/100 | Do nothing | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | VVV/USD | 74.278 | 25.335 | -0.25% | 6.67x |
| 2 | ICNT/USD | 64.353 | 0.331 | +0.03% | 0.86x |
| 3 | XMR/USD | 63.102 | 495.64 | -0.29% | 0.19x |
| 4 | 2Z/USD | 63.044 | 0.01644 | +0.92% | 0.52x |
| 5 | GBP/USD | 59.011 | 1.31093 | +0.01% | 1.02x |
| 6 | NIGHT/USD | 45.861 | 0.04873 | +0.35% | 6.22x |
| 7 | AUD/USD | 43.700 | 0.66528 | -0.01% | 0.39x |
| 8 | BAT/USD | 35.425 | 0.07756 | +0.57% | 1.06x |

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

- Persisted scans: 1589; predictions: 13698; observations: 962795.
- Matured sampled outcomes across 1/6/24/48h: 27033; gap abstentions: 22370. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 143 (sampled only; not a success-rate estimate).
- False positives / missed movers: NOT VERIFIED without eligible continuous outcome coverage.
- Baseline vs challenger: recorded as-of; unbiased held-out lift NOT MEASURED.
- Online Kraken /USD stablecoin-base pairs excluded: 18 (counted from this scan's online AssetPairs metadata, not inferred from price).
- Stablecoin base exclusions: BRL1, BUSD, DAI, EUR, EURC, EUROP, EURQ, EURR, EURT, FDUSD, FRAX, GUSD, PYUSD, QCAD, RLUSD, TGBP, TUSD, USD, USD1, USDC, USDD, USDE, USDG, USDQ, USDR, USDS, USDT, ZUSD.
- DEX: NOT USED; no DEX freshness gate.
- OHLC screening abstentions: 7; details in immutable scan JSON artifact.
- Storage: ledger and results published in one non-force Git commit and read back. Independent artifact recovery is NOT VERIFIED by this scan alone.
- Errors: none in successful committed scan; a failed workflow must not publish a SUCCESS report.

# Cryptoscanner — challenger and independent legacy-inspired WATCH

Paper only · risk is high or higher · 30%+ in 48h probability NOT CALIBRATED
Signal confidence 0–100 means setup strength only, NOT a win probability. Actions are research guidance; no trade authorization.

**Writer:** 45420279049 · **Generation:** 1589 · **Legacy run:** 45420279049
**Main quote time:** 2026-11-24T15:01:45.350942+00:00 · **Legacy report time:** 2026-11-24T15:02:34.902293+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | VVV/USD | 25.335 | 88.05 | -0.25% | 6.67x | MODERATE 69/100 | HIGH 67/100 | Watch |
| 2 | ICNT/USD | 0.331 | 63.10 | +0.03% | 0.86x | WEAK 42/100 | VERY_HIGH 79/100 | Watch |
| 3 | 2Z/USD | 0.01644 | 62.82 | +0.92% | 0.52x | MODERATE 61/100 | VERY_HIGH 82/100 | Watch |
| 4 | NIGHT/USD ⭐ | 0.04873 | 62.61 | +0.35% | 6.22x | STRONG 91/100 | HIGH 61/100 | Consider small entry |
| 5 | GBP/USD | 1.31093 | 59.20 | +0.01% | 1.02x | MODERATE 55/100 | HIGH 62/100 | Watch |
| 6 | XMR/USD | 495.64 | 53.54 | -0.29% | 0.19x | WEAK 27/100 | VERY_HIGH 82/100 | Do nothing |
| 7 | BAT/USD | 0.07756 | 38.85 | +0.57% | 1.06x | MODERATE 54/100 | HIGH 67/100 | Watch |
| 8 | AUD/USD | 0.66528 | 37.51 | -0.01% | 0.39x | WEAK 24/100 | VERY_HIGH 76/100 | Do nothing |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | NIGHT/USD ⭐ | 0.04872 | 52.79 | +0.35% | 6.22x | 10144 | STRONG 86/100 | HIGH 61/100 | Consider small entry |

**Same-run overlap:** NIGHT/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
