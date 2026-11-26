# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-26T22:21:01.084142+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/45904045645
**Source SHA:** 858c8bc8ec5d7641ddb39cacd8aca91719f855b1
**Previous ledger commit:** a04a6c5678b787be86ff0007981d13178faed66e (atomic ledger/results publication)
**Ledger generation:** 1921 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 7s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 628; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 610; valid market observations: 599; OHLC screened: 24.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | DRV/USD | 0.38614 | 92.033 | 83.008 | +7.92% | -1.20% | 4.02x | 0.3 | 2026-11-26T22:20:54.381783+00:00 | Not calibrated | STRONG 76/100 | HIGH 65/100 | Watch | WATCH |
| 2 | LTC/USD | 44.17 | 86.850 | 76.664 | +3.42% | +0.11% | 1.96x | 4.5 | 2026-11-26T22:20:54.381783+00:00 | Not calibrated | STRONG 78/100 | HIGH 55/100 | Watch | WATCH |
| 3 | AKT/USD | 0.5052 | 77.918 | 72.982 | +6.79% | +0.00% | 1.49x | 9.9 | 2026-11-26T22:20:54.381783+00:00 | Not calibrated | STRONG 74/100 | HIGH 60/100 | Watch | WATCH |
| 4 | LINK/USD | 9.35098 | 73.352 | 77.258 | +3.39% | -0.31% | 0.77x | 2.9 | 2026-11-26T22:20:54.381783+00:00 | Not calibrated | WEAK 42/100 | HIGH 68/100 | Watch | WATCH |
| 5 | ZRO/USD | 1.139 | 68.667 | 72.088 | +11.23% | -0.26% | 0.79x | 17.6 | 2026-11-26T22:20:54.381783+00:00 | Not calibrated | WEAK 34/100 | VERY_HIGH 79/100 | Do nothing | WATCH |
| 6 | HYPE/USD | 62.51 | 67.054 | 64.311 | +1.44% | -0.18% | 1.36x | 1.6 | 2026-11-26T22:20:54.381783+00:00 | Not calibrated | MODERATE 54/100 | HIGH 61/100 | Watch | WATCH |
| 7 | W/USD | 0.00883 | 65.251 | 71.292 | +6.39% | -0.45% | 0.62x | 11.3 | 2026-11-26T22:20:54.381783+00:00 | Not calibrated | WEAK 33/100 | EXTREME 87/100 | Do nothing | WATCH |
| 8 | XDG/USD | 0.0566548 | 65.018 | 50.964 | +1.24% | -0.19% | 3.20x | 1.6 | 2026-11-26T22:20:54.381783+00:00 | Not calibrated | MODERATE 63/100 | HIGH 61/100 | Watch | WATCH |
| 9 | SOL/USD | 71.19 | 64.556 | 62.253 | +1.14% | -0.25% | 1.36x | 1.4 | 2026-11-26T22:20:54.381783+00:00 | Not calibrated | MODERATE 52/100 | HIGH 61/100 | Watch | WATCH |
| 10 | ADA/USD | 0.149694 | 63.206 | 71.905 | +2.69% | -0.08% | 0.17x | 3.9 | 2026-11-26T22:20:54.381783+00:00 | Not calibrated | WEAK 37/100 | VERY_HIGH 76/100 | Watch | WATCH |
| 11 | XBT/USD | 60534.2 | 56.134 | 56.912 | +0.27% | -0.14% | 0.99x | 0.0 | 2026-11-26T22:20:54.381783+00:00 | Not calibrated | WEAK 33/100 | HIGH 68/100 | Do nothing | WATCH |
| 12 | XRP/USD | 0.94956 | 56.097 | 64.295 | +1.39% | -0.04% | 0.20x | 0.8 | 2026-11-26T22:20:54.381783+00:00 | Not calibrated | WEAK 33/100 | VERY_HIGH 76/100 | Do nothing | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | DRV/USD | 83.008 | 0.38614 | -1.20% | 4.02x |
| 2 | LINK/USD | 77.258 | 9.35098 | -0.31% | 0.77x |
| 3 | LTC/USD | 76.664 | 44.17 | +0.11% | 1.96x |
| 4 | AKT/USD | 72.982 | 0.5052 | +0.00% | 1.49x |
| 5 | ZRO/USD | 72.088 | 1.139 | -0.26% | 0.79x |
| 6 | ADA/USD | 71.905 | 0.149694 | -0.08% | 0.17x |
| 7 | W/USD | 71.292 | 0.00883 | -0.45% | 0.62x |
| 8 | HYPE/USD | 64.311 | 62.51 | -0.18% | 1.36x |
| 9 | XRP/USD | 64.295 | 0.94956 | -0.04% | 0.20x |
| 10 | SOL/USD | 62.253 | 71.19 | -0.25% | 1.36x |
| 11 | XBT/USD | 56.912 | 60534.2 | -0.14% | 0.99x |
| 12 | XDG/USD | 50.964 | 0.0566548 | -0.19% | 3.20x |

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

- Persisted scans: 1921; predictions: 16787; observations: 1163613.
- Matured sampled outcomes across 1/6/24/48h: 36572; gap abstentions: 25305. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 146 (sampled only; not a success-rate estimate).
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

**Writer:** 45904045645 · **Generation:** 1921 · **Legacy run:** 45904045645
**Main quote time:** 2026-11-26T22:21:01.084142+00:00 · **Legacy report time:** 2026-11-26T22:21:41.696715+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | DRV/USD | 0.38614 | 92.03 | -1.20% | 4.02x | STRONG 76/100 | HIGH 65/100 | Watch |
| 2 | LTC/USD ⭐ | 44.17 | 86.85 | +0.11% | 1.96x | STRONG 88/100 | HIGH 55/100 | Watch |
| 3 | AKT/USD | 0.5052 | 77.92 | +0.00% | 1.49x | STRONG 74/100 | HIGH 60/100 | Watch |
| 4 | LINK/USD | 9.35098 | 73.35 | -0.31% | 0.77x | WEAK 42/100 | HIGH 68/100 | Watch |
| 5 | ZRO/USD | 1.139 | 68.67 | -0.26% | 0.79x | WEAK 34/100 | VERY_HIGH 79/100 | Do nothing |
| 6 | HYPE/USD | 62.51 | 67.05 | -0.18% | 1.36x | MODERATE 54/100 | HIGH 61/100 | Watch |
| 7 | W/USD | 0.00883 | 65.25 | -0.45% | 0.62x | WEAK 33/100 | EXTREME 87/100 | Do nothing |
| 8 | XDG/USD | 0.0566548 | 65.02 | -0.19% | 3.20x | MODERATE 63/100 | HIGH 61/100 | Watch |
| 9 | SOL/USD | 71.19 | 64.56 | -0.25% | 1.36x | MODERATE 52/100 | HIGH 61/100 | Watch |
| 10 | ADA/USD | 0.149694 | 63.21 | -0.08% | 0.17x | WEAK 37/100 | VERY_HIGH 76/100 | Watch |
| 11 | XBT/USD | 60534.2 | 56.13 | -0.14% | 0.99x | WEAK 33/100 | HIGH 68/100 | Do nothing |
| 12 | XRP/USD | 0.94956 | 56.10 | -0.04% | 0.20x | WEAK 33/100 | VERY_HIGH 76/100 | Do nothing |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | LTC/USD ⭐ | 44.16 | 87.87 | +0.11% | 1.96x | 14411 | STRONG 89/100 | HIGH 55/100 | Watch |

**Same-run overlap:** LTC/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
