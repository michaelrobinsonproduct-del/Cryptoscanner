# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-21T01:20:44.412975+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/44849498555
**Source SHA:** bdc7e68f7fa75fae6636b7738d52f10a65d92038
**Previous ledger commit:** 6b42102463b71c038f81b72a04e0b8e3cfe03a77 (atomic ledger/results publication)
**Ledger generation:** 1054 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 7s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 628; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 610; valid market observations: 608; OHLC screened: 24.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | VVV/USD | 21.048 | 82.157 | 59.477 | +1.49% | +1.54% | 2.96x | 11.9 | 2026-11-21T01:20:37.295843+00:00 | Not calibrated | STRONG 91/100 | HIGH 61/100 | Consider small entry | WATCH |
| 2 | LINK/USD | 8.55367 | 71.792 | 54.696 | +0.28% | +0.42% | 4.14x | 4.5 | 2026-11-21T01:20:37.295843+00:00 | Not calibrated | STRONG 91/100 | HIGH 55/100 | Consider small entry | WATCH |
| 3 | QNT/USD | 139.17 | 67.130 | 49.965 | +0.30% | +0.43% | 3.28x | 6.5 | 2026-11-21T01:20:37.295843+00:00 | Not calibrated | STRONG 89/100 | HIGH 55/100 | Watch | WATCH |
| 4 | XBT/USD | 58988.8 | 58.215 | 57.163 | +0.31% | +0.29% | 0.96x | 0.0 | 2026-11-21T01:20:37.295843+00:00 | Not calibrated | MODERATE 59/100 | HIGH 62/100 | Watch | WATCH |
| 5 | XDG/USD | 0.0544339 | 56.113 | 56.829 | +0.29% | +0.40% | 0.73x | 0.4 | 2026-11-21T01:20:37.295843+00:00 | Not calibrated | MODERATE 58/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 6 | AVAX/USD | 6.526 | 50.953 | 48.637 | +0.31% | +0.48% | 0.99x | 1.5 | 2026-11-21T01:20:37.295843+00:00 | Not calibrated | MODERATE 55/100 | HIGH 62/100 | Watch | WATCH |
| 7 | CC/USD | 0.07483 | 47.282 | 35.781 | +0.38% | +0.00% | 2.15x | 6.7 | 2026-11-21T01:20:37.295843+00:00 | Not calibrated | MODERATE 69/100 | HIGH 60/100 | Watch | WATCH |
| 8 | SKY/USD | 0.04416 | 46.918 | 36.364 | +0.73% | +0.50% | 1.81x | 9.1 | 2026-11-21T01:20:37.295843+00:00 | Not calibrated | MODERATE 68/100 | HIGH 60/100 | Watch | WATCH |
| 9 | UNI/USD | 4.482 | 45.142 | 48.933 | +0.33% | +0.36% | 0.44x | 3.4 | 2026-11-21T01:20:37.295843+00:00 | Not calibrated | MODERATE 53/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 10 | PIEVERSE/USD | 3.0522 | 44.162 | 43.104 | +1.78% | +0.57% | 0.82x | 8.5 | 2026-11-21T01:20:37.295843+00:00 | Not calibrated | MODERATE 52/100 | HIGH 67/100 | Watch | WATCH |
| 11 | DCR/USD | 10.141 | 28.446 | 29.274 | +0.36% | -0.05% | 0.94x | 7.9 | 2026-11-21T01:20:37.295843+00:00 | Not calibrated | WEAK 19/100 | VERY_HIGH 80/100 | Do nothing | WATCH |
| 12 | TRAC/USD | 0.2709 | 8.355 | 12.829 | +0.33% | +0.26% | 0.42x | 40.7 | 2026-11-21T01:20:37.295843+00:00 | Not calibrated | WEAK 19/100 | EXTREME 100/100 | Do nothing | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | VVV/USD | 59.477 | 21.048 | +1.54% | 2.96x |
| 2 | XBT/USD | 57.163 | 58988.8 | +0.29% | 0.96x |
| 3 | XDG/USD | 56.829 | 0.0544339 | +0.40% | 0.73x |
| 4 | LINK/USD | 54.696 | 8.55367 | +0.42% | 4.14x |
| 5 | QNT/USD | 49.965 | 139.17 | +0.43% | 3.28x |
| 6 | UNI/USD | 48.933 | 4.482 | +0.36% | 0.44x |
| 7 | AVAX/USD | 48.637 | 6.526 | +0.48% | 0.99x |
| 8 | PIEVERSE/USD | 43.104 | 3.0522 | +0.57% | 0.82x |
| 9 | SKY/USD | 36.364 | 0.04416 | +0.50% | 1.81x |
| 10 | CC/USD | 35.781 | 0.07483 | +0.00% | 2.15x |
| 11 | DCR/USD | 29.274 | 10.141 | -0.05% | 0.94x |
| 12 | TRAC/USD | 12.829 | 0.2709 | +0.26% | 0.42x |

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

