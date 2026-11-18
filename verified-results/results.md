# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-18T21:30:11.047511+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/44402017764
**Source SHA:** b271b90a2cae9e5307600070ce7d0e510fe68996
**Previous ledger commit:** 6ae2195ae421a55b0ab0e976e36484fdad494737 (atomic ledger/results publication)
**Ledger generation:** 672 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 5s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 627; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 609; valid market observations: 609; OHLC screened: 12.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | SENT/USD | 0.020125 | 77.115 | 75.678 | +7.80% | +0.51% | 0.89x | 1.0 | 2026-11-18T21:30:06.532788+00:00 | Not calibrated | MODERATE 69/100 | VERY_HIGH 74/100 | Watch | WATCH |
| 2 | VVV/USD | 21.171 | 50.651 | 49.144 | +0.69% | +0.44% | 0.93x | 7.5 | 2026-11-18T21:30:06.532788+00:00 | Not calibrated | MODERATE 55/100 | HIGH 62/100 | Watch | WATCH |
| 3 | TRX/USD | 0.30875 | 41.217 | 41.514 | +0.28% | +0.11% | 0.91x | 0.9 | 2026-11-18T21:30:06.532788+00:00 | Not calibrated | WEAK 41/100 | HIGH 62/100 | Watch | WATCH |
| 4 | AKT/USD | 0.5113 | 32.855 | 30.598 | +0.39% | +0.39% | 1.03x | 7.8 | 2026-11-18T21:30:06.532788+00:00 | Not calibrated | MODERATE 51/100 | HIGH 67/100 | Watch | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | SENT/USD | 75.678 | 0.020125 | +0.51% | 0.89x |
| 2 | VVV/USD | 49.144 | 21.171 | +0.44% | 0.93x |
| 3 | TRX/USD | 41.514 | 0.30875 | +0.11% | 0.91x |
| 4 | AKT/USD | 30.598 | 0.5113 | +0.39% | 1.03x |

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

- Persisted scans: 672; predictions: 5538; observations: 406255.
- Matured sampled outcomes across 1/6/24/48h: 5175; gap abstentions: 13146. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 10 (sampled only; not a success-rate estimate).
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

**Writer:** 44402017764 · **Generation:** 672 · **Legacy run:** 44402017764
**Main quote time:** 2026-11-18T21:30:11.047511+00:00 · **Legacy report time:** 2026-11-18T21:30:44.426711+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | SENT/USD | 0.020125 | 77.12 | +0.51% | 0.89x | MODERATE 69/100 | VERY_HIGH 74/100 | Watch |
| 2 | VVV/USD | 21.171 | 50.65 | +0.44% | 0.93x | MODERATE 55/100 | HIGH 62/100 | Watch |
| 3 | TRX/USD | 0.30875 | 41.22 | +0.11% | 0.91x | WEAK 41/100 | HIGH 62/100 | Watch |
| 4 | AKT/USD ⭐ | 0.5113 | 32.85 | +0.39% | 1.03x | MODERATE 61/100 | HIGH 67/100 | Watch |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | AKT/USD ⭐ | 0.5117 | 30.00 | +0.39% | 1.03x | 4295 | MODERATE 55/100 | VERY_HIGH 73/100 | Watch |

**Same-run overlap:** AKT/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
