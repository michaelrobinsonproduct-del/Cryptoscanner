# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-20T07:50:51.379403+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/44697814208
**Source SHA:** bdc7e68f7fa75fae6636b7738d52f10a65d92038
**Previous ledger commit:** 70cffd199a85fc6bed3c970b89387af70991d650 (atomic ledger/results publication)
**Ledger generation:** 950 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 7s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 627; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 609; valid market observations: 605; OHLC screened: 19.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | XLM/USD | 0.13433 | 80.011 | 62.965 | +1.23% | +0.41% | 3.14x | 1.3 | 2026-11-20T07:50:44.506848+00:00 | Not calibrated | STRONG 95/100 | HIGH 55/100 | Consider small entry | WATCH |
| 2 | SKR/USD | 0.010403 | 56.631 | 53.234 | +3.55% | +0.58% | 1.05x | 5.8 | 2026-11-20T07:50:44.506848+00:00 | Not calibrated | MODERATE 63/100 | VERY_HIGH 74/100 | Watch | WATCH |
| 3 | STRK/USD | 0.03195 | 55.669 | 35.284 | +0.82% | +1.08% | 4.32x | 9.4 | 2026-11-20T07:50:44.506848+00:00 | Not calibrated | STRONG 83/100 | HIGH 60/100 | Watch | WATCH |
| 4 | XRP/USD | 0.96431 | 54.549 | 58.641 | +0.53% | +0.50% | 0.34x | 0.1 | 2026-11-20T07:50:44.506848+00:00 | Not calibrated | MODERATE 57/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 5 | ICNT/USD | 0.45 | 53.309 | 56.016 | +5.61% | +0.57% | 0.44x | 44.4 | 2026-11-20T07:50:44.506848+00:00 | Not calibrated | WEAK 42/100 | EXTREME 92/100 | Do nothing | WATCH |
| 6 | GBP/USD | 1.31159 | 52.722 | 56.461 | +0.25% | +0.03% | 0.61x | 0.6 | 2026-11-20T07:50:44.506848+00:00 | Not calibrated | MODERATE 46/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 7 | SYRUP/USD | 0.09968 | 47.382 | 50.159 | +3.59% | -0.26% | 0.85x | 14.1 | 2026-11-20T07:50:44.506848+00:00 | Not calibrated | WEAK 24/100 | VERY_HIGH 79/100 | Do nothing | WATCH |
| 8 | AUD/USD | 0.66759 | 41.947 | 40.905 | +0.32% | +0.05% | 1.08x | 0.4 | 2026-11-20T07:50:44.506848+00:00 | Not calibrated | MODERATE 46/100 | HIGH 62/100 | Watch | WATCH |
| 9 | ENA/USD | 0.1051 | 40.540 | 43.876 | +0.29% | +1.06% | 0.14x | 9.5 | 2026-11-20T07:50:44.506848+00:00 | Not calibrated | MODERATE 50/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 10 | HBAR/USD | 0.05408 | 37.505 | 42.737 | +0.60% | +0.46% | 0.24x | 3.7 | 2026-11-20T07:50:44.506848+00:00 | Not calibrated | MODERATE 49/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 11 | ATOM/USD | 1.2669 | 34.538 | 32.386 | +0.43% | +0.28% | 1.07x | 6.3 | 2026-11-20T07:50:44.506848+00:00 | Not calibrated | MODERATE 52/100 | HIGH 67/100 | Watch | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | XLM/USD | 62.965 | 0.13433 | +0.41% | 3.14x |
| 2 | XRP/USD | 58.641 | 0.96431 | +0.50% | 0.34x |
| 3 | GBP/USD | 56.461 | 1.31159 | +0.03% | 0.61x |
| 4 | ICNT/USD | 56.016 | 0.45 | +0.57% | 0.44x |
| 5 | SKR/USD | 53.234 | 0.010403 | +0.58% | 1.05x |
| 6 | SYRUP/USD | 50.159 | 0.09968 | -0.26% | 0.85x |
| 7 | ENA/USD | 43.876 | 0.1051 | +1.06% | 0.14x |
| 8 | HBAR/USD | 42.737 | 0.05408 | +0.46% | 0.24x |
| 9 | AUD/USD | 40.905 | 0.66759 | +0.05% | 1.08x |
| 10 | STRK/USD | 35.284 | 0.03195 | +1.08% | 4.32x |
| 11 | ATOM/USD | 32.386 | 1.2669 | +0.28% | 1.07x |

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

- Persisted scans: 950; predictions: 8067; observations: 574021.
- Matured sampled outcomes across 1/6/24/48h: 9508; gap abstentions: 17435. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 10 (sampled only; not a success-rate estimate).
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

**Writer:** 44697814208 · **Generation:** 950 · **Legacy run:** 44697814208
**Main quote time:** 2026-11-20T07:50:51.379403+00:00 · **Legacy report time:** 2026-11-20T07:51:39.914430+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | XLM/USD ⭐ | 0.13433 | 80.01 | +0.41% | 3.14x | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 2 | SKR/USD ⭐ | 0.010403 | 56.63 | +0.58% | 1.05x | STRONG 73/100 | VERY_HIGH 74/100 | Watch |
| 3 | STRK/USD ⭐ | 0.03195 | 55.67 | +1.08% | 4.32x | STRONG 93/100 | HIGH 60/100 | Consider small entry |
| 4 | XRP/USD | 0.96431 | 54.55 | +0.50% | 0.34x | MODERATE 57/100 | VERY_HIGH 70/100 | Watch |
| 5 | ICNT/USD | 0.45 | 53.31 | +0.57% | 0.44x | WEAK 42/100 | EXTREME 92/100 | Do nothing |
| 6 | GBP/USD | 1.31159 | 52.72 | +0.03% | 0.61x | MODERATE 46/100 | VERY_HIGH 70/100 | Watch |
| 7 | SYRUP/USD | 0.09968 | 47.38 | -0.26% | 0.85x | WEAK 24/100 | VERY_HIGH 79/100 | Do nothing |
| 8 | AUD/USD ⭐ | 0.66759 | 41.95 | +0.05% | 1.08x | MODERATE 56/100 | HIGH 62/100 | Watch |
| 9 | ENA/USD | 0.1051 | 40.54 | +1.06% | 0.14x | MODERATE 50/100 | VERY_HIGH 70/100 | Watch |
| 10 | HBAR/USD | 0.05408 | 37.51 | +0.46% | 0.24x | MODERATE 49/100 | VERY_HIGH 70/100 | Watch |
| 11 | ATOM/USD | 1.2669 | 34.54 | +0.28% | 1.07x | MODERATE 52/100 | HIGH 67/100 | Watch |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | XLM/USD ⭐ | 0.134265 | 67.78 | +0.41% | 3.14x | 9663 | STRONG 99/100 | HIGH 55/100 | Consider small entry |
| 2 | SKR/USD ⭐ | 0.010389 | 57.43 | +0.58% | 1.05x | 1653 | MODERATE 69/100 | VERY_HIGH 80/100 | Watch |
| 3 | STRK/USD ⭐ | 0.032 | 47.52 | +1.08% | 4.32x | 3336 | STRONG 84/100 | HIGH 66/100 | Consider small entry |
| 4 | AUD/USD ⭐ | 0.66759 | 45.41 | +0.05% | 1.08x | 3951 | MODERATE 58/100 | HIGH 62/100 | Watch |

**Same-run overlap:** XLM/USD, SKR/USD, STRK/USD, AUD/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
