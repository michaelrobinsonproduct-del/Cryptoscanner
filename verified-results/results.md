# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-26T00:46:10.164522+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/45730891510
**Source SHA:** 858c8bc8ec5d7641ddb39cacd8aca91719f855b1
**Previous ledger commit:** 4c1bfbb33795d2bd6153695f543951430400c9a0 (atomic ledger/results publication)
**Ledger generation:** 1789 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 6s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 628; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 610; valid market observations: 609; OHLC screened: 24.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | VVV/USD | 30.138 | 81.253 | 61.957 | +3.23% | +0.86% | 2.87x | 31.3 | 2026-11-26T00:46:03.940983+00:00 | Not calibrated | STRONG 86/100 | HIGH 67/100 | Consider small entry | WATCH |
| 2 | XRP/USD | 0.93992 | 72.208 | 57.458 | +0.36% | -0.05% | 2.80x | 0.1 | 2026-11-26T00:46:03.940983+00:00 | Not calibrated | MODERATE 66/100 | HIGH 61/100 | Watch | WATCH |
| 3 | SOL/USD | 70.72 | 71.096 | 57.575 | +0.47% | -0.30% | 2.52x | 1.4 | 2026-11-26T00:46:03.940983+00:00 | Not calibrated | MODERATE 66/100 | HIGH 61/100 | Watch | WATCH |
| 4 | ADA/USD | 0.146498 | 70.562 | 56.312 | +0.50% | -0.15% | 5.50x | 4.4 | 2026-11-26T00:46:03.940983+00:00 | Not calibrated | MODERATE 65/100 | HIGH 61/100 | Watch | WATCH |
| 5 | XDG/USD | 0.05636 | 66.568 | 53.039 | +0.72% | -0.29% | 7.11x | 3.5 | 2026-11-26T00:46:03.940983+00:00 | Not calibrated | MODERATE 63/100 | HIGH 61/100 | Watch | WATCH |
| 6 | LINK/USD | 9.09861 | 65.456 | 52.855 | +0.60% | -0.19% | 2.35x | 0.7 | 2026-11-26T00:46:03.940983+00:00 | Not calibrated | MODERATE 63/100 | HIGH 61/100 | Watch | WATCH |
| 7 | LTC/USD | 42.85 | 55.381 | 56.128 | +0.33% | -0.07% | 0.96x | 2.3 | 2026-11-26T00:46:03.940983+00:00 | Not calibrated | WEAK 33/100 | HIGH 68/100 | Do nothing | WATCH |
| 8 | BCH/USD | 206.86 | 51.955 | 38.713 | +0.62% | -0.35% | 2.89x | 2.4 | 2026-11-26T00:46:03.940983+00:00 | Not calibrated | MODERATE 56/100 | HIGH 66/100 | Watch | WATCH |
| 9 | TAO/USD | 183.0522 | 51.498 | 58.002 | +0.80% | +0.03% | 0.33x | 5.2 | 2026-11-26T00:46:03.940983+00:00 | Not calibrated | MODERATE 46/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 10 | BNB/USD | 554.54 | 50.076 | 38.312 | +0.27% | -0.21% | 2.28x | 1.8 | 2026-11-26T00:46:03.940983+00:00 | Not calibrated | MODERATE 55/100 | HIGH 61/100 | Watch | WATCH |
| 11 | DOT/USD | 0.6621 | 45.607 | 36.120 | +0.58% | -0.08% | 1.99x | 1.5 | 2026-11-26T00:46:03.940983+00:00 | Not calibrated | WEAK 43/100 | HIGH 66/100 | Watch | WATCH |
| 12 | XLM/USD | 0.128718 | 41.095 | 48.284 | +0.70% | -0.43% | 0.50x | 3.0 | 2026-11-26T00:46:03.940983+00:00 | Not calibrated | WEAK 26/100 | VERY_HIGH 76/100 | Do nothing | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | VVV/USD | 61.957 | 30.138 | +0.86% | 2.87x |
| 2 | TAO/USD | 58.002 | 183.0522 | +0.03% | 0.33x |
| 3 | SOL/USD | 57.575 | 70.72 | -0.30% | 2.52x |
| 4 | XRP/USD | 57.458 | 0.93992 | -0.05% | 2.80x |
| 5 | ADA/USD | 56.312 | 0.146498 | -0.15% | 5.50x |
| 6 | LTC/USD | 56.128 | 42.85 | -0.07% | 0.96x |
| 7 | XDG/USD | 53.039 | 0.05636 | -0.29% | 7.11x |
| 8 | LINK/USD | 52.855 | 9.09861 | -0.19% | 2.35x |
| 9 | XLM/USD | 48.284 | 0.128718 | -0.43% | 0.50x |
| 10 | BCH/USD | 38.713 | 206.86 | -0.35% | 2.89x |
| 11 | BNB/USD | 38.312 | 554.54 | -0.21% | 2.28x |
| 12 | DOT/USD | 36.120 | 0.6621 | -0.08% | 1.99x |

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

