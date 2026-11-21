# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-21T02:00:26.416974+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/44853340278
**Source SHA:** bdc7e68f7fa75fae6636b7738d52f10a65d92038
**Previous ledger commit:** 89df2e17a6a80670ef5f88eb8b02a1f33f639f40 (atomic ledger/results publication)
**Ledger generation:** 1060 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 7s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 628; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 610; valid market observations: 608; OHLC screened: 24.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | VVV/USD | 21.301 | 74.382 | 70.220 | +2.71% | +0.65% | 1.09x | 7.5 | 2026-11-21T02:00:19.443558+00:00 | Not calibrated | STRONG 72/100 | HIGH 62/100 | Watch | WATCH |
| 2 | UNI/USD | 4.4866 | 64.676 | 49.117 | +0.43% | +0.11% | 5.43x | 3.8 | 2026-11-21T02:00:19.443558+00:00 | Not calibrated | STRONG 77/100 | HIGH 55/100 | Watch | WATCH |
| 3 | XDG/USD | 0.0545264 | 58.916 | 57.628 | +0.46% | +0.29% | 0.98x | 1.2 | 2026-11-21T02:00:19.443558+00:00 | Not calibrated | MODERATE 59/100 | HIGH 62/100 | Watch | WATCH |
| 4 | SKY/USD | 0.04429 | 54.468 | 38.562 | +1.03% | +0.18% | 8.45x | 9.0 | 2026-11-21T02:00:19.443558+00:00 | Not calibrated | STRONG 72/100 | HIGH 60/100 | Watch | WATCH |
| 5 | ETH/USD | 1623.95 | 51.924 | 56.971 | +0.29% | +0.12% | 0.43x | 0.1 | 2026-11-21T02:00:19.443558+00:00 | Not calibrated | MODERATE 46/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 6 | DCR/USD | 10.241 | 51.492 | 34.769 | +1.35% | +0.34% | 2.67x | 10.8 | 2026-11-21T02:00:19.443558+00:00 | Not calibrated | STRONG 76/100 | VERY_HIGH 73/100 | Watch | WATCH |
| 7 | ALGO/USD | 0.07352 | 49.347 | 38.145 | +0.49% | +0.40% | 1.92x | 8.2 | 2026-11-21T02:00:19.443558+00:00 | Not calibrated | STRONG 70/100 | HIGH 55/100 | Watch | WATCH |
| 8 | DOT/USD | 0.6664 | 33.060 | 35.488 | +0.82% | +0.44% | 0.54x | 9.0 | 2026-11-21T02:00:19.443558+00:00 | Not calibrated | MODERATE 47/100 | VERY_HIGH 75/100 | Watch | WATCH |
| 9 | CC/USD | 0.07496 | 32.065 | 37.316 | +0.55% | +0.32% | 0.31x | 5.3 | 2026-11-21T02:00:19.443558+00:00 | Not calibrated | MODERATE 46/100 | VERY_HIGH 75/100 | Watch | WATCH |
| 10 | CT/USD | 0.1232 | 29.828 | 35.917 | +1.73% | +0.16% | 0.31x | 16.3 | 2026-11-21T02:00:19.443558+00:00 | Not calibrated | WEAK 30/100 | VERY_HIGH 81/100 | Do nothing | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | VVV/USD | 70.220 | 21.301 | +0.65% | 1.09x |
| 2 | XDG/USD | 57.628 | 0.0545264 | +0.29% | 0.98x |
| 3 | ETH/USD | 56.971 | 1623.95 | +0.12% | 0.43x |
| 4 | UNI/USD | 49.117 | 4.4866 | +0.11% | 5.43x |
| 5 | SKY/USD | 38.562 | 0.04429 | +0.18% | 8.45x |
| 6 | ALGO/USD | 38.145 | 0.07352 | +0.40% | 1.92x |
| 7 | CC/USD | 37.316 | 0.07496 | +0.32% | 0.31x |
| 8 | CT/USD | 35.917 | 0.1232 | +0.16% | 0.31x |
| 9 | DOT/USD | 35.488 | 0.6664 | +0.44% | 0.54x |
| 10 | DCR/USD | 34.769 | 10.241 | +0.34% | 2.67x |

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

- Persisted scans: 1060; predictions: 8506; observations: 640840.
- Matured sampled outcomes across 1/6/24/48h: 10945; gap abstentions: 19298. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 10 (sampled only; not a success-rate estimate).
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

**Writer:** 44853340278 · **Generation:** 1060 · **Legacy run:** 44853340278
**Main quote time:** 2026-11-21T02:00:26.416974+00:00 · **Legacy report time:** 2026-11-21T02:01:09.054332+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | VVV/USD ⭐ | 21.301 | 74.38 | +0.65% | 1.09x | STRONG 82/100 | HIGH 62/100 | Watch |
| 2 | UNI/USD ⭐ | 4.4866 | 64.68 | +0.11% | 5.43x | STRONG 87/100 | HIGH 55/100 | Watch |
| 3 | XDG/USD | 0.0545264 | 58.92 | +0.29% | 0.98x | MODERATE 59/100 | HIGH 62/100 | Watch |
| 4 | SKY/USD | 0.04429 | 54.47 | +0.18% | 8.45x | STRONG 72/100 | HIGH 60/100 | Watch |
| 5 | ETH/USD | 1623.95 | 51.92 | +0.12% | 0.43x | MODERATE 46/100 | VERY_HIGH 70/100 | Watch |
| 6 | DCR/USD | 10.241 | 51.49 | +0.34% | 2.67x | STRONG 76/100 | VERY_HIGH 73/100 | Watch |
| 7 | ALGO/USD | 0.07352 | 49.35 | +0.40% | 1.92x | STRONG 70/100 | HIGH 55/100 | Watch |
| 8 | DOT/USD | 0.6664 | 33.06 | +0.44% | 0.54x | MODERATE 47/100 | VERY_HIGH 75/100 | Watch |
| 9 | CC/USD | 0.07496 | 32.06 | +0.32% | 0.31x | MODERATE 46/100 | VERY_HIGH 75/100 | Watch |
| 10 | CT/USD | 0.1232 | 29.83 | +0.16% | 0.31x | WEAK 30/100 | VERY_HIGH 81/100 | Do nothing |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | VVV/USD ⭐ | 21.386 | 79.58 | +0.65% | 1.09x | 11641 | STRONG 85/100 | HIGH 62/100 | Watch |
| 2 | UNI/USD ⭐ | 4.4906 | 57.51 | +0.11% | 5.43x | 8992 | STRONG 84/100 | HIGH 55/100 | Watch |
| 3 | XBT/USD | 58934.8 | 55.11 | +0.08% | 1.07x | 227556 | MODERATE 53/100 | HIGH 62/100 | Watch |

**Same-run overlap:** VVV/USD, UNI/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
