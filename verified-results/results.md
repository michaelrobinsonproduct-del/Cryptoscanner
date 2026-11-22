# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-22T22:11:29.756234+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/45076122621
**Source SHA:** 193371a597e6dbc5a6a884defbe9e1519a6a183a
**Previous ledger commit:** 0621b4f537a5901c14373dcb408e08f4d46ea68d (atomic ledger/results publication)
**Ledger generation:** 1343 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 8s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 628; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 610; valid market observations: 608; OHLC screened: 24.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | NIGHT/USD | 0.04937 | 99.479 | 91.841 | +11.49% | +0.24% | 1.64x | 4.0 | 2026-11-22T22:11:21.576269+00:00 | Not calibrated | STRONG 95/100 | HIGH 55/100 | Consider small entry | WATCH |
| 2 | PIEVERSE/USD | 3.711 | 96.029 | 75.678 | +9.05% | +1.07% | 2.86x | 20.0 | 2026-11-22T22:11:21.576269+00:00 | Not calibrated | STRONG 98/100 | HIGH 61/100 | Consider small entry | WATCH |
| 3 | NEAR/USD | 2.9966 | 83.135 | 80.916 | +3.82% | +0.10% | 1.17x | 1.7 | 2026-11-22T22:11:21.576269+00:00 | Not calibrated | MODERATE 67/100 | HIGH 62/100 | Watch | WATCH |
| 4 | DRV/USD | 0.37307 | 81.151 | 85.838 | +11.30% | -0.71% | 0.89x | 6.2 | 2026-11-22T22:11:21.576269+00:00 | Not calibrated | MODERATE 46/100 | HIGH 68/100 | Watch | WATCH |
| 5 | VVV/USD | 26.057 | 79.079 | 83.689 | +4.65% | +0.18% | 0.45x | 7.7 | 2026-11-22T22:11:21.576269+00:00 | Not calibrated | MODERATE 60/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 6 | PUMP/USD | 0.002572 | 78.865 | 84.655 | +9.73% | -0.23% | 0.54x | 3.9 | 2026-11-22T22:11:21.576269+00:00 | Not calibrated | WEAK 44/100 | VERY_HIGH 76/100 | Watch | WATCH |
| 7 | ZEC/USD | 795.3 | 74.860 | 70.346 | +2.20% | +0.21% | 1.34x | 0.1 | 2026-11-22T22:11:21.576269+00:00 | Not calibrated | STRONG 82/100 | HIGH 55/100 | Watch | WATCH |
| 8 | STBL/USD | 0.017138 | 72.501 | 69.314 | +7.09% | -0.08% | 1.36x | 13.4 | 2026-11-22T22:11:21.576269+00:00 | Not calibrated | MODERATE 51/100 | VERY_HIGH 79/100 | Watch | WATCH |
| 9 | LINK/USD | 8.77198 | 69.750 | 56.192 | +2.06% | -0.29% | 5.50x | 2.6 | 2026-11-22T22:11:21.576269+00:00 | Not calibrated | MODERATE 65/100 | HIGH 61/100 | Watch | WATCH |
| 10 | XBT/USD | 60801.4 | 67.632 | 63.280 | +1.18% | -0.09% | 1.48x | 0.0 | 2026-11-22T22:11:21.576269+00:00 | Not calibrated | MODERATE 54/100 | HIGH 61/100 | Watch | WATCH |
| 11 | ETH/USD | 1714.45 | 63.311 | 68.357 | +1.91% | -0.25% | 0.62x | 0.1 | 2026-11-22T22:11:21.576269+00:00 | Not calibrated | WEAK 37/100 | VERY_HIGH 76/100 | Watch | WATCH |
| 12 | HYPE/USD | 62.55 | 62.613 | 68.376 | +2.14% | -0.14% | 0.50x | 3.2 | 2026-11-22T22:11:21.576269+00:00 | Not calibrated | WEAK 36/100 | VERY_HIGH 76/100 | Watch | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | NIGHT/USD | 91.841 | 0.04937 | +0.24% | 1.64x |
| 2 | DRV/USD | 85.838 | 0.37307 | -0.71% | 0.89x |
| 3 | PUMP/USD | 84.655 | 0.002572 | -0.23% | 0.54x |
| 4 | VVV/USD | 83.689 | 26.057 | +0.18% | 0.45x |
| 5 | NEAR/USD | 80.916 | 2.9966 | +0.10% | 1.17x |
| 6 | PIEVERSE/USD | 75.678 | 3.711 | +1.07% | 2.86x |
| 7 | ZEC/USD | 70.346 | 795.3 | +0.21% | 1.34x |
| 8 | STBL/USD | 69.314 | 0.017138 | -0.08% | 1.36x |
| 9 | HYPE/USD | 68.376 | 62.55 | -0.14% | 0.50x |
| 10 | ETH/USD | 68.357 | 1714.45 | -0.25% | 0.62x |
| 11 | XBT/USD | 63.280 | 60801.4 | -0.09% | 1.48x |
| 12 | LINK/USD | 56.192 | 8.77198 | -0.29% | 5.50x |

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

