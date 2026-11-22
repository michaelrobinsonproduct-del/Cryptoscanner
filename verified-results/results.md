# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-22T12:11:02.797835+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/45020834349
**Source SHA:** 17af11513c515cf2dc9dda8017f091d9b1f13397
**Previous ledger commit:** 6effb48493ad0d45c8e351ae86c4b205f26bccf8 (atomic ledger/results publication)
**Ledger generation:** 1281 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 6s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 628; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 610; valid market observations: 609; OHLC screened: 24.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | NIGHT/USD | 0.04706 | 86.084 | 83.857 | +6.28% | +0.62% | 0.91x | 10.6 | 2026-11-22T12:10:56.922429+00:00 | Not calibrated | MODERATE 68/100 | HIGH 68/100 | Watch | WATCH |
| 2 | NEAR/USD | 2.9986 | 78.003 | 80.235 | +3.89% | +0.62% | 0.47x | 4.0 | 2026-11-22T12:10:56.922429+00:00 | Not calibrated | MODERATE 69/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 3 | PUMP/USD | 0.002489 | 75.731 | 81.198 | +6.19% | +0.12% | 0.39x | 8.0 | 2026-11-22T12:10:56.922429+00:00 | Not calibrated | MODERATE 58/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 4 | HYPE/USD | 62.68 | 75.274 | 69.864 | +2.35% | +0.08% | 1.50x | 3.2 | 2026-11-22T12:10:56.922429+00:00 | Not calibrated | STRONG 73/100 | HIGH 55/100 | Watch | WATCH |
| 5 | INJ/USD | 6.238 | 73.746 | 71.706 | +4.44% | +0.42% | 0.99x | 3.2 | 2026-11-22T12:10:56.922429+00:00 | Not calibrated | MODERATE 67/100 | HIGH 62/100 | Watch | WATCH |
| 6 | XBT/USD | 61102.2 | 73.686 | 66.784 | +1.68% | +0.27% | 1.56x | 0.0 | 2026-11-22T12:10:56.922429+00:00 | Not calibrated | STRONG 82/100 | HIGH 55/100 | Consider small entry | WATCH |
| 7 | TAO/USD | 191.1158 | 71.181 | 69.546 | +2.90% | +0.48% | 0.92x | 6.0 | 2026-11-22T12:10:56.922429+00:00 | Not calibrated | MODERATE 66/100 | HIGH 62/100 | Watch | WATCH |
| 8 | XLM/USD | 0.129347 | 67.319 | 52.264 | +0.43% | +0.01% | 6.41x | 4.1 | 2026-11-22T12:10:56.922429+00:00 | Not calibrated | STRONG 79/100 | HIGH 55/100 | Watch | WATCH |
| 9 | SUI/USD | 0.6603 | 65.153 | 68.301 | +2.01% | +0.11% | 0.63x | 1.5 | 2026-11-22T12:10:56.922429+00:00 | Not calibrated | MODERATE 53/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 10 | ETH/USD | 1709.92 | 63.346 | 66.472 | +1.64% | +0.22% | 0.58x | 0.1 | 2026-11-22T12:10:56.922429+00:00 | Not calibrated | MODERATE 62/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 11 | ZEC/USD | 797.12 | 61.326 | 69.914 | +2.44% | -0.02% | 0.15x | 4.3 | 2026-11-22T12:10:56.922429+00:00 | Not calibrated | WEAK 36/100 | VERY_HIGH 76/100 | Watch | WATCH |
| 12 | CRV/USD | 0.18588 | 60.645 | 69.757 | +4.22% | -0.02% | 0.10x | 9.7 | 2026-11-22T12:10:56.922429+00:00 | Not calibrated | WEAK 35/100 | VERY_HIGH 76/100 | Watch | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | NIGHT/USD | 83.857 | 0.04706 | +0.62% | 0.91x |
| 2 | PUMP/USD | 81.198 | 0.002489 | +0.12% | 0.39x |
| 3 | NEAR/USD | 80.235 | 2.9986 | +0.62% | 0.47x |
| 4 | INJ/USD | 71.706 | 6.238 | +0.42% | 0.99x |
| 5 | ZEC/USD | 69.914 | 797.12 | -0.02% | 0.15x |
| 6 | HYPE/USD | 69.864 | 62.68 | +0.08% | 1.50x |
| 7 | CRV/USD | 69.757 | 0.18588 | -0.02% | 0.10x |
| 8 | TAO/USD | 69.546 | 191.1158 | +0.48% | 0.92x |
| 9 | SUI/USD | 68.301 | 0.6603 | +0.11% | 0.63x |
| 10 | XBT/USD | 66.784 | 61102.2 | +0.27% | 1.56x |
| 11 | ETH/USD | 66.472 | 1709.92 | +0.22% | 0.58x |
| 12 | XLM/USD | 52.264 | 0.129347 | +0.01% | 6.41x |

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

