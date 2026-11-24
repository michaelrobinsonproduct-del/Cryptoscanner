# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-24T21:51:50.975671+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/45494956157
**Source SHA:** 858c8bc8ec5d7641ddb39cacd8aca91719f855b1
**Previous ledger commit:** 3a165d6163cfa2480ac7bf457e5b5b97b4cbabe9 (atomic ledger/results publication)
**Ledger generation:** 1630 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 4s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 628; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 610; valid market observations: 609; OHLC screened: 11.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | XMR/USD | 503.65 | 84.410 | 79.995 | +3.63% | +0.49% | 1.20x | 0.8 | 2026-11-24T21:51:47.319963+00:00 | Not calibrated | STRONG 77/100 | HIGH 62/100 | Watch | WATCH |
| 2 | PEPE/USD | 3.488e-06 | 66.606 | 56.728 | +1.93% | +0.49% | 1.74x | 2.9 | 2026-11-24T21:51:47.319963+00:00 | Not calibrated | STRONG 78/100 | HIGH 55/100 | Watch | WATCH |
| 3 | GBP/USD | 1.31088 | 58.826 | 59.022 | +0.59% | -0.01% | 0.99x | 0.2 | 2026-11-24T21:51:47.319963+00:00 | Not calibrated | WEAK 34/100 | HIGH 68/100 | Do nothing | WATCH |
| 4 | SKY/USD | 0.04083 | 57.571 | 36.504 | +1.09% | +1.21% | 4.03x | 9.8 | 2026-11-24T21:51:47.319963+00:00 | Not calibrated | STRONG 84/100 | HIGH 60/100 | Watch | WATCH |
| 5 | NIGHT/USD | 0.04838 | 37.400 | 40.210 | +0.48% | -0.14% | 0.79x | 6.2 | 2026-11-24T21:51:47.319963+00:00 | Not calibrated | WEAK 24/100 | HIGH 68/100 | Do nothing | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | XMR/USD | 79.995 | 503.65 | +0.49% | 1.20x |
| 2 | GBP/USD | 59.022 | 1.31088 | -0.01% | 0.99x |
| 3 | PEPE/USD | 56.728 | 3.488e-06 | +0.49% | 1.74x |
| 4 | NIGHT/USD | 40.210 | 0.04838 | -0.14% | 0.79x |
| 5 | SKY/USD | 36.504 | 0.04083 | +1.21% | 4.03x |

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

- Persisted scans: 1630; predictions: 13967; observations: 987761.
- Matured sampled outcomes across 1/6/24/48h: 28702; gap abstentions: 22370. Per-horizon counts require independent audit; do not infer held-out lift.
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

**Writer:** 45494956157 · **Generation:** 1630 · **Legacy run:** 45494956157
**Main quote time:** 2026-11-24T21:51:50.975671+00:00 · **Legacy report time:** 2026-11-24T21:52:40.930281+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | XMR/USD ⭐ | 503.65 | 84.41 | +0.49% | 1.20x | STRONG 87/100 | HIGH 62/100 | Watch |
| 2 | PEPE/USD ⭐ | 3.488e-06 | 66.61 | +0.49% | 1.74x | STRONG 88/100 | HIGH 55/100 | Consider small entry |
| 3 | GBP/USD | 1.31088 | 58.83 | -0.01% | 0.99x | WEAK 34/100 | HIGH 68/100 | Do nothing |
| 4 | SKY/USD ⭐ | 0.04083 | 57.57 | +1.21% | 4.03x | STRONG 94/100 | HIGH 60/100 | Consider small entry |
| 5 | NIGHT/USD | 0.04838 | 37.40 | -0.14% | 0.79x | WEAK 24/100 | HIGH 68/100 | Do nothing |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | XMR/USD ⭐ | 503.75 | 96.05 | +0.49% | 1.20x | 7615 | STRONG 93/100 | HIGH 62/100 | Watch |
| 2 | PEPE/USD ⭐ | 3.481e-06 | 65.17 | +0.49% | 1.74x | 6656 | STRONG 88/100 | HIGH 55/100 | Consider small entry |
| 3 | SKY/USD ⭐ | 0.04081 | 58.49 | +1.21% | 4.03x | 4380 | STRONG 94/100 | HIGH 60/100 | Consider small entry |

**Same-run overlap:** XMR/USD, PEPE/USD, SKY/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
