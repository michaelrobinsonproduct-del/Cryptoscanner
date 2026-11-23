# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-23T18:01:52.473161+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/45233552572
**Source SHA:** 858c8bc8ec5d7641ddb39cacd8aca91719f855b1
**Previous ledger commit:** fc140577467efb7468aa0a0a8c2d4156f3c4a35d (atomic ledger/results publication)
**Ledger generation:** 1463 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 9s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 628; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 610; valid market observations: 609; OHLC screened: 24.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | UNI/USD | 4.9415 | 104.108 | 85.933 | +5.56% | +0.64% | 3.19x | 7.9 | 2026-11-23T18:01:43.938816+00:00 | Not calibrated | STRONG 100/100 | HIGH 55/100 | Consider small entry | WATCH |
| 2 | INJ/USD | 6.651 | 103.436 | 95.697 | +6.79% | +0.17% | 1.69x | 4.5 | 2026-11-23T18:01:43.938816+00:00 | Not calibrated | STRONG 85/100 | HIGH 55/100 | Watch | WATCH |
| 3 | LTC/USD | 41.96 | 98.729 | 85.186 | +4.48% | +0.29% | 2.21x | 2.4 | 2026-11-23T18:01:43.938816+00:00 | Not calibrated | STRONG 100/100 | HIGH 55/100 | Consider small entry | WATCH |
| 4 | SUI/USD | 0.6898 | 93.244 | 89.954 | +5.20% | +0.32% | 1.17x | 2.9 | 2026-11-23T18:01:43.938816+00:00 | Not calibrated | STRONG 82/100 | HIGH 62/100 | Watch | WATCH |
| 5 | XDG/USD | 0.0573345 | 86.104 | 79.763 | +3.71% | +0.02% | 1.62x | 2.4 | 2026-11-23T18:01:43.938816+00:00 | Not calibrated | STRONG 78/100 | HIGH 55/100 | Watch | WATCH |
| 6 | CC/USD | 0.07852 | 85.703 | 78.966 | +7.17% | +0.41% | 1.47x | 5.1 | 2026-11-23T18:01:43.938816+00:00 | Not calibrated | STRONG 88/100 | HIGH 60/100 | Watch | WATCH |
| 7 | SOL/USD | 73.67 | 84.957 | 84.450 | +4.30% | +0.23% | 0.93x | 1.4 | 2026-11-23T18:01:43.938816+00:00 | Not calibrated | STRONG 72/100 | HIGH 62/100 | Watch | WATCH |
| 8 | XRP/USD | 0.9562 | 84.170 | 75.897 | +3.09% | +0.02% | 1.82x | 1.5 | 2026-11-23T18:01:43.938816+00:00 | Not calibrated | STRONG 77/100 | HIGH 55/100 | Watch | WATCH |
| 9 | HYPE/USD | 65.68 | 83.189 | 82.562 | +4.15% | -0.20% | 1.16x | 3.0 | 2026-11-23T18:01:43.938816+00:00 | Not calibrated | MODERATE 52/100 | HIGH 68/100 | Watch | WATCH |
| 10 | ADA/USD | 0.150463 | 80.769 | 79.886 | +4.05% | +0.27% | 0.95x | 7.0 | 2026-11-23T18:01:43.938816+00:00 | Not calibrated | STRONG 70/100 | HIGH 62/100 | Watch | WATCH |
| 11 | PAXG/USD | 3643.82 | 80.731 | 65.689 | +2.00% | +0.01% | 6.34x | 0.0 | 2026-11-23T18:01:43.938816+00:00 | Not calibrated | STRONG 85/100 | HIGH 55/100 | Watch | WATCH |
| 12 | XLM/USD | 0.131913 | 80.422 | 77.023 | +3.44% | +0.21% | 1.23x | 4.1 | 2026-11-23T18:01:43.938816+00:00 | Not calibrated | STRONG 75/100 | HIGH 62/100 | Watch | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | INJ/USD | 95.697 | 6.651 | +0.17% | 1.69x |
| 2 | SUI/USD | 89.954 | 0.6898 | +0.32% | 1.17x |
| 3 | UNI/USD | 85.933 | 4.9415 | +0.64% | 3.19x |
| 4 | LTC/USD | 85.186 | 41.96 | +0.29% | 2.21x |
| 5 | SOL/USD | 84.450 | 73.67 | +0.23% | 0.93x |
| 6 | HYPE/USD | 82.562 | 65.68 | -0.20% | 1.16x |
| 7 | ADA/USD | 79.886 | 0.150463 | +0.27% | 0.95x |
| 8 | XDG/USD | 79.763 | 0.0573345 | +0.02% | 1.62x |
| 9 | CC/USD | 78.966 | 0.07852 | +0.41% | 1.47x |
| 10 | XLM/USD | 77.023 | 0.131913 | +0.21% | 1.23x |
| 11 | XRP/USD | 75.897 | 0.9562 | +0.02% | 1.82x |
| 12 | PAXG/USD | 65.689 | 3643.82 | +0.01% | 6.34x |

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

