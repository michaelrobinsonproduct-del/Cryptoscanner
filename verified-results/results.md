# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-18T05:50:04.417551+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/44246924061
**Source SHA:** 394c17eeb7071fba40e02dbbb1ea97cedb3a0a8a
**Previous ledger commit:** 378a51af9cb7815e65d230c2e6695ca709926bf9 (atomic ledger/results publication)
**Ledger generation:** 547 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 5s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 627; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 609; valid market observations: 609; OHLC screened: 18.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | SENT/USD | 0.019754 | 71.279 | 67.627 | +5.81% | +1.70% | 0.51x | 8.1 | 2026-11-18T05:49:59.216578+00:00 | Not calibrated | MODERATE 66/100 | VERY_HIGH 82/100 | Watch | WATCH |
| 2 | VVV/USD | 21.176 | 64.708 | 49.212 | +0.71% | +0.10% | 16.27x | 8.5 | 2026-11-18T05:49:59.216578+00:00 | Not calibrated | STRONG 77/100 | HIGH 55/100 | Watch | WATCH |
| 3 | CT/USD | 0.1156 | 52.561 | 38.424 | +2.30% | -0.17% | 3.87x | 17.3 | 2026-11-18T05:49:59.216578+00:00 | Not calibrated | MODERATE 51/100 | VERY_HIGH 79/100 | Watch | WATCH |
| 4 | CC/USD | 0.08452 | 50.558 | 54.764 | +2.91% | +0.51% | 0.32x | 2.4 | 2026-11-18T05:49:59.216578+00:00 | Not calibrated | MODERATE 55/100 | VERY_HIGH 75/100 | Watch | WATCH |
| 5 | XDC/USD | 0.0309 | 48.625 | 49.750 | +1.91% | +0.06% | 0.86x | 3.2 | 2026-11-18T05:49:59.216578+00:00 | Not calibrated | WEAK 44/100 | HIGH 62/100 | Watch | WATCH |
| 6 | UP/USD | 0.05503 | 46.569 | 52.909 | +3.85% | -0.51% | 0.62x | 12.7 | 2026-11-18T05:49:59.216578+00:00 | Not calibrated | WEAK 23/100 | EXTREME 87/100 | Do nothing | WATCH |
| 7 | MNT/USD | 0.3772 | 34.797 | 37.514 | +1.04% | +0.03% | 0.71x | 5.3 | 2026-11-18T05:49:59.216578+00:00 | Not calibrated | WEAK 37/100 | VERY_HIGH 75/100 | Watch | WATCH |
| 8 | PEARL/USD | 1.8468 | 33.796 | 41.473 | +2.00% | +0.16% | 0.15x | 14.6 | 2026-11-18T05:49:59.216578+00:00 | Not calibrated | WEAK 32/100 | VERY_HIGH 81/100 | Do nothing | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | SENT/USD | 67.627 | 0.019754 | +1.70% | 0.51x |
| 2 | CC/USD | 54.764 | 0.08452 | +0.51% | 0.32x |
| 3 | UP/USD | 52.909 | 0.05503 | -0.51% | 0.62x |
| 4 | XDC/USD | 49.750 | 0.0309 | +0.06% | 0.86x |
| 5 | VVV/USD | 49.212 | 21.176 | +0.10% | 16.27x |
| 6 | PEARL/USD | 41.473 | 1.8468 | +0.16% | 0.15x |
| 7 | CT/USD | 38.424 | 0.1156 | -0.17% | 3.87x |
| 8 | MNT/USD | 37.514 | 0.3772 | +0.03% | 0.71x |

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

- Persisted scans: 547; predictions: 4620; observations: 330130.
- Matured sampled outcomes across 1/6/24/48h: 3799; gap abstentions: 12463. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 0 (sampled only; not a success-rate estimate).
- False positives / missed movers: NOT VERIFIED without eligible continuous outcome coverage.
- Baseline vs challenger: recorded as-of; unbiased held-out lift NOT MEASURED.
- Online Kraken /USD stablecoin-base pairs excluded: 18 (counted from this scan's online AssetPairs metadata, not inferred from price).
- Stablecoin base exclusions: BRL1, BUSD, DAI, EUR, EURC, EUROP, EURQ, EURR, EURT, FDUSD, FRAX, GUSD, PYUSD, QCAD, RLUSD, TGBP, TUSD, USD, USD1, USDC, USDD, USDE, USDG, USDQ, USDR, USDS, USDT, ZUSD.
- DEX: NOT USED; no DEX freshness gate.
- OHLC screening abstentions: 10; details in immutable scan JSON artifact.
- Storage: ledger and results published in one non-force Git commit and read back. Independent artifact recovery is NOT VERIFIED by this scan alone.
- Errors: none in successful committed scan; a failed workflow must not publish a SUCCESS report.

# Cryptoscanner — challenger and independent legacy-inspired WATCH

Paper only · risk is high or higher · 30%+ in 48h probability NOT CALIBRATED
Signal confidence 0–100 means setup strength only, NOT a win probability. Actions are research guidance; no trade authorization.

**Writer:** 44246924061 · **Generation:** 547 · **Legacy run:** 44246924061
**Main quote time:** 2026-11-18T05:50:04.417551+00:00 · **Legacy report time:** 2026-11-18T05:50:21.893307+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | SENT/USD | 0.019754 | 71.28 | +1.70% | 0.51x | MODERATE 66/100 | VERY_HIGH 82/100 | Watch |
| 2 | VVV/USD ⭐ | 21.176 | 64.71 | +0.10% | 16.27x | STRONG 87/100 | HIGH 55/100 | Watch |
| 3 | CT/USD | 0.1156 | 52.56 | -0.17% | 3.87x | MODERATE 51/100 | VERY_HIGH 79/100 | Watch |
| 4 | CC/USD | 0.08452 | 50.56 | +0.51% | 0.32x | MODERATE 55/100 | VERY_HIGH 75/100 | Watch |
| 5 | XDC/USD | 0.0309 | 48.63 | +0.06% | 0.86x | WEAK 44/100 | HIGH 62/100 | Watch |
| 6 | UP/USD | 0.05503 | 46.57 | -0.51% | 0.62x | WEAK 23/100 | EXTREME 87/100 | Do nothing |
| 7 | MNT/USD | 0.3772 | 34.80 | +0.03% | 0.71x | WEAK 37/100 | VERY_HIGH 75/100 | Watch |
| 8 | PEARL/USD | 1.8468 | 33.80 | +0.16% | 0.15x | WEAK 32/100 | VERY_HIGH 81/100 | Do nothing |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | VVV/USD ⭐ | 21.176 | 51.70 | +0.10% | 16.27x | 7307 | STRONG 81/100 | HIGH 55/100 | Watch |

**Same-run overlap:** VVV/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
