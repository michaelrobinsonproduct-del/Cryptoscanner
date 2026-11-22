# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-22T19:11:46.286313+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/45059149947
**Source SHA:** 193371a597e6dbc5a6a884defbe9e1519a6a183a
**Previous ledger commit:** 0e00a8191c10c99d61f7de995d57f541a3b584f0 (atomic ledger/results publication)
**Ledger generation:** 1324 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 8s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 628; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 610; valid market observations: 609; OHLC screened: 24.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | DRV/USD | 0.37272 | 102.098 | 84.446 | +11.19% | +0.63% | 2.45x | 9.4 | 2026-11-22T19:11:38.211772+00:00 | Not calibrated | STRONG 100/100 | HIGH 55/100 | Consider small entry | WATCH |
| 2 | WLD/USD | 0.2394 | 86.542 | 67.192 | +5.14% | +0.89% | 2.49x | 4.2 | 2026-11-22T19:11:38.211772+00:00 | Not calibrated | STRONG 98/100 | HIGH 60/100 | Consider small entry | WATCH |
| 3 | NIGHT/USD | 0.04884 | 83.045 | 86.359 | +10.30% | -0.16% | 0.75x | 12.3 | 2026-11-22T19:11:38.211772+00:00 | Not calibrated | WEAK 42/100 | VERY_HIGH 74/100 | Watch | WATCH |
| 4 | NEAR/USD | 3.0067 | 78.917 | 82.870 | +4.17% | +0.37% | 0.42x | 2.7 | 2026-11-22T19:11:38.211772+00:00 | Not calibrated | MODERATE 69/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 5 | LINK/USD | 8.79638 | 73.209 | 59.160 | +2.34% | -0.19% | 2.91x | 2.4 | 2026-11-22T19:11:38.211772+00:00 | Not calibrated | MODERATE 67/100 | HIGH 61/100 | Watch | WATCH |
| 6 | VVV/USD | 25.867 | 72.157 | 77.164 | +3.88% | -0.37% | 0.68x | 10.0 | 2026-11-22T19:11:38.211772+00:00 | Not calibrated | WEAK 36/100 | VERY_HIGH 82/100 | Watch | WATCH |
| 7 | PUMP/USD | 0.00255 | 71.429 | 80.047 | +8.79% | -0.08% | 0.18x | 11.8 | 2026-11-22T19:11:38.211772+00:00 | Not calibrated | WEAK 36/100 | VERY_HIGH 82/100 | Watch | WATCH |
| 8 | PIEVERSE/USD | 3.6769 | 67.033 | 69.422 | +8.05% | +1.04% | 0.24x | 32.2 | 2026-11-22T19:11:38.211772+00:00 | Not calibrated | MODERATE 54/100 | VERY_HIGH 82/100 | Watch | WATCH |
| 9 | ETH/USD | 1713.31 | 65.570 | 67.882 | +1.84% | -0.10% | 0.82x | 0.1 | 2026-11-22T19:11:38.211772+00:00 | Not calibrated | WEAK 38/100 | HIGH 68/100 | Watch | WATCH |
| 10 | XBT/USD | 60646.3 | 61.292 | 61.473 | +0.93% | -0.13% | 1.05x | 0.0 | 2026-11-22T19:11:38.211772+00:00 | Not calibrated | WEAK 41/100 | HIGH 68/100 | Watch | WATCH |
| 11 | HYPE/USD | 62.39 | 59.154 | 67.343 | +1.88% | -0.43% | 0.40x | 1.6 | 2026-11-22T19:11:38.211772+00:00 | Not calibrated | WEAK 35/100 | VERY_HIGH 76/100 | Watch | WATCH |
| 12 | BNB/USD | 556.56 | 55.955 | 47.357 | +1.67% | -0.28% | 2.00x | 2.2 | 2026-11-22T19:11:38.211772+00:00 | Not calibrated | MODERATE 58/100 | HIGH 61/100 | Watch | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | NIGHT/USD | 86.359 | 0.04884 | -0.16% | 0.75x |
| 2 | DRV/USD | 84.446 | 0.37272 | +0.63% | 2.45x |
| 3 | NEAR/USD | 82.870 | 3.0067 | +0.37% | 0.42x |
| 4 | PUMP/USD | 80.047 | 0.00255 | -0.08% | 0.18x |
| 5 | VVV/USD | 77.164 | 25.867 | -0.37% | 0.68x |
| 6 | PIEVERSE/USD | 69.422 | 3.6769 | +1.04% | 0.24x |
| 7 | ETH/USD | 67.882 | 1713.31 | -0.10% | 0.82x |
| 8 | HYPE/USD | 67.343 | 62.39 | -0.43% | 0.40x |
| 9 | WLD/USD | 67.192 | 0.2394 | +0.89% | 2.49x |
| 10 | XBT/USD | 61.473 | 60646.3 | -0.13% | 1.05x |
| 11 | LINK/USD | 59.160 | 8.79638 | -0.19% | 2.91x |
| 12 | BNB/USD | 47.357 | 556.56 | -0.28% | 2.00x |

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

