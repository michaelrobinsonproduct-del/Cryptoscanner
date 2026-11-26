# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-26T18:31:22.175871+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/45876342662
**Source SHA:** 858c8bc8ec5d7641ddb39cacd8aca91719f855b1
**Previous ledger commit:** 8e28706bc817596e96cd67d95ee09bf81744d281 (atomic ledger/results publication)
**Ledger generation:** 1897 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 7s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 628; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 610; valid market observations: 596; OHLC screened: 24.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | XRP/USD | 0.95497 | 85.174 | 68.393 | +1.97% | +0.36% | 3.76x | 0.7 | 2026-11-26T18:31:15.142517+00:00 | Not calibrated | STRONG 98/100 | HIGH 55/100 | Consider small entry | WATCH |
| 2 | FET/USD | 0.1186 | 84.852 | 70.000 | +9.31% | +0.76% | 2.10x | 16.9 | 2026-11-26T18:31:15.142517+00:00 | Not calibrated | STRONG 92/100 | HIGH 66/100 | Consider small entry | WATCH |
| 3 | LINK/USD | 9.25921 | 83.758 | 69.794 | +2.37% | +0.36% | 2.22x | 3.6 | 2026-11-26T18:31:15.142517+00:00 | Not calibrated | STRONG 97/100 | HIGH 55/100 | Consider small entry | WATCH |
| 4 | WIF/USD | 0.1402 | 83.085 | 69.468 | +10.13% | +1.30% | 1.71x | 14.3 | 2026-11-26T18:31:15.142517+00:00 | Not calibrated | STRONG 82/100 | VERY_HIGH 73/100 | Watch | WATCH |
| 5 | AKT/USD | 0.5047 | 75.722 | 69.986 | +6.68% | +0.64% | 1.25x | 15.9 | 2026-11-26T18:31:15.142517+00:00 | Not calibrated | MODERATE 68/100 | HIGH 66/100 | Watch | WATCH |
| 6 | XDG/USD | 0.0569517 | 75.281 | 58.623 | +1.77% | +0.33% | 7.69x | 0.0 | 2026-11-26T18:31:15.142517+00:00 | Not calibrated | STRONG 93/100 | HIGH 55/100 | Consider small entry | WATCH |
| 7 | ADA/USD | 0.149865 | 74.472 | 73.264 | +2.81% | +0.34% | 0.95x | 2.8 | 2026-11-26T18:31:15.142517+00:00 | Not calibrated | MODERATE 67/100 | HIGH 62/100 | Watch | WATCH |
| 8 | XBT/USD | 60579.7 | 71.918 | 57.440 | +0.35% | +0.34% | 2.28x | 0.0 | 2026-11-26T18:31:15.142517+00:00 | Not calibrated | STRONG 91/100 | HIGH 55/100 | Consider small entry | WATCH |
| 9 | SKY/USD | 0.04572 | 70.830 | 76.552 | +9.17% | +0.51% | 0.18x | 6.6 | 2026-11-26T18:31:15.142517+00:00 | Not calibrated | MODERATE 65/100 | VERY_HIGH 75/100 | Watch | WATCH |
| 10 | ETH/USD | 1697.62 | 68.206 | 57.632 | +0.43% | +0.51% | 1.80x | 0.7 | 2026-11-26T18:31:15.142517+00:00 | Not calibrated | STRONG 79/100 | HIGH 55/100 | Watch | WATCH |
| 11 | HBAR/USD | 0.05458 | 68.172 | 67.759 | +4.76% | +0.57% | 0.76x | 1.8 | 2026-11-26T18:31:15.142517+00:00 | Not calibrated | MODERATE 64/100 | HIGH 67/100 | Watch | WATCH |
| 12 | ZRO/USD | 1.086 | 66.801 | 69.738 | +6.05% | +0.93% | 0.24x | 18.4 | 2026-11-26T18:31:15.142517+00:00 | Not calibrated | MODERATE 58/100 | VERY_HIGH 81/100 | Watch | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | SKY/USD | 76.552 | 0.04572 | +0.51% | 0.18x |
| 2 | ADA/USD | 73.264 | 0.149865 | +0.34% | 0.95x |
| 3 | FET/USD | 70.000 | 0.1186 | +0.76% | 2.10x |
| 4 | AKT/USD | 69.986 | 0.5047 | +0.64% | 1.25x |
| 5 | LINK/USD | 69.794 | 9.25921 | +0.36% | 2.22x |
| 6 | ZRO/USD | 69.738 | 1.086 | +0.93% | 0.24x |
| 7 | WIF/USD | 69.468 | 0.1402 | +1.30% | 1.71x |
| 8 | XRP/USD | 68.393 | 0.95497 | +0.36% | 3.76x |
| 9 | HBAR/USD | 67.759 | 0.05458 | +0.57% | 0.76x |
| 10 | XDG/USD | 58.623 | 0.0569517 | +0.33% | 7.69x |
| 11 | ETH/USD | 57.632 | 1697.62 | +0.51% | 1.80x |
| 12 | XBT/USD | 57.440 | 60579.7 | +0.34% | 2.28x |

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