- Persisted scans: 1789; predictions: 15203; observations: 1084545.
- Matured sampled outcomes across 1/6/24/48h: 33056; gap abstentions: 23534. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 146 (sampled only; not a success-rate estimate).
- False positives / missed movers: NOT VERIFIED without eligible continuous outcome coverage.
- Baseline vs challenger: recorded as-of; unbiased held-out lift NOT MEASURED.
- Online Kraken /USD stablecoin-base pairs excluded: 18 (counted from this scan's online AssetPairs metadata, not inferred from price).
- Stablecoin base exclusions: BRL1, BUSD, DAI, EUR, EURC, EUROP, EURQ, EURR, EURT, FDUSD, FRAX, GUSD, PYUSD, QCAD, RLUSD, TGBP, TUSD, USD, USD1, USDC, USDD, USDE, USDG, USDQ, USDR, USDS, USDT, ZUSD.
- DEX: NOT USED; no DEX freshness gate.
- OHLC screening abstentions: 10; details in immutable scan JSON artifact.
- Storage: ledger and results published in one non-force Git commit and read back. Independent artifact recovery is NOT VERIFIED by this scan alone.
- Errors: none in successful committed scan; a failed workflow must not publish a SUCCESS report.

# Cryptoscanner — challenger and independent legacy-inspired WATCH

Paper only · risk is high or higher · 30%+ in 48h probability NOT CALIBRATED
Signal confidence 0–100 means setup strength only, NOT a win probability. Actions are research guidance; no trade authorization.

**Writer:** 45730891510 · **Generation:** 1789 · **Legacy run:** 45730891510
**Main quote time:** 2026-11-26T00:46:10.164522+00:00 · **Legacy report time:** 2026-11-26T00:47:26.490371+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | VVV/USD ⭐ | 30.138 | 81.25 | +0.86% | 2.87x | STRONG 96/100 | HIGH 67/100 | Consider small entry |
| 2 | XRP/USD | 0.93992 | 72.21 | -0.05% | 2.80x | MODERATE 66/100 | HIGH 61/100 | Watch |
| 3 | SOL/USD | 70.72 | 71.10 | -0.30% | 2.52x | MODERATE 66/100 | HIGH 61/100 | Watch |
| 4 | ADA/USD | 0.146498 | 70.56 | -0.15% | 5.50x | MODERATE 65/100 | HIGH 61/100 | Watch |
| 5 | XDG/USD | 0.05636 | 66.57 | -0.29% | 7.11x | MODERATE 63/100 | HIGH 61/100 | Watch |
| 6 | LINK/USD | 9.09861 | 65.46 | -0.19% | 2.35x | MODERATE 63/100 | HIGH 61/100 | Watch |
| 7 | LTC/USD | 42.85 | 55.38 | -0.07% | 0.96x | WEAK 33/100 | HIGH 68/100 | Do nothing |
| 8 | BCH/USD | 206.86 | 51.95 | -0.35% | 2.89x | MODERATE 56/100 | HIGH 66/100 | Watch |
| 9 | TAO/USD | 183.0522 | 51.50 | +0.03% | 0.33x | MODERATE 46/100 | VERY_HIGH 70/100 | Watch |
| 10 | BNB/USD | 554.54 | 50.08 | -0.21% | 2.28x | MODERATE 55/100 | HIGH 61/100 | Watch |
| 11 | DOT/USD | 0.6621 | 45.61 | -0.08% | 1.99x | WEAK 43/100 | HIGH 66/100 | Watch |
| 12 | XLM/USD | 0.128718 | 41.10 | -0.43% | 0.50x | WEAK 26/100 | VERY_HIGH 76/100 | Do nothing |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | VVV/USD ⭐ | 30.119 | 85.05 | +0.86% | 2.87x | 16845 | STRONG 100/100 | HIGH 61/100 | Consider small entry |
| 2 | PIEVERSE/USD | 3.65 | 70.13 | +2.81% | 8.92x | 1804 | STRONG 85/100 | HIGH 66/100 | Consider small entry |

**Same-run overlap:** VVV/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
