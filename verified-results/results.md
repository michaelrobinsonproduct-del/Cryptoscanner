# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-21T07:50:38.809357+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/44882020439
**Source SHA:** bdc7e68f7fa75fae6636b7738d52f10a65d92038
**Previous ledger commit:** 0b3385d6a2dd97fc750ae7bcf0e7594b3248fa5e (atomic ledger/results publication)
**Ledger generation:** 1104 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 5s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 628; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 610; valid market observations: 608; OHLC screened: 18.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | VVV/USD | 21.419 | 63.921 | 68.849 | +3.28% | +0.03% | 0.49x | 18.2 | 2026-11-21T07:50:33.772370+00:00 | Not calibrated | MODERATE 47/100 | VERY_HIGH 76/100 | Watch | WATCH |
| 2 | CAP/USD | 0.094131 | 56.981 | 52.324 | +2.83% | +0.41% | 1.26x | 2.3 | 2026-11-21T07:50:33.772370+00:00 | Not calibrated | MODERATE 63/100 | HIGH 60/100 | Watch | WATCH |
| 3 | TRX/USD | 0.302519 | 51.171 | 56.619 | +0.34% | +0.06% | 0.43x | 1.1 | 2026-11-21T07:50:33.772370+00:00 | Not calibrated | MODERATE 46/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 4 | ETH/USD | 1627.65 | 48.323 | 57.587 | +0.51% | -0.54% | 0.34x | 2.0 | 2026-11-21T07:50:33.772370+00:00 | Not calibrated | WEAK 29/100 | VERY_HIGH 76/100 | Do nothing | WATCH |
| 5 | SENT/USD | 0.020732 | 33.184 | 32.217 | +0.67% | +0.06% | 1.07x | 6.8 | 2026-11-21T07:50:33.772370+00:00 | Not calibrated | WEAK 42/100 | VERY_HIGH 74/100 | Watch | WATCH |
| 6 | BLUR/USD | 0.00732 | 27.195 | 20.189 | +0.27% | -0.14% | 1.77x | 27.4 | 2026-11-21T07:50:33.772370+00:00 | Not calibrated | WEAK 24/100 | VERY_HIGH 78/100 | Do nothing | WATCH |
| 7 | MORPHO/USD | 1.55455 | 26.623 | 30.062 | +1.51% | +0.52% | 0.40x | 30.1 | 2026-11-21T07:50:33.772370+00:00 | Not calibrated | WEAK 33/100 | EXTREME 87/100 | Do nothing | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | VVV/USD | 68.849 | 21.419 | +0.03% | 0.49x |
| 2 | ETH/USD | 57.587 | 1627.65 | -0.54% | 0.34x |
| 3 | TRX/USD | 56.619 | 0.302519 | +0.06% | 0.43x |
| 4 | CAP/USD | 52.324 | 0.094131 | +0.41% | 1.26x |
| 5 | SENT/USD | 32.217 | 0.020732 | +0.06% | 1.07x |
| 6 | MORPHO/USD | 30.062 | 1.55455 | +0.52% | 0.40x |
| 7 | BLUR/USD | 20.189 | 0.00732 | -0.14% | 1.77x |

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

- Persisted scans: 1104; predictions: 8701; observations: 667591.
- Matured sampled outcomes across 1/6/24/48h: 11334; gap abstentions: 20199. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 10 (sampled only; not a success-rate estimate).
- False positives / missed movers: NOT VERIFIED without eligible continuous outcome coverage.
- Baseline vs challenger: recorded as-of; unbiased held-out lift NOT MEASURED.
- Online Kraken /USD stablecoin-base pairs excluded: 18 (counted from this scan's online AssetPairs metadata, not inferred from price).
- Stablecoin base exclusions: BRL1, BUSD, DAI, EUR, EURC, EUROP, EURQ, EURR, EURT, FDUSD, FRAX, GUSD, PYUSD, QCAD, RLUSD, TGBP, TUSD, USD, USD1, USDC, USDD, USDE, USDG, USDQ, USDR, USDS, USDT, ZUSD.
- DEX: NOT USED; no DEX freshness gate.
- OHLC screening abstentions: 11; details in immutable scan JSON artifact.
- Storage: ledger and results published in one non-force Git commit and read back. Independent artifact recovery is NOT VERIFIED by this scan alone.
- Errors: none in successful committed scan; a failed workflow must not publish a SUCCESS report.

# Cryptoscanner — challenger and independent legacy-inspired WATCH

Paper only · risk is high or higher · 30%+ in 48h probability NOT CALIBRATED
Signal confidence 0–100 means setup strength only, NOT a win probability. Actions are research guidance; no trade authorization.

**Writer:** 44882020439 · **Generation:** 1104 · **Legacy run:** 44882020439
**Main quote time:** 2026-11-21T07:50:38.809357+00:00 · **Legacy report time:** 2026-11-21T07:51:40.765848+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | VVV/USD | 21.419 | 63.92 | +0.03% | 0.49x | MODERATE 47/100 | VERY_HIGH 76/100 | Watch |
| 2 | CAP/USD ⭐ | 0.094131 | 56.98 | +0.41% | 1.26x | STRONG 73/100 | HIGH 60/100 | Watch |
| 3 | TRX/USD | 0.302519 | 51.17 | +0.06% | 0.43x | MODERATE 46/100 | VERY_HIGH 70/100 | Watch |
| 4 | ETH/USD | 1627.65 | 48.32 | -0.54% | 0.34x | WEAK 29/100 | VERY_HIGH 76/100 | Do nothing |
| 5 | SENT/USD ⭐ | 0.020732 | 33.18 | +0.06% | 1.07x | MODERATE 52/100 | VERY_HIGH 74/100 | Watch |
| 6 | BLUR/USD | 0.00732 | 27.20 | -0.14% | 1.77x | WEAK 24/100 | VERY_HIGH 78/100 | Do nothing |
| 7 | MORPHO/USD | 1.55455 | 26.62 | +0.52% | 0.40x | WEAK 33/100 | EXTREME 87/100 | Do nothing |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | CAP/USD ⭐ | 0.094131 | 64.17 | +0.41% | 1.26x | 4879 | STRONG 77/100 | HIGH 60/100 | Watch |
| 2 | SENT/USD ⭐ | 0.020732 | 30.99 | +0.06% | 1.07x | 4769 | MODERATE 50/100 | VERY_HIGH 74/100 | Watch |

**Same-run overlap:** CAP/USD, SENT/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
