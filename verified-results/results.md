# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-23T02:33:03.434777+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/45100505868
**Source SHA:** 193371a597e6dbc5a6a884defbe9e1519a6a183a
**Previous ledger commit:** 91aa2f885cfdb4cbfd1caf7259fb064a25adece1 (atomic ledger/results publication)
**Ledger generation:** 1369 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 4s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 628; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 610; valid market observations: 609; OHLC screened: 12.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | ICNT/USD | 0.3636 | 66.820 | 48.896 | +3.24% | +0.58% | 7.55x | 13.8 | 2026-11-23T02:32:59.434627+00:00 | Not calibrated | STRONG 83/100 | HIGH 66/100 | Watch | WATCH |
| 2 | BLESS/USD | 0.016714 | 56.642 | 50.586 | +3.86% | +0.95% | 1.13x | 30.0 | 2026-11-23T02:32:59.434627+00:00 | Not calibrated | MODERATE 53/100 | VERY_HIGH 74/100 | Watch | WATCH |
| 3 | AUD/USD | 0.66351 | 39.219 | 39.962 | +0.29% | +0.00% | 0.92x | 3.6 | 2026-11-23T02:32:59.434627+00:00 | Not calibrated | WEAK 40/100 | HIGH 62/100 | Watch | WATCH |
| 4 | DRV/USD | 0.37042 | 29.929 | 41.377 | +0.43% | -1.72% | 0.71x | 12.7 | 2026-11-23T02:32:59.434627+00:00 | Not calibrated | WEAK 15/100 | EXTREME 86/100 | Do nothing | WATCH |
| 5 | CAP/USD | 0.09396 | 25.951 | 32.191 | +0.41% | +0.16% | 0.29x | 6.2 | 2026-11-23T02:32:59.434627+00:00 | Not calibrated | WEAK 33/100 | VERY_HIGH 75/100 | Do nothing | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | BLESS/USD | 50.586 | 0.016714 | +0.95% | 1.13x |
| 2 | ICNT/USD | 48.896 | 0.3636 | +0.58% | 7.55x |
| 3 | DRV/USD | 41.377 | 0.37042 | -1.72% | 0.71x |
| 4 | AUD/USD | 39.962 | 0.66351 | +0.00% | 0.92x |
| 5 | CAP/USD | 32.191 | 0.09396 | +0.16% | 0.29x |

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

- Persisted scans: 1369; predictions: 11223; observations: 828826.
- Matured sampled outcomes across 1/6/24/48h: 17933; gap abstentions: 22370. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 86 (sampled only; not a success-rate estimate).
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

**Writer:** 45100505868 · **Generation:** 1369 · **Legacy run:** 45100505868
**Main quote time:** 2026-11-23T02:33:03.434777+00:00 · **Legacy report time:** 2026-11-23T02:34:13.192377+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | ICNT/USD ⭐ | 0.3636 | 66.82 | +0.58% | 7.55x | STRONG 93/100 | HIGH 66/100 | Consider small entry |
| 2 | BLESS/USD ⭐ | 0.016714 | 56.64 | +0.95% | 1.13x | MODERATE 63/100 | VERY_HIGH 74/100 | Watch |
| 3 | AUD/USD | 0.66351 | 39.22 | +0.00% | 0.92x | WEAK 40/100 | HIGH 62/100 | Watch |
| 4 | DRV/USD | 0.37042 | 29.93 | -1.72% | 0.71x | WEAK 15/100 | EXTREME 86/100 | Do nothing |
| 5 | CAP/USD | 0.09396 | 25.95 | +0.16% | 0.29x | WEAK 33/100 | VERY_HIGH 75/100 | Do nothing |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | BLESS/USD ⭐ | 0.016714 | 76.81 | +0.95% | 1.13x | 5662 | STRONG 73/100 | VERY_HIGH 74/100 | Watch |
| 2 | ICNT/USD ⭐ | 0.3636 | 72.32 | +0.58% | 7.55x | 2622 | STRONG 96/100 | HIGH 66/100 | Consider small entry |
| 3 | GBP/USD | 1.3111 | 60.74 | +0.07% | 3.09x | 15424 | STRONG 75/100 | HIGH 55/100 | Watch |

**Same-run overlap:** ICNT/USD, BLESS/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
