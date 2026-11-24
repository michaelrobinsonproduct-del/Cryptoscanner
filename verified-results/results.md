# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-24T10:11:49.923960+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/45372064631
**Source SHA:** 858c8bc8ec5d7641ddb39cacd8aca91719f855b1
**Previous ledger commit:** 22d369a66f0e6fa4dd9d54aeb9e9fe321ca5d712 (atomic ledger/results publication)
**Ledger generation:** 1560 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 7s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 628; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 610; valid market observations: 609; OHLC screened: 24.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | VVV/USD | 25.28 | 81.467 | 74.265 | +3.40% | +0.65% | 1.40x | 9.1 | 2026-11-24T10:11:42.792633+00:00 | Not calibrated | STRONG 86/100 | HIGH 55/100 | Watch | WATCH |
| 2 | MON/USD | 0.01239 | 76.389 | 78.234 | +7.55% | -0.64% | 1.14x | 16.1 | 2026-11-24T10:11:42.792633+00:00 | Not calibrated | WEAK 43/100 | VERY_HIGH 74/100 | Watch | WATCH |
| 3 | XMR/USD | 496.08 | 72.723 | 66.969 | +2.07% | -0.06% | 1.60x | 5.0 | 2026-11-24T10:11:42.792633+00:00 | Not calibrated | MODERATE 56/100 | HIGH 61/100 | Watch | WATCH |
| 4 | LUNA/USD | 4.697e-05 | 65.265 | 66.474 | +8.05% | +0.58% | 0.59x | 21.3 | 2026-11-24T10:11:42.792633+00:00 | Not calibrated | MODERATE 53/100 | EXTREME 87/100 | Do nothing | WATCH |
| 5 | PEPE/USD | 3.486e-06 | 56.573 | 60.764 | +1.87% | +0.17% | 0.49x | 5.7 | 2026-11-24T10:11:42.792633+00:00 | Not calibrated | MODERATE 48/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 6 | GBP/USD | 1.30676 | 49.806 | 56.847 | +0.27% | +0.02% | 0.29x | 0.1 | 2026-11-24T10:11:42.792633+00:00 | Not calibrated | MODERATE 45/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 7 | ATOM/USD | 1.2893 | 47.049 | 30.922 | +0.55% | +0.23% | 3.68x | 12.4 | 2026-11-24T10:11:42.792633+00:00 | Not calibrated | STRONG 74/100 | HIGH 66/100 | Watch | WATCH |
| 8 | 2Z/USD | 0.01615 | 42.982 | 40.697 | +3.19% | -0.55% | 1.51x | 24.8 | 2026-11-24T10:11:42.792633+00:00 | Not calibrated | WEAK 31/100 | EXTREME 85/100 | Do nothing | WATCH |
| 9 | BAT/USD | 0.07824 | 39.424 | 39.532 | +1.39% | -0.09% | 1.03x | 5.1 | 2026-11-24T10:11:42.792633+00:00 | Not calibrated | WEAK 30/100 | VERY_HIGH 73/100 | Do nothing | WATCH |
| 10 | INX/USD | 0.003999 | 29.455 | 39.844 | +2.59% | -0.67% | 0.30x | 20.0 | 2026-11-24T10:11:42.792633+00:00 | Not calibrated | WEAK 10/100 | EXTREME 93/100 | Do nothing | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | MON/USD | 78.234 | 0.01239 | -0.64% | 1.14x |
| 2 | VVV/USD | 74.265 | 25.28 | +0.65% | 1.40x |
| 3 | XMR/USD | 66.969 | 496.08 | -0.06% | 1.60x |
| 4 | LUNA/USD | 66.474 | 4.697e-05 | +0.58% | 0.59x |
| 5 | PEPE/USD | 60.764 | 3.486e-06 | +0.17% | 0.49x |
| 6 | GBP/USD | 56.847 | 1.30676 | +0.02% | 0.29x |
| 7 | 2Z/USD | 40.697 | 0.01615 | -0.55% | 1.51x |
| 8 | INX/USD | 39.844 | 0.003999 | -0.67% | 0.30x |
| 9 | BAT/USD | 39.532 | 0.07824 | -0.09% | 1.03x |
| 10 | ATOM/USD | 30.922 | 1.2893 | +0.23% | 3.68x |

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

