# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-22T08:21:13.346754+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/45002273828
**Source SHA:** 4066e028afbd46ef7ad268722dcaaaa2ca6a4e7e
**Previous ledger commit:** 5396358d19f2218a686e4b673fa4a6c02e653f23 (atomic ledger/results publication)
**Ledger generation:** 1256 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 8s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 628; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 610; valid market observations: 609; OHLC screened: 24.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | VVV/USD | 25.392 | 79.885 | 63.911 | +1.98% | +1.17% | 2.01x | 9.8 | 2026-11-22T08:21:04.926685+00:00 | Not calibrated | STRONG 95/100 | HIGH 55/100 | Consider small entry | WATCH |
| 2 | NEAR/USD | 2.898 | 74.871 | 55.075 | +0.41% | +0.96% | 2.82x | 5.5 | 2026-11-22T08:21:04.926685+00:00 | Not calibrated | STRONG 92/100 | HIGH 55/100 | Consider small entry | WATCH |
| 3 | TAO/USD | 188.7394 | 68.215 | 61.505 | +1.62% | +1.13% | 1.10x | 9.7 | 2026-11-22T08:21:04.926685+00:00 | Not calibrated | MODERATE 69/100 | HIGH 62/100 | Watch | WATCH |
| 4 | LINK/USD | 8.62143 | 67.432 | 49.846 | +0.31% | +0.65% | 2.44x | 8.1 | 2026-11-22T08:21:04.926685+00:00 | Not calibrated | STRONG 89/100 | HIGH 55/100 | Watch | WATCH |
| 5 | ZBCN/USD | 0.001825 | 66.716 | 52.809 | +5.67% | -0.22% | 5.99x | 38.5 | 2026-11-22T08:21:04.926685+00:00 | Not calibrated | MODERATE 48/100 | VERY_HIGH 78/100 | Watch | WATCH |
| 6 | ASTER/USD | 0.49687 | 66.691 | 47.715 | +2.31% | +0.80% | 3.24x | 6.2 | 2026-11-22T08:21:04.926685+00:00 | Not calibrated | STRONG 88/100 | HIGH 60/100 | Watch | WATCH |
| 7 | INJ/USD | 6.094 | 61.576 | 38.439 | +2.03% | +1.63% | 3.72x | 31.3 | 2026-11-22T08:21:04.926685+00:00 | Not calibrated | STRONG 76/100 | HIGH 67/100 | Watch | WATCH |
| 8 | ZEC/USD | 787.3 | 57.116 | 60.169 | +1.17% | +0.45% | 0.47x | 6.1 | 2026-11-22T08:21:04.926685+00:00 | Not calibrated | MODERATE 59/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 9 | ENA/USD | 0.0986 | 51.620 | 33.045 | +0.31% | +0.71% | 2.52x | 10.1 | 2026-11-22T08:21:04.926685+00:00 | Not calibrated | STRONG 76/100 | HIGH 66/100 | Watch | WATCH |
| 10 | PEARL/USD | 1.9799 | 42.006 | 40.671 | +1.62% | +0.11% | 1.08x | 25.3 | 2026-11-22T08:21:04.926685+00:00 | Not calibrated | WEAK 36/100 | VERY_HIGH 74/100 | Watch | WATCH |
| 11 | NIGHT/USD | 0.04469 | 34.816 | 45.208 | +0.93% | -0.27% | 0.09x | 11.2 | 2026-11-22T08:21:04.926685+00:00 | Not calibrated | WEAK 17/100 | VERY_HIGH 82/100 | Do nothing | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | VVV/USD | 63.911 | 25.392 | +1.17% | 2.01x |
| 2 | TAO/USD | 61.505 | 188.7394 | +1.13% | 1.10x |
| 3 | ZEC/USD | 60.169 | 787.3 | +0.45% | 0.47x |
| 4 | NEAR/USD | 55.075 | 2.898 | +0.96% | 2.82x |
| 5 | ZBCN/USD | 52.809 | 0.001825 | -0.22% | 5.99x |
| 6 | LINK/USD | 49.846 | 8.62143 | +0.65% | 2.44x |
| 7 | ASTER/USD | 47.715 | 0.49687 | +0.80% | 3.24x |
| 8 | NIGHT/USD | 45.208 | 0.04469 | -0.27% | 0.09x |
| 9 | PEARL/USD | 40.671 | 1.9799 | +0.11% | 1.08x |
| 10 | INJ/USD | 38.439 | 6.094 | +1.63% | 3.72x |
| 11 | ENA/USD | 33.045 | 0.0986 | +0.71% | 2.52x |

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

