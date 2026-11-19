# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-19T19:30:27.569350+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/44598855676
**Source SHA:** f854bf15990e1aa3564d35bbec4100f929bd3d42
**Previous ledger commit:** 278047eaa156f4554b92c1771fc2d70a8ff1f908 (atomic ledger/results publication)
**Ledger generation:** 844 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 7s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 627; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 609; valid market observations: 599; OHLC screened: 24.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | AKT/USD | 0.5512 | 92.247 | 74.236 | +6.41% | +0.60% | 2.52x | 5.4 | 2026-11-19T19:30:20.783721+00:00 | Not calibrated | STRONG 100/100 | HIGH 60/100 | Consider small entry | WATCH |
| 2 | VVV/USD | 22.616 | 79.396 | 82.867 | +4.36% | +0.43% | 0.44x | 5.3 | 2026-11-19T19:30:20.783721+00:00 | Not calibrated | STRONG 70/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 3 | CT/USD | 0.1305 | 73.593 | 65.382 | +10.41% | +1.87% | 0.88x | 23.1 | 2026-11-19T19:30:20.783721+00:00 | Not calibrated | MODERATE 57/100 | VERY_HIGH 79/100 | Watch | WATCH |
| 4 | ALEO/USD | 0.03108 | 66.177 | 59.663 | +3.67% | +1.30% | 1.00x | 3.2 | 2026-11-19T19:30:20.783721+00:00 | Not calibrated | MODERATE 68/100 | HIGH 67/100 | Watch | WATCH |
| 5 | SENT/USD | 0.021582 | 61.026 | 62.231 | +4.74% | +1.00% | 0.38x | 10.7 | 2026-11-19T19:30:20.783721+00:00 | Not calibrated | MODERATE 56/100 | VERY_HIGH 81/100 | Watch | WATCH |
| 6 | USELESS/USD | 0.09949 | 59.839 | 59.538 | +4.11% | +0.67% | 0.70x | 13.1 | 2026-11-19T19:30:20.783721+00:00 | Not calibrated | MODERATE 55/100 | VERY_HIGH 76/100 | Watch | WATCH |
| 7 | HYPE/USD | 67.88 | 57.431 | 63.256 | +1.50% | +0.10% | 0.37x | 4.4 | 2026-11-19T19:30:20.783721+00:00 | Not calibrated | MODERATE 49/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 8 | ADA/USD | 0.153228 | 56.469 | 62.504 | +1.31% | +0.21% | 0.29x | 3.3 | 2026-11-19T19:30:20.783721+00:00 | Not calibrated | MODERATE 58/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 9 | ONDO/USD | 0.29997 | 55.424 | 39.790 | +0.78% | +0.13% | 10.06x | 3.3 | 2026-11-19T19:30:20.783721+00:00 | Not calibrated | STRONG 73/100 | HIGH 60/100 | Watch | WATCH |
| 10 | SOL/USD | 73.82 | 50.989 | 56.988 | +0.38% | +0.05% | 0.37x | 1.4 | 2026-11-19T19:30:20.783721+00:00 | Not calibrated | MODERATE 45/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 11 | PEPE/USD | 3.76e-06 | 49.605 | 41.093 | +0.37% | +0.27% | 1.72x | 5.3 | 2026-11-19T19:30:20.783721+00:00 | Not calibrated | STRONG 70/100 | HIGH 55/100 | Watch | WATCH |
| 12 | INJ/USD | 7.104 | 48.941 | 54.853 | +1.76% | +0.57% | 0.13x | 5.6 | 2026-11-19T19:30:20.783721+00:00 | Not calibrated | MODERATE 54/100 | VERY_HIGH 70/100 | Watch | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | VVV/USD | 82.867 | 22.616 | +0.43% | 0.44x |
| 2 | AKT/USD | 74.236 | 0.5512 | +0.60% | 2.52x |
| 3 | CT/USD | 65.382 | 0.1305 | +1.87% | 0.88x |
| 4 | HYPE/USD | 63.256 | 67.88 | +0.10% | 0.37x |
| 5 | ADA/USD | 62.504 | 0.153228 | +0.21% | 0.29x |
| 6 | SENT/USD | 62.231 | 0.021582 | +1.00% | 0.38x |
| 7 | ALEO/USD | 59.663 | 0.03108 | +1.30% | 1.00x |
| 8 | USELESS/USD | 59.538 | 0.09949 | +0.67% | 0.70x |
| 9 | SOL/USD | 56.988 | 73.82 | +0.05% | 0.37x |
| 10 | INJ/USD | 54.853 | 7.104 | +0.57% | 0.13x |
| 11 | PEPE/USD | 41.093 | 3.76e-06 | +0.27% | 1.72x |
| 12 | ONDO/USD | 39.790 | 0.29997 | +0.13% | 10.06x |

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

