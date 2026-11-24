# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-24T23:52:18.556860+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/45513171899
**Source SHA:** 858c8bc8ec5d7641ddb39cacd8aca91719f855b1
**Previous ledger commit:** b6f44cd12f5d519674e7b2223b676bdbed3f1e7b (atomic ledger/results publication)
**Ledger generation:** 1642 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 4s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 628; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 610; valid market observations: 609; OHLC screened: 12.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | XMR/USD | 507.71 | 75.682 | 79.934 | +4.46% | -0.05% | 0.60x | 12.6 | 2026-11-24T23:52:14.429365+00:00 | Not calibrated | WEAK 38/100 | VERY_HIGH 82/100 | Watch | WATCH |
| 2 | WINGS/USD | 0.002214 | 69.482 | 74.244 | +6.85% | -0.27% | 0.66x | 4.5 | 2026-11-24T23:52:14.429365+00:00 | Not calibrated | WEAK 40/100 | EXTREME 88/100 | Do nothing | WATCH |
| 3 | LUNA/USD | 4.584e-05 | 64.174 | 50.161 | +5.45% | +0.17% | 2.31x | 39.4 | 2026-11-24T23:52:14.429365+00:00 | Not calibrated | MODERATE 62/100 | VERY_HIGH 72/100 | Watch | WATCH |
| 4 | GBP/USD | 1.31078 | 59.814 | 58.892 | +0.58% | +0.01% | 1.08x | 0.3 | 2026-11-24T23:52:14.429365+00:00 | Not calibrated | MODERATE 55/100 | HIGH 62/100 | Watch | WATCH |
| 5 | NIGHT/USD | 0.04885 | 51.434 | 48.090 | +1.45% | +0.02% | 1.32x | 2.0 | 2026-11-24T23:52:14.429365+00:00 | Not calibrated | MODERATE 61/100 | HIGH 55/100 | Watch | WATCH |
| 6 | VVV/USD | 24.663 | 51.172 | 58.109 | +0.88% | +0.20% | 0.20x | 6.1 | 2026-11-24T23:52:14.429365+00:00 | Not calibrated | MODERATE 56/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 7 | PEPE/USD | 3.45e-06 | 48.009 | 48.350 | +0.82% | +0.26% | 0.84x | 5.8 | 2026-11-24T23:52:14.429365+00:00 | Not calibrated | MODERATE 54/100 | HIGH 62/100 | Watch | WATCH |
| 8 | SKY/USD | 0.04094 | 46.563 | 40.909 | +1.36% | -0.20% | 1.66x | 4.9 | 2026-11-24T23:52:14.429365+00:00 | Not calibrated | WEAK 43/100 | HIGH 66/100 | Watch | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | XMR/USD | 79.934 | 507.71 | -0.05% | 0.60x |
| 2 | WINGS/USD | 74.244 | 0.002214 | -0.27% | 0.66x |
| 3 | GBP/USD | 58.892 | 1.31078 | +0.01% | 1.08x |
| 4 | VVV/USD | 58.109 | 24.663 | +0.20% | 0.20x |
| 5 | LUNA/USD | 50.161 | 4.584e-05 | +0.17% | 2.31x |
| 6 | PEPE/USD | 48.350 | 3.45e-06 | +0.26% | 0.84x |
| 7 | NIGHT/USD | 48.090 | 0.04885 | +0.02% | 1.32x |
| 8 | SKY/USD | 40.909 | 0.04094 | -0.20% | 1.66x |

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

- Persisted scans: 1642; predictions: 14059; observations: 995069.
- Matured sampled outcomes across 1/6/24/48h: 29144; gap abstentions: 22370. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 143 (sampled only; not a success-rate estimate).
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

**Writer:** 45513171899 · **Generation:** 1642 · **Legacy run:** 45513171899
**Main quote time:** 2026-11-24T23:52:18.556860+00:00 · **Legacy report time:** 2026-11-24T23:53:27.932007+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | XMR/USD | 507.71 | 75.68 | -0.05% | 0.60x | WEAK 38/100 | VERY_HIGH 82/100 | Watch |
| 2 | WINGS/USD | 0.002214 | 69.48 | -0.27% | 0.66x | WEAK 40/100 | EXTREME 88/100 | Do nothing |
| 3 | LUNA/USD ⭐ | 4.584e-05 | 64.17 | +0.17% | 2.31x | STRONG 72/100 | VERY_HIGH 72/100 | Watch |
| 4 | GBP/USD | 1.31078 | 59.81 | +0.01% | 1.08x | MODERATE 55/100 | HIGH 62/100 | Watch |
| 5 | NIGHT/USD | 0.04885 | 51.43 | +0.02% | 1.32x | MODERATE 61/100 | HIGH 55/100 | Watch |
| 6 | VVV/USD | 24.663 | 51.17 | +0.20% | 0.20x | MODERATE 56/100 | VERY_HIGH 70/100 | Watch |
| 7 | PEPE/USD | 3.45e-06 | 48.01 | +0.26% | 0.84x | MODERATE 54/100 | HIGH 62/100 | Watch |
| 8 | SKY/USD | 0.04094 | 46.56 | -0.20% | 1.66x | WEAK 43/100 | HIGH 66/100 | Watch |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | LUNA/USD ⭐ | 4.584e-05 | 70.68 | +0.17% | 2.31x | 1907 | STRONG 80/100 | VERY_HIGH 72/100 | Watch |

**Same-run overlap:** LUNA/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
