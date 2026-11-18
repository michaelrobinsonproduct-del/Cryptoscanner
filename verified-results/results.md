# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-18T19:00:14.641847+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/44375662036
**Source SHA:** b271b90a2cae9e5307600070ce7d0e510fe68996
**Previous ledger commit:** 55c1fa212fec201e6d5bc85af5fc05334d6d5caf (atomic ledger/results publication)
**Ledger generation:** 642 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 6s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 627; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 609; valid market observations: 609; OHLC screened: 18.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | INFI/USD | 0.1336 | 103.777 | 63.777 | +5.20% | +8.27% | 3.32x | 7.5 | 2026-11-18T19:00:09.034404+00:00 | Not calibrated | STRONG 100/100 | VERY_HIGH 77/100 | Watch | WATCH |
| 2 | SENT/USD | 0.019865 | 87.601 | 74.455 | +6.41% | -0.37% | 2.83x | 3.0 | 2026-11-18T19:00:09.034404+00:00 | Not calibrated | STRONG 74/100 | VERY_HIGH 73/100 | Watch | WATCH |
| 3 | AKE/USD | 0.01054067 | 52.039 | 56.444 | +5.57% | +0.58% | 0.27x | 34.4 | 2026-11-18T19:00:09.034404+00:00 | Not calibrated | MODERATE 46/100 | EXTREME 87/100 | Do nothing | WATCH |
| 4 | AKT/USD | 0.5114 | 43.145 | 28.047 | +0.41% | +0.02% | 2.92x | 13.7 | 2026-11-18T19:00:09.034404+00:00 | Not calibrated | MODERATE 62/100 | HIGH 66/100 | Watch | WATCH |
| 5 | MNT/USD | 0.3856 | 36.970 | 44.545 | +3.29% | +0.16% | 0.16x | 20.8 | 2026-11-18T19:00:09.034404+00:00 | Not calibrated | WEAK 28/100 | EXTREME 87/100 | Do nothing | WATCH |
| 6 | CC/USD | 0.08243 | 36.333 | 32.838 | +0.37% | -0.04% | 1.37x | 9.7 | 2026-11-18T19:00:09.034404+00:00 | Not calibrated | WEAK 38/100 | HIGH 66/100 | Watch | WATCH |
| 7 | UAI/USD | 0.03352 | 25.700 | 24.856 | +0.42% | +0.06% | 1.05x | 17.9 | 2026-11-18T19:00:09.034404+00:00 | Not calibrated | WEAK 33/100 | VERY_HIGH 80/100 | Do nothing | WATCH |
| 8 | W/USD | 0.009 | 20.437 | 20.122 | +0.78% | +0.22% | 0.92x | 33.3 | 2026-11-18T19:00:09.034404+00:00 | Not calibrated | WEAK 30/100 | EXTREME 86/100 | Do nothing | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | SENT/USD | 74.455 | 0.019865 | -0.37% | 2.83x |
| 2 | INFI/USD | 63.777 | 0.1336 | +8.27% | 3.32x |
| 3 | AKE/USD | 56.444 | 0.01054067 | +0.58% | 0.27x |
| 4 | MNT/USD | 44.545 | 0.3856 | +0.16% | 0.16x |
| 5 | CC/USD | 32.838 | 0.08243 | -0.04% | 1.37x |
| 6 | AKT/USD | 28.047 | 0.5114 | +0.02% | 2.92x |
| 7 | UAI/USD | 24.856 | 0.03352 | +0.06% | 1.05x |
| 8 | W/USD | 20.122 | 0.009 | +0.22% | 0.92x |

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

- Persisted scans: 642; predictions: 5450; observations: 387985.
- Matured sampled outcomes across 1/6/24/48h: 4742; gap abstentions: 13125. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 0 (sampled only; not a success-rate estimate).
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

**Writer:** 44375662036 · **Generation:** 642 · **Legacy run:** 44375662036
**Main quote time:** 2026-11-18T19:00:14.641847+00:00 · **Legacy report time:** 2026-11-18T19:00:48.538460+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | INFI/USD ⭐ | 0.1336 | 103.78 | +8.27% | 3.32x | STRONG 100/100 | VERY_HIGH 77/100 | Watch |
| 2 | SENT/USD | 0.019865 | 87.60 | -0.37% | 2.83x | STRONG 74/100 | VERY_HIGH 73/100 | Watch |
| 3 | AKE/USD | 0.01054067 | 52.04 | +0.58% | 0.27x | MODERATE 46/100 | EXTREME 87/100 | Do nothing |
| 4 | AKT/USD | 0.5114 | 43.14 | +0.02% | 2.92x | MODERATE 62/100 | HIGH 66/100 | Watch |
| 5 | MNT/USD | 0.3856 | 36.97 | +0.16% | 0.16x | WEAK 28/100 | EXTREME 87/100 | Do nothing |
| 6 | CC/USD | 0.08243 | 36.33 | -0.04% | 1.37x | WEAK 38/100 | HIGH 66/100 | Watch |
| 7 | UAI/USD | 0.03352 | 25.70 | +0.06% | 1.05x | WEAK 33/100 | VERY_HIGH 80/100 | Do nothing |
| 8 | W/USD | 0.009 | 20.44 | +0.22% | 0.92x | WEAK 30/100 | EXTREME 86/100 | Do nothing |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | INFI/USD ⭐ | 0.1336 | 86.71 | +8.27% | 3.32x | 3689 | STRONG 100/100 | VERY_HIGH 77/100 | Watch |
| 2 | TRX/USD | 0.308538 | 43.96 | +0.09% | 1.09x | 4151 | MODERATE 47/100 | HIGH 62/100 | Watch |

**Same-run overlap:** INFI/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
