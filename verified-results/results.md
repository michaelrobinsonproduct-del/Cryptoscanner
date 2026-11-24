# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-24T03:31:19.293472+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/45319877596
**Source SHA:** 858c8bc8ec5d7641ddb39cacd8aca91719f855b1
**Previous ledger commit:** 95c8110f2c391c2b7569d762cfecae5f3e19e0df (atomic ledger/results publication)
**Ledger generation:** 1519 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 4s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 628; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 610; valid market observations: 608; OHLC screened: 17.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | MON/USD | 0.01234 | 91.167 | 76.244 | +7.12% | +2.57% | 1.20x | 16.2 | 2026-11-24T03:31:14.876789+00:00 | Not calibrated | STRONG 76/100 | HIGH 68/100 | Watch | WATCH |
| 2 | XRP/USD | 0.94263 | 68.236 | 57.361 | +0.34% | +0.85% | 1.66x | 0.1 | 2026-11-24T03:31:14.876789+00:00 | Not calibrated | STRONG 79/100 | HIGH 55/100 | Watch | WATCH |
| 3 | AI/USD | 0.01592 | 62.185 | 56.560 | +4.53% | +1.80% | 0.66x | 12.6 | 2026-11-24T03:31:14.876789+00:00 | Not calibrated | MODERATE 56/100 | EXTREME 88/100 | Do nothing | WATCH |
| 4 | NIGHT/USD | 0.04861 | 58.768 | 52.030 | +0.96% | +0.12% | 1.61x | 8.2 | 2026-11-24T03:31:14.876789+00:00 | Not calibrated | MODERATE 64/100 | HIGH 55/100 | Watch | WATCH |
| 5 | XDC/USD | 0.02638 | 57.416 | 36.664 | +1.54% | +1.15% | 2.68x | 19.0 | 2026-11-24T03:31:14.876789+00:00 | Not calibrated | STRONG 79/100 | HIGH 66/100 | Watch | WATCH |
| 6 | PEPE/USD | 3.443e-06 | 54.203 | 49.058 | +0.61% | +1.29% | 0.87x | 8.7 | 2026-11-24T03:31:14.876789+00:00 | Not calibrated | MODERATE 57/100 | HIGH 62/100 | Watch | WATCH |
| 7 | BABY/USD | 0.00863 | 41.419 | 35.930 | +1.53% | +1.77% | 0.66x | 11.6 | 2026-11-24T03:31:14.876789+00:00 | Not calibrated | MODERATE 46/100 | EXTREME 88/100 | Do nothing | WATCH |
| 8 | BAT/USD | 0.07837 | 38.909 | 30.576 | +1.55% | +2.06% | 0.80x | 24.3 | 2026-11-24T03:31:14.876789+00:00 | Not calibrated | WEAK 39/100 | VERY_HIGH 79/100 | Watch | WATCH |
| 9 | XTZ/USD | 0.21489 | 30.161 | 29.172 | +0.95% | +0.67% | 0.77x | 16.8 | 2026-11-24T03:31:14.876789+00:00 | Not calibrated | WEAK 40/100 | VERY_HIGH 80/100 | Watch | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | MON/USD | 76.244 | 0.01234 | +2.57% | 1.20x |
| 2 | XRP/USD | 57.361 | 0.94263 | +0.85% | 1.66x |
| 3 | AI/USD | 56.560 | 0.01592 | +1.80% | 0.66x |
| 4 | NIGHT/USD | 52.030 | 0.04861 | +0.12% | 1.61x |
| 5 | PEPE/USD | 49.058 | 3.443e-06 | +1.29% | 0.87x |
| 6 | XDC/USD | 36.664 | 0.02638 | +1.15% | 2.68x |
| 7 | BABY/USD | 35.930 | 0.00863 | +1.77% | 0.66x |
| 8 | BAT/USD | 30.576 | 0.07837 | +2.06% | 0.80x |
| 9 | XTZ/USD | 29.172 | 0.21489 | +0.67% | 0.77x |

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

- Persisted scans: 1519; predictions: 12964; observations: 920169.
- Matured sampled outcomes across 1/6/24/48h: 24097; gap abstentions: 22370. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 135 (sampled only; not a success-rate estimate).
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

**Writer:** 45319877596 · **Generation:** 1519 · **Legacy run:** 45319877596
**Main quote time:** 2026-11-24T03:31:19.293472+00:00 · **Legacy report time:** 2026-11-24T03:32:16.646525+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | MON/USD ⭐ | 0.01234 | 91.17 | +2.57% | 1.20x | STRONG 86/100 | HIGH 68/100 | Watch |
| 2 | XRP/USD ⭐ | 0.94263 | 68.24 | +0.85% | 1.66x | STRONG 89/100 | HIGH 55/100 | Consider small entry |
| 3 | AI/USD | 0.01592 | 62.19 | +1.80% | 0.66x | MODERATE 56/100 | EXTREME 88/100 | Do nothing |
| 4 | NIGHT/USD ⭐ | 0.04861 | 58.77 | +0.12% | 1.61x | STRONG 74/100 | HIGH 55/100 | Watch |
| 5 | XDC/USD ⭐ | 0.02638 | 57.42 | +1.15% | 2.68x | STRONG 89/100 | HIGH 66/100 | Consider small entry |
| 6 | PEPE/USD | 3.443e-06 | 54.20 | +1.29% | 0.87x | MODERATE 57/100 | HIGH 62/100 | Watch |
| 7 | BABY/USD | 0.00863 | 41.42 | +1.77% | 0.66x | MODERATE 46/100 | EXTREME 88/100 | Do nothing |
| 8 | BAT/USD | 0.07837 | 38.91 | +2.06% | 0.80x | WEAK 39/100 | VERY_HIGH 79/100 | Watch |
| 9 | XTZ/USD | 0.21489 | 30.16 | +0.67% | 0.77x | WEAK 40/100 | VERY_HIGH 80/100 | Watch |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | MON/USD ⭐ | 0.01234 | 84.16 | +2.57% | 1.20x | 8157 | STRONG 82/100 | HIGH 68/100 | Watch |
| 2 | XRP/USD ⭐ | 0.94223 | 59.13 | +0.85% | 1.66x | 46764 | STRONG 85/100 | HIGH 55/100 | Consider small entry |
| 3 | XDC/USD ⭐ | 0.02638 | 53.89 | +1.15% | 2.68x | 4488 | STRONG 87/100 | HIGH 66/100 | Consider small entry |
| 4 | NIGHT/USD ⭐ | 0.04861 | 50.51 | +0.12% | 1.61x | 12038 | STRONG 70/100 | HIGH 55/100 | Watch |

**Same-run overlap:** MON/USD, XRP/USD, NIGHT/USD, XDC/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
