# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-28T15:23:22.851990+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/46159263586
**Source SHA:** 858c8bc8ec5d7641ddb39cacd8aca91719f855b1
**Previous ledger commit:** 145f4c0a644dcad082f0fa062d1dd39b9bfadde0 (atomic ledger/results publication)
**Ledger generation:** 2171 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 3s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 628; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 610; valid market observations: 606; OHLC screened: 10.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | XMR/USD | 431.26 | 89.523 | 87.053 | +5.89% | -0.12% | 1.31x | 18.4 | 2026-11-28T15:23:19.534938+00:00 | Not calibrated | MODERATE 60/100 | HIGH 67/100 | Watch | WATCH |
| 2 | NIGHT/USD | 0.05285 | 76.942 | 86.004 | +5.20% | -0.79% | 0.49x | 9.5 | 2026-11-28T15:23:19.534938+00:00 | Not calibrated | WEAK 43/100 | VERY_HIGH 76/100 | Watch | WATCH |
| 3 | LUNA/USD | 4.826e-05 | 70.201 | 60.657 | +5.86% | +0.71% | 1.60x | 22.9 | 2026-11-28T15:23:19.534938+00:00 | Not calibrated | STRONG 70/100 | VERY_HIGH 79/100 | Watch | WATCH |
| 4 | VVV/USD | 26.681 | 57.455 | 63.860 | +3.62% | -0.35% | 0.54x | 7.1 | 2026-11-28T15:23:19.534938+00:00 | Not calibrated | WEAK 34/100 | VERY_HIGH 76/100 | Do nothing | WATCH |
| 5 | SENT/USD | 0.024139 | 39.835 | 41.966 | +1.79% | +0.61% | 0.48x | 4.1 | 2026-11-28T15:23:19.534938+00:00 | Not calibrated | MODERATE 50/100 | VERY_HIGH 82/100 | Watch | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | XMR/USD | 87.053 | 431.26 | -0.12% | 1.31x |
| 2 | NIGHT/USD | 86.004 | 0.05285 | -0.79% | 0.49x |
| 3 | VVV/USD | 63.860 | 26.681 | -0.35% | 0.54x |
| 4 | LUNA/USD | 60.657 | 4.826e-05 | +0.71% | 1.60x |
| 5 | SENT/USD | 41.966 | 0.024139 | +0.61% | 0.48x |

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

- Persisted scans: 2171; predictions: 19287; observations: 1314672.
- Matured sampled outcomes across 1/6/24/48h: 46476; gap abstentions: 25968. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 155 (sampled only; not a success-rate estimate).
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

**Writer:** 46159263586 · **Generation:** 2171 · **Legacy run:** 46159263586
**Main quote time:** 2026-11-28T15:23:22.851990+00:00 · **Legacy report time:** 2026-11-28T15:24:17.465451+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | XMR/USD | 431.26 | 89.52 | -0.12% | 1.31x | MODERATE 60/100 | HIGH 67/100 | Watch |
| 2 | NIGHT/USD | 0.05285 | 76.94 | -0.79% | 0.49x | WEAK 43/100 | VERY_HIGH 76/100 | Watch |
| 3 | LUNA/USD | 4.826e-05 | 70.20 | +0.71% | 1.60x | STRONG 70/100 | VERY_HIGH 79/100 | Watch |
| 4 | VVV/USD | 26.681 | 57.45 | -0.35% | 0.54x | WEAK 34/100 | VERY_HIGH 76/100 | Do nothing |
| 5 | SENT/USD | 0.024139 | 39.84 | +0.61% | 0.48x | MODERATE 50/100 | VERY_HIGH 82/100 | Watch |

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
