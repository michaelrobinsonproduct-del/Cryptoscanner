# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-28T00:52:45.284253+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/46089944386
**Source SHA:** 858c8bc8ec5d7641ddb39cacd8aca91719f855b1
**Previous ledger commit:** fe83f0471243968b9313e093e33de97dcc81099e (atomic ledger/results publication)
**Ledger generation:** 2083 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 7s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 628; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 610; valid market observations: 605; OHLC screened: 19.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | TAO/USD | 187.4538 | 70.623 | 54.804 | +0.27% | +0.16% | 4.69x | 4.1 | 2026-11-28T00:52:38.490969+00:00 | Not calibrated | STRONG 80/100 | HIGH 55/100 | Watch | WATCH |
| 2 | DRV/USD | 0.36541 | 56.509 | 39.487 | +0.71% | +0.40% | 7.62x | 0.8 | 2026-11-28T00:52:38.490969+00:00 | Not calibrated | STRONG 83/100 | HIGH 60/100 | Watch | WATCH |
| 3 | BCH/USD | 208.08 | 53.478 | 39.319 | +0.52% | +0.22% | 2.31x | 4.8 | 2026-11-28T00:52:38.490969+00:00 | Not calibrated | STRONG 82/100 | HIGH 55/100 | Watch | WATCH |
| 4 | HYPE/USD | 63.67 | 45.299 | 55.414 | +0.28% | -0.14% | 0.06x | 3.1 | 2026-11-28T00:52:38.490969+00:00 | Not calibrated | WEAK 28/100 | VERY_HIGH 76/100 | Do nothing | WATCH |
| 5 | BAT/USD | 0.07538 | 44.451 | 32.697 | +0.53% | +0.57% | 1.89x | 4.0 | 2026-11-28T00:52:38.490969+00:00 | Not calibrated | MODERATE 67/100 | HIGH 67/100 | Watch | WATCH |
| 6 | SKY/USD | 0.05258 | 40.073 | 45.103 | +1.31% | +0.13% | 0.43x | 7.6 | 2026-11-28T00:52:38.490969+00:00 | Not calibrated | WEAK 40/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 7 | SENT/USD | 0.023833 | 38.423 | 31.515 | +0.50% | +1.35% | 1.02x | 5.5 | 2026-11-28T00:52:38.490969+00:00 | Not calibrated | MODERATE 54/100 | VERY_HIGH 74/100 | Watch | WATCH |
| 8 | SPX/USD | 0.2734 | 19.456 | 29.139 | +0.37% | +0.00% | 0.03x | 11.0 | 2026-11-28T00:52:38.490969+00:00 | Not calibrated | WEAK 25/100 | VERY_HIGH 81/100 | Do nothing | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | HYPE/USD | 55.414 | 63.67 | -0.14% | 0.06x |
| 2 | TAO/USD | 54.804 | 187.4538 | +0.16% | 4.69x |
| 3 | SKY/USD | 45.103 | 0.05258 | +0.13% | 0.43x |
| 4 | DRV/USD | 39.487 | 0.36541 | +0.40% | 7.62x |
| 5 | BCH/USD | 39.319 | 208.08 | +0.22% | 2.31x |
| 6 | BAT/USD | 32.697 | 0.07538 | +0.57% | 1.89x |
| 7 | SENT/USD | 31.515 | 0.023833 | +1.35% | 1.02x |
| 8 | SPX/USD | 29.139 | 0.2734 | +0.00% | 0.03x |

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

- Persisted scans: 2083; predictions: 18661; observations: 1261344.
- Matured sampled outcomes across 1/6/24/48h: 42837; gap abstentions: 25968. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 155 (sampled only; not a success-rate estimate).
- False positives / missed movers: NOT VERIFIED without eligible continuous outcome coverage.
- Baseline vs challenger: recorded as-of; unbiased held-out lift NOT MEASURED.
- Online Kraken /USD stablecoin-base pairs excluded: 18 (counted from this scan's online AssetPairs metadata, not inferred from price).
- Stablecoin base exclusions: BRL1, BUSD, DAI, EUR, EURC, EUROP, EURQ, EURR, EURT, FDUSD, FRAX, GUSD, PYUSD, QCAD, RLUSD, TGBP, TUSD, USD, USD1, USDC, USDD, USDE, USDG, USDQ, USDR, USDS, USDT, ZUSD.
- DEX: NOT USED; no DEX freshness gate.
- OHLC screening abstentions: 11; details in immutable scan JSON artifact.
- Storage: ledger and results published in one non-force Git commit and read back. Independent artifact recovery is NOT VERIFIED by this scan alone.
- Errors: none in successful committed scan; a failed workflow must not publish a SUCCESS report.

# Cryptoscanner — challenger and independent legacy-inspired WATCH

Paper only · risk is high or higher · 30%+ in 48h probability NOT CALIBRATED
Signal confidence 0–100 means setup strength only, NOT a win probability. Actions are research guidance; no trade authorization.

**Writer:** 46089944386 · **Generation:** 2083 · **Legacy run:** 46089944386
**Main quote time:** 2026-11-28T00:52:45.284253+00:00 · **Legacy report time:** 2026-11-28T00:53:42.630859+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | TAO/USD ⭐ | 187.4538 | 70.62 | +0.16% | 4.69x | STRONG 90/100 | HIGH 55/100 | Watch |
| 2 | DRV/USD ⭐ | 0.36541 | 56.51 | +0.40% | 7.62x | STRONG 93/100 | HIGH 60/100 | Consider small entry |
| 3 | BCH/USD ⭐ | 208.08 | 53.48 | +0.22% | 2.31x | STRONG 92/100 | HIGH 55/100 | Consider small entry |
| 4 | HYPE/USD | 63.67 | 45.30 | -0.14% | 0.06x | WEAK 28/100 | VERY_HIGH 76/100 | Do nothing |
| 5 | BAT/USD | 0.07538 | 44.45 | +0.57% | 1.89x | MODERATE 67/100 | HIGH 67/100 | Watch |
| 6 | SKY/USD | 0.05258 | 40.07 | +0.13% | 0.43x | WEAK 40/100 | VERY_HIGH 70/100 | Watch |
| 7 | SENT/USD ⭐ | 0.023833 | 38.42 | +1.35% | 1.02x | MODERATE 64/100 | VERY_HIGH 74/100 | Watch |
| 8 | SPX/USD | 0.2734 | 19.46 | +0.00% | 0.03x | WEAK 25/100 | VERY_HIGH 81/100 | Do nothing |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | XRP/USD | 0.95045 | 58.56 | +0.08% | 1.87x | 40425 | MODERATE 64/100 | HIGH 55/100 | Watch |
| 2 | DRV/USD ⭐ | 0.36541 | 56.06 | +0.40% | 7.62x | 4983 | STRONG 93/100 | HIGH 60/100 | Consider small entry |
| 3 | TAO/USD ⭐ | 187.5572 | 53.41 | +0.16% | 4.69x | 9248 | STRONG 82/100 | HIGH 55/100 | Watch |
| 4 | BCH/USD ⭐ | 208.4 | 45.29 | +0.22% | 2.31x | 3266 | STRONG 88/100 | HIGH 55/100 | Consider small entry |
| 5 | SENT/USD ⭐ | 0.02382 | 36.83 | +1.35% | 1.02x | 3544 | MODERATE 63/100 | VERY_HIGH 74/100 | Watch |

**Same-run overlap:** TAO/USD, DRV/USD, BCH/USD, SENT/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
