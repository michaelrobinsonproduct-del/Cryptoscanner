# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-27T12:21:56.590446+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/45997682950
**Source SHA:** 858c8bc8ec5d7641ddb39cacd8aca91719f855b1
**Previous ledger commit:** 42eb93176a31375d9ca1ec251c7adcd8a1501cce (atomic ledger/results publication)
**Ledger generation:** 2007 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 6s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 628; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 610; valid market observations: 603; OHLC screened: 24.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | HYPE/USD | 65.82 | 96.432 | 94.742 | +5.79% | -0.02% | 1.18x | 1.5 | 2026-11-27T12:21:50.725163+00:00 | Not calibrated | MODERATE 58/100 | HIGH 68/100 | Watch | WATCH |
| 2 | ZEC/USD | 759.93 | 95.776 | 99.934 | +11.48% | +0.51% | 0.33x | 0.1 | 2026-11-27T12:21:50.725163+00:00 | Not calibrated | STRONG 78/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 3 | INJ/USD | 6.496 | 87.463 | 72.386 | +4.91% | +0.02% | 2.54x | 3.1 | 2026-11-27T12:21:50.725163+00:00 | Not calibrated | STRONG 89/100 | HIGH 55/100 | Watch | WATCH |
| 4 | SOL/USD | 73.12 | 81.223 | 75.827 | +3.07% | -0.05% | 1.57x | 1.4 | 2026-11-27T12:21:50.725163+00:00 | Not calibrated | MODERATE 61/100 | HIGH 61/100 | Watch | WATCH |
| 5 | UNI/USD | 4.8838 | 80.108 | 77.008 | +5.03% | -0.29% | 1.45x | 6.1 | 2026-11-27T12:21:50.725163+00:00 | Not calibrated | MODERATE 60/100 | HIGH 61/100 | Watch | WATCH |
| 6 | PAXG/USD | 3656.6 | 75.523 | 60.597 | +2.81% | -0.01% | 8.09x | 1.4 | 2026-11-27T12:21:50.725163+00:00 | Not calibrated | MODERATE 68/100 | HIGH 61/100 | Watch | WATCH |
| 7 | XRP/USD | 0.97397 | 75.508 | 77.719 | +3.31% | -0.02% | 0.79x | 0.9 | 2026-11-27T12:21:50.725163+00:00 | Not calibrated | WEAK 43/100 | HIGH 68/100 | Watch | WATCH |
| 8 | ENA/USD | 0.1078 | 74.762 | 77.511 | +7.37% | -0.55% | 1.00x | 9.3 | 2026-11-27T12:21:50.725163+00:00 | Not calibrated | MODERATE 47/100 | HIGH 68/100 | Watch | WATCH |
| 9 | XDG/USD | 0.0588165 | 73.000 | 77.304 | +4.33% | -0.02% | 0.58x | 0.0 | 2026-11-27T12:21:50.725163+00:00 | Not calibrated | WEAK 41/100 | VERY_HIGH 76/100 | Watch | WATCH |
| 10 | SUI/USD | 0.6885 | 71.703 | 76.080 | +3.12% | +0.16% | 0.48x | 1.5 | 2026-11-27T12:21:50.725163+00:00 | Not calibrated | MODERATE 56/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 11 | LIGHTER/USD | 2.71 | 71.372 | 73.999 | +9.19% | +0.26% | 0.61x | 7.4 | 2026-11-27T12:21:50.725163+00:00 | Not calibrated | MODERATE 66/100 | VERY_HIGH 75/100 | Watch | WATCH |
| 12 | VVV/USD | 27.108 | 69.469 | 73.608 | +3.53% | +0.33% | 0.42x | 6.6 | 2026-11-27T12:21:50.725163+00:00 | Not calibrated | MODERATE 65/100 | VERY_HIGH 70/100 | Watch | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | ZEC/USD | 99.934 | 759.93 | +0.51% | 0.33x |
| 2 | HYPE/USD | 94.742 | 65.82 | -0.02% | 1.18x |
| 3 | XRP/USD | 77.719 | 0.97397 | -0.02% | 0.79x |
| 4 | ENA/USD | 77.511 | 0.1078 | -0.55% | 1.00x |
| 5 | XDG/USD | 77.304 | 0.0588165 | -0.02% | 0.58x |
| 6 | UNI/USD | 77.008 | 4.8838 | -0.29% | 1.45x |
| 7 | SUI/USD | 76.080 | 0.6885 | +0.16% | 0.48x |
| 8 | SOL/USD | 75.827 | 73.12 | -0.05% | 1.57x |
| 9 | LIGHTER/USD | 73.999 | 2.71 | +0.26% | 0.61x |
| 10 | VVV/USD | 73.608 | 27.108 | +0.33% | 0.42x |
| 11 | INJ/USD | 72.386 | 6.496 | +0.02% | 2.54x |
| 12 | PAXG/USD | 60.597 | 3656.6 | -0.01% | 8.09x |

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

- Persisted scans: 2007; predictions: 17786; observations: 1215370.
- Matured sampled outcomes across 1/6/24/48h: 39569; gap abstentions: 25827. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 150 (sampled only; not a success-rate estimate).
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

**Writer:** 45997682950 · **Generation:** 2007 · **Legacy run:** 45997682950
**Main quote time:** 2026-11-27T12:21:56.590446+00:00 · **Legacy report time:** 2026-11-27T12:22:34.690500+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | HYPE/USD | 65.82 | 96.43 | -0.02% | 1.18x | MODERATE 58/100 | HIGH 68/100 | Watch |
| 2 | ZEC/USD | 759.93 | 95.78 | +0.51% | 0.33x | STRONG 78/100 | VERY_HIGH 70/100 | Watch |
| 3 | INJ/USD | 6.496 | 87.46 | +0.02% | 2.54x | STRONG 89/100 | HIGH 55/100 | Watch |
| 4 | SOL/USD | 73.12 | 81.22 | -0.05% | 1.57x | MODERATE 61/100 | HIGH 61/100 | Watch |
| 5 | UNI/USD | 4.8838 | 80.11 | -0.29% | 1.45x | MODERATE 60/100 | HIGH 61/100 | Watch |
| 6 | PAXG/USD | 3656.6 | 75.52 | -0.01% | 8.09x | MODERATE 68/100 | HIGH 61/100 | Watch |
| 7 | XRP/USD | 0.97397 | 75.51 | -0.02% | 0.79x | WEAK 43/100 | HIGH 68/100 | Watch |
| 8 | ENA/USD | 0.1078 | 74.76 | -0.55% | 1.00x | MODERATE 47/100 | HIGH 68/100 | Watch |
| 9 | XDG/USD | 0.0588165 | 73.00 | -0.02% | 0.58x | WEAK 41/100 | VERY_HIGH 76/100 | Watch |
| 10 | SUI/USD | 0.6885 | 71.70 | +0.16% | 0.48x | MODERATE 56/100 | VERY_HIGH 70/100 | Watch |
| 11 | LIGHTER/USD | 2.71 | 71.37 | +0.26% | 0.61x | MODERATE 66/100 | VERY_HIGH 75/100 | Watch |
| 12 | VVV/USD | 27.108 | 69.47 | +0.33% | 0.42x | MODERATE 65/100 | VERY_HIGH 70/100 | Watch |

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
