# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-25T16:48:05.124387+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/45657205454
**Source SHA:** 858c8bc8ec5d7641ddb39cacd8aca91719f855b1
**Previous ledger commit:** 87846f3b2ea88194e6f5dd77b9109d18e986f0ab (atomic ledger/results publication)
**Ledger generation:** 1740 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 3s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 627; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 609; valid market observations: 608; OHLC screened: 11.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | XPL/USD | 0.0455 | 51.825 | 48.460 | +3.41% | -0.44% | 1.56x | 22.0 | 2026-11-25T16:48:02.166972+00:00 | Not calibrated | WEAK 36/100 | VERY_HIGH 78/100 | Watch | WATCH |
| 2 | DRV/USD | 0.32522 | 48.372 | 54.702 | +3.48% | -0.20% | 0.47x | 15.1 | 2026-11-25T16:48:02.166972+00:00 | Not calibrated | WEAK 24/100 | VERY_HIGH 82/100 | Do nothing | WATCH |
| 3 | PIEVERSE/USD | 3.294 | 41.424 | 58.105 | +6.93% | -2.00% | 0.33x | 37.4 | 2026-11-25T16:48:02.166972+00:00 | Not calibrated | WEAK 11/100 | EXTREME 97/100 | Do nothing | WATCH |
| 4 | VVV/USD | 24.801 | 38.944 | 57.132 | +1.07% | -1.88% | 0.12x | 9.7 | 2026-11-25T16:48:02.166972+00:00 | Not calibrated | WEAK 24/100 | VERY_HIGH 80/100 | Do nothing | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | PIEVERSE/USD | 58.105 | 3.294 | -2.00% | 0.33x |
| 2 | VVV/USD | 57.132 | 24.801 | -1.88% | 0.12x |
| 3 | DRV/USD | 54.702 | 0.32522 | -0.20% | 0.47x |
| 4 | XPL/USD | 48.460 | 0.0455 | -0.44% | 1.56x |

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

- Persisted scans: 1740; predictions: 14635; observations: 1054705.
- Matured sampled outcomes across 1/6/24/48h: 32504; gap abstentions: 22430. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 146 (sampled only; not a success-rate estimate).
- False positives / missed movers: NOT VERIFIED without eligible continuous outcome coverage.
- Baseline vs challenger: recorded as-of; unbiased held-out lift NOT MEASURED.
- Online Kraken /USD stablecoin-base pairs excluded: 18 (counted from this scan's online AssetPairs metadata, not inferred from price).
- Stablecoin base exclusions: BRL1, BUSD, DAI, EUR, EURC, EUROP, EURQ, EURR, EURT, FDUSD, FRAX, GUSD, PYUSD, QCAD, RLUSD, TGBP, TUSD, USD, USD1, USDC, USDD, USDE, USDG, USDQ, USDR, USDS, USDT, ZUSD.
- DEX: NOT USED; no DEX freshness gate.
- OHLC screening abstentions: 7; details in immutable scan JSON artifact.
- Storage: ledger and results published in one non-force Git commit and read back. Independent artifact recovery is NOT VERIFIED by this scan alone.
- Errors: none in successful committed scan; a failed workflow must not publish a SUCCESS report.

# Cryptoscanner — challenger and independent legacy-inspired WATCH

Paper only · risk is high or higher · 30%+ in 48h probability NOT CALIBRATED
Signal confidence 0–100 means setup strength only, NOT a win probability. Actions are research guidance; no trade authorization.

**Writer:** 45657205454 · **Generation:** 1740 · **Legacy run:** 45657205454
**Main quote time:** 2026-11-25T16:48:05.124387+00:00 · **Legacy report time:** 2026-11-25T16:49:16.324738+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | XPL/USD | 0.0455 | 51.83 | -0.44% | 1.56x | WEAK 36/100 | VERY_HIGH 78/100 | Watch |
| 2 | DRV/USD | 0.32522 | 48.37 | -0.20% | 0.47x | WEAK 24/100 | VERY_HIGH 82/100 | Do nothing |
| 3 | PIEVERSE/USD | 3.294 | 41.42 | -2.00% | 0.33x | WEAK 11/100 | EXTREME 97/100 | Do nothing |
| 4 | VVV/USD | 24.801 | 38.94 | -1.88% | 0.12x | WEAK 24/100 | VERY_HIGH 80/100 | Do nothing |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | MON/USD | 0.01077 | 86.24 | +1.91% | 1.62x | 14029 | STRONG 88/100 | HIGH 55/100 | Consider small entry |

**Same-run overlap:** None
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
