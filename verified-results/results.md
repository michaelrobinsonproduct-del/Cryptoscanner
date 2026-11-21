# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-21T17:10:55.899387+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/44928497973
**Source SHA:** 7ac7b40f8385b7b363a3015feba153e001ac4fc4
**Previous ledger commit:** 382b959abd337c98405308697a9f33681d013345 (atomic ledger/results publication)
**Ledger generation:** 1162 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 6s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 628; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 610; valid market observations: 608; OHLC screened: 24.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | UNI/USD | 4.7283 | 89.358 | 93.692 | +5.84% | -0.36% | 0.75x | 4.4 | 2026-11-21T17:10:49.401761+00:00 | Not calibrated | MODERATE 50/100 | VERY_HIGH 76/100 | Watch | WATCH |
| 2 | XMR/USD | 482.95 | 88.623 | 92.173 | +5.84% | +0.17% | 0.56x | 7.5 | 2026-11-21T17:10:49.401761+00:00 | Not calibrated | MODERATE 64/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 3 | NIGHT/USD | 0.04461 | 87.347 | 72.688 | +5.66% | +2.07% | 1.43x | 27.0 | 2026-11-21T17:10:49.401761+00:00 | Not calibrated | STRONG 79/100 | HIGH 67/100 | Watch | WATCH |
| 4 | SOL/USD | 70.68 | 85.099 | 74.362 | +2.87% | +0.06% | 2.05x | 1.4 | 2026-11-21T17:10:49.401761+00:00 | Not calibrated | STRONG 88/100 | HIGH 55/100 | Watch | WATCH |
| 5 | ETH/USD | 1683.91 | 83.547 | 82.891 | +3.99% | +0.10% | 1.02x | 0.1 | 2026-11-21T17:10:49.401761+00:00 | Not calibrated | MODERATE 67/100 | HIGH 62/100 | Watch | WATCH |
| 6 | ZEC/USD | 790.99 | 83.028 | 83.084 | +4.36% | +0.17% | 0.91x | 4.9 | 2026-11-21T17:10:49.401761+00:00 | Not calibrated | MODERATE 62/100 | HIGH 62/100 | Watch | WATCH |
| 7 | XBT/USD | 60104.9 | 79.296 | 70.448 | +2.21% | +0.14% | 1.81x | 0.0 | 2026-11-21T17:10:49.401761+00:00 | Not calibrated | STRONG 75/100 | HIGH 55/100 | Watch | WATCH |
| 8 | PAXG/USD | 3548 | 73.368 | 58.050 | +0.47% | +0.08% | 2.49x | 0.0 | 2026-11-21T17:10:49.401761+00:00 | Not calibrated | STRONG 82/100 | HIGH 55/100 | Watch | WATCH |
| 9 | TAO/USD | 185.7238 | 68.442 | 71.763 | +2.89% | -0.28% | 0.81x | 6.9 | 2026-11-21T17:10:49.401761+00:00 | Not calibrated | WEAK 39/100 | HIGH 68/100 | Watch | WATCH |
| 10 | BEAM/USD | 0.003548 | 65.272 | 68.523 | +8.24% | +0.50% | 0.42x | 16.9 | 2026-11-21T17:10:49.401761+00:00 | Not calibrated | MODERATE 58/100 | VERY_HIGH 81/100 | Watch | WATCH |
| 11 | XRP/USD | 0.93029 | 65.232 | 71.140 | +2.37% | +0.08% | 0.37x | 1.0 | 2026-11-21T17:10:49.401761+00:00 | Not calibrated | MODERATE 53/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 12 | CT/USD | 0.1326 | 64.166 | 68.969 | +9.50% | +0.08% | 0.48x | 15.1 | 2026-11-21T17:10:49.401761+00:00 | Not calibrated | MODERATE 47/100 | EXTREME 88/100 | Do nothing | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | UNI/USD | 93.692 | 4.7283 | -0.36% | 0.75x |
| 2 | XMR/USD | 92.173 | 482.95 | +0.17% | 0.56x |
| 3 | ZEC/USD | 83.084 | 790.99 | +0.17% | 0.91x |
| 4 | ETH/USD | 82.891 | 1683.91 | +0.10% | 1.02x |
| 5 | SOL/USD | 74.362 | 70.68 | +0.06% | 2.05x |
| 6 | NIGHT/USD | 72.688 | 0.04461 | +2.07% | 1.43x |
| 7 | TAO/USD | 71.763 | 185.7238 | -0.28% | 0.81x |
| 8 | XRP/USD | 71.140 | 0.93029 | +0.08% | 0.37x |
| 9 | XBT/USD | 70.448 | 60104.9 | +0.14% | 1.81x |
| 10 | CT/USD | 68.969 | 0.1326 | +0.08% | 0.48x |
| 11 | BEAM/USD | 68.523 | 0.003548 | +0.50% | 0.42x |
| 12 | PAXG/USD | 58.050 | 3548 | +0.08% | 2.49x |

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

