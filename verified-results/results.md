# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-25T05:27:30.740830+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/45553367069
**Source SHA:** 858c8bc8ec5d7641ddb39cacd8aca91719f855b1
**Previous ledger commit:** e2f9e2324e97b6dc7f109226d652d11337e5a4f5 (atomic ledger/results publication)
**Ledger generation:** 1675 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 6s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 628; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 610; valid market observations: 609; OHLC screened: 22.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | DRV/USD | 0.33466 | 72.230 | 76.020 | +6.48% | +0.64% | 0.30x | 12.0 | 2026-11-25T05:27:24.792808+00:00 | Not calibrated | MODERATE 61/100 | VERY_HIGH 76/100 | Watch | WATCH |
| 2 | MON/USD | 0.00985 | 63.520 | 66.068 | +4.01% | +0.20% | 0.64x | 20.3 | 2026-11-25T05:27:24.792808+00:00 | Not calibrated | MODERATE 52/100 | VERY_HIGH 82/100 | Watch | WATCH |
| 3 | VVV/USD | 25.062 | 61.795 | 66.158 | +2.14% | -0.24% | 0.68x | 7.6 | 2026-11-25T05:27:24.792808+00:00 | Not calibrated | WEAK 36/100 | VERY_HIGH 76/100 | Watch | WATCH |
| 4 | XMR/USD | 513.73 | 51.283 | 55.935 | +0.81% | -0.03% | 0.55x | 6.4 | 2026-11-25T05:27:24.792808+00:00 | Not calibrated | WEAK 31/100 | VERY_HIGH 76/100 | Do nothing | WATCH |
| 5 | BLUR/USD | 0.00876 | 36.872 | 31.420 | +1.74% | +1.51% | 0.79x | 22.9 | 2026-11-25T05:27:24.792808+00:00 | Not calibrated | WEAK 38/100 | EXTREME 86/100 | Do nothing | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | DRV/USD | 76.020 | 0.33466 | +0.64% | 0.30x |
| 2 | VVV/USD | 66.158 | 25.062 | -0.24% | 0.68x |
| 3 | MON/USD | 66.068 | 0.00985 | +0.20% | 0.64x |
| 4 | XMR/USD | 55.935 | 513.73 | -0.03% | 0.55x |
| 5 | BLUR/USD | 31.420 | 0.00876 | +1.51% | 0.79x |

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

- Persisted scans: 1675; predictions: 14222; observations: 1015166.
- Matured sampled outcomes across 1/6/24/48h: 30185; gap abstentions: 22370. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 146 (sampled only; not a success-rate estimate).
- False positives / missed movers: NOT VERIFIED without eligible continuous outcome coverage.
- Baseline vs challenger: recorded as-of; unbiased held-out lift NOT MEASURED.
- Online Kraken /USD stablecoin-base pairs excluded: 18 (counted from this scan's online AssetPairs metadata, not inferred from price).
- Stablecoin base exclusions: BRL1, BUSD, DAI, EUR, EURC, EUROP, EURQ, EURR, EURT, FDUSD, FRAX, GUSD, PYUSD, QCAD, RLUSD, TGBP, TUSD, USD, USD1, USDC, USDD, USDE, USDG, USDQ, USDR, USDS, USDT, ZUSD.
- DEX: NOT USED; no DEX freshness gate.
- OHLC screening abstentions: 17; details in immutable scan JSON artifact.
- Storage: ledger and results published in one non-force Git commit and read back. Independent artifact recovery is NOT VERIFIED by this scan alone.
- Errors: none in successful committed scan; a failed workflow must not publish a SUCCESS report.

# Cryptoscanner — challenger and independent legacy-inspired WATCH

Paper only · risk is high or higher · 30%+ in 48h probability NOT CALIBRATED
Signal confidence 0–100 means setup strength only, NOT a win probability. Actions are research guidance; no trade authorization.

**Writer:** 45553367069 · **Generation:** 1675 · **Legacy run:** 45553367069
**Main quote time:** 2026-11-25T05:27:30.740830+00:00 · **Legacy report time:** 2026-11-25T05:28:44.199394+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | DRV/USD | 0.33466 | 72.23 | +0.64% | 0.30x | MODERATE 61/100 | VERY_HIGH 76/100 | Watch |
| 2 | MON/USD | 0.00985 | 63.52 | +0.20% | 0.64x | MODERATE 52/100 | VERY_HIGH 82/100 | Watch |
| 3 | VVV/USD | 25.062 | 61.80 | -0.24% | 0.68x | WEAK 36/100 | VERY_HIGH 76/100 | Watch |
| 4 | XMR/USD | 513.73 | 51.28 | -0.03% | 0.55x | WEAK 31/100 | VERY_HIGH 76/100 | Do nothing |
| 5 | BLUR/USD | 0.00876 | 36.87 | +1.51% | 0.79x | WEAK 38/100 | EXTREME 86/100 | Do nothing |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | BLESS/USD | 0.018075 | 74.37 | +3.34% | 2.75x | 3468 | STRONG 77/100 | EXTREME 87/100 | Do nothing |

**Same-run overlap:** None
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
