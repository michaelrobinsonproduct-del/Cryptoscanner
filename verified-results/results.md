# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-24T13:11:43.245020+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/45400545817
**Source SHA:** 858c8bc8ec5d7641ddb39cacd8aca91719f855b1
**Previous ledger commit:** f585d7c294cc8d37153f91c9e1bf0f9c6c667e54 (atomic ledger/results publication)
**Ledger generation:** 1578 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 4s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 628; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 610; valid market observations: 609; OHLC screened: 12.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | VVV/USD | 25.646 | 87.875 | 80.885 | +4.90% | -0.90% | 2.15x | 16.8 | 2026-11-24T13:11:38.849340+00:00 | Not calibrated | MODERATE 69/100 | HIGH 67/100 | Watch | WATCH |
| 2 | XMR/USD | 497.26 | 80.360 | 66.662 | +2.31% | -0.26% | 2.84x | 9.1 | 2026-11-24T13:11:38.849340+00:00 | Not calibrated | STRONG 70/100 | HIGH 61/100 | Watch | WATCH |
| 3 | GBP/USD | 1.30983 | 73.634 | 58.458 | +0.50% | +0.04% | 9.02x | 0.2 | 2026-11-24T13:11:38.849340+00:00 | Not calibrated | STRONG 82/100 | HIGH 55/100 | Watch | WATCH |
| 4 | MON/USD | 0.01209 | 61.530 | 72.383 | +4.95% | -1.46% | 0.65x | 8.3 | 2026-11-24T13:11:38.849340+00:00 | Not calibrated | WEAK 36/100 | VERY_HIGH 80/100 | Do nothing | WATCH |
| 5 | NIGHT/USD | 0.04888 | 46.576 | 50.752 | +1.52% | +0.04% | 0.56x | 16.4 | 2026-11-24T13:11:38.849340+00:00 | Not calibrated | WEAK 38/100 | VERY_HIGH 76/100 | Watch | WATCH |
| 6 | 2Z/USD | 0.0158 | 22.919 | 31.111 | +0.96% | -0.88% | 0.62x | 12.7 | 2026-11-24T13:11:38.849340+00:00 | Not calibrated | WEAK 11/100 | EXTREME 94/100 | Do nothing | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | VVV/USD | 80.885 | 25.646 | -0.90% | 2.15x |
| 2 | MON/USD | 72.383 | 0.01209 | -1.46% | 0.65x |
| 3 | XMR/USD | 66.662 | 497.26 | -0.26% | 2.84x |
| 4 | GBP/USD | 58.458 | 1.30983 | +0.04% | 9.02x |
| 5 | NIGHT/USD | 50.752 | 0.04888 | +0.04% | 0.56x |
| 6 | 2Z/USD | 31.111 | 0.0158 | -0.88% | 0.62x |

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

- Persisted scans: 1578; predictions: 13612; observations: 956100.
- Matured sampled outcomes across 1/6/24/48h: 26534; gap abstentions: 22370. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 143 (sampled only; not a success-rate estimate).
- False positives / missed movers: NOT VERIFIED without eligible continuous outcome coverage.
- Baseline vs challenger: recorded as-of; unbiased held-out lift NOT MEASURED.
- Online Kraken /USD stablecoin-base pairs excluded: 18 (counted from this scan's online AssetPairs metadata, not inferred from price).
- Stablecoin base exclusions: BRL1, BUSD, DAI, EUR, EURC, EUROP, EURQ, EURR, EURT, FDUSD, FRAX, GUSD, PYUSD, QCAD, RLUSD, TGBP, TUSD, USD, USD1, USDC, USDD, USDE, USDG, USDQ, USDR, USDS, USDT, ZUSD.
- DEX: NOT USED; no DEX freshness gate.
- OHLC screening abstentions: 6; details in immutable scan JSON artifact.
- Storage: ledger and results published in one non-force Git commit and read back. Independent artifact recovery is NOT VERIFIED by this scan alone.
- Errors: none in successful committed scan; a failed workflow must not publish a SUCCESS report.

# Cryptoscanner — challenger and independent legacy-inspired WATCH

Paper only · risk is high or higher · 30%+ in 48h probability NOT CALIBRATED
Signal confidence 0–100 means setup strength only, NOT a win probability. Actions are research guidance; no trade authorization.

**Writer:** 45400545817 · **Generation:** 1578 · **Legacy run:** 45400545817
**Main quote time:** 2026-11-24T13:11:43.245020+00:00 · **Legacy report time:** 2026-11-24T13:12:41.360333+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | VVV/USD | 25.646 | 87.88 | -0.90% | 2.15x | MODERATE 69/100 | HIGH 67/100 | Watch |
| 2 | XMR/USD | 497.26 | 80.36 | -0.26% | 2.84x | STRONG 70/100 | HIGH 61/100 | Watch |
| 3 | GBP/USD | 1.30983 | 73.63 | +0.04% | 9.02x | STRONG 82/100 | HIGH 55/100 | Watch |
| 4 | MON/USD | 0.01209 | 61.53 | -1.46% | 0.65x | WEAK 36/100 | VERY_HIGH 80/100 | Do nothing |
| 5 | NIGHT/USD | 0.04888 | 46.58 | +0.04% | 0.56x | WEAK 38/100 | VERY_HIGH 76/100 | Watch |
| 6 | 2Z/USD | 0.0158 | 22.92 | -0.88% | 0.62x | WEAK 11/100 | EXTREME 94/100 | Do nothing |

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
