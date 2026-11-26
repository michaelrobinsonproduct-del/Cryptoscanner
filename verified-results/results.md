# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-26T13:01:13.509909+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/45824798774
**Source SHA:** 858c8bc8ec5d7641ddb39cacd8aca91719f855b1
**Previous ledger commit:** e013c95a16a6ded8aa3905b5feb748798a53a3e0 (atomic ledger/results publication)
**Ledger generation:** 1864 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 7s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 628; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 610; valid market observations: 588; OHLC screened: 24.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | QNT/USD | 150.34 | 85.324 | 72.908 | +3.83% | -0.52% | 12.48x | 5.3 | 2026-11-26T13:01:06.941833+00:00 | Not calibrated | STRONG 73/100 | HIGH 61/100 | Watch | WATCH |
| 2 | LTC/USD | 43.53 | 80.224 | 66.141 | +1.92% | -0.18% | 3.98x | 4.6 | 2026-11-26T13:01:06.941833+00:00 | Not calibrated | STRONG 70/100 | HIGH 61/100 | Watch | WATCH |
| 3 | SYRUP/USD | 0.07249 | 79.522 | 66.927 | +9.39% | +0.28% | 2.12x | 20.7 | 2026-11-26T13:01:06.941833+00:00 | Not calibrated | STRONG 85/100 | VERY_HIGH 72/100 | Watch | WATCH |
| 4 | PUMP/USD | 0.002648 | 70.036 | 61.247 | +2.76% | -0.56% | 2.16x | 7.6 | 2026-11-26T13:01:06.941833+00:00 | Not calibrated | MODERATE 65/100 | HIGH 61/100 | Watch | WATCH |
| 5 | SEI/USD | 0.03664 | 67.466 | 72.689 | +10.00% | -2.55% | 1.75x | 10.9 | 2026-11-26T13:01:06.941833+00:00 | Not calibrated | MODERATE 49/100 | VERY_HIGH 76/100 | Do nothing | WATCH |
| 6 | ADA/USD | 0.148731 | 63.956 | 67.974 | +2.03% | -0.28% | 0.74x | 2.5 | 2026-11-26T13:01:06.941833+00:00 | Not calibrated | WEAK 37/100 | VERY_HIGH 76/100 | Watch | WATCH |
| 7 | XDG/USD | 0.0566805 | 62.392 | 59.984 | +1.29% | -0.21% | 1.35x | 0.0 | 2026-11-26T13:01:06.941833+00:00 | Not calibrated | MODERATE 51/100 | HIGH 61/100 | Watch | WATCH |
| 8 | LINK/USD | 9.22682 | 60.068 | 69.104 | +2.02% | -0.06% | 0.13x | 0.0 | 2026-11-26T13:01:06.941833+00:00 | Not calibrated | WEAK 35/100 | VERY_HIGH 76/100 | Watch | WATCH |
| 9 | XBT/USD | 60754.1 | 58.655 | 59.462 | +0.64% | -0.14% | 0.99x | 0.0 | 2026-11-26T13:01:06.941833+00:00 | Not calibrated | WEAK 34/100 | HIGH 68/100 | Do nothing | WATCH |
| 10 | XRP/USD | 0.94944 | 58.510 | 64.574 | +1.38% | -0.19% | 0.49x | 0.1 | 2026-11-26T13:01:06.941833+00:00 | Not calibrated | WEAK 34/100 | VERY_HIGH 76/100 | Do nothing | WATCH |
| 11 | INJ/USD | 6.172 | 55.414 | 66.511 | +3.66% | -0.47% | 0.12x | 4.9 | 2026-11-26T13:01:06.941833+00:00 | Not calibrated | WEAK 33/100 | VERY_HIGH 76/100 | Do nothing | WATCH |
| 12 | SOL/USD | 70.87 | 53.875 | 59.068 | +0.68% | -0.07% | 0.52x | 1.4 | 2026-11-26T13:01:06.941833+00:00 | Not calibrated | WEAK 32/100 | VERY_HIGH 76/100 | Do nothing | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | QNT/USD | 72.908 | 150.34 | -0.52% | 12.48x |
| 2 | SEI/USD | 72.689 | 0.03664 | -2.55% | 1.75x |
| 3 | LINK/USD | 69.104 | 9.22682 | -0.06% | 0.13x |
| 4 | ADA/USD | 67.974 | 0.148731 | -0.28% | 0.74x |
| 5 | SYRUP/USD | 66.927 | 0.07249 | +0.28% | 2.12x |
| 6 | INJ/USD | 66.511 | 6.172 | -0.47% | 0.12x |
| 7 | LTC/USD | 66.141 | 43.53 | -0.18% | 3.98x |
| 8 | XRP/USD | 64.574 | 0.94944 | -0.19% | 0.49x |
| 9 | PUMP/USD | 61.247 | 0.002648 | -0.56% | 2.16x |
| 10 | XDG/USD | 59.984 | 0.0566805 | -0.21% | 1.35x |
| 11 | XBT/USD | 59.462 | 60754.1 | -0.14% | 0.99x |
| 12 | SOL/USD | 59.068 | 70.87 | -0.07% | 0.52x |

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

