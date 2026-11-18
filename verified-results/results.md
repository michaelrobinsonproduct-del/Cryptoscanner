# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-18T00:35:04.571816+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/44208942543
**Source SHA:** 394c17eeb7071fba40e02dbbb1ea97cedb3a0a8a
**Previous ledger commit:** 0708fa927731610736406a53c88e3f30250d05b7 (atomic ledger/results publication)
**Ledger generation:** 484 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 5s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 627; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 609; valid market observations: 609; OHLC screened: 14.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | VVV/USD | 21.157 | 65.068 | 47.687 | +0.62% | +0.48% | 14.51x | 10.9 | 2026-11-18T00:34:59.758885+00:00 | Not calibrated | STRONG 83/100 | HIGH 61/100 | Watch | WATCH |
| 2 | SENT/USD | 0.01881 | 50.454 | 34.041 | +0.76% | +0.28% | 6.48x | 4.3 | 2026-11-18T00:34:59.758885+00:00 | Not calibrated | STRONG 80/100 | HIGH 67/100 | Watch | WATCH |
| 3 | CAP/USD | 0.102694 | 44.391 | 41.449 | +1.70% | +1.30% | 0.64x | 6.1 | 2026-11-18T00:34:59.758885+00:00 | Not calibrated | MODERATE 52/100 | VERY_HIGH 75/100 | Watch | WATCH |
| 4 | XLM/USD | 0.141763 | 44.200 | 44.774 | +0.30% | +0.23% | 0.83x | 2.0 | 2026-11-18T00:34:59.758885+00:00 | Not calibrated | MODERATE 52/100 | HIGH 62/100 | Watch | WATCH |
| 5 | KAS/USD | 0.02759 | 30.895 | 31.886 | +0.36% | -0.07% | 0.94x | 7.3 | 2026-11-18T00:34:59.758885+00:00 | Not calibrated | WEAK 20/100 | VERY_HIGH 73/100 | Do nothing | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | VVV/USD | 47.687 | 21.157 | +0.48% | 14.51x |
| 2 | XLM/USD | 44.774 | 0.141763 | +0.23% | 0.83x |
| 3 | CAP/USD | 41.449 | 0.102694 | +1.30% | 0.64x |
| 4 | SENT/USD | 34.041 | 0.01881 | +0.28% | 6.48x |
| 5 | KAS/USD | 31.886 | 0.02759 | -0.07% | 0.94x |

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

- Persisted scans: 484; predictions: 4226; observations: 291763.
- Matured sampled outcomes across 1/6/24/48h: 3279; gap abstentions: 12410. Per-horizon counts require independent audit; do not infer held-out lift.
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

**Writer:** 44208942543 · **Generation:** 484 · **Legacy run:** 44208942543
**Main quote time:** 2026-11-18T00:35:04.571816+00:00 · **Legacy report time:** 2026-11-18T00:35:19.558360+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | VVV/USD ⭐ | 21.157 | 65.07 | +0.48% | 14.51x | STRONG 93/100 | HIGH 61/100 | Consider small entry |
| 2 | SENT/USD ⭐ | 0.01881 | 50.45 | +0.28% | 6.48x | STRONG 90/100 | HIGH 67/100 | Consider small entry |
| 3 | CAP/USD | 0.102694 | 44.39 | +1.30% | 0.64x | MODERATE 52/100 | VERY_HIGH 75/100 | Watch |
| 4 | XLM/USD | 0.141763 | 44.20 | +0.23% | 0.83x | MODERATE 52/100 | HIGH 62/100 | Watch |
| 5 | KAS/USD | 0.02759 | 30.90 | -0.07% | 0.94x | WEAK 20/100 | VERY_HIGH 73/100 | Do nothing |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | VVV/USD ⭐ | 21.17 | 51.49 | +0.66% | 10.34x | 7591 | STRONG 86/100 | HIGH 61/100 | Consider small entry |
| 2 | XMR/USD | 509.43 | 48.74 | +0.15% | 1.61x | 12327 | MODERATE 59/100 | HIGH 55/100 | Watch |
| 3 | SENT/USD ⭐ | 0.01881 | 43.75 | +0.28% | 6.48x | 3818 | STRONG 87/100 | HIGH 67/100 | Consider small entry |

**Same-run overlap:** VVV/USD, SENT/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
