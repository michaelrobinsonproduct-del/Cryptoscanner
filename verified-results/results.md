# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-22T18:01:23.309748+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/45052495560
**Source SHA:** 193371a597e6dbc5a6a884defbe9e1519a6a183a
**Previous ledger commit:** 636415eb7ec68ab8c10e132509720e873d737010 (atomic ledger/results publication)
**Ledger generation:** 1317 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 8s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 628; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 610; valid market observations: 609; OHLC screened: 24.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | PUMP/USD | 0.002553 | 87.844 | 82.532 | +8.92% | -0.82% | 1.94x | 7.8 | 2026-11-22T18:01:15.622284+00:00 | Not calibrated | MODERATE 64/100 | HIGH 61/100 | Watch | WATCH |
| 2 | DRV/USD | 0.36629 | 77.385 | 84.232 | +9.28% | -0.03% | 0.33x | 9.6 | 2026-11-22T18:01:15.622284+00:00 | Not calibrated | WEAK 44/100 | VERY_HIGH 76/100 | Watch | WATCH |
| 3 | HYPE/USD | 62.99 | 77.320 | 74.209 | +2.86% | +0.00% | 1.31x | 1.6 | 2026-11-22T18:01:15.622284+00:00 | Not calibrated | STRONG 74/100 | HIGH 55/100 | Watch | WATCH |
| 4 | NEAR/USD | 3.0027 | 75.997 | 81.399 | +4.03% | -0.14% | 0.53x | 3.7 | 2026-11-22T18:01:15.622284+00:00 | Not calibrated | WEAK 43/100 | VERY_HIGH 76/100 | Watch | WATCH |
| 5 | PIEVERSE/USD | 3.6717 | 73.657 | 70.521 | +7.89% | +1.36% | 0.63x | 30.2 | 2026-11-22T18:01:15.622284+00:00 | Not calibrated | MODERATE 57/100 | VERY_HIGH 82/100 | Watch | WATCH |
| 6 | ZEC/USD | 795.63 | 70.688 | 68.695 | +2.24% | -0.30% | 1.35x | 4.0 | 2026-11-22T18:01:15.622284+00:00 | Not calibrated | MODERATE 55/100 | HIGH 61/100 | Watch | WATCH |
| 7 | AVAX/USD | 6.671 | 67.230 | 52.305 | +1.65% | -0.01% | 4.41x | 1.5 | 2026-11-22T18:01:15.622284+00:00 | Not calibrated | MODERATE 64/100 | HIGH 61/100 | Watch | WATCH |
| 8 | AERO/USD | 0.4236 | 63.543 | 66.506 | +6.30% | -0.73% | 1.07x | 18.9 | 2026-11-22T18:01:15.622284+00:00 | Not calibrated | WEAK 37/100 | VERY_HIGH 79/100 | Watch | WATCH |
| 9 | VVV/USD | 25.483 | 62.783 | 68.451 | +2.34% | +0.10% | 0.38x | 5.9 | 2026-11-22T18:01:15.622284+00:00 | Not calibrated | MODERATE 51/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 10 | ETH/USD | 1712.26 | 59.622 | 67.445 | +1.78% | -0.10% | 0.27x | 0.1 | 2026-11-22T18:01:15.622284+00:00 | Not calibrated | WEAK 35/100 | VERY_HIGH 76/100 | Watch | WATCH |
| 11 | STBL/USD | 0.016993 | 56.704 | 65.340 | +6.18% | -0.19% | 0.23x | 17.7 | 2026-11-22T18:01:15.622284+00:00 | Not calibrated | WEAK 28/100 | EXTREME 94/100 | Do nothing | WATCH |
| 12 | XBT/USD | 60732.2 | 55.434 | 61.824 | +1.07% | -0.16% | 0.44x | 1.3 | 2026-11-22T18:01:15.622284+00:00 | Not calibrated | WEAK 33/100 | VERY_HIGH 76/100 | Do nothing | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | DRV/USD | 84.232 | 0.36629 | -0.03% | 0.33x |
| 2 | PUMP/USD | 82.532 | 0.002553 | -0.82% | 1.94x |
| 3 | NEAR/USD | 81.399 | 3.0027 | -0.14% | 0.53x |
| 4 | HYPE/USD | 74.209 | 62.99 | +0.00% | 1.31x |
| 5 | PIEVERSE/USD | 70.521 | 3.6717 | +1.36% | 0.63x |
| 6 | ZEC/USD | 68.695 | 795.63 | -0.30% | 1.35x |
| 7 | VVV/USD | 68.451 | 25.483 | +0.10% | 0.38x |
| 8 | ETH/USD | 67.445 | 1712.26 | -0.10% | 0.27x |
| 9 | AERO/USD | 66.506 | 0.4236 | -0.73% | 1.07x |
| 10 | STBL/USD | 65.340 | 0.016993 | -0.19% | 0.23x |
| 11 | XBT/USD | 61.824 | 60732.2 | -0.16% | 0.44x |
| 12 | AVAX/USD | 52.305 | 6.671 | -0.01% | 4.41x |

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

