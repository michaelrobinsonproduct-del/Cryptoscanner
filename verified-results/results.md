# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-25T04:37:28.351248+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/45547719805
**Source SHA:** 858c8bc8ec5d7641ddb39cacd8aca91719f855b1
**Previous ledger commit:** d123b1bc96a3badb765a0127b1698bd7d8637691 (atomic ledger/results publication)
**Ledger generation:** 1670 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 7s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 628; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 610; valid market observations: 609; OHLC screened: 21.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | MON/USD | 0.00987 | 75.641 | 67.697 | +4.22% | +0.71% | 1.44x | 20.3 | 2026-11-25T04:37:21.354194+00:00 | Not calibrated | STRONG 73/100 | HIGH 67/100 | Watch | WATCH |
| 2 | DRV/USD | 0.33192 | 57.909 | 60.022 | +5.61% | -1.32% | 1.45x | 31.7 | 2026-11-25T04:37:21.354194+00:00 | Not calibrated | WEAK 39/100 | VERY_HIGH 82/100 | Do nothing | WATCH |
| 3 | XMR/USD | 512.26 | 51.169 | 55.018 | +0.52% | -0.18% | 0.71x | 3.7 | 2026-11-25T04:37:21.354194+00:00 | Not calibrated | WEAK 31/100 | VERY_HIGH 76/100 | Do nothing | WATCH |
| 4 | SKY/USD | 0.04146 | 30.128 | 38.471 | +1.17% | -0.26% | 0.30x | 7.2 | 2026-11-25T04:37:21.354194+00:00 | Not calibrated | WEAK 20/100 | VERY_HIGH 81/100 | Do nothing | WATCH |
| 5 | BLESS/USD | 0.017798 | 23.857 | 29.483 | +1.18% | -0.52% | 0.70x | 32.1 | 2026-11-25T04:37:21.354194+00:00 | Not calibrated | WEAK 7/100 | EXTREME 88/100 | Do nothing | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | MON/USD | 67.697 | 0.00987 | +0.71% | 1.44x |
| 2 | DRV/USD | 60.022 | 0.33192 | -1.32% | 1.45x |
| 3 | XMR/USD | 55.018 | 512.26 | -0.18% | 0.71x |
| 4 | SKY/USD | 38.471 | 0.04146 | -0.26% | 0.30x |
| 5 | BLESS/USD | 29.483 | 0.017798 | -0.52% | 0.70x |

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

- Persisted scans: 1670; predictions: 14195; observations: 1012121.
- Matured sampled outcomes across 1/6/24/48h: 30008; gap abstentions: 22370. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 146 (sampled only; not a success-rate estimate).
- False positives / missed movers: NOT VERIFIED without eligible continuous outcome coverage.
- Baseline vs challenger: recorded as-of; unbiased held-out lift NOT MEASURED.
- Online Kraken /USD stablecoin-base pairs excluded: 18 (counted from this scan's online AssetPairs metadata, not inferred from price).
- Stablecoin base exclusions: BRL1, BUSD, DAI, EUR, EURC, EUROP, EURQ, EURR, EURT, FDUSD, FRAX, GUSD, PYUSD, QCAD, RLUSD, TGBP, TUSD, USD, USD1, USDC, USDD, USDE, USDG, USDQ, USDR, USDS, USDT, ZUSD.
- DEX: NOT USED; no DEX freshness gate.
- OHLC screening abstentions: 16; details in immutable scan JSON artifact.
- Storage: ledger and results published in one non-force Git commit and read back. Independent artifact recovery is NOT VERIFIED by this scan alone.
- Errors: none in successful committed scan; a failed workflow must not publish a SUCCESS report.

# Cryptoscanner — challenger and independent legacy-inspired WATCH

Paper only · risk is high or higher · 30%+ in 48h probability NOT CALIBRATED
Signal confidence 0–100 means setup strength only, NOT a win probability. Actions are research guidance; no trade authorization.

**Writer:** 45547719805 · **Generation:** 1670 · **Legacy run:** 45547719805
**Main quote time:** 2026-11-25T04:37:28.351248+00:00 · **Legacy report time:** 2026-11-25T04:38:43.457404+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | MON/USD ⭐ | 0.00987 | 75.64 | +0.71% | 1.44x | STRONG 83/100 | HIGH 67/100 | Watch |
| 2 | DRV/USD | 0.33192 | 57.91 | -1.32% | 1.45x | WEAK 39/100 | VERY_HIGH 82/100 | Do nothing |
| 3 | XMR/USD | 512.26 | 51.17 | -0.18% | 0.71x | WEAK 31/100 | VERY_HIGH 76/100 | Do nothing |
| 4 | SKY/USD | 0.04146 | 30.13 | -0.26% | 0.30x | WEAK 20/100 | VERY_HIGH 81/100 | Do nothing |
| 5 | BLESS/USD | 0.017798 | 23.86 | -0.52% | 0.70x | WEAK 7/100 | EXTREME 88/100 | Do nothing |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | MON/USD ⭐ | 0.00989 | 84.87 | +0.71% | 1.44x | 18621 | STRONG 92/100 | HIGH 61/100 | Watch |

**Same-run overlap:** MON/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
