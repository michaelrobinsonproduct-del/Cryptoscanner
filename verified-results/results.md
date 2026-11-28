# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-28T10:48:01.593605+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/46136595176
**Source SHA:** 858c8bc8ec5d7641ddb39cacd8aca91719f855b1
**Previous ledger commit:** cf39e2e61531e46ae6f0d11e02f94eac19fc339e (atomic ledger/results publication)
**Ledger generation:** 2143 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 3s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 628; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 610; valid market observations: 606; OHLC screened: 9.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | NIGHT/USD | 0.05272 | 84.723 | 85.761 | +4.94% | -0.21% | 1.00x | 7.6 | 2026-11-28T10:47:58.482156+00:00 | Not calibrated | MODERATE 52/100 | HIGH 68/100 | Watch | WATCH |
| 2 | SPACE/USD | 0.004444 | 76.995 | 66.026 | +6.37% | -0.04% | 2.12x | 20.3 | 2026-11-28T10:47:58.482156+00:00 | Not calibrated | MODERATE 58/100 | EXTREME 85/100 | Do nothing | WATCH |
| 3 | VVV/USD | 26.819 | 69.695 | 69.330 | +4.16% | +0.43% | 0.82x | 7.8 | 2026-11-28T10:47:58.482156+00:00 | Not calibrated | MODERATE 65/100 | HIGH 62/100 | Watch | WATCH |
| 4 | SENT/USD | 0.024472 | 43.240 | 53.114 | +3.20% | -0.54% | 0.28x | 1.2 | 2026-11-28T10:47:58.482156+00:00 | Not calibrated | WEAK 27/100 | EXTREME 88/100 | Do nothing | WATCH |
| 5 | CC/USD | 0.07469 | 26.181 | 35.807 | +0.73% | -0.32% | 0.20x | 6.7 | 2026-11-28T10:47:58.482156+00:00 | Not calibrated | WEAK 18/100 | VERY_HIGH 81/100 | Do nothing | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | NIGHT/USD | 85.761 | 0.05272 | -0.21% | 1.00x |
| 2 | VVV/USD | 69.330 | 26.819 | +0.43% | 0.82x |
| 3 | SPACE/USD | 66.026 | 0.004444 | -0.04% | 2.12x |
| 4 | SENT/USD | 53.114 | 0.024472 | -0.54% | 0.28x |
| 5 | CC/USD | 35.807 | 0.07469 | -0.32% | 0.20x |

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

- Persisted scans: 2143; predictions: 19128; observations: 1297704.
- Matured sampled outcomes across 1/6/24/48h: 45459; gap abstentions: 25968. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 155 (sampled only; not a success-rate estimate).
- False positives / missed movers: NOT VERIFIED without eligible continuous outcome coverage.
- Baseline vs challenger: recorded as-of; unbiased held-out lift NOT MEASURED.
- Online Kraken /USD stablecoin-base pairs excluded: 18 (counted from this scan's online AssetPairs metadata, not inferred from price).
- Stablecoin base exclusions: BRL1, BUSD, DAI, EUR, EURC, EUROP, EURQ, EURR, EURT, FDUSD, FRAX, GUSD, PYUSD, QCAD, RLUSD, TGBP, TUSD, USD, USD1, USDC, USDD, USDE, USDG, USDQ, USDR, USDS, USDT, ZUSD.
- DEX: NOT USED; no DEX freshness gate.
- OHLC screening abstentions: 4; details in immutable scan JSON artifact.
- Storage: ledger and results published in one non-force Git commit and read back. Independent artifact recovery is NOT VERIFIED by this scan alone.
- Errors: none in successful committed scan; a failed workflow must not publish a SUCCESS report.

# Cryptoscanner — challenger and independent legacy-inspired WATCH

Paper only · risk is high or higher · 30%+ in 48h probability NOT CALIBRATED
Signal confidence 0–100 means setup strength only, NOT a win probability. Actions are research guidance; no trade authorization.

**Writer:** 46136595176 · **Generation:** 2143 · **Legacy run:** 46136595176
**Main quote time:** 2026-11-28T10:48:01.593605+00:00 · **Legacy report time:** 2026-11-28T10:48:43.418779+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | NIGHT/USD | 0.05272 | 84.72 | -0.21% | 1.00x | MODERATE 52/100 | HIGH 68/100 | Watch |
| 2 | SPACE/USD | 0.004444 | 77.00 | -0.04% | 2.12x | MODERATE 58/100 | EXTREME 85/100 | Do nothing |
| 3 | VVV/USD | 26.819 | 69.69 | +0.43% | 0.82x | MODERATE 65/100 | HIGH 62/100 | Watch |
| 4 | SENT/USD | 0.024472 | 43.24 | -0.54% | 0.28x | WEAK 27/100 | EXTREME 88/100 | Do nothing |
| 5 | CC/USD | 0.07469 | 26.18 | -0.32% | 0.20x | WEAK 18/100 | VERY_HIGH 81/100 | Do nothing |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | PIEVERSE/USD | 3.95 | 64.81 | +2.60% | 18.21x | 1991 | STRONG 72/100 | VERY_HIGH 77/100 | Watch |

**Same-run overlap:** None
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
