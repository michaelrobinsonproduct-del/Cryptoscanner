# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-24T15:24:15.996502+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/45424185393
**Source SHA:** 858c8bc8ec5d7641ddb39cacd8aca91719f855b1
**Previous ledger commit:** c80b22b16a9014a477a95fa122282116e188921c (atomic ledger/results publication)
**Ledger generation:** 1591 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 4s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 628; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 610; valid market observations: 608; OHLC screened: 12.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | GBP/USD | 1.31079 | 73.676 | 58.974 | +0.58% | -0.06% | 2.57x | 0.2 | 2026-11-24T15:24:11.900729+00:00 | Not calibrated | MODERATE 67/100 | HIGH 61/100 | Watch | WATCH |
| 2 | VVV/USD | 24.813 | 70.350 | 61.626 | +1.49% | -1.26% | 9.52x | 7.6 | 2026-11-24T15:24:11.900729+00:00 | Not calibrated | MODERATE 65/100 | HIGH 65/100 | Do nothing | WATCH |
| 3 | XMR/USD | 493.27 | 59.100 | 61.487 | +1.49% | -0.37% | 0.94x | 7.9 | 2026-11-24T15:24:11.900729+00:00 | Not calibrated | WEAK 35/100 | HIGH 68/100 | Watch | WATCH |
| 4 | AUD/USD | 0.66445 | 49.075 | 42.540 | +0.28% | -0.08% | 1.69x | 1.1 | 2026-11-24T15:24:11.900729+00:00 | Not calibrated | MODERATE 45/100 | HIGH 61/100 | Watch | WATCH |
| 5 | 2Z/USD | 0.0161 | 35.121 | 47.759 | +2.88% | -2.13% | 0.80x | 6.2 | 2026-11-24T15:24:11.900729+00:00 | Not calibrated | WEAK 23/100 | VERY_HIGH 84/100 | Do nothing | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | VVV/USD | 61.626 | 24.813 | -1.26% | 9.52x |
| 2 | XMR/USD | 61.487 | 493.27 | -0.37% | 0.94x |
| 3 | GBP/USD | 58.974 | 1.31079 | -0.06% | 2.57x |
| 4 | 2Z/USD | 47.759 | 0.0161 | -2.13% | 0.80x |
| 5 | AUD/USD | 42.540 | 0.66445 | -0.08% | 1.69x |

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

- Persisted scans: 1591; predictions: 13709; observations: 964011.
- Matured sampled outcomes across 1/6/24/48h: 27117; gap abstentions: 22370. Per-horizon counts require independent audit; do not infer held-out lift.
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

**Writer:** 45424185393 · **Generation:** 1591 · **Legacy run:** 45424185393
**Main quote time:** 2026-11-24T15:24:15.996502+00:00 · **Legacy report time:** 2026-11-24T15:25:28.604127+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | GBP/USD | 1.31079 | 73.68 | -0.06% | 2.57x | MODERATE 67/100 | HIGH 61/100 | Watch |
| 2 | VVV/USD | 24.813 | 70.35 | -1.26% | 9.52x | MODERATE 65/100 | HIGH 65/100 | Do nothing |
| 3 | XMR/USD | 493.27 | 59.10 | -0.37% | 0.94x | WEAK 35/100 | HIGH 68/100 | Watch |
| 4 | AUD/USD | 0.66445 | 49.08 | -0.08% | 1.69x | MODERATE 45/100 | HIGH 61/100 | Watch |
| 5 | 2Z/USD | 0.0161 | 35.12 | -2.13% | 0.80x | WEAK 23/100 | VERY_HIGH 84/100 | Do nothing |

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
