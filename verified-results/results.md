# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-24T21:02:10.322190+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/45486479490
**Source SHA:** 858c8bc8ec5d7641ddb39cacd8aca91719f855b1
**Previous ledger commit:** 7da091fee75ca132915de2e43ebac9e13d6a2fc4 (atomic ledger/results publication)
**Ledger generation:** 1625 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 5s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 628; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 610; valid market observations: 609; OHLC screened: 13.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | LUNA/USD | 4.59e-05 | 74.180 | 69.908 | +5.59% | +0.00% | 1.43x | 2.2 | 2026-11-24T21:02:05.084464+00:00 | Not calibrated | STRONG 72/100 | HIGH 60/100 | Watch | WATCH |
| 2 | XMR/USD | 499.47 | 64.749 | 69.459 | +2.77% | +0.13% | 0.46x | 9.8 | 2026-11-24T21:02:05.084464+00:00 | Not calibrated | MODERATE 52/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 3 | GBP/USD | 1.3108 | 58.065 | 58.750 | +0.58% | -0.01% | 0.94x | 0.6 | 2026-11-24T21:02:05.084464+00:00 | Not calibrated | WEAK 34/100 | HIGH 68/100 | Do nothing | WATCH |
| 4 | 2Z/USD | 0.01629 | 53.058 | 56.403 | +4.09% | +0.49% | 0.42x | 6.1 | 2026-11-24T21:02:05.084464+00:00 | Not calibrated | MODERATE 57/100 | VERY_HIGH 82/100 | Watch | WATCH |
| 5 | NIGHT/USD | 0.04847 | 45.230 | 42.117 | +0.66% | -0.08% | 1.35x | 6.2 | 2026-11-24T21:02:05.084464+00:00 | Not calibrated | WEAK 43/100 | HIGH 61/100 | Watch | WATCH |
| 6 | PEPE/USD | 3.454e-06 | 38.196 | 47.804 | +0.94% | -0.09% | 0.08x | 5.8 | 2026-11-24T21:02:05.084464+00:00 | Not calibrated | WEAK 24/100 | VERY_HIGH 76/100 | Do nothing | WATCH |
| 7 | AUD/USD | 0.66443 | 37.633 | 44.424 | +0.28% | +0.02% | 0.31x | 2.1 | 2026-11-24T21:02:05.084464+00:00 | Not calibrated | WEAK 39/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 8 | SKY/USD | 0.04057 | 33.719 | 33.086 | +0.45% | +0.42% | 0.85x | 7.4 | 2026-11-24T21:02:05.084464+00:00 | Not calibrated | MODERATE 47/100 | HIGH 67/100 | Watch | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | LUNA/USD | 69.908 | 4.59e-05 | +0.00% | 1.43x |
| 2 | XMR/USD | 69.459 | 499.47 | +0.13% | 0.46x |
| 3 | GBP/USD | 58.750 | 1.3108 | -0.01% | 0.94x |
| 4 | 2Z/USD | 56.403 | 0.01629 | +0.49% | 0.42x |
| 5 | PEPE/USD | 47.804 | 3.454e-06 | -0.09% | 0.08x |
| 6 | AUD/USD | 44.424 | 0.66443 | +0.02% | 0.31x |
| 7 | NIGHT/USD | 42.117 | 0.04847 | -0.08% | 1.35x |
| 8 | SKY/USD | 33.086 | 0.04057 | +0.42% | 0.85x |

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

- Persisted scans: 1625; predictions: 13938; observations: 984717.
- Matured sampled outcomes across 1/6/24/48h: 28514; gap abstentions: 22370. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 143 (sampled only; not a success-rate estimate).
- False positives / missed movers: NOT VERIFIED without eligible continuous outcome coverage.
- Baseline vs challenger: recorded as-of; unbiased held-out lift NOT MEASURED.
- Online Kraken /USD stablecoin-base pairs excluded: 18 (counted from this scan's online AssetPairs metadata, not inferred from price).
- Stablecoin base exclusions: BRL1, BUSD, DAI, EUR, EURC, EUROP, EURQ, EURR, EURT, FDUSD, FRAX, GUSD, PYUSD, QCAD, RLUSD, TGBP, TUSD, USD, USD1, USDC, USDD, USDE, USDG, USDQ, USDR, USDS, USDT, ZUSD.
- DEX: NOT USED; no DEX freshness gate.
- OHLC screening abstentions: 5; details in immutable scan JSON artifact.
- Storage: ledger and results published in one non-force Git commit and read back. Independent artifact recovery is NOT VERIFIED by this scan alone.
- Errors: none in successful committed scan; a failed workflow must not publish a SUCCESS report.

# Cryptoscanner — challenger and independent legacy-inspired WATCH

Paper only · risk is high or higher · 30%+ in 48h probability NOT CALIBRATED
Signal confidence 0–100 means setup strength only, NOT a win probability. Actions are research guidance; no trade authorization.

**Writer:** 45486479490 · **Generation:** 1625 · **Legacy run:** 45486479490
**Main quote time:** 2026-11-24T21:02:10.322190+00:00 · **Legacy report time:** 2026-11-24T21:03:26.270534+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | LUNA/USD | 4.59e-05 | 74.18 | +0.00% | 1.43x | STRONG 72/100 | HIGH 60/100 | Watch |
| 2 | XMR/USD | 499.47 | 64.75 | +0.13% | 0.46x | MODERATE 52/100 | VERY_HIGH 70/100 | Watch |
| 3 | GBP/USD | 1.3108 | 58.06 | -0.01% | 0.94x | WEAK 34/100 | HIGH 68/100 | Do nothing |
| 4 | 2Z/USD | 0.01629 | 53.06 | +0.49% | 0.42x | MODERATE 57/100 | VERY_HIGH 82/100 | Watch |
| 5 | NIGHT/USD | 0.04847 | 45.23 | -0.08% | 1.35x | WEAK 43/100 | HIGH 61/100 | Watch |
| 6 | PEPE/USD | 3.454e-06 | 38.20 | -0.09% | 0.08x | WEAK 24/100 | VERY_HIGH 76/100 | Do nothing |
| 7 | AUD/USD | 0.66443 | 37.63 | +0.02% | 0.31x | WEAK 39/100 | VERY_HIGH 70/100 | Watch |
| 8 | SKY/USD | 0.04057 | 33.72 | +0.42% | 0.85x | MODERATE 47/100 | HIGH 67/100 | Watch |

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
