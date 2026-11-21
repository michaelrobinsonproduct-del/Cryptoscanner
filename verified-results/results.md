# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-21T04:55:31.300433+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/44868343866
**Source SHA:** bdc7e68f7fa75fae6636b7738d52f10a65d92038
**Previous ledger commit:** dcbd91103d21f05878c3452e7946064e5216c000 (atomic ledger/results publication)
**Ledger generation:** 1085 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 2s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 628; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 610; valid market observations: 608; OHLC screened: 7.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | CAP/USD | 0.096378 | 84.227 | 68.734 | +5.28% | +0.10% | 6.20x | 3.8 | 2026-11-21T04:55:28.958831+00:00 | Not calibrated | STRONG 87/100 | HIGH 60/100 | Watch | WATCH |
| 2 | DRV/USD | 0.25596 | 59.487 | 60.244 | +4.24% | +1.13% | 0.36x | 13.7 | 2026-11-21T04:55:28.958831+00:00 | Not calibrated | MODERATE 55/100 | VERY_HIGH 76/100 | Watch | WATCH |
| 3 | SAPIEN/USD | 0.04258 | 45.639 | 34.703 | +3.42% | +1.21% | 1.49x | 40.1 | 2026-11-21T04:55:28.958831+00:00 | Not calibrated | MODERATE 53/100 | EXTREME 89/100 | Do nothing | WATCH |
| 4 | BLESS/USD | 0.014136 | 42.966 | 36.256 | +2.64% | +2.02% | 0.66x | 36.2 | 2026-11-21T04:55:28.958831+00:00 | Not calibrated | WEAK 36/100 | EXTREME 87/100 | Do nothing | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | CAP/USD | 68.734 | 0.096378 | +0.10% | 6.20x |
| 2 | DRV/USD | 60.244 | 0.25596 | +1.13% | 0.36x |
| 3 | BLESS/USD | 36.256 | 0.014136 | +2.02% | 0.66x |
| 4 | SAPIEN/USD | 34.703 | 0.04258 | +1.21% | 1.49x |

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

- Persisted scans: 1085; predictions: 8603; observations: 656040.
- Matured sampled outcomes across 1/6/24/48h: 11164; gap abstentions: 19806. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 10 (sampled only; not a success-rate estimate).
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

**Writer:** 44868343866 · **Generation:** 1085 · **Legacy run:** 44868343866
**Main quote time:** 2026-11-21T04:55:31.300433+00:00 · **Legacy report time:** 2026-11-21T04:56:19.735201+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | CAP/USD ⭐ | 0.096378 | 84.23 | +0.10% | 6.20x | STRONG 97/100 | HIGH 60/100 | Watch |
| 2 | DRV/USD | 0.25596 | 59.49 | +1.13% | 0.36x | MODERATE 55/100 | VERY_HIGH 76/100 | Watch |
| 3 | SAPIEN/USD ⭐ | 0.04258 | 45.64 | +1.21% | 1.49x | MODERATE 63/100 | EXTREME 89/100 | Do nothing |
| 4 | BLESS/USD | 0.014136 | 42.97 | +2.02% | 0.66x | WEAK 36/100 | EXTREME 87/100 | Do nothing |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | CAP/USD ⭐ | 0.096117 | 80.50 | +0.10% | 6.20x | 4681 | STRONG 90/100 | HIGH 66/100 | Watch |
| 2 | SAPIEN/USD ⭐ | 0.04258 | 56.83 | +1.21% | 1.49x | 1162 | STRONG 73/100 | VERY_HIGH 79/100 | Watch |

**Same-run overlap:** CAP/USD, SAPIEN/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
