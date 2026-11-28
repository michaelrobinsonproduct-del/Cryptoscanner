# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-28T13:22:56.305721+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/46149045296
**Source SHA:** 858c8bc8ec5d7641ddb39cacd8aca91719f855b1
**Previous ledger commit:** d87f941a46d3219e54e53c7067925027d2d78f02 (atomic ledger/results publication)
**Ledger generation:** 2159 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 2s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 628; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 610; valid market observations: 606; OHLC screened: 9.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | NIGHT/USD | 0.0542 | 93.154 | 96.308 | +7.88% | -1.14% | 1.25x | 7.4 | 2026-11-28T13:22:53.951326+00:00 | Not calibrated | MODERATE 57/100 | HIGH 65/100 | Watch | WATCH |
| 2 | XMR/USD | 437 | 82.218 | 86.692 | +7.30% | -0.24% | 0.67x | 26.6 | 2026-11-28T13:22:53.951326+00:00 | Not calibrated | WEAK 36/100 | EXTREME 88/100 | Do nothing | WATCH |
| 3 | SENT/USD | 0.024625 | 55.702 | 55.517 | +3.84% | +0.82% | 0.61x | 5.7 | 2026-11-28T13:22:53.951326+00:00 | Not calibrated | MODERATE 58/100 | VERY_HIGH 82/100 | Watch | WATCH |
| 4 | VVV/USD | 26.643 | 54.403 | 63.146 | +3.47% | -0.37% | 0.31x | 9.4 | 2026-11-28T13:22:53.951326+00:00 | Not calibrated | WEAK 32/100 | VERY_HIGH 76/100 | Do nothing | WATCH |
| 5 | AKE/USD | 0.00110629 | 17.257 | 26.040 | +1.82% | -3.20% | 1.72x | 44.9 | 2026-11-28T13:22:53.951326+00:00 | Not calibrated | WEAK 14/100 | EXTREME 92/100 | Do nothing | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | NIGHT/USD | 96.308 | 0.0542 | -1.14% | 1.25x |
| 2 | XMR/USD | 86.692 | 437 | -0.24% | 0.67x |
| 3 | VVV/USD | 63.146 | 26.643 | -0.37% | 0.31x |
| 4 | SENT/USD | 55.517 | 0.024625 | +0.82% | 0.61x |
| 5 | AKE/USD | 26.040 | 0.00110629 | -3.20% | 1.72x |

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

- Persisted scans: 2159; predictions: 19225; observations: 1307400.
- Matured sampled outcomes across 1/6/24/48h: 46046; gap abstentions: 25968. Per-horizon counts require independent audit; do not infer held-out lift.
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

**Writer:** 46149045296 · **Generation:** 2159 · **Legacy run:** 46149045296
**Main quote time:** 2026-11-28T13:22:56.305721+00:00 · **Legacy report time:** 2026-11-28T13:23:54.104690+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | NIGHT/USD | 0.0542 | 93.15 | -1.14% | 1.25x | MODERATE 57/100 | HIGH 65/100 | Watch |
| 2 | XMR/USD | 437 | 82.22 | -0.24% | 0.67x | WEAK 36/100 | EXTREME 88/100 | Do nothing |
| 3 | SENT/USD | 0.024625 | 55.70 | +0.82% | 0.61x | MODERATE 58/100 | VERY_HIGH 82/100 | Watch |
| 4 | VVV/USD | 26.643 | 54.40 | -0.37% | 0.31x | WEAK 32/100 | VERY_HIGH 76/100 | Do nothing |
| 5 | AKE/USD | 0.00110629 | 17.26 | -3.20% | 1.72x | WEAK 14/100 | EXTREME 92/100 | Do nothing |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | SKY/USD | 0.05201 | 41.57 | +0.17% | 3.53x | 9238 | MODERATE 66/100 | HIGH 55/100 | Watch |

**Same-run overlap:** None
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
