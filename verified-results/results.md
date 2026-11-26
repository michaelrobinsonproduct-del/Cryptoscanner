# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-26T06:36:01.793806+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/45769138542
**Source SHA:** 858c8bc8ec5d7641ddb39cacd8aca91719f855b1
**Previous ledger commit:** 593720fae1dd2a46b52463d30d4c4c3028da282a (atomic ledger/results publication)
**Ledger generation:** 1825 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 7s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 628; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 610; valid market observations: 609; OHLC screened: 24.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | LINK/USD | 9.17742 | 78.828 | 62.892 | +1.47% | +0.19% | 4.08x | 1.6 | 2026-11-26T06:35:54.370491+00:00 | Not calibrated | STRONG 84/100 | HIGH 55/100 | Watch | WATCH |
| 2 | SYRUP/USD | 0.07023 | 78.754 | 63.304 | +5.98% | +1.31% | 1.89x | 21.3 | 2026-11-26T06:35:54.370491+00:00 | Not calibrated | STRONG 74/100 | VERY_HIGH 72/100 | Watch | WATCH |
| 3 | SKY/USD | 0.04387 | 76.038 | 63.459 | +4.75% | +0.11% | 2.20x | 6.8 | 2026-11-26T06:35:54.370491+00:00 | Not calibrated | STRONG 83/100 | HIGH 60/100 | Watch | WATCH |
| 4 | PUMP/USD | 0.00264 | 74.078 | 60.221 | +2.44% | +0.69% | 2.04x | 3.8 | 2026-11-26T06:35:54.370491+00:00 | Not calibrated | STRONG 92/100 | HIGH 55/100 | Consider small entry | WATCH |
| 5 | XBT/USD | 60547.4 | 73.693 | 57.065 | +0.30% | +0.33% | 2.67x | 0.0 | 2026-11-26T06:35:54.370491+00:00 | Not calibrated | STRONG 92/100 | HIGH 55/100 | Consider small entry | WATCH |
| 6 | ADA/USD | 0.148293 | 66.297 | 65.632 | +1.73% | +0.22% | 0.96x | 3.0 | 2026-11-26T06:35:54.370491+00:00 | Not calibrated | MODERATE 63/100 | HIGH 62/100 | Watch | WATCH |
| 7 | LTC/USD | 43.62 | 64.401 | 68.768 | +2.13% | +0.41% | 0.36x | 2.3 | 2026-11-26T06:35:54.370491+00:00 | Not calibrated | MODERATE 62/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 8 | XRP/USD | 0.95285 | 63.771 | 67.123 | +1.74% | +0.11% | 0.61x | 0.1 | 2026-11-26T06:35:54.370491+00:00 | Not calibrated | MODERATE 52/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 9 | NEAR/USD | 3.0705 | 61.522 | 59.565 | +0.68% | +0.82% | 0.79x | 0.3 | 2026-11-26T06:35:54.370491+00:00 | Not calibrated | MODERATE 61/100 | HIGH 62/100 | Watch | WATCH |
| 10 | SOL/USD | 70.85 | 60.042 | 58.869 | +0.65% | +0.26% | 0.99x | 1.4 | 2026-11-26T06:35:54.370491+00:00 | Not calibrated | MODERATE 60/100 | HIGH 62/100 | Watch | WATCH |
| 11 | XMR/USD | 526.58 | 59.704 | 62.619 | +1.86% | +1.07% | 0.17x | 10.8 | 2026-11-26T06:35:54.370491+00:00 | Not calibrated | MODERATE 55/100 | VERY_HIGH 76/100 | Watch | WATCH |
| 12 | TAO/USD | 183.3295 | 58.871 | 60.525 | +0.96% | +0.20% | 0.74x | 2.3 | 2026-11-26T06:35:54.370491+00:00 | Not calibrated | MODERATE 49/100 | VERY_HIGH 70/100 | Watch | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | LTC/USD | 68.768 | 43.62 | +0.41% | 0.36x |
| 2 | XRP/USD | 67.123 | 0.95285 | +0.11% | 0.61x |
| 3 | ADA/USD | 65.632 | 0.148293 | +0.22% | 0.96x |
| 4 | SKY/USD | 63.459 | 0.04387 | +0.11% | 2.20x |
| 5 | SYRUP/USD | 63.304 | 0.07023 | +1.31% | 1.89x |
| 6 | LINK/USD | 62.892 | 9.17742 | +0.19% | 4.08x |
| 7 | XMR/USD | 62.619 | 526.58 | +1.07% | 0.17x |
| 8 | TAO/USD | 60.525 | 183.3295 | +0.20% | 0.74x |
| 9 | PUMP/USD | 60.221 | 0.00264 | +0.69% | 2.04x |
| 10 | NEAR/USD | 59.565 | 3.0705 | +0.82% | 0.79x |
| 11 | SOL/USD | 58.869 | 70.85 | +0.26% | 0.99x |
| 12 | XBT/USD | 57.065 | 60547.4 | +0.33% | 2.67x |

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

