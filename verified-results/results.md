# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-25T08:07:21.822031+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/45573152432
**Source SHA:** 858c8bc8ec5d7641ddb39cacd8aca91719f855b1
**Previous ledger commit:** 7fc0da35775f6cf04389a6027b085eb927d0a16b (atomic ledger/results publication)
**Ledger generation:** 1691 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 7s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 628; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 610; valid market observations: 609; OHLC screened: 21.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | DRV/USD | 0.33264 | 90.319 | 76.084 | +5.84% | -0.12% | 2.48x | 4.2 | 2026-11-25T08:07:14.959830+00:00 | Not calibrated | STRONG 75/100 | HIGH 61/100 | Watch | WATCH |
| 2 | PROS/USD | 0.7274 | 67.832 | 63.314 | +8.45% | +1.80% | 0.55x | 27.4 | 2026-11-25T08:07:14.959830+00:00 | Not calibrated | MODERATE 54/100 | EXTREME 87/100 | Do nothing | WATCH |
| 3 | PEPE/USD | 3.481e-06 | 56.581 | 47.794 | +0.81% | +0.49% | 1.63x | 5.7 | 2026-11-25T08:07:14.959830+00:00 | Not calibrated | STRONG 73/100 | HIGH 55/100 | Watch | WATCH |
| 4 | CC/USD | 0.07538 | 51.793 | 33.597 | +0.44% | +0.64% | 10.35x | 8.0 | 2026-11-25T08:07:14.959830+00:00 | Not calibrated | STRONG 81/100 | HIGH 60/100 | Watch | WATCH |
| 5 | AKT/USD | 0.469 | 47.361 | 32.772 | +0.88% | +0.69% | 2.12x | 10.7 | 2026-11-25T08:07:14.959830+00:00 | Not calibrated | STRONG 74/100 | HIGH 66/100 | Watch | WATCH |
| 6 | XPL/USD | 0.0449 | 40.566 | 38.463 | +2.05% | +0.45% | 0.99x | 22.3 | 2026-11-25T08:07:14.959830+00:00 | Not calibrated | WEAK 40/100 | VERY_HIGH 79/100 | Watch | WATCH |
| 7 | BABY/USD | 0.00868 | 37.606 | 56.380 | +5.08% | -2.93% | 0.59x | 23.0 | 2026-11-25T08:07:14.959830+00:00 | Not calibrated | WEAK 14/100 | EXTREME 97/100 | Do nothing | WATCH |
| 8 | CAP/USD | 0.09305 | 31.503 | 33.976 | +0.68% | +0.33% | 0.59x | 5.9 | 2026-11-25T08:07:14.959830+00:00 | Not calibrated | MODERATE 46/100 | VERY_HIGH 75/100 | Watch | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | DRV/USD | 76.084 | 0.33264 | -0.12% | 2.48x |
| 2 | PROS/USD | 63.314 | 0.7274 | +1.80% | 0.55x |
| 3 | BABY/USD | 56.380 | 0.00868 | -2.93% | 0.59x |
| 4 | PEPE/USD | 47.794 | 3.481e-06 | +0.49% | 1.63x |
| 5 | XPL/USD | 38.463 | 0.0449 | +0.45% | 0.99x |
| 6 | CAP/USD | 33.976 | 0.09305 | +0.33% | 0.59x |
| 7 | CC/USD | 33.597 | 0.07538 | +0.64% | 10.35x |
| 8 | AKT/USD | 32.772 | 0.469 | +0.69% | 2.12x |

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

- Persisted scans: 1691; predictions: 14356; observations: 1024910.
- Matured sampled outcomes across 1/6/24/48h: 30783; gap abstentions: 22370. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 146 (sampled only; not a success-rate estimate).
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

**Writer:** 45573152432 · **Generation:** 1691 · **Legacy run:** 45573152432
**Main quote time:** 2026-11-25T08:07:21.822031+00:00 · **Legacy report time:** 2026-11-25T08:08:12.031772+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | DRV/USD | 0.33264 | 90.32 | -0.12% | 2.48x | STRONG 75/100 | HIGH 61/100 | Watch |
| 2 | PROS/USD | 0.7274 | 67.83 | +1.80% | 0.55x | MODERATE 54/100 | EXTREME 87/100 | Do nothing |
| 3 | PEPE/USD ⭐ | 3.481e-06 | 56.58 | +0.49% | 1.63x | STRONG 83/100 | HIGH 55/100 | Consider small entry |
| 4 | CC/USD ⭐ | 0.07538 | 51.79 | +0.64% | 10.35x | STRONG 91/100 | HIGH 60/100 | Consider small entry |
| 5 | AKT/USD ⭐ | 0.469 | 47.36 | +0.69% | 2.12x | STRONG 84/100 | HIGH 66/100 | Consider small entry |
| 6 | XPL/USD | 0.0449 | 40.57 | +0.45% | 0.99x | WEAK 40/100 | VERY_HIGH 79/100 | Watch |
| 7 | BABY/USD | 0.00868 | 37.61 | -2.93% | 0.59x | WEAK 14/100 | EXTREME 97/100 | Do nothing |
| 8 | CAP/USD | 0.09305 | 31.50 | +0.33% | 0.59x | MODERATE 46/100 | VERY_HIGH 75/100 | Watch |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | TRX/USD | 0.308133 | 51.06 | +0.09% | 8.25x | 3554 | STRONG 71/100 | HIGH 55/100 | Watch |
| 2 | PEPE/USD ⭐ | 3.48e-06 | 47.92 | +0.49% | 1.63x | 5784 | STRONG 79/100 | HIGH 55/100 | Consider small entry |
| 3 | CC/USD ⭐ | 0.07529 | 42.83 | +0.64% | 10.35x | 5486 | STRONG 86/100 | HIGH 60/100 | Consider small entry |
| 4 | AKT/USD ⭐ | 0.469 | 40.27 | +0.69% | 2.12x | 2747 | STRONG 80/100 | HIGH 66/100 | Consider small entry |

**Same-run overlap:** PEPE/USD, CC/USD, AKT/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
