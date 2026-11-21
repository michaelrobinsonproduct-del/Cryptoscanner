# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-21T09:30:37.278560+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/44889823361
**Source SHA:** bdc7e68f7fa75fae6636b7738d52f10a65d92038
**Previous ledger commit:** 8e7008803fff6c535ecf70d5e2921f0abf5272cb (atomic ledger/results publication)
**Ledger generation:** 1115 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 6s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 628; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 610; valid market observations: 608; OHLC screened: 19.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | VVV/USD | 21.694 | 80.394 | 84.235 | +4.60% | -0.10% | 0.66x | 6.0 | 2026-11-21T09:30:31.121457+00:00 | Not calibrated | MODERATE 45/100 | VERY_HIGH 76/100 | Watch | WATCH |
| 2 | CAP/USD | 0.094166 | 63.316 | 49.714 | +2.87% | -0.28% | 3.07x | 8.1 | 2026-11-21T09:30:31.121457+00:00 | Not calibrated | MODERATE 62/100 | HIGH 66/100 | Watch | WATCH |
| 3 | ETH/USD | 1635.96 | 57.134 | 61.826 | +1.03% | +0.24% | 0.41x | 0.7 | 2026-11-21T09:30:31.121457+00:00 | Not calibrated | MODERATE 59/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 4 | RARE/USD | 0.01364 | 56.137 | 38.812 | +2.56% | +0.52% | 2.47x | 22.0 | 2026-11-21T09:30:31.121457+00:00 | Not calibrated | STRONG 73/100 | VERY_HIGH 72/100 | Watch | WATCH |
| 5 | ZAMA/USD | 0.05796 | 55.744 | 34.278 | +1.67% | +1.29% | 3.06x | 17.3 | 2026-11-21T09:30:31.121457+00:00 | Not calibrated | STRONG 78/100 | VERY_HIGH 73/100 | Watch | WATCH |
| 6 | TRX/USD | 0.30268 | 49.230 | 57.020 | +0.39% | +0.05% | 0.20x | 1.4 | 2026-11-21T09:30:31.121457+00:00 | Not calibrated | MODERATE 45/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 7 | MORPHO/USD | 1.54674 | 42.534 | 29.797 | +1.00% | +0.44% | 2.05x | 23.4 | 2026-11-21T09:30:31.121457+00:00 | Not calibrated | MODERATE 66/100 | VERY_HIGH 72/100 | Watch | WATCH |
| 8 | CSPR/USD | 0.001703 | 24.295 | 37.566 | +1.84% | -1.21% | 0.28x | 12.3 | 2026-11-21T09:30:31.121457+00:00 | Not calibrated | WEAK 12/100 | EXTREME 98/100 | Do nothing | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | VVV/USD | 84.235 | 21.694 | -0.10% | 0.66x |
| 2 | ETH/USD | 61.826 | 1635.96 | +0.24% | 0.41x |
| 3 | TRX/USD | 57.020 | 0.30268 | +0.05% | 0.20x |
| 4 | CAP/USD | 49.714 | 0.094166 | -0.28% | 3.07x |
| 5 | RARE/USD | 38.812 | 0.01364 | +0.52% | 2.47x |
| 6 | CSPR/USD | 37.566 | 0.001703 | -1.21% | 0.28x |
| 7 | ZAMA/USD | 34.278 | 0.05796 | +1.29% | 3.06x |
| 8 | MORPHO/USD | 29.797 | 1.54674 | +0.44% | 2.05x |

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

- Persisted scans: 1115; predictions: 8753; observations: 674279.
- Matured sampled outcomes across 1/6/24/48h: 11521; gap abstentions: 20294. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 10 (sampled only; not a success-rate estimate).
- False positives / missed movers: NOT VERIFIED without eligible continuous outcome coverage.
- Baseline vs challenger: recorded as-of; unbiased held-out lift NOT MEASURED.
- Online Kraken /USD stablecoin-base pairs excluded: 18 (counted from this scan's online AssetPairs metadata, not inferred from price).
- Stablecoin base exclusions: BRL1, BUSD, DAI, EUR, EURC, EUROP, EURQ, EURR, EURT, FDUSD, FRAX, GUSD, PYUSD, QCAD, RLUSD, TGBP, TUSD, USD, USD1, USDC, USDD, USDE, USDG, USDQ, USDR, USDS, USDT, ZUSD.
- DEX: NOT USED; no DEX freshness gate.
- OHLC screening abstentions: 11; details in immutable scan JSON artifact.
- Storage: ledger and results published in one non-force Git commit and read back. Independent artifact recovery is NOT VERIFIED by this scan alone.
- Errors: none in successful committed scan; a failed workflow must not publish a SUCCESS report.

# Cryptoscanner — challenger and independent legacy-inspired WATCH

Paper only · risk is high or higher · 30%+ in 48h probability NOT CALIBRATED
Signal confidence 0–100 means setup strength only, NOT a win probability. Actions are research guidance; no trade authorization.

**Writer:** 44889823361 · **Generation:** 1115 · **Legacy run:** 44889823361
**Main quote time:** 2026-11-21T09:30:37.278560+00:00 · **Legacy report time:** 2026-11-21T09:31:20.307040+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | VVV/USD | 21.694 | 80.39 | -0.10% | 0.66x | MODERATE 45/100 | VERY_HIGH 76/100 | Watch |
| 2 | CAP/USD | 0.094166 | 63.32 | -0.28% | 3.07x | MODERATE 62/100 | HIGH 66/100 | Watch |
| 3 | ETH/USD | 1635.96 | 57.13 | +0.24% | 0.41x | MODERATE 59/100 | VERY_HIGH 70/100 | Watch |
| 4 | RARE/USD ⭐ | 0.01364 | 56.14 | +0.52% | 2.47x | STRONG 83/100 | VERY_HIGH 72/100 | Watch |
| 5 | ZAMA/USD ⭐ | 0.05796 | 55.74 | +1.29% | 3.06x | STRONG 88/100 | VERY_HIGH 73/100 | Watch |
| 6 | TRX/USD | 0.30268 | 49.23 | +0.05% | 0.20x | MODERATE 45/100 | VERY_HIGH 70/100 | Watch |
| 7 | MORPHO/USD ⭐ | 1.54674 | 42.53 | +0.44% | 2.05x | STRONG 76/100 | VERY_HIGH 72/100 | Watch |
| 8 | CSPR/USD | 0.001703 | 24.30 | -1.21% | 0.28x | WEAK 12/100 | EXTREME 98/100 | Do nothing |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | RARE/USD ⭐ | 0.01364 | 61.27 | +0.52% | 2.47x | 7474 | STRONG 86/100 | VERY_HIGH 72/100 | Watch |
| 2 | ZAMA/USD ⭐ | 0.05796 | 54.47 | +1.29% | 3.06x | 2620 | STRONG 87/100 | VERY_HIGH 73/100 | Watch |
| 3 | MORPHO/USD ⭐ | 1.54905 | 44.04 | +0.44% | 2.05x | 2741 | STRONG 82/100 | HIGH 66/100 | Consider small entry |

**Same-run overlap:** RARE/USD, ZAMA/USD, MORPHO/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
