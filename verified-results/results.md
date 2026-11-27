# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-27T01:41:30.392013+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/45923812116
**Source SHA:** 858c8bc8ec5d7641ddb39cacd8aca91719f855b1
**Previous ledger commit:** 80254a4bf7d4fb645775d2fe5d21ae047a3d2a41 (atomic ledger/results publication)
**Ledger generation:** 1941 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 9s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 628; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 610; valid market observations: 601; OHLC screened: 24.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | ZEC/USD | 705.53 | 73.551 | 76.606 | +3.50% | +0.01% | 0.69x | 5.8 | 2026-11-27T01:41:21.796075+00:00 | Not calibrated | MODERATE 57/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 2 | SOL/USD | 71.31 | 69.572 | 57.950 | +0.52% | -0.04% | 2.18x | 1.4 | 2026-11-27T01:41:21.796075+00:00 | Not calibrated | MODERATE 65/100 | HIGH 61/100 | Watch | WATCH |
| 3 | ADA/USD | 0.149218 | 60.455 | 55.527 | +0.51% | +0.08% | 1.45x | 2.5 | 2026-11-27T01:41:21.796075+00:00 | Not calibrated | MODERATE 65/100 | HIGH 55/100 | Watch | WATCH |
| 4 | ETH/USD | 1697.24 | 59.704 | 58.936 | +0.57% | -0.01% | 1.08x | 0.1 | 2026-11-27T01:41:21.796075+00:00 | Not calibrated | WEAK 40/100 | HIGH 68/100 | Watch | WATCH |
| 5 | PEPE/USD | 3.509e-06 | 58.372 | 44.226 | +0.89% | -0.17% | 5.42x | 2.8 | 2026-11-27T01:41:21.796075+00:00 | Not calibrated | MODERATE 59/100 | HIGH 61/100 | Watch | WATCH |
| 6 | LTC/USD | 44.22 | 58.269 | 61.551 | +1.10% | +0.29% | 0.52x | 2.3 | 2026-11-27T01:41:21.796075+00:00 | Not calibrated | MODERATE 59/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 7 | XRP/USD | 0.94723 | 57.724 | 57.904 | +0.48% | +0.01% | 0.98x | 0.8 | 2026-11-27T01:41:21.796075+00:00 | Not calibrated | MODERATE 49/100 | HIGH 62/100 | Watch | WATCH |
| 8 | HYPE/USD | 62.65 | 56.249 | 59.041 | +0.69% | -0.22% | 0.83x | 1.6 | 2026-11-27T01:41:21.796075+00:00 | Not calibrated | WEAK 33/100 | HIGH 68/100 | Do nothing | WATCH |
| 9 | XDG/USD | 0.0566513 | 56.204 | 44.550 | +0.49% | +0.09% | 2.12x | 0.0 | 2026-11-27T01:41:21.796075+00:00 | Not calibrated | STRONG 73/100 | HIGH 55/100 | Watch | WATCH |
| 10 | AAVE/USD | 94.77 | 53.598 | 38.703 | +0.31% | -0.02% | 3.12x | 4.2 | 2026-11-27T01:41:21.796075+00:00 | Not calibrated | MODERATE 57/100 | HIGH 61/100 | Watch | WATCH |
| 11 | TIA/USD | 0.3403 | 50.866 | 38.934 | +1.19% | +0.24% | 2.08x | 2.9 | 2026-11-27T01:41:21.796075+00:00 | Not calibrated | STRONG 80/100 | HIGH 60/100 | Watch | WATCH |
| 12 | NEAR/USD | 3.0572 | 50.260 | 54.685 | +0.31% | -0.30% | 0.71x | 4.9 | 2026-11-27T01:41:21.796075+00:00 | Not calibrated | WEAK 30/100 | VERY_HIGH 76/100 | Do nothing | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | ZEC/USD | 76.606 | 705.53 | +0.01% | 0.69x |
| 2 | LTC/USD | 61.551 | 44.22 | +0.29% | 0.52x |
| 3 | HYPE/USD | 59.041 | 62.65 | -0.22% | 0.83x |
| 4 | ETH/USD | 58.936 | 1697.24 | -0.01% | 1.08x |
| 5 | SOL/USD | 57.950 | 71.31 | -0.04% | 2.18x |
| 6 | XRP/USD | 57.904 | 0.94723 | +0.01% | 0.98x |
| 7 | ADA/USD | 55.527 | 0.149218 | +0.08% | 1.45x |
| 8 | NEAR/USD | 54.685 | 3.0572 | -0.30% | 0.71x |
| 9 | XDG/USD | 44.550 | 0.0566513 | +0.09% | 2.12x |
| 10 | PEPE/USD | 44.226 | 3.509e-06 | -0.17% | 5.42x |
| 11 | TIA/USD | 38.934 | 0.3403 | +0.24% | 2.08x |
| 12 | AAVE/USD | 38.703 | 94.77 | -0.02% | 3.12x |

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

