# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-28T07:37:33.992350+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/46121835836
**Source SHA:** 858c8bc8ec5d7641ddb39cacd8aca91719f855b1
**Previous ledger commit:** 06d086c6c3e6495093e80f3c0eaf8066ef9e1a83 (atomic ledger/results publication)
**Ledger generation:** 2124 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 4s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 628; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 610; valid market observations: 606; OHLC screened: 15.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | XMR/USD | 423 | 80.091 | 79.791 | +3.86% | -0.37% | 1.22x | 4.5 | 2026-11-28T07:37:30.228773+00:00 | Not calibrated | MODERATE 50/100 | HIGH 68/100 | Watch | WATCH |
| 2 | SPACE/USD | 0.004343 | 75.052 | 53.799 | +3.95% | +1.25% | 3.13x | 9.2 | 2026-11-28T07:37:30.228773+00:00 | Not calibrated | STRONG 93/100 | HIGH 67/100 | Consider small entry | WATCH |
| 3 | NEAR/USD | 3.0424 | 73.853 | 59.462 | +0.80% | -0.12% | 27.41x | 2.3 | 2026-11-28T07:37:30.228773+00:00 | Not calibrated | MODERATE 67/100 | HIGH 61/100 | Watch | WATCH |
| 4 | ZEC/USD | 736.67 | 68.385 | 54.354 | +0.29% | -0.19% | 6.59x | 5.3 | 2026-11-28T07:37:30.228773+00:00 | Not calibrated | MODERATE 64/100 | HIGH 61/100 | Watch | WATCH |
| 5 | CC/USD | 0.07536 | 60.767 | 43.702 | +1.63% | +0.41% | 3.75x | 4.0 | 2026-11-28T07:37:30.228773+00:00 | Not calibrated | STRONG 85/100 | HIGH 60/100 | Watch | WATCH |
| 6 | HYPE/USD | 63.95 | 57.347 | 58.506 | +0.72% | +0.11% | 0.83x | 3.1 | 2026-11-28T07:37:30.228773+00:00 | Not calibrated | MODERATE 49/100 | HIGH 62/100 | Watch | WATCH |
| 7 | VVV/USD | 26.296 | 47.572 | 54.889 | +2.12% | -0.54% | 0.54x | 8.7 | 2026-11-28T07:37:30.228773+00:00 | Not calibrated | WEAK 29/100 | VERY_HIGH 76/100 | Do nothing | WATCH |
| 8 | SEI/USD | 0.03862 | 32.769 | 33.698 | +0.55% | -0.57% | 1.19x | 5.2 | 2026-11-28T07:37:30.228773+00:00 | Not calibrated | WEAK 26/100 | VERY_HIGH 73/100 | Do nothing | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | XMR/USD | 79.791 | 423 | -0.37% | 1.22x |
| 2 | NEAR/USD | 59.462 | 3.0424 | -0.12% | 27.41x |
| 3 | HYPE/USD | 58.506 | 63.95 | +0.11% | 0.83x |
| 4 | VVV/USD | 54.889 | 26.296 | -0.54% | 0.54x |
| 5 | ZEC/USD | 54.354 | 736.67 | -0.19% | 6.59x |
| 6 | SPACE/USD | 53.799 | 0.004343 | +1.25% | 3.13x |
| 7 | CC/USD | 43.702 | 0.07536 | +0.41% | 3.75x |
| 8 | SEI/USD | 33.698 | 0.03862 | -0.57% | 1.19x |

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

- Persisted scans: 2124; predictions: 19029; observations: 1286190.
- Matured sampled outcomes across 1/6/24/48h: 44667; gap abstentions: 25968. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 155 (sampled only; not a success-rate estimate).
- False positives / missed movers: NOT VERIFIED without eligible continuous outcome coverage.
- Baseline vs challenger: recorded as-of; unbiased held-out lift NOT MEASURED.
- Online Kraken /USD stablecoin-base pairs excluded: 18 (counted from this scan's online AssetPairs metadata, not inferred from price).
- Stablecoin base exclusions: BRL1, BUSD, DAI, EUR, EURC, EUROP, EURQ, EURR, EURT, FDUSD, FRAX, GUSD, PYUSD, QCAD, RLUSD, TGBP, TUSD, USD, USD1, USDC, USDD, USDE, USDG, USDQ, USDR, USDS, USDT, ZUSD.
- DEX: NOT USED; no DEX freshness gate.
- OHLC screening abstentions: 7; details in immutable scan JSON artifact.
- Storage: ledger and results published in one non-force Git commit and read back. Independent artifact recovery is NOT VERIFIED by this scan alone.
- Errors: none in successful committed scan; a failed workflow must not publish a SUCCESS report.

# Cryptoscanner — challenger and independent legacy-inspired WATCH

Paper only · risk is high or higher · 30%+ in 48h probability NOT CALIBRATED
Signal confidence 0–100 means setup strength only, NOT a win probability. Actions are research guidance; no trade authorization.

**Writer:** 46121835836 · **Generation:** 2124 · **Legacy run:** 46121835836
**Main quote time:** 2026-11-28T07:37:33.992350+00:00 · **Legacy report time:** 2026-11-28T07:38:14.749129+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | XMR/USD | 423 | 80.09 | -0.37% | 1.22x | MODERATE 50/100 | HIGH 68/100 | Watch |
| 2 | SPACE/USD ⭐ | 0.004343 | 75.05 | +1.25% | 3.13x | STRONG 100/100 | HIGH 67/100 | Consider small entry |
| 3 | NEAR/USD | 3.0424 | 73.85 | -0.12% | 27.41x | MODERATE 67/100 | HIGH 61/100 | Watch |
| 4 | ZEC/USD | 736.67 | 68.38 | -0.19% | 6.59x | MODERATE 64/100 | HIGH 61/100 | Watch |
| 5 | CC/USD ⭐ | 0.07536 | 60.77 | +0.41% | 3.75x | STRONG 95/100 | HIGH 60/100 | Consider small entry |
| 6 | HYPE/USD | 63.95 | 57.35 | +0.11% | 0.83x | MODERATE 49/100 | HIGH 62/100 | Watch |
| 7 | VVV/USD | 26.296 | 47.57 | -0.54% | 0.54x | WEAK 29/100 | VERY_HIGH 76/100 | Do nothing |
| 8 | SEI/USD | 0.03862 | 32.77 | -0.57% | 1.19x | WEAK 26/100 | VERY_HIGH 73/100 | Do nothing |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | SPACE/USD ⭐ | 0.004379 | 77.75 | +1.25% | 3.13x | 2106 | STRONG 100/100 | HIGH 67/100 | Consider small entry |
| 2 | CC/USD ⭐ | 0.07536 | 53.38 | +0.41% | 3.75x | 5084 | STRONG 92/100 | HIGH 60/100 | Consider small entry |

**Same-run overlap:** SPACE/USD, CC/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