- Persisted scans: 1343; predictions: 11035; observations: 812994.
- Matured sampled outcomes across 1/6/24/48h: 16917; gap abstentions: 22370. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 61 (sampled only; not a success-rate estimate).
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

**Writer:** 45076122621 · **Generation:** 1343 · **Legacy run:** 45076122621
**Main quote time:** 2026-11-22T22:11:29.756234+00:00 · **Legacy report time:** 2026-11-22T22:12:24.685652+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | NIGHT/USD ⭐ | 0.04937 | 99.48 | +0.24% | 1.64x | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 2 | PIEVERSE/USD ⭐ | 3.711 | 96.03 | +1.07% | 2.86x | STRONG 100/100 | HIGH 61/100 | Consider small entry |
| 3 | NEAR/USD ⭐ | 2.9966 | 83.14 | +0.10% | 1.17x | STRONG 77/100 | HIGH 62/100 | Watch |
| 4 | DRV/USD | 0.37307 | 81.15 | -0.71% | 0.89x | MODERATE 46/100 | HIGH 68/100 | Watch |
| 5 | VVV/USD | 26.057 | 79.08 | +0.18% | 0.45x | MODERATE 60/100 | VERY_HIGH 70/100 | Watch |
| 6 | PUMP/USD | 0.002572 | 78.86 | -0.23% | 0.54x | WEAK 44/100 | VERY_HIGH 76/100 | Watch |
| 7 | ZEC/USD ⭐ | 795.3 | 74.86 | +0.21% | 1.34x | STRONG 92/100 | HIGH 55/100 | Watch |
| 8 | STBL/USD | 0.017138 | 72.50 | -0.08% | 1.36x | MODERATE 51/100 | VERY_HIGH 79/100 | Watch |
| 9 | LINK/USD | 8.77198 | 69.75 | -0.29% | 5.50x | MODERATE 65/100 | HIGH 61/100 | Watch |
| 10 | XBT/USD | 60801.4 | 67.63 | -0.09% | 1.48x | MODERATE 54/100 | HIGH 61/100 | Watch |
| 11 | ETH/USD | 1714.45 | 63.31 | -0.25% | 0.62x | WEAK 37/100 | VERY_HIGH 76/100 | Watch |
| 12 | HYPE/USD | 62.55 | 62.61 | -0.14% | 0.50x | WEAK 36/100 | VERY_HIGH 76/100 | Watch |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | NEAR/USD ⭐ | 2.9975 | 93.21 | +0.10% | 1.17x | 12695 | STRONG 82/100 | HIGH 62/100 | Watch |
| 2 | NIGHT/USD ⭐ | 0.04936 | 87.47 | +0.24% | 1.64x | 10115 | STRONG 99/100 | HIGH 55/100 | Consider small entry |
| 3 | PIEVERSE/USD ⭐ | 3.7053 | 87.05 | +1.07% | 2.86x | 5876 | STRONG 99/100 | HIGH 67/100 | Consider small entry |
| 4 | ZEC/USD ⭐ | 795.51 | 75.22 | +0.21% | 1.34x | 18302 | STRONG 93/100 | HIGH 55/100 | Watch |

**Same-run overlap:** NIGHT/USD, PIEVERSE/USD, NEAR/USD, ZEC/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
