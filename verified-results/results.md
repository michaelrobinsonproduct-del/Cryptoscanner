# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-25T05:37:19.714127+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/45554530250
**Source SHA:** 858c8bc8ec5d7641ddb39cacd8aca91719f855b1
**Previous ledger commit:** 22be4e800cf7da44c88d9f353f82926e758dfcc2 (atomic ledger/results publication)
**Ledger generation:** 1676 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 5s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 628; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 610; valid market observations: 609; OHLC screened: 17.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | DRV/USD | 0.33012 | 72.052 | 69.533 | +5.04% | +0.67% | 0.91x | 5.5 | 2026-11-25T05:37:14.842424+00:00 | Not calibrated | MODERATE 66/100 | HIGH 62/100 | Watch | WATCH |
| 2 | MON/USD | 0.0099 | 71.234 | 74.950 | +4.54% | +0.30% | 0.48x | 10.1 | 2026-11-25T05:37:14.842424+00:00 | Not calibrated | MODERATE 61/100 | VERY_HIGH 76/100 | Watch | WATCH |
| 3 | VVV/USD | 24.799 | 52.949 | 58.611 | +1.06% | -0.49% | 0.68x | 7.7 | 2026-11-25T05:37:14.842424+00:00 | Not calibrated | WEAK 31/100 | VERY_HIGH 76/100 | Do nothing | WATCH |
| 4 | XMR/USD | 510.94 | 44.823 | 52.914 | +0.26% | -0.44% | 0.41x | 4.5 | 2026-11-25T05:37:14.842424+00:00 | Not calibrated | WEAK 27/100 | VERY_HIGH 76/100 | Do nothing | WATCH |
| 5 | SYRUP/USD | 0.07142 | 35.277 | 32.501 | +2.51% | +0.46% | 1.05x | 33.7 | 2026-11-25T05:37:14.842424+00:00 | Not calibrated | WEAK 43/100 | VERY_HIGH 79/100 | Watch | WATCH |
| 6 | BLUR/USD | 0.00868 | 31.691 | 24.847 | +0.81% | +1.74% | 0.81x | 23.0 | 2026-11-25T05:37:14.842424+00:00 | Not calibrated | WEAK 36/100 | EXTREME 86/100 | Do nothing | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | MON/USD | 74.950 | 0.0099 | +0.30% | 0.48x |
| 2 | DRV/USD | 69.533 | 0.33012 | +0.67% | 0.91x |
| 3 | VVV/USD | 58.611 | 24.799 | -0.49% | 0.68x |
| 4 | XMR/USD | 52.914 | 510.94 | -0.44% | 0.41x |
| 5 | SYRUP/USD | 32.501 | 0.07142 | +0.46% | 1.05x |
| 6 | BLUR/USD | 24.847 | 0.00868 | +1.74% | 0.81x |

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

- Persisted scans: 1676; predictions: 14228; observations: 1015775.
- Matured sampled outcomes across 1/6/24/48h: 30225; gap abstentions: 22370. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 146 (sampled only; not a success-rate estimate).
- False positives / missed movers: NOT VERIFIED without eligible continuous outcome coverage.
- Baseline vs challenger: recorded as-of; unbiased held-out lift NOT MEASURED.
- Online Kraken /USD stablecoin-base pairs excluded: 18 (counted from this scan's online AssetPairs metadata, not inferred from price).
- Stablecoin base exclusions: BRL1, BUSD, DAI, EUR, EURC, EUROP, EURQ, EURR, EURT, FDUSD, FRAX, GUSD, PYUSD, QCAD, RLUSD, TGBP, TUSD, USD, USD1, USDC, USDD, USDE, USDG, USDQ, USDR, USDS, USDT, ZUSD.
- DEX: NOT USED; no DEX freshness gate.
- OHLC screening abstentions: 11; details in immutable scan JSON artifact.
- Storage: ledger and results published in one non-force Git commit and read back. Independent artifact recovery is NOT VERIFIED by this scan alone.
- Errors: none in successful committed scan; a failed workflow must not publish a SUCCESS report.

# Cryptoscanner — challenger and independent legacy-inspired WATCH

Paper only · risk is high or higher · 30%+ in 48h probability NOT CALIBRATED
Signal confidence 0–100 means setup strength only, NOT a win probability. Actions are research guidance; no trade authorization.

**Writer:** 45554530250 · **Generation:** 1676 · **Legacy run:** 45554530250
**Main quote time:** 2026-11-25T05:37:19.714127+00:00 · **Legacy report time:** 2026-11-25T05:38:19.050260+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | DRV/USD | 0.33012 | 72.05 | +0.67% | 0.91x | MODERATE 66/100 | HIGH 62/100 | Watch |
| 2 | MON/USD | 0.0099 | 71.23 | +0.30% | 0.48x | MODERATE 61/100 | VERY_HIGH 76/100 | Watch |
| 3 | VVV/USD | 24.799 | 52.95 | -0.49% | 0.68x | WEAK 31/100 | VERY_HIGH 76/100 | Do nothing |
| 4 | XMR/USD | 510.94 | 44.82 | -0.44% | 0.41x | WEAK 27/100 | VERY_HIGH 76/100 | Do nothing |
| 5 | SYRUP/USD ⭐ | 0.07142 | 35.28 | +0.46% | 1.05x | MODERATE 53/100 | VERY_HIGH 79/100 | Watch |
| 6 | BLUR/USD | 0.00868 | 31.69 | +1.74% | 0.81x | WEAK 36/100 | EXTREME 86/100 | Do nothing |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | SYRUP/USD ⭐ | 0.07142 | 54.77 | +0.46% | 1.05x | 3451 | MODERATE 67/100 | VERY_HIGH 73/100 | Watch |

**Same-run overlap:** SYRUP/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
