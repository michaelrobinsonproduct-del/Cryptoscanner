# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-18T00:30:09.957293+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/44208242204
**Source SHA:** 394c17eeb7071fba40e02dbbb1ea97cedb3a0a8a
**Previous ledger commit:** 2244ccf2bb3928acc69e700d65dc8d091b97f6aa (atomic ledger/results publication)
**Ledger generation:** 483 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 8s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 627; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 609; valid market observations: 609; OHLC screened: 20.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | VVV/USD | 21.095 | 64.413 | 47.031 | +0.33% | +0.48% | 14.51x | 7.6 | 2026-11-18T00:30:02.250321+00:00 | Not calibrated | STRONG 87/100 | HIGH 55/100 | Watch | WATCH |
| 2 | TAO/USD | 198.2081 | 56.541 | 54.321 | +0.34% | +0.10% | 1.17x | 6.1 | 2026-11-18T00:30:02.250321+00:00 | Not calibrated | MODERATE 53/100 | HIGH 62/100 | Watch | WATCH |
| 3 | SENT/USD | 0.018771 | 49.602 | 32.838 | +0.55% | +0.35% | 5.33x | 3.7 | 2026-11-18T00:30:02.250321+00:00 | Not calibrated | STRONG 80/100 | HIGH 67/100 | Watch | WATCH |
| 4 | XLM/USD | 0.141707 | 43.225 | 43.798 | +0.26% | +0.23% | 0.83x | 3.6 | 2026-11-18T00:30:02.250321+00:00 | Not calibrated | MODERATE 52/100 | HIGH 62/100 | Watch | WATCH |
| 5 | KAS/USD | 0.02763 | 30.510 | 29.294 | +0.51% | +0.29% | 0.98x | 14.5 | 2026-11-18T00:30:02.250321+00:00 | Not calibrated | WEAK 40/100 | VERY_HIGH 73/100 | Watch | WATCH |
| 6 | CAP/USD | 0.101413 | 22.145 | 28.806 | +0.43% | +0.50% | 0.08x | 13.6 | 2026-11-18T00:30:02.250321+00:00 | Not calibrated | WEAK 36/100 | VERY_HIGH 81/100 | Watch | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | TAO/USD | 54.321 | 198.2081 | +0.10% | 1.17x |
| 2 | VVV/USD | 47.031 | 21.095 | +0.48% | 14.51x |
| 3 | XLM/USD | 43.798 | 0.141707 | +0.23% | 0.83x |
| 4 | SENT/USD | 32.838 | 0.018771 | +0.35% | 5.33x |
| 5 | KAS/USD | 29.294 | 0.02763 | +0.29% | 0.98x |
| 6 | CAP/USD | 28.806 | 0.101413 | +0.50% | 0.08x |

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

- Persisted scans: 483; predictions: 4221; observations: 291154.
- Matured sampled outcomes across 1/6/24/48h: 3267; gap abstentions: 12410. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 0 (sampled only; not a success-rate estimate).
- False positives / missed movers: NOT VERIFIED without eligible continuous outcome coverage.
- Baseline vs challenger: recorded as-of; unbiased held-out lift NOT MEASURED.
- Online Kraken /USD stablecoin-base pairs excluded: 18 (counted from this scan's online AssetPairs metadata, not inferred from price).
- Stablecoin base exclusions: BRL1, BUSD, DAI, EUR, EURC, EUROP, EURQ, EURR, EURT, FDUSD, FRAX, GUSD, PYUSD, QCAD, RLUSD, TGBP, TUSD, USD, USD1, USDC, USDD, USDE, USDG, USDQ, USDR, USDS, USDT, ZUSD.
- DEX: NOT USED; no DEX freshness gate.
- OHLC screening abstentions: 14; details in immutable scan JSON artifact.
- Storage: ledger and results published in one non-force Git commit and read back. Independent artifact recovery is NOT VERIFIED by this scan alone.
- Errors: none in successful committed scan; a failed workflow must not publish a SUCCESS report.

# Cryptoscanner — challenger and independent legacy-inspired WATCH

Paper only · risk is high or higher · 30%+ in 48h probability NOT CALIBRATED
Signal confidence 0–100 means setup strength only, NOT a win probability. Actions are research guidance; no trade authorization.

**Writer:** 44208242204 · **Generation:** 483 · **Legacy run:** 44208242204
**Main quote time:** 2026-11-18T00:30:09.957293+00:00 · **Legacy report time:** 2026-11-18T00:30:23.176527+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | VVV/USD ⭐ | 21.095 | 64.41 | +0.48% | 14.51x | STRONG 97/100 | HIGH 55/100 | Consider small entry |
| 2 | TAO/USD ⭐ | 198.2081 | 56.54 | +0.10% | 1.17x | MODERATE 63/100 | HIGH 62/100 | Watch |
| 3 | SENT/USD ⭐ | 0.018771 | 49.60 | +0.35% | 5.33x | STRONG 90/100 | HIGH 67/100 | Consider small entry |
| 4 | XLM/USD | 0.141707 | 43.22 | +0.23% | 0.83x | MODERATE 52/100 | HIGH 62/100 | Watch |
| 5 | KAS/USD | 0.02763 | 30.51 | +0.29% | 0.98x | WEAK 40/100 | VERY_HIGH 73/100 | Watch |
| 6 | CAP/USD | 0.101413 | 22.15 | +0.50% | 0.08x | WEAK 36/100 | VERY_HIGH 81/100 | Watch |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | TAO/USD ⭐ | 198.2081 | 48.21 | +0.10% | 1.17x | 5728 | MODERATE 59/100 | HIGH 62/100 | Watch |
| 2 | VVV/USD ⭐ | 21.095 | 46.48 | +0.48% | 14.51x | 7533 | STRONG 78/100 | HIGH 67/100 | Consider small entry |
| 3 | SENT/USD ⭐ | 0.018771 | 43.57 | +0.35% | 5.33x | 3799 | STRONG 87/100 | HIGH 67/100 | Consider small entry |

**Same-run overlap:** VVV/USD, TAO/USD, SENT/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
