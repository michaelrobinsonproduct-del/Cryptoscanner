# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-24T13:41:45.480875+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/45405708993
**Source SHA:** 858c8bc8ec5d7641ddb39cacd8aca91719f855b1
**Previous ledger commit:** 397d941c3112fdb2c596afb826df9aa63eeb8e17 (atomic ledger/results publication)
**Ledger generation:** 1581 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 3s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 628; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 610; valid market observations: 609; OHLC screened: 13.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | MON/USD | 0.0123 | 81.463 | 79.042 | +6.77% | +1.56% | 0.46x | 16.3 | 2026-11-24T13:41:42.179403+00:00 | Not calibrated | MODERATE 66/100 | VERY_HIGH 76/100 | Watch | WATCH |
| 2 | VVV/USD | 25.513 | 76.726 | 79.997 | +4.36% | +0.32% | 0.51x | 11.0 | 2026-11-24T13:41:42.179403+00:00 | Not calibrated | MODERATE 63/100 | VERY_HIGH 76/100 | Watch | WATCH |
| 3 | ICNT/USD | 0.3344 | 69.892 | 68.954 | +8.19% | +1.46% | 0.37x | 18.0 | 2026-11-24T13:41:42.179403+00:00 | Not calibrated | MODERATE 60/100 | VERY_HIGH 81/100 | Watch | WATCH |
| 4 | XMR/USD | 498.51 | 64.093 | 63.649 | +2.57% | +0.30% | 0.90x | 18.7 | 2026-11-24T13:41:42.179403+00:00 | Not calibrated | MODERATE 57/100 | HIGH 68/100 | Watch | WATCH |
| 5 | LUNA/USD | 4.546e-05 | 60.461 | 55.049 | +4.58% | +0.31% | 1.39x | 17.6 | 2026-11-24T13:41:42.179403+00:00 | Not calibrated | STRONG 70/100 | HIGH 66/100 | Watch | WATCH |
| 6 | GBP/USD | 1.30919 | 50.123 | 57.999 | +0.46% | -0.01% | 0.22x | 0.4 | 2026-11-24T13:41:42.179403+00:00 | Not calibrated | WEAK 30/100 | VERY_HIGH 76/100 | Do nothing | WATCH |
| 7 | NIGHT/USD | 0.0485 | 47.037 | 50.076 | +0.73% | -0.25% | 0.82x | 6.2 | 2026-11-24T13:41:42.179403+00:00 | Not calibrated | WEAK 29/100 | HIGH 68/100 | Do nothing | WATCH |
| 8 | 2Z/USD | 0.01596 | 41.818 | 41.485 | +1.98% | +0.38% | 0.84x | 6.3 | 2026-11-24T13:41:42.179403+00:00 | Not calibrated | MODERATE 51/100 | VERY_HIGH 74/100 | Watch | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | VVV/USD | 79.997 | 25.513 | +0.32% | 0.51x |
| 2 | MON/USD | 79.042 | 0.0123 | +1.56% | 0.46x |
| 3 | ICNT/USD | 68.954 | 0.3344 | +1.46% | 0.37x |
| 4 | XMR/USD | 63.649 | 498.51 | +0.30% | 0.90x |
| 5 | GBP/USD | 57.999 | 1.30919 | -0.01% | 0.22x |
| 6 | LUNA/USD | 55.049 | 4.546e-05 | +0.31% | 1.39x |
| 7 | NIGHT/USD | 50.076 | 0.0485 | -0.25% | 0.82x |
| 8 | 2Z/USD | 41.485 | 0.01596 | +0.38% | 0.84x |

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

- Persisted scans: 1581; predictions: 13633; observations: 957926.
- Matured sampled outcomes across 1/6/24/48h: 26673; gap abstentions: 22370. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 143 (sampled only; not a success-rate estimate).
- False positives / missed movers: NOT VERIFIED without eligible continuous outcome coverage.
- Baseline vs challenger: recorded as-of; unbiased held-out lift NOT MEASURED.
- Online Kraken /USD stablecoin-base pairs excluded: 18 (counted from this scan's online AssetPairs metadata, not inferred from price).
- Stablecoin base exclusions: BRL1, BUSD, DAI, EUR, EURC, EUROP, EURQ, EURR, EURT, FDUSD, FRAX, GUSD, PYUSD, QCAD, RLUSD, TGBP, TUSD, USD, USD1, USDC, USDD, USDE, USDG, USDQ, USDR, USDS, USDT, ZUSD.
- DEX: NOT USED; no DEX freshness gate.
- OHLC screening abstentions: 5; details in immutable scan JSON artifact.
- Storage: ledger and results published in one non-force Git commit and read back. Independent artifact recovery is NOT VERIFIED by this scan alone.
- Errors: none in successful committed scan; a failed workflow must not publish a SUCCESS report.

# Cryptoscanner — challenger and independent legacy-inspired WATCH

Paper only · risk is high or higher · 30%+ in 48h probability NOT CALIBRATED
Signal confidence 0–100 means setup strength only, NOT a win probability. Actions are research guidance; no trade authorization.

**Writer:** 45405708993 · **Generation:** 1581 · **Legacy run:** 45405708993
**Main quote time:** 2026-11-24T13:41:45.480875+00:00 · **Legacy report time:** 2026-11-24T13:42:36.462924+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | MON/USD | 0.0123 | 81.46 | +1.56% | 0.46x | MODERATE 66/100 | VERY_HIGH 76/100 | Watch |
| 2 | VVV/USD | 25.513 | 76.73 | +0.32% | 0.51x | MODERATE 63/100 | VERY_HIGH 76/100 | Watch |
| 3 | ICNT/USD | 0.3344 | 69.89 | +1.46% | 0.37x | MODERATE 60/100 | VERY_HIGH 81/100 | Watch |
| 4 | XMR/USD | 498.51 | 64.09 | +0.30% | 0.90x | MODERATE 57/100 | HIGH 68/100 | Watch |
| 5 | LUNA/USD ⭐ | 4.546e-05 | 60.46 | +0.31% | 1.39x | STRONG 80/100 | HIGH 66/100 | Watch |
| 6 | GBP/USD | 1.30919 | 50.12 | -0.01% | 0.22x | WEAK 30/100 | VERY_HIGH 76/100 | Do nothing |
| 7 | NIGHT/USD | 0.0485 | 47.04 | -0.25% | 0.82x | WEAK 29/100 | HIGH 68/100 | Do nothing |
| 8 | 2Z/USD | 0.01596 | 41.82 | +0.38% | 0.84x | MODERATE 51/100 | VERY_HIGH 74/100 | Watch |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | LUNA/USD ⭐ | 4.562e-05 | 66.02 | +0.31% | 1.39x | 1735 | STRONG 78/100 | VERY_HIGH 72/100 | Watch |

**Same-run overlap:** LUNA/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
