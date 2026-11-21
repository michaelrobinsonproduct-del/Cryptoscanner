# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-21T21:01:25.269357+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/44949150936
**Source SHA:** 4066e028afbd46ef7ad268722dcaaaa2ca6a4e7e
**Previous ledger commit:** 1ecc7121c84984b684ff1ce968a888c9fa99bfb6 (atomic ledger/results publication)
**Ledger generation:** 1185 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 8s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 628; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 610; valid market observations: 608; OHLC screened: 24.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | XMR/USD | 491.19 | 109.727 | 94.596 | +7.65% | +0.67% | 2.18x | 10.8 | 2026-11-21T21:01:17.392474+00:00 | Not calibrated | STRONG 100/100 | HIGH 61/100 | Consider small entry | WATCH |
| 2 | UNI/USD | 4.703 | 97.504 | 90.461 | +5.28% | +0.12% | 1.64x | 3.0 | 2026-11-21T21:01:17.392474+00:00 | Not calibrated | STRONG 84/100 | HIGH 55/100 | Watch | WATCH |
| 3 | ZEC/USD | 791.66 | 91.579 | 84.278 | +4.45% | +0.20% | 1.63x | 3.8 | 2026-11-21T21:01:17.392474+00:00 | Not calibrated | STRONG 91/100 | HIGH 55/100 | Consider small entry | WATCH |
| 4 | TAO/USD | 185.4091 | 88.359 | 71.583 | +2.71% | +0.36% | 2.75x | 4.8 | 2026-11-21T21:01:17.392474+00:00 | Not calibrated | STRONG 99/100 | HIGH 55/100 | Consider small entry | WATCH |
| 5 | XRP/USD | 0.93025 | 86.259 | 71.002 | +2.37% | +0.05% | 4.11x | 1.2 | 2026-11-21T21:01:17.392474+00:00 | Not calibrated | STRONG 88/100 | HIGH 55/100 | Watch | WATCH |
| 6 | XBT/USD | 60335.1 | 85.564 | 73.189 | +2.60% | +0.03% | 2.22x | 0.0 | 2026-11-21T21:01:17.392474+00:00 | Not calibrated | STRONG 88/100 | HIGH 55/100 | Watch | WATCH |
| 7 | QNT/USD | 142.12 | 83.508 | 69.139 | +2.42% | -0.13% | 3.78x | 5.6 | 2026-11-21T21:01:17.392474+00:00 | Not calibrated | STRONG 72/100 | HIGH 61/100 | Watch | WATCH |
| 8 | ETH/USD | 1683.32 | 82.128 | 82.636 | +3.95% | -0.01% | 0.96x | 0.1 | 2026-11-21T21:01:17.392474+00:00 | Not calibrated | MODERATE 46/100 | HIGH 68/100 | Watch | WATCH |
| 9 | NIGHT/USD | 0.04497 | 79.103 | 86.928 | +6.51% | +0.11% | 0.16x | 13.3 | 2026-11-21T21:01:17.392474+00:00 | Not calibrated | MODERATE 55/100 | VERY_HIGH 76/100 | Watch | WATCH |
| 10 | PEARL/USD | 1.9603 | 74.886 | 75.743 | +7.22% | +0.54% | 0.65x | 28.6 | 2026-11-21T21:01:17.392474+00:00 | Not calibrated | MODERATE 57/100 | VERY_HIGH 82/100 | Watch | WATCH |
| 11 | SOL/USD | 70.43 | 68.845 | 71.813 | +2.50% | +0.06% | 0.67x | 1.4 | 2026-11-21T21:01:17.392474+00:00 | Not calibrated | MODERATE 54/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 12 | NEAR/USD | 2.8962 | 67.974 | 66.621 | +1.88% | -0.12% | 1.20x | 3.1 | 2026-11-21T21:01:17.392474+00:00 | Not calibrated | WEAK 44/100 | HIGH 68/100 | Watch | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | XMR/USD | 94.596 | 491.19 | +0.67% | 2.18x |
| 2 | UNI/USD | 90.461 | 4.703 | +0.12% | 1.64x |
| 3 | NIGHT/USD | 86.928 | 0.04497 | +0.11% | 0.16x |
| 4 | ZEC/USD | 84.278 | 791.66 | +0.20% | 1.63x |
| 5 | ETH/USD | 82.636 | 1683.32 | -0.01% | 0.96x |
| 6 | PEARL/USD | 75.743 | 1.9603 | +0.54% | 0.65x |
| 7 | XBT/USD | 73.189 | 60335.1 | +0.03% | 2.22x |
| 8 | SOL/USD | 71.813 | 70.43 | +0.06% | 0.67x |
| 9 | TAO/USD | 71.583 | 185.4091 | +0.36% | 2.75x |
| 10 | XRP/USD | 71.002 | 0.93025 | +0.05% | 4.11x |
| 11 | QNT/USD | 69.139 | 142.12 | -0.13% | 3.78x |
| 12 | NEAR/USD | 66.621 | 2.8962 | -0.12% | 1.20x |

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