- Persisted scans: 1162; predictions: 9253; observations: 702855.
- Matured sampled outcomes across 1/6/24/48h: 12176; gap abstentions: 20891. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 16 (sampled only; not a success-rate estimate).
- False positives / missed movers: NOT VERIFIED without eligible continuous outcome coverage.
- Baseline vs challenger: recorded as-of; unbiased held-out lift NOT MEASURED.
- Online Kraken /USD stablecoin-base pairs excluded: 18 (counted from this scan's online AssetPairs metadata, not inferred from price).
- Stablecoin base exclusions: BRL1, BUSD, DAI, EUR, EURC, EUROP, EURQ, EURR, EURT, FDUSD, FRAX, GUSD, PYUSD, QCAD, RLUSD, TGBP, TUSD, USD, USD1, USDC, USDD, USDE, USDG, USDQ, USDR, USDS, USDT, ZUSD.
- DEX: NOT USED; no DEX freshness gate.
- OHLC screening abstentions: 4; details in immutable scan JSON artifact.
- Storage: ledger and results published in one non-force Git commit and read back. Independent artifact recovery is NOT VERIFIED by this scan alone.
- Errors: none in successful committed scan; a failed workflow must not publish a SUCCESS report.

# Cryptoscanner — challenger and independent legacy-inspired WATCH

Paper only · risk is high or higher · 30%+ in 48h probability NOT CALIBRATED
Signal confidence 0–100 means setup strength only, NOT a win probability. Actions are research guidance; no trade authorization.

**Writer:** 44928497973 · **Generation:** 1162 · **Legacy run:** 44928497973
**Main quote time:** 2026-11-21T17:10:55.899387+00:00 · **Legacy report time:** 2026-11-21T17:11:48.417426+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | UNI/USD | 4.7283 | 89.36 | -0.36% | 0.75x | MODERATE 50/100 | VERY_HIGH 76/100 | Watch |
| 2 | XMR/USD | 482.95 | 88.62 | +0.17% | 0.56x | MODERATE 64/100 | VERY_HIGH 70/100 | Watch |
| 3 | NIGHT/USD ⭐ | 0.04461 | 87.35 | +2.07% | 1.43x | STRONG 89/100 | HIGH 67/100 | Watch |
| 4 | SOL/USD ⭐ | 70.68 | 85.10 | +0.06% | 2.05x | STRONG 98/100 | HIGH 55/100 | Watch |
| 5 | ETH/USD ⭐ | 1683.91 | 83.55 | +0.10% | 1.02x | STRONG 77/100 | HIGH 62/100 | Watch |
| 6 | ZEC/USD | 790.99 | 83.03 | +0.17% | 0.91x | MODERATE 62/100 | HIGH 62/100 | Watch |
| 7 | XBT/USD ⭐ | 60104.9 | 79.30 | +0.14% | 1.81x | STRONG 85/100 | HIGH 55/100 | Watch |
| 8 | PAXG/USD | 3548 | 73.37 | +0.08% | 2.49x | STRONG 82/100 | HIGH 55/100 | Watch |
| 9 | TAO/USD | 185.7238 | 68.44 | -0.28% | 0.81x | WEAK 39/100 | HIGH 68/100 | Watch |
| 10 | BEAM/USD | 0.003548 | 65.27 | +0.50% | 0.42x | MODERATE 58/100 | VERY_HIGH 81/100 | Watch |
| 11 | XRP/USD | 0.93029 | 65.23 | +0.08% | 0.37x | MODERATE 53/100 | VERY_HIGH 70/100 | Watch |
| 12 | CT/USD | 0.1326 | 64.17 | +0.08% | 0.48x | MODERATE 47/100 | EXTREME 88/100 | Do nothing |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | ETH/USD ⭐ | 1683.53 | 99.82 | +0.10% | 1.02x | 87253 | STRONG 85/100 | HIGH 62/100 | Watch |
| 2 | NIGHT/USD ⭐ | 0.0447 | 98.44 | +2.07% | 1.43x | 11094 | STRONG 100/100 | HIGH 55/100 | Watch |
| 3 | SOL/USD ⭐ | 70.71 | 88.45 | +0.06% | 2.05x | 52863 | STRONG 99/100 | HIGH 55/100 | Watch |
| 4 | XBT/USD ⭐ | 60080 | 81.64 | +0.14% | 1.81x | 247564 | STRONG 86/100 | HIGH 55/100 | Watch |

**Same-run overlap:** NIGHT/USD, SOL/USD, ETH/USD, XBT/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
