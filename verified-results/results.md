# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-23T06:31:26.592257+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/45124445997
**Source SHA:** 858c8bc8ec5d7641ddb39cacd8aca91719f855b1
**Previous ledger commit:** a23e584b30831766795265fedbea253c578d802d (atomic ledger/results publication)
**Ledger generation:** 1393 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 7s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 628; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 610; valid market observations: 609; OHLC screened: 24.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | AI/USD | 0.01629 | 93.244 | 66.994 | +11.42% | +2.25% | 5.53x | 18.4 | 2026-11-23T06:31:19.923912+00:00 | Not calibrated | STRONG 97/100 | VERY_HIGH 73/100 | Watch | WATCH |
| 2 | XRP/USD | 0.93798 | 74.057 | 62.453 | +1.13% | -0.68% | 5.66x | 0.9 | 2026-11-23T06:31:19.923912+00:00 | Not calibrated | MODERATE 67/100 | HIGH 61/100 | Watch | WATCH |
| 3 | JUP/USD | 0.24082 | 72.660 | 74.446 | +7.24% | -0.49% | 1.07x | 10.0 | 2026-11-23T06:31:19.923912+00:00 | Not calibrated | MODERATE 46/100 | VERY_HIGH 73/100 | Watch | WATCH |
| 4 | XLM/USD | 0.12809 | 65.484 | 56.953 | +0.44% | -0.17% | 1.94x | 0.9 | 2026-11-23T06:31:19.923912+00:00 | Not calibrated | MODERATE 53/100 | HIGH 61/100 | Watch | WATCH |
| 5 | SOL/USD | 71.71 | 62.385 | 65.006 | +1.53% | -0.29% | 0.88x | 1.4 | 2026-11-23T06:31:19.923912+00:00 | Not calibrated | WEAK 36/100 | HIGH 68/100 | Watch | WATCH |
| 6 | QNT/USD | 146.88 | 62.042 | 57.012 | +2.40% | +0.20% | 1.40x | 5.4 | 2026-11-23T06:31:19.923912+00:00 | Not calibrated | MODERATE 66/100 | HIGH 55/100 | Watch | WATCH |
| 7 | NIGHT/USD | 0.05012 | 59.910 | 60.474 | +1.93% | -0.16% | 1.02x | 8.0 | 2026-11-23T06:31:19.923912+00:00 | Not calibrated | WEAK 40/100 | HIGH 68/100 | Watch | WATCH |
| 8 | PIEVERSE/USD | 3.8971 | 58.951 | 57.815 | +5.01% | +1.78% | 0.22x | 39.9 | 2026-11-23T06:31:19.923912+00:00 | Not calibrated | WEAK 44/100 | VERY_HIGH 82/100 | Watch | WATCH |
| 9 | CC/USD | 0.07608 | 58.628 | 60.113 | +3.84% | +0.04% | 0.83x | 3.9 | 2026-11-23T06:31:19.923912+00:00 | Not calibrated | MODERATE 49/100 | HIGH 67/100 | Watch | WATCH |
| 10 | SUI/USD | 0.6629 | 54.588 | 61.932 | +1.10% | -0.18% | 0.36x | 1.5 | 2026-11-23T06:31:19.923912+00:00 | Not calibrated | WEAK 32/100 | VERY_HIGH 76/100 | Do nothing | WATCH |
| 11 | PAXG/USD | 3604.91 | 54.527 | 50.179 | +0.92% | -0.01% | 1.44x | 1.6 | 2026-11-23T06:31:19.923912+00:00 | Not calibrated | MODERATE 47/100 | HIGH 61/100 | Watch | WATCH |
| 12 | XBT/USD | 61511 | 52.498 | 58.893 | +0.56% | -0.33% | 0.53x | 0.0 | 2026-11-23T06:31:19.923912+00:00 | Not calibrated | WEAK 31/100 | VERY_HIGH 76/100 | Do nothing | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | JUP/USD | 74.446 | 0.24082 | -0.49% | 1.07x |
| 2 | AI/USD | 66.994 | 0.01629 | +2.25% | 5.53x |
| 3 | SOL/USD | 65.006 | 71.71 | -0.29% | 0.88x |
| 4 | XRP/USD | 62.453 | 0.93798 | -0.68% | 5.66x |
| 5 | SUI/USD | 61.932 | 0.6629 | -0.18% | 0.36x |
| 6 | NIGHT/USD | 60.474 | 0.05012 | -0.16% | 1.02x |
| 7 | CC/USD | 60.113 | 0.07608 | +0.04% | 0.83x |
| 8 | XBT/USD | 58.893 | 61511 | -0.33% | 0.53x |
| 9 | PIEVERSE/USD | 57.815 | 3.8971 | +1.78% | 0.22x |
| 10 | QNT/USD | 57.012 | 146.88 | +0.20% | 1.40x |
| 11 | XLM/USD | 56.953 | 0.12809 | -0.17% | 1.94x |
| 12 | PAXG/USD | 50.179 | 3604.91 | -0.01% | 1.44x |

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

