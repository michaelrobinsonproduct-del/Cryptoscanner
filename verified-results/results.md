# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-21T19:21:02.533334+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/44940322424
**Source SHA:** 4066e028afbd46ef7ad268722dcaaaa2ca6a4e7e
**Previous ledger commit:** 8ce2aef87332d22c6d534fd2b051104d2d98751e (atomic ledger/results publication)
**Ledger generation:** 1175 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 7s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 628; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 610; valid market observations: 608; OHLC screened: 24.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | XMR/USD | 483.9 | 88.193 | 93.224 | +6.05% | +0.11% | 0.44x | 8.3 | 2026-11-21T19:20:55.813023+00:00 | Not calibrated | MODERATE 64/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 2 | NIGHT/USD | 0.04571 | 85.852 | 90.292 | +8.27% | +0.26% | 0.42x | 6.6 | 2026-11-21T19:20:55.813023+00:00 | Not calibrated | STRONG 73/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 3 | UNI/USD | 4.6874 | 85.832 | 88.439 | +4.93% | -0.17% | 0.82x | 2.1 | 2026-11-21T19:20:55.813023+00:00 | Not calibrated | MODERATE 48/100 | HIGH 68/100 | Watch | WATCH |
| 4 | XBT/USD | 60177.8 | 85.209 | 71.316 | +2.33% | -0.06% | 2.42x | 0.0 | 2026-11-21T19:20:55.813023+00:00 | Not calibrated | STRONG 73/100 | HIGH 61/100 | Watch | WATCH |
| 5 | TAO/USD | 185.3067 | 82.701 | 71.001 | +2.66% | -0.66% | 3.96x | 5.2 | 2026-11-21T19:20:55.813023+00:00 | Not calibrated | STRONG 71/100 | HIGH 61/100 | Watch | WATCH |
| 6 | ETH/USD | 1680.78 | 79.069 | 81.538 | +3.80% | -0.09% | 0.80x | 0.1 | 2026-11-21T19:20:55.813023+00:00 | Not calibrated | MODERATE 45/100 | HIGH 68/100 | Watch | WATCH |
| 7 | ZEC/USD | 786.02 | 76.044 | 79.311 | +3.71% | -0.54% | 0.94x | 3.3 | 2026-11-21T19:20:55.813023+00:00 | Not calibrated | WEAK 43/100 | HIGH 68/100 | Watch | WATCH |
| 8 | PEARL/USD | 1.9736 | 73.732 | 83.689 | +7.95% | -1.85% | 0.93x | 14.7 | 2026-11-21T19:20:55.813023+00:00 | Not calibrated | WEAK 37/100 | VERY_HIGH 78/100 | Do nothing | WATCH |
| 9 | SOL/USD | 70.59 | 71.028 | 73.445 | +2.74% | -0.11% | 0.81x | 1.4 | 2026-11-21T19:20:55.813023+00:00 | Not calibrated | WEAK 41/100 | HIGH 68/100 | Watch | WATCH |
| 10 | XRP/USD | 0.93168 | 68.905 | 72.104 | +2.53% | -0.16% | 0.76x | 1.2 | 2026-11-21T19:20:55.813023+00:00 | Not calibrated | WEAK 39/100 | HIGH 68/100 | Watch | WATCH |
| 11 | HYPE/USD | 61.31 | 66.540 | 59.244 | +0.72% | +0.34% | 1.56x | 1.6 | 2026-11-21T19:20:55.813023+00:00 | Not calibrated | STRONG 78/100 | HIGH 55/100 | Watch | WATCH |
| 12 | XDG/USD | 0.0551012 | 66.189 | 65.438 | +1.52% | -0.13% | 1.14x | 0.4 | 2026-11-21T19:20:55.813023+00:00 | Not calibrated | WEAK 43/100 | HIGH 68/100 | Watch | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | XMR/USD | 93.224 | 483.9 | +0.11% | 0.44x |
| 2 | NIGHT/USD | 90.292 | 0.04571 | +0.26% | 0.42x |
| 3 | UNI/USD | 88.439 | 4.6874 | -0.17% | 0.82x |
| 4 | PEARL/USD | 83.689 | 1.9736 | -1.85% | 0.93x |
| 5 | ETH/USD | 81.538 | 1680.78 | -0.09% | 0.80x |
| 6 | ZEC/USD | 79.311 | 786.02 | -0.54% | 0.94x |
| 7 | SOL/USD | 73.445 | 70.59 | -0.11% | 0.81x |
| 8 | XRP/USD | 72.104 | 0.93168 | -0.16% | 0.76x |
| 9 | XBT/USD | 71.316 | 60177.8 | -0.06% | 2.42x |
| 10 | TAO/USD | 71.001 | 185.3067 | -0.66% | 3.96x |
| 11 | XDG/USD | 65.438 | 0.0551012 | -0.13% | 1.14x |
| 12 | HYPE/USD | 59.244 | 61.31 | +0.34% | 1.56x |

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

- Persisted scans: 1175; predictions: 9409; observations: 710759.
- Matured sampled outcomes across 1/6/24/48h: 12462; gap abstentions: 21182. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 16 (sampled only; not a success-rate estimate).
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

**Writer:** 44940322424 · **Generation:** 1175 · **Legacy run:** 44940322424
**Main quote time:** 2026-11-21T19:21:02.533334+00:00 · **Legacy report time:** 2026-11-21T19:22:05.490638+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | XMR/USD | 483.9 | 88.19 | +0.11% | 0.44x | MODERATE 64/100 | VERY_HIGH 70/100 | Watch |
| 2 | NIGHT/USD | 0.04571 | 85.85 | +0.26% | 0.42x | STRONG 73/100 | VERY_HIGH 70/100 | Watch |
| 3 | UNI/USD | 4.6874 | 85.83 | -0.17% | 0.82x | MODERATE 48/100 | HIGH 68/100 | Watch |
| 4 | XBT/USD | 60177.8 | 85.21 | -0.06% | 2.42x | STRONG 73/100 | HIGH 61/100 | Watch |
| 5 | TAO/USD | 185.3067 | 82.70 | -0.66% | 3.96x | STRONG 71/100 | HIGH 61/100 | Watch |
| 6 | ETH/USD | 1680.78 | 79.07 | -0.09% | 0.80x | MODERATE 45/100 | HIGH 68/100 | Watch |
| 7 | ZEC/USD | 786.02 | 76.04 | -0.54% | 0.94x | WEAK 43/100 | HIGH 68/100 | Watch |
| 8 | PEARL/USD | 1.9736 | 73.73 | -1.85% | 0.93x | WEAK 37/100 | VERY_HIGH 78/100 | Do nothing |
| 9 | SOL/USD | 70.59 | 71.03 | -0.11% | 0.81x | WEAK 41/100 | HIGH 68/100 | Watch |
| 10 | XRP/USD | 0.93168 | 68.91 | -0.16% | 0.76x | WEAK 39/100 | HIGH 68/100 | Watch |
| 11 | HYPE/USD | 61.31 | 66.54 | +0.34% | 1.56x | STRONG 78/100 | HIGH 55/100 | Watch |
| 12 | XDG/USD | 0.0551012 | 66.19 | -0.13% | 1.14x | WEAK 43/100 | HIGH 68/100 | Watch |

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
