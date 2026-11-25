# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-25T15:42:23.680318+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/45647647558
**Source SHA:** 858c8bc8ec5d7641ddb39cacd8aca91719f855b1
**Previous ledger commit:** 01bdaf44a232a3cafeac7e48bcd28c83d777d4f4 (atomic ledger/results publication)
**Ledger generation:** 1737 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 4s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 627; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 609; valid market observations: 608; OHLC screened: 12.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | MON/USD | 0.01014 | 80.085 | 78.160 | +7.08% | +1.81% | 0.29x | 19.7 | 2026-11-25T15:42:19.681040+00:00 | Not calibrated | MODERATE 65/100 | VERY_HIGH 76/100 | Watch | WATCH |
| 2 | VVV/USD | 24.799 | 67.391 | 57.665 | +1.06% | +2.05% | 0.95x | 8.0 | 2026-11-25T15:42:19.681040+00:00 | Not calibrated | MODERATE 64/100 | HIGH 62/100 | Watch | WATCH |
| 3 | CT/USD | 0.1314 | 47.992 | 44.154 | +4.04% | +0.77% | 1.00x | 30.5 | 2026-11-25T15:42:19.681040+00:00 | Not calibrated | MODERATE 49/100 | EXTREME 86/100 | Do nothing | WATCH |
| 4 | DRV/USD | 0.32747 | 47.914 | 46.004 | +4.20% | +1.02% | 0.68x | 42.6 | 2026-11-25T15:42:19.681040+00:00 | Not calibrated | WEAK 39/100 | EXTREME 92/100 | Do nothing | WATCH |
| 5 | PIEVERSE/USD | 3.2939 | 46.998 | 56.999 | +6.93% | -0.84% | 0.42x | 39.5 | 2026-11-25T15:42:19.681040+00:00 | Not calibrated | WEAK 13/100 | EXTREME 93/100 | Do nothing | WATCH |
| 6 | XPL/USD | 0.0449 | 39.335 | 38.677 | +2.05% | +0.67% | 0.73x | 22.2 | 2026-11-25T15:42:19.681040+00:00 | Not calibrated | WEAK 40/100 | EXTREME 87/100 | Do nothing | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | MON/USD | 78.160 | 0.01014 | +1.81% | 0.29x |
| 2 | VVV/USD | 57.665 | 24.799 | +2.05% | 0.95x |
| 3 | PIEVERSE/USD | 56.999 | 3.2939 | -0.84% | 0.42x |
| 4 | DRV/USD | 46.004 | 0.32747 | +1.02% | 0.68x |
| 5 | CT/USD | 44.154 | 0.1314 | +0.77% | 1.00x |
| 6 | XPL/USD | 38.677 | 0.0449 | +0.67% | 0.73x |

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

- Persisted scans: 1737; predictions: 14618; observations: 1052881.
- Matured sampled outcomes across 1/6/24/48h: 32370; gap abstentions: 22370. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 146 (sampled only; not a success-rate estimate).
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

**Writer:** 45647647558 · **Generation:** 1737 · **Legacy run:** 45647647558
**Main quote time:** 2026-11-25T15:42:23.680318+00:00 · **Legacy report time:** 2026-11-25T15:43:11.495782+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | MON/USD | 0.01014 | 80.08 | +1.81% | 0.29x | MODERATE 65/100 | VERY_HIGH 76/100 | Watch |
| 2 | VVV/USD | 24.799 | 67.39 | +2.05% | 0.95x | MODERATE 64/100 | HIGH 62/100 | Watch |
| 3 | CT/USD ⭐ | 0.1314 | 47.99 | +0.77% | 1.00x | MODERATE 59/100 | EXTREME 86/100 | Do nothing |
| 4 | DRV/USD | 0.32747 | 47.91 | +1.02% | 0.68x | WEAK 39/100 | EXTREME 92/100 | Do nothing |
| 5 | PIEVERSE/USD | 3.2939 | 47.00 | -0.84% | 0.42x | WEAK 13/100 | EXTREME 93/100 | Do nothing |
| 6 | XPL/USD | 0.0449 | 39.33 | +0.67% | 0.73x | WEAK 40/100 | EXTREME 87/100 | Do nothing |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | CT/USD ⭐ | 0.131 | 60.68 | +0.77% | 1.00x | 1564 | MODERATE 65/100 | EXTREME 86/100 | Do nothing |

**Same-run overlap:** CT/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
