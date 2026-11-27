# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-27T00:21:17.101715+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/45916056494
**Source SHA:** 858c8bc8ec5d7641ddb39cacd8aca91719f855b1
**Previous ledger commit:** 10a5b3f377923f48abce5630a5314766cea0bbba (atomic ledger/results publication)
**Ledger generation:** 1933 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 6s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 628; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 610; valid market observations: 601; OHLC screened: 22.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | LINK/USD | 9.3 | 72.101 | 56.621 | +0.34% | +0.10% | 14.14x | 1.5 | 2026-11-27T00:21:11.057097+00:00 | Not calibrated | STRONG 81/100 | HIGH 55/100 | Watch | WATCH |
| 2 | ZEC/USD | 688.2 | 62.854 | 59.969 | +0.96% | +0.06% | 1.26x | 3.5 | 2026-11-27T00:21:11.057097+00:00 | Not calibrated | MODERATE 56/100 | HIGH 55/100 | Watch | WATCH |
| 3 | LTC/USD | 43.87 | 61.218 | 55.941 | +0.30% | +0.23% | 1.41x | 2.3 | 2026-11-27T00:21:11.057097+00:00 | Not calibrated | STRONG 76/100 | HIGH 55/100 | Watch | WATCH |
| 4 | HYPE/USD | 62.47 | 57.849 | 57.012 | +0.40% | +0.06% | 1.05x | 1.6 | 2026-11-27T00:21:11.057097+00:00 | Not calibrated | MODERATE 54/100 | HIGH 62/100 | Watch | WATCH |
| 5 | VVV/USD | 26.412 | 55.072 | 57.146 | +0.87% | +0.25% | 0.67x | 8.0 | 2026-11-27T00:21:11.057097+00:00 | Not calibrated | MODERATE 58/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 6 | ATOM/USD | 1.2244 | 46.385 | 29.910 | +0.60% | +0.30% | 3.07x | 13.9 | 2026-11-27T00:21:11.057097+00:00 | Not calibrated | STRONG 73/100 | HIGH 66/100 | Watch | WATCH |
| 7 | PEPE/USD | 3.488e-06 | 38.611 | 40.045 | +0.29% | +0.09% | 0.81x | 2.9 | 2026-11-27T00:21:11.057097+00:00 | Not calibrated | WEAK 39/100 | HIGH 62/100 | Watch | WATCH |
| 8 | CRV/USD | 0.17493 | 31.000 | 35.111 | +0.47% | +0.30% | 0.44x | 8.0 | 2026-11-27T00:21:11.057097+00:00 | Not calibrated | MODERATE 45/100 | VERY_HIGH 75/100 | Watch | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | ZEC/USD | 59.969 | 688.2 | +0.06% | 1.26x |
| 2 | VVV/USD | 57.146 | 26.412 | +0.25% | 0.67x |
| 3 | HYPE/USD | 57.012 | 62.47 | +0.06% | 1.05x |
| 4 | LINK/USD | 56.621 | 9.3 | +0.10% | 14.14x |
| 5 | LTC/USD | 55.941 | 43.87 | +0.23% | 1.41x |
| 6 | PEPE/USD | 40.045 | 3.488e-06 | +0.09% | 0.81x |
| 7 | CRV/USD | 35.111 | 0.17493 | +0.30% | 0.44x |
| 8 | ATOM/USD | 29.910 | 1.2244 | +0.30% | 3.07x |

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

- Persisted scans: 1933; predictions: 16901; observations: 1170818.
- Matured sampled outcomes across 1/6/24/48h: 37004; gap abstentions: 25393. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 149 (sampled only; not a success-rate estimate).
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

**Writer:** 45916056494 · **Generation:** 1933 · **Legacy run:** 45916056494
**Main quote time:** 2026-11-27T00:21:17.101715+00:00 · **Legacy report time:** 2026-11-27T00:22:09.445451+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | LINK/USD ⭐ | 9.3 | 72.10 | +0.10% | 14.14x | STRONG 91/100 | HIGH 55/100 | Watch |
| 2 | ZEC/USD ⭐ | 688.2 | 62.85 | +0.06% | 1.26x | MODERATE 66/100 | HIGH 55/100 | Watch |
| 3 | LTC/USD ⭐ | 43.87 | 61.22 | +0.23% | 1.41x | STRONG 86/100 | HIGH 55/100 | Watch |
| 4 | HYPE/USD ⭐ | 62.47 | 57.85 | +0.06% | 1.05x | MODERATE 64/100 | HIGH 62/100 | Watch |
| 5 | VVV/USD | 26.412 | 55.07 | +0.25% | 0.67x | MODERATE 58/100 | VERY_HIGH 70/100 | Watch |
| 6 | ATOM/USD | 1.2244 | 46.38 | +0.30% | 3.07x | STRONG 73/100 | HIGH 66/100 | Watch |
| 7 | PEPE/USD | 3.488e-06 | 38.61 | +0.09% | 0.81x | WEAK 39/100 | HIGH 62/100 | Watch |
| 8 | CRV/USD | 0.17493 | 31.00 | +0.30% | 0.44x | MODERATE 45/100 | VERY_HIGH 75/100 | Watch |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | LINK/USD ⭐ | 9.3 | 56.51 | +0.10% | 14.14x | 6970 | STRONG 83/100 | HIGH 55/100 | Watch |
| 2 | ZEC/USD ⭐ | 688.5 | 54.80 | +0.06% | 1.26x | 33093 | MODERATE 62/100 | HIGH 55/100 | Watch |
| 3 | LTC/USD ⭐ | 43.89 | 53.90 | +0.23% | 1.41x | 14143 | STRONG 82/100 | HIGH 55/100 | Watch |
| 4 | HYPE/USD ⭐ | 62.51 | 51.60 | +0.06% | 1.05x | 12873 | MODERATE 61/100 | HIGH 62/100 | Watch |
| 5 | XMR/USD | 457.54 | 41.11 | +0.36% | 1.37x | 18045 | MODERATE 56/100 | HIGH 67/100 | Watch |

**Same-run overlap:** LINK/USD, ZEC/USD, LTC/USD, HYPE/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
