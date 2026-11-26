# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-26T05:26:18.776309+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/45761396771
**Source SHA:** 858c8bc8ec5d7641ddb39cacd8aca91719f855b1
**Previous ledger commit:** 94df65b4b22b148f8785c722fb2337e492f5f2e5 (atomic ledger/results publication)
**Ledger generation:** 1818 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 6s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 628; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 610; valid market observations: 609; OHLC screened: 24.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | XRP/USD | 0.9613 | 89.741 | 72.919 | +2.64% | +0.36% | 4.27x | 1.1 | 2026-11-26T05:26:12.932964+00:00 | Not calibrated | STRONG 100/100 | HIGH 55/100 | Consider small entry | WATCH |
| 2 | LTC/USD | 43.71 | 76.619 | 70.246 | +2.34% | -0.25% | 1.76x | 2.3 | 2026-11-26T05:26:12.932964+00:00 | Not calibrated | MODERATE 58/100 | HIGH 61/100 | Watch | WATCH |
| 3 | SUI/USD | 0.6719 | 76.557 | 60.139 | +0.84% | +0.28% | 15.19x | 1.5 | 2026-11-26T05:26:12.932964+00:00 | Not calibrated | STRONG 93/100 | HIGH 55/100 | Consider small entry | WATCH |
| 4 | HBAR/USD | 0.05376 | 75.543 | 58.299 | +3.19% | +0.45% | 2.51x | 1.9 | 2026-11-26T05:26:12.932964+00:00 | Not calibrated | STRONG 93/100 | HIGH 55/100 | Consider small entry | WATCH |
| 5 | PIEVERSE/USD | 3.8093 | 75.539 | 64.715 | +7.58% | -0.84% | 9.20x | 33.9 | 2026-11-26T05:26:12.932964+00:00 | Not calibrated | MODERATE 58/100 | VERY_HIGH 73/100 | Watch | WATCH |
| 6 | SOL/USD | 71.26 | 70.275 | 62.950 | +1.24% | +0.24% | 1.61x | 1.4 | 2026-11-26T05:26:12.932964+00:00 | Not calibrated | STRONG 80/100 | HIGH 55/100 | Consider small entry | WATCH |
| 7 | ADA/USD | 0.149493 | 68.307 | 70.837 | +2.55% | +0.47% | 0.51x | 4.1 | 2026-11-26T05:26:12.932964+00:00 | Not calibrated | MODERATE 64/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 8 | ETH/USD | 1699.76 | 66.725 | 58.842 | +0.55% | +0.02% | 1.78x | 0.1 | 2026-11-26T05:26:12.932964+00:00 | Not calibrated | MODERATE 68/100 | HIGH 55/100 | Watch | WATCH |
| 9 | XMR/USD | 518.27 | 63.766 | 56.691 | +0.26% | -0.07% | 1.74x | 0.2 | 2026-11-26T05:26:12.932964+00:00 | Not calibrated | MODERATE 52/100 | HIGH 61/100 | Watch | WATCH |
| 10 | LINK/USD | 9.25243 | 62.402 | 66.433 | +2.30% | +0.21% | 0.49x | 4.9 | 2026-11-26T05:26:12.932964+00:00 | Not calibrated | MODERATE 61/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 11 | XBT/USD | 60930.1 | 60.999 | 61.503 | +0.93% | +0.08% | 0.91x | 0.0 | 2026-11-26T05:26:12.932964+00:00 | Not calibrated | MODERATE 50/100 | HIGH 62/100 | Watch | WATCH |
| 12 | TAO/USD | 184 | 60.639 | 63.111 | +1.33% | +0.06% | 0.72x | 2.3 | 2026-11-26T05:26:12.932964+00:00 | Not calibrated | MODERATE 50/100 | VERY_HIGH 70/100 | Watch | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | XRP/USD | 72.919 | 0.9613 | +0.36% | 4.27x |
| 2 | ADA/USD | 70.837 | 0.149493 | +0.47% | 0.51x |
| 3 | LTC/USD | 70.246 | 43.71 | -0.25% | 1.76x |
| 4 | LINK/USD | 66.433 | 9.25243 | +0.21% | 0.49x |
| 5 | PIEVERSE/USD | 64.715 | 3.8093 | -0.84% | 9.20x |
| 6 | TAO/USD | 63.111 | 184 | +0.06% | 0.72x |
| 7 | SOL/USD | 62.950 | 71.26 | +0.24% | 1.61x |
| 8 | XBT/USD | 61.503 | 60930.1 | +0.08% | 0.91x |
| 9 | SUI/USD | 60.139 | 0.6719 | +0.28% | 15.19x |
| 10 | ETH/USD | 58.842 | 1699.76 | +0.02% | 1.78x |
| 11 | HBAR/USD | 58.299 | 0.05376 | +0.45% | 2.51x |
| 12 | XMR/USD | 56.691 | 518.27 | -0.07% | 1.74x |

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

