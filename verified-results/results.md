# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-21T04:50:25.334511+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/44867960774
**Source SHA:** bdc7e68f7fa75fae6636b7738d52f10a65d92038
**Previous ledger commit:** 60aada4d2bacdac7f363e16ec395cc37cae18401 (atomic ledger/results publication)
**Ledger generation:** 1084 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 2s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 628; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 610; valid market observations: 608; OHLC screened: 6.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | CAP/USD | 0.096073 | 90.548 | 65.220 | +4.95% | +2.07% | 5.43x | 6.1 | 2026-11-21T04:50:23.429084+00:00 | Not calibrated | STRONG 100/100 | HIGH 60/100 | Consider small entry | WATCH |
| 2 | DRV/USD | 0.25542 | 56.995 | 59.461 | +4.02% | +0.92% | 0.29x | 12.1 | 2026-11-21T04:50:23.429084+00:00 | Not calibrated | MODERATE 53/100 | VERY_HIGH 76/100 | Watch | WATCH |
| 3 | SAPIEN/USD | 0.04211 | 35.715 | 34.958 | +2.28% | -0.71% | 1.43x | 23.6 | 2026-11-21T04:50:23.429084+00:00 | Not calibrated | WEAK 28/100 | EXTREME 85/100 | Do nothing | WATCH |
| 4 | BLESS/USD | 0.013873 | 24.054 | 21.525 | +0.73% | +1.15% | 0.68x | 38.7 | 2026-11-21T04:50:23.429084+00:00 | Not calibrated | WEAK 27/100 | EXTREME 87/100 | Do nothing | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | CAP/USD | 65.220 | 0.096073 | +2.07% | 5.43x |
| 2 | DRV/USD | 59.461 | 0.25542 | +0.92% | 0.29x |
| 3 | SAPIEN/USD | 34.958 | 0.04211 | -0.71% | 1.43x |
| 4 | BLESS/USD | 21.525 | 0.013873 | +1.15% | 0.68x |

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

- Persisted scans: 1084; predictions: 8599; observations: 655432.
- Matured sampled outcomes across 1/6/24/48h: 11161; gap abstentions: 19792. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 10 (sampled only; not a success-rate estimate).
- False positives / missed movers: NOT VERIFIED without eligible continuous outcome coverage.
- Baseline vs challenger: recorded as-of; unbiased held-out lift NOT MEASURED.
- Online Kraken /USD stablecoin-base pairs excluded: 18 (counted from this scan's online AssetPairs metadata, not inferred from price).
- Stablecoin base exclusions: BRL1, BUSD, DAI, EUR, EURC, EUROP, EURQ, EURR, EURT, FDUSD, FRAX, GUSD, PYUSD, QCAD, RLUSD, TGBP, TUSD, USD, USD1, USDC, USDD, USDE, USDG, USDQ, USDR, USDS, USDT, ZUSD.
- DEX: NOT USED; no DEX freshness gate.
- OHLC screening abstentions: 2; details in immutable scan JSON artifact.
- Storage: ledger and results published in one non-force Git commit and read back. Independent artifact recovery is NOT VERIFIED by this scan alone.
- Errors: none in successful committed scan; a failed workflow must not publish a SUCCESS report.

# Cryptoscanner — challenger and independent legacy-inspired WATCH

Paper only · risk is high or higher · 30%+ in 48h probability NOT CALIBRATED
Signal confidence 0–100 means setup strength only, NOT a win probability. Actions are research guidance; no trade authorization.

**Writer:** 44867960774 · **Generation:** 1084 · **Legacy run:** 44867960774
**Main quote time:** 2026-11-21T04:50:25.334511+00:00 · **Legacy report time:** 2026-11-21T04:51:08.410235+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | CAP/USD ⭐ | 0.096073 | 90.55 | +2.07% | 5.43x | STRONG 100/100 | HIGH 60/100 | Consider small entry |
| 2 | DRV/USD | 0.25542 | 56.99 | +0.92% | 0.29x | MODERATE 53/100 | VERY_HIGH 76/100 | Watch |
| 3 | SAPIEN/USD | 0.04211 | 35.71 | -0.71% | 1.43x | WEAK 28/100 | EXTREME 85/100 | Do nothing |
| 4 | BLESS/USD | 0.013873 | 24.05 | +1.15% | 0.68x | WEAK 27/100 | EXTREME 87/100 | Do nothing |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | CAP/USD ⭐ | 0.096556 | 86.40 | +2.07% | 5.43x | 4642 | STRONG 100/100 | HIGH 66/100 | Consider small entry |

**Same-run overlap:** CAP/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
