# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-27T16:53:13.208016+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/46036840401
**Source SHA:** 858c8bc8ec5d7641ddb39cacd8aca91719f855b1
**Previous ledger commit:** 7ac88a62f3de344088e354ae9981accf2dc1ee25 (atomic ledger/results publication)
**Ledger generation:** 2034 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 8s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 628; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 610; valid market observations: 605; OHLC screened: 24.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | ZEC/USD | 753.68 | 111.924 | 98.141 | +10.57% | -0.24% | 6.31x | 3.7 | 2026-11-27T16:53:05.394534+00:00 | Not calibrated | STRONG 80/100 | HIGH 61/100 | Watch | WATCH |
| 2 | SPACE/USD | 0.004164 | 82.224 | 73.335 | +7.54% | -0.65% | 2.21x | 4.8 | 2026-11-27T16:53:05.394534+00:00 | Not calibrated | STRONG 71/100 | VERY_HIGH 73/100 | Watch | WATCH |
| 3 | HYPE/USD | 64.87 | 78.647 | 83.271 | +4.26% | -0.25% | 0.66x | 3.1 | 2026-11-27T16:53:05.394534+00:00 | Not calibrated | WEAK 44/100 | VERY_HIGH 76/100 | Watch | WATCH |
| 4 | UNI/USD | 4.7862 | 72.045 | 71.151 | +2.93% | -0.08% | 1.13x | 3.8 | 2026-11-27T16:53:05.394534+00:00 | Not calibrated | MODERATE 46/100 | HIGH 68/100 | Watch | WATCH |
| 5 | NIGHT/USD | 0.04965 | 71.304 | 70.428 | +2.43% | +0.40% | 0.89x | 2.0 | 2026-11-27T16:53:05.394534+00:00 | Not calibrated | MODERATE 66/100 | HIGH 62/100 | Watch | WATCH |
| 6 | PAXG/USD | 3616.69 | 69.617 | 54.102 | +1.69% | +0.10% | 11.60x | 1.7 | 2026-11-27T16:53:05.394534+00:00 | Not calibrated | STRONG 80/100 | HIGH 55/100 | Watch | WATCH |
| 7 | XDG/USD | 0.0577114 | 66.561 | 71.592 | +2.37% | -0.14% | 0.56x | 0.0 | 2026-11-27T16:53:05.394534+00:00 | Not calibrated | WEAK 38/100 | VERY_HIGH 76/100 | Watch | WATCH |
| 8 | XAUT/USD | 3619 | 64.166 | 48.793 | +1.67% | +0.07% | 3.93x | 0.3 | 2026-11-27T16:53:05.394534+00:00 | Not calibrated | STRONG 77/100 | HIGH 55/100 | Watch | WATCH |
| 9 | SOL/USD | 72.26 | 61.901 | 67.333 | +1.86% | -0.37% | 0.64x | 1.4 | 2026-11-27T16:53:05.394534+00:00 | Not calibrated | WEAK 36/100 | VERY_HIGH 76/100 | Watch | WATCH |
| 10 | VVV/USD | 26.852 | 59.562 | 64.137 | +2.56% | -0.46% | 0.77x | 7.1 | 2026-11-27T16:53:05.394534+00:00 | Not calibrated | WEAK 35/100 | HIGH 68/100 | Watch | WATCH |
| 11 | SUI/USD | 0.6727 | 55.549 | 59.498 | +0.75% | -0.19% | 0.70x | 1.5 | 2026-11-27T16:53:05.394534+00:00 | Not calibrated | WEAK 33/100 | VERY_HIGH 76/100 | Do nothing | WATCH |
| 12 | XRP/USD | 0.94995 | 51.774 | 60.293 | +0.76% | -0.15% | 0.22x | 0.1 | 2026-11-27T16:53:05.394534+00:00 | Not calibrated | WEAK 31/100 | VERY_HIGH 76/100 | Do nothing | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | ZEC/USD | 98.141 | 753.68 | -0.24% | 6.31x |
| 2 | HYPE/USD | 83.271 | 64.87 | -0.25% | 0.66x |
| 3 | SPACE/USD | 73.335 | 0.004164 | -0.65% | 2.21x |
| 4 | XDG/USD | 71.592 | 0.0577114 | -0.14% | 0.56x |
| 5 | UNI/USD | 71.151 | 4.7862 | -0.08% | 1.13x |
| 6 | NIGHT/USD | 70.428 | 0.04965 | +0.40% | 0.89x |
| 7 | SOL/USD | 67.333 | 72.26 | -0.37% | 0.64x |
| 8 | VVV/USD | 64.137 | 26.852 | -0.46% | 0.77x |
| 9 | XRP/USD | 60.293 | 0.94995 | -0.15% | 0.22x |
| 10 | SUI/USD | 59.498 | 0.6727 | -0.19% | 0.70x |
| 11 | PAXG/USD | 54.102 | 3616.69 | +0.10% | 11.60x |
| 12 | XAUT/USD | 48.793 | 3619 | +0.07% | 3.93x |

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

- Persisted scans: 2034; predictions: 18110; observations: 1231679.
- Matured sampled outcomes across 1/6/24/48h: 40553; gap abstentions: 25968. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 152 (sampled only; not a success-rate estimate).
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

**Writer:** 46036840401 · **Generation:** 2034 · **Legacy run:** 46036840401
**Main quote time:** 2026-11-27T16:53:13.208016+00:00 · **Legacy report time:** 2026-11-27T16:54:08.009696+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | ZEC/USD | 753.68 | 111.92 | -0.24% | 6.31x | STRONG 80/100 | HIGH 61/100 | Watch |
| 2 | SPACE/USD | 0.004164 | 82.22 | -0.65% | 2.21x | STRONG 71/100 | VERY_HIGH 73/100 | Watch |
| 3 | HYPE/USD | 64.87 | 78.65 | -0.25% | 0.66x | WEAK 44/100 | VERY_HIGH 76/100 | Watch |
| 4 | UNI/USD | 4.7862 | 72.05 | -0.08% | 1.13x | MODERATE 46/100 | HIGH 68/100 | Watch |
| 5 | NIGHT/USD | 0.04965 | 71.30 | +0.40% | 0.89x | MODERATE 66/100 | HIGH 62/100 | Watch |
| 6 | PAXG/USD | 3616.69 | 69.62 | +0.10% | 11.60x | STRONG 80/100 | HIGH 55/100 | Watch |
| 7 | XDG/USD | 0.0577114 | 66.56 | -0.14% | 0.56x | WEAK 38/100 | VERY_HIGH 76/100 | Watch |
| 8 | XAUT/USD | 3619 | 64.17 | +0.07% | 3.93x | STRONG 77/100 | HIGH 55/100 | Watch |
| 9 | SOL/USD | 72.26 | 61.90 | -0.37% | 0.64x | WEAK 36/100 | VERY_HIGH 76/100 | Watch |
| 10 | VVV/USD | 26.852 | 59.56 | -0.46% | 0.77x | WEAK 35/100 | HIGH 68/100 | Watch |
| 11 | SUI/USD | 0.6727 | 55.55 | -0.19% | 0.70x | WEAK 33/100 | VERY_HIGH 76/100 | Do nothing |
| 12 | XRP/USD | 0.94995 | 51.77 | -0.15% | 0.22x | WEAK 31/100 | VERY_HIGH 76/100 | Do nothing |

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
