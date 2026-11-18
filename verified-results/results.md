# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-18T03:55:11.302117+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/44233651914
**Source SHA:** 394c17eeb7071fba40e02dbbb1ea97cedb3a0a8a
**Previous ledger commit:** 99c5bdd4d6de19d1cc8038dde6302c6d094c1e24 (atomic ledger/results publication)
**Ledger generation:** 524 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 6s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 627; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 609; valid market observations: 609; OHLC screened: 16.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | MELANIA/USD | 0.0513 | 61.392 | 58.304 | +5.34% | +0.59% | 1.01x | 19.5 | 2026-11-18T03:55:05.387151+00:00 | Not calibrated | MODERATE 61/100 | VERY_HIGH 80/100 | Watch | WATCH |
| 2 | SENT/USD | 0.019069 | 58.411 | 41.675 | +2.14% | +0.35% | 4.08x | 8.4 | 2026-11-18T03:55:05.387151+00:00 | Not calibrated | STRONG 84/100 | HIGH 67/100 | Watch | WATCH |
| 3 | XDC/USD | 0.03056 | 58.064 | 35.254 | +0.79% | +1.56% | 10.69x | 16.4 | 2026-11-18T03:55:05.387151+00:00 | Not calibrated | STRONG 79/100 | HIGH 61/100 | Watch | WATCH |
| 4 | CC/USD | 0.08376 | 56.725 | 45.627 | +1.98% | +0.10% | 2.06x | 7.2 | 2026-11-18T03:55:05.387151+00:00 | Not calibrated | STRONG 73/100 | HIGH 60/100 | Watch | WATCH |
| 5 | AKT/USD | 0.5169 | 48.791 | 38.011 | +1.49% | -0.84% | 3.55x | 9.7 | 2026-11-18T03:55:05.387151+00:00 | Not calibrated | MODERATE 54/100 | HIGH 66/100 | Watch | WATCH |
| 6 | ZAMA/USD | 0.06105 | 44.891 | 39.992 | +1.87% | +0.79% | 1.09x | 13.1 | 2026-11-18T03:55:05.387151+00:00 | Not calibrated | MODERATE 52/100 | VERY_HIGH 73/100 | Watch | WATCH |
| 7 | PEARL/USD | 1.8308 | 33.506 | 32.681 | +1.12% | +0.02% | 1.07x | 20.8 | 2026-11-18T03:55:05.387151+00:00 | Not calibrated | WEAK 32/100 | VERY_HIGH 79/100 | Do nothing | WATCH |
| 8 | ICNT/USD | 0.2811 | 30.954 | 34.227 | +1.81% | +0.43% | 0.46x | 21.5 | 2026-11-18T03:55:05.387151+00:00 | Not calibrated | WEAK 35/100 | EXTREME 87/100 | Do nothing | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | MELANIA/USD | 58.304 | 0.0513 | +0.59% | 1.01x |
| 2 | CC/USD | 45.627 | 0.08376 | +0.10% | 2.06x |
| 3 | SENT/USD | 41.675 | 0.019069 | +0.35% | 4.08x |
| 4 | ZAMA/USD | 39.992 | 0.06105 | +0.79% | 1.09x |
| 5 | AKT/USD | 38.011 | 0.5169 | -0.84% | 3.55x |
| 6 | XDC/USD | 35.254 | 0.03056 | +1.56% | 10.69x |
| 7 | ICNT/USD | 34.227 | 0.2811 | +0.43% | 0.46x |
| 8 | PEARL/USD | 32.681 | 1.8308 | +0.02% | 1.07x |

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

- Persisted scans: 524; predictions: 4428; observations: 316123.
- Matured sampled outcomes across 1/6/24/48h: 3534; gap abstentions: 12439. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 0 (sampled only; not a success-rate estimate).
- False positives / missed movers: NOT VERIFIED without eligible continuous outcome coverage.
- Baseline vs challenger: recorded as-of; unbiased held-out lift NOT MEASURED.
- Online Kraken /USD stablecoin-base pairs excluded: 18 (counted from this scan's online AssetPairs metadata, not inferred from price).
- Stablecoin base exclusions: BRL1, BUSD, DAI, EUR, EURC, EUROP, EURQ, EURR, EURT, FDUSD, FRAX, GUSD, PYUSD, QCAD, RLUSD, TGBP, TUSD, USD, USD1, USDC, USDD, USDE, USDG, USDQ, USDR, USDS, USDT, ZUSD.
- DEX: NOT USED; no DEX freshness gate.
- OHLC screening abstentions: 8; details in immutable scan JSON artifact.
- Storage: ledger and results published in one non-force Git commit and read back. Independent artifact recovery is NOT VERIFIED by this scan alone.
- Errors: none in successful committed scan; a failed workflow must not publish a SUCCESS report.

# Cryptoscanner — challenger and independent legacy-inspired WATCH

Paper only · risk is high or higher · 30%+ in 48h probability NOT CALIBRATED
Signal confidence 0–100 means setup strength only, NOT a win probability. Actions are research guidance; no trade authorization.

**Writer:** 44233651914 · **Generation:** 524 · **Legacy run:** 44233651914
**Main quote time:** 2026-11-18T03:55:11.302117+00:00 · **Legacy report time:** 2026-11-18T03:55:27.685117+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | MELANIA/USD | 0.0513 | 61.39 | +0.59% | 1.01x | MODERATE 61/100 | VERY_HIGH 80/100 | Watch |
| 2 | SENT/USD ⭐ | 0.019069 | 58.41 | +0.35% | 4.08x | STRONG 94/100 | HIGH 67/100 | Consider small entry |
| 3 | XDC/USD ⭐ | 0.03056 | 58.06 | +1.56% | 10.69x | STRONG 89/100 | HIGH 61/100 | Consider small entry |
| 4 | CC/USD ⭐ | 0.08376 | 56.73 | +0.10% | 2.06x | STRONG 83/100 | HIGH 60/100 | Watch |
| 5 | AKT/USD | 0.5169 | 48.79 | -0.84% | 3.55x | MODERATE 54/100 | HIGH 66/100 | Watch |
| 6 | ZAMA/USD ⭐ | 0.06105 | 44.89 | +0.79% | 1.09x | MODERATE 62/100 | VERY_HIGH 73/100 | Watch |
| 7 | PEARL/USD | 1.8308 | 33.51 | +0.02% | 1.07x | WEAK 32/100 | VERY_HIGH 79/100 | Do nothing |
| 8 | ICNT/USD | 0.2811 | 30.95 | +0.43% | 0.46x | WEAK 35/100 | EXTREME 87/100 | Do nothing |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | CC/USD ⭐ | 0.08376 | 58.99 | +0.10% | 2.06x | 4054 | STRONG 84/100 | HIGH 60/100 | Watch |
| 2 | SENT/USD ⭐ | 0.019069 | 57.28 | +0.35% | 4.08x | 3888 | STRONG 94/100 | HIGH 67/100 | Consider small entry |
| 3 | XDC/USD ⭐ | 0.03056 | 48.93 | +1.56% | 10.69x | 6197 | STRONG 84/100 | HIGH 61/100 | Consider small entry |
| 4 | ZAMA/USD ⭐ | 0.06099 | 48.06 | +0.79% | 1.09x | 4497 | MODERATE 64/100 | VERY_HIGH 73/100 | Watch |

**Same-run overlap:** SENT/USD, XDC/USD, CC/USD, ZAMA/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
