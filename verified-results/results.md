# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-28T10:57:57.348472+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/46137363808
**Source SHA:** 858c8bc8ec5d7641ddb39cacd8aca91719f855b1
**Previous ledger commit:** 48d2dad6acde9341bbf9fc5546836ca80571bbbf (atomic ledger/results publication)
**Ledger generation:** 2144 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 3s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 628; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 610; valid market observations: 606; OHLC screened: 8.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | VVV/USD | 26.748 | 78.620 | 67.048 | +3.88% | +0.75% | 1.78x | 8.6 | 2026-11-28T10:57:54.365883+00:00 | Not calibrated | STRONG 84/100 | HIGH 55/100 | Consider small entry | WATCH |
| 2 | NIGHT/USD | 0.05253 | 78.367 | 84.051 | +4.56% | -0.74% | 0.80x | 5.7 | 2026-11-28T10:57:54.365883+00:00 | Not calibrated | WEAK 44/100 | HIGH 68/100 | Watch | WATCH |
| 3 | SPACE/USD | 0.004378 | 60.347 | 51.354 | +4.79% | -1.20% | 2.61x | 27.5 | 2026-11-28T10:57:54.365883+00:00 | Not calibrated | MODERATE 50/100 | EXTREME 89/100 | Do nothing | WATCH |
| 4 | SENT/USD | 0.024417 | 43.513 | 49.844 | +2.96% | +0.25% | 0.24x | 4.5 | 2026-11-28T10:57:54.365883+00:00 | Not calibrated | MODERATE 52/100 | VERY_HIGH 82/100 | Watch | WATCH |
| 5 | KAVA/USD | 0.028 | 34.091 | 31.907 | +2.56% | -0.71% | 1.57x | 35.7 | 2026-11-28T10:57:54.365883+00:00 | Not calibrated | WEAK 22/100 | VERY_HIGH 78/100 | Do nothing | WATCH |
| 6 | CC/USD | 0.07444 | 29.057 | 33.425 | +0.39% | -0.24% | 0.68x | 6.7 | 2026-11-28T10:57:54.365883+00:00 | Not calibrated | WEAK 20/100 | VERY_HIGH 81/100 | Do nothing | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | NIGHT/USD | 84.051 | 0.05253 | -0.74% | 0.80x |
| 2 | VVV/USD | 67.048 | 26.748 | +0.75% | 1.78x |
| 3 | SPACE/USD | 51.354 | 0.004378 | -1.20% | 2.61x |
| 4 | SENT/USD | 49.844 | 0.024417 | +0.25% | 0.24x |
| 5 | CC/USD | 33.425 | 0.07444 | -0.24% | 0.68x |
| 6 | KAVA/USD | 31.907 | 0.028 | -0.71% | 1.57x |

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

- Persisted scans: 2144; predictions: 19134; observations: 1298310.
- Matured sampled outcomes across 1/6/24/48h: 45497; gap abstentions: 25968. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 155 (sampled only; not a success-rate estimate).
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

**Writer:** 46137363808 · **Generation:** 2144 · **Legacy run:** 46137363808
**Main quote time:** 2026-11-28T10:57:57.348472+00:00 · **Legacy report time:** 2026-11-28T10:58:47.956388+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | VVV/USD ⭐ | 26.748 | 78.62 | +0.75% | 1.78x | STRONG 94/100 | HIGH 55/100 | Consider small entry |
| 2 | NIGHT/USD | 0.05253 | 78.37 | -0.74% | 0.80x | WEAK 44/100 | HIGH 68/100 | Watch |
| 3 | SPACE/USD | 0.004378 | 60.35 | -1.20% | 2.61x | MODERATE 50/100 | EXTREME 89/100 | Do nothing |
| 4 | SENT/USD | 0.024417 | 43.51 | +0.25% | 0.24x | MODERATE 52/100 | VERY_HIGH 82/100 | Watch |
| 5 | KAVA/USD | 0.028 | 34.09 | -0.71% | 1.57x | WEAK 22/100 | VERY_HIGH 78/100 | Do nothing |
| 6 | CC/USD | 0.07444 | 29.06 | -0.24% | 0.68x | WEAK 20/100 | VERY_HIGH 81/100 | Do nothing |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | VVV/USD ⭐ | 26.797 | 83.91 | +0.75% | 1.78x | 7743 | STRONG 92/100 | HIGH 61/100 | Consider small entry |

**Same-run overlap:** VVV/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
