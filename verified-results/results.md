# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-23T19:11:42.853612+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/45245970159
**Source SHA:** 858c8bc8ec5d7641ddb39cacd8aca91719f855b1
**Previous ledger commit:** e52f666cf3877d369a9155db98b857d05c3dc519 (atomic ledger/results publication)
**Ledger generation:** 1470 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 6s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 628; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 610; valid market observations: 609; OHLC screened: 24.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | XMR/USD | 512 | 100.454 | 80.150 | +3.70% | +1.19% | 2.44x | 1.6 | 2026-11-23T19:11:36.991593+00:00 | Not calibrated | STRONG 100/100 | HIGH 55/100 | Consider small entry | WATCH |
| 2 | UNI/USD | 4.9161 | 100.255 | 84.565 | +5.02% | +0.14% | 4.11x | 5.1 | 2026-11-23T19:11:36.991593+00:00 | Not calibrated | STRONG 95/100 | HIGH 55/100 | Watch | WATCH |
| 3 | INJ/USD | 6.642 | 97.925 | 95.994 | +6.65% | +0.68% | 0.85x | 4.5 | 2026-11-23T19:11:36.991593+00:00 | Not calibrated | STRONG 79/100 | HIGH 62/100 | Watch | WATCH |
| 4 | ALGO/USD | 0.08342 | 93.573 | 88.261 | +10.59% | -0.54% | 1.80x | 7.2 | 2026-11-23T19:11:36.991593+00:00 | Not calibrated | MODERATE 67/100 | HIGH 61/100 | Watch | WATCH |
| 5 | SOL/USD | 73.2 | 91.908 | 79.788 | +3.64% | +0.11% | 2.16x | 1.4 | 2026-11-23T19:11:36.991593+00:00 | Not calibrated | STRONG 91/100 | HIGH 55/100 | Watch | WATCH |
| 6 | LTC/USD | 41.78 | 83.697 | 80.844 | +4.03% | +0.12% | 1.23x | 4.8 | 2026-11-23T19:11:36.991593+00:00 | Not calibrated | MODERATE 67/100 | HIGH 62/100 | Watch | WATCH |
| 7 | XDG/USD | 0.0571073 | 80.417 | 77.704 | +3.30% | +0.13% | 1.21x | 0.8 | 2026-11-23T19:11:36.991593+00:00 | Not calibrated | MODERATE 65/100 | HIGH 62/100 | Watch | WATCH |
| 8 | ADA/USD | 0.149717 | 78.053 | 78.019 | +3.54% | +0.05% | 0.98x | 3.5 | 2026-11-23T19:11:36.991593+00:00 | Not calibrated | MODERATE 59/100 | HIGH 62/100 | Watch | WATCH |
| 9 | SUI/USD | 0.6827 | 74.589 | 82.359 | +4.12% | +0.07% | 0.19x | 2.9 | 2026-11-23T19:11:36.991593+00:00 | Not calibrated | MODERATE 57/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 10 | CC/USD | 0.0784 | 73.994 | 77.719 | +7.00% | +0.44% | 0.41x | 7.7 | 2026-11-23T19:11:36.991593+00:00 | Not calibrated | MODERATE 67/100 | VERY_HIGH 75/100 | Watch | WATCH |
| 11 | HYPE/USD | 65.03 | 69.517 | 75.330 | +3.12% | -0.27% | 0.56x | 3.1 | 2026-11-23T19:11:36.991593+00:00 | Not calibrated | WEAK 40/100 | VERY_HIGH 76/100 | Watch | WATCH |
| 12 | ZEC/USD | 815.51 | 68.160 | 70.738 | +2.26% | +0.39% | 0.55x | 0.1 | 2026-11-23T19:11:36.991593+00:00 | Not calibrated | MODERATE 64/100 | VERY_HIGH 70/100 | Watch | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | INJ/USD | 95.994 | 6.642 | +0.68% | 0.85x |
| 2 | ALGO/USD | 88.261 | 0.08342 | -0.54% | 1.80x |
| 3 | UNI/USD | 84.565 | 4.9161 | +0.14% | 4.11x |
| 4 | SUI/USD | 82.359 | 0.6827 | +0.07% | 0.19x |
| 5 | LTC/USD | 80.844 | 41.78 | +0.12% | 1.23x |
| 6 | XMR/USD | 80.150 | 512 | +1.19% | 2.44x |
| 7 | SOL/USD | 79.788 | 73.2 | +0.11% | 2.16x |
| 8 | ADA/USD | 78.019 | 0.149717 | +0.05% | 0.98x |
| 9 | CC/USD | 77.719 | 0.0784 | +0.44% | 0.41x |
| 10 | XDG/USD | 77.704 | 0.0571073 | +0.13% | 1.21x |
| 11 | HYPE/USD | 75.330 | 65.03 | -0.27% | 0.56x |
| 12 | ZEC/USD | 70.738 | 815.51 | +0.39% | 0.55x |

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

