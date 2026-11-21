# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-21T21:21:17.069428+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/44950940070
**Source SHA:** 4066e028afbd46ef7ad268722dcaaaa2ca6a4e7e
**Previous ledger commit:** 5e2aa132daaf4733ccb60622f98a6b89fb323e6a (atomic ledger/results publication)
**Ledger generation:** 1187 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 8s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 628; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 610; valid market observations: 608; OHLC screened: 24.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | XMR/USD | 490.07 | 110.979 | 97.039 | +7.40% | -0.21% | 3.98x | 5.9 | 2026-11-21T21:21:08.746417+00:00 | Not calibrated | STRONG 80/100 | HIGH 61/100 | Watch | WATCH |
| 2 | PEARL/USD | 1.9934 | 106.465 | 86.655 | +9.03% | +2.08% | 1.94x | 7.0 | 2026-11-21T21:21:08.746417+00:00 | Not calibrated | STRONG 95/100 | HIGH 55/100 | Consider small entry | WATCH |
| 3 | UNI/USD | 4.7229 | 97.654 | 91.783 | +5.72% | +0.47% | 1.35x | 6.6 | 2026-11-21T21:21:08.746417+00:00 | Not calibrated | STRONG 94/100 | HIGH 55/100 | Watch | WATCH |
| 4 | NIGHT/USD | 0.04471 | 94.636 | 84.508 | +5.90% | -0.20% | 2.11x | 11.2 | 2026-11-21T21:21:08.746417+00:00 | Not calibrated | STRONG 72/100 | HIGH 67/100 | Watch | WATCH |
| 5 | ETH/USD | 1684.38 | 88.609 | 83.094 | +4.02% | +0.09% | 1.50x | 0.1 | 2026-11-21T21:21:08.746417+00:00 | Not calibrated | STRONG 79/100 | HIGH 55/100 | Watch | WATCH |
| 6 | ZEC/USD | 796.19 | 85.165 | 88.220 | +5.05% | +0.71% | 0.34x | 4.3 | 2026-11-21T21:21:08.746417+00:00 | Not calibrated | STRONG 73/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 7 | QNT/USD | 143.09 | 73.965 | 75.097 | +3.12% | +0.11% | 0.83x | 3.5 | 2026-11-21T21:21:08.746417+00:00 | Not calibrated | MODERATE 57/100 | HIGH 62/100 | Watch | WATCH |
| 8 | SOL/USD | 70.46 | 73.871 | 72.119 | +2.55% | +0.17% | 1.09x | 1.4 | 2026-11-21T21:21:08.746417+00:00 | Not calibrated | MODERATE 62/100 | HIGH 62/100 | Watch | WATCH |
| 9 | XBT/USD | 60364.5 | 72.834 | 73.538 | +2.65% | +0.10% | 0.88x | 0.0 | 2026-11-21T21:21:08.746417+00:00 | Not calibrated | MODERATE 56/100 | HIGH 62/100 | Watch | WATCH |
| 10 | TAO/USD | 185.804 | 71.200 | 73.902 | +2.93% | -0.00% | 0.73x | 3.3 | 2026-11-21T21:21:08.746417+00:00 | Not calibrated | WEAK 41/100 | VERY_HIGH 76/100 | Watch | WATCH |
| 11 | XRP/USD | 0.93093 | 66.620 | 71.687 | +2.45% | +0.02% | 0.48x | 0.9 | 2026-11-21T21:21:08.746417+00:00 | Not calibrated | MODERATE 53/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 12 | XDG/USD | 0.0552575 | 61.347 | 67.581 | +1.81% | +0.22% | 0.27x | 0.2 | 2026-11-21T21:21:08.746417+00:00 | Not calibrated | MODERATE 61/100 | VERY_HIGH 70/100 | Watch | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | XMR/USD | 97.039 | 490.07 | -0.21% | 3.98x |
| 2 | UNI/USD | 91.783 | 4.7229 | +0.47% | 1.35x |
| 3 | ZEC/USD | 88.220 | 796.19 | +0.71% | 0.34x |
| 4 | PEARL/USD | 86.655 | 1.9934 | +2.08% | 1.94x |
| 5 | NIGHT/USD | 84.508 | 0.04471 | -0.20% | 2.11x |
| 6 | ETH/USD | 83.094 | 1684.38 | +0.09% | 1.50x |
| 7 | QNT/USD | 75.097 | 143.09 | +0.11% | 0.83x |
| 8 | TAO/USD | 73.902 | 185.804 | -0.00% | 0.73x |
| 9 | XBT/USD | 73.538 | 60364.5 | +0.10% | 0.88x |
| 10 | SOL/USD | 72.119 | 70.46 | +0.17% | 1.09x |
| 11 | XRP/USD | 71.687 | 0.93093 | +0.02% | 0.48x |
| 12 | XDG/USD | 67.581 | 0.0552575 | +0.22% | 0.27x |

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

