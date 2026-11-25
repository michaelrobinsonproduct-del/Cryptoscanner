# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-25T09:27:20.590573+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/45585117034
**Source SHA:** 858c8bc8ec5d7641ddb39cacd8aca91719f855b1
**Previous ledger commit:** ca267b913b0a1fa1890c4bcc070081cffa98a644 (atomic ledger/results publication)
**Ledger generation:** 1699 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 5s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 628; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 610; valid market observations: 608; OHLC screened: 18.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | MON/USD | 0.0106 | 97.171 | 86.134 | +11.93% | -0.56% | 2.39x | 18.9 | 2026-11-25T09:27:15.448453+00:00 | Not calibrated | STRONG 74/100 | HIGH 67/100 | Watch | WATCH |
| 2 | 2Z/USD | 0.01676 | 63.581 | 43.770 | +2.26% | +0.96% | 4.38x | 6.0 | 2026-11-25T09:27:15.448453+00:00 | Not calibrated | STRONG 87/100 | HIGH 67/100 | Watch | WATCH |
| 3 | BABY/USD | 0.00872 | 59.798 | 64.819 | +5.57% | -1.02% | 1.01x | 11.5 | 2026-11-25T09:27:15.448453+00:00 | Not calibrated | WEAK 35/100 | EXTREME 90/100 | Do nothing | WATCH |
| 4 | SYRUP/USD | 0.07091 | 33.479 | 34.142 | +1.78% | -0.42% | 1.14x | 19.8 | 2026-11-25T09:27:15.448453+00:00 | Not calibrated | WEAK 22/100 | EXTREME 86/100 | Do nothing | WATCH |
| 5 | ATOM/USD | 1.2536 | 29.726 | 34.815 | +0.66% | -0.43% | 0.71x | 4.0 | 2026-11-25T09:27:15.448453+00:00 | Not calibrated | WEAK 20/100 | VERY_HIGH 81/100 | Do nothing | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | MON/USD | 86.134 | 0.0106 | -0.56% | 2.39x |
| 2 | BABY/USD | 64.819 | 0.00872 | -1.02% | 1.01x |
| 3 | 2Z/USD | 43.770 | 0.01676 | +0.96% | 4.38x |
| 4 | ATOM/USD | 34.815 | 1.2536 | -0.43% | 0.71x |
| 5 | SYRUP/USD | 34.142 | 0.07091 | -0.42% | 1.14x |

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

- Persisted scans: 1699; predictions: 14419; observations: 1029775.
- Matured sampled outcomes across 1/6/24/48h: 31050; gap abstentions: 22370. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 146 (sampled only; not a success-rate estimate).
- False positives / missed movers: NOT VERIFIED without eligible continuous outcome coverage.
- Baseline vs challenger: recorded as-of; unbiased held-out lift NOT MEASURED.
- Online Kraken /USD stablecoin-base pairs excluded: 18 (counted from this scan's online AssetPairs metadata, not inferred from price).
- Stablecoin base exclusions: BRL1, BUSD, DAI, EUR, EURC, EUROP, EURQ, EURR, EURT, FDUSD, FRAX, GUSD, PYUSD, QCAD, RLUSD, TGBP, TUSD, USD, USD1, USDC, USDD, USDE, USDG, USDQ, USDR, USDS, USDT, ZUSD.
- DEX: NOT USED; no DEX freshness gate.
- OHLC screening abstentions: 13; details in immutable scan JSON artifact.
- Storage: ledger and results published in one non-force Git commit and read back. Independent artifact recovery is NOT VERIFIED by this scan alone.
- Errors: none in successful committed scan; a failed workflow must not publish a SUCCESS report.

# Cryptoscanner — challenger and independent legacy-inspired WATCH

Paper only · risk is high or higher · 30%+ in 48h probability NOT CALIBRATED
Signal confidence 0–100 means setup strength only, NOT a win probability. Actions are research guidance; no trade authorization.

**Writer:** 45585117034 · **Generation:** 1699 · **Legacy run:** 45585117034
**Main quote time:** 2026-11-25T09:27:20.590573+00:00 · **Legacy report time:** 2026-11-25T09:28:37.121739+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | MON/USD | 0.0106 | 97.17 | -0.56% | 2.39x | STRONG 74/100 | HIGH 67/100 | Watch |
| 2 | 2Z/USD ⭐ | 0.01676 | 63.58 | +0.96% | 4.38x | STRONG 97/100 | HIGH 67/100 | Consider small entry |
| 3 | BABY/USD | 0.00872 | 59.80 | -1.02% | 1.01x | WEAK 35/100 | EXTREME 90/100 | Do nothing |
| 4 | SYRUP/USD | 0.07091 | 33.48 | -0.42% | 1.14x | WEAK 22/100 | EXTREME 86/100 | Do nothing |
| 5 | ATOM/USD | 1.2536 | 29.73 | -0.43% | 0.71x | WEAK 20/100 | VERY_HIGH 81/100 | Do nothing |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | 2Z/USD ⭐ | 0.01676 | 52.06 | +0.96% | 4.38x | 1622 | STRONG 86/100 | VERY_HIGH 73/100 | Watch |

**Same-run overlap:** 2Z/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