- Persisted scans: 1560; predictions: 13437; observations: 945138.
- Matured sampled outcomes across 1/6/24/48h: 25671; gap abstentions: 22370. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 142 (sampled only; not a success-rate estimate).
- False positives / missed movers: NOT VERIFIED without eligible continuous outcome coverage.
- Baseline vs challenger: recorded as-of; unbiased held-out lift NOT MEASURED.
- Online Kraken /USD stablecoin-base pairs excluded: 18 (counted from this scan's online AssetPairs metadata, not inferred from price).
- Stablecoin base exclusions: BRL1, BUSD, DAI, EUR, EURC, EUROP, EURQ, EURR, EURT, FDUSD, FRAX, GUSD, PYUSD, QCAD, RLUSD, TGBP, TUSD, USD, USD1, USDC, USDD, USDE, USDG, USDQ, USDR, USDS, USDT, ZUSD.
- DEX: NOT USED; no DEX freshness gate.
- OHLC screening abstentions: 14; details in immutable scan JSON artifact.
- Storage: ledger and results published in one non-force Git commit and read back. Independent artifact recovery is NOT VERIFIED by this scan alone.
- Errors: none in successful committed scan; a failed workflow must not publish a SUCCESS report.

# Cryptoscanner — challenger and independent legacy-inspired WATCH

Paper only · risk is high or higher · 30%+ in 48h probability NOT CALIBRATED
Signal confidence 0–100 means setup strength only, NOT a win probability. Actions are research guidance; no trade authorization.

**Writer:** 45372064631 · **Generation:** 1560 · **Legacy run:** 45372064631
**Main quote time:** 2026-11-24T10:11:49.923960+00:00 · **Legacy report time:** 2026-11-24T10:12:56.241219+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | VVV/USD ⭐ | 25.28 | 81.47 | +0.65% | 1.40x | STRONG 96/100 | HIGH 55/100 | Watch |
| 2 | MON/USD | 0.01239 | 76.39 | -0.64% | 1.14x | WEAK 43/100 | VERY_HIGH 74/100 | Watch |
| 3 | XMR/USD | 496.08 | 72.72 | -0.06% | 1.60x | MODERATE 56/100 | HIGH 61/100 | Watch |
| 4 | LUNA/USD | 4.697e-05 | 65.27 | +0.58% | 0.59x | MODERATE 53/100 | EXTREME 87/100 | Do nothing |
| 5 | PEPE/USD | 3.486e-06 | 56.57 | +0.17% | 0.49x | MODERATE 48/100 | VERY_HIGH 70/100 | Watch |
| 6 | GBP/USD | 1.30676 | 49.81 | +0.02% | 0.29x | MODERATE 45/100 | VERY_HIGH 70/100 | Watch |
| 7 | ATOM/USD | 1.2893 | 47.05 | +0.23% | 3.68x | STRONG 74/100 | HIGH 66/100 | Watch |
| 8 | 2Z/USD | 0.01615 | 42.98 | -0.55% | 1.51x | WEAK 31/100 | EXTREME 85/100 | Do nothing |
| 9 | BAT/USD | 0.07824 | 39.42 | -0.09% | 1.03x | WEAK 30/100 | VERY_HIGH 73/100 | Do nothing |
| 10 | INX/USD | 0.003999 | 29.46 | -0.67% | 0.30x | WEAK 10/100 | EXTREME 93/100 | Do nothing |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | VVV/USD ⭐ | 25.28 | 81.37 | +0.65% | 1.40x | 13423 | STRONG 96/100 | HIGH 55/100 | Watch |

**Same-run overlap:** VVV/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
