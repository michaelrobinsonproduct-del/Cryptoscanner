# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-24T23:22:08.621912+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/45508992773
**Source SHA:** 858c8bc8ec5d7641ddb39cacd8aca91719f855b1
**Previous ledger commit:** 7e6e5a0fdcc31b066185971d02d9adbf08f225f8 (atomic ledger/results publication)
**Ledger generation:** 1639 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 4s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 628; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 610; valid market observations: 609; OHLC screened: 13.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | XMR/USD | 509.59 | 81.290 | 86.297 | +4.85% | -0.13% | 0.56x | 5.3 | 2026-11-24T23:22:04.883095+00:00 | Not calibrated | MODERATE 46/100 | VERY_HIGH 76/100 | Watch | WATCH |
| 2 | SKY/USD | 0.04105 | 58.459 | 41.626 | +1.63% | +0.37% | 3.33x | 7.3 | 2026-11-24T23:22:04.883095+00:00 | Not calibrated | STRONG 84/100 | HIGH 60/100 | Watch | WATCH |
| 3 | VVV/USD | 24.796 | 54.801 | 60.726 | +1.42% | -0.35% | 0.58x | 8.5 | 2026-11-24T23:22:04.883095+00:00 | Not calibrated | WEAK 32/100 | VERY_HIGH 76/100 | Do nothing | WATCH |
| 4 | GBP/USD | 1.31076 | 53.002 | 58.919 | +0.58% | +0.01% | 0.40x | 0.2 | 2026-11-24T23:22:04.883095+00:00 | Not calibrated | MODERATE 47/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 5 | ZEUS/USD | 0.00457 | 50.447 | 51.051 | +4.34% | +0.88% | 0.50x | 21.9 | 2026-11-24T23:22:04.883095+00:00 | Not calibrated | MODERATE 45/100 | EXTREME 94/100 | Do nothing | WATCH |
| 6 | NIGHT/USD | 0.0491 | 47.103 | 48.891 | +1.97% | +0.45% | 0.60x | 8.2 | 2026-11-24T23:22:04.883095+00:00 | Not calibrated | MODERATE 54/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 7 | PEPE/USD | 3.469e-06 | 44.399 | 50.691 | +1.37% | -0.29% | 0.51x | 8.7 | 2026-11-24T23:22:04.883095+00:00 | Not calibrated | WEAK 27/100 | VERY_HIGH 76/100 | Do nothing | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | XMR/USD | 86.297 | 509.59 | -0.13% | 0.56x |
| 2 | VVV/USD | 60.726 | 24.796 | -0.35% | 0.58x |
| 3 | GBP/USD | 58.919 | 1.31076 | +0.01% | 0.40x |
| 4 | ZEUS/USD | 51.051 | 0.00457 | +0.88% | 0.50x |
| 5 | PEPE/USD | 50.691 | 3.469e-06 | -0.29% | 0.51x |
| 6 | NIGHT/USD | 48.891 | 0.0491 | +0.45% | 0.60x |
| 7 | SKY/USD | 41.626 | 0.04105 | +0.37% | 3.33x |

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

- Persisted scans: 1639; predictions: 14035; observations: 993242.
- Matured sampled outcomes across 1/6/24/48h: 29034; gap abstentions: 22370. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 143 (sampled only; not a success-rate estimate).
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

**Writer:** 45508992773 · **Generation:** 1639 · **Legacy run:** 45508992773
**Main quote time:** 2026-11-24T23:22:08.621912+00:00 · **Legacy report time:** 2026-11-24T23:23:14.594631+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | XMR/USD | 509.59 | 81.29 | -0.13% | 0.56x | MODERATE 46/100 | VERY_HIGH 76/100 | Watch |
| 2 | SKY/USD ⭐ | 0.04105 | 58.46 | +0.37% | 3.33x | STRONG 94/100 | HIGH 60/100 | Consider small entry |
| 3 | VVV/USD | 24.796 | 54.80 | -0.35% | 0.58x | WEAK 32/100 | VERY_HIGH 76/100 | Do nothing |
| 4 | GBP/USD | 1.31076 | 53.00 | +0.01% | 0.40x | MODERATE 47/100 | VERY_HIGH 70/100 | Watch |
| 5 | ZEUS/USD | 0.00457 | 50.45 | +0.88% | 0.50x | MODERATE 45/100 | EXTREME 94/100 | Do nothing |
| 6 | NIGHT/USD | 0.0491 | 47.10 | +0.45% | 0.60x | MODERATE 54/100 | VERY_HIGH 70/100 | Watch |
| 7 | PEPE/USD | 3.469e-06 | 44.40 | -0.29% | 0.51x | WEAK 27/100 | VERY_HIGH 76/100 | Do nothing |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | SKY/USD ⭐ | 0.04105 | 63.15 | +0.37% | 3.33x | 4455 | STRONG 97/100 | HIGH 60/100 | Consider small entry |

**Same-run overlap:** SKY/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
