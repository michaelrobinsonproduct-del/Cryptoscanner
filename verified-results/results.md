# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-25T10:17:30.398401+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/45593075783
**Source SHA:** 858c8bc8ec5d7641ddb39cacd8aca91719f855b1
**Previous ledger commit:** d162a57e328212ff8e17bb81f74f64f56ca87391 (atomic ledger/results publication)
**Ledger generation:** 1704 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 5s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 627; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 609; valid market observations: 608; OHLC screened: 19.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | VVV/USD | 24.926 | 73.499 | 58.436 | +1.58% | +0.14% | 2.44x | 15.3 | 2026-11-25T10:17:24.901930+00:00 | Not calibrated | STRONG 77/100 | HIGH 61/100 | Watch | WATCH |
| 2 | MON/USD | 0.00998 | 64.451 | 77.191 | +5.39% | -2.35% | 0.90x | 20.1 | 2026-11-25T10:17:24.901930+00:00 | Not calibrated | WEAK 27/100 | VERY_HIGH 84/100 | Do nothing | WATCH |
| 3 | BABY/USD | 0.0086 | 43.126 | 42.953 | +4.12% | +0.82% | 0.61x | 34.8 | 2026-11-25T10:17:24.901930+00:00 | Not calibrated | WEAK 42/100 | EXTREME 94/100 | Do nothing | WATCH |
| 4 | CAP/USD | 0.093452 | 39.475 | 36.587 | +1.12% | +0.97% | 0.80x | 6.1 | 2026-11-25T10:17:24.901930+00:00 | Not calibrated | MODERATE 50/100 | HIGH 67/100 | Watch | WATCH |
| 5 | 2Z/USD | 0.01655 | 18.817 | 25.738 | +0.98% | -1.14% | 0.88x | 24.2 | 2026-11-25T10:17:24.901930+00:00 | Not calibrated | WEAK 4/100 | EXTREME 96/100 | Do nothing | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | MON/USD | 77.191 | 0.00998 | -2.35% | 0.90x |
| 2 | VVV/USD | 58.436 | 24.926 | +0.14% | 2.44x |
| 3 | BABY/USD | 42.953 | 0.0086 | +0.82% | 0.61x |
| 4 | CAP/USD | 36.587 | 0.093452 | +0.97% | 0.80x |
| 5 | 2Z/USD | 25.738 | 0.01655 | -1.14% | 0.88x |

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

- Persisted scans: 1704; predictions: 14444; observations: 1032817.
- Matured sampled outcomes across 1/6/24/48h: 31250; gap abstentions: 22370. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 146 (sampled only; not a success-rate estimate).
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

**Writer:** 45593075783 · **Generation:** 1704 · **Legacy run:** 45593075783
**Main quote time:** 2026-11-25T10:17:30.398401+00:00 · **Legacy report time:** 2026-11-25T10:18:45.810802+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | VVV/USD ⭐ | 24.926 | 73.50 | +0.14% | 2.44x | STRONG 87/100 | HIGH 61/100 | Watch |
| 2 | MON/USD | 0.00998 | 64.45 | -2.35% | 0.90x | WEAK 27/100 | VERY_HIGH 84/100 | Do nothing |
| 3 | BABY/USD | 0.0086 | 43.13 | +0.82% | 0.61x | WEAK 42/100 | EXTREME 94/100 | Do nothing |
| 4 | CAP/USD | 0.093452 | 39.48 | +0.97% | 0.80x | MODERATE 50/100 | HIGH 67/100 | Watch |
| 5 | 2Z/USD | 0.01655 | 18.82 | -1.14% | 0.88x | WEAK 4/100 | EXTREME 96/100 | Do nothing |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | VVV/USD ⭐ | 24.926 | 62.14 | +0.14% | 2.44x | 13740 | STRONG 81/100 | HIGH 61/100 | Watch |

**Same-run overlap:** VVV/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
