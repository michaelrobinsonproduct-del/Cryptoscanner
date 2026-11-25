# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-25T22:45:59.754004+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/45715792378
**Source SHA:** 858c8bc8ec5d7641ddb39cacd8aca91719f855b1
**Previous ledger commit:** 0436e580dd705e3eef7652524bf31e1bf1f0191d (atomic ledger/results publication)
**Ledger generation:** 1777 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 6s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 628; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 610; valid market observations: 609; OHLC screened: 24.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | PUMP/USD | 0.002549 | 93.199 | 71.028 | +4.51% | +1.43% | 4.93x | 7.9 | 2026-11-25T22:45:53.597691+00:00 | Not calibrated | STRONG 100/100 | HIGH 55/100 | Consider small entry | WATCH |
| 2 | NEAR/USD | 3.0221 | 82.832 | 87.565 | +4.77% | -0.62% | 0.84x | 1.7 | 2026-11-25T22:45:53.597691+00:00 | Not calibrated | MODERATE 46/100 | HIGH 68/100 | Watch | WATCH |
| 3 | LTC/USD | 42.37 | 78.418 | 79.866 | +3.72% | +0.07% | 0.82x | 2.4 | 2026-11-25T22:45:53.597691+00:00 | Not calibrated | MODERATE 59/100 | HIGH 62/100 | Watch | WATCH |
| 4 | HYPE/USD | 61.38 | 75.021 | 71.841 | +2.52% | +0.05% | 1.29x | 1.6 | 2026-11-25T22:45:53.597691+00:00 | Not calibrated | MODERATE 63/100 | HIGH 55/100 | Watch | WATCH |
| 5 | SUI/USD | 0.6624 | 71.620 | 70.353 | +2.30% | +0.11% | 1.07x | 1.5 | 2026-11-25T22:45:53.597691+00:00 | Not calibrated | MODERATE 61/100 | HIGH 62/100 | Watch | WATCH |
| 6 | SOL/USD | 70.42 | 69.367 | 62.537 | +1.18% | +0.07% | 1.65x | 1.4 | 2026-11-25T22:45:53.597691+00:00 | Not calibrated | STRONG 70/100 | HIGH 55/100 | Watch | WATCH |
| 7 | XRP/USD | 0.93697 | 66.610 | 65.072 | +1.45% | +0.19% | 1.06x | 0.1 | 2026-11-25T22:45:53.597691+00:00 | Not calibrated | MODERATE 58/100 | HIGH 62/100 | Watch | WATCH |
| 8 | ZEC/USD | 755.06 | 61.380 | 69.259 | +2.19% | -0.43% | 0.43x | 2.1 | 2026-11-25T22:45:53.597691+00:00 | Not calibrated | WEAK 36/100 | VERY_HIGH 76/100 | Watch | WATCH |
| 9 | XBT/USD | 60131.5 | 58.903 | 59.564 | +0.65% | +0.11% | 0.88x | 0.0 | 2026-11-25T22:45:53.597691+00:00 | Not calibrated | MODERATE 49/100 | HIGH 62/100 | Watch | WATCH |
| 10 | XDG/USD | 0.0558113 | 58.561 | 55.272 | +1.04% | -0.02% | 1.34x | 0.0 | 2026-11-25T22:45:53.597691+00:00 | Not calibrated | MODERATE 49/100 | HIGH 61/100 | Watch | WATCH |
| 11 | XMR/USD | 519.62 | 57.827 | 65.013 | +1.97% | +0.21% | 0.18x | 7.5 | 2026-11-25T22:45:53.597691+00:00 | Not calibrated | MODERATE 59/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 12 | PAXG/USD | 3579.69 | 55.937 | 61.730 | +1.07% | -0.02% | 0.43x | 1.5 | 2026-11-25T22:45:53.597691+00:00 | Not calibrated | WEAK 33/100 | VERY_HIGH 76/100 | Do nothing | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | NEAR/USD | 87.565 | 3.0221 | -0.62% | 0.84x |
| 2 | LTC/USD | 79.866 | 42.37 | +0.07% | 0.82x |
| 3 | HYPE/USD | 71.841 | 61.38 | +0.05% | 1.29x |
| 4 | PUMP/USD | 71.028 | 0.002549 | +1.43% | 4.93x |
| 5 | SUI/USD | 70.353 | 0.6624 | +0.11% | 1.07x |
| 6 | ZEC/USD | 69.259 | 755.06 | -0.43% | 0.43x |
| 7 | XRP/USD | 65.072 | 0.93697 | +0.19% | 1.06x |
| 8 | XMR/USD | 65.013 | 519.62 | +0.21% | 0.18x |
| 9 | SOL/USD | 62.537 | 70.42 | +0.07% | 1.65x |
| 10 | PAXG/USD | 61.730 | 3579.69 | -0.02% | 0.43x |
| 11 | XBT/USD | 59.564 | 60131.5 | +0.11% | 0.88x |
| 12 | XDG/USD | 55.272 | 0.0558113 | -0.02% | 1.34x |

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

