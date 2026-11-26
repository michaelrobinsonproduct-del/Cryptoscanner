# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-26T23:51:17.080417+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/45913182232
**Source SHA:** 858c8bc8ec5d7641ddb39cacd8aca91719f855b1
**Previous ledger commit:** 2cbe63df2460b84ba1ceffa761edf3df5c38d7a2 (atomic ledger/results publication)
**Ledger generation:** 1930 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 7s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 628; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 610; valid market observations: 601; OHLC screened: 24.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | LTC/USD | 43.83 | 70.813 | 72.215 | +2.62% | +0.11% | 0.80x | 2.3 | 2026-11-26T23:51:10.222351+00:00 | Not calibrated | MODERATE 55/100 | HIGH 62/100 | Watch | WATCH |
| 2 | LINK/USD | 9.26845 | 65.404 | 70.745 | +2.48% | +0.28% | 0.33x | 3.2 | 2026-11-26T23:51:10.222351+00:00 | Not calibrated | MODERATE 63/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 3 | SOL/USD | 70.91 | 56.344 | 59.466 | +0.74% | +0.08% | 0.65x | 1.4 | 2026-11-26T23:51:10.222351+00:00 | Not calibrated | MODERATE 48/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 4 | HYPE/USD | 62.12 | 55.862 | 59.875 | +0.81% | +0.21% | 0.49x | 1.6 | 2026-11-26T23:51:10.222351+00:00 | Not calibrated | MODERATE 58/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 5 | XRP/USD | 0.94237 | 54.947 | 59.289 | +0.62% | +0.11% | 0.51x | 0.1 | 2026-11-26T23:51:10.222351+00:00 | Not calibrated | MODERATE 47/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 6 | XDG/USD | 0.0563467 | 42.529 | 47.573 | +0.69% | +0.08% | 0.46x | 0.0 | 2026-11-26T23:51:10.222351+00:00 | Not calibrated | WEAK 41/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 7 | ONDO/USD | 0.28683 | 37.097 | 42.740 | +1.53% | +0.14% | 0.37x | 0.7 | 2026-11-26T23:51:10.222351+00:00 | Not calibrated | WEAK 39/100 | VERY_HIGH 75/100 | Watch | WATCH |
| 8 | DOT/USD | 0.6708 | 36.948 | 45.047 | +1.90% | +0.24% | 0.07x | 1.5 | 2026-11-26T23:51:10.222351+00:00 | Not calibrated | MODERATE 48/100 | VERY_HIGH 75/100 | Watch | WATCH |
| 9 | SPX/USD | 0.2735 | 26.200 | 27.029 | +0.48% | +0.55% | 0.64x | 14.6 | 2026-11-26T23:51:10.222351+00:00 | Not calibrated | WEAK 38/100 | EXTREME 88/100 | Do nothing | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | LTC/USD | 72.215 | 43.83 | +0.11% | 0.80x |
| 2 | LINK/USD | 70.745 | 9.26845 | +0.28% | 0.33x |
| 3 | HYPE/USD | 59.875 | 62.12 | +0.21% | 0.49x |
| 4 | SOL/USD | 59.466 | 70.91 | +0.08% | 0.65x |
| 5 | XRP/USD | 59.289 | 0.94237 | +0.11% | 0.51x |
| 6 | XDG/USD | 47.573 | 0.0563467 | +0.08% | 0.46x |
| 7 | DOT/USD | 45.047 | 0.6708 | +0.24% | 0.07x |
| 8 | ONDO/USD | 42.740 | 0.28683 | +0.14% | 0.37x |
| 9 | SPX/USD | 27.029 | 0.2735 | +0.55% | 0.64x |

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

- Persisted scans: 1930; predictions: 16887; observations: 1169015.
- Matured sampled outcomes across 1/6/24/48h: 36896; gap abstentions: 25370. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 149 (sampled only; not a success-rate estimate).
- False positives / missed movers: NOT VERIFIED without eligible continuous outcome coverage.
- Baseline vs challenger: recorded as-of; unbiased held-out lift NOT MEASURED.
- Online Kraken /USD stablecoin-base pairs excluded: 18 (counted from this scan's online AssetPairs metadata, not inferred from price).
- Stablecoin base exclusions: BRL1, BUSD, DAI, EUR, EURC, EUROP, EURQ, EURR, EURT, FDUSD, FRAX, GUSD, PYUSD, QCAD, RLUSD, TGBP, TUSD, USD, USD1, USDC, USDD, USDE, USDG, USDQ, USDR, USDS, USDT, ZUSD.
- DEX: NOT USED; no DEX freshness gate.
- OHLC screening abstentions: 15; details in immutable scan JSON artifact.
- Storage: ledger and results published in one non-force Git commit and read back. Independent artifact recovery is NOT VERIFIED by this scan alone.
- Errors: none in successful committed scan; a failed workflow must not publish a SUCCESS report.

# Cryptoscanner — challenger and independent legacy-inspired WATCH

Paper only · risk is high or higher · 30%+ in 48h probability NOT CALIBRATED
Signal confidence 0–100 means setup strength only, NOT a win probability. Actions are research guidance; no trade authorization.

**Writer:** 45913182232 · **Generation:** 1930 · **Legacy run:** 45913182232
**Main quote time:** 2026-11-26T23:51:17.080417+00:00 · **Legacy report time:** 2026-11-26T23:52:08.411343+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | LTC/USD | 43.83 | 70.81 | +0.11% | 0.80x | MODERATE 55/100 | HIGH 62/100 | Watch |
| 2 | LINK/USD | 9.26845 | 65.40 | +0.28% | 0.33x | MODERATE 63/100 | VERY_HIGH 70/100 | Watch |
| 3 | SOL/USD | 70.91 | 56.34 | +0.08% | 0.65x | MODERATE 48/100 | VERY_HIGH 70/100 | Watch |
| 4 | HYPE/USD | 62.12 | 55.86 | +0.21% | 0.49x | MODERATE 58/100 | VERY_HIGH 70/100 | Watch |
| 5 | XRP/USD | 0.94237 | 54.95 | +0.11% | 0.51x | MODERATE 47/100 | VERY_HIGH 70/100 | Watch |
| 6 | XDG/USD | 0.0563467 | 42.53 | +0.08% | 0.46x | WEAK 41/100 | VERY_HIGH 70/100 | Watch |
| 7 | ONDO/USD | 0.28683 | 37.10 | +0.14% | 0.37x | WEAK 39/100 | VERY_HIGH 75/100 | Watch |
| 8 | DOT/USD | 0.6708 | 36.95 | +0.24% | 0.07x | MODERATE 48/100 | VERY_HIGH 75/100 | Watch |
| 9 | SPX/USD | 0.2735 | 26.20 | +0.55% | 0.64x | WEAK 38/100 | EXTREME 88/100 | Do nothing |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | INJ/USD | 6.184 | 78.39 | +0.24% | 1.55x | 5199 | STRONG 84/100 | HIGH 55/100 | Consider small entry |

**Same-run overlap:** None
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
