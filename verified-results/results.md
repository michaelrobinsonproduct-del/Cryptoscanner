# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-24T20:27:23.492899+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/45480501715
**Source SHA:** 858c8bc8ec5d7641ddb39cacd8aca91719f855b1
**Previous ledger commit:** cdbee694b4e678c84d72590ebe491842345145f5 (atomic ledger/results publication)
**Ledger generation:** 1622 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 3s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 628; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 610; valid market observations: 609; OHLC screened: 12.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | XMR/USD | 500.78 | 72.539 | 72.259 | +3.04% | -0.02% | 1.04x | 8.0 | 2026-11-24T20:27:20.084386+00:00 | Not calibrated | MODERATE 46/100 | HIGH 68/100 | Watch | WATCH |
| 2 | PEPE/USD | 3.445e-06 | 61.227 | 45.936 | +0.67% | +0.06% | 3.38x | 5.8 | 2026-11-24T20:27:20.084386+00:00 | Not calibrated | STRONG 76/100 | HIGH 55/100 | Watch | WATCH |
| 3 | GBP/USD | 1.31126 | 59.108 | 59.264 | +0.61% | +0.01% | 0.98x | 0.1 | 2026-11-24T20:27:20.084386+00:00 | Not calibrated | MODERATE 50/100 | HIGH 62/100 | Watch | WATCH |
| 4 | NIGHT/USD | 0.04867 | 57.440 | 47.169 | +1.08% | +0.25% | 1.90x | 2.1 | 2026-11-24T20:27:20.084386+00:00 | Not calibrated | STRONG 74/100 | HIGH 55/100 | Watch | WATCH |
| 5 | AUD/USD | 0.66442 | 42.300 | 41.209 | +0.28% | +0.01% | 1.10x | 8.6 | 2026-11-24T20:27:20.084386+00:00 | Not calibrated | MODERATE 46/100 | HIGH 62/100 | Watch | WATCH |
| 6 | LUNA/USD | 4.539e-05 | 41.358 | 46.164 | +4.42% | -0.09% | 0.56x | 33.2 | 2026-11-24T20:27:20.084386+00:00 | Not calibrated | WEAK 16/100 | EXTREME 93/100 | Do nothing | WATCH |
| 7 | 2Z/USD | 0.01618 | 38.427 | 45.264 | +3.39% | -0.61% | 0.62x | 18.6 | 2026-11-24T20:27:20.084386+00:00 | Not calibrated | WEAK 19/100 | EXTREME 94/100 | Do nothing | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | XMR/USD | 72.259 | 500.78 | -0.02% | 1.04x |
| 2 | GBP/USD | 59.264 | 1.31126 | +0.01% | 0.98x |
| 3 | NIGHT/USD | 47.169 | 0.04867 | +0.25% | 1.90x |
| 4 | LUNA/USD | 46.164 | 4.539e-05 | -0.09% | 0.56x |
| 5 | PEPE/USD | 45.936 | 3.445e-06 | +0.06% | 3.38x |
| 6 | 2Z/USD | 45.264 | 0.01618 | -0.61% | 0.62x |
| 7 | AUD/USD | 41.209 | 0.66442 | +0.01% | 1.10x |

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

- Persisted scans: 1622; predictions: 13917; observations: 982890.
- Matured sampled outcomes across 1/6/24/48h: 28376; gap abstentions: 22370. Per-horizon counts require independent audit; do not infer held-out lift.
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

**Writer:** 45480501715 · **Generation:** 1622 · **Legacy run:** 45480501715
**Main quote time:** 2026-11-24T20:27:23.492899+00:00 · **Legacy report time:** 2026-11-24T20:28:22.365665+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | XMR/USD | 500.78 | 72.54 | -0.02% | 1.04x | MODERATE 46/100 | HIGH 68/100 | Watch |
| 2 | PEPE/USD ⭐ | 3.445e-06 | 61.23 | +0.06% | 3.38x | STRONG 86/100 | HIGH 55/100 | Watch |
| 3 | GBP/USD | 1.31126 | 59.11 | +0.01% | 0.98x | MODERATE 50/100 | HIGH 62/100 | Watch |
| 4 | NIGHT/USD ⭐ | 0.04867 | 57.44 | +0.25% | 1.90x | STRONG 84/100 | HIGH 55/100 | Consider small entry |
| 5 | AUD/USD | 0.66442 | 42.30 | +0.01% | 1.10x | MODERATE 46/100 | HIGH 62/100 | Watch |
| 6 | LUNA/USD | 4.539e-05 | 41.36 | -0.09% | 0.56x | WEAK 16/100 | EXTREME 93/100 | Do nothing |
| 7 | 2Z/USD | 0.01618 | 38.43 | -0.61% | 0.62x | WEAK 19/100 | EXTREME 94/100 | Do nothing |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | NIGHT/USD ⭐ | 0.04863 | 55.58 | +0.25% | 1.90x | 9317 | STRONG 83/100 | HIGH 55/100 | Consider small entry |
| 2 | PEPE/USD ⭐ | 3.449e-06 | 51.53 | +0.06% | 3.38x | 6612 | STRONG 81/100 | HIGH 55/100 | Watch |

**Same-run overlap:** PEPE/USD, NIGHT/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
