# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-19T17:30:31.960041+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/44577741455
**Source SHA:** f854bf15990e1aa3564d35bbec4100f929bd3d42
**Previous ledger commit:** d2ec442afc446eadf967f72eb6c7fa11cbfd7172 (atomic ledger/results publication)
**Ledger generation:** 825 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 8s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 627; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 609; valid market observations: 598; OHLC screened: 24.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | VVV/USD | 22.72 | 109.767 | 85.807 | +4.84% | +1.79% | 10.15x | 6.2 | 2026-11-19T17:30:24.139726+00:00 | Not calibrated | STRONG 100/100 | HIGH 55/100 | Consider small entry | WATCH |
| 2 | AKT/USD | 0.5495 | 90.520 | 64.550 | +6.08% | +2.77% | 2.21x | 20.0 | 2026-11-19T17:30:24.139726+00:00 | Not calibrated | STRONG 90/100 | VERY_HIGH 72/100 | Watch | WATCH |
| 3 | LIGHTER/USD | 2.863 | 89.653 | 68.644 | +5.49% | +1.20% | 5.07x | 10.4 | 2026-11-19T17:30:24.139726+00:00 | Not calibrated | STRONG 95/100 | HIGH 66/100 | Consider small entry | WATCH |
| 4 | ZEC/USD | 923.34 | 86.395 | 62.552 | +1.25% | +1.77% | 3.63x | 2.4 | 2026-11-19T17:30:24.139726+00:00 | Not calibrated | STRONG 98/100 | HIGH 55/100 | Consider small entry | WATCH |
| 5 | SKR/USD | 0.010239 | 85.192 | 68.749 | +6.29% | +0.76% | 2.27x | 12.7 | 2026-11-19T17:30:24.139726+00:00 | Not calibrated | STRONG 93/100 | VERY_HIGH 73/100 | Watch | WATCH |
| 6 | BMT/USD | 0.02059 | 83.801 | 71.453 | +9.06% | -0.53% | 39.00x | 9.7 | 2026-11-19T17:30:24.139726+00:00 | Not calibrated | STRONG 72/100 | VERY_HIGH 73/100 | Watch | WATCH |
| 7 | HYPE/USD | 68.24 | 83.480 | 67.037 | +2.03% | +1.62% | 1.83x | 4.4 | 2026-11-19T17:30:24.139726+00:00 | Not calibrated | STRONG 87/100 | HIGH 55/100 | Consider small entry | WATCH |
| 8 | PEPE/USD | 3.819e-06 | 76.625 | 53.252 | +1.95% | +1.67% | 2.91x | 2.6 | 2026-11-19T17:30:24.139726+00:00 | Not calibrated | STRONG 93/100 | HIGH 55/100 | Consider small entry | WATCH |
| 9 | XRP/USD | 0.97358 | 68.083 | 59.144 | +0.75% | +1.11% | 1.34x | 2.2 | 2026-11-19T17:30:24.139726+00:00 | Not calibrated | STRONG 79/100 | HIGH 55/100 | Watch | WATCH |
| 10 | INJ/USD | 7.147 | 67.269 | 58.880 | +2.38% | +1.51% | 1.09x | 2.8 | 2026-11-19T17:30:24.139726+00:00 | Not calibrated | MODERATE 69/100 | HIGH 62/100 | Watch | WATCH |
| 11 | SOL/USD | 73.88 | 66.716 | 57.559 | +0.46% | +1.22% | 1.31x | 1.4 | 2026-11-19T17:30:24.139726+00:00 | Not calibrated | STRONG 78/100 | HIGH 55/100 | Watch | WATCH |
| 12 | ADA/USD | 0.153142 | 65.754 | 62.073 | +1.25% | +1.22% | 0.76x | 3.3 | 2026-11-19T17:30:24.139726+00:00 | Not calibrated | MODERATE 63/100 | HIGH 62/100 | Watch | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | VVV/USD | 85.807 | 22.72 | +1.79% | 10.15x |
| 2 | BMT/USD | 71.453 | 0.02059 | -0.53% | 39.00x |
| 3 | SKR/USD | 68.749 | 0.010239 | +0.76% | 2.27x |
| 4 | LIGHTER/USD | 68.644 | 2.863 | +1.20% | 5.07x |
| 5 | HYPE/USD | 67.037 | 68.24 | +1.62% | 1.83x |
| 6 | AKT/USD | 64.550 | 0.5495 | +2.77% | 2.21x |
| 7 | ZEC/USD | 62.552 | 923.34 | +1.77% | 3.63x |
| 8 | ADA/USD | 62.073 | 0.153142 | +1.22% | 0.76x |
| 9 | XRP/USD | 59.144 | 0.97358 | +1.11% | 1.34x |
| 10 | INJ/USD | 58.880 | 7.147 | +1.51% | 1.09x |
| 11 | SOL/USD | 57.559 | 73.88 | +1.22% | 1.31x |
| 12 | PEPE/USD | 53.252 | 3.819e-06 | +1.67% | 2.91x |

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