- Persisted scans: 1897; predictions: 16499; observations: 1149253.
- Matured sampled outcomes across 1/6/24/48h: 35708; gap abstentions: 25139. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 146 (sampled only; not a success-rate estimate).
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

**Writer:** 45876342662 · **Generation:** 1897 · **Legacy run:** 45876342662
**Main quote time:** 2026-11-26T18:31:22.175871+00:00 · **Legacy report time:** 2026-11-26T18:32:13.015742+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | XRP/USD ⭐ | 0.95497 | 85.17 | +0.36% | 3.76x | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 2 | FET/USD | 0.1186 | 84.85 | +0.76% | 2.10x | STRONG 92/100 | HIGH 66/100 | Consider small entry |
| 3 | LINK/USD ⭐ | 9.25921 | 83.76 | +0.36% | 2.22x | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 4 | WIF/USD | 0.1402 | 83.08 | +1.30% | 1.71x | STRONG 82/100 | VERY_HIGH 73/100 | Watch |
| 5 | AKT/USD ⭐ | 0.5047 | 75.72 | +0.64% | 1.25x | STRONG 78/100 | HIGH 66/100 | Watch |
| 6 | XDG/USD | 0.0569517 | 75.28 | +0.33% | 7.69x | STRONG 93/100 | HIGH 55/100 | Consider small entry |
| 7 | ADA/USD | 0.149865 | 74.47 | +0.34% | 0.95x | MODERATE 67/100 | HIGH 62/100 | Watch |
| 8 | XBT/USD | 60579.7 | 71.92 | +0.34% | 2.28x | STRONG 91/100 | HIGH 55/100 | Consider small entry |
| 9 | SKY/USD | 0.04572 | 70.83 | +0.51% | 0.18x | MODERATE 65/100 | VERY_HIGH 75/100 | Watch |
| 10 | ETH/USD | 1697.62 | 68.21 | +0.51% | 1.80x | STRONG 79/100 | HIGH 55/100 | Watch |
| 11 | HBAR/USD | 0.05458 | 68.17 | +0.57% | 0.76x | MODERATE 64/100 | HIGH 67/100 | Watch |
| 12 | ZRO/USD | 1.086 | 66.80 | +0.93% | 0.24x | MODERATE 58/100 | VERY_HIGH 81/100 | Watch |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | DRV/USD | 0.3913 | 89.33 | +2.52% | 5.91x | 7665 | STRONG 95/100 | HIGH 66/100 | Consider small entry |
| 2 | XRP/USD ⭐ | 0.95506 | 83.10 | +0.36% | 3.76x | 29992 | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 3 | LINK/USD ⭐ | 9.25921 | 81.15 | +0.36% | 2.22x | 7607 | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 4 | QNT/USD | 149.5 | 78.62 | +0.47% | 1.63x | 6543 | STRONG 84/100 | HIGH 55/100 | Consider small entry |
| 5 | AKT/USD ⭐ | 0.5061 | 74.69 | +0.64% | 1.25x | 2699 | STRONG 77/100 | HIGH 66/100 | Watch |

**Same-run overlap:** XRP/USD, LINK/USD, AKT/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
