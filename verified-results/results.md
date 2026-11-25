# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-25T20:47:19.126842+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/45697845195
**Source SHA:** 858c8bc8ec5d7641ddb39cacd8aca91719f855b1
**Previous ledger commit:** 30a9401d79f41ba6c4b5bf8123539434e1606f2f (atomic ledger/results publication)
**Ledger generation:** 1765 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 9s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 628; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 610; valid market observations: 609; OHLC screened: 24.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | HYPE/USD | 61.28 | 83.877 | 70.669 | +2.36% | -0.36% | 4.08x | 1.6 | 2026-11-25T20:47:10.512557+00:00 | Not calibrated | STRONG 72/100 | HIGH 61/100 | Watch | WATCH |
| 2 | NEAR/USD | 3.0101 | 83.336 | 82.654 | +4.35% | +0.51% | 0.81x | 5.7 | 2026-11-25T20:47:10.512557+00:00 | Not calibrated | STRONG 72/100 | HIGH 62/100 | Watch | WATCH |
| 3 | DRV/USD | 0.349 | 78.367 | 71.636 | +11.05% | -0.24% | 1.79x | 25.3 | 2026-11-25T20:47:10.512557+00:00 | Not calibrated | MODERATE 49/100 | VERY_HIGH 73/100 | Watch | WATCH |
| 4 | LINK/USD | 9.05493 | 75.150 | 61.974 | +2.42% | -0.36% | 3.63x | 6.5 | 2026-11-25T20:47:10.512557+00:00 | Not calibrated | MODERATE 68/100 | HIGH 61/100 | Watch | WATCH |
| 5 | LTC/USD | 42.31 | 74.954 | 77.654 | +3.57% | -0.52% | 0.99x | 4.7 | 2026-11-25T20:47:10.512557+00:00 | Not calibrated | WEAK 42/100 | HIGH 68/100 | Watch | WATCH |
| 6 | XPL/USD | 0.0476 | 74.644 | 71.897 | +8.18% | +0.21% | 1.17x | 21.1 | 2026-11-25T20:47:10.512557+00:00 | Not calibrated | MODERATE 62/100 | VERY_HIGH 74/100 | Watch | WATCH |
| 7 | ZEC/USD | 754.79 | 68.591 | 68.738 | +2.15% | -0.27% | 1.12x | 2.6 | 2026-11-25T20:47:10.512557+00:00 | Not calibrated | WEAK 44/100 | HIGH 68/100 | Watch | WATCH |
| 8 | XMR/USD | 520.9 | 68.033 | 65.819 | +2.22% | +0.22% | 1.11x | 9.4 | 2026-11-25T20:47:10.512557+00:00 | Not calibrated | MODERATE 69/100 | HIGH 62/100 | Watch | WATCH |
| 9 | SUI/USD | 0.6614 | 60.319 | 68.514 | +2.15% | -0.36% | 0.36x | 3.0 | 2026-11-25T20:47:10.512557+00:00 | Not calibrated | WEAK 35/100 | VERY_HIGH 76/100 | Watch | WATCH |
| 10 | XLM/USD | 0.127638 | 59.454 | 62.834 | +2.89% | -0.08% | 0.70x | 2.5 | 2026-11-25T20:47:10.512557+00:00 | Not calibrated | WEAK 35/100 | VERY_HIGH 76/100 | Watch | WATCH |
| 11 | PAXG/USD | 3567.89 | 57.940 | 59.704 | +0.74% | -0.38% | 1.01x | 0.9 | 2026-11-25T20:47:10.512557+00:00 | Not calibrated | WEAK 39/100 | HIGH 68/100 | Watch | WATCH |
| 12 | XRP/USD | 0.93549 | 56.596 | 63.416 | +1.29% | -0.31% | 0.47x | 1.2 | 2026-11-25T20:47:10.512557+00:00 | Not calibrated | WEAK 33/100 | VERY_HIGH 76/100 | Do nothing | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | NEAR/USD | 82.654 | 3.0101 | +0.51% | 0.81x |
| 2 | LTC/USD | 77.654 | 42.31 | -0.52% | 0.99x |
| 3 | XPL/USD | 71.897 | 0.0476 | +0.21% | 1.17x |
| 4 | DRV/USD | 71.636 | 0.349 | -0.24% | 1.79x |
| 5 | HYPE/USD | 70.669 | 61.28 | -0.36% | 4.08x |
| 6 | ZEC/USD | 68.738 | 754.79 | -0.27% | 1.12x |
| 7 | SUI/USD | 68.514 | 0.6614 | -0.36% | 0.36x |
| 8 | XMR/USD | 65.819 | 520.9 | +0.22% | 1.11x |
| 9 | XRP/USD | 63.416 | 0.93549 | -0.31% | 0.47x |
| 10 | XLM/USD | 62.834 | 0.127638 | -0.08% | 0.70x |
| 11 | LINK/USD | 61.974 | 9.05493 | -0.36% | 3.63x |
| 12 | PAXG/USD | 59.704 | 3567.89 | -0.38% | 1.01x |

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

