# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-28T00:32:35.472571+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/46088154039
**Source SHA:** 858c8bc8ec5d7641ddb39cacd8aca91719f855b1
**Previous ledger commit:** 5c1867fe2c776311c8f7f97a7e1a914eb693253c (atomic ledger/results publication)
**Ledger generation:** 2081 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 4s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 628; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 610; valid market observations: 606; OHLC screened: 15.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | HYPE/USD | 63.67 | 70.650 | 56.199 | +0.28% | -0.11% | 5.66x | 1.6 | 2026-11-28T00:32:31.322662+00:00 | Not calibrated | MODERATE 65/100 | HIGH 61/100 | Watch | WATCH |
| 2 | LTC/USD | 45.41 | 56.548 | 56.827 | +0.58% | +0.38% | 0.78x | 4.4 | 2026-11-28T00:32:31.322662+00:00 | Not calibrated | MODERATE 58/100 | HIGH 62/100 | Watch | WATCH |
| 3 | SKY/USD | 0.05225 | 48.217 | 38.560 | +0.67% | -1.07% | 6.04x | 11.5 | 2026-11-28T00:32:31.322662+00:00 | Not calibrated | MODERATE 49/100 | VERY_HIGH 71/100 | Watch | WATCH |
| 4 | VVV/USD | 25.9 | 47.372 | 48.328 | +0.59% | +0.66% | 0.57x | 7.3 | 2026-11-28T00:32:31.322662+00:00 | Not calibrated | MODERATE 54/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 5 | DRV/USD | 0.36419 | 40.752 | 31.720 | +0.37% | +0.30% | 1.75x | 11.5 | 2026-11-28T00:32:31.322662+00:00 | Not calibrated | MODERATE 60/100 | HIGH 66/100 | Watch | WATCH |
| 6 | SPX/USD | 0.2733 | 23.340 | 28.881 | +0.33% | -0.04% | 0.46x | 11.0 | 2026-11-28T00:32:31.322662+00:00 | Not calibrated | WEAK 12/100 | EXTREME 87/100 | Do nothing | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | LTC/USD | 56.827 | 45.41 | +0.38% | 0.78x |
| 2 | HYPE/USD | 56.199 | 63.67 | -0.11% | 5.66x |
| 3 | VVV/USD | 48.328 | 25.9 | +0.66% | 0.57x |
| 4 | SKY/USD | 38.560 | 0.05225 | -1.07% | 6.04x |
| 5 | DRV/USD | 31.720 | 0.36419 | +0.30% | 1.75x |
| 6 | SPX/USD | 28.881 | 0.2733 | -0.04% | 0.46x |

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

- Persisted scans: 2081; predictions: 18644; observations: 1260133.
- Matured sampled outcomes across 1/6/24/48h: 42762; gap abstentions: 25968. Per-horizon counts require independent audit; do not infer held-out lift.
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

**Writer:** 46088154039 · **Generation:** 2081 · **Legacy run:** 46088154039
**Main quote time:** 2026-11-28T00:32:35.472571+00:00 · **Legacy report time:** 2026-11-28T00:33:30.901990+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | HYPE/USD | 63.67 | 70.65 | -0.11% | 5.66x | MODERATE 65/100 | HIGH 61/100 | Watch |
| 2 | LTC/USD | 45.41 | 56.55 | +0.38% | 0.78x | MODERATE 58/100 | HIGH 62/100 | Watch |
| 3 | SKY/USD | 0.05225 | 48.22 | -1.07% | 6.04x | MODERATE 49/100 | VERY_HIGH 71/100 | Watch |
| 4 | VVV/USD | 25.9 | 47.37 | +0.66% | 0.57x | MODERATE 54/100 | VERY_HIGH 70/100 | Watch |
| 5 | DRV/USD | 0.36419 | 40.75 | +0.30% | 1.75x | MODERATE 60/100 | HIGH 66/100 | Watch |
| 6 | SPX/USD | 0.2733 | 23.34 | -0.04% | 0.46x | WEAK 12/100 | EXTREME 87/100 | Do nothing |

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
