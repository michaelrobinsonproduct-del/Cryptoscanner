# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-21T01:05:36.932409+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/44847933901
**Source SHA:** bdc7e68f7fa75fae6636b7738d52f10a65d92038
**Previous ledger commit:** a47bcc85eed2bbff392fcd16f689bc7f2641b325 (atomic ledger/results publication)
**Ledger generation:** 1052 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 9s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 628; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 610; valid market observations: 608; OHLC screened: 24.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | PUMP/USD | 0.002432 | 64.617 | 47.967 | +0.50% | +0.33% | 5.21x | 8.2 | 2026-11-21T01:05:27.988446+00:00 | Not calibrated | STRONG 87/100 | HIGH 55/100 | Watch | WATCH |
| 2 | PEARL/USD | 1.8755 | 54.293 | 59.114 | +2.58% | -1.19% | 1.11x | 15.5 | 2026-11-21T01:05:27.988446+00:00 | Not calibrated | WEAK 32/100 | VERY_HIGH 78/100 | Do nothing | WATCH |
| 3 | PIEVERSE/USD | 3.035 | 53.164 | 34.379 | +1.21% | +0.76% | 8.18x | 17.8 | 2026-11-21T01:05:27.988446+00:00 | Not calibrated | STRONG 77/100 | HIGH 66/100 | Watch | WATCH |
| 4 | CC/USD | 0.07483 | 51.566 | 36.499 | +0.38% | +0.01% | 3.77x | 5.3 | 2026-11-21T01:05:27.988446+00:00 | Not calibrated | STRONG 71/100 | HIGH 60/100 | Watch | WATCH |
| 5 | KAS/USD | 0.02609 | 51.513 | 35.553 | +0.42% | +0.19% | 12.43x | 11.5 | 2026-11-21T01:05:27.988446+00:00 | Not calibrated | MODERATE 66/100 | HIGH 61/100 | Watch | WATCH |
| 6 | AKE/USD | 0.00619423 | 50.635 | 49.658 | +1.36% | +0.61% | 0.79x | 29.7 | 2026-11-21T01:05:27.988446+00:00 | Not calibrated | MODERATE 45/100 | VERY_HIGH 74/100 | Watch | WATCH |
| 7 | BLUR/USD | 0.00743 | 47.932 | 37.725 | +1.78% | +0.95% | 1.55x | 13.5 | 2026-11-21T01:05:27.988446+00:00 | Not calibrated | MODERATE 64/100 | HIGH 66/100 | Watch | WATCH |
| 8 | CAP/USD | 0.092282 | 38.857 | 35.339 | +0.81% | +0.21% | 1.25x | 6.0 | 2026-11-21T01:05:27.988446+00:00 | Not calibrated | MODERATE 54/100 | HIGH 67/100 | Watch | WATCH |
| 9 | DCR/USD | 10.146 | 26.456 | 29.618 | +0.41% | -0.13% | 0.75x | 7.9 | 2026-11-21T01:05:27.988446+00:00 | Not calibrated | WEAK 18/100 | EXTREME 88/100 | Do nothing | WATCH |
| 10 | TRAC/USD | 0.2707 | 25.337 | 21.551 | +0.26% | +0.33% | 1.21x | 22.2 | 2026-11-21T01:05:27.988446+00:00 | Not calibrated | WEAK 38/100 | EXTREME 86/100 | Do nothing | WATCH |
| 11 | CT/USD | 0.1218 | 20.432 | 23.645 | +0.58% | +0.08% | 0.64x | 24.6 | 2026-11-21T01:05:27.988446+00:00 | Not calibrated | WEAK 20/100 | EXTREME 87/100 | Do nothing | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | PEARL/USD | 59.114 | 1.8755 | -1.19% | 1.11x |
| 2 | AKE/USD | 49.658 | 0.00619423 | +0.61% | 0.79x |
| 3 | PUMP/USD | 47.967 | 0.002432 | +0.33% | 5.21x |
| 4 | BLUR/USD | 37.725 | 0.00743 | +0.95% | 1.55x |
| 5 | CC/USD | 36.499 | 0.07483 | +0.01% | 3.77x |
| 6 | KAS/USD | 35.553 | 0.02609 | +0.19% | 12.43x |
| 7 | CAP/USD | 35.339 | 0.092282 | +0.21% | 1.25x |
| 8 | PIEVERSE/USD | 34.379 | 3.035 | +0.76% | 8.18x |
| 9 | DCR/USD | 29.618 | 10.146 | -0.13% | 0.75x |
| 10 | CT/USD | 23.645 | 0.1218 | +0.08% | 0.64x |
| 11 | TRAC/USD | 21.551 | 0.2707 | +0.33% | 1.21x |

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