- Persisted scans: 1317; predictions: 10723; observations: 797161.
- Matured sampled outcomes across 1/6/24/48h: 15994; gap abstentions: 22334. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 61 (sampled only; not a success-rate estimate).
- False positives / missed movers: NOT VERIFIED without eligible continuous outcome coverage.
- Baseline vs challenger: recorded as-of; unbiased held-out lift NOT MEASURED.
- Online Kraken /USD stablecoin-base pairs excluded: 18 (counted from this scan's online AssetPairs metadata, not inferred from price).
- Stablecoin base exclusions: BRL1, BUSD, DAI, EUR, EURC, EUROP, EURQ, EURR, EURT, FDUSD, FRAX, GUSD, PYUSD, QCAD, RLUSD, TGBP, TUSD, USD, USD1, USDC, USDD, USDE, USDG, USDQ, USDR, USDS, USDT, ZUSD.
- DEX: NOT USED; no DEX freshness gate.
- OHLC screening abstentions: 6; details in immutable scan JSON artifact.
- Storage: ledger and results published in one non-force Git commit and read back. Independent artifact recovery is NOT VERIFIED by this scan alone.
- Errors: none in successful committed scan; a failed workflow must not publish a SUCCESS report.

# Cryptoscanner — challenger and independent legacy-inspired WATCH

Paper only · risk is high or higher · 30%+ in 48h probability NOT CALIBRATED
Signal confidence 0–100 means setup strength only, NOT a win probability. Actions are research guidance; no trade authorization.

**Writer:** 45052495560 · **Generation:** 1317 · **Legacy run:** 45052495560
**Main quote time:** 2026-11-22T18:01:23.309748+00:00 · **Legacy report time:** 2026-11-22T18:02:28.933153+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | PUMP/USD | 0.002553 | 87.84 | -0.82% | 1.94x | MODERATE 64/100 | HIGH 61/100 | Watch |
| 2 | DRV/USD | 0.36629 | 77.38 | -0.03% | 0.33x | WEAK 44/100 | VERY_HIGH 76/100 | Watch |
| 3 | HYPE/USD | 62.99 | 77.32 | +0.00% | 1.31x | STRONG 74/100 | HIGH 55/100 | Watch |
| 4 | NEAR/USD | 3.0027 | 76.00 | -0.14% | 0.53x | WEAK 43/100 | VERY_HIGH 76/100 | Watch |
| 5 | PIEVERSE/USD | 3.6717 | 73.66 | +1.36% | 0.63x | MODERATE 57/100 | VERY_HIGH 82/100 | Watch |
| 6 | ZEC/USD | 795.63 | 70.69 | -0.30% | 1.35x | MODERATE 55/100 | HIGH 61/100 | Watch |
| 7 | AVAX/USD | 6.671 | 67.23 | -0.01% | 4.41x | MODERATE 64/100 | HIGH 61/100 | Watch |
| 8 | AERO/USD | 0.4236 | 63.54 | -0.73% | 1.07x | WEAK 37/100 | VERY_HIGH 79/100 | Watch |
| 9 | VVV/USD | 25.483 | 62.78 | +0.10% | 0.38x | MODERATE 51/100 | VERY_HIGH 70/100 | Watch |
| 10 | ETH/USD | 1712.26 | 59.62 | -0.10% | 0.27x | WEAK 35/100 | VERY_HIGH 76/100 | Watch |
| 11 | STBL/USD | 0.016993 | 56.70 | -0.19% | 0.23x | WEAK 28/100 | EXTREME 94/100 | Do nothing |
| 12 | XBT/USD | 60732.2 | 55.43 | -0.16% | 0.44x | WEAK 33/100 | VERY_HIGH 76/100 | Do nothing |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | NIGHT/USD | 0.04996 | 83.59 | +0.34% | 1.32x | 10022 | STRONG 82/100 | HIGH 61/100 | Watch |

**Same-run overlap:** None
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
