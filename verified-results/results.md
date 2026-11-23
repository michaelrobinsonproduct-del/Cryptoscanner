# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-23T18:31:59.013302+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/45238964741
**Source SHA:** 858c8bc8ec5d7641ddb39cacd8aca91719f855b1
**Previous ledger commit:** 1dba63be74797e8da7a4266d13274813515f3b39 (atomic ledger/results publication)
**Ledger generation:** 1466 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 8s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 628; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 610; valid market observations: 609; OHLC screened: 24.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | HYPE/USD | 65.39 | 95.102 | 79.335 | +3.69% | +0.15% | 2.77x | 3.1 | 2026-11-23T18:31:50.766915+00:00 | Not calibrated | STRONG 93/100 | HIGH 55/100 | Watch | WATCH |
| 2 | ICP/USD | 2.087 | 92.259 | 76.781 | +6.15% | +0.10% | 12.66x | 9.6 | 2026-11-23T18:31:50.766915+00:00 | Not calibrated | STRONG 91/100 | HIGH 55/100 | Watch | WATCH |
| 3 | INJ/USD | 6.619 | 87.675 | 94.699 | +6.28% | -0.26% | 0.43x | 4.5 | 2026-11-23T18:31:50.766915+00:00 | Not calibrated | MODERATE 49/100 | VERY_HIGH 76/100 | Watch | WATCH |
| 4 | CAP/USD | 0.103242 | 86.267 | 75.113 | +10.33% | +0.07% | 2.08x | 6.1 | 2026-11-23T18:31:50.766915+00:00 | Not calibrated | STRONG 88/100 | HIGH 60/100 | Watch | WATCH |
| 5 | SUI/USD | 0.6866 | 85.950 | 87.260 | +4.71% | +0.01% | 0.86x | 1.5 | 2026-11-23T18:31:50.766915+00:00 | Not calibrated | MODERATE 63/100 | HIGH 62/100 | Watch | WATCH |
| 6 | UNI/USD | 4.9483 | 85.408 | 88.922 | +5.71% | +0.15% | 0.57x | 4.2 | 2026-11-23T18:31:50.766915+00:00 | Not calibrated | MODERATE 63/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 7 | LTC/USD | 41.94 | 78.228 | 84.836 | +4.43% | -0.12% | 0.40x | 2.4 | 2026-11-23T18:31:50.766915+00:00 | Not calibrated | WEAK 44/100 | VERY_HIGH 76/100 | Watch | WATCH |
| 8 | ADA/USD | 0.150414 | 77.182 | 80.870 | +4.02% | -0.41% | 0.83x | 4.5 | 2026-11-23T18:31:50.766915+00:00 | Not calibrated | WEAK 44/100 | HIGH 68/100 | Watch | WATCH |
| 9 | XLM/USD | 0.131518 | 76.495 | 76.863 | +3.13% | -0.28% | 1.11x | 0.1 | 2026-11-23T18:31:50.766915+00:00 | Not calibrated | MODERATE 48/100 | HIGH 68/100 | Watch | WATCH |
| 10 | CC/USD | 0.07824 | 75.048 | 78.365 | +6.78% | -0.06% | 0.70x | 6.4 | 2026-11-23T18:31:50.766915+00:00 | Not calibrated | WEAK 43/100 | VERY_HIGH 81/100 | Watch | WATCH |
| 11 | SOL/USD | 73.58 | 74.640 | 83.557 | +4.18% | -0.03% | 0.12x | 1.4 | 2026-11-23T18:31:50.766915+00:00 | Not calibrated | WEAK 42/100 | VERY_HIGH 76/100 | Watch | WATCH |
| 12 | XMR/USD | 507.94 | 73.921 | 75.077 | +2.88% | +0.62% | 0.58x | 0.2 | 2026-11-23T18:31:50.766915+00:00 | Not calibrated | MODERATE 67/100 | VERY_HIGH 70/100 | Watch | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | INJ/USD | 94.699 | 6.619 | -0.26% | 0.43x |
| 2 | UNI/USD | 88.922 | 4.9483 | +0.15% | 0.57x |
| 3 | SUI/USD | 87.260 | 0.6866 | +0.01% | 0.86x |
| 4 | LTC/USD | 84.836 | 41.94 | -0.12% | 0.40x |
| 5 | SOL/USD | 83.557 | 73.58 | -0.03% | 0.12x |
| 6 | ADA/USD | 80.870 | 0.150414 | -0.41% | 0.83x |
| 7 | HYPE/USD | 79.335 | 65.39 | +0.15% | 2.77x |
| 8 | CC/USD | 78.365 | 0.07824 | -0.06% | 0.70x |
| 9 | XLM/USD | 76.863 | 0.131518 | -0.28% | 1.11x |
| 10 | ICP/USD | 76.781 | 2.087 | +0.10% | 12.66x |
| 11 | CAP/USD | 75.113 | 0.103242 | +0.07% | 2.08x |
| 12 | XMR/USD | 75.077 | 507.94 | +0.62% | 0.58x |

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

