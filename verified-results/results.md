# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-25T07:57:20.633443+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/45571816515
**Source SHA:** 858c8bc8ec5d7641ddb39cacd8aca91719f855b1
**Previous ledger commit:** afe5573a9ed309af96b39f699708f6f570b2751f (atomic ledger/results publication)
**Ledger generation:** 1690 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 5s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 628; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 610; valid market observations: 609; OHLC screened: 18.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | MON/USD | 0.01051 | 88.671 | 85.144 | +10.98% | +0.77% | 0.97x | 19.0 | 2026-11-25T07:57:16.093011+00:00 | Not calibrated | MODERATE 69/100 | HIGH 68/100 | Watch | WATCH |
| 2 | DRV/USD | 0.33301 | 79.348 | 76.469 | +5.96% | +0.66% | 0.96x | 5.1 | 2026-11-25T07:57:16.093011+00:00 | Not calibrated | STRONG 70/100 | HIGH 62/100 | Watch | WATCH |
| 3 | PROS/USD | 0.7449 | 70.136 | 60.909 | +11.06% | +2.14% | 0.85x | 32.2 | 2026-11-25T07:57:16.093011+00:00 | Not calibrated | MODERATE 55/100 | VERY_HIGH 79/100 | Watch | WATCH |
| 4 | BABY/USD | 0.00887 | 67.826 | 71.630 | +7.38% | +0.91% | 0.17x | 11.3 | 2026-11-25T07:57:16.093011+00:00 | Not calibrated | MODERATE 59/100 | VERY_HIGH 81/100 | Watch | WATCH |
| 5 | PEPE/USD | 3.474e-06 | 53.754 | 47.703 | +0.61% | +0.61% | 1.30x | 2.9 | 2026-11-25T07:57:16.093011+00:00 | Not calibrated | STRONG 72/100 | HIGH 55/100 | Watch | WATCH |
| 6 | XPL/USD | 0.0448 | 38.978 | 36.831 | +1.82% | +0.67% | 0.88x | 22.4 | 2026-11-25T07:57:16.093011+00:00 | Not calibrated | WEAK 39/100 | VERY_HIGH 79/100 | Watch | WATCH |
| 7 | SYRUP/USD | 0.07147 | 37.706 | 40.003 | +2.58% | +0.53% | 0.50x | 19.6 | 2026-11-25T07:57:16.093011+00:00 | Not calibrated | WEAK 44/100 | VERY_HIGH 81/100 | Watch | WATCH |
| 8 | AKT/USD | 0.467 | 27.890 | 33.956 | +0.45% | -0.06% | 0.43x | 2.1 | 2026-11-25T07:57:16.093011+00:00 | Not calibrated | WEAK 19/100 | VERY_HIGH 81/100 | Do nothing | WATCH |
| 9 | CAP/USD | 0.092875 | 27.481 | 32.662 | +0.49% | -0.44% | 0.70x | 6.0 | 2026-11-25T07:57:16.093011+00:00 | Not calibrated | WEAK 19/100 | VERY_HIGH 81/100 | Do nothing | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | MON/USD | 85.144 | 0.01051 | +0.77% | 0.97x |
| 2 | DRV/USD | 76.469 | 0.33301 | +0.66% | 0.96x |
| 3 | BABY/USD | 71.630 | 0.00887 | +0.91% | 0.17x |
| 4 | PROS/USD | 60.909 | 0.7449 | +2.14% | 0.85x |
| 5 | PEPE/USD | 47.703 | 3.474e-06 | +0.61% | 1.30x |
| 6 | SYRUP/USD | 40.003 | 0.07147 | +0.53% | 0.50x |
| 7 | XPL/USD | 36.831 | 0.0448 | +0.67% | 0.88x |
| 8 | AKT/USD | 33.956 | 0.467 | -0.06% | 0.43x |
| 9 | CAP/USD | 32.662 | 0.092875 | -0.44% | 0.70x |

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

- Persisted scans: 1690; predictions: 14348; observations: 1024301.
- Matured sampled outcomes across 1/6/24/48h: 30744; gap abstentions: 22370. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 146 (sampled only; not a success-rate estimate).
- False positives / missed movers: NOT VERIFIED without eligible continuous outcome coverage.
- Baseline vs challenger: recorded as-of; unbiased held-out lift NOT MEASURED.
- Online Kraken /USD stablecoin-base pairs excluded: 18 (counted from this scan's online AssetPairs metadata, not inferred from price).
- Stablecoin base exclusions: BRL1, BUSD, DAI, EUR, EURC, EUROP, EURQ, EURR, EURT, FDUSD, FRAX, GUSD, PYUSD, QCAD, RLUSD, TGBP, TUSD, USD, USD1, USDC, USDD, USDE, USDG, USDQ, USDR, USDS, USDT, ZUSD.
- DEX: NOT USED; no DEX freshness gate.
- OHLC screening abstentions: 9; details in immutable scan JSON artifact.
- Storage: ledger and results published in one non-force Git commit and read back. Independent artifact recovery is NOT VERIFIED by this scan alone.
- Errors: none in successful committed scan; a failed workflow must not publish a SUCCESS report.

# Cryptoscanner — challenger and independent legacy-inspired WATCH

Paper only · risk is high or higher · 30%+ in 48h probability NOT CALIBRATED
Signal confidence 0–100 means setup strength only, NOT a win probability. Actions are research guidance; no trade authorization.

**Writer:** 45571816515 · **Generation:** 1690 · **Legacy run:** 45571816515
**Main quote time:** 2026-11-25T07:57:20.633443+00:00 · **Legacy report time:** 2026-11-25T07:58:14.080982+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | MON/USD | 0.01051 | 88.67 | +0.77% | 0.97x | MODERATE 69/100 | HIGH 68/100 | Watch |
| 2 | DRV/USD | 0.33301 | 79.35 | +0.66% | 0.96x | STRONG 70/100 | HIGH 62/100 | Watch |
| 3 | PROS/USD | 0.7449 | 70.14 | +2.14% | 0.85x | MODERATE 55/100 | VERY_HIGH 79/100 | Watch |
| 4 | BABY/USD | 0.00887 | 67.83 | +0.91% | 0.17x | MODERATE 59/100 | VERY_HIGH 81/100 | Watch |
| 5 | PEPE/USD ⭐ | 3.474e-06 | 53.75 | +0.61% | 1.30x | STRONG 82/100 | HIGH 55/100 | Watch |
| 6 | XPL/USD | 0.0448 | 38.98 | +0.67% | 0.88x | WEAK 39/100 | VERY_HIGH 79/100 | Watch |
| 7 | SYRUP/USD | 0.07147 | 37.71 | +0.53% | 0.50x | WEAK 44/100 | VERY_HIGH 81/100 | Watch |
| 8 | AKT/USD | 0.467 | 27.89 | -0.06% | 0.43x | WEAK 19/100 | VERY_HIGH 81/100 | Do nothing |
| 9 | CAP/USD | 0.092875 | 27.48 | -0.44% | 0.70x | WEAK 19/100 | VERY_HIGH 81/100 | Do nothing |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | PEPE/USD ⭐ | 3.477e-06 | 51.55 | +0.61% | 1.30x | 5747 | STRONG 81/100 | HIGH 55/100 | Watch |
| 2 | TRX/USD | 0.30803 | 51.29 | +0.08% | 11.91x | 3555 | STRONG 71/100 | HIGH 55/100 | Watch |
| 3 | CC/USD | 0.07516 | 38.29 | +0.74% | 7.87x | 5444 | STRONG 74/100 | HIGH 60/100 | Watch |

**Same-run overlap:** PEPE/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
