# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-27T08:42:01.422511+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/45967373684
**Source SHA:** 858c8bc8ec5d7641ddb39cacd8aca91719f855b1
**Previous ledger commit:** a6d8d77d9bd879e35c5b305f63335af88cd750c3 (atomic ledger/results publication)
**Ledger generation:** 1984 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 8s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 628; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 610; valid market observations: 603; OHLC screened: 24.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | ZEC/USD | 745.9 | 90.718 | 97.920 | +9.42% | -0.53% | 0.54x | 4.2 | 2026-11-27T08:41:53.496593+00:00 | Not calibrated | MODERATE 50/100 | VERY_HIGH 76/100 | Watch | WATCH |
| 2 | HYPE/USD | 65.58 | 87.839 | 91.276 | +5.40% | -0.30% | 0.81x | 3.1 | 2026-11-27T08:41:53.496593+00:00 | Not calibrated | MODERATE 49/100 | HIGH 68/100 | Watch | WATCH |
| 3 | INJ/USD | 6.501 | 85.403 | 69.787 | +4.99% | +0.12% | 3.24x | 6.1 | 2026-11-27T08:41:53.496593+00:00 | Not calibrated | STRONG 88/100 | HIGH 55/100 | Watch | WATCH |
| 4 | ADA/USD | 0.152891 | 84.762 | 71.884 | +2.98% | -0.42% | 3.64x | 2.0 | 2026-11-27T08:41:53.496593+00:00 | Not calibrated | STRONG 72/100 | HIGH 61/100 | Watch | WATCH |
| 5 | XBT/USD | 61675.5 | 81.466 | 68.616 | +1.95% | -0.40% | 2.49x | 0.0 | 2026-11-27T08:41:53.496593+00:00 | Not calibrated | STRONG 71/100 | HIGH 61/100 | Watch | WATCH |
| 6 | SUI/USD | 0.6865 | 80.455 | 73.253 | +2.82% | -0.47% | 1.95x | 2.9 | 2026-11-27T08:41:53.496593+00:00 | Not calibrated | MODERATE 60/100 | HIGH 61/100 | Watch | WATCH |
| 7 | XRP/USD | 0.97864 | 77.927 | 81.035 | +3.81% | -0.40% | 0.89x | 1.2 | 2026-11-27T08:41:53.496593+00:00 | Not calibrated | WEAK 44/100 | HIGH 68/100 | Watch | WATCH |
| 8 | PAXG/USD | 3659.03 | 72.711 | 58.806 | +2.88% | -0.22% | 3.16x | 2.8 | 2026-11-27T08:41:53.496593+00:00 | Not calibrated | MODERATE 66/100 | HIGH 61/100 | Watch | WATCH |
| 9 | SOL/USD | 73.13 | 72.332 | 75.926 | +3.09% | -0.38% | 0.83x | 1.4 | 2026-11-27T08:41:53.496593+00:00 | Not calibrated | WEAK 41/100 | HIGH 68/100 | Watch | WATCH |
| 10 | LINK/USD | 9.59511 | 71.403 | 78.886 | +3.52% | -0.50% | 0.50x | 1.6 | 2026-11-27T08:41:53.496593+00:00 | Not calibrated | WEAK 41/100 | VERY_HIGH 76/100 | Watch | WATCH |
| 11 | ETH/USD | 1727.84 | 70.489 | 71.628 | +2.38% | -0.51% | 1.14x | 0.1 | 2026-11-27T08:41:53.496593+00:00 | Not calibrated | MODERATE 45/100 | HIGH 68/100 | Watch | WATCH |
| 12 | UNI/USD | 4.8871 | 66.347 | 78.106 | +5.10% | -0.61% | 0.13x | 4.1 | 2026-11-27T08:41:53.496593+00:00 | Not calibrated | WEAK 38/100 | VERY_HIGH 76/100 | Watch | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | ZEC/USD | 97.920 | 745.9 | -0.53% | 0.54x |
| 2 | HYPE/USD | 91.276 | 65.58 | -0.30% | 0.81x |
| 3 | XRP/USD | 81.035 | 0.97864 | -0.40% | 0.89x |
| 4 | LINK/USD | 78.886 | 9.59511 | -0.50% | 0.50x |
| 5 | UNI/USD | 78.106 | 4.8871 | -0.61% | 0.13x |
| 6 | SOL/USD | 75.926 | 73.13 | -0.38% | 0.83x |
| 7 | SUI/USD | 73.253 | 0.6865 | -0.47% | 1.95x |
| 8 | ADA/USD | 71.884 | 0.152891 | -0.42% | 3.64x |
| 9 | ETH/USD | 71.628 | 1727.84 | -0.51% | 1.14x |
| 10 | INJ/USD | 69.787 | 6.501 | +0.12% | 3.24x |
| 11 | XBT/USD | 68.616 | 61675.5 | -0.40% | 2.49x |
| 12 | PAXG/USD | 58.806 | 3659.03 | -0.22% | 3.16x |

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

- Persisted scans: 1984; predictions: 17510; observations: 1201505.
- Matured sampled outcomes across 1/6/24/48h: 38765; gap abstentions: 25689. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 150 (sampled only; not a success-rate estimate).
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

**Writer:** 45967373684 · **Generation:** 1984 · **Legacy run:** 45967373684
**Main quote time:** 2026-11-27T08:42:01.422511+00:00 · **Legacy report time:** 2026-11-27T08:42:51.455811+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | ZEC/USD | 745.9 | 90.72 | -0.53% | 0.54x | MODERATE 50/100 | VERY_HIGH 76/100 | Watch |
| 2 | HYPE/USD | 65.58 | 87.84 | -0.30% | 0.81x | MODERATE 49/100 | HIGH 68/100 | Watch |
| 3 | INJ/USD ⭐ | 6.501 | 85.40 | +0.12% | 3.24x | STRONG 98/100 | HIGH 55/100 | Watch |
| 4 | ADA/USD | 0.152891 | 84.76 | -0.42% | 3.64x | STRONG 72/100 | HIGH 61/100 | Watch |
| 5 | XBT/USD | 61675.5 | 81.47 | -0.40% | 2.49x | STRONG 71/100 | HIGH 61/100 | Watch |
| 6 | SUI/USD | 0.6865 | 80.46 | -0.47% | 1.95x | MODERATE 60/100 | HIGH 61/100 | Watch |
| 7 | XRP/USD | 0.97864 | 77.93 | -0.40% | 0.89x | WEAK 44/100 | HIGH 68/100 | Watch |
| 8 | PAXG/USD | 3659.03 | 72.71 | -0.22% | 3.16x | MODERATE 66/100 | HIGH 61/100 | Watch |
| 9 | SOL/USD | 73.13 | 72.33 | -0.38% | 0.83x | WEAK 41/100 | HIGH 68/100 | Watch |
| 10 | LINK/USD | 9.59511 | 71.40 | -0.50% | 0.50x | WEAK 41/100 | VERY_HIGH 76/100 | Watch |
| 11 | ETH/USD | 1727.84 | 70.49 | -0.51% | 1.14x | MODERATE 45/100 | HIGH 68/100 | Watch |
| 12 | UNI/USD | 4.8871 | 66.35 | -0.61% | 0.13x | WEAK 38/100 | VERY_HIGH 76/100 | Watch |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | INJ/USD ⭐ | 6.53 | 85.89 | +0.12% | 3.24x | 5089 | STRONG 98/100 | HIGH 55/100 | Watch |

**Same-run overlap:** INJ/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
