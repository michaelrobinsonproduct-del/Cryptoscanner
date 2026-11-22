# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-22T23:31:14.425189+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/45083523121
**Source SHA:** 193371a597e6dbc5a6a884defbe9e1519a6a183a
**Previous ledger commit:** f3922b6e0f79b74887ebdc506ad654b0852c7a8a (atomic ledger/results publication)
**Ledger generation:** 1350 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 6s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 628; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 610; valid market observations: 609; OHLC screened: 24.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | VVV/USD | 26.451 | 110.656 | 91.433 | +6.23% | +0.84% | 4.95x | 11.4 | 2026-11-22T23:31:08.340244+00:00 | Not calibrated | STRONG 100/100 | HIGH 61/100 | Consider small entry | WATCH |
| 2 | PUMP/USD | 0.002568 | 89.400 | 80.964 | +9.56% | +0.16% | 1.77x | 11.7 | 2026-11-22T23:31:08.340244+00:00 | Not calibrated | STRONG 75/100 | HIGH 61/100 | Watch | WATCH |
| 3 | PIEVERSE/USD | 3.6966 | 85.492 | 79.902 | +8.62% | +1.00% | 1.06x | 11.7 | 2026-11-22T23:31:08.340244+00:00 | Not calibrated | STRONG 73/100 | HIGH 68/100 | Watch | WATCH |
| 4 | ZEC/USD | 794.79 | 83.518 | 66.047 | +2.14% | +0.49% | 4.13x | 7.8 | 2026-11-22T23:31:08.340244+00:00 | Not calibrated | STRONG 97/100 | HIGH 55/100 | Consider small entry | WATCH |
| 5 | XBT/USD | 61080.7 | 79.680 | 66.534 | +1.65% | +0.09% | 2.27x | 0.0 | 2026-11-22T23:31:08.340244+00:00 | Not calibrated | STRONG 85/100 | HIGH 55/100 | Watch | WATCH |
| 6 | NEAR/USD | 2.9793 | 75.641 | 75.539 | +3.22% | +0.21% | 0.91x | 4.0 | 2026-11-22T23:31:08.340244+00:00 | Not calibrated | MODERATE 68/100 | HIGH 62/100 | Watch | WATCH |
| 7 | DRV/USD | 0.36897 | 73.674 | 80.894 | +10.07% | -0.03% | 0.29x | 15.7 | 2026-11-22T23:31:08.340244+00:00 | Not calibrated | WEAK 37/100 | VERY_HIGH 82/100 | Watch | WATCH |
| 8 | SUI/USD | 0.6551 | 68.895 | 62.671 | +1.21% | +0.17% | 1.54x | 1.5 | 2026-11-22T23:31:08.340244+00:00 | Not calibrated | MODERATE 69/100 | HIGH 55/100 | Watch | WATCH |
| 9 | ETH/USD | 1721.67 | 67.781 | 71.361 | +2.34% | +0.18% | 0.55x | 0.1 | 2026-11-22T23:31:08.340244+00:00 | Not calibrated | MODERATE 54/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 10 | HYPE/USD | 62.77 | 65.559 | 70.894 | +2.50% | +0.06% | 0.43x | 3.2 | 2026-11-22T23:31:08.340244+00:00 | Not calibrated | MODERATE 53/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 11 | BNB/USD | 558.32 | 61.419 | 50.393 | +1.99% | +0.20% | 2.00x | 1.6 | 2026-11-22T23:31:08.340244+00:00 | Not calibrated | STRONG 86/100 | HIGH 55/100 | Watch | WATCH |
| 12 | XMR/USD | 494.99 | 59.067 | 59.439 | +0.65% | -0.07% | 1.00x | 0.2 | 2026-11-22T23:31:08.340244+00:00 | Not calibrated | WEAK 35/100 | HIGH 68/100 | Watch | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | VVV/USD | 91.433 | 26.451 | +0.84% | 4.95x |
| 2 | PUMP/USD | 80.964 | 0.002568 | +0.16% | 1.77x |
| 3 | DRV/USD | 80.894 | 0.36897 | -0.03% | 0.29x |
| 4 | PIEVERSE/USD | 79.902 | 3.6966 | +1.00% | 1.06x |
| 5 | NEAR/USD | 75.539 | 2.9793 | +0.21% | 0.91x |
| 6 | ETH/USD | 71.361 | 1721.67 | +0.18% | 0.55x |
| 7 | HYPE/USD | 70.894 | 62.77 | +0.06% | 0.43x |
| 8 | XBT/USD | 66.534 | 61080.7 | +0.09% | 2.27x |
| 9 | ZEC/USD | 66.047 | 794.79 | +0.49% | 4.13x |
| 10 | SUI/USD | 62.671 | 0.6551 | +0.17% | 1.54x |
| 11 | XMR/USD | 59.439 | 494.99 | -0.07% | 1.00x |
| 12 | BNB/USD | 50.393 | 558.32 | +0.20% | 2.00x |

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