- Persisted scans: 1052; predictions: 8428; observations: 635976.
- Matured sampled outcomes across 1/6/24/48h: 10934; gap abstentions: 19110. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 10 (sampled only; not a success-rate estimate).
- False positives / missed movers: NOT VERIFIED without eligible continuous outcome coverage.
- Baseline vs challenger: recorded as-of; unbiased held-out lift NOT MEASURED.
- Online Kraken /USD stablecoin-base pairs excluded: 18 (counted from this scan's online AssetPairs metadata, not inferred from price).
- Stablecoin base exclusions: BRL1, BUSD, DAI, EUR, EURC, EUROP, EURQ, EURR, EURT, FDUSD, FRAX, GUSD, PYUSD, QCAD, RLUSD, TGBP, TUSD, USD, USD1, USDC, USDD, USDE, USDG, USDQ, USDR, USDS, USDT, ZUSD.
- DEX: NOT USED; no DEX freshness gate.
- OHLC screening abstentions: 13; details in immutable scan JSON artifact.
- Storage: ledger and results published in one non-force Git commit and read back. Independent artifact recovery is NOT VERIFIED by this scan alone.
- Errors: none in successful committed scan; a failed workflow must not publish a SUCCESS report.

# Cryptoscanner — challenger and independent legacy-inspired WATCH

Paper only · risk is high or higher · 30%+ in 48h probability NOT CALIBRATED
Signal confidence 0–100 means setup strength only, NOT a win probability. Actions are research guidance; no trade authorization.

**Writer:** 44847933901 · **Generation:** 1052 · **Legacy run:** 44847933901
**Main quote time:** 2026-11-21T01:05:36.932409+00:00 · **Legacy report time:** 2026-11-21T01:06:36.498141+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | PUMP/USD ⭐ | 0.002432 | 64.62 | +0.33% | 5.21x | STRONG 97/100 | HIGH 55/100 | Consider small entry |
| 2 | PEARL/USD | 1.8755 | 54.29 | -1.19% | 1.11x | WEAK 32/100 | VERY_HIGH 78/100 | Do nothing |
| 3 | PIEVERSE/USD ⭐ | 3.035 | 53.16 | +0.76% | 8.18x | STRONG 87/100 | HIGH 66/100 | Consider small entry |
| 4 | CC/USD | 0.07483 | 51.57 | +0.01% | 3.77x | STRONG 71/100 | HIGH 60/100 | Watch |
| 5 | KAS/USD | 0.02609 | 51.51 | +0.19% | 12.43x | MODERATE 66/100 | HIGH 61/100 | Watch |
| 6 | AKE/USD | 0.00619423 | 50.64 | +0.61% | 0.79x | MODERATE 45/100 | VERY_HIGH 74/100 | Watch |
| 7 | BLUR/USD ⭐ | 0.00743 | 47.93 | +0.95% | 1.55x | STRONG 74/100 | HIGH 66/100 | Watch |
| 8 | CAP/USD | 0.092282 | 38.86 | +0.21% | 1.25x | MODERATE 54/100 | HIGH 67/100 | Watch |
| 9 | DCR/USD | 10.146 | 26.46 | -0.13% | 0.75x | WEAK 18/100 | EXTREME 88/100 | Do nothing |
| 10 | TRAC/USD | 0.2707 | 25.34 | +0.33% | 1.21x | WEAK 38/100 | EXTREME 86/100 | Do nothing |
| 11 | CT/USD | 0.1218 | 20.43 | +0.08% | 0.64x | WEAK 20/100 | EXTREME 87/100 | Do nothing |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | PIEVERSE/USD ⭐ | 3.0346 | 49.53 | +0.76% | 8.18x | 2661 | STRONG 85/100 | HIGH 66/100 | Consider small entry |
| 2 | PUMP/USD ⭐ | 0.002432 | 48.11 | +0.33% | 5.21x | 7128 | STRONG 89/100 | HIGH 55/100 | Consider small entry |
| 3 | LTC/USD | 40.62 | 46.78 | +0.10% | 1.71x | 14947 | MODERATE 58/100 | HIGH 55/100 | Watch |
| 4 | BLUR/USD ⭐ | 0.0074 | 39.70 | +0.95% | 1.55x | 2044 | MODERATE 65/100 | VERY_HIGH 72/100 | Watch |

**Same-run overlap:** PUMP/USD, PIEVERSE/USD, BLUR/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
