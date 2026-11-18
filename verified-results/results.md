# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-18T22:05:19.466167+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/44407969281
**Source SHA:** b271b90a2cae9e5307600070ce7d0e510fe68996
**Previous ledger commit:** bf454403ca6e6cf418ee10bf20b0d28878cfa1fe (atomic ledger/results publication)
**Ledger generation:** 679 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 5s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 627; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 609; valid market observations: 609; OHLC screened: 12.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | SENT/USD | 0.020531 | 90.267 | 69.632 | +9.97% | +1.13% | 2.57x | 13.2 | 2026-11-18T22:05:14.621080+00:00 | Not calibrated | STRONG 95/100 | VERY_HIGH 73/100 | Watch | WATCH |
| 2 | VVV/USD | 21.244 | 62.547 | 50.844 | +1.04% | -0.66% | 4.91x | 7.5 | 2026-11-18T22:05:14.621080+00:00 | Not calibrated | MODERATE 61/100 | HIGH 61/100 | Watch | WATCH |
| 3 | AKE/USD | 0.01035685 | 46.362 | 49.393 | +3.73% | +0.35% | 0.52x | 22.7 | 2026-11-18T22:05:14.621080+00:00 | Not calibrated | WEAK 43/100 | EXTREME 87/100 | Do nothing | WATCH |
| 4 | TRX/USD | 0.308791 | 45.429 | 41.458 | +0.29% | +0.02% | 1.39x | 0.9 | 2026-11-18T22:05:14.621080+00:00 | Not calibrated | MODERATE 58/100 | HIGH 55/100 | Watch | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | SENT/USD | 69.632 | 0.020531 | +1.13% | 2.57x |
| 2 | VVV/USD | 50.844 | 21.244 | -0.66% | 4.91x |
| 3 | AKE/USD | 49.393 | 0.01035685 | +0.35% | 0.52x |
| 4 | TRX/USD | 41.458 | 0.308791 | +0.02% | 1.39x |

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

- Persisted scans: 679; predictions: 5566; observations: 410518.
- Matured sampled outcomes across 1/6/24/48h: 5284; gap abstentions: 13170. Per-horizon counts require independent audit; do not infer held-out lift.
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

**Writer:** 44407969281 · **Generation:** 679 · **Legacy run:** 44407969281
**Main quote time:** 2026-11-18T22:05:19.466167+00:00 · **Legacy report time:** 2026-11-18T22:05:55.435901+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | SENT/USD ⭐ | 0.020531 | 90.27 | +1.13% | 2.57x | STRONG 100/100 | VERY_HIGH 73/100 | Watch |
| 2 | VVV/USD | 21.244 | 62.55 | -0.66% | 4.91x | MODERATE 61/100 | HIGH 61/100 | Watch |
| 3 | AKE/USD | 0.01035685 | 46.36 | +0.35% | 0.52x | WEAK 43/100 | EXTREME 87/100 | Do nothing |
| 4 | TRX/USD | 0.308791 | 45.43 | +0.02% | 1.39x | MODERATE 58/100 | HIGH 55/100 | Watch |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | SENT/USD ⭐ | 0.020476 | 80.38 | +1.13% | 2.57x | 6416 | STRONG 100/100 | HIGH 67/100 | Consider small entry |

**Same-run overlap:** SENT/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
