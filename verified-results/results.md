# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-28T10:07:33.605655+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/46133423375
**Source SHA:** 858c8bc8ec5d7641ddb39cacd8aca91719f855b1
**Previous ledger commit:** d3b026d08a6e50fc24a32c67bd04de42096ffa0f (atomic ledger/results publication)
**Ledger generation:** 2139 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 4s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 628; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 610; valid market observations: 606; OHLC screened: 10.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | XMR/USD | 433.23 | 86.851 | 87.928 | +6.37% | -0.22% | 1.00x | 23.4 | 2026-11-28T10:07:29.776269+00:00 | Not calibrated | WEAK 43/100 | VERY_HIGH 80/100 | Watch | WATCH |
| 2 | NIGHT/USD | 0.05264 | 73.739 | 81.791 | +4.78% | -0.10% | 0.24x | 13.3 | 2026-11-28T10:07:29.776269+00:00 | Not calibrated | WEAK 37/100 | VERY_HIGH 82/100 | Watch | WATCH |
| 3 | VVV/USD | 26.644 | 68.084 | 64.394 | +3.48% | +0.12% | 1.31x | 8.6 | 2026-11-28T10:07:29.776269+00:00 | Not calibrated | MODERATE 69/100 | HIGH 55/100 | Watch | WATCH |
| 4 | SPACE/USD | 0.004533 | 66.394 | 75.538 | +8.50% | -0.24% | 0.21x | 2.2 | 2026-11-28T10:07:29.776269+00:00 | Not calibrated | WEAK 38/100 | EXTREME 88/100 | Do nothing | WATCH |
| 5 | SENT/USD | 0.023922 | 47.373 | 37.035 | +0.88% | -0.93% | 6.61x | 0.8 | 2026-11-28T10:07:29.776269+00:00 | Not calibrated | MODERATE 54/100 | VERY_HIGH 73/100 | Watch | WATCH |
| 6 | PONS/USD | 0.1027 | 27.446 | 24.435 | +0.39% | -0.29% | 1.45x | 19.5 | 2026-11-28T10:07:29.776269+00:00 | Not calibrated | WEAK 29/100 | VERY_HIGH 79/100 | Do nothing | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | XMR/USD | 87.928 | 433.23 | -0.22% | 1.00x |
| 2 | NIGHT/USD | 81.791 | 0.05264 | -0.10% | 0.24x |
| 3 | SPACE/USD | 75.538 | 0.004533 | -0.24% | 0.21x |
| 4 | VVV/USD | 64.394 | 26.644 | +0.12% | 1.31x |
| 5 | SENT/USD | 37.035 | 0.023922 | -0.93% | 6.61x |
| 6 | PONS/USD | 24.435 | 0.1027 | -0.29% | 1.45x |

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

- Persisted scans: 2139; predictions: 19106; observations: 1295280.
- Matured sampled outcomes across 1/6/24/48h: 45304; gap abstentions: 25968. Per-horizon counts require independent audit; do not infer held-out lift.
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

**Writer:** 46133423375 · **Generation:** 2139 · **Legacy run:** 46133423375
**Main quote time:** 2026-11-28T10:07:33.605655+00:00 · **Legacy report time:** 2026-11-28T10:08:13.191889+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | XMR/USD | 433.23 | 86.85 | -0.22% | 1.00x | WEAK 43/100 | VERY_HIGH 80/100 | Watch |
| 2 | NIGHT/USD | 0.05264 | 73.74 | -0.10% | 0.24x | WEAK 37/100 | VERY_HIGH 82/100 | Watch |
| 3 | VVV/USD ⭐ | 26.644 | 68.08 | +0.12% | 1.31x | STRONG 79/100 | HIGH 55/100 | Watch |
| 4 | SPACE/USD | 0.004533 | 66.39 | -0.24% | 0.21x | WEAK 38/100 | EXTREME 88/100 | Do nothing |
| 5 | SENT/USD | 0.023922 | 47.37 | -0.93% | 6.61x | MODERATE 54/100 | VERY_HIGH 73/100 | Watch |
| 6 | PONS/USD | 0.1027 | 27.45 | -0.29% | 1.45x | WEAK 29/100 | VERY_HIGH 79/100 | Do nothing |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | VVV/USD ⭐ | 26.642 | 74.57 | +0.12% | 1.31x | 7589 | STRONG 82/100 | HIGH 55/100 | Watch |

**Same-run overlap:** VVV/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
