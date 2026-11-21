# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-21T12:20:48.887099+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/44903327072
**Source SHA:** bdc7e68f7fa75fae6636b7738d52f10a65d92038
**Previous ledger commit:** 8f7fc1403ff6e48a26760afd41beef99b1c9cc90 (atomic ledger/results publication)
**Ledger generation:** 1132 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 8s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 628; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 610; valid market observations: 608; OHLC screened: 24.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | VVV/USD | 22.343 | 101.760 | 94.621 | +7.73% | +0.99% | 1.22x | 10.8 | 2026-11-21T12:20:40.602158+00:00 | Not calibrated | STRONG 80/100 | HIGH 68/100 | Watch | WATCH |
| 2 | XMR/USD | 475.35 | 77.514 | 80.977 | +4.18% | +0.62% | 0.34x | 6.5 | 2026-11-21T12:20:40.602158+00:00 | Not calibrated | MODERATE 69/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 3 | ETH/USD | 1655.22 | 64.466 | 70.489 | +2.22% | +0.48% | 0.16x | 0.1 | 2026-11-21T12:20:40.602158+00:00 | Not calibrated | MODERATE 62/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 4 | SOL/USD | 69.06 | 62.358 | 57.842 | +0.51% | +0.70% | 1.10x | 1.4 | 2026-11-21T12:20:40.602158+00:00 | Not calibrated | MODERATE 66/100 | HIGH 62/100 | Watch | WATCH |
| 5 | ZEC/USD | 768.8 | 61.932 | 61.804 | +1.44% | +1.29% | 0.37x | 6.5 | 2026-11-21T12:20:40.602158+00:00 | Not calibrated | MODERATE 61/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 6 | AAVE/USD | 99.7 | 58.569 | 57.518 | +1.85% | +0.26% | 0.97x | 3.0 | 2026-11-21T12:20:40.602158+00:00 | Not calibrated | MODERATE 59/100 | HIGH 62/100 | Watch | WATCH |
| 7 | SENT/USD | 0.021223 | 53.458 | 48.345 | +3.05% | +0.20% | 1.41x | 8.0 | 2026-11-21T12:20:40.602158+00:00 | Not calibrated | STRONG 72/100 | HIGH 67/100 | Watch | WATCH |
| 8 | UNI/USD | 4.5166 | 53.450 | 59.074 | +1.11% | +0.59% | 0.14x | 7.3 | 2026-11-21T12:20:40.602158+00:00 | Not calibrated | MODERATE 57/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 9 | TRX/USD | 0.302795 | 52.172 | 57.981 | +0.43% | -0.01% | 0.43x | 0.0 | 2026-11-21T12:20:40.602158+00:00 | Not calibrated | WEAK 31/100 | VERY_HIGH 76/100 | Do nothing | WATCH |
| 10 | TAO/USD | 181.9179 | 52.139 | 55.003 | +0.78% | +0.76% | 0.34x | 10.9 | 2026-11-21T12:20:40.602158+00:00 | Not calibrated | MODERATE 51/100 | VERY_HIGH 76/100 | Watch | WATCH |
| 11 | SKY/USD | 0.04461 | 41.366 | 43.207 | +1.76% | +0.34% | 0.65x | 6.7 | 2026-11-21T12:20:40.602158+00:00 | Not calibrated | MODERATE 51/100 | VERY_HIGH 75/100 | Watch | WATCH |
| 12 | ZAMA/USD | 0.05831 | 34.897 | 42.952 | +2.28% | +0.22% | 0.08x | 8.6 | 2026-11-21T12:20:40.602158+00:00 | Not calibrated | MODERATE 47/100 | VERY_HIGH 82/100 | Watch | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | VVV/USD | 94.621 | 22.343 | +0.99% | 1.22x |
| 2 | XMR/USD | 80.977 | 475.35 | +0.62% | 0.34x |
| 3 | ETH/USD | 70.489 | 1655.22 | +0.48% | 0.16x |
| 4 | ZEC/USD | 61.804 | 768.8 | +1.29% | 0.37x |
| 5 | UNI/USD | 59.074 | 4.5166 | +0.59% | 0.14x |
| 6 | TRX/USD | 57.981 | 0.302795 | -0.01% | 0.43x |
| 7 | SOL/USD | 57.842 | 69.06 | +0.70% | 1.10x |
| 8 | AAVE/USD | 57.518 | 99.7 | +0.26% | 0.97x |
| 9 | TAO/USD | 55.003 | 181.9179 | +0.76% | 0.34x |
| 10 | SENT/USD | 48.345 | 0.021223 | +0.20% | 1.41x |
| 11 | SKY/USD | 43.207 | 0.04461 | +0.34% | 0.65x |
| 12 | ZAMA/USD | 42.952 | 0.05831 | +0.22% | 0.08x |

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