- Persisted scans: 1187; predictions: 9553; observations: 718055.
- Matured sampled outcomes across 1/6/24/48h: 12748; gap abstentions: 21450. Per-horizon counts require independent audit; do not infer held-out lift.
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

**Writer:** 44950940070 · **Generation:** 1187 · **Legacy run:** 44950940070
**Main quote time:** 2026-11-21T21:21:17.069428+00:00 · **Legacy report time:** 2026-11-21T21:22:03.343661+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | XMR/USD | 490.07 | 110.98 | -0.21% | 3.98x | STRONG 80/100 | HIGH 61/100 | Watch |
| 2 | PEARL/USD | 1.9934 | 106.46 | +2.08% | 1.94x | STRONG 95/100 | HIGH 55/100 | Consider small entry |
| 3 | UNI/USD ⭐ | 4.7229 | 97.65 | +0.47% | 1.35x | STRONG 100/100 | HIGH 55/100 | Watch |
| 4 | NIGHT/USD | 0.04471 | 94.64 | -0.20% | 2.11x | STRONG 72/100 | HIGH 67/100 | Watch |
| 5 | ETH/USD ⭐ | 1684.38 | 88.61 | +0.09% | 1.50x | STRONG 89/100 | HIGH 55/100 | Watch |
| 6 | ZEC/USD | 796.19 | 85.16 | +0.71% | 0.34x | STRONG 73/100 | VERY_HIGH 70/100 | Watch |
| 7 | QNT/USD | 143.09 | 73.96 | +0.11% | 0.83x | MODERATE 57/100 | HIGH 62/100 | Watch |
| 8 | SOL/USD ⭐ | 70.46 | 73.87 | +0.17% | 1.09x | STRONG 72/100 | HIGH 62/100 | Watch |
| 9 | XBT/USD | 60364.5 | 72.83 | +0.10% | 0.88x | MODERATE 56/100 | HIGH 62/100 | Watch |
| 10 | TAO/USD | 185.804 | 71.20 | -0.00% | 0.73x | WEAK 41/100 | VERY_HIGH 76/100 | Watch |
| 11 | XRP/USD | 0.93093 | 66.62 | +0.02% | 0.48x | MODERATE 53/100 | VERY_HIGH 70/100 | Watch |
| 12 | XDG/USD | 0.0552575 | 61.35 | +0.22% | 0.27x | MODERATE 61/100 | VERY_HIGH 70/100 | Watch |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | ETH/USD ⭐ | 1684.64 | 100.00 | +0.09% | 1.50x | 70505 | STRONG 95/100 | HIGH 55/100 | Watch |
| 2 | UNI/USD ⭐ | 4.7273 | 97.73 | +0.47% | 1.35x | 11109 | STRONG 100/100 | HIGH 55/100 | Watch |
| 3 | SOL/USD ⭐ | 70.47 | 80.77 | +0.17% | 1.09x | 48305 | STRONG 75/100 | HIGH 62/100 | Watch |

**Same-run overlap:** UNI/USD, ETH/USD, SOL/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
