# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-15T00:26:42.333857+00:00
**GitHub trigger:** scheduled (verified event=schedule; originating cron=20,50 * * * *, intended UTC minute=20,50; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/43658156612
**Source SHA:** 9922dc49dd064a8fcfd48f279dd9fbd2f3c87952
**Previous ledger commit:** 2b7c26a3fb43be211d65426dc5d6309ed84d9d55 (atomic ledger/results publication)
**Ledger generation:** 425 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 8s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 625; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 607; valid market observations: 606; OHLC screened: 24.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | XRP/USD | 0.92763 | 77.339 | 64.963 | +1.52% | +1.27% | 1.60x | 1.3 | 2026-11-15T00:26:34.505780+00:00 | Not calibrated | STRONG 84/100 | HIGH 55/100 | Consider small entry | WATCH |
| 2 | PAXG/USD | 3812.44 | 66.357 | 49.994 | +0.36% | +0.27% | 2.54x | 2.7 | 2026-11-15T00:26:34.505780+00:00 | Not calibrated | STRONG 88/100 | HIGH 55/100 | Watch | WATCH |
| 3 | INJ/USD | 6.873 | 65.800 | 58.564 | +0.93% | +0.72% | 1.36x | 5.8 | 2026-11-15T00:26:34.505780+00:00 | Not calibrated | STRONG 78/100 | HIGH 55/100 | Watch | WATCH |
| 4 | XDG/USD | 0.0575067 | 65.727 | 56.112 | +0.33% | +0.64% | 1.64x | 2.5 | 2026-11-15T00:26:34.505780+00:00 | Not calibrated | STRONG 78/100 | HIGH 55/100 | Watch | WATCH |
| 5 | JUP/USD | 0.25253 | 62.742 | 48.298 | +1.85% | +1.22% | 1.83x | 16.3 | 2026-11-15T00:26:34.505780+00:00 | Not calibrated | STRONG 71/100 | HIGH 61/100 | Watch | WATCH |
| 6 | NEAR/USD | 3.04 | 58.119 | 54.437 | +0.37% | +0.33% | 1.20x | 6.3 | 2026-11-15T00:26:34.505780+00:00 | Not calibrated | MODERATE 64/100 | HIGH 62/100 | Watch | WATCH |
| 7 | ADA/USD | 0.14804 | 55.091 | 53.915 | +0.26% | +0.67% | 0.79x | 5.8 | 2026-11-15T00:26:34.505780+00:00 | Not calibrated | MODERATE 58/100 | HIGH 62/100 | Watch | WATCH |
| 8 | TAO/USD | 184.5534 | 52.960 | 50.806 | +0.37% | +0.57% | 0.93x | 13.6 | 2026-11-15T00:26:34.505780+00:00 | Not calibrated | MODERATE 51/100 | HIGH 68/100 | Watch | WATCH |
| 9 | HBAR/USD | 0.05669 | 50.801 | 49.798 | +0.82% | +0.62% | 0.79x | 5.3 | 2026-11-15T00:26:34.505780+00:00 | Not calibrated | MODERATE 55/100 | HIGH 62/100 | Watch | WATCH |
| 10 | XMR/USD | 471.73 | 50.408 | 48.592 | +0.33% | +0.64% | 0.86x | 17.5 | 2026-11-15T00:26:34.505780+00:00 | Not calibrated | MODERATE 50/100 | HIGH 68/100 | Watch | WATCH |
| 11 | FET/USD | 0.1281 | 48.100 | 44.725 | +0.55% | +0.39% | 1.14x | 7.8 | 2026-11-15T00:26:34.505780+00:00 | Not calibrated | MODERATE 59/100 | HIGH 62/100 | Watch | WATCH |
| 12 | KAS/USD | 0.02641 | 39.707 | 34.917 | +0.27% | +0.34% | 1.31x | 11.4 | 2026-11-15T00:26:34.505780+00:00 | Not calibrated | MODERATE 60/100 | HIGH 61/100 | Watch | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | XRP/USD | 64.963 | 0.92763 | +1.27% | 1.60x |
| 2 | INJ/USD | 58.564 | 6.873 | +0.72% | 1.36x |
| 3 | XDG/USD | 56.112 | 0.0575067 | +0.64% | 1.64x |
| 4 | NEAR/USD | 54.437 | 3.04 | +0.33% | 1.20x |
| 5 | ADA/USD | 53.915 | 0.14804 | +0.67% | 0.79x |
| 6 | TAO/USD | 50.806 | 184.5534 | +0.57% | 0.93x |
| 7 | PAXG/USD | 49.994 | 3812.44 | +0.27% | 2.54x |
| 8 | HBAR/USD | 49.798 | 0.05669 | +0.62% | 0.79x |
| 9 | XMR/USD | 48.592 | 471.73 | +0.64% | 0.86x |
| 10 | JUP/USD | 48.298 | 0.25253 | +1.22% | 1.83x |
| 11 | FET/USD | 44.725 | 0.1281 | +0.39% | 1.14x |
| 12 | KAS/USD | 34.917 | 0.02641 | +0.34% | 1.31x |

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

- Persisted scans: 425; predictions: 3622; observations: 255893.
- Matured sampled outcomes across 1/6/24/48h: 3182; gap abstentions: 10617. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 0 (sampled only; not a success-rate estimate).
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

**Writer:** 43658156612 · **Generation:** 425 · **Legacy run:** 43658156612
**Main quote time:** 2026-11-15T00:26:42.333857+00:00 · **Legacy report time:** 2026-11-15T00:26:54.665967+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | XRP/USD ⭐ | 0.92763 | 77.34 | +1.27% | 1.60x | STRONG 94/100 | HIGH 55/100 | Consider small entry |
| 2 | PAXG/USD ⭐ | 3812.44 | 66.36 | +0.27% | 2.54x | STRONG 98/100 | HIGH 55/100 | Consider small entry |
| 3 | INJ/USD ⭐ | 6.873 | 65.80 | +0.72% | 1.36x | STRONG 88/100 | HIGH 55/100 | Watch |
| 4 | XDG/USD ⭐ | 0.0575067 | 65.73 | +0.64% | 1.64x | STRONG 88/100 | HIGH 55/100 | Consider small entry |
| 5 | JUP/USD ⭐ | 0.25253 | 62.74 | +1.22% | 1.83x | STRONG 81/100 | HIGH 61/100 | Consider small entry |
| 6 | NEAR/USD ⭐ | 3.04 | 58.12 | +0.33% | 1.20x | STRONG 74/100 | HIGH 62/100 | Watch |
| 7 | ADA/USD | 0.14804 | 55.09 | +0.67% | 0.79x | MODERATE 58/100 | HIGH 62/100 | Watch |
| 8 | TAO/USD | 184.5534 | 52.96 | +0.57% | 0.93x | MODERATE 51/100 | HIGH 68/100 | Watch |
| 9 | HBAR/USD | 0.05669 | 50.80 | +0.62% | 0.79x | MODERATE 55/100 | HIGH 62/100 | Watch |
| 10 | XMR/USD | 471.73 | 50.41 | +0.64% | 0.86x | MODERATE 50/100 | HIGH 68/100 | Watch |
| 11 | FET/USD | 0.1281 | 48.10 | +0.39% | 1.14x | MODERATE 59/100 | HIGH 62/100 | Watch |
| 12 | KAS/USD | 0.02641 | 39.71 | +0.34% | 1.31x | MODERATE 60/100 | HIGH 61/100 | Watch |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | XRP/USD ⭐ | 0.927 | 74.72 | +1.27% | 1.60x | 71435 | STRONG 92/100 | HIGH 55/100 | Consider small entry |
| 2 | XDG/USD ⭐ | 0.0575067 | 60.46 | +0.64% | 1.64x | 20640 | STRONG 85/100 | HIGH 55/100 | Consider small entry |
| 3 | JUP/USD ⭐ | 0.25253 | 59.27 | +1.22% | 1.83x | 5605 | STRONG 80/100 | HIGH 61/100 | Consider small entry |
| 4 | PAXG/USD ⭐ | 3812.44 | 54.24 | +0.27% | 2.54x | 5157 | STRONG 92/100 | HIGH 55/100 | Consider small entry |
| 5 | DRV/USD | 0.24128 | 53.29 | +0.37% | 8.13x | 3744 | STRONG 77/100 | HIGH 66/100 | Watch |
| 6 | HYPE/USD | 64.46 | 53.24 | +0.16% | 1.27x | 31799 | MODERATE 52/100 | HIGH 55/100 | Watch |
| 7 | INJ/USD ⭐ | 6.858 | 49.07 | +0.72% | 1.36x | 18653 | STRONG 80/100 | HIGH 55/100 | Watch |
| 8 | NEAR/USD ⭐ | 3.035 | 41.71 | +0.33% | 1.20x | 23992 | MODERATE 66/100 | HIGH 62/100 | Watch |

**Same-run overlap:** XRP/USD, PAXG/USD, INJ/USD, XDG/USD, JUP/USD, NEAR/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