- Persisted scans: 1777; predictions: 15068; observations: 1077237.
- Matured sampled outcomes across 1/6/24/48h: 32822; gap abstentions: 23298. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 146 (sampled only; not a success-rate estimate).
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

**Writer:** 45715792378 · **Generation:** 1777 · **Legacy run:** 45715792378
**Main quote time:** 2026-11-25T22:45:59.754004+00:00 · **Legacy report time:** 2026-11-25T22:47:15.675777+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | PUMP/USD ⭐ | 0.002549 | 93.20 | +1.43% | 4.93x | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 2 | NEAR/USD | 3.0221 | 82.83 | -0.62% | 0.84x | MODERATE 46/100 | HIGH 68/100 | Watch |
| 3 | LTC/USD | 42.37 | 78.42 | +0.07% | 0.82x | MODERATE 59/100 | HIGH 62/100 | Watch |
| 4 | HYPE/USD | 61.38 | 75.02 | +0.05% | 1.29x | MODERATE 63/100 | HIGH 55/100 | Watch |
| 5 | SUI/USD ⭐ | 0.6624 | 71.62 | +0.11% | 1.07x | STRONG 71/100 | HIGH 62/100 | Watch |
| 6 | SOL/USD | 70.42 | 69.37 | +0.07% | 1.65x | STRONG 70/100 | HIGH 55/100 | Watch |
| 7 | XRP/USD ⭐ | 0.93697 | 66.61 | +0.19% | 1.06x | MODERATE 68/100 | HIGH 62/100 | Watch |
| 8 | ZEC/USD | 755.06 | 61.38 | -0.43% | 0.43x | WEAK 36/100 | VERY_HIGH 76/100 | Watch |
| 9 | XBT/USD | 60131.5 | 58.90 | +0.11% | 0.88x | MODERATE 49/100 | HIGH 62/100 | Watch |
| 10 | XDG/USD | 0.0558113 | 58.56 | -0.02% | 1.34x | MODERATE 49/100 | HIGH 61/100 | Watch |
| 11 | XMR/USD | 519.62 | 57.83 | +0.21% | 0.18x | MODERATE 59/100 | VERY_HIGH 70/100 | Watch |
| 12 | PAXG/USD | 3579.69 | 55.94 | -0.02% | 0.43x | WEAK 33/100 | VERY_HIGH 76/100 | Do nothing |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | PUMP/USD ⭐ | 0.002554 | 97.52 | +1.43% | 4.93x | 6092 | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 2 | TON/USD | 0.965 | 78.73 | +0.73% | 11.61x | 2877 | STRONG 89/100 | HIGH 66/100 | Consider small entry |
| 3 | SUI/USD ⭐ | 0.6624 | 74.20 | +0.11% | 1.07x | 7480 | STRONG 72/100 | HIGH 62/100 | Watch |
| 4 | XRP/USD ⭐ | 0.93694 | 67.35 | +0.19% | 1.06x | 42332 | MODERATE 69/100 | HIGH 62/100 | Watch |

**Same-run overlap:** PUMP/USD, SUI/USD, XRP/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
