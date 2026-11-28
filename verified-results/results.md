# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-28T01:12:25.531568+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/46091667835
**Source SHA:** 858c8bc8ec5d7641ddb39cacd8aca91719f855b1
**Previous ledger commit:** 7fa2ff47f1184b93de48839ec6e7a92a3334febe (atomic ledger/results publication)
**Ledger generation:** 2085 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 8s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 628; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 610; valid market observations: 606; OHLC screened: 24.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | ZEC/USD | 742.14 | 77.669 | 60.260 | +1.03% | +0.91% | 2.29x | 3.9 | 2026-11-28T01:12:17.988817+00:00 | Not calibrated | STRONG 94/100 | HIGH 55/100 | Consider small entry | WATCH |
| 2 | TAO/USD | 188.4868 | 76.107 | 58.375 | +0.82% | +0.55% | 5.33x | 4.7 | 2026-11-28T01:12:17.988817+00:00 | Not calibrated | STRONG 93/100 | HIGH 55/100 | Consider small entry | WATCH |
| 3 | SOL/USD | 71.84 | 71.831 | 56.650 | +0.34% | +0.15% | 2.44x | 1.4 | 2026-11-28T01:12:17.988817+00:00 | Not calibrated | STRONG 81/100 | HIGH 55/100 | Watch | WATCH |
| 4 | ETH/USD | 1665.17 | 67.147 | 56.765 | +0.26% | +0.18% | 1.95x | 0.1 | 2026-11-28T01:12:17.988817+00:00 | Not calibrated | MODERATE 69/100 | HIGH 55/100 | Watch | WATCH |
| 5 | BCH/USD | 208.96 | 58.888 | 43.342 | +0.95% | +0.17% | 2.47x | 2.9 | 2026-11-28T01:12:17.988817+00:00 | Not calibrated | STRONG 74/100 | HIGH 55/100 | Watch | WATCH |
| 6 | HYPE/USD | 63.96 | 54.292 | 59.400 | +0.74% | +0.36% | 0.31x | 1.6 | 2026-11-28T01:12:17.988817+00:00 | Not calibrated | MODERATE 57/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 7 | SEI/USD | 0.03853 | 47.682 | 28.894 | +0.31% | +0.76% | 3.44x | 13.0 | 2026-11-28T01:12:17.988817+00:00 | Not calibrated | STRONG 74/100 | HIGH 66/100 | Watch | WATCH |
| 8 | CFG/USD | 0.059 | 46.913 | 55.879 | +4.61% | -0.68% | 0.44x | 17.1 | 2026-11-28T01:12:17.988817+00:00 | Not calibrated | WEAK 23/100 | EXTREME 87/100 | Do nothing | WATCH |
| 9 | CC/USD | 0.07488 | 43.532 | 38.160 | +0.98% | +0.62% | 1.23x | 6.7 | 2026-11-28T01:12:17.988817+00:00 | Not calibrated | MODERATE 57/100 | HIGH 67/100 | Watch | WATCH |
| 10 | SKY/USD | 0.05223 | 40.796 | 40.456 | +0.64% | -0.36% | 1.21x | 7.7 | 2026-11-28T01:12:17.988817+00:00 | Not calibrated | WEAK 30/100 | HIGH 68/100 | Do nothing | WATCH |
| 11 | DRV/USD | 0.36378 | 37.529 | 27.466 | +0.26% | +0.14% | 1.93x | 18.7 | 2026-11-28T01:12:17.988817+00:00 | Not calibrated | MODERATE 49/100 | HIGH 66/100 | Watch | WATCH |
| 12 | ATOM/USD | 1.2399 | 31.081 | 33.981 | +0.99% | +0.50% | 0.46x | 9.7 | 2026-11-28T01:12:17.988817+00:00 | Not calibrated | MODERATE 46/100 | VERY_HIGH 75/100 | Watch | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | ZEC/USD | 60.260 | 742.14 | +0.91% | 2.29x |
| 2 | HYPE/USD | 59.400 | 63.96 | +0.36% | 0.31x |
| 3 | TAO/USD | 58.375 | 188.4868 | +0.55% | 5.33x |
| 4 | ETH/USD | 56.765 | 1665.17 | +0.18% | 1.95x |
| 5 | SOL/USD | 56.650 | 71.84 | +0.15% | 2.44x |
| 6 | CFG/USD | 55.879 | 0.059 | -0.68% | 0.44x |
| 7 | BCH/USD | 43.342 | 208.96 | +0.17% | 2.47x |
| 8 | SKY/USD | 40.456 | 0.05223 | -0.36% | 1.21x |
| 9 | CC/USD | 38.160 | 0.07488 | +0.62% | 1.23x |
| 10 | ATOM/USD | 33.981 | 1.2399 | +0.50% | 0.46x |
| 11 | SEI/USD | 28.894 | 0.03853 | +0.76% | 3.44x |
| 12 | DRV/USD | 27.466 | 0.36378 | +0.14% | 1.93x |

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

