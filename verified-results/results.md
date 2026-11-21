# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-21T10:00:48.253599+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/44892150045
**Source SHA:** bdc7e68f7fa75fae6636b7738d52f10a65d92038
**Previous ledger commit:** 7309331db259f657aa4e3bcb4005c3d8a3d9b231 (atomic ledger/results publication)
**Ledger generation:** 1118 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 6s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 628; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 610; valid market observations: 608; OHLC screened: 21.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | VVV/USD | 21.692 | 83.967 | 82.559 | +4.60% | -0.41% | 1.34x | 9.2 | 2026-11-21T10:00:42.263966+00:00 | Not calibrated | MODERATE 62/100 | HIGH 61/100 | Watch | WATCH |
| 2 | ETH/USD | 1634.21 | 75.997 | 61.406 | +0.92% | -0.08% | 2.84x | 0.1 | 2026-11-21T10:00:42.263966+00:00 | Not calibrated | MODERATE 68/100 | HIGH 61/100 | Watch | WATCH |
| 3 | RARE/USD | 0.01411 | 72.121 | 60.491 | +6.09% | -0.49% | 2.41x | 28.4 | 2026-11-21T10:00:42.263966+00:00 | Not calibrated | MODERATE 56/100 | VERY_HIGH 78/100 | Watch | WATCH |
| 4 | ZAMA/USD | 0.05833 | 58.742 | 44.255 | +2.32% | -0.10% | 9.94x | 6.9 | 2026-11-21T10:00:42.263966+00:00 | Not calibrated | MODERATE 59/100 | VERY_HIGH 73/100 | Watch | WATCH |
| 5 | XMR/USD | 461.74 | 58.178 | 60.113 | +1.19% | +0.48% | 0.56x | 6.5 | 2026-11-21T10:00:42.263966+00:00 | Not calibrated | MODERATE 59/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 6 | TRX/USD | 0.302328 | 53.919 | 56.218 | +0.27% | -0.07% | 0.80x | 1.4 | 2026-11-21T10:00:42.263966+00:00 | Not calibrated | WEAK 32/100 | HIGH 68/100 | Do nothing | WATCH |
| 7 | USELESS/USD | 0.07514 | 32.892 | 32.740 | +0.86% | +1.43% | 0.30x | 25.4 | 2026-11-21T10:00:42.263966+00:00 | Not calibrated | WEAK 36/100 | VERY_HIGH 82/100 | Watch | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | VVV/USD | 82.559 | 21.692 | -0.41% | 1.34x |
| 2 | ETH/USD | 61.406 | 1634.21 | -0.08% | 2.84x |
| 3 | RARE/USD | 60.491 | 0.01411 | -0.49% | 2.41x |
| 4 | XMR/USD | 60.113 | 461.74 | +0.48% | 0.56x |
| 5 | TRX/USD | 56.218 | 0.302328 | -0.07% | 0.80x |
| 6 | ZAMA/USD | 44.255 | 0.05833 | -0.10% | 9.94x |
| 7 | USELESS/USD | 32.740 | 0.07514 | +1.43% | 0.30x |

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

- Persisted scans: 1118; predictions: 8775; observations: 676103.
- Matured sampled outcomes across 1/6/24/48h: 11552; gap abstentions: 20308. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 10 (sampled only; not a success-rate estimate).
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

**Writer:** 44892150045 · **Generation:** 1118 · **Legacy run:** 44892150045
**Main quote time:** 2026-11-21T10:00:48.253599+00:00 · **Legacy report time:** 2026-11-21T10:01:49.874739+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | VVV/USD | 21.692 | 83.97 | -0.41% | 1.34x | MODERATE 62/100 | HIGH 61/100 | Watch |
| 2 | ETH/USD | 1634.21 | 76.00 | -0.08% | 2.84x | MODERATE 68/100 | HIGH 61/100 | Watch |
| 3 | RARE/USD | 0.01411 | 72.12 | -0.49% | 2.41x | MODERATE 56/100 | VERY_HIGH 78/100 | Watch |
| 4 | ZAMA/USD | 0.05833 | 58.74 | -0.10% | 9.94x | MODERATE 59/100 | VERY_HIGH 73/100 | Watch |
| 5 | XMR/USD | 461.74 | 58.18 | +0.48% | 0.56x | MODERATE 59/100 | VERY_HIGH 70/100 | Watch |
| 6 | TRX/USD | 0.302328 | 53.92 | -0.07% | 0.80x | WEAK 32/100 | HIGH 68/100 | Do nothing |
| 7 | USELESS/USD | 0.07514 | 32.89 | +1.43% | 0.30x | WEAK 36/100 | VERY_HIGH 82/100 | Watch |

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
