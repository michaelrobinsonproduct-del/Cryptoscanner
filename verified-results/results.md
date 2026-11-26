# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-26T05:36:17.335020+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/45762496216
**Source SHA:** 858c8bc8ec5d7641ddb39cacd8aca91719f855b1
**Previous ledger commit:** 0ed621df9be9f18dec09c4e84a4f4c66d6246890 (atomic ledger/results publication)
**Ledger generation:** 1819 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 9s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 628; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 610; valid market observations: 609; OHLC screened: 24.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | XRP/USD | 0.96244 | 89.964 | 73.927 | +2.76% | +0.21% | 5.41x | 0.8 | 2026-11-26T05:36:08.818511+00:00 | Not calibrated | STRONG 100/100 | HIGH 55/100 | Consider small entry | WATCH |
| 2 | PIEVERSE/USD | 3.7822 | 80.673 | 68.026 | +6.81% | -0.47% | 5.10x | 27.2 | 2026-11-26T05:36:08.818511+00:00 | Not calibrated | MODERATE 60/100 | VERY_HIGH 78/100 | Watch | WATCH |
| 3 | SUI/USD | 0.6731 | 77.741 | 61.401 | +1.02% | +0.27% | 12.53x | 1.5 | 2026-11-26T05:36:08.818511+00:00 | Not calibrated | STRONG 94/100 | HIGH 55/100 | Consider small entry | WATCH |
| 4 | TAO/USD | 184.0978 | 77.654 | 62.140 | +1.38% | +0.10% | 4.38x | 5.0 | 2026-11-26T05:36:08.818511+00:00 | Not calibrated | STRONG 84/100 | HIGH 55/100 | Watch | WATCH |
| 5 | SOL/USD | 71.24 | 76.048 | 62.751 | +1.21% | +0.11% | 2.27x | 1.4 | 2026-11-26T05:36:08.818511+00:00 | Not calibrated | STRONG 83/100 | HIGH 55/100 | Watch | WATCH |
| 6 | HBAR/USD | 0.05383 | 75.845 | 59.261 | +3.32% | +0.32% | 3.48x | 1.9 | 2026-11-26T05:36:08.818511+00:00 | Not calibrated | STRONG 93/100 | HIGH 55/100 | Consider small entry | WATCH |
| 7 | SYRUP/USD | 0.07066 | 74.674 | 67.213 | +6.62% | -1.26% | 2.38x | 19.9 | 2026-11-26T05:36:08.818511+00:00 | Not calibrated | MODERATE 62/100 | VERY_HIGH 76/100 | Do nothing | WATCH |
| 8 | ADA/USD | 0.149639 | 70.089 | 72.911 | +2.65% | +0.29% | 0.57x | 1.3 | 2026-11-26T05:36:08.818511+00:00 | Not calibrated | MODERATE 65/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 9 | LTC/USD | 43.57 | 66.173 | 67.948 | +2.01% | -0.43% | 1.04x | 2.3 | 2026-11-26T05:36:08.818511+00:00 | Not calibrated | WEAK 43/100 | HIGH 68/100 | Watch | WATCH |
| 10 | INJ/USD | 6.177 | 65.367 | 64.485 | +3.75% | -0.21% | 1.19x | 8.1 | 2026-11-26T05:36:08.818511+00:00 | Not calibrated | WEAK 43/100 | HIGH 68/100 | Watch | WATCH |
| 11 | XDG/USD | 0.0568393 | 64.755 | 61.362 | +1.57% | +0.19% | 1.24x | 0.0 | 2026-11-26T05:36:08.818511+00:00 | Not calibrated | MODERATE 57/100 | HIGH 62/100 | Watch | WATCH |
| 12 | ETH/USD | 1700.17 | 64.638 | 59.012 | +0.58% | +0.10% | 1.51x | 0.1 | 2026-11-26T05:36:08.818511+00:00 | Not calibrated | MODERATE 67/100 | HIGH 55/100 | Watch | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | XRP/USD | 73.927 | 0.96244 | +0.21% | 5.41x |
| 2 | ADA/USD | 72.911 | 0.149639 | +0.29% | 0.57x |
| 3 | PIEVERSE/USD | 68.026 | 3.7822 | -0.47% | 5.10x |
| 4 | LTC/USD | 67.948 | 43.57 | -0.43% | 1.04x |
| 5 | SYRUP/USD | 67.213 | 0.07066 | -1.26% | 2.38x |
| 6 | INJ/USD | 64.485 | 6.177 | -0.21% | 1.19x |
| 7 | SOL/USD | 62.751 | 71.24 | +0.11% | 2.27x |
| 8 | TAO/USD | 62.140 | 184.0978 | +0.10% | 4.38x |
| 9 | SUI/USD | 61.401 | 0.6731 | +0.27% | 12.53x |
| 10 | XDG/USD | 61.362 | 0.0568393 | +0.19% | 1.24x |
| 11 | HBAR/USD | 59.261 | 0.05383 | +0.32% | 3.48x |
| 12 | ETH/USD | 59.012 | 1700.17 | +0.10% | 1.51x |

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

