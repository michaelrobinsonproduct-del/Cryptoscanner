# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-16T11:02:29.959070+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/43854116054
**Source SHA:** 885b4a0465f5c74a8a87db5ca921c3c0a00021af
**Previous ledger commit:** 164a3399abb07ef284c96b3fa75adc6c70a9870a (atomic ledger/results publication)
**Ledger generation:** 447 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 5s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 625; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 607; valid market observations: 607; OHLC screened: 15.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | XMR/USD | 508.09 | 76.793 | 61.200 | +1.97% | +0.12% | 4.51x | 15.2 | 2026-11-16T11:02:24.529365+00:00 | Not calibrated | STRONG 78/100 | HIGH 61/100 | Watch | WATCH |
| 2 | SKR/USD | 0.010419 | 69.349 | 64.644 | +10.39% | +0.83% | 1.05x | 29.8 | 2026-11-16T11:02:24.529365+00:00 | Not calibrated | MODERATE 60/100 | VERY_HIGH 79/100 | Watch | WATCH |
| 3 | SENT/USD | 0.017571 | 62.033 | 56.525 | +4.28% | +0.35% | 1.37x | 8.5 | 2026-11-16T11:02:24.529365+00:00 | Not calibrated | STRONG 76/100 | HIGH 67/100 | Watch | WATCH |
| 4 | XDC/USD | 0.0297 | 61.853 | 57.438 | +3.88% | +1.26% | 0.81x | 10.1 | 2026-11-16T11:02:24.529365+00:00 | Not calibrated | MODERATE 56/100 | VERY_HIGH 73/100 | Watch | WATCH |
| 5 | AKT/USD | 0.4971 | 43.205 | 32.550 | +0.77% | +0.18% | 1.97x | 10.1 | 2026-11-16T11:02:24.529365+00:00 | Not calibrated | MODERATE 52/100 | HIGH 66/100 | Watch | WATCH |
| 6 | BEAM/USD | 0.004198 | 20.547 | 26.804 | +2.39% | -0.14% | 0.45x | 42.8 | 2026-11-16T11:02:24.529365+00:00 | Not calibrated | WEAK 0/100 | EXTREME 100/100 | Do nothing | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | SKR/USD | 64.644 | 0.010419 | +0.83% | 1.05x |
| 2 | XMR/USD | 61.200 | 508.09 | +0.12% | 4.51x |
| 3 | XDC/USD | 57.438 | 0.0297 | +1.26% | 0.81x |
| 4 | SENT/USD | 56.525 | 0.017571 | +0.35% | 1.37x |
| 5 | AKT/USD | 32.550 | 0.4971 | +0.18% | 1.97x |
| 6 | BEAM/USD | 26.804 | 0.004198 | -0.14% | 0.45x |

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

- Persisted scans: 447; predictions: 3858; observations: 269244.
- Matured sampled outcomes across 1/6/24/48h: 3195; gap abstentions: 11694. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 0 (sampled only; not a success-rate estimate).
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

**Writer:** 43854116054 · **Generation:** 447 · **Legacy run:** 43854116054
**Main quote time:** 2026-11-16T11:02:29.959070+00:00 · **Legacy report time:** 2026-11-16T11:02:42.099370+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | XMR/USD ⭐ | 508.09 | 76.79 | +0.12% | 4.51x | STRONG 88/100 | HIGH 61/100 | Watch |
| 2 | SKR/USD ⭐ | 0.010419 | 69.35 | +0.83% | 1.05x | STRONG 70/100 | VERY_HIGH 79/100 | Watch |
| 3 | SENT/USD ⭐ | 0.017571 | 62.03 | +0.35% | 1.37x | STRONG 86/100 | HIGH 67/100 | Watch |
| 4 | XDC/USD | 0.0297 | 61.85 | +1.26% | 0.81x | MODERATE 56/100 | VERY_HIGH 73/100 | Watch |
| 5 | AKT/USD ⭐ | 0.4971 | 43.20 | +0.18% | 1.97x | MODERATE 62/100 | HIGH 66/100 | Watch |
| 6 | BEAM/USD | 0.004198 | 20.55 | -0.14% | 0.45x | WEAK 0/100 | EXTREME 100/100 | Do nothing |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | SKR/USD ⭐ | 0.010419 | 75.44 | +0.83% | 1.05x | 6074 | MODERATE 68/100 | EXTREME 89/100 | Do nothing |
| 2 | SENT/USD ⭐ | 0.01758 | 73.06 | +0.35% | 1.37x | 3962 | STRONG 87/100 | VERY_HIGH 73/100 | Watch |
| 3 | XMR/USD ⭐ | 508.09 | 69.01 | +0.12% | 4.51x | 10304 | STRONG 80/100 | HIGH 67/100 | Watch |
| 4 | AKT/USD ⭐ | 0.4972 | 44.20 | +0.18% | 1.97x | 3429 | MODERATE 67/100 | HIGH 60/100 | Watch |
| 5 | AAVE/USD | 109.83 | 39.15 | +0.29% | 1.01x | 4556 | MODERATE 55/100 | HIGH 62/100 | Watch |
| 6 | CAP/USD | 0.105508 | 37.35 | +0.49% | 4.97x | 3457 | MODERATE 69/100 | HIGH 66/100 | Watch |

**Same-run overlap:** XMR/USD, SKR/USD, SENT/USD, AKT/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
