# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-23T17:31:51.308088+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/45228241462
**Source SHA:** 858c8bc8ec5d7641ddb39cacd8aca91719f855b1
**Previous ledger commit:** 22cc20fa5a7d7b0eca5039cec4b8e6d41c8f24cd (atomic ledger/results publication)
**Ledger generation:** 1460 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 9s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 628; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 610; valid market observations: 609; OHLC screened: 24.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | SUI/USD | 0.6943 | 85.302 | 94.049 | +5.89% | -1.04% | 0.64x | 4.3 | 2026-11-23T17:31:42.451985+00:00 | Not calibrated | MODERATE 48/100 | VERY_HIGH 80/100 | Watch | WATCH |
| 2 | INJ/USD | 6.692 | 84.637 | 95.564 | +7.45% | -1.40% | 0.61x | 4.5 | 2026-11-23T17:31:42.451985+00:00 | Not calibrated | MODERATE 47/100 | VERY_HIGH 80/100 | Do nothing | WATCH |
| 3 | LTC/USD | 42.1 | 84.016 | 86.439 | +4.83% | -0.68% | 1.10x | 4.8 | 2026-11-23T17:31:42.451985+00:00 | Not calibrated | MODERATE 52/100 | HIGH 68/100 | Watch | WATCH |
| 4 | SOL/USD | 73.97 | 81.993 | 86.749 | +4.73% | -0.83% | 0.94x | 2.7 | 2026-11-23T17:31:42.451985+00:00 | Not calibrated | MODERATE 46/100 | HIGH 68/100 | Watch | WATCH |
| 5 | ADA/USD | 0.150891 | 80.011 | 82.326 | +4.35% | -1.11% | 1.32x | 6.2 | 2026-11-23T17:31:42.451985+00:00 | Not calibrated | MODERATE 60/100 | HIGH 65/100 | Watch | WATCH |
| 6 | HYPE/USD | 65.81 | 79.192 | 84.007 | +4.36% | -0.30% | 0.67x | 3.0 | 2026-11-23T17:31:42.451985+00:00 | Not calibrated | MODERATE 45/100 | VERY_HIGH 76/100 | Watch | WATCH |
| 7 | UNI/USD | 5.0035 | 78.735 | 91.426 | +6.88% | -0.69% | 0.08x | 9.0 | 2026-11-23T17:31:42.451985+00:00 | Not calibrated | WEAK 44/100 | VERY_HIGH 76/100 | Watch | WATCH |
| 8 | CC/USD | 0.07825 | 73.119 | 79.600 | +6.80% | -0.87% | 0.79x | 3.8 | 2026-11-23T17:31:42.451985+00:00 | Not calibrated | WEAK 42/100 | VERY_HIGH 73/100 | Watch | WATCH |
| 9 | XRP/USD | 0.965 | 72.492 | 82.287 | +4.04% | -0.63% | 0.33x | 2.0 | 2026-11-23T17:31:42.451985+00:00 | Not calibrated | WEAK 41/100 | VERY_HIGH 76/100 | Watch | WATCH |
| 10 | XDG/USD | 0.057712 | 71.966 | 82.334 | +4.39% | -0.95% | 0.44x | 6.8 | 2026-11-23T17:31:42.451985+00:00 | Not calibrated | WEAK 41/100 | VERY_HIGH 76/100 | Watch | WATCH |
| 11 | ZEC/USD | 830.14 | 71.428 | 80.208 | +4.09% | -1.07% | 0.66x | 6.9 | 2026-11-23T17:31:42.451985+00:00 | Not calibrated | WEAK 41/100 | VERY_HIGH 80/100 | Watch | WATCH |
| 12 | HBAR/USD | 0.05436 | 70.692 | 74.142 | +5.35% | -0.62% | 0.97x | 1.8 | 2026-11-23T17:31:42.451985+00:00 | Not calibrated | WEAK 40/100 | HIGH 68/100 | Watch | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | INJ/USD | 95.564 | 6.692 | -1.40% | 0.61x |
| 2 | SUI/USD | 94.049 | 0.6943 | -1.04% | 0.64x |
| 3 | UNI/USD | 91.426 | 5.0035 | -0.69% | 0.08x |
| 4 | SOL/USD | 86.749 | 73.97 | -0.83% | 0.94x |
| 5 | LTC/USD | 86.439 | 42.1 | -0.68% | 1.10x |
| 6 | HYPE/USD | 84.007 | 65.81 | -0.30% | 0.67x |
| 7 | XDG/USD | 82.334 | 0.057712 | -0.95% | 0.44x |
| 8 | ADA/USD | 82.326 | 0.150891 | -1.11% | 1.32x |
| 9 | XRP/USD | 82.287 | 0.965 | -0.63% | 0.33x |
| 10 | ZEC/USD | 80.208 | 830.14 | -1.07% | 0.66x |
| 11 | CC/USD | 79.600 | 0.07825 | -0.87% | 0.79x |
| 12 | HBAR/USD | 74.142 | 0.05436 | -0.62% | 0.97x |

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

- Persisted scans: 1460; predictions: 12287; observations: 884242.
- Matured sampled outcomes across 1/6/24/48h: 21412; gap abstentions: 22370. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 131 (sampled only; not a success-rate estimate).
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

**Writer:** 45228241462 · **Generation:** 1460 · **Legacy run:** 45228241462
**Main quote time:** 2026-11-23T17:31:51.308088+00:00 · **Legacy report time:** 2026-11-23T17:32:59.653863+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | SUI/USD | 0.6943 | 85.30 | -1.04% | 0.64x | MODERATE 48/100 | VERY_HIGH 80/100 | Watch |
| 2 | INJ/USD | 6.692 | 84.64 | -1.40% | 0.61x | MODERATE 47/100 | VERY_HIGH 80/100 | Do nothing |
| 3 | LTC/USD | 42.1 | 84.02 | -0.68% | 1.10x | MODERATE 52/100 | HIGH 68/100 | Watch |
| 4 | SOL/USD | 73.97 | 81.99 | -0.83% | 0.94x | MODERATE 46/100 | HIGH 68/100 | Watch |
| 5 | ADA/USD | 0.150891 | 80.01 | -1.11% | 1.32x | MODERATE 60/100 | HIGH 65/100 | Watch |
| 6 | HYPE/USD | 65.81 | 79.19 | -0.30% | 0.67x | MODERATE 45/100 | VERY_HIGH 76/100 | Watch |
| 7 | UNI/USD | 5.0035 | 78.73 | -0.69% | 0.08x | WEAK 44/100 | VERY_HIGH 76/100 | Watch |
| 8 | CC/USD | 0.07825 | 73.12 | -0.87% | 0.79x | WEAK 42/100 | VERY_HIGH 73/100 | Watch |
| 9 | XRP/USD | 0.965 | 72.49 | -0.63% | 0.33x | WEAK 41/100 | VERY_HIGH 76/100 | Watch |
| 10 | XDG/USD | 0.057712 | 71.97 | -0.95% | 0.44x | WEAK 41/100 | VERY_HIGH 76/100 | Watch |
| 11 | ZEC/USD | 830.14 | 71.43 | -1.07% | 0.66x | WEAK 41/100 | VERY_HIGH 80/100 | Watch |
| 12 | HBAR/USD | 0.05436 | 70.69 | -0.62% | 0.97x | WEAK 40/100 | HIGH 68/100 | Watch |

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