- Persisted scans: 1324; predictions: 10807; observations: 801424.
- Matured sampled outcomes across 1/6/24/48h: 16270; gap abstentions: 22342. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 61 (sampled only; not a success-rate estimate).
- False positives / missed movers: NOT VERIFIED without eligible continuous outcome coverage.
- Baseline vs challenger: recorded as-of; unbiased held-out lift NOT MEASURED.
- Online Kraken /USD stablecoin-base pairs excluded: 18 (counted from this scan's online AssetPairs metadata, not inferred from price).
- Stablecoin base exclusions: BRL1, BUSD, DAI, EUR, EURC, EUROP, EURQ, EURR, EURT, FDUSD, FRAX, GUSD, PYUSD, QCAD, RLUSD, TGBP, TUSD, USD, USD1, USDC, USDD, USDE, USDG, USDQ, USDR, USDS, USDT, ZUSD.
- DEX: NOT USED; no DEX freshness gate.
- OHLC screening abstentions: 9; details in immutable scan JSON artifact.
- Storage: ledger and results published in one non-force Git commit and read back. Independent artifact recovery is NOT VERIFIED by this scan alone.
- Errors: none in successful committed scan; a failed workflow must not publish a SUCCESS report.

# Cryptoscanner — challenger and independent legacy-inspired WATCH

Paper only · risk is high or higher · 30%+ in 48h probability NOT CALIBRATED
Signal confidence 0–100 means setup strength only, NOT a win probability. Actions are research guidance; no trade authorization.

**Writer:** 45059149947 · **Generation:** 1324 · **Legacy run:** 45059149947
**Main quote time:** 2026-11-22T19:11:46.286313+00:00 · **Legacy report time:** 2026-11-22T19:12:53.681419+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | DRV/USD ⭐ | 0.37272 | 102.10 | +0.63% | 2.45x | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 2 | WLD/USD ⭐ | 0.2394 | 86.54 | +0.89% | 2.49x | STRONG 100/100 | HIGH 60/100 | Consider small entry |
| 3 | NIGHT/USD | 0.04884 | 83.04 | -0.16% | 0.75x | WEAK 42/100 | VERY_HIGH 74/100 | Watch |
| 4 | NEAR/USD | 3.0067 | 78.92 | +0.37% | 0.42x | MODERATE 69/100 | VERY_HIGH 70/100 | Watch |
| 5 | LINK/USD | 8.79638 | 73.21 | -0.19% | 2.91x | MODERATE 67/100 | HIGH 61/100 | Watch |
| 6 | VVV/USD | 25.867 | 72.16 | -0.37% | 0.68x | WEAK 36/100 | VERY_HIGH 82/100 | Watch |
| 7 | PUMP/USD | 0.00255 | 71.43 | -0.08% | 0.18x | WEAK 36/100 | VERY_HIGH 82/100 | Watch |
| 8 | PIEVERSE/USD | 3.6769 | 67.03 | +1.04% | 0.24x | MODERATE 54/100 | VERY_HIGH 82/100 | Watch |
| 9 | ETH/USD | 1713.31 | 65.57 | -0.10% | 0.82x | WEAK 38/100 | HIGH 68/100 | Watch |
| 10 | XBT/USD | 60646.3 | 61.29 | -0.13% | 1.05x | WEAK 41/100 | HIGH 68/100 | Watch |
| 11 | HYPE/USD | 62.39 | 59.15 | -0.43% | 0.40x | WEAK 35/100 | VERY_HIGH 76/100 | Watch |
| 12 | BNB/USD | 556.56 | 55.95 | -0.28% | 2.00x | MODERATE 58/100 | HIGH 61/100 | Watch |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | DRV/USD ⭐ | 0.37272 | 86.16 | +0.63% | 2.45x | 18452 | STRONG 100/100 | HIGH 61/100 | Consider small entry |
| 2 | WLD/USD ⭐ | 0.239 | 78.62 | +0.89% | 2.49x | 2401 | STRONG 100/100 | HIGH 60/100 | Consider small entry |

**Same-run overlap:** DRV/USD, WLD/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