- Persisted scans: 1054; predictions: 8451; observations: 637192.
- Matured sampled outcomes across 1/6/24/48h: 10937; gap abstentions: 19165. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 10 (sampled only; not a success-rate estimate).
- False positives / missed movers: NOT VERIFIED without eligible continuous outcome coverage.
- Baseline vs challenger: recorded as-of; unbiased held-out lift NOT MEASURED.
- Online Kraken /USD stablecoin-base pairs excluded: 18 (counted from this scan's online AssetPairs metadata, not inferred from price).
- Stablecoin base exclusions: BRL1, BUSD, DAI, EUR, EURC, EUROP, EURQ, EURR, EURT, FDUSD, FRAX, GUSD, PYUSD, QCAD, RLUSD, TGBP, TUSD, USD, USD1, USDC, USDD, USDE, USDG, USDQ, USDR, USDS, USDT, ZUSD.
- DEX: NOT USED; no DEX freshness gate.
- OHLC screening abstentions: 12; details in immutable scan JSON artifact.
- Storage: ledger and results published in one non-force Git commit and read back. Independent artifact recovery is NOT VERIFIED by this scan alone.
- Errors: none in successful committed scan; a failed workflow must not publish a SUCCESS report.

# Cryptoscanner — challenger and independent legacy-inspired WATCH

Paper only · risk is high or higher · 30%+ in 48h probability NOT CALIBRATED
Signal confidence 0–100 means setup strength only, NOT a win probability. Actions are research guidance; no trade authorization.

**Writer:** 44849498555 · **Generation:** 1054 · **Legacy run:** 44849498555
**Main quote time:** 2026-11-21T01:20:44.412975+00:00 · **Legacy report time:** 2026-11-21T01:21:48.483692+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | VVV/USD ⭐ | 21.048 | 82.16 | +1.54% | 2.96x | STRONG 100/100 | HIGH 61/100 | Consider small entry |
| 2 | LINK/USD ⭐ | 8.55367 | 71.79 | +0.42% | 4.14x | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 3 | QNT/USD | 139.17 | 67.13 | +0.43% | 3.28x | STRONG 89/100 | HIGH 55/100 | Watch |
| 4 | XBT/USD | 58988.8 | 58.22 | +0.29% | 0.96x | MODERATE 59/100 | HIGH 62/100 | Watch |
| 5 | XDG/USD | 0.0544339 | 56.11 | +0.40% | 0.73x | MODERATE 58/100 | VERY_HIGH 70/100 | Watch |
| 6 | AVAX/USD | 6.526 | 50.95 | +0.48% | 0.99x | MODERATE 55/100 | HIGH 62/100 | Watch |
| 7 | CC/USD | 0.07483 | 47.28 | +0.00% | 2.15x | MODERATE 69/100 | HIGH 60/100 | Watch |
| 8 | SKY/USD | 0.04416 | 46.92 | +0.50% | 1.81x | MODERATE 68/100 | HIGH 60/100 | Watch |
| 9 | UNI/USD | 4.482 | 45.14 | +0.36% | 0.44x | MODERATE 53/100 | VERY_HIGH 70/100 | Watch |
| 10 | PIEVERSE/USD | 3.0522 | 44.16 | +0.57% | 0.82x | MODERATE 52/100 | HIGH 67/100 | Watch |
| 11 | DCR/USD | 10.141 | 28.45 | -0.05% | 0.94x | WEAK 19/100 | VERY_HIGH 80/100 | Do nothing |
| 12 | TRAC/USD | 0.2709 | 8.36 | +0.26% | 0.42x | WEAK 19/100 | EXTREME 100/100 | Do nothing |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | VVV/USD ⭐ | 21.051 | 67.51 | +1.54% | 2.96x | 11581 | STRONG 94/100 | HIGH 61/100 | Consider small entry |
| 2 | ETH/USD | 1621.13 | 62.27 | +0.35% | 3.02x | 86244 | STRONG 86/100 | HIGH 55/100 | Watch |
| 3 | LINK/USD ⭐ | 8.54644 | 55.18 | +0.42% | 4.14x | 10997 | STRONG 93/100 | HIGH 55/100 | Consider small entry |
| 4 | CT/USD | 0.1232 | 49.54 | +0.99% | 2.13x | 2409 | STRONG 70/100 | VERY_HIGH 72/100 | Watch |
| 5 | KAS/USD | 0.02622 | 44.30 | +0.34% | 2.29x | 5614 | STRONG 72/100 | HIGH 61/100 | Watch |

**Same-run overlap:** VVV/USD, LINK/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
