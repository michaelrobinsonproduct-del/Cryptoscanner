# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-18T03:00:03.890293+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/44227206505
**Source SHA:** 394c17eeb7071fba40e02dbbb1ea97cedb3a0a8a
**Previous ledger commit:** a5782089cae44cfaeec2d1bf7990279f0499f96b (atomic ledger/results publication)
**Ledger generation:** 513 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 5s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 627; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 609; valid market observations: 609; OHLC screened: 12.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | AKE/USD | 0.01018153 | 46.927 | 35.012 | +1.98% | +1.99% | 1.20x | 27.4 | 2026-11-18T02:59:59.184489+00:00 | Not calibrated | MODERATE 48/100 | VERY_HIGH 79/100 | Watch | WATCH |
| 2 | AKT/USD | 0.523 | 39.959 | 49.313 | +2.69% | -0.99% | 0.56x | 3.8 | 2026-11-18T02:59:59.184489+00:00 | Not calibrated | WEAK 25/100 | VERY_HIGH 81/100 | Do nothing | WATCH |
| 3 | SENT/USD | 0.018723 | 39.323 | 31.540 | +0.29% | +0.73% | 1.42x | 2.7 | 2026-11-18T02:59:59.184489+00:00 | Not calibrated | MODERATE 65/100 | HIGH 67/100 | Watch | WATCH |
| 4 | CC/USD | 0.08295 | 34.690 | 40.870 | +1.00% | +0.11% | 0.33x | 2.4 | 2026-11-18T02:59:59.184489+00:00 | Not calibrated | WEAK 37/100 | VERY_HIGH 75/100 | Watch | WATCH |
| 5 | ICNT/USD | 0.2792 | 31.368 | 29.334 | +1.12% | -0.96% | 1.68x | 21.5 | 2026-11-18T02:59:59.184489+00:00 | Not calibrated | WEAK 26/100 | VERY_HIGH 78/100 | Do nothing | WATCH |
| 6 | CAP/USD | 0.101402 | 28.265 | 29.719 | +0.42% | +0.22% | 0.74x | 10.7 | 2026-11-18T02:59:59.184489+00:00 | Not calibrated | WEAK 39/100 | VERY_HIGH 81/100 | Watch | WATCH |
| 7 | TON/USD | 1.08 | 26.163 | 36.232 | +0.28% | -0.46% | 0.22x | 9.3 | 2026-11-18T02:59:59.184489+00:00 | Not calibrated | WEAK 18/100 | VERY_HIGH 76/100 | Do nothing | WATCH |
| 8 | PEARL/USD | 1.8215 | 9.535 | 17.684 | +0.61% | +0.14% | 0.11x | 43.6 | 2026-11-18T02:59:59.184489+00:00 | Not calibrated | WEAK 10/100 | EXTREME 97/100 | Do nothing | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | AKT/USD | 49.313 | 0.523 | -0.99% | 0.56x |
| 2 | CC/USD | 40.870 | 0.08295 | +0.11% | 0.33x |
| 3 | TON/USD | 36.232 | 1.08 | -0.46% | 0.22x |
| 4 | AKE/USD | 35.012 | 0.01018153 | +1.99% | 1.20x |
| 5 | SENT/USD | 31.540 | 0.018723 | +0.73% | 1.42x |
| 6 | CAP/USD | 29.719 | 0.101402 | +0.22% | 0.74x |
| 7 | ICNT/USD | 29.334 | 0.2792 | -0.96% | 1.68x |
| 8 | PEARL/USD | 17.684 | 1.8215 | +0.14% | 0.11x |

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

- Persisted scans: 513; predictions: 4344; observations: 309424.
- Matured sampled outcomes across 1/6/24/48h: 3494; gap abstentions: 12424. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 0 (sampled only; not a success-rate estimate).
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

**Writer:** 44227206505 · **Generation:** 513 · **Legacy run:** 44227206505
**Main quote time:** 2026-11-18T03:00:03.890293+00:00 · **Legacy report time:** 2026-11-18T03:00:20.995446+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | AKE/USD ⭐ | 0.01018153 | 46.93 | +1.99% | 1.20x | MODERATE 58/100 | VERY_HIGH 79/100 | Watch |
| 2 | AKT/USD | 0.523 | 39.96 | -0.99% | 0.56x | WEAK 25/100 | VERY_HIGH 81/100 | Do nothing |
| 3 | SENT/USD ⭐ | 0.018723 | 39.32 | +0.73% | 1.42x | STRONG 75/100 | HIGH 67/100 | Watch |
| 4 | CC/USD ⭐ | 0.08295 | 34.69 | +0.11% | 0.33x | MODERATE 47/100 | VERY_HIGH 75/100 | Watch |
| 5 | ICNT/USD | 0.2792 | 31.37 | -0.96% | 1.68x | WEAK 26/100 | VERY_HIGH 78/100 | Do nothing |
| 6 | CAP/USD | 0.101402 | 28.27 | +0.22% | 0.74x | WEAK 39/100 | VERY_HIGH 81/100 | Watch |
| 7 | TON/USD | 1.08 | 26.16 | -0.46% | 0.22x | WEAK 18/100 | VERY_HIGH 76/100 | Do nothing |
| 8 | PEARL/USD | 1.8215 | 9.54 | +0.14% | 0.11x | WEAK 10/100 | EXTREME 97/100 | Do nothing |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | AKE/USD ⭐ | 0.01018153 | 55.39 | +1.99% | 1.20x | 5565 | MODERATE 63/100 | VERY_HIGH 79/100 | Watch |
| 2 | CC/USD ⭐ | 0.08292 | 48.22 | +0.74% | 1.41x | 3975 | STRONG 79/100 | HIGH 60/100 | Watch |
| 3 | SENT/USD ⭐ | 0.018723 | 32.02 | +0.73% | 1.42x | 3806 | STRONG 71/100 | HIGH 67/100 | Watch |

**Same-run overlap:** AKE/USD, SENT/USD, CC/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