- Persisted scans: 1463; predictions: 12323; observations: 886069.
- Matured sampled outcomes across 1/6/24/48h: 21568; gap abstentions: 22370. Per-horizon counts require independent audit; do not infer held-out lift.
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

**Writer:** 45233552572 · **Generation:** 1463 · **Legacy run:** 45233552572
**Main quote time:** 2026-11-23T18:01:52.473161+00:00 · **Legacy report time:** 2026-11-23T18:02:50.372248+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | UNI/USD ⭐ | 4.9415 | 104.11 | +0.64% | 3.19x | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 2 | INJ/USD ⭐ | 6.651 | 103.44 | +0.17% | 1.69x | STRONG 95/100 | HIGH 55/100 | Watch |
| 3 | LTC/USD ⭐ | 41.96 | 98.73 | +0.29% | 2.21x | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 4 | SUI/USD ⭐ | 0.6898 | 93.24 | +0.32% | 1.17x | STRONG 92/100 | HIGH 62/100 | Watch |
| 5 | XDG/USD | 0.0573345 | 86.10 | +0.02% | 1.62x | STRONG 78/100 | HIGH 55/100 | Watch |
| 6 | CC/USD | 0.07852 | 85.70 | +0.41% | 1.47x | STRONG 88/100 | HIGH 60/100 | Watch |
| 7 | SOL/USD | 73.67 | 84.96 | +0.23% | 0.93x | STRONG 72/100 | HIGH 62/100 | Watch |
| 8 | XRP/USD | 0.9562 | 84.17 | +0.02% | 1.82x | STRONG 77/100 | HIGH 55/100 | Watch |
| 9 | HYPE/USD | 65.68 | 83.19 | -0.20% | 1.16x | MODERATE 52/100 | HIGH 68/100 | Watch |
| 10 | ADA/USD | 0.150463 | 80.77 | +0.27% | 0.95x | STRONG 70/100 | HIGH 62/100 | Watch |
| 11 | PAXG/USD | 3643.82 | 80.73 | +0.01% | 6.34x | STRONG 85/100 | HIGH 55/100 | Watch |
| 12 | XLM/USD ⭐ | 0.131913 | 80.42 | +0.21% | 1.23x | STRONG 85/100 | HIGH 62/100 | Watch |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | LTC/USD ⭐ | 42.11 | 100.00 | +0.29% | 2.21x | 12611 | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 2 | XLM/USD ⭐ | 0.13212 | 96.63 | +0.21% | 1.23x | 18143 | STRONG 93/100 | HIGH 62/100 | Watch |
| 3 | UNI/USD ⭐ | 4.9541 | 96.19 | +0.64% | 3.19x | 9060 | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 4 | SUI/USD ⭐ | 0.6903 | 95.84 | +0.32% | 1.17x | 11392 | STRONG 93/100 | HIGH 62/100 | Watch |
| 5 | INJ/USD ⭐ | 6.652 | 93.06 | +0.17% | 1.69x | 8520 | STRONG 92/100 | HIGH 55/100 | Watch |
| 6 | ALGO/USD | 0.08518 | 89.76 | +0.51% | 5.05x | 8742 | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 7 | DOT/USD | 0.6909 | 88.58 | +0.12% | 1.67x | 8991 | STRONG 79/100 | HIGH 60/100 | Watch |
| 8 | PENGU/USD | 0.004548 | 84.68 | +0.15% | 1.17x | 4039 | MODERATE 67/100 | HIGH 67/100 | Watch |

**Same-run overlap:** UNI/USD, INJ/USD, LTC/USD, SUI/USD, XLM/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
