# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-18T16:20:17.982810+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/44345914085
**Source SHA:** b271b90a2cae9e5307600070ce7d0e510fe68996
**Previous ledger commit:** 27b87be80bf9c6ed0afc7b336e10be8e11d99a97 (atomic ledger/results publication)
**Ledger generation:** 611 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 4s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 627; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 609; valid market observations: 609; OHLC screened: 11.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | SENT/USD | 0.019476 | 51.325 | 56.937 | +4.32% | +0.02% | 0.43x | 8.7 | 2026-11-18T16:20:14.369249+00:00 | Not calibrated | MODERATE 46/100 | VERY_HIGH 82/100 | Watch | WATCH |
| 2 | TRUST/USD | 0.04911 | 38.732 | 48.208 | +4.16% | -0.28% | 0.19x | 26.5 | 2026-11-18T16:20:14.369249+00:00 | Not calibrated | WEAK 14/100 | EXTREME 93/100 | Do nothing | WATCH |
| 3 | TRX/USD | 0.308771 | 34.581 | 42.467 | +0.28% | -0.12% | 0.27x | 0.0 | 2026-11-18T16:20:14.369249+00:00 | Not calibrated | WEAK 22/100 | VERY_HIGH 76/100 | Do nothing | WATCH |
| 4 | FLR/USD | 0.00514 | 28.490 | 25.529 | +0.59% | -0.19% | 1.39x | 19.5 | 2026-11-18T16:20:14.369249+00:00 | Not calibrated | WEAK 29/100 | VERY_HIGH 79/100 | Do nothing | WATCH |
| 5 | ZAMA/USD | 0.06038 | 26.888 | 32.716 | +0.75% | -0.49% | 0.66x | 8.3 | 2026-11-18T16:20:14.369249+00:00 | Not calibrated | WEAK 18/100 | EXTREME 88/100 | Do nothing | WATCH |
| 6 | MEGA/USD | 0.05249 | 26.665 | 36.918 | +1.65% | -0.25% | 0.10x | 11.5 | 2026-11-18T16:20:14.369249+00:00 | Not calibrated | WEAK 13/100 | EXTREME 94/100 | Do nothing | WATCH |
| 7 | AKE/USD | 0.01024938 | 24.206 | 33.113 | +2.66% | -0.96% | 0.59x | 37.9 | 2026-11-18T16:20:14.369249+00:00 | Not calibrated | WEAK 2/100 | EXTREME 93/100 | Do nothing | WATCH |
| 8 | CT/USD | 0.1157 | 17.877 | 39.183 | +2.39% | -2.45% | 0.09x | 17.3 | 2026-11-18T16:20:14.369249+00:00 | Not calibrated | WEAK 9/100 | EXTREME 98/100 | Do nothing | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | SENT/USD | 56.937 | 0.019476 | +0.02% | 0.43x |
| 2 | TRUST/USD | 48.208 | 0.04911 | -0.28% | 0.19x |
| 3 | TRX/USD | 42.467 | 0.308771 | -0.12% | 0.27x |
| 4 | CT/USD | 39.183 | 0.1157 | -2.45% | 0.09x |
| 5 | MEGA/USD | 36.918 | 0.05249 | -0.25% | 0.10x |
| 6 | AKE/USD | 33.113 | 0.01024938 | -0.96% | 0.59x |
| 7 | ZAMA/USD | 32.716 | 0.06038 | -0.49% | 0.66x |
| 8 | FLR/USD | 25.529 | 0.00514 | -0.19% | 1.39x |

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

- Persisted scans: 611; predictions: 5246; observations: 369106.
- Matured sampled outcomes across 1/6/24/48h: 4472; gap abstentions: 13125. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 0 (sampled only; not a success-rate estimate).
- False positives / missed movers: NOT VERIFIED without eligible continuous outcome coverage.
- Baseline vs challenger: recorded as-of; unbiased held-out lift NOT MEASURED.
- Online Kraken /USD stablecoin-base pairs excluded: 18 (counted from this scan's online AssetPairs metadata, not inferred from price).
- Stablecoin base exclusions: BRL1, BUSD, DAI, EUR, EURC, EUROP, EURQ, EURR, EURT, FDUSD, FRAX, GUSD, PYUSD, QCAD, RLUSD, TGBP, TUSD, USD, USD1, USDC, USDD, USDE, USDG, USDQ, USDR, USDS, USDT, ZUSD.
- DEX: NOT USED; no DEX freshness gate.
- OHLC screening abstentions: 3; details in immutable scan JSON artifact.
- Storage: ledger and results published in one non-force Git commit and read back. Independent artifact recovery is NOT VERIFIED by this scan alone.
- Errors: none in successful committed scan; a failed workflow must not publish a SUCCESS report.

# Cryptoscanner — challenger and independent legacy-inspired WATCH

Paper only · risk is high or higher · 30%+ in 48h probability NOT CALIBRATED
Signal confidence 0–100 means setup strength only, NOT a win probability. Actions are research guidance; no trade authorization.

**Writer:** 44345914085 · **Generation:** 611 · **Legacy run:** 44345914085
**Main quote time:** 2026-11-18T16:20:17.982810+00:00 · **Legacy report time:** 2026-11-18T16:20:48.145641+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | SENT/USD | 0.019476 | 51.33 | +0.02% | 0.43x | MODERATE 46/100 | VERY_HIGH 82/100 | Watch |
| 2 | TRUST/USD | 0.04911 | 38.73 | -0.28% | 0.19x | WEAK 14/100 | EXTREME 93/100 | Do nothing |
| 3 | TRX/USD | 0.308771 | 34.58 | -0.12% | 0.27x | WEAK 22/100 | VERY_HIGH 76/100 | Do nothing |
| 4 | FLR/USD | 0.00514 | 28.49 | -0.19% | 1.39x | WEAK 29/100 | VERY_HIGH 79/100 | Do nothing |
| 5 | ZAMA/USD | 0.06038 | 26.89 | -0.49% | 0.66x | WEAK 18/100 | EXTREME 88/100 | Do nothing |
| 6 | MEGA/USD | 0.05249 | 26.66 | -0.25% | 0.10x | WEAK 13/100 | EXTREME 94/100 | Do nothing |
| 7 | AKE/USD | 0.01024938 | 24.21 | -0.96% | 0.59x | WEAK 2/100 | EXTREME 93/100 | Do nothing |
| 8 | CT/USD | 0.1157 | 17.88 | -2.45% | 0.09x | WEAK 9/100 | EXTREME 98/100 | Do nothing |

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
