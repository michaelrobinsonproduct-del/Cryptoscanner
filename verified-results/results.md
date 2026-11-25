# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-25T09:07:43.472421+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/45581950920
**Source SHA:** 858c8bc8ec5d7641ddb39cacd8aca91719f855b1
**Previous ledger commit:** a781a116db2b11d599cb35eb50075911f0c8cb37 (atomic ledger/results publication)
**Ledger generation:** 1697 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 8s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 628; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 610; valid market observations: 608; OHLC screened: 23.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | DRV/USD | 0.33605 | 89.784 | 72.642 | +6.93% | +0.43% | 2.50x | 19.9 | 2026-11-25T09:07:35.077484+00:00 | Not calibrated | STRONG 95/100 | HIGH 61/100 | Consider small entry | WATCH |
| 2 | VVV/USD | 24.701 | 72.802 | 57.418 | +0.66% | +0.08% | 3.91x | 4.5 | 2026-11-25T09:07:35.077484+00:00 | Not calibrated | STRONG 81/100 | HIGH 55/100 | Watch | WATCH |
| 3 | BABY/USD | 0.00889 | 57.200 | 59.699 | +7.63% | +0.34% | 0.58x | 33.9 | 2026-11-25T09:07:35.077484+00:00 | Not calibrated | MODERATE 49/100 | EXTREME 94/100 | Do nothing | WATCH |
| 4 | PROS/USD | 0.7037 | 51.216 | 54.398 | +4.92% | -0.91% | 1.14x | 24.1 | 2026-11-25T09:07:35.077484+00:00 | Not calibrated | WEAK 26/100 | EXTREME 85/100 | Do nothing | WATCH |
| 5 | CC/USD | 0.07527 | 29.348 | 32.469 | +0.29% | -0.39% | 0.88x | 8.0 | 2026-11-25T09:07:35.077484+00:00 | Not calibrated | WEAK 20/100 | VERY_HIGH 73/100 | Do nothing | WATCH |
| 6 | PEPE/USD | 3.467e-06 | 28.096 | 38.987 | +0.41% | -0.43% | 0.13x | 17.3 | 2026-11-25T09:07:35.077484+00:00 | Not calibrated | WEAK 14/100 | VERY_HIGH 82/100 | Do nothing | WATCH |
| 7 | ATOM/USD | 1.2622 | 27.266 | 34.528 | +1.35% | +0.20% | 0.17x | 14.3 | 2026-11-25T09:07:35.077484+00:00 | Not calibrated | WEAK 29/100 | VERY_HIGH 81/100 | Do nothing | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | DRV/USD | 72.642 | 0.33605 | +0.43% | 2.50x |
| 2 | BABY/USD | 59.699 | 0.00889 | +0.34% | 0.58x |
| 3 | VVV/USD | 57.418 | 24.701 | +0.08% | 3.91x |
| 4 | PROS/USD | 54.398 | 0.7037 | -0.91% | 1.14x |
| 5 | PEPE/USD | 38.987 | 3.467e-06 | -0.43% | 0.13x |
| 6 | ATOM/USD | 34.528 | 1.2622 | +0.20% | 0.17x |
| 7 | CC/USD | 32.469 | 0.07527 | -0.39% | 0.88x |

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

- Persisted scans: 1697; predictions: 14408; observations: 1028559.
- Matured sampled outcomes across 1/6/24/48h: 31004; gap abstentions: 22370. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 146 (sampled only; not a success-rate estimate).
- False positives / missed movers: NOT VERIFIED without eligible continuous outcome coverage.
- Baseline vs challenger: recorded as-of; unbiased held-out lift NOT MEASURED.
- Online Kraken /USD stablecoin-base pairs excluded: 18 (counted from this scan's online AssetPairs metadata, not inferred from price).
- Stablecoin base exclusions: BRL1, BUSD, DAI, EUR, EURC, EUROP, EURQ, EURR, EURT, FDUSD, FRAX, GUSD, PYUSD, QCAD, RLUSD, TGBP, TUSD, USD, USD1, USDC, USDD, USDE, USDG, USDQ, USDR, USDS, USDT, ZUSD.
- DEX: NOT USED; no DEX freshness gate.
- OHLC screening abstentions: 16; details in immutable scan JSON artifact.
- Storage: ledger and results published in one non-force Git commit and read back. Independent artifact recovery is NOT VERIFIED by this scan alone.
- Errors: none in successful committed scan; a failed workflow must not publish a SUCCESS report.

# Cryptoscanner — challenger and independent legacy-inspired WATCH

Paper only · risk is high or higher · 30%+ in 48h probability NOT CALIBRATED
Signal confidence 0–100 means setup strength only, NOT a win probability. Actions are research guidance; no trade authorization.

**Writer:** 45581950920 · **Generation:** 1697 · **Legacy run:** 45581950920
**Main quote time:** 2026-11-25T09:07:43.472421+00:00 · **Legacy report time:** 2026-11-25T09:08:45.742781+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | DRV/USD ⭐ | 0.33605 | 89.78 | +0.43% | 2.50x | STRONG 100/100 | HIGH 61/100 | Consider small entry |
| 2 | VVV/USD ⭐ | 24.701 | 72.80 | +0.08% | 3.91x | STRONG 91/100 | HIGH 55/100 | Watch |
| 3 | BABY/USD | 0.00889 | 57.20 | +0.34% | 0.58x | MODERATE 49/100 | EXTREME 94/100 | Do nothing |
| 4 | PROS/USD | 0.7037 | 51.22 | -0.91% | 1.14x | WEAK 26/100 | EXTREME 85/100 | Do nothing |
| 5 | CC/USD | 0.07527 | 29.35 | -0.39% | 0.88x | WEAK 20/100 | VERY_HIGH 73/100 | Do nothing |
| 6 | PEPE/USD | 3.467e-06 | 28.10 | -0.43% | 0.13x | WEAK 14/100 | VERY_HIGH 82/100 | Do nothing |
| 7 | ATOM/USD | 1.2622 | 27.27 | +0.20% | 0.17x | WEAK 29/100 | VERY_HIGH 81/100 | Do nothing |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | DRV/USD ⭐ | 0.33541 | 85.51 | +0.43% | 2.50x | 9377 | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 2 | VVV/USD ⭐ | 24.653 | 51.24 | +0.08% | 3.91x | 14126 | STRONG 81/100 | HIGH 55/100 | Watch |

**Same-run overlap:** DRV/USD, VVV/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
