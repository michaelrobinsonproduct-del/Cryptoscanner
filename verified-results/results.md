# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-24T21:12:05.124747+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/45488214322
**Source SHA:** 858c8bc8ec5d7641ddb39cacd8aca91719f855b1
**Previous ledger commit:** 4231824a0ba2aa9e06c070104ab345f83f25576c (atomic ledger/results publication)
**Ledger generation:** 1626 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 4s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 628; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 610; valid market observations: 609; OHLC screened: 13.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | XMR/USD | 499.04 | 67.404 | 70.544 | +2.68% | -0.00% | 0.69x | 6.4 | 2026-11-24T21:12:01.516271+00:00 | Not calibrated | WEAK 39/100 | VERY_HIGH 76/100 | Watch | WATCH |
| 2 | GBP/USD | 1.31076 | 60.966 | 58.996 | +0.58% | +0.00% | 1.20x | 0.1 | 2026-11-24T21:12:01.516271+00:00 | Not calibrated | MODERATE 55/100 | HIGH 62/100 | Watch | WATCH |
| 3 | PEPE/USD | 3.463e-06 | 42.786 | 51.251 | +1.20% | -0.12% | 0.21x | 2.9 | 2026-11-24T21:12:01.516271+00:00 | Not calibrated | WEAK 26/100 | VERY_HIGH 76/100 | Do nothing | WATCH |
| 4 | AUD/USD | 0.66443 | 39.622 | 44.538 | +0.28% | +0.00% | 0.51x | 1.8 | 2026-11-24T21:12:01.516271+00:00 | Not calibrated | WEAK 40/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 5 | NIGHT/USD | 0.04833 | 35.956 | 38.969 | +0.37% | -0.86% | 1.13x | 8.3 | 2026-11-24T21:12:01.516271+00:00 | Not calibrated | WEAK 28/100 | HIGH 68/100 | Do nothing | WATCH |
| 6 | SKY/USD | 0.0405 | 34.143 | 31.839 | +0.27% | +0.05% | 1.21x | 7.4 | 2026-11-24T21:12:01.516271+00:00 | Not calibrated | WEAK 42/100 | HIGH 67/100 | Watch | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | XMR/USD | 70.544 | 499.04 | -0.00% | 0.69x |
| 2 | GBP/USD | 58.996 | 1.31076 | +0.00% | 1.20x |
| 3 | PEPE/USD | 51.251 | 3.463e-06 | -0.12% | 0.21x |
| 4 | AUD/USD | 44.538 | 0.66443 | +0.00% | 0.51x |
| 5 | NIGHT/USD | 38.969 | 0.04833 | -0.86% | 1.13x |
| 6 | SKY/USD | 31.839 | 0.0405 | +0.05% | 1.21x |

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

- Persisted scans: 1626; predictions: 13944; observations: 985326.
- Matured sampled outcomes across 1/6/24/48h: 28553; gap abstentions: 22370. Per-horizon counts require independent audit; do not infer held-out lift.
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

**Writer:** 45488214322 · **Generation:** 1626 · **Legacy run:** 45488214322
**Main quote time:** 2026-11-24T21:12:05.124747+00:00 · **Legacy report time:** 2026-11-24T21:13:19.313652+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | XMR/USD | 499.04 | 67.40 | -0.00% | 0.69x | WEAK 39/100 | VERY_HIGH 76/100 | Watch |
| 2 | GBP/USD | 1.31076 | 60.97 | +0.00% | 1.20x | MODERATE 55/100 | HIGH 62/100 | Watch |
| 3 | PEPE/USD | 3.463e-06 | 42.79 | -0.12% | 0.21x | WEAK 26/100 | VERY_HIGH 76/100 | Do nothing |
| 4 | AUD/USD | 0.66443 | 39.62 | +0.00% | 0.51x | WEAK 40/100 | VERY_HIGH 70/100 | Watch |
| 5 | NIGHT/USD | 0.04833 | 35.96 | -0.86% | 1.13x | WEAK 28/100 | HIGH 68/100 | Do nothing |
| 6 | SKY/USD | 0.0405 | 34.14 | +0.05% | 1.21x | WEAK 42/100 | HIGH 67/100 | Watch |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| — | No confirmed WATCH signals | — | — | — | — | — | — | — | — |

**Same-run overlap:** None
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
