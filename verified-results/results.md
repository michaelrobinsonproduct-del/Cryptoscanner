# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-21T23:51:18.982014+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/44963656918
**Source SHA:** 4066e028afbd46ef7ad268722dcaaaa2ca6a4e7e
**Previous ledger commit:** 162c136b73eed0a3c982710d3099582f6ce3a867 (atomic ledger/results publication)
**Ledger generation:** 1204 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 8s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 628; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 610; valid market observations: 608; OHLC screened: 24.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | XMR/USD | 491.94 | 103.161 | 98.475 | +7.81% | +0.21% | 1.36x | 3.1 | 2026-11-21T23:51:10.647765+00:00 | Not calibrated | STRONG 95/100 | HIGH 55/100 | Watch | WATCH |
| 2 | ZEC/USD | 780.27 | 90.263 | 74.115 | +2.95% | +0.23% | 2.94x | 3.1 | 2026-11-21T23:51:10.647765+00:00 | Not calibrated | STRONG 100/100 | HIGH 55/100 | Consider small entry | WATCH |
| 3 | NIGHT/USD | 0.04437 | 88.860 | 77.413 | +5.09% | +0.05% | 2.12x | 11.3 | 2026-11-21T23:51:10.647765+00:00 | Not calibrated | STRONG 84/100 | HIGH 61/100 | Watch | WATCH |
| 4 | ETH/USD | 1682.03 | 85.508 | 82.079 | +3.87% | +0.08% | 1.30x | 0.1 | 2026-11-21T23:51:10.647765+00:00 | Not calibrated | STRONG 78/100 | HIGH 55/100 | Watch | WATCH |
| 5 | UNI/USD | 4.7278 | 85.086 | 92.822 | +5.83% | -0.14% | 0.30x | 5.1 | 2026-11-21T23:51:10.647765+00:00 | Not calibrated | MODERATE 48/100 | VERY_HIGH 76/100 | Watch | WATCH |
| 6 | XDG/USD | 0.0551634 | 79.520 | 66.150 | +1.64% | +0.22% | 2.23x | 0.6 | 2026-11-21T23:51:10.647765+00:00 | Not calibrated | STRONG 95/100 | HIGH 55/100 | Consider small entry | WATCH |
| 7 | TAO/USD | 186.2334 | 77.847 | 76.525 | +3.17% | +0.24% | 1.01x | 1.4 | 2026-11-21T23:51:10.647765+00:00 | Not calibrated | STRONG 74/100 | HIGH 62/100 | Watch | WATCH |
| 8 | QNT/USD | 143.76 | 75.240 | 77.438 | +3.60% | +0.52% | 0.52x | 5.6 | 2026-11-21T23:51:10.647765+00:00 | Not calibrated | MODERATE 68/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 9 | HYPE/USD | 61.23 | 73.977 | 58.323 | +0.59% | +0.13% | 5.31x | 1.6 | 2026-11-21T23:51:10.647765+00:00 | Not calibrated | STRONG 82/100 | HIGH 55/100 | Watch | WATCH |
| 10 | PEARL/USD | 1.9491 | 70.304 | 75.480 | +6.61% | -0.55% | 0.76x | 24.7 | 2026-11-21T23:51:10.647765+00:00 | Not calibrated | WEAK 30/100 | VERY_HIGH 80/100 | Do nothing | WATCH |
| 11 | SOL/USD | 70.22 | 69.296 | 69.671 | +2.20% | +0.04% | 0.94x | 1.4 | 2026-11-21T23:51:10.647765+00:00 | Not calibrated | MODERATE 55/100 | HIGH 62/100 | Watch | WATCH |
| 12 | XRP/USD | 0.93203 | 68.333 | 72.696 | +2.57% | -0.00% | 0.56x | 0.5 | 2026-11-21T23:51:10.647765+00:00 | Not calibrated | WEAK 39/100 | VERY_HIGH 76/100 | Watch | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | XMR/USD | 98.475 | 491.94 | +0.21% | 1.36x |
| 2 | UNI/USD | 92.822 | 4.7278 | -0.14% | 0.30x |
| 3 | ETH/USD | 82.079 | 1682.03 | +0.08% | 1.30x |
| 4 | QNT/USD | 77.438 | 143.76 | +0.52% | 0.52x |
| 5 | NIGHT/USD | 77.413 | 0.04437 | +0.05% | 2.12x |
| 6 | TAO/USD | 76.525 | 186.2334 | +0.24% | 1.01x |
| 7 | PEARL/USD | 75.480 | 1.9491 | -0.55% | 0.76x |
| 8 | ZEC/USD | 74.115 | 780.27 | +0.23% | 2.94x |
| 9 | XRP/USD | 72.696 | 0.93203 | -0.00% | 0.56x |
| 10 | SOL/USD | 69.671 | 70.22 | +0.04% | 0.94x |
| 11 | XDG/USD | 66.150 | 0.0551634 | +0.22% | 2.23x |
| 12 | HYPE/USD | 58.323 | 61.23 | +0.13% | 5.31x |

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

