# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-27T16:22:29.619767+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/46032638728
**Source SHA:** 858c8bc8ec5d7641ddb39cacd8aca91719f855b1
**Previous ledger commit:** 043ba7e2ef3bd4cbdc47ed9ae68345dbf323b7d9 (atomic ledger/results publication)
**Ledger generation:** 2031 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 9s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 628; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 610; valid market observations: 605; OHLC screened: 24.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | ZEC/USD | 740.77 | 92.863 | 97.975 | +8.67% | +0.52% | 0.23x | 4.1 | 2026-11-27T16:22:20.472465+00:00 | Not calibrated | STRONG 76/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 2 | HYPE/USD | 64.56 | 79.239 | 80.551 | +3.76% | +0.26% | 0.74x | 1.6 | 2026-11-27T16:22:20.472465+00:00 | Not calibrated | STRONG 70/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 3 | XDG/USD | 0.0576955 | 70.798 | 71.316 | +2.34% | +0.05% | 0.92x | 0.2 | 2026-11-27T16:22:20.472465+00:00 | Not calibrated | MODERATE 55/100 | HIGH 62/100 | Watch | WATCH |
| 4 | UNI/USD | 4.7667 | 63.764 | 69.949 | +2.51% | -0.26% | 0.51x | 1.9 | 2026-11-27T16:22:20.472465+00:00 | Not calibrated | WEAK 37/100 | VERY_HIGH 76/100 | Watch | WATCH |
| 5 | SOL/USD | 71.88 | 63.021 | 63.580 | +1.33% | -0.08% | 0.99x | 1.4 | 2026-11-27T16:22:20.472465+00:00 | Not calibrated | WEAK 37/100 | HIGH 68/100 | Watch | WATCH |
| 6 | SPACE/USD | 0.004126 | 57.733 | 69.649 | +6.56% | -1.06% | 0.34x | 12.1 | 2026-11-27T16:22:20.472465+00:00 | Not calibrated | WEAK 29/100 | EXTREME 98/100 | Do nothing | WATCH |
| 7 | XRP/USD | 0.94705 | 50.104 | 57.823 | +0.46% | -0.38% | 0.42x | 0.7 | 2026-11-27T16:22:20.472465+00:00 | Not calibrated | WEAK 30/100 | VERY_HIGH 76/100 | Do nothing | WATCH |
| 8 | ADA/USD | 0.149061 | 49.771 | 54.269 | +0.40% | -0.06% | 0.58x | 5.9 | 2026-11-27T16:22:20.472465+00:00 | Not calibrated | WEAK 30/100 | VERY_HIGH 76/100 | Do nothing | WATCH |
| 9 | SUI/USD | 0.6703 | 48.920 | 56.980 | +0.39% | -0.15% | 0.27x | 1.5 | 2026-11-27T16:22:20.472465+00:00 | Not calibrated | WEAK 29/100 | VERY_HIGH 76/100 | Do nothing | WATCH |
| 10 | VVV/USD | 26.656 | 48.279 | 59.114 | +1.81% | -1.10% | 0.47x | 8.3 | 2026-11-27T16:22:20.472465+00:00 | Not calibrated | WEAK 29/100 | VERY_HIGH 80/100 | Do nothing | WATCH |
| 11 | XAUT/USD | 3610.8 | 48.036 | 46.792 | +1.44% | -0.12% | 1.18x | 0.3 | 2026-11-27T16:22:20.472465+00:00 | Not calibrated | WEAK 34/100 | HIGH 68/100 | Do nothing | WATCH |
| 12 | LINK/USD | 9.31673 | 47.279 | 55.921 | +0.52% | -0.04% | 0.15x | 5.5 | 2026-11-27T16:22:20.472465+00:00 | Not calibrated | WEAK 29/100 | VERY_HIGH 76/100 | Do nothing | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | ZEC/USD | 97.975 | 740.77 | +0.52% | 0.23x |
| 2 | HYPE/USD | 80.551 | 64.56 | +0.26% | 0.74x |
| 3 | XDG/USD | 71.316 | 0.0576955 | +0.05% | 0.92x |
| 4 | UNI/USD | 69.949 | 4.7667 | -0.26% | 0.51x |
| 5 | SPACE/USD | 69.649 | 0.004126 | -1.06% | 0.34x |
| 6 | SOL/USD | 63.580 | 71.88 | -0.08% | 0.99x |
| 7 | VVV/USD | 59.114 | 26.656 | -1.10% | 0.47x |
| 8 | XRP/USD | 57.823 | 0.94705 | -0.38% | 0.42x |
| 9 | SUI/USD | 56.980 | 0.6703 | -0.15% | 0.27x |
| 10 | LINK/USD | 55.921 | 9.31673 | -0.04% | 0.15x |
| 11 | ADA/USD | 54.269 | 0.149061 | -0.06% | 0.58x |
| 12 | XAUT/USD | 46.792 | 3610.8 | -0.12% | 1.18x |

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

- Persisted scans: 2031; predictions: 18074; observations: 1229864.
- Matured sampled outcomes across 1/6/24/48h: 40445; gap abstentions: 25962. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 150 (sampled only; not a success-rate estimate).
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

**Writer:** 46032638728 · **Generation:** 2031 · **Legacy run:** 46032638728
**Main quote time:** 2026-11-27T16:22:29.619767+00:00 · **Legacy report time:** 2026-11-27T16:23:22.118656+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | ZEC/USD | 740.77 | 92.86 | +0.52% | 0.23x | STRONG 76/100 | VERY_HIGH 70/100 | Watch |
| 2 | HYPE/USD | 64.56 | 79.24 | +0.26% | 0.74x | STRONG 70/100 | VERY_HIGH 70/100 | Watch |
| 3 | XDG/USD | 0.0576955 | 70.80 | +0.05% | 0.92x | MODERATE 55/100 | HIGH 62/100 | Watch |
| 4 | UNI/USD | 4.7667 | 63.76 | -0.26% | 0.51x | WEAK 37/100 | VERY_HIGH 76/100 | Watch |
| 5 | SOL/USD | 71.88 | 63.02 | -0.08% | 0.99x | WEAK 37/100 | HIGH 68/100 | Watch |
| 6 | SPACE/USD | 0.004126 | 57.73 | -1.06% | 0.34x | WEAK 29/100 | EXTREME 98/100 | Do nothing |
| 7 | XRP/USD | 0.94705 | 50.10 | -0.38% | 0.42x | WEAK 30/100 | VERY_HIGH 76/100 | Do nothing |
| 8 | ADA/USD | 0.149061 | 49.77 | -0.06% | 0.58x | WEAK 30/100 | VERY_HIGH 76/100 | Do nothing |
| 9 | SUI/USD | 0.6703 | 48.92 | -0.15% | 0.27x | WEAK 29/100 | VERY_HIGH 76/100 | Do nothing |
| 10 | VVV/USD | 26.656 | 48.28 | -1.10% | 0.47x | WEAK 29/100 | VERY_HIGH 80/100 | Do nothing |
| 11 | XAUT/USD | 3610.8 | 48.04 | -0.12% | 1.18x | WEAK 34/100 | HIGH 68/100 | Do nothing |
| 12 | LINK/USD | 9.31673 | 47.28 | -0.04% | 0.15x | WEAK 29/100 | VERY_HIGH 76/100 | Do nothing |

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
