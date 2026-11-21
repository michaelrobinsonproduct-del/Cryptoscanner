# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-21T07:00:42.984787+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/44878106301
**Source SHA:** bdc7e68f7fa75fae6636b7738d52f10a65d92038
**Previous ledger commit:** 81992ff39d694d89d5a21e69bd63f8ec2a5b025c (atomic ledger/results publication)
**Ledger generation:** 1099 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 4s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 628; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 610; valid market observations: 608; OHLC screened: 15.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | VVV/USD | 21.865 | 122.001 | 86.372 | +5.43% | +4.13% | 21.03x | 13.3 | 2026-11-21T07:00:38.937060+00:00 | Not calibrated | STRONG 100/100 | VERY_HIGH 71/100 | Watch | WATCH |
| 2 | DRV/USD | 0.26404 | 81.713 | 73.969 | +7.53% | +2.33% | 0.61x | 18.2 | 2026-11-21T07:00:38.937060+00:00 | Not calibrated | MODERATE 66/100 | VERY_HIGH 76/100 | Watch | WATCH |
| 3 | ETH/USD | 1634.78 | 80.028 | 60.857 | +0.95% | +1.61% | 2.11x | 1.7 | 2026-11-21T07:00:38.937060+00:00 | Not calibrated | STRONG 95/100 | HIGH 55/100 | Consider small entry | WATCH |
| 4 | RARE/USD | 0.01434 | 69.382 | 62.968 | +7.82% | +2.43% | 0.42x | 28.0 | 2026-11-21T07:00:38.937060+00:00 | Not calibrated | MODERATE 55/100 | EXTREME 87/100 | Do nothing | WATCH |
| 5 | DCR/USD | 10.145 | 50.239 | 32.071 | +0.40% | +0.63% | 6.90x | 3.0 | 2026-11-21T07:00:38.937060+00:00 | Not calibrated | STRONG 80/100 | HIGH 67/100 | Watch | WATCH |
| 6 | USELESS/USD | 0.07481 | 49.662 | 25.235 | +0.42% | +1.89% | 3.41x | 33.5 | 2026-11-21T07:00:38.937060+00:00 | Not calibrated | STRONG 70/100 | HIGH 67/100 | Watch | WATCH |
| 7 | ZAMA/USD | 0.05764 | 40.817 | 30.261 | +1.11% | +1.44% | 1.34x | 17.3 | 2026-11-21T07:00:38.937060+00:00 | Not calibrated | MODERATE 60/100 | VERY_HIGH 73/100 | Watch | WATCH |
| 8 | CAP/USD | 0.093639 | 35.601 | 37.618 | +2.29% | +0.72% | 0.44x | 24.3 | 2026-11-21T07:00:38.937060+00:00 | Not calibrated | WEAK 38/100 | EXTREME 87/100 | Do nothing | WATCH |
| 9 | CT/USD | 0.1217 | 30.123 | 22.833 | +0.50% | +1.76% | 0.85x | 24.7 | 2026-11-21T07:00:38.937060+00:00 | Not calibrated | WEAK 35/100 | VERY_HIGH 79/100 | Watch | WATCH |
| 10 | A/USD | 0.0644 | 27.441 | 24.415 | +1.26% | +1.26% | 0.67x | 31.1 | 2026-11-21T07:00:38.937060+00:00 | Not calibrated | WEAK 34/100 | EXTREME 94/100 | Do nothing | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | VVV/USD | 86.372 | 21.865 | +4.13% | 21.03x |
| 2 | DRV/USD | 73.969 | 0.26404 | +2.33% | 0.61x |
| 3 | RARE/USD | 62.968 | 0.01434 | +2.43% | 0.42x |
| 4 | ETH/USD | 60.857 | 1634.78 | +1.61% | 2.11x |
| 5 | CAP/USD | 37.618 | 0.093639 | +0.72% | 0.44x |
| 6 | DCR/USD | 32.071 | 10.145 | +0.63% | 6.90x |
| 7 | ZAMA/USD | 30.261 | 0.05764 | +1.44% | 1.34x |
| 8 | USELESS/USD | 25.235 | 0.07481 | +1.89% | 3.41x |
| 9 | A/USD | 24.415 | 0.0644 | +1.26% | 0.67x |
| 10 | CT/USD | 22.833 | 0.1217 | +1.76% | 0.85x |

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

