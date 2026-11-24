# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-24T22:01:49.985032+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/45496544979
**Source SHA:** 858c8bc8ec5d7641ddb39cacd8aca91719f855b1
**Previous ledger commit:** 0f4871dbd09236972c52d126d37a82e25fa4789a (atomic ledger/results publication)
**Ledger generation:** 1631 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 4s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 628; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 610; valid market observations: 609; OHLC screened: 13.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | XMR/USD | 504.95 | 77.200 | 74.529 | +3.89% | +0.52% | 1.01x | 15.5 | 2026-11-24T22:01:45.553662+00:00 | Not calibrated | MODERATE 69/100 | HIGH 68/100 | Watch | WATCH |
| 2 | GBP/USD | 1.3111 | 60.459 | 58.988 | +0.60% | +0.00% | 1.15x | 0.5 | 2026-11-24T22:01:45.553662+00:00 | Not calibrated | MODERATE 55/100 | HIGH 62/100 | Watch | WATCH |
| 3 | PEPE/USD | 3.484e-06 | 60.351 | 56.196 | +1.81% | +0.17% | 1.33x | 2.9 | 2026-11-24T22:01:45.553662+00:00 | Not calibrated | MODERATE 65/100 | HIGH 55/100 | Watch | WATCH |
| 4 | SKY/USD | 0.04084 | 59.355 | 40.414 | +1.11% | +0.79% | 10.38x | 2.4 | 2026-11-24T22:01:45.553662+00:00 | Not calibrated | STRONG 85/100 | HIGH 60/100 | Watch | WATCH |
| 5 | NIGHT/USD | 0.04862 | 52.485 | 45.570 | +0.98% | +0.31% | 1.54x | 2.1 | 2026-11-24T22:01:45.553662+00:00 | Not calibrated | STRONG 71/100 | HIGH 55/100 | Watch | WATCH |
| 6 | LUNA/USD | 4.528e-05 | 46.599 | 57.635 | +4.16% | -0.83% | 0.31x | 6.6 | 2026-11-24T22:01:45.553662+00:00 | Not calibrated | WEAK 28/100 | VERY_HIGH 81/100 | Do nothing | WATCH |
| 7 | REKT/USD | 7.95e-08 | 42.656 | 27.249 | +1.53% | +1.27% | 1.91x | 37.9 | 2026-11-24T22:01:45.553662+00:00 | Not calibrated | MODERATE 51/100 | VERY_HIGH 72/100 | Watch | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | XMR/USD | 74.529 | 504.95 | +0.52% | 1.01x |
| 2 | GBP/USD | 58.988 | 1.3111 | +0.00% | 1.15x |
| 3 | LUNA/USD | 57.635 | 4.528e-05 | -0.83% | 0.31x |
| 4 | PEPE/USD | 56.196 | 3.484e-06 | +0.17% | 1.33x |
| 5 | NIGHT/USD | 45.570 | 0.04862 | +0.31% | 1.54x |
| 6 | SKY/USD | 40.414 | 0.04084 | +0.79% | 10.38x |
| 7 | REKT/USD | 27.249 | 7.95e-08 | +1.27% | 1.91x |

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

- Persisted scans: 1631; predictions: 13974; observations: 988370.
- Matured sampled outcomes across 1/6/24/48h: 28739; gap abstentions: 22370. Per-horizon counts require independent audit; do not infer held-out lift.
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

**Writer:** 45496544979 · **Generation:** 1631 · **Legacy run:** 45496544979
**Main quote time:** 2026-11-24T22:01:49.985032+00:00 · **Legacy report time:** 2026-11-24T22:02:40.316671+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | XMR/USD ⭐ | 504.95 | 77.20 | +0.52% | 1.01x | STRONG 79/100 | HIGH 68/100 | Watch |
| 2 | GBP/USD | 1.3111 | 60.46 | +0.00% | 1.15x | MODERATE 55/100 | HIGH 62/100 | Watch |
| 3 | PEPE/USD ⭐ | 3.484e-06 | 60.35 | +0.17% | 1.33x | STRONG 75/100 | HIGH 55/100 | Watch |
| 4 | SKY/USD ⭐ | 0.04084 | 59.35 | +0.79% | 10.38x | STRONG 95/100 | HIGH 60/100 | Consider small entry |
| 5 | NIGHT/USD ⭐ | 0.04862 | 52.48 | +0.31% | 1.54x | STRONG 81/100 | HIGH 55/100 | Consider small entry |
| 6 | LUNA/USD | 4.528e-05 | 46.60 | -0.83% | 0.31x | WEAK 28/100 | VERY_HIGH 81/100 | Do nothing |
| 7 | REKT/USD ⭐ | 7.95e-08 | 42.66 | +1.27% | 1.91x | MODERATE 61/100 | VERY_HIGH 72/100 | Watch |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | XMR/USD ⭐ | 505.88 | 86.59 | +0.52% | 1.01x | 7567 | STRONG 83/100 | HIGH 68/100 | Watch |
| 2 | PEPE/USD ⭐ | 3.483e-06 | 63.45 | +0.17% | 1.33x | 6710 | STRONG 77/100 | HIGH 55/100 | Watch |
| 3 | SKY/USD ⭐ | 0.04084 | 53.25 | +0.79% | 10.38x | 4431 | STRONG 92/100 | HIGH 60/100 | Consider small entry |
| 4 | REKT/USD ⭐ | 7.95e-08 | 51.10 | +1.27% | 1.91x | 12280 | MODERATE 66/100 | VERY_HIGH 72/100 | Watch |
| 5 | NIGHT/USD ⭐ | 0.04867 | 50.66 | +0.31% | 1.54x | 9195 | STRONG 80/100 | HIGH 55/100 | Consider small entry |

**Same-run overlap:** XMR/USD, PEPE/USD, SKY/USD, NIGHT/USD, REKT/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
