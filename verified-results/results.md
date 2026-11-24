# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-24T15:42:13.071477+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/45428068457
**Source SHA:** 858c8bc8ec5d7641ddb39cacd8aca91719f855b1
**Previous ledger commit:** 8a2010e9455576671dbaf684b44b38cb2ee79286 (atomic ledger/results publication)
**Ledger generation:** 1593 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 3s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 628; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 610; valid market observations: 609; OHLC screened: 9.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | XMR/USD | 491.19 | 72.992 | 59.291 | +1.06% | -0.26% | 4.45x | 6.3 | 2026-11-24T15:42:09.793769+00:00 | Not calibrated | MODERATE 66/100 | HIGH 61/100 | Watch | WATCH |
| 2 | VVV/USD | 24.547 | 61.300 | 53.144 | +0.40% | -1.37% | 2.82x | 9.4 | 2026-11-24T15:42:09.793769+00:00 | Not calibrated | MODERATE 61/100 | HIGH 65/100 | Do nothing | WATCH |
| 3 | LUNA/USD | 4.617e-05 | 55.720 | 58.545 | +6.21% | +0.59% | 0.42x | 32.6 | 2026-11-24T15:42:09.793769+00:00 | Not calibrated | MODERATE 48/100 | EXTREME 94/100 | Do nothing | WATCH |
| 4 | GBP/USD | 1.30988 | 54.936 | 58.332 | +0.51% | -0.03% | 0.68x | 0.5 | 2026-11-24T15:42:09.793769+00:00 | Not calibrated | WEAK 32/100 | VERY_HIGH 76/100 | Do nothing | WATCH |
| 5 | 2Z/USD | 0.01596 | 29.814 | 32.065 | +1.98% | -0.75% | 1.15x | 25.1 | 2026-11-24T15:42:09.793769+00:00 | Not calibrated | WEAK 15/100 | EXTREME 92/100 | Do nothing | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | XMR/USD | 59.291 | 491.19 | -0.26% | 4.45x |
| 2 | LUNA/USD | 58.545 | 4.617e-05 | +0.59% | 0.42x |
| 3 | GBP/USD | 58.332 | 1.30988 | -0.03% | 0.68x |
| 4 | VVV/USD | 53.144 | 24.547 | -1.37% | 2.82x |
| 5 | 2Z/USD | 32.065 | 0.01596 | -0.75% | 1.15x |

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

- Persisted scans: 1593; predictions: 13719; observations: 965229.
- Matured sampled outcomes across 1/6/24/48h: 27207; gap abstentions: 22370. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 143 (sampled only; not a success-rate estimate).
- False positives / missed movers: NOT VERIFIED without eligible continuous outcome coverage.
- Baseline vs challenger: recorded as-of; unbiased held-out lift NOT MEASURED.
- Online Kraken /USD stablecoin-base pairs excluded: 18 (counted from this scan's online AssetPairs metadata, not inferred from price).
- Stablecoin base exclusions: BRL1, BUSD, DAI, EUR, EURC, EUROP, EURQ, EURR, EURT, FDUSD, FRAX, GUSD, PYUSD, QCAD, RLUSD, TGBP, TUSD, USD, USD1, USDC, USDD, USDE, USDG, USDQ, USDR, USDS, USDT, ZUSD.
- DEX: NOT USED; no DEX freshness gate.
- OHLC screening abstentions: 4; details in immutable scan JSON artifact.
- Storage: ledger and results published in one non-force Git commit and read back. Independent artifact recovery is NOT VERIFIED by this scan alone.
- Errors: none in successful committed scan; a failed workflow must not publish a SUCCESS report.

# Cryptoscanner — challenger and independent legacy-inspired WATCH

Paper only · risk is high or higher · 30%+ in 48h probability NOT CALIBRATED
Signal confidence 0–100 means setup strength only, NOT a win probability. Actions are research guidance; no trade authorization.

**Writer:** 45428068457 · **Generation:** 1593 · **Legacy run:** 45428068457
**Main quote time:** 2026-11-24T15:42:13.071477+00:00 · **Legacy report time:** 2026-11-24T15:43:04.195578+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | XMR/USD | 491.19 | 72.99 | -0.26% | 4.45x | MODERATE 66/100 | HIGH 61/100 | Watch |
| 2 | VVV/USD | 24.547 | 61.30 | -1.37% | 2.82x | MODERATE 61/100 | HIGH 65/100 | Do nothing |
| 3 | LUNA/USD | 4.617e-05 | 55.72 | +0.59% | 0.42x | MODERATE 48/100 | EXTREME 94/100 | Do nothing |
| 4 | GBP/USD | 1.30988 | 54.94 | -0.03% | 0.68x | WEAK 32/100 | VERY_HIGH 76/100 | Do nothing |
| 5 | 2Z/USD | 0.01596 | 29.81 | -0.75% | 1.15x | WEAK 15/100 | EXTREME 92/100 | Do nothing |

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
