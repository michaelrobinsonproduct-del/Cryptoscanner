# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-27T16:12:27.259379+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/46031189073
**Source SHA:** 858c8bc8ec5d7641ddb39cacd8aca91719f855b1
**Previous ledger commit:** 81bdbbfefed4a5ce9a68aa1f4975f3f82057e9d1 (atomic ledger/results publication)
**Ledger generation:** 2030 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 7s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 628; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 610; valid market observations: 605; OHLC screened: 24.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | ZEC/USD | 738.96 | 90.819 | 97.429 | +8.41% | +0.07% | 0.30x | 5.1 | 2026-11-27T16:12:20.342381+00:00 | Not calibrated | MODERATE 65/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 2 | HYPE/USD | 64.3 | 72.269 | 76.846 | +3.34% | +0.36% | 0.36x | 3.1 | 2026-11-27T16:12:20.342381+00:00 | Not calibrated | MODERATE 66/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 3 | UNI/USD | 4.7808 | 69.431 | 71.743 | +2.81% | +0.99% | 0.27x | 2.9 | 2026-11-27T16:12:20.342381+00:00 | Not calibrated | MODERATE 65/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 4 | VVV/USD | 26.925 | 64.468 | 65.590 | +2.83% | +0.40% | 0.69x | 10.8 | 2026-11-27T16:12:20.342381+00:00 | Not calibrated | MODERATE 57/100 | VERY_HIGH 76/100 | Watch | WATCH |
| 5 | SPACE/USD | 0.004129 | 63.509 | 69.634 | +6.64% | -1.06% | 0.92x | 12.1 | 2026-11-27T16:12:20.342381+00:00 | Not calibrated | WEAK 32/100 | EXTREME 90/100 | Do nothing | WATCH |
| 6 | SOL/USD | 72.23 | 61.625 | 67.037 | +1.82% | +0.42% | 0.25x | 1.4 | 2026-11-27T16:12:20.342381+00:00 | Not calibrated | MODERATE 61/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 7 | XDG/USD | 0.0575997 | 60.470 | 68.332 | +2.17% | -0.06% | 0.24x | 3.8 | 2026-11-27T16:12:20.342381+00:00 | Not calibrated | WEAK 35/100 | VERY_HIGH 76/100 | Watch | WATCH |
| 8 | W/USD | 0.0092 | 57.989 | 59.398 | +4.43% | +0.66% | 0.53x | 10.8 | 2026-11-27T16:12:20.342381+00:00 | Not calibrated | MODERATE 54/100 | VERY_HIGH 81/100 | Watch | WATCH |
| 9 | SUI/USD | 0.6713 | 54.751 | 56.539 | +0.54% | +0.48% | 0.58x | 4.5 | 2026-11-27T16:12:20.342381+00:00 | Not calibrated | MODERATE 57/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 10 | XRP/USD | 0.95015 | 54.073 | 60.126 | +0.78% | -0.11% | 0.45x | 0.7 | 2026-11-27T16:12:20.342381+00:00 | Not calibrated | WEAK 32/100 | VERY_HIGH 76/100 | Do nothing | WATCH |
| 11 | ADA/USD | 0.149011 | 49.959 | 54.726 | +0.37% | +0.22% | 0.41x | 4.6 | 2026-11-27T16:12:20.342381+00:00 | Not calibrated | MODERATE 55/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 12 | XLM/USD | 0.127182 | 46.021 | 47.880 | +0.45% | +0.18% | 0.72x | 0.1 | 2026-11-27T16:12:20.342381+00:00 | Not calibrated | WEAK 43/100 | VERY_HIGH 70/100 | Watch | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | ZEC/USD | 97.429 | 738.96 | +0.07% | 0.30x |
| 2 | HYPE/USD | 76.846 | 64.3 | +0.36% | 0.36x |
| 3 | UNI/USD | 71.743 | 4.7808 | +0.99% | 0.27x |
| 4 | SPACE/USD | 69.634 | 0.004129 | -1.06% | 0.92x |
| 5 | XDG/USD | 68.332 | 0.0575997 | -0.06% | 0.24x |
| 6 | SOL/USD | 67.037 | 72.23 | +0.42% | 0.25x |
| 7 | VVV/USD | 65.590 | 26.925 | +0.40% | 0.69x |
| 8 | XRP/USD | 60.126 | 0.95015 | -0.11% | 0.45x |
| 9 | W/USD | 59.398 | 0.0092 | +0.66% | 0.53x |
| 10 | SUI/USD | 56.539 | 0.6713 | +0.48% | 0.58x |
| 11 | ADA/USD | 54.726 | 0.149011 | +0.22% | 0.41x |
| 12 | XLM/USD | 47.880 | 0.127182 | +0.18% | 0.72x |

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

