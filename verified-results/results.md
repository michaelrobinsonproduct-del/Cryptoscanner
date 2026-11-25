# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-25T02:27:20.652360+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/45532724399
**Source SHA:** 858c8bc8ec5d7641ddb39cacd8aca91719f855b1
**Previous ledger commit:** 57e981f21e41f10ec84a8d9de3ee528ce95f4898 (atomic ledger/results publication)
**Ledger generation:** 1657 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 3s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 628; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 610; valid market observations: 609; OHLC screened: 11.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | DRV/USD | 0.32891 | 66.469 | 54.805 | +4.66% | +0.81% | 1.76x | 24.7 | 2026-11-25T02:27:17.732111+00:00 | Not calibrated | MODERATE 68/100 | VERY_HIGH 72/100 | Watch | WATCH |
| 2 | PAXG/USD | 3551.36 | 36.110 | 40.813 | +0.27% | +0.20% | 0.43x | 0.3 | 2026-11-25T02:27:17.732111+00:00 | Not calibrated | WEAK 38/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 3 | XAUT/USD | 3554.9 | 35.150 | 35.743 | +0.49% | +0.25% | 0.82x | 0.3 | 2026-11-25T02:27:17.732111+00:00 | Not calibrated | MODERATE 48/100 | HIGH 67/100 | Watch | WATCH |
| 4 | GWEI/USD | 0.010333 | 16.591 | 21.006 | +0.27% | +0.13% | 0.50x | 23.3 | 2026-11-25T02:27:17.732111+00:00 | Not calibrated | WEAK 18/100 | EXTREME 94/100 | Do nothing | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | DRV/USD | 54.805 | 0.32891 | +0.81% | 1.76x |
| 2 | PAXG/USD | 40.813 | 3551.36 | +0.20% | 0.43x |
| 3 | XAUT/USD | 35.743 | 3554.9 | +0.25% | 0.82x |
| 4 | GWEI/USD | 21.006 | 0.010333 | +0.13% | 0.50x |

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

- Persisted scans: 1657; predictions: 14126; observations: 1004204.
- Matured sampled outcomes across 1/6/24/48h: 29617; gap abstentions: 22370. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 143 (sampled only; not a success-rate estimate).
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

**Writer:** 45532724399 · **Generation:** 1657 · **Legacy run:** 45532724399
**Main quote time:** 2026-11-25T02:27:20.652360+00:00 · **Legacy report time:** 2026-11-25T02:28:14.052432+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | DRV/USD ⭐ | 0.32891 | 66.47 | +0.81% | 1.76x | STRONG 78/100 | VERY_HIGH 72/100 | Watch |
| 2 | PAXG/USD | 3551.36 | 36.11 | +0.20% | 0.43x | WEAK 38/100 | VERY_HIGH 70/100 | Watch |
| 3 | XAUT/USD | 3554.9 | 35.15 | +0.25% | 0.82x | MODERATE 48/100 | HIGH 67/100 | Watch |
| 4 | GWEI/USD | 0.010333 | 16.59 | +0.13% | 0.50x | WEAK 18/100 | EXTREME 94/100 | Do nothing |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | DRV/USD ⭐ | 0.32756 | 78.21 | +0.81% | 1.76x | 6502 | STRONG 89/100 | HIGH 66/100 | Consider small entry |

**Same-run overlap:** DRV/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
