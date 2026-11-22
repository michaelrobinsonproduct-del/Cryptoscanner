# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-22T20:01:09.787984+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/45063841472
**Source SHA:** 193371a597e6dbc5a6a884defbe9e1519a6a183a
**Previous ledger commit:** e4b1cf199b1258a246230cd3fbdb00bf58b3e4f2 (atomic ledger/results publication)
**Ledger generation:** 1329 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 7s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 628; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 610; valid market observations: 609; OHLC screened: 24.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | VVV/USD | 26.083 | 94.814 | 83.269 | +4.75% | -0.33% | 2.32x | 10.0 | 2026-11-22T20:01:03.136678+00:00 | Not calibrated | STRONG 77/100 | HIGH 61/100 | Watch | WATCH |
| 2 | NIGHT/USD | 0.04831 | 82.588 | 88.950 | +9.10% | +0.06% | 0.33x | 8.3 | 2026-11-22T20:01:03.136678+00:00 | Not calibrated | MODERATE 61/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 3 | HYPE/USD | 62.37 | 82.516 | 67.115 | +1.85% | +0.08% | 11.51x | 1.6 | 2026-11-22T20:01:03.136678+00:00 | Not calibrated | STRONG 86/100 | HIGH 55/100 | Watch | WATCH |
| 4 | NEAR/USD | 2.9793 | 78.329 | 76.212 | +3.22% | -0.36% | 1.39x | 2.7 | 2026-11-22T20:01:03.136678+00:00 | Not calibrated | MODERATE 59/100 | HIGH 61/100 | Watch | WATCH |
| 5 | PUMP/USD | 0.002576 | 75.800 | 81.939 | +9.90% | +0.08% | 0.35x | 7.8 | 2026-11-22T20:01:03.136678+00:00 | Not calibrated | MODERATE 58/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 6 | SUI/USD | 0.6553 | 63.170 | 62.769 | +1.24% | +0.00% | 1.04x | 1.5 | 2026-11-22T20:01:03.136678+00:00 | Not calibrated | MODERATE 57/100 | HIGH 62/100 | Watch | WATCH |
| 7 | ETH/USD | 1712.74 | 60.999 | 67.645 | +1.81% | +0.03% | 0.32x | 0.1 | 2026-11-22T20:01:03.136678+00:00 | Not calibrated | MODERATE 50/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 8 | XBT/USD | 60643.2 | 60.193 | 61.437 | +0.92% | -0.01% | 0.88x | 0.0 | 2026-11-22T20:01:03.136678+00:00 | Not calibrated | WEAK 35/100 | HIGH 68/100 | Watch | WATCH |
| 9 | PIEVERSE/USD | 3.6271 | 59.676 | 69.972 | +6.58% | -0.69% | 0.32x | 31.0 | 2026-11-22T20:01:03.136678+00:00 | Not calibrated | WEAK 25/100 | EXTREME 88/100 | Do nothing | WATCH |
| 10 | ZBCN/USD | 0.001835 | 56.483 | 64.864 | +6.25% | +0.00% | 0.16x | 27.3 | 2026-11-22T20:01:03.136678+00:00 | Not calibrated | WEAK 38/100 | EXTREME 87/100 | Do nothing | WATCH |
| 11 | ZEC/USD | 786.85 | 54.185 | 61.918 | +1.12% | -0.13% | 0.29x | 1.8 | 2026-11-22T20:01:03.136678+00:00 | Not calibrated | WEAK 32/100 | VERY_HIGH 76/100 | Do nothing | WATCH |
| 12 | LINK/USD | 8.78912 | 50.151 | 58.772 | +2.26% | -0.05% | 0.16x | 1.5 | 2026-11-22T20:01:03.136678+00:00 | Not calibrated | WEAK 30/100 | VERY_HIGH 76/100 | Do nothing | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | NIGHT/USD | 88.950 | 0.04831 | +0.06% | 0.33x |
| 2 | VVV/USD | 83.269 | 26.083 | -0.33% | 2.32x |
| 3 | PUMP/USD | 81.939 | 0.002576 | +0.08% | 0.35x |
| 4 | NEAR/USD | 76.212 | 2.9793 | -0.36% | 1.39x |
| 5 | PIEVERSE/USD | 69.972 | 3.6271 | -0.69% | 0.32x |
| 6 | ETH/USD | 67.645 | 1712.74 | +0.03% | 0.32x |
| 7 | HYPE/USD | 67.115 | 62.37 | +0.08% | 11.51x |
| 8 | ZBCN/USD | 64.864 | 0.001835 | +0.00% | 0.16x |
| 9 | SUI/USD | 62.769 | 0.6553 | +0.00% | 1.04x |
| 10 | ZEC/USD | 61.918 | 786.85 | -0.13% | 0.29x |
| 11 | XBT/USD | 61.437 | 60643.2 | -0.01% | 0.88x |
| 12 | LINK/USD | 58.772 | 8.78912 | -0.05% | 0.16x |

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

