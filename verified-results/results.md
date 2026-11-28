# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-28T00:22:32.553800+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/46087269319
**Source SHA:** 858c8bc8ec5d7641ddb39cacd8aca91719f855b1
**Previous ledger commit:** 71fdc2bd7847a5af6ee6e2c2dae7531460f05b06 (atomic ledger/results publication)
**Ledger generation:** 2080 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 4s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 628; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 610; valid market observations: 606; OHLC screened: 13.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | SKY/USD | 0.05299 | 69.826 | 47.741 | +2.10% | +1.42% | 4.17x | 13.2 | 2026-11-28T00:22:28.939644+00:00 | Not calibrated | STRONG 85/100 | HIGH 61/100 | Watch | WATCH |
| 2 | VVV/USD | 25.931 | 66.134 | 49.179 | +0.71% | +0.42% | 2.49x | 7.3 | 2026-11-28T00:22:28.939644+00:00 | Not calibrated | STRONG 88/100 | HIGH 55/100 | Watch | WATCH |
| 3 | LTC/USD | 45.32 | 58.184 | 56.531 | +0.38% | +0.95% | 0.69x | 2.2 | 2026-11-28T00:22:28.939644+00:00 | Not calibrated | MODERATE 59/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 4 | SPX/USD | 0.2734 | 21.402 | 25.476 | +0.37% | +0.37% | 0.41x | 18.3 | 2026-11-28T00:22:28.939644+00:00 | Not calibrated | WEAK 36/100 | VERY_HIGH 81/100 | Watch | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | LTC/USD | 56.531 | 45.32 | +0.95% | 0.69x |
| 2 | VVV/USD | 49.179 | 25.931 | +0.42% | 2.49x |
| 3 | SKY/USD | 47.741 | 0.05299 | +1.42% | 4.17x |
| 4 | SPX/USD | 25.476 | 0.2734 | +0.37% | 0.41x |

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

- Persisted scans: 2080; predictions: 18638; observations: 1259527.
- Matured sampled outcomes across 1/6/24/48h: 42714; gap abstentions: 25968. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 154 (sampled only; not a success-rate estimate).
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

**Writer:** 46087269319 · **Generation:** 2080 · **Legacy run:** 46087269319
**Main quote time:** 2026-11-28T00:22:32.553800+00:00 · **Legacy report time:** 2026-11-28T00:23:29.438080+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | SKY/USD ⭐ | 0.05299 | 69.83 | +1.42% | 4.17x | STRONG 95/100 | HIGH 61/100 | Consider small entry |
| 2 | VVV/USD ⭐ | 25.931 | 66.13 | +0.42% | 2.49x | STRONG 98/100 | HIGH 55/100 | Consider small entry |
| 3 | LTC/USD | 45.32 | 58.18 | +0.95% | 0.69x | MODERATE 59/100 | VERY_HIGH 70/100 | Watch |
| 4 | SPX/USD | 0.2734 | 21.40 | +0.37% | 0.41x | WEAK 36/100 | VERY_HIGH 81/100 | Watch |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | SKY/USD ⭐ | 0.05295 | 64.32 | +1.42% | 4.17x | 9985 | STRONG 97/100 | HIGH 55/100 | Consider small entry |
| 2 | XDG/USD | 0.0577433 | 60.01 | +0.11% | 2.67x | 13392 | STRONG 75/100 | HIGH 55/100 | Watch |
| 3 | VVV/USD ⭐ | 25.981 | 52.67 | +0.42% | 2.49x | 9068 | STRONG 91/100 | HIGH 55/100 | Consider small entry |
| 4 | XLM/USD | 0.126947 | 47.76 | +0.18% | 1.28x | 8673 | MODERATE 49/100 | HIGH 55/100 | Watch |
| 5 | BNB/USD | 554.96 | 40.01 | +0.05% | 1.08x | 4219 | MODERATE 45/100 | HIGH 62/100 | Watch |

**Same-run overlap:** SKY/USD, VVV/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
