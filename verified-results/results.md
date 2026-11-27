# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-27T12:42:00.343262+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/46000475616
**Source SHA:** 858c8bc8ec5d7641ddb39cacd8aca91719f855b1
**Previous ledger commit:** ce29674bf43f71192c7acd6f62f4422966e8d4fb (atomic ledger/results publication)
**Ledger generation:** 2009 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 6s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 628; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 610; valid market observations: 603; OHLC screened: 24.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | ZEC/USD | 757.41 | 112.374 | 98.416 | +11.11% | -0.21% | 10.91x | 3.2 | 2026-11-27T12:41:54.456662+00:00 | Not calibrated | STRONG 80/100 | HIGH 61/100 | Watch | WATCH |
| 2 | HYPE/USD | 65.65 | 105.561 | 92.826 | +5.51% | -0.26% | 2.40x | 1.5 | 2026-11-27T12:41:54.456662+00:00 | Not calibrated | STRONG 80/100 | HIGH 61/100 | Watch | WATCH |
| 3 | LINK/USD | 9.51458 | 86.601 | 71.987 | +2.66% | -0.08% | 7.23x | 3.2 | 2026-11-27T12:41:54.456662+00:00 | Not calibrated | STRONG 73/100 | HIGH 61/100 | Watch | WATCH |
| 4 | SOL/USD | 72.96 | 79.739 | 74.247 | +2.85% | -0.15% | 1.62x | 1.4 | 2026-11-27T12:41:54.456662+00:00 | Not calibrated | MODERATE 60/100 | HIGH 61/100 | Watch | WATCH |
| 5 | VVV/USD | 27.19 | 79.296 | 74.859 | +3.85% | +0.27% | 1.31x | 8.1 | 2026-11-27T12:41:54.456662+00:00 | Not calibrated | STRONG 85/100 | HIGH 55/100 | Watch | WATCH |
| 6 | XDG/USD | 0.0586111 | 76.605 | 74.450 | +3.97% | -0.26% | 1.35x | 0.0 | 2026-11-27T12:41:54.456662+00:00 | Not calibrated | MODERATE 58/100 | HIGH 61/100 | Watch | WATCH |
| 7 | XRP/USD | 0.97065 | 76.439 | 75.356 | +2.96% | -0.26% | 1.24x | 0.7 | 2026-11-27T12:41:54.456662+00:00 | Not calibrated | MODERATE 48/100 | HIGH 68/100 | Watch | WATCH |
| 8 | PEPE/USD | 3.636e-06 | 69.754 | 73.088 | +4.54% | +0.14% | 0.60x | 5.5 | 2026-11-27T12:41:54.456662+00:00 | Not calibrated | MODERATE 55/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 9 | KNTQ/USD | 0.22019 | 69.531 | 67.025 | +4.96% | +0.56% | 0.97x | 0.5 | 2026-11-27T12:41:54.456662+00:00 | Not calibrated | MODERATE 65/100 | HIGH 67/100 | Watch | WATCH |
| 10 | XBT/USD | 61460 | 66.096 | 66.123 | +1.59% | -0.10% | 1.05x | 0.0 | 2026-11-27T12:41:54.456662+00:00 | Not calibrated | WEAK 43/100 | HIGH 68/100 | Watch | WATCH |
| 11 | ETH/USD | 1720.57 | 65.368 | 68.613 | +1.95% | +0.03% | 0.66x | 0.1 | 2026-11-27T12:41:54.456662+00:00 | Not calibrated | MODERATE 53/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 12 | SUI/USD | 0.6858 | 63.467 | 72.517 | +2.71% | -0.22% | 0.20x | 2.9 | 2026-11-27T12:41:54.456662+00:00 | Not calibrated | WEAK 37/100 | VERY_HIGH 76/100 | Watch | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | ZEC/USD | 98.416 | 757.41 | -0.21% | 10.91x |
| 2 | HYPE/USD | 92.826 | 65.65 | -0.26% | 2.40x |
| 3 | XRP/USD | 75.356 | 0.97065 | -0.26% | 1.24x |
| 4 | VVV/USD | 74.859 | 27.19 | +0.27% | 1.31x |
| 5 | XDG/USD | 74.450 | 0.0586111 | -0.26% | 1.35x |
| 6 | SOL/USD | 74.247 | 72.96 | -0.15% | 1.62x |
| 7 | PEPE/USD | 73.088 | 3.636e-06 | +0.14% | 0.60x |
| 8 | SUI/USD | 72.517 | 0.6858 | -0.22% | 0.20x |
| 9 | LINK/USD | 71.987 | 9.51458 | -0.08% | 7.23x |
| 10 | ETH/USD | 68.613 | 1720.57 | +0.03% | 0.66x |
| 11 | KNTQ/USD | 67.025 | 0.22019 | +0.56% | 0.97x |
| 12 | XBT/USD | 66.123 | 61460 | -0.10% | 1.05x |

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

- Persisted scans: 2009; predictions: 17810; observations: 1216576.
- Matured sampled outcomes across 1/6/24/48h: 39641; gap abstentions: 25838. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 150 (sampled only; not a success-rate estimate).
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

**Writer:** 46000475616 · **Generation:** 2009 · **Legacy run:** 46000475616
**Main quote time:** 2026-11-27T12:42:00.343262+00:00 · **Legacy report time:** 2026-11-27T12:42:38.809386+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | ZEC/USD | 757.41 | 112.37 | -0.21% | 10.91x | STRONG 80/100 | HIGH 61/100 | Watch |
| 2 | HYPE/USD | 65.65 | 105.56 | -0.26% | 2.40x | STRONG 80/100 | HIGH 61/100 | Watch |
| 3 | LINK/USD | 9.51458 | 86.60 | -0.08% | 7.23x | STRONG 73/100 | HIGH 61/100 | Watch |
| 4 | SOL/USD | 72.96 | 79.74 | -0.15% | 1.62x | MODERATE 60/100 | HIGH 61/100 | Watch |
| 5 | VVV/USD ⭐ | 27.19 | 79.30 | +0.27% | 1.31x | STRONG 95/100 | HIGH 55/100 | Watch |
| 6 | XDG/USD | 0.0586111 | 76.60 | -0.26% | 1.35x | MODERATE 58/100 | HIGH 61/100 | Watch |
| 7 | XRP/USD | 0.97065 | 76.44 | -0.26% | 1.24x | MODERATE 48/100 | HIGH 68/100 | Watch |
| 8 | PEPE/USD | 3.636e-06 | 69.75 | +0.14% | 0.60x | MODERATE 55/100 | VERY_HIGH 70/100 | Watch |
| 9 | KNTQ/USD | 0.22019 | 69.53 | +0.56% | 0.97x | MODERATE 65/100 | HIGH 67/100 | Watch |
| 10 | XBT/USD | 61460 | 66.10 | -0.10% | 1.05x | WEAK 43/100 | HIGH 68/100 | Watch |
| 11 | ETH/USD | 1720.57 | 65.37 | +0.03% | 0.66x | MODERATE 53/100 | VERY_HIGH 70/100 | Watch |
| 12 | SUI/USD | 0.6858 | 63.47 | -0.22% | 0.20x | WEAK 37/100 | VERY_HIGH 76/100 | Watch |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | VVV/USD ⭐ | 27.19 | 83.38 | +0.27% | 1.31x | 9329 | STRONG 97/100 | HIGH 55/100 | Watch |

**Same-run overlap:** VVV/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