- Persisted scans: 1941; predictions: 16994; observations: 1175626.
- Matured sampled outcomes across 1/6/24/48h: 37275; gap abstentions: 25437. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 150 (sampled only; not a success-rate estimate).
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

**Writer:** 45923812116 · **Generation:** 1941 · **Legacy run:** 45923812116
**Main quote time:** 2026-11-27T01:41:30.392013+00:00 · **Legacy report time:** 2026-11-27T01:42:17.126542+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | ZEC/USD | 705.53 | 73.55 | +0.01% | 0.69x | MODERATE 57/100 | VERY_HIGH 70/100 | Watch |
| 2 | SOL/USD | 71.31 | 69.57 | -0.04% | 2.18x | MODERATE 65/100 | HIGH 61/100 | Watch |
| 3 | ADA/USD ⭐ | 0.149218 | 60.45 | +0.08% | 1.45x | STRONG 75/100 | HIGH 55/100 | Watch |
| 4 | ETH/USD | 1697.24 | 59.70 | -0.01% | 1.08x | WEAK 40/100 | HIGH 68/100 | Watch |
| 5 | PEPE/USD | 3.509e-06 | 58.37 | -0.17% | 5.42x | MODERATE 59/100 | HIGH 61/100 | Watch |
| 6 | LTC/USD | 44.22 | 58.27 | +0.29% | 0.52x | MODERATE 59/100 | VERY_HIGH 70/100 | Watch |
| 7 | XRP/USD | 0.94723 | 57.72 | +0.01% | 0.98x | MODERATE 49/100 | HIGH 62/100 | Watch |
| 8 | HYPE/USD | 62.65 | 56.25 | -0.22% | 0.83x | WEAK 33/100 | HIGH 68/100 | Do nothing |
| 9 | XDG/USD ⭐ | 0.0566513 | 56.20 | +0.09% | 2.12x | STRONG 83/100 | HIGH 55/100 | Watch |
| 10 | AAVE/USD | 94.77 | 53.60 | -0.02% | 3.12x | MODERATE 57/100 | HIGH 61/100 | Watch |
| 11 | TIA/USD | 0.3403 | 50.87 | +0.24% | 2.08x | STRONG 80/100 | HIGH 60/100 | Watch |
| 12 | NEAR/USD | 3.0572 | 50.26 | -0.30% | 0.71x | WEAK 30/100 | VERY_HIGH 76/100 | Do nothing |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | SUI/USD | 0.6706 | 55.95 | +0.19% | 19.63x | 4413 | STRONG 73/100 | HIGH 55/100 | Watch |
| 2 | XDG/USD ⭐ | 0.0566664 | 54.60 | +0.09% | 2.12x | 5047 | STRONG 82/100 | HIGH 55/100 | Watch |
| 3 | ADA/USD ⭐ | 0.149218 | 51.07 | +0.08% | 1.45x | 10040 | STRONG 71/100 | HIGH 55/100 | Watch |
| 4 | PIEVERSE/USD | 3.9473 | 50.56 | +0.06% | 1.78x | 3174 | MODERATE 45/100 | HIGH 67/100 | Watch |

**Same-run overlap:** ADA/USD, XDG/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