- Persisted scans: 825; predictions: 7044; observations: 498761.
- Matured sampled outcomes across 1/6/24/48h: 7019; gap abstentions: 15440. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 10 (sampled only; not a success-rate estimate).
- False positives / missed movers: NOT VERIFIED without eligible continuous outcome coverage.
- Baseline vs challenger: recorded as-of; unbiased held-out lift NOT MEASURED.
- Online Kraken /USD stablecoin-base pairs excluded: 18 (counted from this scan's online AssetPairs metadata, not inferred from price).
- Stablecoin base exclusions: BRL1, BUSD, DAI, EUR, EURC, EUROP, EURQ, EURR, EURT, FDUSD, FRAX, GUSD, PYUSD, QCAD, RLUSD, TGBP, TUSD, USD, USD1, USDC, USDD, USDE, USDG, USDQ, USDR, USDS, USDT, ZUSD.
- DEX: NOT USED; no DEX freshness gate.
- OHLC screening abstentions: 6; details in immutable scan JSON artifact.
- Storage: ledger and results published in one non-force Git commit and read back. Independent artifact recovery is NOT VERIFIED by this scan alone.
- Errors: none in successful committed scan; a failed workflow must not publish a SUCCESS report.

# Cryptoscanner — challenger and independent legacy-inspired WATCH

Paper only · risk is high or higher · 30%+ in 48h probability NOT CALIBRATED
Signal confidence 0–100 means setup strength only, NOT a win probability. Actions are research guidance; no trade authorization.

**Writer:** 44577741455 · **Generation:** 825 · **Legacy run:** 44577741455
**Main quote time:** 2026-11-19T17:30:31.960041+00:00 · **Legacy report time:** 2026-11-19T17:31:30.611564+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | VVV/USD ⭐ | 22.72 | 109.77 | +1.79% | 10.15x | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 2 | AKT/USD ⭐ | 0.5495 | 90.52 | +2.77% | 2.21x | STRONG 100/100 | VERY_HIGH 72/100 | Watch |
| 3 | LIGHTER/USD ⭐ | 2.863 | 89.65 | +1.20% | 5.07x | STRONG 100/100 | HIGH 66/100 | Consider small entry |
| 4 | ZEC/USD | 923.34 | 86.40 | +1.77% | 3.63x | STRONG 98/100 | HIGH 55/100 | Consider small entry |
| 5 | SKR/USD | 0.010239 | 85.19 | +0.76% | 2.27x | STRONG 93/100 | VERY_HIGH 73/100 | Watch |
| 6 | BMT/USD | 0.02059 | 83.80 | -0.53% | 39.00x | STRONG 72/100 | VERY_HIGH 73/100 | Watch |
| 7 | HYPE/USD ⭐ | 68.24 | 83.48 | +1.62% | 1.83x | STRONG 97/100 | HIGH 55/100 | Consider small entry |
| 8 | PEPE/USD | 3.819e-06 | 76.63 | +1.67% | 2.91x | STRONG 93/100 | HIGH 55/100 | Consider small entry |
| 9 | XRP/USD | 0.97358 | 68.08 | +1.11% | 1.34x | STRONG 79/100 | HIGH 55/100 | Watch |
| 10 | INJ/USD ⭐ | 7.147 | 67.27 | +1.51% | 1.09x | STRONG 79/100 | HIGH 62/100 | Watch |
| 11 | SOL/USD | 73.88 | 66.72 | +1.22% | 1.31x | STRONG 78/100 | HIGH 55/100 | Watch |
| 12 | ADA/USD | 0.153142 | 65.75 | +1.22% | 0.76x | MODERATE 63/100 | HIGH 62/100 | Watch |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | VVV/USD ⭐ | 22.832 | 100.00 | +1.79% | 10.15x | 12282 | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 2 | USELESS/USD | 0.10008 | 89.55 | +2.40% | 13.17x | 3144 | STRONG 90/100 | HIGH 67/100 | Consider small entry |
| 3 | LIGHTER/USD ⭐ | 2.863 | 84.84 | +1.20% | 5.07x | 3515 | STRONG 100/100 | HIGH 66/100 | Consider small entry |
| 4 | AKT/USD ⭐ | 0.5495 | 84.05 | +2.77% | 2.21x | 3277 | STRONG 100/100 | HIGH 66/100 | Consider small entry |
| 5 | HYPE/USD ⭐ | 68.19 | 77.84 | +1.62% | 1.83x | 12460 | STRONG 94/100 | HIGH 55/100 | Consider small entry |
| 6 | PYTH/USD | 0.05523 | 77.09 | +0.29% | 2.22x | 2922 | STRONG 89/100 | HIGH 66/100 | Consider small entry |
| 7 | INJ/USD ⭐ | 7.142 | 74.91 | +1.51% | 1.09x | 6921 | STRONG 82/100 | HIGH 62/100 | Watch |

**Same-run overlap:** VVV/USD, AKT/USD, LIGHTER/USD, HYPE/USD, INJ/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