- Persisted scans: 1185; predictions: 9529; observations: 716839.
- Matured sampled outcomes across 1/6/24/48h: 12700; gap abstentions: 21414. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 16 (sampled only; not a success-rate estimate).
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

**Writer:** 44949150936 · **Generation:** 1185 · **Legacy run:** 44949150936
**Main quote time:** 2026-11-21T21:01:25.269357+00:00 · **Legacy report time:** 2026-11-21T21:02:26.644455+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | XMR/USD ⭐ | 491.19 | 109.73 | +0.67% | 2.18x | STRONG 100/100 | HIGH 61/100 | Consider small entry |
| 2 | UNI/USD ⭐ | 4.703 | 97.50 | +0.12% | 1.64x | STRONG 94/100 | HIGH 55/100 | Watch |
| 3 | ZEC/USD ⭐ | 791.66 | 91.58 | +0.20% | 1.63x | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 4 | TAO/USD ⭐ | 185.4091 | 88.36 | +0.36% | 2.75x | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 5 | XRP/USD ⭐ | 0.93025 | 86.26 | +0.05% | 4.11x | STRONG 98/100 | HIGH 55/100 | Watch |
| 6 | XBT/USD | 60335.1 | 85.56 | +0.03% | 2.22x | STRONG 88/100 | HIGH 55/100 | Watch |
| 7 | QNT/USD | 142.12 | 83.51 | -0.13% | 3.78x | STRONG 72/100 | HIGH 61/100 | Watch |
| 8 | ETH/USD | 1683.32 | 82.13 | -0.01% | 0.96x | MODERATE 46/100 | HIGH 68/100 | Watch |
| 9 | NIGHT/USD | 0.04497 | 79.10 | +0.11% | 0.16x | MODERATE 55/100 | VERY_HIGH 76/100 | Watch |
| 10 | PEARL/USD | 1.9603 | 74.89 | +0.54% | 0.65x | MODERATE 57/100 | VERY_HIGH 82/100 | Watch |
| 11 | SOL/USD | 70.43 | 68.84 | +0.06% | 0.67x | MODERATE 54/100 | VERY_HIGH 70/100 | Watch |
| 12 | NEAR/USD | 2.8962 | 67.97 | -0.12% | 1.20x | WEAK 44/100 | HIGH 68/100 | Watch |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | ZEC/USD ⭐ | 792.74 | 100.00 | +0.20% | 1.63x | 41885 | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 2 | XMR/USD ⭐ | 489.98 | 91.73 | +0.67% | 2.18x | 12275 | STRONG 100/100 | HIGH 61/100 | Consider small entry |
| 3 | UNI/USD ⭐ | 4.7054 | 91.47 | +0.12% | 1.64x | 11146 | STRONG 91/100 | HIGH 55/100 | Watch |
| 4 | XRP/USD ⭐ | 0.93125 | 88.85 | +0.05% | 4.11x | 50382 | STRONG 99/100 | HIGH 55/100 | Watch |
| 5 | ZRO/USD | 1.197 | 85.35 | +0.34% | 3.10x | 3923 | STRONG 93/100 | HIGH 61/100 | Consider small entry |
| 6 | TAO/USD ⭐ | 185.4893 | 83.84 | +0.36% | 2.75x | 11458 | STRONG 100/100 | HIGH 55/100 | Consider small entry |

**Same-run overlap:** XMR/USD, UNI/USD, ZEC/USD, TAO/USD, XRP/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
