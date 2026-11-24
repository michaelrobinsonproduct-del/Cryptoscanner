# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-24T21:32:13.825554+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/45491625445
**Source SHA:** 858c8bc8ec5d7641ddb39cacd8aca91719f855b1
**Previous ledger commit:** 8174803490c842d40a1a83d48838f22c5babc8c1 (atomic ledger/results publication)
**Ledger generation:** 1628 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 5s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 628; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 610; valid market observations: 609; OHLC screened: 12.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | XMR/USD | 501.26 | 78.537 | 71.164 | +3.14% | +0.53% | 1.47x | 11.6 | 2026-11-24T21:32:09.181723+00:00 | Not calibrated | STRONG 79/100 | HIGH 61/100 | Watch | WATCH |
| 2 | LUNA/USD | 4.604e-05 | 71.334 | 65.627 | +5.91% | +0.26% | 1.44x | 15.2 | 2026-11-24T21:32:09.181723+00:00 | Not calibrated | STRONG 76/100 | HIGH 66/100 | Watch | WATCH |
| 3 | PEPE/USD | 3.471e-06 | 71.045 | 53.009 | +1.43% | +0.61% | 4.22x | 2.9 | 2026-11-24T21:32:09.181723+00:00 | Not calibrated | STRONG 91/100 | HIGH 55/100 | Consider small entry | WATCH |
| 4 | GBP/USD | 1.31084 | 57.362 | 58.924 | +0.58% | +0.01% | 0.84x | 0.3 | 2026-11-24T21:32:09.181723+00:00 | Not calibrated | MODERATE 49/100 | HIGH 62/100 | Watch | WATCH |
| 5 | AUD/USD | 0.66428 | 41.625 | 44.227 | +0.26% | -0.01% | 0.75x | 2.0 | 2026-11-24T21:32:09.181723+00:00 | Not calibrated | WEAK 26/100 | VERY_HIGH 76/100 | Do nothing | WATCH |
| 6 | NIGHT/USD | 0.04844 | 35.464 | 40.395 | +0.60% | +0.19% | 0.41x | 8.3 | 2026-11-24T21:32:09.181723+00:00 | Not calibrated | WEAK 38/100 | VERY_HIGH 70/100 | Watch | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | XMR/USD | 71.164 | 501.26 | +0.53% | 1.47x |
| 2 | LUNA/USD | 65.627 | 4.604e-05 | +0.26% | 1.44x |
| 3 | GBP/USD | 58.924 | 1.31084 | +0.01% | 0.84x |
| 4 | PEPE/USD | 53.009 | 3.471e-06 | +0.61% | 4.22x |
| 5 | AUD/USD | 44.227 | 0.66428 | -0.01% | 0.75x |
| 6 | NIGHT/USD | 40.395 | 0.04844 | +0.19% | 0.41x |

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

- Persisted scans: 1628; predictions: 13955; observations: 986544.
- Matured sampled outcomes across 1/6/24/48h: 28631; gap abstentions: 22370. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 143 (sampled only; not a success-rate estimate).
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

**Writer:** 45491625445 · **Generation:** 1628 · **Legacy run:** 45491625445
**Main quote time:** 2026-11-24T21:32:13.825554+00:00 · **Legacy report time:** 2026-11-24T21:33:03.685177+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | XMR/USD ⭐ | 501.26 | 78.54 | +0.53% | 1.47x | STRONG 89/100 | HIGH 61/100 | Watch |
| 2 | LUNA/USD ⭐ | 4.604e-05 | 71.33 | +0.26% | 1.44x | STRONG 86/100 | HIGH 66/100 | Watch |
| 3 | PEPE/USD ⭐ | 3.471e-06 | 71.05 | +0.61% | 4.22x | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 4 | GBP/USD | 1.31084 | 57.36 | +0.01% | 0.84x | MODERATE 49/100 | HIGH 62/100 | Watch |
| 5 | AUD/USD | 0.66428 | 41.63 | -0.01% | 0.75x | WEAK 26/100 | VERY_HIGH 76/100 | Do nothing |
| 6 | NIGHT/USD | 0.04844 | 35.46 | +0.19% | 0.41x | WEAK 38/100 | VERY_HIGH 70/100 | Watch |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | XMR/USD ⭐ | 501.44 | 78.56 | +0.53% | 1.47x | 7846 | STRONG 94/100 | HIGH 55/100 | Watch |
| 2 | LUNA/USD ⭐ | 4.604e-05 | 67.56 | +0.26% | 1.44x | 1907 | STRONG 84/100 | HIGH 66/100 | Watch |
| 3 | PEPE/USD ⭐ | 3.47e-06 | 60.78 | +0.61% | 4.22x | 6629 | STRONG 95/100 | HIGH 55/100 | Consider small entry |

**Same-run overlap:** XMR/USD, LUNA/USD, PEPE/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