- Persisted scans: 1825; predictions: 15635; observations: 1106469.
- Matured sampled outcomes across 1/6/24/48h: 33911; gap abstentions: 24082. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 146 (sampled only; not a success-rate estimate).
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

**Writer:** 45769138542 · **Generation:** 1825 · **Legacy run:** 45769138542
**Main quote time:** 2026-11-26T06:36:01.793806+00:00 · **Legacy report time:** 2026-11-26T06:37:05.328291+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | LINK/USD ⭐ | 9.17742 | 78.83 | +0.19% | 4.08x | STRONG 94/100 | HIGH 55/100 | Watch |
| 2 | SYRUP/USD ⭐ | 0.07023 | 78.75 | +1.31% | 1.89x | STRONG 84/100 | VERY_HIGH 72/100 | Watch |
| 3 | SKY/USD ⭐ | 0.04387 | 76.04 | +0.11% | 2.20x | STRONG 93/100 | HIGH 60/100 | Watch |
| 4 | PUMP/USD ⭐ | 0.00264 | 74.08 | +0.69% | 2.04x | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 5 | XBT/USD | 60547.4 | 73.69 | +0.33% | 2.67x | STRONG 92/100 | HIGH 55/100 | Consider small entry |
| 6 | ADA/USD | 0.148293 | 66.30 | +0.22% | 0.96x | MODERATE 63/100 | HIGH 62/100 | Watch |
| 7 | LTC/USD | 43.62 | 64.40 | +0.41% | 0.36x | MODERATE 62/100 | VERY_HIGH 70/100 | Watch |
| 8 | XRP/USD | 0.95285 | 63.77 | +0.11% | 0.61x | MODERATE 52/100 | VERY_HIGH 70/100 | Watch |
| 9 | NEAR/USD | 3.0705 | 61.52 | +0.82% | 0.79x | MODERATE 61/100 | HIGH 62/100 | Watch |
| 10 | SOL/USD | 70.85 | 60.04 | +0.26% | 0.99x | MODERATE 60/100 | HIGH 62/100 | Watch |
| 11 | XMR/USD | 526.58 | 59.70 | +1.07% | 0.17x | MODERATE 55/100 | VERY_HIGH 76/100 | Watch |
| 12 | TAO/USD | 183.3295 | 58.87 | +0.20% | 0.74x | MODERATE 49/100 | VERY_HIGH 70/100 | Watch |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | SYRUP/USD ⭐ | 0.07023 | 78.78 | +1.31% | 1.89x | 3679 | STRONG 89/100 | HIGH 66/100 | Consider small entry |
| 2 | SKY/USD ⭐ | 0.04387 | 77.32 | +0.11% | 2.20x | 4084 | STRONG 94/100 | HIGH 60/100 | Watch |
| 3 | PUMP/USD ⭐ | 0.002643 | 75.40 | +0.69% | 2.04x | 6297 | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 4 | LINK/USD ⭐ | 9.18 | 69.76 | +0.19% | 4.08x | 9236 | STRONG 90/100 | HIGH 55/100 | Watch |

**Same-run overlap:** LINK/USD, SYRUP/USD, SKY/USD, PUMP/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
