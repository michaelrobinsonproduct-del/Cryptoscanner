# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-25T12:02:19.236280+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/45609504564
**Source SHA:** 858c8bc8ec5d7641ddb39cacd8aca91719f855b1
**Previous ledger commit:** 0edab572cd33d9c6bfd14c9b6f062afc4765bf56 (atomic ledger/results publication)
**Ledger generation:** 1715 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 5s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 627; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 609; valid market observations: 608; OHLC screened: 14.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | BABY/USD | 0.00878 | 88.326 | 69.869 | +6.30% | +0.69% | 5.40x | 11.4 | 2026-11-25T12:02:14.643087+00:00 | Not calibrated | STRONG 94/100 | VERY_HIGH 73/100 | Watch | WATCH |
| 2 | VVV/USD | 24.84 | 69.735 | 56.360 | +1.23% | -0.33% | 2.98x | 14.5 | 2026-11-25T12:02:14.643087+00:00 | Not calibrated | MODERATE 60/100 | HIGH 67/100 | Watch | WATCH |
| 3 | MON/USD | 0.00985 | 64.901 | 66.383 | +4.01% | -1.01% | 1.36x | 20.4 | 2026-11-25T12:02:14.643087+00:00 | Not calibrated | WEAK 42/100 | VERY_HIGH 77/100 | Watch | WATCH |
| 4 | TREAD/USD | 1.035 | 59.735 | 53.636 | +3.55% | +0.59% | 1.31x | 4.8 | 2026-11-25T12:02:14.643087+00:00 | Not calibrated | STRONG 75/100 | HIGH 67/100 | Watch | WATCH |
| 5 | CT/USD | 0.1295 | 35.240 | 37.070 | +2.53% | +0.94% | 0.35x | 23.2 | 2026-11-25T12:02:14.643087+00:00 | Not calibrated | WEAK 38/100 | EXTREME 94/100 | Do nothing | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | BABY/USD | 69.869 | 0.00878 | +0.69% | 5.40x |
| 2 | MON/USD | 66.383 | 0.00985 | -1.01% | 1.36x |
| 3 | VVV/USD | 56.360 | 24.84 | -0.33% | 2.98x |
| 4 | TREAD/USD | 53.636 | 1.035 | +0.59% | 1.31x |
| 5 | CT/USD | 37.070 | 0.1295 | +0.94% | 0.35x |

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

- Persisted scans: 1715; predictions: 14493; observations: 1039505.
- Matured sampled outcomes across 1/6/24/48h: 31608; gap abstentions: 22370. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 146 (sampled only; not a success-rate estimate).
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

**Writer:** 45609504564 · **Generation:** 1715 · **Legacy run:** 45609504564
**Main quote time:** 2026-11-25T12:02:19.236280+00:00 · **Legacy report time:** 2026-11-25T12:03:08.601987+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | BABY/USD ⭐ | 0.00878 | 88.33 | +0.69% | 5.40x | STRONG 100/100 | VERY_HIGH 73/100 | Watch |
| 2 | VVV/USD | 24.84 | 69.73 | -0.33% | 2.98x | MODERATE 60/100 | HIGH 67/100 | Watch |
| 3 | MON/USD | 0.00985 | 64.90 | -1.01% | 1.36x | WEAK 42/100 | VERY_HIGH 77/100 | Watch |
| 4 | TREAD/USD ⭐ | 1.035 | 59.73 | +0.59% | 1.31x | STRONG 85/100 | HIGH 67/100 | Watch |
| 5 | CT/USD | 0.1295 | 35.24 | +0.94% | 0.35x | WEAK 38/100 | EXTREME 94/100 | Do nothing |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | BABY/USD ⭐ | 0.0088 | 80.98 | +0.69% | 5.40x | 2984 | STRONG 95/100 | VERY_HIGH 79/100 | Watch |
| 2 | TREAD/USD ⭐ | 1.035 | 73.71 | +0.59% | 1.31x | 2722 | STRONG 92/100 | HIGH 67/100 | Watch |

**Same-run overlap:** BABY/USD, TREAD/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