- Persisted scans: 2030; predictions: 18062; observations: 1229259.
- Matured sampled outcomes across 1/6/24/48h: 40409; gap abstentions: 25957. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 150 (sampled only; not a success-rate estimate).
- False positives / missed movers: NOT VERIFIED without eligible continuous outcome coverage.
- Baseline vs challenger: recorded as-of; unbiased held-out lift NOT MEASURED.
- Online Kraken /USD stablecoin-base pairs excluded: 18 (counted from this scan's online AssetPairs metadata, not inferred from price).
- Stablecoin base exclusions: BRL1, BUSD, DAI, EUR, EURC, EUROP, EURQ, EURR, EURT, FDUSD, FRAX, GUSD, PYUSD, QCAD, RLUSD, TGBP, TUSD, USD, USD1, USDC, USDD, USDE, USDG, USDQ, USDR, USDS, USDT, ZUSD.
- DEX: NOT USED; no DEX freshness gate.
- OHLC screening abstentions: 3; details in immutable scan JSON artifact.
- Storage: ledger and results published in one non-force Git commit and read back. Independent artifact recovery is NOT VERIFIED by this scan alone.
- Errors: none in successful committed scan; a failed workflow must not publish a SUCCESS report.

# Cryptoscanner — challenger and independent legacy-inspired WATCH

Paper only · risk is high or higher · 30%+ in 48h probability NOT CALIBRATED
Signal confidence 0–100 means setup strength only, NOT a win probability. Actions are research guidance; no trade authorization.

**Writer:** 46031189073 · **Generation:** 2030 · **Legacy run:** 46031189073
**Main quote time:** 2026-11-27T16:12:27.259379+00:00 · **Legacy report time:** 2026-11-27T16:13:20.613653+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | ZEC/USD | 738.96 | 90.82 | +0.07% | 0.30x | MODERATE 65/100 | VERY_HIGH 70/100 | Watch |
| 2 | HYPE/USD | 64.3 | 72.27 | +0.36% | 0.36x | MODERATE 66/100 | VERY_HIGH 70/100 | Watch |
| 3 | UNI/USD | 4.7808 | 69.43 | +0.99% | 0.27x | MODERATE 65/100 | VERY_HIGH 70/100 | Watch |
| 4 | VVV/USD | 26.925 | 64.47 | +0.40% | 0.69x | MODERATE 57/100 | VERY_HIGH 76/100 | Watch |
| 5 | SPACE/USD | 0.004129 | 63.51 | -1.06% | 0.92x | WEAK 32/100 | EXTREME 90/100 | Do nothing |
| 6 | SOL/USD | 72.23 | 61.63 | +0.42% | 0.25x | MODERATE 61/100 | VERY_HIGH 70/100 | Watch |
| 7 | XDG/USD | 0.0575997 | 60.47 | -0.06% | 0.24x | WEAK 35/100 | VERY_HIGH 76/100 | Watch |
| 8 | W/USD | 0.0092 | 57.99 | +0.66% | 0.53x | MODERATE 54/100 | VERY_HIGH 81/100 | Watch |
| 9 | SUI/USD | 0.6713 | 54.75 | +0.48% | 0.58x | MODERATE 57/100 | VERY_HIGH 70/100 | Watch |
| 10 | XRP/USD | 0.95015 | 54.07 | -0.11% | 0.45x | WEAK 32/100 | VERY_HIGH 76/100 | Do nothing |
| 11 | ADA/USD | 0.149011 | 49.96 | +0.22% | 0.41x | MODERATE 55/100 | VERY_HIGH 70/100 | Watch |
| 12 | XLM/USD | 0.127182 | 46.02 | +0.18% | 0.72x | WEAK 43/100 | VERY_HIGH 70/100 | Watch |

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
