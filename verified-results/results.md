# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-21T18:50:57.535979+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/44937618227
**Source SHA:** 4066e028afbd46ef7ad268722dcaaaa2ca6a4e7e
**Previous ledger commit:** 01fb353d4162fc6d8f51daa77c5bd04c1a5a0121 (atomic ledger/results publication)
**Ledger generation:** 1172 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 6s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 628; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 610; valid market observations: 608; OHLC screened: 24.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | NIGHT/USD | 0.04536 | 98.840 | 88.872 | +7.44% | +0.38% | 1.81x | 8.8 | 2026-11-21T18:50:51.476207+00:00 | Not calibrated | STRONG 94/100 | HIGH 55/100 | Consider small entry | WATCH |
| 2 | ETH/USD | 1680 | 95.580 | 81.201 | +3.75% | -0.12% | 3.02x | 0.1 | 2026-11-21T18:50:51.476207+00:00 | Not calibrated | STRONG 78/100 | HIGH 61/100 | Watch | WATCH |
| 3 | XMR/USD | 483.49 | 95.302 | 94.866 | +5.96% | +0.07% | 1.01x | 3.7 | 2026-11-21T18:50:51.476207+00:00 | Not calibrated | STRONG 73/100 | HIGH 62/100 | Watch | WATCH |
| 4 | UNI/USD | 4.6855 | 94.757 | 85.364 | +4.89% | -1.12% | 4.85x | 7.7 | 2026-11-21T18:50:51.476207+00:00 | Not calibrated | STRONG 77/100 | HIGH 65/100 | Watch | WATCH |
| 5 | XRP/USD | 0.93345 | 88.275 | 73.683 | +2.72% | +0.08% | 2.42x | 0.7 | 2026-11-21T18:50:51.476207+00:00 | Not calibrated | STRONG 89/100 | HIGH 55/100 | Watch | WATCH |
| 6 | ZEC/USD | 789.48 | 86.123 | 84.094 | +4.17% | -0.32% | 1.36x | 0.1 | 2026-11-21T18:50:51.476207+00:00 | Not calibrated | MODERATE 63/100 | HIGH 61/100 | Watch | WATCH |
| 7 | SOL/USD | 70.67 | 81.808 | 74.260 | +2.85% | -0.06% | 1.78x | 1.4 | 2026-11-21T18:50:51.476207+00:00 | Not calibrated | MODERATE 61/100 | HIGH 61/100 | Watch | WATCH |
| 8 | XDG/USD | 0.0552119 | 81.363 | 66.866 | +1.73% | -0.10% | 4.35x | 0.4 | 2026-11-21T18:50:51.476207+00:00 | Not calibrated | STRONG 71/100 | HIGH 61/100 | Watch | WATCH |
| 9 | QNT/USD | 141.88 | 78.345 | 68.625 | +2.25% | -0.53% | 2.24x | 4.2 | 2026-11-21T18:50:51.476207+00:00 | Not calibrated | MODERATE 69/100 | HIGH 61/100 | Watch | WATCH |
| 10 | TAO/USD | 186.0482 | 75.372 | 74.567 | +3.07% | -0.37% | 1.26x | 3.8 | 2026-11-21T18:50:51.476207+00:00 | Not calibrated | MODERATE 48/100 | HIGH 61/100 | Watch | WATCH |
| 11 | XLM/USD | 0.12903 | 68.118 | 65.026 | +1.44% | +0.02% | 1.30x | 0.1 | 2026-11-21T18:50:51.476207+00:00 | Not calibrated | MODERATE 69/100 | HIGH 55/100 | Watch | WATCH |
| 12 | XBT/USD | 60026.5 | 65.319 | 69.515 | +2.07% | -0.08% | 0.62x | 0.0 | 2026-11-21T18:50:51.476207+00:00 | Not calibrated | WEAK 38/100 | VERY_HIGH 76/100 | Watch | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | XMR/USD | 94.866 | 483.49 | +0.07% | 1.01x |
| 2 | NIGHT/USD | 88.872 | 0.04536 | +0.38% | 1.81x |
| 3 | UNI/USD | 85.364 | 4.6855 | -1.12% | 4.85x |
| 4 | ZEC/USD | 84.094 | 789.48 | -0.32% | 1.36x |
| 5 | ETH/USD | 81.201 | 1680 | -0.12% | 3.02x |
| 6 | TAO/USD | 74.567 | 186.0482 | -0.37% | 1.26x |
| 7 | SOL/USD | 74.260 | 70.67 | -0.06% | 1.78x |
| 8 | XRP/USD | 73.683 | 0.93345 | +0.08% | 2.42x |
| 9 | XBT/USD | 69.515 | 60026.5 | -0.08% | 0.62x |
| 10 | QNT/USD | 68.625 | 141.88 | -0.53% | 2.24x |
| 11 | XDG/USD | 66.866 | 0.0552119 | -0.10% | 4.35x |
| 12 | XLM/USD | 65.026 | 0.12903 | +0.02% | 1.30x |

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