- Persisted scans: 1818; predictions: 15551; observations: 1102206.
- Matured sampled outcomes across 1/6/24/48h: 33743; gap abstentions: 23960. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 146 (sampled only; not a success-rate estimate).
- False positives / missed movers: NOT VERIFIED without eligible continuous outcome coverage.
- Baseline vs challenger: recorded as-of; unbiased held-out lift NOT MEASURED.
- Online Kraken /USD stablecoin-base pairs excluded: 18 (counted from this scan's online AssetPairs metadata, not inferred from price).
- Stablecoin base exclusions: BRL1, BUSD, DAI, EUR, EURC, EUROP, EURQ, EURR, EURT, FDUSD, FRAX, GUSD, PYUSD, QCAD, RLUSD, TGBP, TUSD, USD, USD1, USDC, USDD, USDE, USDG, USDQ, USDR, USDS, USDT, ZUSD.
- DEX: NOT USED; no DEX freshness gate.
- OHLC screening abstentions: 4; details in immutable scan JSON artifact.
- Storage: ledger and results published in one non-force Git commit and read back. Independent artifact recovery is NOT VERIFIED by this scan alone.
- Errors: none in successful committed scan; a failed workflow must not publish a SUCCESS report.

# Cryptoscanner — challenger and independent legacy-inspired WATCH

Paper only · risk is high or higher · 30%+ in 48h probability NOT CALIBRATED
Signal confidence 0–100 means setup strength only, NOT a win probability. Actions are research guidance; no trade authorization.

**Writer:** 45761396771 · **Generation:** 1818 · **Legacy run:** 45761396771
**Main quote time:** 2026-11-26T05:26:18.776309+00:00 · **Legacy report time:** 2026-11-26T05:27:37.076093+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | XRP/USD ⭐ | 0.9613 | 89.74 | +0.36% | 4.27x | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 2 | LTC/USD | 43.71 | 76.62 | -0.25% | 1.76x | MODERATE 58/100 | HIGH 61/100 | Watch |
| 3 | SUI/USD | 0.6719 | 76.56 | +0.28% | 15.19x | STRONG 93/100 | HIGH 55/100 | Consider small entry |
| 4 | HBAR/USD ⭐ | 0.05376 | 75.54 | +0.45% | 2.51x | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 5 | PIEVERSE/USD | 3.8093 | 75.54 | -0.84% | 9.20x | MODERATE 58/100 | VERY_HIGH 73/100 | Watch |
| 6 | SOL/USD | 71.26 | 70.28 | +0.24% | 1.61x | STRONG 80/100 | HIGH 55/100 | Consider small entry |
| 7 | ADA/USD | 0.149493 | 68.31 | +0.47% | 0.51x | MODERATE 64/100 | VERY_HIGH 70/100 | Watch |
| 8 | ETH/USD | 1699.76 | 66.72 | +0.02% | 1.78x | MODERATE 68/100 | HIGH 55/100 | Watch |
| 9 | XMR/USD | 518.27 | 63.77 | -0.07% | 1.74x | MODERATE 52/100 | HIGH 61/100 | Watch |
| 10 | LINK/USD | 9.25243 | 62.40 | +0.21% | 0.49x | MODERATE 61/100 | VERY_HIGH 70/100 | Watch |
| 11 | XBT/USD | 60930.1 | 61.00 | +0.08% | 0.91x | MODERATE 50/100 | HIGH 62/100 | Watch |
| 12 | TAO/USD | 184 | 60.64 | +0.06% | 0.72x | MODERATE 50/100 | VERY_HIGH 70/100 | Watch |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | XRP/USD ⭐ | 0.96126 | 91.91 | +0.36% | 4.27x | 42228 | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 2 | HBAR/USD ⭐ | 0.05378 | 79.81 | +0.45% | 2.51x | 6196 | STRONG 100/100 | HIGH 55/100 | Consider small entry |

**Same-run overlap:** XRP/USD, HBAR/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
