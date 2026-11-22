# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-22T12:01:10.940239+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/45019981038
**Source SHA:** 4066e028afbd46ef7ad268722dcaaaa2ca6a4e7e
**Previous ledger commit:** f6fbad3dfd6bead254578ef5b63e64607a65d7bf (atomic ledger/results publication)
**Ledger generation:** 1280 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 6s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 628; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 610; valid market observations: 609; OHLC screened: 24.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | NIGHT/USD | 0.04676 | 90.770 | 76.412 | +5.60% | -0.13% | 7.30x | 17.1 | 2026-11-22T12:01:04.642267+00:00 | Not calibrated | STRONG 70/100 | HIGH 67/100 | Watch | WATCH |
| 2 | PUMP/USD | 0.00248 | 79.659 | 78.426 | +5.80% | +0.20% | 1.02x | 8.1 | 2026-11-22T12:01:04.642267+00:00 | Not calibrated | STRONG 75/100 | HIGH 62/100 | Watch | WATCH |
| 3 | HYPE/USD | 62.63 | 75.815 | 69.292 | +2.27% | +0.29% | 1.51x | 3.2 | 2026-11-22T12:01:04.642267+00:00 | Not calibrated | STRONG 83/100 | HIGH 55/100 | Consider small entry | WATCH |
| 4 | NEAR/USD | 2.9842 | 73.295 | 76.565 | +3.39% | -0.26% | 0.81x | 4.4 | 2026-11-22T12:01:04.642267+00:00 | Not calibrated | WEAK 42/100 | HIGH 68/100 | Watch | WATCH |
| 5 | TAO/USD | 190.2565 | 70.700 | 66.301 | +2.44% | +0.07% | 1.41x | 6.5 | 2026-11-22T12:01:04.642267+00:00 | Not calibrated | STRONG 70/100 | HIGH 55/100 | Watch | WATCH |
| 6 | XBT/USD | 61014.9 | 67.337 | 65.767 | +1.54% | +0.11% | 1.10x | 0.0 | 2026-11-22T12:01:04.642267+00:00 | Not calibrated | MODERATE 59/100 | HIGH 62/100 | Watch | WATCH |
| 7 | ZEC/USD | 796.18 | 66.016 | 68.879 | +2.31% | +0.06% | 0.68x | 4.6 | 2026-11-22T12:01:04.642267+00:00 | Not calibrated | MODERATE 53/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 8 | INJ/USD | 6.21 | 64.798 | 68.250 | +3.97% | -0.58% | 0.94x | 3.2 | 2026-11-22T12:01:04.642267+00:00 | Not calibrated | WEAK 37/100 | HIGH 68/100 | Watch | WATCH |
| 9 | SUI/USD | 0.659 | 62.641 | 66.135 | +1.81% | -0.03% | 0.67x | 3.0 | 2026-11-22T12:01:04.642267+00:00 | Not calibrated | WEAK 36/100 | VERY_HIGH 76/100 | Watch | WATCH |
| 10 | ETH/USD | 1706.75 | 57.997 | 65.153 | +1.45% | +0.03% | 0.27x | 0.1 | 2026-11-22T12:01:04.642267+00:00 | Not calibrated | MODERATE 49/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 11 | CRV/USD | 0.18509 | 53.784 | 65.785 | +3.77% | -0.64% | 0.12x | 11.4 | 2026-11-22T12:01:04.642267+00:00 | Not calibrated | WEAK 27/100 | VERY_HIGH 82/100 | Do nothing | WATCH |
| 12 | SOL/USD | 70.53 | 52.380 | 57.882 | +0.51% | -0.14% | 0.52x | 1.4 | 2026-11-22T12:01:04.642267+00:00 | Not calibrated | WEAK 31/100 | VERY_HIGH 76/100 | Do nothing | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | PUMP/USD | 78.426 | 0.00248 | +0.20% | 1.02x |
| 2 | NEAR/USD | 76.565 | 2.9842 | -0.26% | 0.81x |
| 3 | NIGHT/USD | 76.412 | 0.04676 | -0.13% | 7.30x |
| 4 | HYPE/USD | 69.292 | 62.63 | +0.29% | 1.51x |
| 5 | ZEC/USD | 68.879 | 796.18 | +0.06% | 0.68x |
| 6 | INJ/USD | 68.250 | 6.21 | -0.58% | 0.94x |
| 7 | TAO/USD | 66.301 | 190.2565 | +0.07% | 1.41x |
| 8 | SUI/USD | 66.135 | 0.659 | -0.03% | 0.67x |
| 9 | CRV/USD | 65.785 | 0.18509 | -0.64% | 0.12x |
| 10 | XBT/USD | 65.767 | 61014.9 | +0.11% | 1.10x |
| 11 | ETH/USD | 65.153 | 1706.75 | +0.03% | 0.27x |
| 12 | SOL/USD | 57.882 | 70.53 | -0.14% | 0.52x |

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