- Persisted scans: 1466; predictions: 12359; observations: 887896.
- Matured sampled outcomes across 1/6/24/48h: 21712; gap abstentions: 22370. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 131 (sampled only; not a success-rate estimate).
- False positives / missed movers: NOT VERIFIED without eligible continuous outcome coverage.
- Baseline vs challenger: recorded as-of; unbiased held-out lift NOT MEASURED.
- Online Kraken /USD stablecoin-base pairs excluded: 18 (counted from this scan's online AssetPairs metadata, not inferred from price).
- Stablecoin base exclusions: BRL1, BUSD, DAI, EUR, EURC, EUROP, EURQ, EURR, EURT, FDUSD, FRAX, GUSD, PYUSD, QCAD, RLUSD, TGBP, TUSD, USD, USD1, USDC, USDD, USDE, USDG, USDQ, USDR, USDS, USDT, ZUSD.
- DEX: NOT USED; no DEX freshness gate.
- OHLC screening abstentions: 2; details in immutable scan JSON artifact.
- Storage: ledger and results published in one non-force Git commit and read back. Independent artifact recovery is NOT VERIFIED by this scan alone.
- Errors: none in successful committed scan; a failed workflow must not publish a SUCCESS report.

# Cryptoscanner — challenger and independent legacy-inspired WATCH

Paper only · risk is high or higher · 30%+ in 48h probability NOT CALIBRATED
Signal confidence 0–100 means setup strength only, NOT a win probability. Actions are research guidance; no trade authorization.

**Writer:** 45238964741 · **Generation:** 1466 · **Legacy run:** 45238964741
**Main quote time:** 2026-11-23T18:31:59.013302+00:00 · **Legacy report time:** 2026-11-23T18:32:55.430328+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | HYPE/USD ⭐ | 65.39 | 95.10 | +0.15% | 2.77x | STRONG 100/100 | HIGH 55/100 | Watch |
| 2 | ICP/USD | 2.087 | 92.26 | +0.10% | 12.66x | STRONG 91/100 | HIGH 55/100 | Watch |
| 3 | INJ/USD | 6.619 | 87.67 | -0.26% | 0.43x | MODERATE 49/100 | VERY_HIGH 76/100 | Watch |
| 4 | CAP/USD | 0.103242 | 86.27 | +0.07% | 2.08x | STRONG 88/100 | HIGH 60/100 | Watch |
| 5 | SUI/USD | 0.6866 | 85.95 | +0.01% | 0.86x | MODERATE 63/100 | HIGH 62/100 | Watch |
| 6 | UNI/USD | 4.9483 | 85.41 | +0.15% | 0.57x | MODERATE 63/100 | VERY_HIGH 70/100 | Watch |
| 7 | LTC/USD | 41.94 | 78.23 | -0.12% | 0.40x | WEAK 44/100 | VERY_HIGH 76/100 | Watch |
| 8 | ADA/USD | 0.150414 | 77.18 | -0.41% | 0.83x | WEAK 44/100 | HIGH 68/100 | Watch |
| 9 | XLM/USD | 0.131518 | 76.49 | -0.28% | 1.11x | MODERATE 48/100 | HIGH 68/100 | Watch |
| 10 | CC/USD | 0.07824 | 75.05 | -0.06% | 0.70x | WEAK 43/100 | VERY_HIGH 81/100 | Watch |
| 11 | SOL/USD | 73.58 | 74.64 | -0.03% | 0.12x | WEAK 42/100 | VERY_HIGH 76/100 | Watch |
| 12 | XMR/USD | 507.94 | 73.92 | +0.62% | 0.58x | MODERATE 67/100 | VERY_HIGH 70/100 | Watch |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | HYPE/USD ⭐ | 65.33 | 96.60 | +0.15% | 2.77x | 24088 | STRONG 100/100 | HIGH 55/100 | Watch |

**Same-run overlap:** HYPE/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