- Persisted scans: 1329; predictions: 10867; observations: 804469.
- Matured sampled outcomes across 1/6/24/48h: 16450; gap abstentions: 22344. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 61 (sampled only; not a success-rate estimate).
- False positives / missed movers: NOT VERIFIED without eligible continuous outcome coverage.
- Baseline vs challenger: recorded as-of; unbiased held-out lift NOT MEASURED.
- Online Kraken /USD stablecoin-base pairs excluded: 18 (counted from this scan's online AssetPairs metadata, not inferred from price).
- Stablecoin base exclusions: BRL1, BUSD, DAI, EUR, EURC, EUROP, EURQ, EURR, EURT, FDUSD, FRAX, GUSD, PYUSD, QCAD, RLUSD, TGBP, TUSD, USD, USD1, USDC, USDD, USDE, USDG, USDQ, USDR, USDS, USDT, ZUSD.
- DEX: NOT USED; no DEX freshness gate.
- OHLC screening abstentions: 9; details in immutable scan JSON artifact.
- Storage: ledger and results published in one non-force Git commit and read back. Independent artifact recovery is NOT VERIFIED by this scan alone.
- Errors: none in successful committed scan; a failed workflow must not publish a SUCCESS report.

# Cryptoscanner — challenger and independent legacy-inspired WATCH

Paper only · risk is high or higher · 30%+ in 48h probability NOT CALIBRATED
Signal confidence 0–100 means setup strength only, NOT a win probability. Actions are research guidance; no trade authorization.

**Writer:** 45063841472 · **Generation:** 1329 · **Legacy run:** 45063841472
**Main quote time:** 2026-11-22T20:01:09.787984+00:00 · **Legacy report time:** 2026-11-22T20:02:14.887294+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | VVV/USD | 26.083 | 94.81 | -0.33% | 2.32x | STRONG 77/100 | HIGH 61/100 | Watch |
| 2 | NIGHT/USD | 0.04831 | 82.59 | +0.06% | 0.33x | MODERATE 61/100 | VERY_HIGH 70/100 | Watch |
| 3 | HYPE/USD ⭐ | 62.37 | 82.52 | +0.08% | 11.51x | STRONG 96/100 | HIGH 55/100 | Watch |
| 4 | NEAR/USD | 2.9793 | 78.33 | -0.36% | 1.39x | MODERATE 59/100 | HIGH 61/100 | Watch |
| 5 | PUMP/USD | 0.002576 | 75.80 | +0.08% | 0.35x | MODERATE 58/100 | VERY_HIGH 70/100 | Watch |
| 6 | SUI/USD | 0.6553 | 63.17 | +0.00% | 1.04x | MODERATE 57/100 | HIGH 62/100 | Watch |
| 7 | ETH/USD | 1712.74 | 61.00 | +0.03% | 0.32x | MODERATE 50/100 | VERY_HIGH 70/100 | Watch |
| 8 | XBT/USD | 60643.2 | 60.19 | -0.01% | 0.88x | WEAK 35/100 | HIGH 68/100 | Watch |
| 9 | PIEVERSE/USD | 3.6271 | 59.68 | -0.69% | 0.32x | WEAK 25/100 | EXTREME 88/100 | Do nothing |
| 10 | ZBCN/USD | 0.001835 | 56.48 | +0.00% | 0.16x | WEAK 38/100 | EXTREME 87/100 | Do nothing |
| 11 | ZEC/USD | 786.85 | 54.18 | -0.13% | 0.29x | WEAK 32/100 | VERY_HIGH 76/100 | Do nothing |
| 12 | LINK/USD | 8.78912 | 50.15 | -0.05% | 0.16x | WEAK 30/100 | VERY_HIGH 76/100 | Do nothing |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | HYPE/USD ⭐ | 62.32 | 74.99 | +0.08% | 11.51x | 10134 | STRONG 92/100 | HIGH 55/100 | Watch |

**Same-run overlap:** HYPE/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
