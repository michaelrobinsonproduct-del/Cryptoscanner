# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-24T22:12:31.403354+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/45498217269
**Source SHA:** 858c8bc8ec5d7641ddb39cacd8aca91719f855b1
**Previous ledger commit:** 91a25dc06e415d5cb837b9907031b4fa1401b2f6 (atomic ledger/results publication)
**Ledger generation:** 1632 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 5s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 628; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 610; valid market observations: 609; OHLC screened: 13.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | XMR/USD | 505.24 | 75.633 | 75.243 | +3.95% | -0.01% | 1.04x | 14.9 | 2026-11-24T22:12:26.894444+00:00 | Not calibrated | WEAK 43/100 | VERY_HIGH 74/100 | Watch | WATCH |
| 2 | PEPE/USD | 3.491e-06 | 68.807 | 56.203 | +2.02% | -0.26% | 2.39x | 5.7 | 2026-11-24T22:12:26.894444+00:00 | Not calibrated | MODERATE 64/100 | HIGH 61/100 | Watch | WATCH |
| 3 | SKY/USD | 0.04111 | 63.360 | 43.946 | +1.78% | +0.96% | 2.46x | 4.9 | 2026-11-24T22:12:26.894444+00:00 | Not calibrated | STRONG 87/100 | HIGH 60/100 | Watch | WATCH |
| 4 | GBP/USD | 1.31058 | 61.719 | 58.594 | +0.56% | -0.02% | 1.32x | 0.7 | 2026-11-24T22:12:26.894444+00:00 | Not calibrated | MODERATE 51/100 | HIGH 61/100 | Watch | WATCH |
| 5 | NIGHT/USD | 0.04852 | 51.856 | 41.008 | +0.77% | +0.64% | 1.76x | 8.2 | 2026-11-24T22:12:26.894444+00:00 | Not calibrated | STRONG 71/100 | HIGH 55/100 | Watch | WATCH |
| 6 | LUNA/USD | 4.5e-05 | 41.231 | 51.854 | +3.52% | -1.40% | 0.64x | 8.9 | 2026-11-24T22:12:26.894444+00:00 | Not calibrated | WEAK 26/100 | EXTREME 92/100 | Do nothing | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | XMR/USD | 75.243 | 505.24 | -0.01% | 1.04x |
| 2 | GBP/USD | 58.594 | 1.31058 | -0.02% | 1.32x |
| 3 | PEPE/USD | 56.203 | 3.491e-06 | -0.26% | 2.39x |
| 4 | LUNA/USD | 51.854 | 4.5e-05 | -1.40% | 0.64x |
| 5 | SKY/USD | 43.946 | 0.04111 | +0.96% | 2.46x |
| 6 | NIGHT/USD | 41.008 | 0.04852 | +0.64% | 1.76x |

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

- Persisted scans: 1632; predictions: 13980; observations: 988979.
- Matured sampled outcomes across 1/6/24/48h: 28782; gap abstentions: 22370. Per-horizon counts require independent audit; do not infer held-out lift.
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

**Writer:** 45498217269 · **Generation:** 1632 · **Legacy run:** 45498217269
**Main quote time:** 2026-11-24T22:12:31.403354+00:00 · **Legacy report time:** 2026-11-24T22:13:21.452946+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | XMR/USD | 505.24 | 75.63 | -0.01% | 1.04x | WEAK 43/100 | VERY_HIGH 74/100 | Watch |
| 2 | PEPE/USD | 3.491e-06 | 68.81 | -0.26% | 2.39x | MODERATE 64/100 | HIGH 61/100 | Watch |
| 3 | SKY/USD ⭐ | 0.04111 | 63.36 | +0.96% | 2.46x | STRONG 97/100 | HIGH 60/100 | Consider small entry |
| 4 | GBP/USD | 1.31058 | 61.72 | -0.02% | 1.32x | MODERATE 51/100 | HIGH 61/100 | Watch |
| 5 | NIGHT/USD ⭐ | 0.04852 | 51.86 | +0.64% | 1.76x | STRONG 81/100 | HIGH 55/100 | Consider small entry |
| 6 | LUNA/USD | 4.5e-05 | 41.23 | -1.40% | 0.64x | WEAK 26/100 | EXTREME 92/100 | Do nothing |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | SKY/USD ⭐ | 0.04111 | 54.46 | +0.96% | 2.46x | 4472 | STRONG 87/100 | HIGH 66/100 | Consider small entry |
| 2 | NIGHT/USD ⭐ | 0.04858 | 50.29 | +0.64% | 1.76x | 9218 | STRONG 80/100 | HIGH 55/100 | Consider small entry |

**Same-run overlap:** SKY/USD, NIGHT/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