- Persisted scans: 1172; predictions: 9373; observations: 708935.
- Matured sampled outcomes across 1/6/24/48h: 12391; gap abstentions: 21134. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 16 (sampled only; not a success-rate estimate).
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

**Writer:** 44937618227 · **Generation:** 1172 · **Legacy run:** 44937618227
**Main quote time:** 2026-11-21T18:50:57.535979+00:00 · **Legacy report time:** 2026-11-21T18:51:43.794153+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | NIGHT/USD ⭐ | 0.04536 | 98.84 | +0.38% | 1.81x | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 2 | ETH/USD | 1680 | 95.58 | -0.12% | 3.02x | STRONG 78/100 | HIGH 61/100 | Watch |
| 3 | XMR/USD ⭐ | 483.49 | 95.30 | +0.07% | 1.01x | STRONG 83/100 | HIGH 62/100 | Watch |
| 4 | UNI/USD | 4.6855 | 94.76 | -1.12% | 4.85x | STRONG 77/100 | HIGH 65/100 | Watch |
| 5 | XRP/USD ⭐ | 0.93345 | 88.28 | +0.08% | 2.42x | STRONG 99/100 | HIGH 55/100 | Watch |
| 6 | ZEC/USD | 789.48 | 86.12 | -0.32% | 1.36x | MODERATE 63/100 | HIGH 61/100 | Watch |
| 7 | SOL/USD | 70.67 | 81.81 | -0.06% | 1.78x | MODERATE 61/100 | HIGH 61/100 | Watch |
| 8 | XDG/USD | 0.0552119 | 81.36 | -0.10% | 4.35x | STRONG 71/100 | HIGH 61/100 | Watch |
| 9 | QNT/USD | 141.88 | 78.35 | -0.53% | 2.24x | MODERATE 69/100 | HIGH 61/100 | Watch |
| 10 | TAO/USD | 186.0482 | 75.37 | -0.37% | 1.26x | MODERATE 48/100 | HIGH 61/100 | Watch |
| 11 | XLM/USD | 0.12903 | 68.12 | +0.02% | 1.30x | MODERATE 69/100 | HIGH 55/100 | Watch |
| 12 | XBT/USD | 60026.5 | 65.32 | -0.08% | 0.62x | WEAK 38/100 | VERY_HIGH 76/100 | Watch |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | NIGHT/USD ⭐ | 0.04535 | 91.51 | +0.38% | 1.81x | 11551 | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 2 | XRP/USD ⭐ | 0.93369 | 90.26 | +0.08% | 2.42x | 58772 | STRONG 100/100 | HIGH 55/100 | Watch |
| 3 | XMR/USD ⭐ | 483.37 | 85.24 | +0.07% | 1.01x | 12751 | STRONG 78/100 | HIGH 62/100 | Watch |

**Same-run overlap:** NIGHT/USD, XMR/USD, XRP/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
