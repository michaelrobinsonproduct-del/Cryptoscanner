# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-22T20:21:11.385065+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/45065792511
**Source SHA:** 193371a597e6dbc5a6a884defbe9e1519a6a183a
**Previous ledger commit:** 92b613234b1c82e52a91dd10bb40a9801f58cac4 (atomic ledger/results publication)
**Ledger generation:** 1331 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 8s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 628; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 610; valid market observations: 609; OHLC screened: 24.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | PUMP/USD | 0.002556 | 94.817 | 82.348 | +9.04% | -0.51% | 6.60x | 7.8 | 2026-11-22T20:21:03.384404+00:00 | Not calibrated | STRONG 77/100 | HIGH 61/100 | Watch | WATCH |
| 2 | VVV/USD | 26.152 | 89.624 | 88.287 | +5.03% | +0.85% | 0.71x | 3.8 | 2026-11-22T20:21:03.384404+00:00 | Not calibrated | STRONG 75/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 3 | NIGHT/USD | 0.04834 | 84.645 | 90.796 | +9.17% | +0.37% | 0.20x | 4.1 | 2026-11-22T20:21:03.384404+00:00 | Not calibrated | STRONG 72/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 4 | ETH/USD | 1710.25 | 80.780 | 66.609 | +1.66% | -0.17% | 3.07x | 0.1 | 2026-11-22T20:21:03.384404+00:00 | Not calibrated | STRONG 70/100 | HIGH 61/100 | Watch | WATCH |
| 5 | WLD/USD | 0.2378 | 77.514 | 62.934 | +4.44% | -0.08% | 18.09x | 4.2 | 2026-11-22T20:21:03.384404+00:00 | Not calibrated | MODERATE 69/100 | HIGH 66/100 | Watch | WATCH |
| 6 | NEAR/USD | 2.9585 | 74.802 | 71.496 | +2.50% | -0.53% | 1.59x | 2.0 | 2026-11-22T20:21:03.384404+00:00 | Not calibrated | MODERATE 57/100 | HIGH 61/100 | Watch | WATCH |
| 7 | AVAX/USD | 6.666 | 65.385 | 51.432 | +1.57% | -0.21% | 4.33x | 3.0 | 2026-11-22T20:21:03.384404+00:00 | Not calibrated | MODERATE 63/100 | HIGH 61/100 | Watch | WATCH |
| 8 | XMR/USD | 493.56 | 64.214 | 55.479 | +0.36% | -0.07% | 1.91x | 4.1 | 2026-11-22T20:21:03.384404+00:00 | Not calibrated | MODERATE 52/100 | HIGH 61/100 | Watch | WATCH |
| 9 | PIEVERSE/USD | 3.6232 | 64.032 | 73.830 | +6.47% | -0.51% | 0.27x | 23.2 | 2026-11-22T20:21:03.384404+00:00 | Not calibrated | WEAK 27/100 | EXTREME 88/100 | Do nothing | WATCH |
| 10 | XBT/USD | 60539 | 59.854 | 60.223 | +0.75% | -0.21% | 1.07x | 0.0 | 2026-11-22T20:21:03.384404+00:00 | Not calibrated | WEAK 40/100 | HIGH 68/100 | Watch | WATCH |
| 11 | HYPE/USD | 62.37 | 57.952 | 67.115 | +1.85% | +0.03% | 0.07x | 1.6 | 2026-11-22T20:21:03.384404+00:00 | Not calibrated | MODERATE 49/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 12 | LINK/USD | 8.76994 | 57.414 | 56.920 | +2.04% | -0.18% | 1.14x | 2.3 | 2026-11-22T20:21:03.384404+00:00 | Not calibrated | WEAK 39/100 | HIGH 68/100 | Watch | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | NIGHT/USD | 90.796 | 0.04834 | +0.37% | 0.20x |
| 2 | VVV/USD | 88.287 | 26.152 | +0.85% | 0.71x |
| 3 | PUMP/USD | 82.348 | 0.002556 | -0.51% | 6.60x |
| 4 | PIEVERSE/USD | 73.830 | 3.6232 | -0.51% | 0.27x |
| 5 | NEAR/USD | 71.496 | 2.9585 | -0.53% | 1.59x |
| 6 | HYPE/USD | 67.115 | 62.37 | +0.03% | 0.07x |
| 7 | ETH/USD | 66.609 | 1710.25 | -0.17% | 3.07x |
| 8 | WLD/USD | 62.934 | 0.2378 | -0.08% | 18.09x |
| 9 | XBT/USD | 60.223 | 60539 | -0.21% | 1.07x |
| 10 | LINK/USD | 56.920 | 8.76994 | -0.18% | 1.14x |
| 11 | XMR/USD | 55.479 | 493.56 | -0.07% | 1.91x |
| 12 | AVAX/USD | 51.432 | 6.666 | -0.21% | 4.33x |

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

