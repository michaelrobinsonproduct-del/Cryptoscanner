# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-27T05:21:24.945866+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/45945123479
**Source SHA:** 858c8bc8ec5d7641ddb39cacd8aca91719f855b1
**Previous ledger commit:** 0447ead827e629635593848f68d3bf209ff741e4 (atomic ledger/results publication)
**Ledger generation:** 1964 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 8s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 628; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 610; valid market observations: 602; OHLC screened: 24.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | ZEC/USD | 760.77 | 96.462 | 97.371 | +11.61% | -0.00% | 0.91x | 5.3 | 2026-11-27T05:21:17.350843+00:00 | Not calibrated | MODERATE 53/100 | HIGH 68/100 | Watch | WATCH |
| 2 | VVV/USD | 27.168 | 95.578 | 77.650 | +3.76% | +0.59% | 3.41x | 7.4 | 2026-11-27T05:21:17.350843+00:00 | Not calibrated | STRONG 100/100 | HIGH 55/100 | Consider small entry | WATCH |
| 3 | SOL/USD | 73.14 | 93.016 | 76.025 | +3.10% | +0.40% | 3.18x | 1.4 | 2026-11-27T05:21:17.350843+00:00 | Not calibrated | STRONG 100/100 | HIGH 55/100 | Consider small entry | WATCH |
| 4 | HYPE/USD | 65.98 | 87.906 | 96.543 | +6.04% | +0.00% | 0.14x | 1.5 | 2026-11-27T05:21:17.350843+00:00 | Not calibrated | MODERATE 64/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 5 | SUI/USD | 0.6849 | 86.893 | 71.161 | +2.58% | +0.15% | 3.29x | 1.5 | 2026-11-27T05:21:17.350843+00:00 | Not calibrated | STRONG 88/100 | HIGH 55/100 | Watch | WATCH |
| 6 | LTC/USD | 44.73 | 81.183 | 69.726 | +2.26% | +0.27% | 2.01x | 2.2 | 2026-11-27T05:21:17.350843+00:00 | Not calibrated | STRONG 96/100 | HIGH 55/100 | Consider small entry | WATCH |
| 7 | LINK/USD | 9.68061 | 79.037 | 86.125 | +4.45% | +0.33% | 0.12x | 0.0 | 2026-11-27T05:21:17.350843+00:00 | Not calibrated | STRONG 70/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 8 | XDG/USD | 0.0578696 | 78.089 | 62.095 | +2.65% | +0.20% | 15.56x | 0.0 | 2026-11-27T05:21:17.350843+00:00 | Not calibrated | STRONG 84/100 | HIGH 55/100 | Watch | WATCH |
| 9 | ETH/USD | 1742.58 | 76.965 | 77.627 | +3.25% | +0.44% | 0.71x | 0.3 | 2026-11-27T05:21:17.350843+00:00 | Not calibrated | MODERATE 68/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 10 | XBT/USD | 61635.7 | 75.737 | 68.156 | +1.88% | +0.27% | 1.63x | 0.0 | 2026-11-27T05:21:17.350843+00:00 | Not calibrated | STRONG 83/100 | HIGH 55/100 | Consider small entry | WATCH |
| 11 | ADA/USD | 0.152066 | 72.368 | 68.662 | +2.43% | +0.23% | 1.25x | 3.7 | 2026-11-27T05:21:17.350843+00:00 | Not calibrated | STRONG 71/100 | HIGH 55/100 | Watch | WATCH |
| 12 | XRP/USD | 0.96382 | 66.900 | 70.281 | +2.23% | +0.33% | 0.50x | 0.7 | 2026-11-27T05:21:17.350843+00:00 | Not calibrated | MODERATE 63/100 | VERY_HIGH 70/100 | Watch | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | ZEC/USD | 97.371 | 760.77 | -0.00% | 0.91x |
| 2 | HYPE/USD | 96.543 | 65.98 | +0.00% | 0.14x |
| 3 | LINK/USD | 86.125 | 9.68061 | +0.33% | 0.12x |
| 4 | VVV/USD | 77.650 | 27.168 | +0.59% | 3.41x |
| 5 | ETH/USD | 77.627 | 1742.58 | +0.44% | 0.71x |
| 6 | SOL/USD | 76.025 | 73.14 | +0.40% | 3.18x |
| 7 | SUI/USD | 71.161 | 0.6849 | +0.15% | 3.29x |
| 8 | XRP/USD | 70.281 | 0.96382 | +0.33% | 0.50x |
| 9 | LTC/USD | 69.726 | 44.73 | +0.27% | 2.01x |
| 10 | ADA/USD | 68.662 | 0.152066 | +0.23% | 1.25x |
| 11 | XBT/USD | 68.156 | 61635.7 | +0.27% | 1.63x |
| 12 | XDG/USD | 62.095 | 0.0578696 | +0.20% | 15.56x |

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

