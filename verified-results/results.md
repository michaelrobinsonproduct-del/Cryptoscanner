# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-25T00:12:11.006703+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/45515861967
**Source SHA:** 858c8bc8ec5d7641ddb39cacd8aca91719f855b1
**Previous ledger commit:** 81b1f37356869b6c01668342871636ebef0732ff (atomic ledger/results publication)
**Ledger generation:** 1644 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 3s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 628; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 610; valid market observations: 609; OHLC screened: 9.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | VVV/USD | 24.645 | 60.006 | 54.604 | +0.44% | +0.33% | 1.38x | 6.9 | 2026-11-25T00:12:08.058749+00:00 | Not calibrated | STRONG 75/100 | HIGH 55/100 | Watch | WATCH |
| 2 | POND/USD | 0.001223 | 56.512 | 43.373 | +4.00% | +2.80% | 0.92x | 32.8 | 2026-11-25T00:12:08.058749+00:00 | Not calibrated | MODERATE 48/100 | VERY_HIGH 79/100 | Watch | WATCH |
| 3 | SKY/USD | 0.04123 | 51.351 | 33.231 | +0.61% | +0.98% | 2.32x | 9.7 | 2026-11-25T00:12:08.058749+00:00 | Not calibrated | STRONG 81/100 | HIGH 60/100 | Watch | WATCH |
| 4 | DRV/USD | 0.31855 | 41.254 | 39.336 | +1.36% | +1.62% | 0.38x | 8.8 | 2026-11-25T00:12:08.058749+00:00 | Not calibrated | MODERATE 51/100 | VERY_HIGH 75/100 | Watch | WATCH |
| 5 | PEARL/USD | 2.1736 | 40.040 | 45.492 | +1.57% | +0.18% | 0.36x | 7.8 | 2026-11-25T00:12:08.058749+00:00 | Not calibrated | WEAK 40/100 | VERY_HIGH 70/100 | Watch | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | VVV/USD | 54.604 | 24.645 | +0.33% | 1.38x |
| 2 | PEARL/USD | 45.492 | 2.1736 | +0.18% | 0.36x |
| 3 | POND/USD | 43.373 | 0.001223 | +2.80% | 0.92x |
| 4 | DRV/USD | 39.336 | 0.31855 | +1.62% | 0.38x |
| 5 | SKY/USD | 33.231 | 0.04123 | +0.98% | 2.32x |

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

- Persisted scans: 1644; predictions: 14066; observations: 996287.
- Matured sampled outcomes across 1/6/24/48h: 29206; gap abstentions: 22370. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 143 (sampled only; not a success-rate estimate).
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

**Writer:** 45515861967 · **Generation:** 1644 · **Legacy run:** 45515861967
**Main quote time:** 2026-11-25T00:12:11.006703+00:00 · **Legacy report time:** 2026-11-25T00:12:57.890943+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | VVV/USD ⭐ | 24.645 | 60.01 | +0.33% | 1.38x | STRONG 85/100 | HIGH 55/100 | Watch |
| 2 | POND/USD | 0.001223 | 56.51 | +2.80% | 0.92x | MODERATE 48/100 | VERY_HIGH 79/100 | Watch |
| 3 | SKY/USD ⭐ | 0.04123 | 51.35 | +0.98% | 2.32x | STRONG 91/100 | HIGH 60/100 | Consider small entry |
| 4 | DRV/USD | 0.31855 | 41.25 | +1.62% | 0.38x | MODERATE 51/100 | VERY_HIGH 75/100 | Watch |
| 5 | PEARL/USD | 2.1736 | 40.04 | +0.18% | 0.36x | WEAK 40/100 | VERY_HIGH 70/100 | Watch |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | VVV/USD ⭐ | 24.668 | 47.87 | +0.33% | 1.38x | 16751 | STRONG 79/100 | HIGH 55/100 | Watch |
| 2 | SKY/USD ⭐ | 0.04127 | 41.01 | +0.98% | 2.32x | 4233 | STRONG 86/100 | HIGH 60/100 | Consider small entry |
| 3 | AKE/USD | 0.00210622 | 28.76 | +0.18% | 1.10x | 7273 | WEAK 24/100 | VERY_HIGH 79/100 | Do nothing |

**Same-run overlap:** VVV/USD, SKY/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
