# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-24T13:21:59.252143+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/45402255014
**Source SHA:** 858c8bc8ec5d7641ddb39cacd8aca91719f855b1
**Previous ledger commit:** 5329d9f1670a027b02ebaf27d38f106284f4bfaf (atomic ledger/results publication)
**Ledger generation:** 1579 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 4s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 628; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 610; valid market observations: 609; OHLC screened: 13.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | VVV/USD | 25.537 | 90.550 | 82.062 | +4.45% | -1.30% | 2.83x | 8.2 | 2026-11-24T13:21:55.290284+00:00 | Not calibrated | STRONG 75/100 | HIGH 65/100 | Do nothing | WATCH |
| 2 | MON/USD | 0.01217 | 78.853 | 77.403 | +5.64% | +0.16% | 1.06x | 8.2 | 2026-11-24T13:21:55.290284+00:00 | Not calibrated | MODERATE 64/100 | HIGH 62/100 | Watch | WATCH |
| 3 | GBP/USD | 1.30925 | 72.875 | 57.955 | +0.46% | -0.02% | 2.52x | 0.5 | 2026-11-24T13:21:55.290284+00:00 | Not calibrated | MODERATE 66/100 | HIGH 61/100 | Watch | WATCH |
| 4 | XMR/USD | 496.84 | 72.681 | 65.749 | +2.23% | -0.46% | 1.92x | 9.7 | 2026-11-24T13:21:55.290284+00:00 | Not calibrated | MODERATE 56/100 | HIGH 61/100 | Watch | WATCH |
| 5 | NIGHT/USD | 0.04859 | 39.925 | 50.482 | +0.91% | -1.06% | 0.47x | 8.2 | 2026-11-24T13:21:55.290284+00:00 | Not calibrated | WEAK 25/100 | VERY_HIGH 80/100 | Do nothing | WATCH |
| 6 | 2Z/USD | 0.01585 | 27.823 | 33.383 | +1.28% | -0.50% | 0.70x | 12.6 | 2026-11-24T13:21:55.290284+00:00 | Not calibrated | WEAK 14/100 | EXTREME 94/100 | Do nothing | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | VVV/USD | 82.062 | 25.537 | -1.30% | 2.83x |
| 2 | MON/USD | 77.403 | 0.01217 | +0.16% | 1.06x |
| 3 | XMR/USD | 65.749 | 496.84 | -0.46% | 1.92x |
| 4 | GBP/USD | 57.955 | 1.30925 | -0.02% | 2.52x |
| 5 | NIGHT/USD | 50.482 | 0.04859 | -1.06% | 0.47x |
| 6 | 2Z/USD | 33.383 | 0.01585 | -0.50% | 0.70x |

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

- Persisted scans: 1579; predictions: 13618; observations: 956709.
- Matured sampled outcomes across 1/6/24/48h: 26581; gap abstentions: 22370. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 143 (sampled only; not a success-rate estimate).
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

**Writer:** 45402255014 · **Generation:** 1579 · **Legacy run:** 45402255014
**Main quote time:** 2026-11-24T13:21:59.252143+00:00 · **Legacy report time:** 2026-11-24T13:23:10.595160+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | VVV/USD | 25.537 | 90.55 | -1.30% | 2.83x | STRONG 75/100 | HIGH 65/100 | Do nothing |
| 2 | MON/USD ⭐ | 0.01217 | 78.85 | +0.16% | 1.06x | STRONG 74/100 | HIGH 62/100 | Watch |
| 3 | GBP/USD | 1.30925 | 72.88 | -0.02% | 2.52x | MODERATE 66/100 | HIGH 61/100 | Watch |
| 4 | XMR/USD | 496.84 | 72.68 | -0.46% | 1.92x | MODERATE 56/100 | HIGH 61/100 | Watch |
| 5 | NIGHT/USD | 0.04859 | 39.92 | -1.06% | 0.47x | WEAK 25/100 | VERY_HIGH 80/100 | Do nothing |
| 6 | 2Z/USD | 0.01585 | 27.82 | -0.50% | 0.70x | WEAK 14/100 | EXTREME 94/100 | Do nothing |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | MON/USD ⭐ | 0.01215 | 77.94 | +0.16% | 1.06x | 10887 | MODERATE 69/100 | HIGH 68/100 | Watch |

**Same-run overlap:** MON/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