- Persisted scans: 1132; predictions: 8895; observations: 684615.
- Matured sampled outcomes across 1/6/24/48h: 11695; gap abstentions: 20370. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 16 (sampled only; not a success-rate estimate).
- False positives / missed movers: NOT VERIFIED without eligible continuous outcome coverage.
- Baseline vs challenger: recorded as-of; unbiased held-out lift NOT MEASURED.
- Online Kraken /USD stablecoin-base pairs excluded: 18 (counted from this scan's online AssetPairs metadata, not inferred from price).
- Stablecoin base exclusions: BRL1, BUSD, DAI, EUR, EURC, EUROP, EURQ, EURR, EURT, FDUSD, FRAX, GUSD, PYUSD, QCAD, RLUSD, TGBP, TUSD, USD, USD1, USDC, USDD, USDE, USDG, USDQ, USDR, USDS, USDT, ZUSD.
- DEX: NOT USED; no DEX freshness gate.
- OHLC screening abstentions: 10; details in immutable scan JSON artifact.
- Storage: ledger and results published in one non-force Git commit and read back. Independent artifact recovery is NOT VERIFIED by this scan alone.
- Errors: none in successful committed scan; a failed workflow must not publish a SUCCESS report.

# Cryptoscanner — challenger and independent legacy-inspired WATCH

Paper only · risk is high or higher · 30%+ in 48h probability NOT CALIBRATED
Signal confidence 0–100 means setup strength only, NOT a win probability. Actions are research guidance; no trade authorization.

**Writer:** 44903327072 · **Generation:** 1132 · **Legacy run:** 44903327072
**Main quote time:** 2026-11-21T12:20:48.887099+00:00 · **Legacy report time:** 2026-11-21T12:21:39.980045+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | VVV/USD ⭐ | 22.343 | 101.76 | +0.99% | 1.22x | STRONG 90/100 | HIGH 68/100 | Watch |
| 2 | XMR/USD | 475.35 | 77.51 | +0.62% | 0.34x | MODERATE 69/100 | VERY_HIGH 70/100 | Watch |
| 3 | ETH/USD | 1655.22 | 64.47 | +0.48% | 0.16x | MODERATE 62/100 | VERY_HIGH 70/100 | Watch |
| 4 | SOL/USD ⭐ | 69.06 | 62.36 | +0.70% | 1.10x | STRONG 76/100 | HIGH 62/100 | Watch |
| 5 | ZEC/USD | 768.8 | 61.93 | +1.29% | 0.37x | MODERATE 61/100 | VERY_HIGH 70/100 | Watch |
| 6 | AAVE/USD | 99.7 | 58.57 | +0.26% | 0.97x | MODERATE 59/100 | HIGH 62/100 | Watch |
| 7 | SENT/USD ⭐ | 0.021223 | 53.46 | +0.20% | 1.41x | STRONG 82/100 | HIGH 67/100 | Watch |
| 8 | UNI/USD | 4.5166 | 53.45 | +0.59% | 0.14x | MODERATE 57/100 | VERY_HIGH 70/100 | Watch |
| 9 | TRX/USD | 0.302795 | 52.17 | -0.01% | 0.43x | WEAK 31/100 | VERY_HIGH 76/100 | Do nothing |
| 10 | TAO/USD | 181.9179 | 52.14 | +0.76% | 0.34x | MODERATE 51/100 | VERY_HIGH 76/100 | Watch |
| 11 | SKY/USD | 0.04461 | 41.37 | +0.34% | 0.65x | MODERATE 51/100 | VERY_HIGH 75/100 | Watch |
| 12 | ZAMA/USD | 0.05831 | 34.90 | +0.22% | 0.08x | MODERATE 47/100 | VERY_HIGH 82/100 | Watch |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | VVV/USD ⭐ | 22.306 | 88.85 | +0.99% | 1.22x | 14323 | STRONG 89/100 | HIGH 62/100 | Watch |
| 2 | SENT/USD ⭐ | 0.021163 | 57.95 | +0.20% | 1.41x | 4994 | STRONG 84/100 | HIGH 67/100 | Watch |
| 3 | SOL/USD ⭐ | 69.08 | 52.28 | +0.70% | 1.10x | 57743 | STRONG 71/100 | HIGH 62/100 | Watch |

**Same-run overlap:** VVV/USD, SOL/USD, SENT/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
