# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-25T00:42:42.202634+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/45519782209
**Source SHA:** 858c8bc8ec5d7641ddb39cacd8aca91719f855b1
**Previous ledger commit:** 354ed6e6d80c3acd12e607e43c091b55822221a5 (atomic ledger/results publication)
**Ledger generation:** 1647 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 4s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 628; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 610; valid market observations: 609; OHLC screened: 15.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | PEARL/USD | 2.1596 | 61.378 | 39.575 | +0.91% | +1.36% | 2.57x | 10.6 | 2026-11-25T00:42:38.137719+00:00 | Not calibrated | STRONG 81/100 | HIGH 61/100 | Watch | WATCH |
| 2 | SKY/USD | 0.04215 | 53.528 | 46.771 | +2.86% | +1.78% | 0.78x | 14.3 | 2026-11-25T00:42:38.137719+00:00 | Not calibrated | MODERATE 52/100 | VERY_HIGH 73/100 | Watch | WATCH |
| 3 | SYRUP/USD | 0.06998 | 34.902 | 26.140 | +0.45% | -0.54% | 2.15x | 17.1 | 2026-11-25T00:42:38.137719+00:00 | Not calibrated | WEAK 42/100 | VERY_HIGH 79/100 | Watch | WATCH |
| 4 | DRV/USD | 0.31704 | 33.663 | 30.484 | +0.88% | +0.56% | 1.04x | 19.9 | 2026-11-25T00:42:38.137719+00:00 | Not calibrated | MODERATE 47/100 | VERY_HIGH 73/100 | Watch | WATCH |
| 5 | BLESS/USD | 0.017677 | 16.043 | 27.246 | +0.49% | -0.84% | 0.30x | 27.2 | 2026-11-25T00:42:38.137719+00:00 | Not calibrated | WEAK 3/100 | EXTREME 88/100 | Do nothing | WATCH |
| 6 | POND/USD | 0.001187 | -6.351 | 17.172 | +0.94% | -4.56% | 0.93x | 42.3 | 2026-11-25T00:42:38.137719+00:00 | Not calibrated | WEAK 0/100 | EXTREME 99/100 | Do nothing | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | SKY/USD | 46.771 | 0.04215 | +1.78% | 0.78x |
| 2 | PEARL/USD | 39.575 | 2.1596 | +1.36% | 2.57x |
| 3 | DRV/USD | 30.484 | 0.31704 | +0.56% | 1.04x |
| 4 | BLESS/USD | 27.246 | 0.017677 | -0.84% | 0.30x |
| 5 | SYRUP/USD | 26.140 | 0.06998 | -0.54% | 2.15x |
| 6 | POND/USD | 17.172 | 0.001187 | -4.56% | 0.93x |

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

- Persisted scans: 1647; predictions: 14081; observations: 998114.
- Matured sampled outcomes across 1/6/24/48h: 29331; gap abstentions: 22370. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 143 (sampled only; not a success-rate estimate).
- False positives / missed movers: NOT VERIFIED without eligible continuous outcome coverage.
- Baseline vs challenger: recorded as-of; unbiased held-out lift NOT MEASURED.
- Online Kraken /USD stablecoin-base pairs excluded: 18 (counted from this scan's online AssetPairs metadata, not inferred from price).
- Stablecoin base exclusions: BRL1, BUSD, DAI, EUR, EURC, EUROP, EURQ, EURR, EURT, FDUSD, FRAX, GUSD, PYUSD, QCAD, RLUSD, TGBP, TUSD, USD, USD1, USDC, USDD, USDE, USDG, USDQ, USDR, USDS, USDT, ZUSD.
- DEX: NOT USED; no DEX freshness gate.
- OHLC screening abstentions: 9; details in immutable scan JSON artifact.
- Storage: ledger and results published in one non-force Git commit and read back. Independent artifact recovery is NOT VERIFIED by this scan alone.
- Errors: none in successful committed scan; a failed workflow must not publish a SUCCESS report.

# Cryptoscanner — challenger and independent legacy-inspired WATCH

Paper only · risk is high or higher · 30%+ in 48h probability NOT CALIBRATED
Signal confidence 0–100 means setup strength only, NOT a win probability. Actions are research guidance; no trade authorization.

**Writer:** 45519782209 · **Generation:** 1647 · **Legacy run:** 45519782209
**Main quote time:** 2026-11-25T00:42:42.202634+00:00 · **Legacy report time:** 2026-11-25T00:43:56.647343+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | PEARL/USD ⭐ | 2.1596 | 61.38 | +1.36% | 2.57x | STRONG 91/100 | HIGH 61/100 | Consider small entry |
| 2 | SKY/USD | 0.04215 | 53.53 | +1.78% | 0.78x | MODERATE 52/100 | VERY_HIGH 73/100 | Watch |
| 3 | SYRUP/USD | 0.06998 | 34.90 | -0.54% | 2.15x | WEAK 42/100 | VERY_HIGH 79/100 | Watch |
| 4 | DRV/USD ⭐ | 0.31704 | 33.66 | +0.56% | 1.04x | MODERATE 57/100 | VERY_HIGH 73/100 | Watch |
| 5 | BLESS/USD | 0.017677 | 16.04 | -0.84% | 0.30x | WEAK 3/100 | EXTREME 88/100 | Do nothing |
| 6 | POND/USD | 0.001187 | -6.35 | -4.56% | 0.93x | WEAK 0/100 | EXTREME 99/100 | Do nothing |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | PEARL/USD ⭐ | 2.1591 | 48.13 | +1.36% | 2.57x | 7469 | STRONG 79/100 | HIGH 67/100 | Consider small entry |
| 2 | DRV/USD ⭐ | 0.31691 | 36.45 | +0.56% | 1.04x | 6247 | MODERATE 53/100 | VERY_HIGH 79/100 | Watch |

**Same-run overlap:** PEARL/USD, DRV/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