- Persisted scans: 1281; predictions: 10292; observations: 775238.
- Matured sampled outcomes across 1/6/24/48h: 14857; gap abstentions: 22233. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 60 (sampled only; not a success-rate estimate).
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

**Writer:** 45020834349 · **Generation:** 1281 · **Legacy run:** 45020834349
**Main quote time:** 2026-11-22T12:11:02.797835+00:00 · **Legacy report time:** 2026-11-22T12:11:46.698028+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | NIGHT/USD | 0.04706 | 86.08 | +0.62% | 0.91x | MODERATE 68/100 | HIGH 68/100 | Watch |
| 2 | NEAR/USD | 2.9986 | 78.00 | +0.62% | 0.47x | MODERATE 69/100 | VERY_HIGH 70/100 | Watch |
| 3 | PUMP/USD | 0.002489 | 75.73 | +0.12% | 0.39x | MODERATE 58/100 | VERY_HIGH 70/100 | Watch |
| 4 | HYPE/USD ⭐ | 62.68 | 75.27 | +0.08% | 1.50x | STRONG 83/100 | HIGH 55/100 | Watch |
| 5 | INJ/USD | 6.238 | 73.75 | +0.42% | 0.99x | MODERATE 67/100 | HIGH 62/100 | Watch |
| 6 | XBT/USD ⭐ | 61102.2 | 73.69 | +0.27% | 1.56x | STRONG 92/100 | HIGH 55/100 | Consider small entry |
| 7 | TAO/USD | 191.1158 | 71.18 | +0.48% | 0.92x | MODERATE 66/100 | HIGH 62/100 | Watch |
| 8 | XLM/USD | 0.129347 | 67.32 | +0.01% | 6.41x | STRONG 79/100 | HIGH 55/100 | Watch |
| 9 | SUI/USD | 0.6603 | 65.15 | +0.11% | 0.63x | MODERATE 53/100 | VERY_HIGH 70/100 | Watch |
| 10 | ETH/USD | 1709.92 | 63.35 | +0.22% | 0.58x | MODERATE 62/100 | VERY_HIGH 70/100 | Watch |
| 11 | ZEC/USD | 797.12 | 61.33 | -0.02% | 0.15x | WEAK 36/100 | VERY_HIGH 76/100 | Watch |
| 12 | CRV/USD | 0.18588 | 60.64 | -0.02% | 0.10x | WEAK 35/100 | VERY_HIGH 76/100 | Watch |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | HYPE/USD ⭐ | 62.71 | 79.86 | +0.08% | 1.50x | 13482 | STRONG 85/100 | HIGH 55/100 | Watch |
| 2 | XBT/USD ⭐ | 61086.8 | 74.90 | +0.27% | 1.56x | 144763 | STRONG 92/100 | HIGH 55/100 | Consider small entry |
| 3 | LINK/USD | 8.81161 | 73.45 | +0.25% | 1.61x | 5859 | STRONG 82/100 | HIGH 55/100 | Consider small entry |
| 4 | ENA/USD | 0.1026 | 73.27 | +0.20% | 1.25x | 2393 | MODERATE 62/100 | HIGH 60/100 | Watch |

**Same-run overlap:** HYPE/USD, XBT/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