- Persisted scans: 1350; predictions: 11119; observations: 817257.
- Matured sampled outcomes across 1/6/24/48h: 17231; gap abstentions: 22370. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 62 (sampled only; not a success-rate estimate).
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

**Writer:** 45083523121 · **Generation:** 1350 · **Legacy run:** 45083523121
**Main quote time:** 2026-11-22T23:31:14.425189+00:00 · **Legacy report time:** 2026-11-22T23:32:01.748212+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | VVV/USD ⭐ | 26.451 | 110.66 | +0.84% | 4.95x | STRONG 100/100 | HIGH 61/100 | Consider small entry |
| 2 | PUMP/USD ⭐ | 0.002568 | 89.40 | +0.16% | 1.77x | STRONG 85/100 | HIGH 61/100 | Watch |
| 3 | PIEVERSE/USD ⭐ | 3.6966 | 85.49 | +1.00% | 1.06x | STRONG 83/100 | HIGH 68/100 | Watch |
| 4 | ZEC/USD ⭐ | 794.79 | 83.52 | +0.49% | 4.13x | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 5 | XBT/USD ⭐ | 61080.7 | 79.68 | +0.09% | 2.27x | STRONG 95/100 | HIGH 55/100 | Watch |
| 6 | NEAR/USD | 2.9793 | 75.64 | +0.21% | 0.91x | MODERATE 68/100 | HIGH 62/100 | Watch |
| 7 | DRV/USD | 0.36897 | 73.67 | -0.03% | 0.29x | WEAK 37/100 | VERY_HIGH 82/100 | Watch |
| 8 | SUI/USD | 0.6551 | 68.89 | +0.17% | 1.54x | MODERATE 69/100 | HIGH 55/100 | Watch |
| 9 | ETH/USD | 1721.67 | 67.78 | +0.18% | 0.55x | MODERATE 54/100 | VERY_HIGH 70/100 | Watch |
| 10 | HYPE/USD | 62.77 | 65.56 | +0.06% | 0.43x | MODERATE 53/100 | VERY_HIGH 70/100 | Watch |
| 11 | BNB/USD | 558.32 | 61.42 | +0.20% | 2.00x | STRONG 86/100 | HIGH 55/100 | Watch |
| 12 | XMR/USD | 494.99 | 59.07 | -0.07% | 1.00x | WEAK 35/100 | HIGH 68/100 | Watch |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | VVV/USD ⭐ | 26.374 | 99.75 | +0.84% | 4.95x | 11543 | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 2 | PUMP/USD ⭐ | 0.002571 | 80.63 | +0.16% | 1.77x | 4349 | STRONG 85/100 | HIGH 55/100 | Watch |
| 3 | ZEC/USD ⭐ | 794.59 | 79.76 | +0.49% | 4.13x | 18186 | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 4 | PIEVERSE/USD ⭐ | 3.6966 | 79.68 | +1.00% | 1.06x | 5876 | STRONG 80/100 | HIGH 68/100 | Watch |
| 5 | XBT/USD ⭐ | 61109.4 | 77.67 | +0.09% | 2.27x | 130813 | STRONG 94/100 | HIGH 55/100 | Watch |

**Same-run overlap:** VVV/USD, PUMP/USD, PIEVERSE/USD, ZEC/USD, XBT/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
