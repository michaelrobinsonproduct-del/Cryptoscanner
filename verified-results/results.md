# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-17T23:00:05.705914+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/44195294365
**Source SHA:** e9b1b6ee47d56a43a454042547735fcd1cdc45a9
**Previous ledger commit:** 20ff6628e052fbf57bcddedfee58a3a176294b57 (atomic ledger/results publication)
**Ledger generation:** 465 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 8s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 627; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 609; valid market observations: 609; OHLC screened: 24.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | INJ/USD | 7.244 | 104.240 | 87.241 | +5.00% | +0.40% | 4.81x | 5.5 | 2026-11-17T22:59:57.265674+00:00 | Not calibrated | STRONG 100/100 | HIGH 55/100 | Consider small entry | WATCH |
| 2 | NEAR/USD | 3.3207 | 96.727 | 89.906 | +5.16% | +0.42% | 1.47x | 2.4 | 2026-11-17T22:59:57.265674+00:00 | Not calibrated | STRONG 93/100 | HIGH 55/100 | Watch | WATCH |
| 3 | ZEC/USD | 945.58 | 91.055 | 87.298 | +4.62% | +0.38% | 1.18x | 0.1 | 2026-11-17T22:59:57.265674+00:00 | Not calibrated | STRONG 81/100 | HIGH 62/100 | Watch | WATCH |
| 4 | STX/USD | 0.2776 | 83.349 | 67.881 | +5.63% | +0.98% | 2.06x | 7.2 | 2026-11-17T22:59:57.265674+00:00 | Not calibrated | STRONG 97/100 | HIGH 60/100 | Consider small entry | WATCH |
| 5 | SOL/USD | 73.99 | 77.392 | 78.499 | +3.45% | +0.27% | 0.75x | 1.4 | 2026-11-17T22:59:57.265674+00:00 | Not calibrated | MODERATE 69/100 | HIGH 62/100 | Watch | WATCH |
| 6 | TAO/USD | 195.1212 | 74.505 | 65.179 | +2.05% | +0.29% | 1.79x | 8.3 | 2026-11-17T22:59:57.265674+00:00 | Not calibrated | STRONG 82/100 | HIGH 55/100 | Consider small entry | WATCH |
| 7 | XMR/USD | 509.36 | 71.883 | 72.560 | +3.20% | +0.68% | 0.59x | 9.6 | 2026-11-17T22:59:57.265674+00:00 | Not calibrated | MODERATE 66/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 8 | TRUST/USD | 0.04728 | 67.799 | 71.655 | +9.93% | +0.00% | 0.61x | 12.7 | 2026-11-17T22:59:57.265674+00:00 | Not calibrated | MODERATE 49/100 | VERY_HIGH 81/100 | Watch | WATCH |
| 9 | SUI/USD | 0.7321 | 62.226 | 66.674 | +1.77% | +0.30% | 0.40x | 1.4 | 2026-11-17T22:59:57.265674+00:00 | Not calibrated | MODERATE 61/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 10 | XRP/USD | 0.97273 | 61.357 | 68.124 | +1.88% | +0.25% | 0.20x | 0.1 | 2026-11-17T22:59:57.265674+00:00 | Not calibrated | MODERATE 61/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 11 | AAVE/USD | 111.74 | 59.853 | 63.019 | +3.01% | +0.01% | 0.68x | 0.9 | 2026-11-17T22:59:57.265674+00:00 | Not calibrated | MODERATE 50/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 12 | AKT/USD | 0.5037 | 59.736 | 64.098 | +5.29% | +0.08% | 0.52x | 10.0 | 2026-11-17T22:59:57.265674+00:00 | Not calibrated | MODERATE 50/100 | VERY_HIGH 75/100 | Watch | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | NEAR/USD | 89.906 | 3.3207 | +0.42% | 1.47x |
| 2 | ZEC/USD | 87.298 | 945.58 | +0.38% | 1.18x |
| 3 | INJ/USD | 87.241 | 7.244 | +0.40% | 4.81x |
| 4 | SOL/USD | 78.499 | 73.99 | +0.27% | 0.75x |
| 5 | XMR/USD | 72.560 | 509.36 | +0.68% | 0.59x |
| 6 | TRUST/USD | 71.655 | 0.04728 | +0.00% | 0.61x |
| 7 | XRP/USD | 68.124 | 0.97273 | +0.25% | 0.20x |
| 8 | STX/USD | 67.881 | 0.2776 | +0.98% | 2.06x |
| 9 | SUI/USD | 66.674 | 0.7321 | +0.30% | 0.40x |
| 10 | TAO/USD | 65.179 | 195.1212 | +0.29% | 1.79x |
| 11 | AKT/USD | 64.098 | 0.5037 | +0.08% | 0.52x |
| 12 | AAVE/USD | 63.019 | 111.74 | +0.01% | 0.68x |

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

- Persisted scans: 465; predictions: 4061; observations: 280192.
- Matured sampled outcomes across 1/6/24/48h: 3195; gap abstentions: 12398. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 0 (sampled only; not a success-rate estimate).
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

**Writer:** 44195294365 · **Generation:** 465 · **Legacy run:** 44195294365
**Main quote time:** 2026-11-17T23:00:05.705914+00:00 · **Legacy report time:** 2026-11-17T23:00:16.886766+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | INJ/USD | 7.244 | 104.24 | +0.40% | 4.81x | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 2 | NEAR/USD | 3.3207 | 96.73 | +0.42% | 1.47x | STRONG 93/100 | HIGH 55/100 | Watch |
| 3 | ZEC/USD | 945.58 | 91.05 | +0.38% | 1.18x | STRONG 81/100 | HIGH 62/100 | Watch |
| 4 | STX/USD ⭐ | 0.2776 | 83.35 | +0.98% | 2.06x | STRONG 100/100 | HIGH 60/100 | Consider small entry |
| 5 | SOL/USD | 73.99 | 77.39 | +0.27% | 0.75x | MODERATE 69/100 | HIGH 62/100 | Watch |
| 6 | TAO/USD | 195.1212 | 74.51 | +0.29% | 1.79x | STRONG 82/100 | HIGH 55/100 | Consider small entry |
| 7 | XMR/USD | 509.36 | 71.88 | +0.68% | 0.59x | MODERATE 66/100 | VERY_HIGH 70/100 | Watch |
| 8 | TRUST/USD | 0.04728 | 67.80 | +0.00% | 0.61x | MODERATE 49/100 | VERY_HIGH 81/100 | Watch |
| 9 | SUI/USD | 0.7321 | 62.23 | +0.30% | 0.40x | MODERATE 61/100 | VERY_HIGH 70/100 | Watch |
| 10 | XRP/USD | 0.97273 | 61.36 | +0.25% | 0.20x | MODERATE 61/100 | VERY_HIGH 70/100 | Watch |
| 11 | AAVE/USD | 111.74 | 59.85 | +0.01% | 0.68x | MODERATE 50/100 | VERY_HIGH 70/100 | Watch |
| 12 | AKT/USD | 0.5037 | 59.74 | +0.08% | 0.52x | MODERATE 50/100 | VERY_HIGH 75/100 | Watch |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | STX/USD ⭐ | 0.2776 | 77.44 | +0.80% | 2.60x | 1397 | STRONG 100/100 | HIGH 60/100 | Consider small entry |

**Same-run overlap:** STX/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