- Persisted scans: 1204; predictions: 9757; observations: 728391.
- Matured sampled outcomes across 1/6/24/48h: 13137; gap abstentions: 21660. Per-horizon counts require independent audit; do not infer held-out lift.
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

**Writer:** 44963656918 · **Generation:** 1204 · **Legacy run:** 44963656918
**Main quote time:** 2026-11-21T23:51:18.982014+00:00 · **Legacy report time:** 2026-11-21T23:52:14.169910+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | XMR/USD ⭐ | 491.94 | 103.16 | +0.21% | 1.36x | STRONG 100/100 | HIGH 55/100 | Watch |
| 2 | ZEC/USD ⭐ | 780.27 | 90.26 | +0.23% | 2.94x | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 3 | NIGHT/USD | 0.04437 | 88.86 | +0.05% | 2.12x | STRONG 84/100 | HIGH 61/100 | Watch |
| 4 | ETH/USD ⭐ | 1682.03 | 85.51 | +0.08% | 1.30x | STRONG 88/100 | HIGH 55/100 | Watch |
| 5 | UNI/USD | 4.7278 | 85.09 | -0.14% | 0.30x | MODERATE 48/100 | VERY_HIGH 76/100 | Watch |
| 6 | XDG/USD | 0.0551634 | 79.52 | +0.22% | 2.23x | STRONG 95/100 | HIGH 55/100 | Consider small entry |
| 7 | TAO/USD ⭐ | 186.2334 | 77.85 | +0.24% | 1.01x | STRONG 84/100 | HIGH 62/100 | Watch |
| 8 | QNT/USD | 143.76 | 75.24 | +0.52% | 0.52x | MODERATE 68/100 | VERY_HIGH 70/100 | Watch |
| 9 | HYPE/USD | 61.23 | 73.98 | +0.13% | 5.31x | STRONG 82/100 | HIGH 55/100 | Watch |
| 10 | PEARL/USD | 1.9491 | 70.30 | -0.55% | 0.76x | WEAK 30/100 | VERY_HIGH 80/100 | Do nothing |
| 11 | SOL/USD | 70.22 | 69.30 | +0.04% | 0.94x | MODERATE 55/100 | HIGH 62/100 | Watch |
| 12 | XRP/USD | 0.93203 | 68.33 | -0.00% | 0.56x | WEAK 39/100 | VERY_HIGH 76/100 | Watch |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | ETH/USD ⭐ | 1682.1 | 99.85 | +0.08% | 1.30x | 65396 | STRONG 95/100 | HIGH 55/100 | Watch |
| 2 | XMR/USD ⭐ | 492.08 | 97.61 | +0.21% | 1.36x | 11720 | STRONG 100/100 | HIGH 55/100 | Watch |
| 3 | ZEC/USD ⭐ | 780 | 89.54 | +0.23% | 2.94x | 39641 | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 4 | TAO/USD ⭐ | 186.079 | 83.21 | +0.24% | 1.01x | 10860 | STRONG 87/100 | HIGH 62/100 | Watch |

**Same-run overlap:** XMR/USD, ZEC/USD, ETH/USD, TAO/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