- Persisted scans: 1280; predictions: 10280; observations: 774629.
- Matured sampled outcomes across 1/6/24/48h: 14836; gap abstentions: 22230. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 60 (sampled only; not a success-rate estimate).
- False positives / missed movers: NOT VERIFIED without eligible continuous outcome coverage.
- Baseline vs challenger: recorded as-of; unbiased held-out lift NOT MEASURED.
- Online Kraken /USD stablecoin-base pairs excluded: 18 (counted from this scan's online AssetPairs metadata, not inferred from price).
- Stablecoin base exclusions: BRL1, BUSD, DAI, EUR, EURC, EUROP, EURQ, EURR, EURT, FDUSD, FRAX, GUSD, PYUSD, QCAD, RLUSD, TGBP, TUSD, USD, USD1, USDC, USDD, USDE, USDG, USDQ, USDR, USDS, USDT, ZUSD.
- DEX: NOT USED; no DEX freshness gate.
- OHLC screening abstentions: 8; details in immutable scan JSON artifact.
- Storage: ledger and results published in one non-force Git commit and read back. Independent artifact recovery is NOT VERIFIED by this scan alone.
- Errors: none in successful committed scan; a failed workflow must not publish a SUCCESS report.

# Cryptoscanner — challenger and independent legacy-inspired WATCH

Paper only · risk is high or higher · 30%+ in 48h probability NOT CALIBRATED
Signal confidence 0–100 means setup strength only, NOT a win probability. Actions are research guidance; no trade authorization.

**Writer:** 45019981038 · **Generation:** 1280 · **Legacy run:** 45019981038
**Main quote time:** 2026-11-22T12:01:10.940239+00:00 · **Legacy report time:** 2026-11-22T12:02:12.570460+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | NIGHT/USD | 0.04676 | 90.77 | -0.13% | 7.30x | STRONG 70/100 | HIGH 67/100 | Watch |
| 2 | PUMP/USD ⭐ | 0.00248 | 79.66 | +0.20% | 1.02x | STRONG 85/100 | HIGH 62/100 | Watch |
| 3 | HYPE/USD ⭐ | 62.63 | 75.82 | +0.29% | 1.51x | STRONG 93/100 | HIGH 55/100 | Consider small entry |
| 4 | NEAR/USD | 2.9842 | 73.30 | -0.26% | 0.81x | WEAK 42/100 | HIGH 68/100 | Watch |
| 5 | TAO/USD | 190.2565 | 70.70 | +0.07% | 1.41x | STRONG 70/100 | HIGH 55/100 | Watch |
| 6 | XBT/USD ⭐ | 61014.9 | 67.34 | +0.11% | 1.10x | MODERATE 69/100 | HIGH 62/100 | Watch |
| 7 | ZEC/USD | 796.18 | 66.02 | +0.06% | 0.68x | MODERATE 53/100 | VERY_HIGH 70/100 | Watch |
| 8 | INJ/USD | 6.21 | 64.80 | -0.58% | 0.94x | WEAK 37/100 | HIGH 68/100 | Watch |
| 9 | SUI/USD | 0.659 | 62.64 | -0.03% | 0.67x | WEAK 36/100 | VERY_HIGH 76/100 | Watch |
| 10 | ETH/USD | 1706.75 | 58.00 | +0.03% | 0.27x | MODERATE 49/100 | VERY_HIGH 70/100 | Watch |
| 11 | CRV/USD | 0.18509 | 53.78 | -0.64% | 0.12x | WEAK 27/100 | VERY_HIGH 82/100 | Do nothing |
| 12 | SOL/USD | 70.53 | 52.38 | -0.14% | 0.52x | WEAK 31/100 | VERY_HIGH 76/100 | Do nothing |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | HYPE/USD ⭐ | 62.66 | 79.53 | +0.29% | 1.51x | 13526 | STRONG 95/100 | HIGH 55/100 | Consider small entry |
| 2 | PUMP/USD ⭐ | 0.00248 | 77.80 | +0.20% | 1.02x | 4512 | STRONG 84/100 | HIGH 62/100 | Watch |
| 3 | XBT/USD ⭐ | 61026.6 | 71.42 | +0.11% | 1.10x | 144548 | STRONG 71/100 | HIGH 62/100 | Watch |
| 4 | TIA/USD | 0.3374 | 71.30 | +0.06% | 2.22x | 1763 | STRONG 81/100 | HIGH 67/100 | Watch |

**Same-run overlap:** PUMP/USD, HYPE/USD, XBT/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
