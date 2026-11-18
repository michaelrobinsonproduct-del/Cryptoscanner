# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-18T21:45:27.265503+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/44404588043
**Source SHA:** b271b90a2cae9e5307600070ce7d0e510fe68996
**Previous ledger commit:** 963ccb5cb0e23060b621546ddb483528041d319a (atomic ledger/results publication)
**Ledger generation:** 675 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 5s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 627; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 609; valid market observations: 609; OHLC screened: 13.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | SENT/USD | 0.020257 | 74.096 | 74.453 | +8.51% | +0.63% | 0.65x | 3.5 | 2026-11-18T21:45:22.260376+00:00 | Not calibrated | MODERATE 67/100 | VERY_HIGH 82/100 | Watch | WATCH |
| 2 | VVV/USD | 21.346 | 71.071 | 55.183 | +1.52% | +0.87% | 2.15x | 5.2 | 2026-11-18T21:45:22.260376+00:00 | Not calibrated | STRONG 91/100 | HIGH 55/100 | Consider small entry | WATCH |
| 3 | TRX/USD | 0.308711 | 35.330 | 41.145 | +0.26% | -0.02% | 0.43x | 1.1 | 2026-11-18T21:45:22.260376+00:00 | Not calibrated | WEAK 23/100 | VERY_HIGH 76/100 | Do nothing | WATCH |
| 4 | WINGS/USD | 0.001862 | 18.160 | 31.900 | +1.58% | -6.02% | 2.13x | 21.6 | 2026-11-18T21:45:22.260376+00:00 | Not calibrated | WEAK 29/100 | EXTREME 89/100 | Do nothing | WATCH |
| 5 | RE/USD | 0.23358 | 17.470 | 25.856 | +0.53% | -0.30% | 0.31x | 17.1 | 2026-11-18T21:45:22.260376+00:00 | Not calibrated | WEAK 9/100 | EXTREME 94/100 | Do nothing | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | SENT/USD | 74.453 | 0.020257 | +0.63% | 0.65x |
| 2 | VVV/USD | 55.183 | 21.346 | +0.87% | 2.15x |
| 3 | TRX/USD | 41.145 | 0.308711 | -0.02% | 0.43x |
| 4 | WINGS/USD | 31.900 | 0.001862 | -6.02% | 2.13x |
| 5 | RE/USD | 25.856 | 0.23358 | -0.30% | 0.31x |

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

- Persisted scans: 675; predictions: 5552; observations: 408082.
- Matured sampled outcomes across 1/6/24/48h: 5228; gap abstentions: 13158. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 10 (sampled only; not a success-rate estimate).
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

**Writer:** 44404588043 · **Generation:** 675 · **Legacy run:** 44404588043
**Main quote time:** 2026-11-18T21:45:27.265503+00:00 · **Legacy report time:** 2026-11-18T21:45:57.467845+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | SENT/USD | 0.020257 | 74.10 | +0.63% | 0.65x | MODERATE 67/100 | VERY_HIGH 82/100 | Watch |
| 2 | VVV/USD ⭐ | 21.346 | 71.07 | +0.87% | 2.15x | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 3 | TRX/USD | 0.308711 | 35.33 | -0.02% | 0.43x | WEAK 23/100 | VERY_HIGH 76/100 | Do nothing |
| 4 | WINGS/USD | 0.001862 | 18.16 | -6.02% | 2.13x | WEAK 29/100 | EXTREME 89/100 | Do nothing |
| 5 | RE/USD | 0.23358 | 17.47 | -0.30% | 0.31x | WEAK 9/100 | EXTREME 94/100 | Do nothing |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | VVV/USD ⭐ | 21.346 | 60.57 | +0.87% | 2.15x | 7399 | STRONG 95/100 | HIGH 55/100 | Consider small entry |

**Same-run overlap:** VVV/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