- Persisted scans: 1964; predictions: 17270; observations: 1189450.
- Matured sampled outcomes across 1/6/24/48h: 38066; gap abstentions: 25540. Per-horizon counts require independent audit; do not infer held-out lift.
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

**Writer:** 45945123479 · **Generation:** 1964 · **Legacy run:** 45945123479
**Main quote time:** 2026-11-27T05:21:24.945866+00:00 · **Legacy report time:** 2026-11-27T05:22:07.978132+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | ZEC/USD | 760.77 | 96.46 | -0.00% | 0.91x | MODERATE 53/100 | HIGH 68/100 | Watch |
| 2 | VVV/USD ⭐ | 27.168 | 95.58 | +0.59% | 3.41x | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 3 | SOL/USD ⭐ | 73.14 | 93.02 | +0.40% | 3.18x | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 4 | HYPE/USD | 65.98 | 87.91 | +0.00% | 0.14x | MODERATE 64/100 | VERY_HIGH 70/100 | Watch |
| 5 | SUI/USD ⭐ | 0.6849 | 86.89 | +0.15% | 3.29x | STRONG 98/100 | HIGH 55/100 | Watch |
| 6 | LTC/USD ⭐ | 44.73 | 81.18 | +0.27% | 2.01x | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 7 | LINK/USD | 9.68061 | 79.04 | +0.33% | 0.12x | STRONG 70/100 | VERY_HIGH 70/100 | Watch |
| 8 | XDG/USD ⭐ | 0.0578696 | 78.09 | +0.20% | 15.56x | STRONG 94/100 | HIGH 55/100 | Watch |
| 9 | ETH/USD | 1742.58 | 76.96 | +0.44% | 0.71x | MODERATE 68/100 | VERY_HIGH 70/100 | Watch |
| 10 | XBT/USD ⭐ | 61635.7 | 75.74 | +0.27% | 1.63x | STRONG 93/100 | HIGH 55/100 | Consider small entry |
| 11 | ADA/USD ⭐ | 0.152066 | 72.37 | +0.23% | 1.25x | STRONG 81/100 | HIGH 55/100 | Watch |
| 12 | XRP/USD | 0.96382 | 66.90 | +0.33% | 0.50x | MODERATE 63/100 | VERY_HIGH 70/100 | Watch |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | SOL/USD ⭐ | 73.09 | 94.83 | +0.40% | 3.18x | 34212 | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 2 | VVV/USD ⭐ | 27.117 | 94.23 | +0.59% | 3.41x | 12499 | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 3 | SUI/USD ⭐ | 0.6849 | 84.82 | +0.15% | 3.29x | 5088 | STRONG 97/100 | HIGH 55/100 | Watch |
| 4 | XDG/USD ⭐ | 0.0578564 | 84.26 | +0.20% | 15.56x | 5560 | STRONG 97/100 | HIGH 55/100 | Watch |
| 5 | LTC/USD ⭐ | 44.73 | 79.54 | +0.27% | 2.01x | 14474 | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 6 | XBT/USD ⭐ | 61628.1 | 77.68 | +0.27% | 1.63x | 135663 | STRONG 94/100 | HIGH 55/100 | Consider small entry |
| 7 | ADA/USD ⭐ | 0.151976 | 76.49 | +0.23% | 1.25x | 10150 | STRONG 83/100 | HIGH 55/100 | Watch |

**Same-run overlap:** VVV/USD, SOL/USD, SUI/USD, LTC/USD, XDG/USD, XBT/USD, ADA/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
