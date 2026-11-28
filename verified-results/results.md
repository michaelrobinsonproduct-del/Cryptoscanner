# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-28T01:02:46.315239+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/46090799995
**Source SHA:** 858c8bc8ec5d7641ddb39cacd8aca91719f855b1
**Previous ledger commit:** 1a6947da55a2b4173d2cfdc12181c0febcbffb08 (atomic ledger/results publication)
**Ledger generation:** 2084 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 8s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 628; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 610; valid market observations: 606; OHLC screened: 23.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | TAO/USD | 187.5825 | 71.203 | 54.901 | +0.34% | +0.26% | 4.09x | 4.9 | 2026-11-28T01:02:38.119322+00:00 | Not calibrated | STRONG 91/100 | HIGH 55/100 | Consider small entry | WATCH |
| 2 | ZEC/USD | 736.92 | 57.377 | 54.524 | +0.32% | +0.27% | 1.15x | 5.4 | 2026-11-28T01:02:38.119322+00:00 | Not calibrated | MODERATE 64/100 | HIGH 62/100 | Watch | WATCH |
| 3 | DRV/USD | 0.36505 | 50.312 | 35.395 | +0.61% | -0.02% | 4.40x | 7.7 | 2026-11-28T01:02:38.119322+00:00 | Not calibrated | MODERATE 55/100 | HIGH 66/100 | Watch | WATCH |
| 4 | BCH/USD | 208.16 | 49.192 | 39.390 | +0.56% | +0.10% | 1.93x | 5.3 | 2026-11-28T01:02:38.119322+00:00 | Not calibrated | MODERATE 60/100 | HIGH 55/100 | Watch | WATCH |
| 5 | BAT/USD | 0.07531 | 48.575 | 31.379 | +0.44% | +0.44% | 4.42x | 5.3 | 2026-11-28T01:02:38.119322+00:00 | Not calibrated | STRONG 79/100 | HIGH 67/100 | Watch | WATCH |
| 6 | HYPE/USD | 63.73 | 46.610 | 56.077 | +0.38% | +0.00% | 0.05x | 3.1 | 2026-11-28T01:02:38.119322+00:00 | Not calibrated | WEAK 43/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 7 | SKY/USD | 0.05234 | 38.661 | 39.993 | +0.85% | +0.81% | 0.46x | 11.5 | 2026-11-28T01:02:38.119322+00:00 | Not calibrated | WEAK 44/100 | VERY_HIGH 76/100 | Watch | WATCH |
| 8 | SENT/USD | 0.023787 | 27.281 | 30.997 | +0.31% | -0.52% | 0.89x | 3.8 | 2026-11-28T01:02:38.119322+00:00 | Not calibrated | WEAK 19/100 | VERY_HIGH 80/100 | Do nothing | WATCH |
| 9 | ATOM/USD | 1.2387 | 26.787 | 32.487 | +0.89% | +0.22% | 0.32x | 11.3 | 2026-11-28T01:02:38.119322+00:00 | Not calibrated | WEAK 38/100 | VERY_HIGH 81/100 | Watch | WATCH |
| 10 | SPX/USD | 0.2731 | 15.370 | 24.683 | +0.26% | +0.04% | 0.05x | 18.3 | 2026-11-28T01:02:38.119322+00:00 | Not calibrated | WEAK 23/100 | VERY_HIGH 81/100 | Do nothing | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | HYPE/USD | 56.077 | 63.73 | +0.00% | 0.05x |
| 2 | TAO/USD | 54.901 | 187.5825 | +0.26% | 4.09x |
| 3 | ZEC/USD | 54.524 | 736.92 | +0.27% | 1.15x |
| 4 | SKY/USD | 39.993 | 0.05234 | +0.81% | 0.46x |
| 5 | BCH/USD | 39.390 | 208.16 | +0.10% | 1.93x |
| 6 | DRV/USD | 35.395 | 0.36505 | -0.02% | 4.40x |
| 7 | ATOM/USD | 32.487 | 1.2387 | +0.22% | 0.32x |
| 8 | BAT/USD | 31.379 | 0.07531 | +0.44% | 4.42x |
| 9 | SENT/USD | 30.997 | 0.023787 | -0.52% | 0.89x |
| 10 | SPX/USD | 24.683 | 0.2731 | +0.04% | 0.05x |

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

- Persisted scans: 2084; predictions: 18671; observations: 1261950.
- Matured sampled outcomes across 1/6/24/48h: 42876; gap abstentions: 25968. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 155 (sampled only; not a success-rate estimate).
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

**Writer:** 46090799995 · **Generation:** 2084 · **Legacy run:** 46090799995
**Main quote time:** 2026-11-28T01:02:46.315239+00:00 · **Legacy report time:** 2026-11-28T01:03:40.750988+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | TAO/USD ⭐ | 187.5825 | 71.20 | +0.26% | 4.09x | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 2 | ZEC/USD ⭐ | 736.92 | 57.38 | +0.27% | 1.15x | STRONG 74/100 | HIGH 62/100 | Watch |
| 3 | DRV/USD | 0.36505 | 50.31 | -0.02% | 4.40x | MODERATE 55/100 | HIGH 66/100 | Watch |
| 4 | BCH/USD ⭐ | 208.16 | 49.19 | +0.10% | 1.93x | STRONG 70/100 | HIGH 55/100 | Watch |
| 5 | BAT/USD | 0.07531 | 48.57 | +0.44% | 4.42x | STRONG 79/100 | HIGH 67/100 | Watch |
| 6 | HYPE/USD | 63.73 | 46.61 | +0.00% | 0.05x | WEAK 43/100 | VERY_HIGH 70/100 | Watch |
| 7 | SKY/USD | 0.05234 | 38.66 | +0.81% | 0.46x | WEAK 44/100 | VERY_HIGH 76/100 | Watch |
| 8 | SENT/USD | 0.023787 | 27.28 | -0.52% | 0.89x | WEAK 19/100 | VERY_HIGH 80/100 | Do nothing |
| 9 | ATOM/USD | 1.2387 | 26.79 | +0.22% | 0.32x | WEAK 38/100 | VERY_HIGH 81/100 | Watch |
| 10 | SPX/USD | 0.2731 | 15.37 | +0.04% | 0.05x | WEAK 23/100 | VERY_HIGH 81/100 | Do nothing |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | TAO/USD ⭐ | 188.1681 | 53.90 | +0.26% | 4.09x | 9289 | STRONG 92/100 | HIGH 55/100 | Consider small entry |
| 2 | ZEC/USD ⭐ | 737.94 | 48.61 | +0.27% | 1.15x | 33628 | MODERATE 69/100 | HIGH 62/100 | Watch |
| 3 | BCH/USD ⭐ | 208.28 | 47.55 | +0.10% | 1.93x | 3289 | MODERATE 69/100 | HIGH 55/100 | Watch |

**Same-run overlap:** TAO/USD, ZEC/USD, BCH/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