- Persisted scans: 1256; predictions: 10001; observations: 760014.
- Matured sampled outcomes across 1/6/24/48h: 14396; gap abstentions: 22094. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 59 (sampled only; not a success-rate estimate).
- False positives / missed movers: NOT VERIFIED without eligible continuous outcome coverage.
- Baseline vs challenger: recorded as-of; unbiased held-out lift NOT MEASURED.
- Online Kraken /USD stablecoin-base pairs excluded: 18 (counted from this scan's online AssetPairs metadata, not inferred from price).
- Stablecoin base exclusions: BRL1, BUSD, DAI, EUR, EURC, EUROP, EURQ, EURR, EURT, FDUSD, FRAX, GUSD, PYUSD, QCAD, RLUSD, TGBP, TUSD, USD, USD1, USDC, USDD, USDE, USDG, USDQ, USDR, USDS, USDT, ZUSD.
- DEX: NOT USED; no DEX freshness gate.
- OHLC screening abstentions: 13; details in immutable scan JSON artifact.
- Storage: ledger and results published in one non-force Git commit and read back. Independent artifact recovery is NOT VERIFIED by this scan alone.
- Errors: none in successful committed scan; a failed workflow must not publish a SUCCESS report.

# Cryptoscanner — challenger and independent legacy-inspired WATCH

Paper only · risk is high or higher · 30%+ in 48h probability NOT CALIBRATED
Signal confidence 0–100 means setup strength only, NOT a win probability. Actions are research guidance; no trade authorization.

**Writer:** 45002273828 · **Generation:** 1256 · **Legacy run:** 45002273828
**Main quote time:** 2026-11-22T08:21:13.346754+00:00 · **Legacy report time:** 2026-11-22T08:22:17.757639+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | VVV/USD ⭐ | 25.392 | 79.88 | +1.17% | 2.01x | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 2 | NEAR/USD ⭐ | 2.898 | 74.87 | +0.96% | 2.82x | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 3 | TAO/USD ⭐ | 188.7394 | 68.21 | +1.13% | 1.10x | STRONG 79/100 | HIGH 62/100 | Watch |
| 4 | LINK/USD | 8.62143 | 67.43 | +0.65% | 2.44x | STRONG 89/100 | HIGH 55/100 | Watch |
| 5 | ZBCN/USD | 0.001825 | 66.72 | -0.22% | 5.99x | MODERATE 48/100 | VERY_HIGH 78/100 | Watch |
| 6 | ASTER/USD ⭐ | 0.49687 | 66.69 | +0.80% | 3.24x | STRONG 98/100 | HIGH 60/100 | Consider small entry |
| 7 | INJ/USD ⭐ | 6.094 | 61.58 | +1.63% | 3.72x | STRONG 86/100 | HIGH 67/100 | Consider small entry |
| 8 | ZEC/USD | 787.3 | 57.12 | +0.45% | 0.47x | MODERATE 59/100 | VERY_HIGH 70/100 | Watch |
| 9 | ENA/USD | 0.0986 | 51.62 | +0.71% | 2.52x | STRONG 76/100 | HIGH 66/100 | Watch |
| 10 | PEARL/USD ⭐ | 1.9799 | 42.01 | +0.11% | 1.08x | MODERATE 46/100 | VERY_HIGH 74/100 | Watch |
| 11 | NIGHT/USD | 0.04469 | 34.82 | -0.27% | 0.09x | WEAK 17/100 | VERY_HIGH 82/100 | Do nothing |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | VVV/USD ⭐ | 25.614 | 78.97 | +1.17% | 2.01x | 13754 | STRONG 99/100 | HIGH 61/100 | Consider small entry |
| 2 | INJ/USD ⭐ | 6.109 | 68.16 | +1.63% | 3.72x | 5981 | STRONG 99/100 | HIGH 55/100 | Consider small entry |
| 3 | TAO/USD ⭐ | 189.6224 | 65.98 | +1.13% | 1.10x | 7216 | STRONG 78/100 | HIGH 62/100 | Watch |
| 4 | ASTER/USD ⭐ | 0.49831 | 62.32 | +0.80% | 3.24x | 2143 | STRONG 96/100 | HIGH 60/100 | Consider small entry |
| 5 | NEAR/USD ⭐ | 2.9128 | 60.79 | +0.96% | 2.82x | 12202 | STRONG 95/100 | HIGH 55/100 | Consider small entry |
| 6 | PEARL/USD ⭐ | 1.9774 | 47.75 | +0.11% | 1.08x | 8350 | MODERATE 54/100 | HIGH 68/100 | Watch |

**Same-run overlap:** VVV/USD, NEAR/USD, TAO/USD, ASTER/USD, INJ/USD, PEARL/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