- Persisted scans: 1765; predictions: 14924; observations: 1069929.
- Matured sampled outcomes across 1/6/24/48h: 32666; gap abstentions: 23031. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 146 (sampled only; not a success-rate estimate).
- False positives / missed movers: NOT VERIFIED without eligible continuous outcome coverage.
- Baseline vs challenger: recorded as-of; unbiased held-out lift NOT MEASURED.
- Online Kraken /USD stablecoin-base pairs excluded: 18 (counted from this scan's online AssetPairs metadata, not inferred from price).
- Stablecoin base exclusions: BRL1, BUSD, DAI, EUR, EURC, EUROP, EURQ, EURR, EURT, FDUSD, FRAX, GUSD, PYUSD, QCAD, RLUSD, TGBP, TUSD, USD, USD1, USDC, USDD, USDE, USDG, USDQ, USDR, USDS, USDT, ZUSD.
- DEX: NOT USED; no DEX freshness gate.
- OHLC screening abstentions: 5; details in immutable scan JSON artifact.
- Storage: ledger and results published in one non-force Git commit and read back. Independent artifact recovery is NOT VERIFIED by this scan alone.
- Errors: none in successful committed scan; a failed workflow must not publish a SUCCESS report.

# Cryptoscanner — challenger and independent legacy-inspired WATCH

Paper only · risk is high or higher · 30%+ in 48h probability NOT CALIBRATED
Signal confidence 0–100 means setup strength only, NOT a win probability. Actions are research guidance; no trade authorization.

**Writer:** 45697845195 · **Generation:** 1765 · **Legacy run:** 45697845195
**Main quote time:** 2026-11-25T20:47:19.126842+00:00 · **Legacy report time:** 2026-11-25T20:48:34.057821+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | HYPE/USD | 61.28 | 83.88 | -0.36% | 4.08x | STRONG 72/100 | HIGH 61/100 | Watch |
| 2 | NEAR/USD | 3.0101 | 83.34 | +0.51% | 0.81x | STRONG 72/100 | HIGH 62/100 | Watch |
| 3 | DRV/USD | 0.349 | 78.37 | -0.24% | 1.79x | MODERATE 49/100 | VERY_HIGH 73/100 | Watch |
| 4 | LINK/USD | 9.05493 | 75.15 | -0.36% | 3.63x | MODERATE 68/100 | HIGH 61/100 | Watch |
| 5 | LTC/USD | 42.31 | 74.95 | -0.52% | 0.99x | WEAK 42/100 | HIGH 68/100 | Watch |
| 6 | XPL/USD ⭐ | 0.0476 | 74.64 | +0.21% | 1.17x | STRONG 72/100 | VERY_HIGH 74/100 | Watch |
| 7 | ZEC/USD | 754.79 | 68.59 | -0.27% | 1.12x | WEAK 44/100 | HIGH 68/100 | Watch |
| 8 | XMR/USD | 520.9 | 68.03 | +0.22% | 1.11x | MODERATE 69/100 | HIGH 62/100 | Watch |
| 9 | SUI/USD | 0.6614 | 60.32 | -0.36% | 0.36x | WEAK 35/100 | VERY_HIGH 76/100 | Watch |
| 10 | XLM/USD | 0.127638 | 59.45 | -0.08% | 0.70x | WEAK 35/100 | VERY_HIGH 76/100 | Watch |
| 11 | PAXG/USD | 3567.89 | 57.94 | -0.38% | 1.01x | WEAK 39/100 | HIGH 68/100 | Watch |
| 12 | XRP/USD | 0.93549 | 56.60 | -0.31% | 0.47x | WEAK 33/100 | VERY_HIGH 76/100 | Do nothing |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | XPL/USD ⭐ | 0.0478 | 73.93 | +0.21% | 1.17x | 2418 | MODERATE 67/100 | VERY_HIGH 84/100 | Watch |

**Same-run overlap:** XPL/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
