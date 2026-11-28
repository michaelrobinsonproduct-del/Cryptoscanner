# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-28T18:39:39.824032+00:00
**GitHub trigger:** scheduled (verified event=schedule; originating cron=2,7,12,17,22,27,32,37,42,47,52,57 * * * *, intended UTC minute=2,7,12,17,22,27,32,37,42,47,52,57; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/46176782645
**Source SHA:** 858c8bc8ec5d7641ddb39cacd8aca91719f855b1
**Previous ledger commit:** f2f0eab99684fc23b8cfa4310118731f6d76b60a (atomic ledger/results publication)
**Ledger generation:** 2191 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 5s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 628; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 610; valid market observations: 607; OHLC screened: 13.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | NIGHT/USD | 0.05242 | 76.794 | 81.327 | +4.34% | +0.23% | 0.43x | 5.7 | 2026-11-28T18:39:35.291806+00:00 | Not calibrated | MODERATE 68/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 2 | XMR/USD | 421.93 | 61.440 | 66.772 | +3.60% | -0.43% | 0.68x | 26.8 | 2026-11-28T18:39:35.291806+00:00 | Not calibrated | WEAK 26/100 | EXTREME 88/100 | Do nothing | WATCH |
| 3 | VVV/USD | 26.296 | 47.658 | 51.341 | +2.12% | +0.42% | 0.42x | 10.7 | 2026-11-28T18:39:35.291806+00:00 | Not calibrated | MODERATE 49/100 | VERY_HIGH 76/100 | Watch | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | NIGHT/USD | 81.327 | 0.05242 | +0.23% | 0.43x |
| 2 | XMR/USD | 66.772 | 421.93 | -0.43% | 0.68x |
| 3 | VVV/USD | 51.341 | 26.296 | +0.42% | 0.42x |

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

- Persisted scans: 2191; predictions: 19362; observations: 1326798.
- Matured sampled outcomes across 1/6/24/48h: 47165; gap abstentions: 25968. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 158 (sampled only; not a success-rate estimate).
- False positives / missed movers: NOT VERIFIED without eligible continuous outcome coverage.
- Baseline vs challenger: recorded as-of; unbiased held-out lift NOT MEASURED.
- Online Kraken /USD stablecoin-base pairs excluded: 18 (counted from this scan's online AssetPairs metadata, not inferred from price).
- Stablecoin base exclusions: BRL1, BUSD, DAI, EUR, EURC, EUROP, EURQ, EURR, EURT, FDUSD, FRAX, GUSD, PYUSD, QCAD, RLUSD, TGBP, TUSD, USD, USD1, USDC, USDD, USDE, USDG, USDQ, USDR, USDS, USDT, ZUSD.
- DEX: NOT USED; no DEX freshness gate.
- OHLC screening abstentions: 10; details in immutable scan JSON artifact.
- Storage: ledger and results published in one non-force Git commit and read back. Independent artifact recovery is NOT VERIFIED by this scan alone.
- Errors: none in successful committed scan; a failed workflow must not publish a SUCCESS report.

# Cryptoscanner — challenger and independent legacy-inspired WATCH

Paper only · risk is high or higher · 30%+ in 48h probability NOT CALIBRATED
Signal confidence 0–100 means setup strength only, NOT a win probability. Actions are research guidance; no trade authorization.

**Writer:** 46176782645 · **Generation:** 2191 · **Legacy run:** 46176782645
**Main quote time:** 2026-11-28T18:39:39.824032+00:00 · **Legacy report time:** 2026-11-28T18:40:23.178125+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | NIGHT/USD | 0.05242 | 76.79 | +0.23% | 0.43x | MODERATE 68/100 | VERY_HIGH 70/100 | Watch |
| 2 | XMR/USD | 421.93 | 61.44 | -0.43% | 0.68x | WEAK 26/100 | EXTREME 88/100 | Do nothing |
| 3 | VVV/USD | 26.296 | 47.66 | +0.42% | 0.42x | MODERATE 49/100 | VERY_HIGH 76/100 | Watch |

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