- Persisted scans: 1331; predictions: 10891; observations: 805687.
- Matured sampled outcomes across 1/6/24/48h: 16522; gap abstentions: 22348. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 61 (sampled only; not a success-rate estimate).
- False positives / missed movers: NOT VERIFIED without eligible continuous outcome coverage.
- Baseline vs challenger: recorded as-of; unbiased held-out lift NOT MEASURED.
- Online Kraken /USD stablecoin-base pairs excluded: 18 (counted from this scan's online AssetPairs metadata, not inferred from price).
- Stablecoin base exclusions: BRL1, BUSD, DAI, EUR, EURC, EUROP, EURQ, EURR, EURT, FDUSD, FRAX, GUSD, PYUSD, QCAD, RLUSD, TGBP, TUSD, USD, USD1, USDC, USDD, USDE, USDG, USDQ, USDR, USDS, USDT, ZUSD.
- DEX: NOT USED; no DEX freshness gate.
- OHLC screening abstentions: 10; details in immutable scan JSON artifact.
- Storage: ledger and results published in one non-force Git commit and read back. Independent artifact recovery is NOT VERIFIED by this scan alone.
- Errors: none in successful committed scan; a failed workflow must not publish a SUCCESS report.

# Cryptoscanner — challenger and independent legacy-inspired WATCH

Paper only · risk is high or higher · 30%+ in 48h probability NOT CALIBRATED
Signal confidence 0–100 means setup strength only, NOT a win probability. Actions are research guidance; no trade authorization.

**Writer:** 45065792511 · **Generation:** 1331 · **Legacy run:** 45065792511
**Main quote time:** 2026-11-22T20:21:11.385065+00:00 · **Legacy report time:** 2026-11-22T20:22:05.223894+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | PUMP/USD | 0.002556 | 94.82 | -0.51% | 6.60x | STRONG 77/100 | HIGH 61/100 | Watch |
| 2 | VVV/USD | 26.152 | 89.62 | +0.85% | 0.71x | STRONG 75/100 | VERY_HIGH 70/100 | Watch |
| 3 | NIGHT/USD | 0.04834 | 84.64 | +0.37% | 0.20x | STRONG 72/100 | VERY_HIGH 70/100 | Watch |
| 4 | ETH/USD | 1710.25 | 80.78 | -0.17% | 3.07x | STRONG 70/100 | HIGH 61/100 | Watch |
| 5 | WLD/USD | 0.2378 | 77.51 | -0.08% | 18.09x | MODERATE 69/100 | HIGH 66/100 | Watch |
| 6 | NEAR/USD | 2.9585 | 74.80 | -0.53% | 1.59x | MODERATE 57/100 | HIGH 61/100 | Watch |
| 7 | AVAX/USD | 6.666 | 65.39 | -0.21% | 4.33x | MODERATE 63/100 | HIGH 61/100 | Watch |
| 8 | XMR/USD | 493.56 | 64.21 | -0.07% | 1.91x | MODERATE 52/100 | HIGH 61/100 | Watch |
| 9 | PIEVERSE/USD | 3.6232 | 64.03 | -0.51% | 0.27x | WEAK 27/100 | EXTREME 88/100 | Do nothing |
| 10 | XBT/USD | 60539 | 59.85 | -0.21% | 1.07x | WEAK 40/100 | HIGH 68/100 | Watch |
| 11 | HYPE/USD | 62.37 | 57.95 | +0.03% | 0.07x | MODERATE 49/100 | VERY_HIGH 70/100 | Watch |
| 12 | LINK/USD | 8.76994 | 57.41 | -0.18% | 1.14x | WEAK 39/100 | HIGH 68/100 | Watch |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| — | No confirmed WATCH signals | — | — | — | — | — | — | — | — |

**Same-run overlap:** None
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