- Persisted scans: 844; predictions: 7272; observations: 510133.
- Matured sampled outcomes across 1/6/24/48h: 7283; gap abstentions: 15596. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 10 (sampled only; not a success-rate estimate).
- False positives / missed movers: NOT VERIFIED without eligible continuous outcome coverage.
- Baseline vs challenger: recorded as-of; unbiased held-out lift NOT MEASURED.
- Online Kraken /USD stablecoin-base pairs excluded: 18 (counted from this scan's online AssetPairs metadata, not inferred from price).
- Stablecoin base exclusions: BRL1, BUSD, DAI, EUR, EURC, EUROP, EURQ, EURR, EURT, FDUSD, FRAX, GUSD, PYUSD, QCAD, RLUSD, TGBP, TUSD, USD, USD1, USDC, USDD, USDE, USDG, USDQ, USDR, USDS, USDT, ZUSD.
- DEX: NOT USED; no DEX freshness gate.
- OHLC screening abstentions: 7; details in immutable scan JSON artifact.
- Storage: ledger and results published in one non-force Git commit and read back. Independent artifact recovery is NOT VERIFIED by this scan alone.
- Errors: none in successful committed scan; a failed workflow must not publish a SUCCESS report.

# Cryptoscanner — challenger and independent legacy-inspired WATCH

Paper only · risk is high or higher · 30%+ in 48h probability NOT CALIBRATED
Signal confidence 0–100 means setup strength only, NOT a win probability. Actions are research guidance; no trade authorization.

**Writer:** 44598855676 · **Generation:** 844 · **Legacy run:** 44598855676
**Main quote time:** 2026-11-19T19:30:27.569350+00:00 · **Legacy report time:** 2026-11-19T19:31:22.127659+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | AKT/USD ⭐ | 0.5512 | 92.25 | +0.60% | 2.52x | STRONG 100/100 | HIGH 60/100 | Consider small entry |
| 2 | VVV/USD | 22.616 | 79.40 | +0.43% | 0.44x | STRONG 70/100 | VERY_HIGH 70/100 | Watch |
| 3 | CT/USD | 0.1305 | 73.59 | +1.87% | 0.88x | MODERATE 57/100 | VERY_HIGH 79/100 | Watch |
| 4 | ALEO/USD ⭐ | 0.03108 | 66.18 | +1.30% | 1.00x | STRONG 78/100 | HIGH 67/100 | Watch |
| 5 | SENT/USD | 0.021582 | 61.03 | +1.00% | 0.38x | MODERATE 56/100 | VERY_HIGH 81/100 | Watch |
| 6 | USELESS/USD | 0.09949 | 59.84 | +0.67% | 0.70x | MODERATE 55/100 | VERY_HIGH 76/100 | Watch |
| 7 | HYPE/USD | 67.88 | 57.43 | +0.10% | 0.37x | MODERATE 49/100 | VERY_HIGH 70/100 | Watch |
| 8 | ADA/USD | 0.153228 | 56.47 | +0.21% | 0.29x | MODERATE 58/100 | VERY_HIGH 70/100 | Watch |
| 9 | ONDO/USD | 0.29997 | 55.42 | +0.13% | 10.06x | STRONG 73/100 | HIGH 60/100 | Watch |
| 10 | SOL/USD | 73.82 | 50.99 | +0.05% | 0.37x | MODERATE 45/100 | VERY_HIGH 70/100 | Watch |
| 11 | PEPE/USD | 3.76e-06 | 49.61 | +0.27% | 1.72x | STRONG 70/100 | HIGH 55/100 | Watch |
| 12 | INJ/USD | 7.104 | 48.94 | +0.57% | 0.13x | MODERATE 54/100 | VERY_HIGH 70/100 | Watch |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | AKT/USD ⭐ | 0.5513 | 79.16 | +0.60% | 2.52x | 3346 | STRONG 100/100 | HIGH 66/100 | Consider small entry |
| 2 | ALEO/USD ⭐ | 0.03093 | 75.81 | +1.30% | 1.00x | 5638 | STRONG 83/100 | HIGH 67/100 | Watch |
| 3 | MEGA/USD | 0.059 | 69.58 | +0.73% | 1.05x | 2147 | MODERATE 65/100 | VERY_HIGH 73/100 | Watch |

**Same-run overlap:** AKT/USD, ALEO/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