- Persisted scans: 1099; predictions: 8657; observations: 664551.
- Matured sampled outcomes across 1/6/24/48h: 11238; gap abstentions: 20129. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 10 (sampled only; not a success-rate estimate).
- False positives / missed movers: NOT VERIFIED without eligible continuous outcome coverage.
- Baseline vs challenger: recorded as-of; unbiased held-out lift NOT MEASURED.
- Online Kraken /USD stablecoin-base pairs excluded: 18 (counted from this scan's online AssetPairs metadata, not inferred from price).
- Stablecoin base exclusions: BRL1, BUSD, DAI, EUR, EURC, EUROP, EURQ, EURR, EURT, FDUSD, FRAX, GUSD, PYUSD, QCAD, RLUSD, TGBP, TUSD, USD, USD1, USDC, USDD, USDE, USDG, USDQ, USDR, USDS, USDT, ZUSD.
- DEX: NOT USED; no DEX freshness gate.
- OHLC screening abstentions: 5; details in immutable scan JSON artifact.
- Storage: ledger and results published in one non-force Git commit and read back. Independent artifact recovery is NOT VERIFIED by this scan alone.
- Errors: none in successful committed scan; a failed workflow must not publish a SUCCESS report.

# Cryptoscanner — challenger and independent legacy-inspired WATCH

Paper only · risk is high or higher · 30%+ in 48h probability NOT CALIBRATED
Signal confidence 0–100 means setup strength only, NOT a win probability. Actions are research guidance; no trade authorization.

**Writer:** 44878106301 · **Generation:** 1099 · **Legacy run:** 44878106301
**Main quote time:** 2026-11-21T07:00:42.984787+00:00 · **Legacy report time:** 2026-11-21T07:01:45.570291+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | VVV/USD ⭐ | 21.865 | 122.00 | +4.13% | 21.03x | STRONG 100/100 | VERY_HIGH 71/100 | Watch |
| 2 | DRV/USD | 0.26404 | 81.71 | +2.33% | 0.61x | MODERATE 66/100 | VERY_HIGH 76/100 | Watch |
| 3 | ETH/USD ⭐ | 1634.78 | 80.03 | +1.61% | 2.11x | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 4 | RARE/USD | 0.01434 | 69.38 | +2.43% | 0.42x | MODERATE 55/100 | EXTREME 87/100 | Do nothing |
| 5 | DCR/USD ⭐ | 10.145 | 50.24 | +0.63% | 6.90x | STRONG 90/100 | HIGH 67/100 | Consider small entry |
| 6 | USELESS/USD | 0.07481 | 49.66 | +1.89% | 3.41x | STRONG 70/100 | HIGH 67/100 | Watch |
| 7 | ZAMA/USD ⭐ | 0.05764 | 40.82 | +1.44% | 1.34x | STRONG 70/100 | VERY_HIGH 73/100 | Watch |
| 8 | CAP/USD | 0.093639 | 35.60 | +0.72% | 0.44x | WEAK 38/100 | EXTREME 87/100 | Do nothing |
| 9 | CT/USD | 0.1217 | 30.12 | +1.76% | 0.85x | WEAK 35/100 | VERY_HIGH 79/100 | Watch |
| 10 | A/USD | 0.0644 | 27.44 | +1.26% | 0.67x | WEAK 34/100 | EXTREME 94/100 | Do nothing |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | VVV/USD ⭐ | 21.703 | 100.00 | +4.13% | 21.03x | 14216 | STRONG 100/100 | HIGH 65/100 | Consider small entry |
| 2 | ETH/USD ⭐ | 1630.09 | 69.13 | +1.61% | 2.11x | 95863 | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 3 | TRX/USD | 0.301957 | 59.24 | +0.41% | 3.01x | 6834 | STRONG 85/100 | HIGH 55/100 | Watch |
| 4 | ZAMA/USD ⭐ | 0.05762 | 39.67 | +1.44% | 1.34x | 2454 | STRONG 70/100 | VERY_HIGH 73/100 | Watch |
| 5 | DCR/USD ⭐ | 10.175 | 36.95 | +0.63% | 6.90x | 2192 | STRONG 83/100 | HIGH 67/100 | Consider small entry |

**Same-run overlap:** VVV/USD, ETH/USD, DCR/USD, ZAMA/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
