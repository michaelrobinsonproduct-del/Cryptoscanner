# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-17T22:45:03.215170+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/44192983318
**Source SHA:** e9b1b6ee47d56a43a454042547735fcd1cdc45a9
**Previous ledger commit:** f039a4323ffb270c14e4137477d4f11be9323602 (atomic ledger/results publication)
**Ledger generation:** 462 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 8s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 627; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 609; valid market observations: 609; OHLC screened: 24.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | NEAR/USD | 3.3229 | 108.171 | 91.448 | +5.23% | +0.34% | 5.92x | 0.3 | 2026-11-17T22:44:55.477966+00:00 | Not calibrated | STRONG 100/100 | HIGH 55/100 | Consider small entry | WATCH |
| 2 | INJ/USD | 7.243 | 105.753 | 87.142 | +4.99% | +0.72% | 9.06x | 5.5 | 2026-11-17T22:44:55.477966+00:00 | Not calibrated | STRONG 100/100 | HIGH 55/100 | Consider small entry | WATCH |
| 3 | ZEC/USD | 948.46 | 103.960 | 88.474 | +4.94% | +0.88% | 2.11x | 2.2 | 2026-11-17T22:44:55.477966+00:00 | Not calibrated | STRONG 100/100 | HIGH 55/100 | Consider small entry | WATCH |
| 4 | AKT/USD | 0.5033 | 82.448 | 67.491 | +5.20% | +0.60% | 2.20x | 2.0 | 2026-11-17T22:44:55.477966+00:00 | Not calibrated | STRONG 96/100 | HIGH 60/100 | Consider small entry | WATCH |
| 5 | LUNA/USD | 4.115e-05 | 74.765 | 64.519 | +10.32% | +0.02% | 2.01x | 26.8 | 2026-11-17T22:44:55.477966+00:00 | Not calibrated | STRONG 72/100 | VERY_HIGH 72/100 | Watch | WATCH |
| 6 | SOL/USD | 73.94 | 72.004 | 78.009 | +3.38% | +0.19% | 0.30x | 1.4 | 2026-11-17T22:44:55.477966+00:00 | Not calibrated | MODERATE 56/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 7 | TRUST/USD | 0.04729 | 69.679 | 76.896 | +9.95% | +0.19% | 0.18x | 2.1 | 2026-11-17T22:44:55.477966+00:00 | Not calibrated | MODERATE 55/100 | VERY_HIGH 75/100 | Watch | WATCH |
| 8 | VVV/USD | 20.854 | 68.979 | 68.331 | +3.50% | +1.20% | 0.46x | 6.7 | 2026-11-17T22:44:55.477966+00:00 | Not calibrated | MODERATE 64/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 9 | JUP/USD | 0.25801 | 66.552 | 72.516 | +7.25% | +0.32% | 0.24x | 11.2 | 2026-11-17T22:44:55.477966+00:00 | Not calibrated | MODERATE 58/100 | VERY_HIGH 81/100 | Watch | WATCH |
| 10 | XMR/USD | 507.46 | 66.400 | 68.080 | +2.81% | -0.22% | 0.94x | 13.2 | 2026-11-17T22:44:55.477966+00:00 | Not calibrated | WEAK 33/100 | VERY_HIGH 74/100 | Do nothing | WATCH |
| 11 | SUI/USD | 0.732 | 61.071 | 66.577 | +1.75% | +0.27% | 0.31x | 1.4 | 2026-11-17T22:44:55.477966+00:00 | Not calibrated | MODERATE 61/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 12 | XRP/USD | 0.97167 | 61.017 | 67.346 | +1.77% | +0.08% | 0.33x | 0.1 | 2026-11-17T22:44:55.477966+00:00 | Not calibrated | MODERATE 51/100 | VERY_HIGH 70/100 | Watch | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | NEAR/USD | 91.448 | 3.3229 | +0.34% | 5.92x |
| 2 | ZEC/USD | 88.474 | 948.46 | +0.88% | 2.11x |
| 3 | INJ/USD | 87.142 | 7.243 | +0.72% | 9.06x |
| 4 | SOL/USD | 78.009 | 73.94 | +0.19% | 0.30x |
| 5 | TRUST/USD | 76.896 | 0.04729 | +0.19% | 0.18x |
| 6 | JUP/USD | 72.516 | 0.25801 | +0.32% | 0.24x |
| 7 | VVV/USD | 68.331 | 20.854 | +1.20% | 0.46x |
| 8 | XMR/USD | 68.080 | 507.46 | -0.22% | 0.94x |
| 9 | AKT/USD | 67.491 | 0.5033 | +0.60% | 2.20x |
| 10 | XRP/USD | 67.346 | 0.97167 | +0.08% | 0.33x |
| 11 | SUI/USD | 66.577 | 0.732 | +0.27% | 0.31x |
| 12 | LUNA/USD | 64.519 | 4.115e-05 | +0.02% | 2.01x |

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

- Persisted scans: 462; predictions: 4025; observations: 278365.
- Matured sampled outcomes across 1/6/24/48h: 3195; gap abstentions: 12386. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 0 (sampled only; not a success-rate estimate).
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

**Writer:** 44192983318 · **Generation:** 462 · **Legacy run:** 44192983318
**Main quote time:** 2026-11-17T22:45:03.215170+00:00 · **Legacy report time:** 2026-11-17T22:45:11.880880+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | NEAR/USD | 3.3229 | 108.17 | +0.34% | 5.92x | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 2 | INJ/USD ⭐ | 7.243 | 105.75 | +0.72% | 9.06x | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 3 | ZEC/USD ⭐ | 948.46 | 103.96 | +0.88% | 2.11x | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 4 | AKT/USD | 0.5033 | 82.45 | +0.60% | 2.20x | STRONG 96/100 | HIGH 60/100 | Consider small entry |
| 5 | LUNA/USD | 4.115e-05 | 74.77 | +0.02% | 2.01x | STRONG 72/100 | VERY_HIGH 72/100 | Watch |
| 6 | SOL/USD | 73.94 | 72.00 | +0.19% | 0.30x | MODERATE 56/100 | VERY_HIGH 70/100 | Watch |
| 7 | TRUST/USD | 0.04729 | 69.68 | +0.19% | 0.18x | MODERATE 55/100 | VERY_HIGH 75/100 | Watch |
| 8 | VVV/USD ⭐ | 20.854 | 68.98 | +1.20% | 0.46x | STRONG 74/100 | VERY_HIGH 70/100 | Watch |
| 9 | JUP/USD | 0.25801 | 66.55 | +0.32% | 0.24x | MODERATE 58/100 | VERY_HIGH 81/100 | Watch |
| 10 | XMR/USD | 507.46 | 66.40 | -0.22% | 0.94x | WEAK 33/100 | VERY_HIGH 74/100 | Do nothing |
| 11 | SUI/USD | 0.732 | 61.07 | +0.27% | 0.31x | MODERATE 61/100 | VERY_HIGH 70/100 | Watch |
| 12 | XRP/USD | 0.97167 | 61.02 | +0.08% | 0.33x | MODERATE 51/100 | VERY_HIGH 70/100 | Watch |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | ZEC/USD ⭐ | 948.46 | 100.00 | +0.57% | 2.23x | 25838 | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 2 | INJ/USD ⭐ | 7.243 | 98.78 | +0.61% | 6.32x | 9740 | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 3 | VVV/USD ⭐ | 20.854 | 85.44 | +0.19% | 6.30x | 7120 | STRONG 98/100 | HIGH 55/100 | Watch |

**Same-run overlap:** INJ/USD, ZEC/USD, VVV/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
