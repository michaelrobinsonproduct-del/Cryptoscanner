# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-24T14:42:11.837012+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/45416556837
**Source SHA:** 858c8bc8ec5d7641ddb39cacd8aca91719f855b1
**Previous ledger commit:** e08b72818018d2f309f516049d857908ba9dcf90 (atomic ledger/results publication)
**Ledger generation:** 1587 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 4s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 628; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 610; valid market observations: 609; OHLC screened: 13.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | VVV/USD | 25.544 | 90.353 | 81.483 | +4.48% | +0.05% | 1.86x | 9.8 | 2026-11-24T14:42:07.471842+00:00 | Not calibrated | STRONG 80/100 | HIGH 55/100 | Watch | WATCH |
| 2 | NIGHT/USD | 0.04852 | 63.452 | 47.935 | +0.77% | +0.10% | 2.78x | 2.1 | 2026-11-24T14:42:07.471842+00:00 | Not calibrated | STRONG 77/100 | HIGH 55/100 | Watch | WATCH |
| 3 | GBP/USD | 1.311 | 60.296 | 58.858 | +0.59% | +0.10% | 1.09x | 0.6 | 2026-11-24T14:42:07.471842+00:00 | Not calibrated | MODERATE 55/100 | HIGH 62/100 | Watch | WATCH |
| 4 | 2Z/USD | 0.01625 | 59.993 | 54.519 | +3.83% | -0.25% | 1.67x | 6.1 | 2026-11-24T14:42:07.471842+00:00 | Not calibrated | MODERATE 50/100 | VERY_HIGH 73/100 | Watch | WATCH |
| 5 | XMR/USD | 496.84 | 56.228 | 64.943 | +2.23% | -0.25% | 0.26x | 11.3 | 2026-11-24T14:42:07.471842+00:00 | Not calibrated | WEAK 28/100 | VERY_HIGH 82/100 | Do nothing | WATCH |
| 6 | AUD/USD | 0.66535 | 46.544 | 44.253 | +0.42% | +0.06% | 1.20x | 0.6 | 2026-11-24T14:42:07.471842+00:00 | Not calibrated | MODERATE 48/100 | HIGH 62/100 | Watch | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | VVV/USD | 81.483 | 25.544 | +0.05% | 1.86x |
| 2 | XMR/USD | 64.943 | 496.84 | -0.25% | 0.26x |
| 3 | GBP/USD | 58.858 | 1.311 | +0.10% | 1.09x |
| 4 | 2Z/USD | 54.519 | 0.01625 | -0.25% | 1.67x |
| 5 | NIGHT/USD | 47.935 | 0.04852 | +0.10% | 2.78x |
| 6 | AUD/USD | 44.253 | 0.66535 | +0.06% | 1.20x |

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

- Persisted scans: 1587; predictions: 13681; observations: 961578.
- Matured sampled outcomes across 1/6/24/48h: 26947; gap abstentions: 22370. Per-horizon counts require independent audit; do not infer held-out lift.
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

**Writer:** 45416556837 · **Generation:** 1587 · **Legacy run:** 45416556837
**Main quote time:** 2026-11-24T14:42:11.837012+00:00 · **Legacy report time:** 2026-11-24T14:43:23.956015+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | VVV/USD ⭐ | 25.544 | 90.35 | +0.05% | 1.86x | STRONG 90/100 | HIGH 55/100 | Watch |
| 2 | NIGHT/USD ⭐ | 0.04852 | 63.45 | +0.10% | 2.78x | STRONG 87/100 | HIGH 55/100 | Watch |
| 3 | GBP/USD ⭐ | 1.311 | 60.30 | +0.10% | 1.09x | MODERATE 65/100 | HIGH 62/100 | Watch |
| 4 | 2Z/USD | 0.01625 | 59.99 | -0.25% | 1.67x | MODERATE 50/100 | VERY_HIGH 73/100 | Watch |
| 5 | XMR/USD | 496.84 | 56.23 | -0.25% | 0.26x | WEAK 28/100 | VERY_HIGH 82/100 | Do nothing |
| 6 | AUD/USD ⭐ | 0.66535 | 46.54 | +0.06% | 1.20x | MODERATE 58/100 | HIGH 62/100 | Watch |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | VVV/USD ⭐ | 25.544 | 88.60 | +0.05% | 1.86x | 12913 | STRONG 89/100 | HIGH 55/100 | Watch |
| 2 | GBP/USD ⭐ | 1.31101 | 58.75 | +0.10% | 1.09x | 21026 | MODERATE 64/100 | HIGH 62/100 | Watch |
| 3 | NIGHT/USD ⭐ | 0.0485 | 57.16 | +0.10% | 2.78x | 10495 | STRONG 84/100 | HIGH 55/100 | Watch |
| 4 | AUD/USD ⭐ | 0.66535 | 49.06 | +0.06% | 1.20x | 4038 | MODERATE 60/100 | HIGH 62/100 | Watch |
| 5 | BAT/USD | 0.07726 | 25.55 | +0.12% | 1.07x | 4020 | WEAK 28/100 | VERY_HIGH 79/100 | Do nothing |

**Same-run overlap:** VVV/USD, NIGHT/USD, GBP/USD, AUD/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