- Persisted scans: 1819; predictions: 15563; observations: 1102815.
- Matured sampled outcomes across 1/6/24/48h: 33767; gap abstentions: 23976. Per-horizon counts require independent audit; do not infer held-out lift.
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

**Writer:** 45762496216 · **Generation:** 1819 · **Legacy run:** 45762496216
**Main quote time:** 2026-11-26T05:36:17.335020+00:00 · **Legacy report time:** 2026-11-26T05:37:36.756558+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | XRP/USD ⭐ | 0.96244 | 89.96 | +0.21% | 5.41x | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 2 | PIEVERSE/USD | 3.7822 | 80.67 | -0.47% | 5.10x | MODERATE 60/100 | VERY_HIGH 78/100 | Watch |
| 3 | SUI/USD | 0.6731 | 77.74 | +0.27% | 12.53x | STRONG 94/100 | HIGH 55/100 | Consider small entry |
| 4 | TAO/USD | 184.0978 | 77.65 | +0.10% | 4.38x | STRONG 84/100 | HIGH 55/100 | Watch |
| 5 | SOL/USD | 71.24 | 76.05 | +0.11% | 2.27x | STRONG 83/100 | HIGH 55/100 | Watch |
| 6 | HBAR/USD ⭐ | 0.05383 | 75.84 | +0.32% | 3.48x | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 7 | SYRUP/USD | 0.07066 | 74.67 | -1.26% | 2.38x | MODERATE 62/100 | VERY_HIGH 76/100 | Do nothing |
| 8 | ADA/USD | 0.149639 | 70.09 | +0.29% | 0.57x | MODERATE 65/100 | VERY_HIGH 70/100 | Watch |
| 9 | LTC/USD | 43.57 | 66.17 | -0.43% | 1.04x | WEAK 43/100 | HIGH 68/100 | Watch |
| 10 | INJ/USD | 6.177 | 65.37 | -0.21% | 1.19x | WEAK 43/100 | HIGH 68/100 | Watch |
| 11 | XDG/USD ⭐ | 0.0568393 | 64.75 | +0.19% | 1.24x | MODERATE 67/100 | HIGH 62/100 | Watch |
| 12 | ETH/USD | 1700.17 | 64.64 | +0.10% | 1.51x | MODERATE 67/100 | HIGH 55/100 | Watch |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | XRP/USD ⭐ | 0.96174 | 92.68 | +0.21% | 5.41x | 42261 | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 2 | HBAR/USD ⭐ | 0.05377 | 81.14 | +0.32% | 3.48x | 6214 | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 3 | XDG/USD ⭐ | 0.0567863 | 67.09 | +0.19% | 1.24x | 7782 | MODERATE 69/100 | HIGH 62/100 | Watch |

**Same-run overlap:** XRP/USD, HBAR/USD, XDG/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
