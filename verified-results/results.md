# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-18T00:25:06.774059+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/44207570703
**Source SHA:** 394c17eeb7071fba40e02dbbb1ea97cedb3a0a8a
**Previous ledger commit:** 0e8c22dc88433312cf1ff59d3b1dc4f73e8cd3aa (atomic ledger/results publication)
**Ledger generation:** 482 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 7s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 627; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 609; valid market observations: 609; OHLC screened: 18.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | TAO/USD | 198.5967 | 49.325 | 56.032 | +0.53% | +0.13% | 0.26x | 5.4 | 2026-11-18T00:24:59.810461+00:00 | Not calibrated | MODERATE 45/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 2 | VVV/USD | 21.186 | 48.023 | 48.209 | +0.76% | +0.24% | 0.86x | 11.3 | 2026-11-18T00:24:59.810461+00:00 | Not calibrated | MODERATE 49/100 | HIGH 68/100 | Watch | WATCH |
| 3 | SENT/USD | 0.018761 | 46.929 | 31.396 | +0.49% | +0.11% | 4.70x | 5.9 | 2026-11-18T00:24:59.810461+00:00 | Not calibrated | MODERATE 68/100 | HIGH 67/100 | Watch | WATCH |
| 4 | KAS/USD | 0.02757 | 21.972 | 29.544 | +0.29% | +0.18% | 0.15x | 10.9 | 2026-11-18T00:24:59.810461+00:00 | Not calibrated | WEAK 26/100 | VERY_HIGH 81/100 | Do nothing | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | TAO/USD | 56.032 | 198.5967 | +0.13% | 0.26x |
| 2 | VVV/USD | 48.209 | 21.186 | +0.24% | 0.86x |
| 3 | SENT/USD | 31.396 | 0.018761 | +0.11% | 4.70x |
| 4 | KAS/USD | 29.544 | 0.02757 | +0.18% | 0.15x |

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

- Persisted scans: 482; predictions: 4215; observations: 290545.
- Matured sampled outcomes across 1/6/24/48h: 3255; gap abstentions: 12410. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 0 (sampled only; not a success-rate estimate).
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

**Writer:** 44207570703 · **Generation:** 482 · **Legacy run:** 44207570703
**Main quote time:** 2026-11-18T00:25:06.774059+00:00 · **Legacy report time:** 2026-11-18T00:25:19.437681+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | TAO/USD | 198.5967 | 49.32 | +0.13% | 0.26x | MODERATE 45/100 | VERY_HIGH 70/100 | Watch |
| 2 | VVV/USD ⭐ | 21.186 | 48.02 | +0.24% | 0.86x | MODERATE 59/100 | HIGH 68/100 | Watch |
| 3 | SENT/USD ⭐ | 0.018761 | 46.93 | +0.11% | 4.70x | STRONG 78/100 | HIGH 67/100 | Watch |
| 4 | KAS/USD | 0.02757 | 21.97 | +0.18% | 0.15x | WEAK 26/100 | VERY_HIGH 81/100 | Do nothing |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | VVV/USD ⭐ | 21.17 | 65.42 | +0.68% | 8.91x | 7506 | STRONG 98/100 | HIGH 55/100 | Consider small entry |
| 2 | SENT/USD ⭐ | 0.018761 | 40.04 | +0.11% | 4.70x | 3791 | STRONG 75/100 | HIGH 67/100 | Watch |

**Same-run overlap:** VVV/USD, SENT/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
