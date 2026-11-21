# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-21T13:00:57.592746+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/44906593364
**Source SHA:** bdc7e68f7fa75fae6636b7738d52f10a65d92038
**Previous ledger commit:** 5d285dcf23d0d2668736264a91c333d74167bc9e (atomic ledger/results publication)
**Ledger generation:** 1136 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 8s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 628; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 610; valid market observations: 608; OHLC screened: 24.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | VVV/USD | 22.529 | 90.574 | 94.669 | +8.63% | -0.84% | 1.01x | 10.7 | 2026-11-21T13:00:49.349680+00:00 | Not calibrated | MODERATE 50/100 | VERY_HIGH 74/100 | Watch | WATCH |
| 2 | XMR/USD | 468.67 | 83.778 | 70.575 | +2.71% | -0.36% | 3.52x | 6.8 | 2026-11-21T13:00:49.349680+00:00 | Not calibrated | STRONG 72/100 | HIGH 61/100 | Watch | WATCH |
| 3 | ZEC/USD | 767.52 | 72.091 | 60.614 | +1.27% | -0.70% | 2.71x | 6.5 | 2026-11-21T13:00:49.349680+00:00 | Not calibrated | MODERATE 66/100 | HIGH 61/100 | Watch | WATCH |
| 4 | TRX/USD | 0.302672 | 72.038 | 57.134 | +0.39% | +0.00% | 2.49x | 1.2 | 2026-11-21T13:00:49.349680+00:00 | Not calibrated | STRONG 81/100 | HIGH 55/100 | Watch | WATCH |
| 5 | ETH/USD | 1660.13 | 70.518 | 72.611 | +2.52% | -0.22% | 0.90x | 0.1 | 2026-11-21T13:00:49.349680+00:00 | Not calibrated | WEAK 40/100 | HIGH 68/100 | Watch | WATCH |
| 6 | SOL/USD | 69.05 | 56.902 | 57.739 | +0.49% | -0.17% | 1.00x | 1.4 | 2026-11-21T13:00:49.349680+00:00 | Not calibrated | WEAK 38/100 | HIGH 68/100 | Watch | WATCH |
| 7 | TAO/USD | 182.3938 | 49.868 | 57.651 | +1.04% | -0.46% | 0.45x | 9.3 | 2026-11-21T13:00:49.349680+00:00 | Not calibrated | WEAK 30/100 | VERY_HIGH 76/100 | Do nothing | WATCH |
| 8 | SENT/USD | 0.021028 | 48.673 | 41.929 | +2.10% | -0.14% | 1.74x | 7.6 | 2026-11-21T13:00:49.349680+00:00 | Not calibrated | WEAK 44/100 | VERY_HIGH 73/100 | Watch | WATCH |
| 9 | AAVE/USD | 99.23 | 45.281 | 53.182 | +1.37% | -1.14% | 0.78x | 5.0 | 2026-11-21T13:00:49.349680+00:00 | Not calibrated | WEAK 28/100 | VERY_HIGH 72/100 | Do nothing | WATCH |
| 10 | SHX/USD | 0.003363 | 35.642 | 27.739 | +0.30% | +0.21% | 1.69x | 11.9 | 2026-11-21T13:00:49.349680+00:00 | Not calibrated | MODERATE 58/100 | VERY_HIGH 73/100 | Watch | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | VVV/USD | 94.669 | 22.529 | -0.84% | 1.01x |
| 2 | ETH/USD | 72.611 | 1660.13 | -0.22% | 0.90x |
| 3 | XMR/USD | 70.575 | 468.67 | -0.36% | 3.52x |
| 4 | ZEC/USD | 60.614 | 767.52 | -0.70% | 2.71x |
| 5 | SOL/USD | 57.739 | 69.05 | -0.17% | 1.00x |
| 6 | TAO/USD | 57.651 | 182.3938 | -0.46% | 0.45x |
| 7 | TRX/USD | 57.134 | 0.302672 | +0.00% | 2.49x |
| 8 | AAVE/USD | 53.182 | 99.23 | -1.14% | 0.78x |
| 9 | SENT/USD | 41.929 | 0.021028 | -0.14% | 1.74x |
| 10 | SHX/USD | 27.739 | 0.003363 | +0.21% | 1.69x |

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

- Persisted scans: 1136; predictions: 8941; observations: 687047.
- Matured sampled outcomes across 1/6/24/48h: 11734; gap abstentions: 20383. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 16 (sampled only; not a success-rate estimate).
- False positives / missed movers: NOT VERIFIED without eligible continuous outcome coverage.
- Baseline vs challenger: recorded as-of; unbiased held-out lift NOT MEASURED.
- Online Kraken /USD stablecoin-base pairs excluded: 18 (counted from this scan's online AssetPairs metadata, not inferred from price).
- Stablecoin base exclusions: BRL1, BUSD, DAI, EUR, EURC, EUROP, EURQ, EURR, EURT, FDUSD, FRAX, GUSD, PYUSD, QCAD, RLUSD, TGBP, TUSD, USD, USD1, USDC, USDD, USDE, USDG, USDQ, USDR, USDS, USDT, ZUSD.
- DEX: NOT USED; no DEX freshness gate.
- OHLC screening abstentions: 14; details in immutable scan JSON artifact.
- Storage: ledger and results published in one non-force Git commit and read back. Independent artifact recovery is NOT VERIFIED by this scan alone.
- Errors: none in successful committed scan; a failed workflow must not publish a SUCCESS report.

# Cryptoscanner — challenger and independent legacy-inspired WATCH

Paper only · risk is high or higher · 30%+ in 48h probability NOT CALIBRATED
Signal confidence 0–100 means setup strength only, NOT a win probability. Actions are research guidance; no trade authorization.

**Writer:** 44906593364 · **Generation:** 1136 · **Legacy run:** 44906593364
**Main quote time:** 2026-11-21T13:00:57.592746+00:00 · **Legacy report time:** 2026-11-21T13:01:44.709331+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | VVV/USD | 22.529 | 90.57 | -0.84% | 1.01x | MODERATE 50/100 | VERY_HIGH 74/100 | Watch |
| 2 | XMR/USD | 468.67 | 83.78 | -0.36% | 3.52x | STRONG 72/100 | HIGH 61/100 | Watch |
| 3 | ZEC/USD | 767.52 | 72.09 | -0.70% | 2.71x | MODERATE 66/100 | HIGH 61/100 | Watch |
| 4 | TRX/USD | 0.302672 | 72.04 | +0.00% | 2.49x | STRONG 81/100 | HIGH 55/100 | Watch |
| 5 | ETH/USD | 1660.13 | 70.52 | -0.22% | 0.90x | WEAK 40/100 | HIGH 68/100 | Watch |
| 6 | SOL/USD | 69.05 | 56.90 | -0.17% | 1.00x | WEAK 38/100 | HIGH 68/100 | Watch |
| 7 | TAO/USD | 182.3938 | 49.87 | -0.46% | 0.45x | WEAK 30/100 | VERY_HIGH 76/100 | Do nothing |
| 8 | SENT/USD | 0.021028 | 48.67 | -0.14% | 1.74x | WEAK 44/100 | VERY_HIGH 73/100 | Watch |
| 9 | AAVE/USD | 99.23 | 45.28 | -1.14% | 0.78x | WEAK 28/100 | VERY_HIGH 72/100 | Do nothing |
| 10 | SHX/USD | 0.003363 | 35.64 | +0.21% | 1.69x | MODERATE 58/100 | VERY_HIGH 73/100 | Watch |

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