- Persisted scans: 1470; predictions: 12407; observations: 890332.
- Matured sampled outcomes across 1/6/24/48h: 21904; gap abstentions: 22370. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 131 (sampled only; not a success-rate estimate).
- False positives / missed movers: NOT VERIFIED without eligible continuous outcome coverage.
- Baseline vs challenger: recorded as-of; unbiased held-out lift NOT MEASURED.
- Online Kraken /USD stablecoin-base pairs excluded: 18 (counted from this scan's online AssetPairs metadata, not inferred from price).
- Stablecoin base exclusions: BRL1, BUSD, DAI, EUR, EURC, EUROP, EURQ, EURR, EURT, FDUSD, FRAX, GUSD, PYUSD, QCAD, RLUSD, TGBP, TUSD, USD, USD1, USDC, USDD, USDE, USDG, USDQ, USDR, USDS, USDT, ZUSD.
- DEX: NOT USED; no DEX freshness gate.
- OHLC screening abstentions: 3; details in immutable scan JSON artifact.
- Storage: ledger and results published in one non-force Git commit and read back. Independent artifact recovery is NOT VERIFIED by this scan alone.
- Errors: none in successful committed scan; a failed workflow must not publish a SUCCESS report.

# Cryptoscanner — challenger and independent legacy-inspired WATCH

Paper only · risk is high or higher · 30%+ in 48h probability NOT CALIBRATED
Signal confidence 0–100 means setup strength only, NOT a win probability. Actions are research guidance; no trade authorization.

**Writer:** 45245970159 · **Generation:** 1470 · **Legacy run:** 45245970159
**Main quote time:** 2026-11-23T19:11:42.853612+00:00 · **Legacy report time:** 2026-11-23T19:12:51.545705+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | XMR/USD ⭐ | 512 | 100.45 | +1.19% | 2.44x | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 2 | UNI/USD ⭐ | 4.9161 | 100.25 | +0.14% | 4.11x | STRONG 100/100 | HIGH 55/100 | Watch |
| 3 | INJ/USD | 6.642 | 97.92 | +0.68% | 0.85x | STRONG 79/100 | HIGH 62/100 | Watch |
| 4 | ALGO/USD | 0.08342 | 93.57 | -0.54% | 1.80x | MODERATE 67/100 | HIGH 61/100 | Watch |
| 5 | SOL/USD ⭐ | 73.2 | 91.91 | +0.11% | 2.16x | STRONG 100/100 | HIGH 55/100 | Watch |
| 6 | LTC/USD ⭐ | 41.78 | 83.70 | +0.12% | 1.23x | STRONG 77/100 | HIGH 62/100 | Watch |
| 7 | XDG/USD ⭐ | 0.0571073 | 80.42 | +0.13% | 1.21x | STRONG 75/100 | HIGH 62/100 | Watch |
| 8 | ADA/USD | 0.149717 | 78.05 | +0.05% | 0.98x | MODERATE 59/100 | HIGH 62/100 | Watch |
| 9 | SUI/USD | 0.6827 | 74.59 | +0.07% | 0.19x | MODERATE 57/100 | VERY_HIGH 70/100 | Watch |
| 10 | CC/USD | 0.0784 | 73.99 | +0.44% | 0.41x | MODERATE 67/100 | VERY_HIGH 75/100 | Watch |
| 11 | HYPE/USD | 65.03 | 69.52 | -0.27% | 0.56x | WEAK 40/100 | VERY_HIGH 76/100 | Watch |
| 12 | ZEC/USD | 815.51 | 68.16 | +0.39% | 0.55x | MODERATE 64/100 | VERY_HIGH 70/100 | Watch |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | SOL/USD ⭐ | 73.31 | 99.76 | +0.11% | 2.16x | 44528 | STRONG 100/100 | HIGH 55/100 | Watch |
| 2 | UNI/USD ⭐ | 4.9131 | 97.26 | +0.14% | 4.11x | 9322 | STRONG 100/100 | HIGH 55/100 | Watch |
| 3 | XMR/USD ⭐ | 512.39 | 94.61 | +1.19% | 2.44x | 10115 | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 4 | LTC/USD ⭐ | 41.84 | 91.70 | +0.12% | 1.23x | 12532 | STRONG 81/100 | HIGH 62/100 | Watch |
| 5 | XDG/USD ⭐ | 0.0571056 | 91.61 | +0.13% | 1.21x | 9394 | STRONG 81/100 | HIGH 62/100 | Watch |
| 6 | PEPE/USD | 3.507e-06 | 90.47 | +0.40% | 2.70x | 7951 | STRONG 100/100 | HIGH 55/100 | Consider small entry |

**Same-run overlap:** XMR/USD, UNI/USD, SOL/USD, LTC/USD, XDG/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