- Persisted scans: 2085; predictions: 18683; observations: 1262556.
- Matured sampled outcomes across 1/6/24/48h: 42920; gap abstentions: 25968. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 155 (sampled only; not a success-rate estimate).
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

**Writer:** 46091667835 · **Generation:** 2085 · **Legacy run:** 46091667835
**Main quote time:** 2026-11-28T01:12:25.531568+00:00 · **Legacy report time:** 2026-11-28T01:13:06.379224+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | ZEC/USD ⭐ | 742.14 | 77.67 | +0.91% | 2.29x | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 2 | TAO/USD ⭐ | 188.4868 | 76.11 | +0.55% | 5.33x | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 3 | SOL/USD ⭐ | 71.84 | 71.83 | +0.15% | 2.44x | STRONG 91/100 | HIGH 55/100 | Watch |
| 4 | ETH/USD ⭐ | 1665.17 | 67.15 | +0.18% | 1.95x | STRONG 79/100 | HIGH 55/100 | Watch |
| 5 | BCH/USD ⭐ | 208.96 | 58.89 | +0.17% | 2.47x | STRONG 84/100 | HIGH 55/100 | Watch |
| 6 | HYPE/USD | 63.96 | 54.29 | +0.36% | 0.31x | MODERATE 57/100 | VERY_HIGH 70/100 | Watch |
| 7 | SEI/USD | 0.03853 | 47.68 | +0.76% | 3.44x | STRONG 74/100 | HIGH 66/100 | Watch |
| 8 | CFG/USD | 0.059 | 46.91 | -0.68% | 0.44x | WEAK 23/100 | EXTREME 87/100 | Do nothing |
| 9 | CC/USD | 0.07488 | 43.53 | +0.62% | 1.23x | MODERATE 57/100 | HIGH 67/100 | Watch |
| 10 | SKY/USD | 0.05223 | 40.80 | -0.36% | 1.21x | WEAK 30/100 | HIGH 68/100 | Do nothing |
| 11 | DRV/USD | 0.36378 | 37.53 | +0.14% | 1.93x | MODERATE 49/100 | HIGH 66/100 | Watch |
| 12 | ATOM/USD | 1.2399 | 31.08 | +0.50% | 0.46x | MODERATE 46/100 | VERY_HIGH 75/100 | Watch |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | ZEC/USD ⭐ | 743.15 | 63.93 | +0.91% | 2.29x | 33549 | STRONG 97/100 | HIGH 55/100 | Consider small entry |
| 2 | SOL/USD ⭐ | 71.84 | 59.46 | +0.15% | 2.44x | 45047 | STRONG 85/100 | HIGH 55/100 | Watch |
| 3 | ETH/USD ⭐ | 1664.68 | 58.94 | +0.18% | 1.95x | 46756 | STRONG 74/100 | HIGH 55/100 | Watch |
| 4 | TAO/USD ⭐ | 188.4868 | 58.87 | +0.55% | 5.33x | 9308 | STRONG 94/100 | HIGH 55/100 | Consider small entry |
| 5 | XBT/USD | 60000.7 | 58.50 | +0.22% | 1.78x | 167144 | STRONG 74/100 | HIGH 55/100 | Watch |
| 6 | BCH/USD ⭐ | 209 | 53.17 | +0.17% | 2.47x | 3286 | STRONG 82/100 | HIGH 55/100 | Watch |
| 7 | AVAX/USD | 6.621 | 51.74 | +0.15% | 4.19x | 4281 | STRONG 71/100 | HIGH 55/100 | Watch |
| 8 | NEAR/USD | 3.0241 | 51.29 | +0.42% | 1.41x | 14197 | STRONG 71/100 | HIGH 55/100 | Watch |

**Same-run overlap:** ZEC/USD, TAO/USD, SOL/USD, ETH/USD, BCH/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