- Persisted scans: 1393; predictions: 11483; observations: 843441.
- Matured sampled outcomes across 1/6/24/48h: 18660; gap abstentions: 22370. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 122 (sampled only; not a success-rate estimate).
- False positives / missed movers: NOT VERIFIED without eligible continuous outcome coverage.
- Baseline vs challenger: recorded as-of; unbiased held-out lift NOT MEASURED.
- Online Kraken /USD stablecoin-base pairs excluded: 18 (counted from this scan's online AssetPairs metadata, not inferred from price).
- Stablecoin base exclusions: BRL1, BUSD, DAI, EUR, EURC, EUROP, EURQ, EURR, EURT, FDUSD, FRAX, GUSD, PYUSD, QCAD, RLUSD, TGBP, TUSD, USD, USD1, USDC, USDD, USDE, USDG, USDQ, USDR, USDS, USDT, ZUSD.
- DEX: NOT USED; no DEX freshness gate.
- OHLC screening abstentions: 5; details in immutable scan JSON artifact.
- Storage: ledger and results published in one non-force Git commit and read back. Independent artifact recovery is NOT VERIFIED by this scan alone.
- Errors: none in successful committed scan; a failed workflow must not publish a SUCCESS report.

# Cryptoscanner — challenger and independent legacy-inspired WATCH

Paper only · risk is high or higher · 30%+ in 48h probability NOT CALIBRATED
Signal confidence 0–100 means setup strength only, NOT a win probability. Actions are research guidance; no trade authorization.

**Writer:** 45124445997 · **Generation:** 1393 · **Legacy run:** 45124445997
**Main quote time:** 2026-11-23T06:31:26.592257+00:00 · **Legacy report time:** 2026-11-23T06:32:19.428431+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | AI/USD ⭐ | 0.01629 | 93.24 | +2.25% | 5.53x | STRONG 100/100 | VERY_HIGH 73/100 | Watch |
| 2 | XRP/USD | 0.93798 | 74.06 | -0.68% | 5.66x | MODERATE 67/100 | HIGH 61/100 | Watch |
| 3 | JUP/USD | 0.24082 | 72.66 | -0.49% | 1.07x | MODERATE 46/100 | VERY_HIGH 73/100 | Watch |
| 4 | XLM/USD | 0.12809 | 65.48 | -0.17% | 1.94x | MODERATE 53/100 | HIGH 61/100 | Watch |
| 5 | SOL/USD | 71.71 | 62.39 | -0.29% | 0.88x | WEAK 36/100 | HIGH 68/100 | Watch |
| 6 | QNT/USD ⭐ | 146.88 | 62.04 | +0.20% | 1.40x | STRONG 76/100 | HIGH 55/100 | Watch |
| 7 | NIGHT/USD | 0.05012 | 59.91 | -0.16% | 1.02x | WEAK 40/100 | HIGH 68/100 | Watch |
| 8 | PIEVERSE/USD | 3.8971 | 58.95 | +1.78% | 0.22x | WEAK 44/100 | VERY_HIGH 82/100 | Watch |
| 9 | CC/USD | 0.07608 | 58.63 | +0.04% | 0.83x | MODERATE 49/100 | HIGH 67/100 | Watch |
| 10 | SUI/USD | 0.6629 | 54.59 | -0.18% | 0.36x | WEAK 32/100 | VERY_HIGH 76/100 | Do nothing |
| 11 | PAXG/USD | 3604.91 | 54.53 | -0.01% | 1.44x | MODERATE 47/100 | HIGH 61/100 | Watch |
| 12 | XBT/USD | 61511 | 52.50 | -0.33% | 0.53x | WEAK 31/100 | VERY_HIGH 76/100 | Do nothing |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | AI/USD ⭐ | 0.01629 | 85.47 | +2.25% | 5.53x | 3240 | STRONG 100/100 | VERY_HIGH 73/100 | Watch |
| 2 | QNT/USD ⭐ | 146.93 | 65.28 | +0.20% | 1.40x | 4494 | STRONG 78/100 | HIGH 55/100 | Watch |

**Same-run overlap:** AI/USD, QNT/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
