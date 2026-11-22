# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-22T09:21:04.353025+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/45006981615
**Source SHA:** 4066e028afbd46ef7ad268722dcaaaa2ca6a4e7e
**Previous ledger commit:** 936f67c8073e641104c2f86b8255953b26387786 (atomic ledger/results publication)
**Ledger generation:** 1263 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 6s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 628; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 610; valid market observations: 609; OHLC screened: 24.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | ZEC/USD | 795.28 | 61.509 | 67.499 | +2.20% | +0.27% | 0.27x | 5.8 | 2026-11-22T09:20:58.664440+00:00 | Not calibrated | MODERATE 61/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 2 | TAO/USD | 190.6045 | 60.867 | 67.543 | +2.63% | +0.10% | 0.28x | 10.7 | 2026-11-22T09:20:58.664440+00:00 | Not calibrated | MODERATE 45/100 | VERY_HIGH 76/100 | Watch | WATCH |
| 3 | NEAR/USD | 2.9261 | 58.167 | 62.091 | +1.38% | +0.05% | 0.58x | 5.1 | 2026-11-22T09:20:58.664440+00:00 | Not calibrated | MODERATE 49/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 4 | ASTER/USD | 0.50224 | 55.312 | 55.847 | +3.42% | +0.53% | 0.68x | 5.0 | 2026-11-22T09:20:58.664440+00:00 | Not calibrated | MODERATE 58/100 | VERY_HIGH 75/100 | Watch | WATCH |
| 5 | VVV/USD | 25.305 | 54.599 | 63.026 | +1.63% | -0.14% | 0.23x | 6.7 | 2026-11-22T09:20:58.664440+00:00 | Not calibrated | WEAK 32/100 | VERY_HIGH 76/100 | Do nothing | WATCH |
| 6 | SUI/USD | 0.6508 | 53.937 | 58.018 | +0.54% | +0.42% | 0.38x | 1.5 | 2026-11-22T09:20:58.664440+00:00 | Not calibrated | MODERATE 57/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 7 | ETH/USD | 1687.87 | 48.992 | 57.296 | +0.33% | +0.16% | 0.09x | 0.1 | 2026-11-22T09:20:58.664440+00:00 | Not calibrated | WEAK 44/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 8 | PUMP/USD | 0.002408 | 48.900 | 54.906 | +2.73% | +0.46% | 0.17x | 12.5 | 2026-11-22T09:20:58.664440+00:00 | Not calibrated | MODERATE 49/100 | VERY_HIGH 76/100 | Watch | WATCH |
| 9 | LINK/USD | 8.64687 | 46.757 | 55.400 | +0.60% | +0.15% | 0.06x | 1.6 | 2026-11-22T09:20:58.664440+00:00 | Not calibrated | WEAK 43/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 10 | AVAX/USD | 6.611 | 41.807 | 48.389 | +0.73% | +0.20% | 0.24x | 3.0 | 2026-11-22T09:20:58.664440+00:00 | Not calibrated | WEAK 41/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 11 | AI/USD | 0.01574 | 29.129 | 53.717 | +11.79% | -3.08% | 0.08x | 44.1 | 2026-11-22T09:20:58.664440+00:00 | Not calibrated | WEAK 5/100 | EXTREME 100/100 | Do nothing | WATCH |
| 12 | DOT/USD | 0.6565 | 25.729 | 32.675 | +0.54% | +0.32% | 0.14x | 7.6 | 2026-11-22T09:20:58.664440+00:00 | Not calibrated | WEAK 43/100 | VERY_HIGH 75/100 | Watch | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | TAO/USD | 67.543 | 190.6045 | +0.10% | 0.28x |
| 2 | ZEC/USD | 67.499 | 795.28 | +0.27% | 0.27x |
| 3 | VVV/USD | 63.026 | 25.305 | -0.14% | 0.23x |
| 4 | NEAR/USD | 62.091 | 2.9261 | +0.05% | 0.58x |
| 5 | SUI/USD | 58.018 | 0.6508 | +0.42% | 0.38x |
| 6 | ETH/USD | 57.296 | 1687.87 | +0.16% | 0.09x |
| 7 | ASTER/USD | 55.847 | 0.50224 | +0.53% | 0.68x |
| 8 | LINK/USD | 55.400 | 8.64687 | +0.15% | 0.06x |
| 9 | PUMP/USD | 54.906 | 0.002408 | +0.46% | 0.17x |
| 10 | AI/USD | 53.717 | 0.01574 | -3.08% | 0.08x |
| 11 | AVAX/USD | 48.389 | 6.611 | +0.20% | 0.24x |
| 12 | DOT/USD | 32.675 | 0.6565 | +0.32% | 0.14x |

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

- Persisted scans: 1263; predictions: 10078; observations: 764276.
- Matured sampled outcomes across 1/6/24/48h: 14502; gap abstentions: 22152. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 59 (sampled only; not a success-rate estimate).
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

**Writer:** 45006981615 · **Generation:** 1263 · **Legacy run:** 45006981615
**Main quote time:** 2026-11-22T09:21:04.353025+00:00 · **Legacy report time:** 2026-11-22T09:21:48.738880+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | ZEC/USD | 795.28 | 61.51 | +0.27% | 0.27x | MODERATE 61/100 | VERY_HIGH 70/100 | Watch |
| 2 | TAO/USD | 190.6045 | 60.87 | +0.10% | 0.28x | MODERATE 45/100 | VERY_HIGH 76/100 | Watch |
| 3 | NEAR/USD | 2.9261 | 58.17 | +0.05% | 0.58x | MODERATE 49/100 | VERY_HIGH 70/100 | Watch |
| 4 | ASTER/USD | 0.50224 | 55.31 | +0.53% | 0.68x | MODERATE 58/100 | VERY_HIGH 75/100 | Watch |
| 5 | VVV/USD | 25.305 | 54.60 | -0.14% | 0.23x | WEAK 32/100 | VERY_HIGH 76/100 | Do nothing |
| 6 | SUI/USD | 0.6508 | 53.94 | +0.42% | 0.38x | MODERATE 57/100 | VERY_HIGH 70/100 | Watch |
| 7 | ETH/USD | 1687.87 | 48.99 | +0.16% | 0.09x | WEAK 44/100 | VERY_HIGH 70/100 | Watch |
| 8 | PUMP/USD | 0.002408 | 48.90 | +0.46% | 0.17x | MODERATE 49/100 | VERY_HIGH 76/100 | Watch |
| 9 | LINK/USD | 8.64687 | 46.76 | +0.15% | 0.06x | WEAK 43/100 | VERY_HIGH 70/100 | Watch |
| 10 | AVAX/USD | 6.611 | 41.81 | +0.20% | 0.24x | WEAK 41/100 | VERY_HIGH 70/100 | Watch |
| 11 | AI/USD | 0.01574 | 29.13 | -3.08% | 0.08x | WEAK 5/100 | EXTREME 100/100 | Do nothing |
| 12 | DOT/USD | 0.6565 | 25.73 | +0.32% | 0.14x | WEAK 43/100 | VERY_HIGH 75/100 | Watch |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | ZBCN/USD | 0.001942 | 84.87 | +1.73% | 13.81x | 3637 | STRONG 82/100 | VERY_HIGH 82/100 | Watch |

**Same-run overlap:** None
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
