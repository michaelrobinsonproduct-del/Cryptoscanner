# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-21T07:20:36.663713+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/44879714305
**Source SHA:** bdc7e68f7fa75fae6636b7738d52f10a65d92038
**Previous ledger commit:** 999403209ae250f3c9efbdddf2d09ec04840356e (atomic ledger/results publication)
**Ledger generation:** 1101 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 6s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 628; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 610; valid market observations: 608; OHLC screened: 16.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | VVV/USD | 21.559 | 70.061 | 78.264 | +3.95% | -0.71% | 0.54x | 8.8 | 2026-11-21T07:20:30.850364+00:00 | Not calibrated | WEAK 40/100 | VERY_HIGH 76/100 | Watch | WATCH |
| 2 | CAP/USD | 0.09434 | 61.436 | 52.160 | +3.06% | +0.11% | 1.87x | 6.0 | 2026-11-21T07:20:30.850364+00:00 | Not calibrated | MODERATE 66/100 | HIGH 60/100 | Watch | WATCH |
| 3 | ETH/USD | 1632.23 | 60.697 | 60.550 | +0.80% | -0.09% | 1.06x | 0.1 | 2026-11-21T07:20:30.850364+00:00 | Not calibrated | WEAK 40/100 | HIGH 68/100 | Watch | WATCH |
| 4 | MORPHO/USD | 1.5409 | 44.835 | 30.901 | +0.62% | -0.21% | 3.23x | 15.8 | 2026-11-21T07:20:30.850364+00:00 | Not calibrated | MODERATE 47/100 | VERY_HIGH 72/100 | Watch | WATCH |
| 5 | BLUR/USD | 0.00738 | 38.528 | 25.960 | +1.10% | +2.07% | 1.22x | 27.3 | 2026-11-21T07:20:30.850364+00:00 | Not calibrated | WEAK 44/100 | VERY_HIGH 79/100 | Watch | WATCH |
| 6 | CT/USD | 0.1225 | 30.508 | 27.564 | +1.16% | +0.08% | 1.25x | 24.5 | 2026-11-21T07:20:30.850364+00:00 | Not calibrated | WEAK 30/100 | VERY_HIGH 72/100 | Do nothing | WATCH |
| 7 | PEAQ/USD | 0.02 | 29.871 | 27.191 | +0.55% | +0.70% | 0.92x | 15.0 | 2026-11-21T07:20:30.850364+00:00 | Not calibrated | WEAK 40/100 | VERY_HIGH 80/100 | Watch | WATCH |
| 8 | SKY/USD | 0.04436 | 26.487 | 39.032 | +1.19% | -0.89% | 0.19x | 9.0 | 2026-11-21T07:20:30.850364+00:00 | Not calibrated | WEAK 18/100 | VERY_HIGH 81/100 | Do nothing | WATCH |
| 9 | ZAMA/USD | 0.05727 | 22.294 | 28.299 | +0.46% | -0.81% | 0.81x | 12.2 | 2026-11-21T07:20:30.850364+00:00 | Not calibrated | WEAK 11/100 | EXTREME 86/100 | Do nothing | WATCH |
| 10 | A/USD | 0.0638 | 16.727 | 17.671 | +0.31% | -0.31% | 1.06x | 31.3 | 2026-11-21T07:20:30.850364+00:00 | Not calibrated | WEAK 8/100 | EXTREME 92/100 | Do nothing | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | VVV/USD | 78.264 | 21.559 | -0.71% | 0.54x |
| 2 | ETH/USD | 60.550 | 1632.23 | -0.09% | 1.06x |
| 3 | CAP/USD | 52.160 | 0.09434 | +0.11% | 1.87x |
| 4 | SKY/USD | 39.032 | 0.04436 | -0.89% | 0.19x |
| 5 | MORPHO/USD | 30.901 | 1.5409 | -0.21% | 3.23x |
| 6 | ZAMA/USD | 28.299 | 0.05727 | -0.81% | 0.81x |
| 7 | CT/USD | 27.564 | 0.1225 | +0.08% | 1.25x |
| 8 | PEAQ/USD | 27.191 | 0.02 | +0.70% | 0.92x |
| 9 | BLUR/USD | 25.960 | 0.00738 | +2.07% | 1.22x |
| 10 | A/USD | 17.671 | 0.0638 | -0.31% | 1.06x |

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

- Persisted scans: 1101; predictions: 8679; observations: 665767.
- Matured sampled outcomes across 1/6/24/48h: 11272; gap abstentions: 20166. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 10 (sampled only; not a success-rate estimate).
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

**Writer:** 44879714305 · **Generation:** 1101 · **Legacy run:** 44879714305
**Main quote time:** 2026-11-21T07:20:36.663713+00:00 · **Legacy report time:** 2026-11-21T07:21:28.377112+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | VVV/USD | 21.559 | 70.06 | -0.71% | 0.54x | WEAK 40/100 | VERY_HIGH 76/100 | Watch |
| 2 | CAP/USD ⭐ | 0.09434 | 61.44 | +0.11% | 1.87x | STRONG 76/100 | HIGH 60/100 | Watch |
| 3 | ETH/USD | 1632.23 | 60.70 | -0.09% | 1.06x | WEAK 40/100 | HIGH 68/100 | Watch |
| 4 | MORPHO/USD | 1.5409 | 44.84 | -0.21% | 3.23x | MODERATE 47/100 | VERY_HIGH 72/100 | Watch |
| 5 | BLUR/USD | 0.00738 | 38.53 | +2.07% | 1.22x | WEAK 44/100 | VERY_HIGH 79/100 | Watch |
| 6 | CT/USD ⭐ | 0.1225 | 30.51 | +0.08% | 1.25x | WEAK 40/100 | VERY_HIGH 72/100 | Watch |
| 7 | PEAQ/USD | 0.02 | 29.87 | +0.70% | 0.92x | WEAK 40/100 | VERY_HIGH 80/100 | Watch |
| 8 | SKY/USD | 0.04436 | 26.49 | -0.89% | 0.19x | WEAK 18/100 | VERY_HIGH 81/100 | Do nothing |
| 9 | ZAMA/USD | 0.05727 | 22.29 | -0.81% | 0.81x | WEAK 11/100 | EXTREME 86/100 | Do nothing |
| 10 | A/USD | 0.0638 | 16.73 | -0.31% | 1.06x | WEAK 8/100 | EXTREME 92/100 | Do nothing |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | DRV/USD | 0.27885 | 87.20 | +4.82% | 1.97x | 9131 | STRONG 84/100 | VERY_HIGH 71/100 | Watch |
| 2 | CAP/USD ⭐ | 0.094232 | 63.35 | +0.11% | 1.87x | 5023 | STRONG 72/100 | HIGH 66/100 | Watch |
| 3 | CT/USD ⭐ | 0.1228 | 39.35 | +0.08% | 1.25x | 2424 | MODERATE 50/100 | HIGH 66/100 | Watch |

**Same-run overlap:** CAP/USD, CT/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
