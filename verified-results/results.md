# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-21T16:31:39.314840+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/44924853931
**Source SHA:** 7ac7b40f8385b7b363a3015feba153e001ac4fc4
**Previous ledger commit:** ede1d9fd0dcc89410e0474655208c76e0539803e (atomic ledger/results publication)
**Ledger generation:** 1158 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 8s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 628; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 610; valid market observations: 608; OHLC screened: 24.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | UNI/USD | 4.6993 | 103.112 | 89.353 | +5.20% | -0.25% | 3.01x | 4.0 | 2026-11-21T16:31:31.288119+00:00 | Not calibrated | STRONG 80/100 | HIGH 61/100 | Watch | WATCH |
| 2 | XMR/USD | 475.28 | 79.770 | 80.452 | +4.16% | -0.22% | 1.04x | 7.4 | 2026-11-21T16:31:31.288119+00:00 | Not calibrated | MODERATE 50/100 | HIGH 68/100 | Watch | WATCH |
| 3 | ETH/USD | 1680.65 | 78.634 | 81.214 | +3.79% | +0.08% | 0.70x | 0.6 | 2026-11-21T16:31:31.288119+00:00 | Not calibrated | MODERATE 59/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 4 | TAO/USD | 185.9989 | 76.485 | 72.487 | +3.04% | -0.24% | 1.52x | 7.6 | 2026-11-21T16:31:31.288119+00:00 | Not calibrated | MODERATE 58/100 | HIGH 61/100 | Watch | WATCH |
| 5 | SOL/USD | 70.33 | 70.605 | 70.793 | +2.36% | +0.09% | 0.94x | 1.4 | 2026-11-21T16:31:31.288119+00:00 | Not calibrated | MODERATE 55/100 | HIGH 62/100 | Watch | WATCH |
| 6 | ZEC/USD | 784.48 | 69.279 | 78.074 | +3.51% | -0.27% | 0.26x | 2.9 | 2026-11-21T16:31:31.288119+00:00 | Not calibrated | WEAK 40/100 | VERY_HIGH 76/100 | Watch | WATCH |
| 7 | XBT/USD | 59953.3 | 68.230 | 68.644 | +1.95% | +0.21% | 0.85x | 0.0 | 2026-11-21T16:31:31.288119+00:00 | Not calibrated | MODERATE 64/100 | HIGH 62/100 | Watch | WATCH |
| 8 | XLM/USD | 0.128178 | 65.889 | 60.337 | +0.77% | -0.05% | 1.58x | 0.1 | 2026-11-21T16:31:31.288119+00:00 | Not calibrated | MODERATE 53/100 | HIGH 61/100 | Watch | WATCH |
| 9 | XRP/USD | 0.9276 | 65.475 | 69.120 | +2.08% | +0.29% | 0.49x | 0.9 | 2026-11-21T16:31:31.288119+00:00 | Not calibrated | MODERATE 63/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 10 | LINK/USD | 8.56845 | 63.848 | 56.783 | +0.45% | -0.08% | 1.75x | 2.8 | 2026-11-21T16:31:31.288119+00:00 | Not calibrated | MODERATE 52/100 | HIGH 61/100 | Watch | WATCH |
| 11 | USELESS/USD | 0.082 | 63.655 | 70.642 | +10.07% | -0.51% | 0.56x | 28.1 | 2026-11-21T16:31:31.288119+00:00 | Not calibrated | WEAK 27/100 | EXTREME 88/100 | Do nothing | WATCH |
| 12 | XDG/USD | 0.0549015 | 63.447 | 62.953 | +1.15% | -0.15% | 1.12x | 0.3 | 2026-11-21T16:31:31.288119+00:00 | Not calibrated | WEAK 42/100 | HIGH 68/100 | Watch | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | UNI/USD | 89.353 | 4.6993 | -0.25% | 3.01x |
| 2 | ETH/USD | 81.214 | 1680.65 | +0.08% | 0.70x |
| 3 | XMR/USD | 80.452 | 475.28 | -0.22% | 1.04x |
| 4 | ZEC/USD | 78.074 | 784.48 | -0.27% | 0.26x |
| 5 | TAO/USD | 72.487 | 185.9989 | -0.24% | 1.52x |
| 6 | SOL/USD | 70.793 | 70.33 | +0.09% | 0.94x |
| 7 | USELESS/USD | 70.642 | 0.082 | -0.51% | 0.56x |
| 8 | XRP/USD | 69.120 | 0.9276 | +0.29% | 0.49x |
| 9 | XBT/USD | 68.644 | 59953.3 | +0.21% | 0.85x |
| 10 | XDG/USD | 62.953 | 0.0549015 | -0.15% | 1.12x |
| 11 | XLM/USD | 60.337 | 0.128178 | -0.05% | 1.58x |
| 12 | LINK/USD | 56.783 | 8.56845 | -0.08% | 1.75x |

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

- Persisted scans: 1158; predictions: 9205; observations: 700423.
- Matured sampled outcomes across 1/6/24/48h: 12099; gap abstentions: 20803. Per-horizon counts require independent audit; do not infer held-out lift.
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

**Writer:** 44924853931 · **Generation:** 1158 · **Legacy run:** 44924853931
**Main quote time:** 2026-11-21T16:31:39.314840+00:00 · **Legacy report time:** 2026-11-21T16:32:44.602495+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | UNI/USD | 4.6993 | 103.11 | -0.25% | 3.01x | STRONG 80/100 | HIGH 61/100 | Watch |
| 2 | XMR/USD | 475.28 | 79.77 | -0.22% | 1.04x | MODERATE 50/100 | HIGH 68/100 | Watch |
| 3 | ETH/USD | 1680.65 | 78.63 | +0.08% | 0.70x | MODERATE 59/100 | VERY_HIGH 70/100 | Watch |
| 4 | TAO/USD | 185.9989 | 76.48 | -0.24% | 1.52x | MODERATE 58/100 | HIGH 61/100 | Watch |
| 5 | SOL/USD | 70.33 | 70.60 | +0.09% | 0.94x | MODERATE 55/100 | HIGH 62/100 | Watch |
| 6 | ZEC/USD | 784.48 | 69.28 | -0.27% | 0.26x | WEAK 40/100 | VERY_HIGH 76/100 | Watch |
| 7 | XBT/USD | 59953.3 | 68.23 | +0.21% | 0.85x | MODERATE 64/100 | HIGH 62/100 | Watch |
| 8 | XLM/USD | 0.128178 | 65.89 | -0.05% | 1.58x | MODERATE 53/100 | HIGH 61/100 | Watch |
| 9 | XRP/USD | 0.9276 | 65.48 | +0.29% | 0.49x | MODERATE 63/100 | VERY_HIGH 70/100 | Watch |
| 10 | LINK/USD | 8.56845 | 63.85 | -0.08% | 1.75x | MODERATE 52/100 | HIGH 61/100 | Watch |
| 11 | USELESS/USD | 0.082 | 63.65 | -0.51% | 0.56x | WEAK 27/100 | EXTREME 88/100 | Do nothing |
| 12 | XDG/USD | 0.0549015 | 63.45 | -0.15% | 1.12x | WEAK 42/100 | HIGH 68/100 | Watch |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | NIGHT/USD | 0.04319 | 71.96 | +0.28% | 1.34x | 11447 | STRONG 81/100 | HIGH 55/100 | Watch |

**Same-run overlap:** None
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