- Persisted scans: 1864; predictions: 16103; observations: 1129713.
- Matured sampled outcomes across 1/6/24/48h: 34826; gap abstentions: 24790. Per-horizon counts require independent audit; do not infer held-out lift.
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

**Writer:** 45824798774 · **Generation:** 1864 · **Legacy run:** 45824798774
**Main quote time:** 2026-11-26T13:01:13.509909+00:00 · **Legacy report time:** 2026-11-26T13:02:21.110522+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | QNT/USD | 150.34 | 85.32 | -0.52% | 12.48x | STRONG 73/100 | HIGH 61/100 | Watch |
| 2 | LTC/USD | 43.53 | 80.22 | -0.18% | 3.98x | STRONG 70/100 | HIGH 61/100 | Watch |
| 3 | SYRUP/USD ⭐ | 0.07249 | 79.52 | +0.28% | 2.12x | STRONG 95/100 | VERY_HIGH 72/100 | Watch |
| 4 | PUMP/USD | 0.002648 | 70.04 | -0.56% | 2.16x | MODERATE 65/100 | HIGH 61/100 | Watch |
| 5 | SEI/USD | 0.03664 | 67.47 | -2.55% | 1.75x | MODERATE 49/100 | VERY_HIGH 76/100 | Do nothing |
| 6 | ADA/USD | 0.148731 | 63.96 | -0.28% | 0.74x | WEAK 37/100 | VERY_HIGH 76/100 | Watch |
| 7 | XDG/USD | 0.0566805 | 62.39 | -0.21% | 1.35x | MODERATE 51/100 | HIGH 61/100 | Watch |
| 8 | LINK/USD | 9.22682 | 60.07 | -0.06% | 0.13x | WEAK 35/100 | VERY_HIGH 76/100 | Watch |
| 9 | XBT/USD | 60754.1 | 58.65 | -0.14% | 0.99x | WEAK 34/100 | HIGH 68/100 | Do nothing |
| 10 | XRP/USD | 0.94944 | 58.51 | -0.19% | 0.49x | WEAK 34/100 | VERY_HIGH 76/100 | Do nothing |
| 11 | INJ/USD | 6.172 | 55.41 | -0.47% | 0.12x | WEAK 33/100 | VERY_HIGH 76/100 | Do nothing |
| 12 | SOL/USD | 70.87 | 53.87 | -0.07% | 0.52x | WEAK 32/100 | VERY_HIGH 76/100 | Do nothing |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | SYRUP/USD ⭐ | 0.0725 | 76.69 | +0.28% | 2.12x | 3855 | STRONG 93/100 | VERY_HIGH 72/100 | Watch |

**Same-run overlap:** SYRUP/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
