# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-24T01:01:52.604427+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/45301569881
**Source SHA:** 858c8bc8ec5d7641ddb39cacd8aca91719f855b1
**Previous ledger commit:** b6ee72a408a225d6e032d80a5987636312304980 (atomic ledger/results publication)
**Ledger generation:** 1504 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 6s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 628; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 610; valid market observations: 608; OHLC screened: 24.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | LINK/USD | 9.0526 | 70.396 | 56.745 | +0.53% | -0.27% | 13.52x | 3.9 | 2026-11-24T01:01:46.309654+00:00 | Not calibrated | MODERATE 65/100 | HIGH 61/100 | Watch | WATCH |
| 2 | VVV/USD | 24.948 | 66.353 | 61.290 | +2.05% | +0.49% | 1.26x | 16.1 | 2026-11-24T01:01:46.309654+00:00 | Not calibrated | MODERATE 63/100 | HIGH 61/100 | Watch | WATCH |
| 3 | XDG/USD | 0.0564956 | 65.790 | 56.847 | +0.34% | -0.11% | 1.95x | 1.0 | 2026-11-24T01:01:46.309654+00:00 | Not calibrated | MODERATE 53/100 | HIGH 61/100 | Watch | WATCH |
| 4 | SOL/USD | 72.2 | 59.640 | 56.935 | +0.38% | +0.03% | 1.26x | 1.4 | 2026-11-24T01:01:46.309654+00:00 | Not calibrated | MODERATE 55/100 | HIGH 55/100 | Watch | WATCH |
| 5 | XLM/USD | 0.131354 | 59.282 | 59.010 | +1.05% | -0.26% | 1.16x | 6.6 | 2026-11-24T01:01:46.309654+00:00 | Not calibrated | WEAK 40/100 | HIGH 68/100 | Watch | WATCH |
| 6 | XRP/USD | 0.94387 | 58.332 | 57.703 | +0.48% | -0.12% | 1.12x | 1.3 | 2026-11-24T01:01:46.309654+00:00 | Not calibrated | WEAK 39/100 | HIGH 68/100 | Watch | WATCH |
| 7 | PAXG/USD | 3646.58 | 56.606 | 52.746 | +0.71% | +0.26% | 1.26x | 2.2 | 2026-11-24T01:01:46.309654+00:00 | Not calibrated | MODERATE 63/100 | HIGH 55/100 | Watch | WATCH |
| 8 | QNT/USD | 155.54 | 56.295 | 58.186 | +0.96% | +0.28% | 0.67x | 7.1 | 2026-11-24T01:01:46.309654+00:00 | Not calibrated | MODERATE 58/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 9 | XAUT/USD | 3648.2 | 54.793 | 38.490 | +0.80% | +0.26% | 2.85x | 1.1 | 2026-11-24T01:01:46.309654+00:00 | Not calibrated | STRONG 82/100 | HIGH 60/100 | Watch | WATCH |
| 10 | LTC/USD | 41.58 | 54.698 | 56.502 | +0.39% | -0.31% | 0.98x | 2.4 | 2026-11-24T01:01:46.309654+00:00 | Not calibrated | WEAK 32/100 | HIGH 68/100 | Do nothing | WATCH |
| 11 | HYPE/USD | 63.85 | 54.135 | 55.746 | +0.33% | +0.19% | 0.74x | 3.1 | 2026-11-24T01:01:46.309654+00:00 | Not calibrated | MODERATE 47/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 12 | ADA/USD | 0.148983 | 53.761 | 55.180 | +0.36% | -0.29% | 1.01x | 4.7 | 2026-11-24T01:01:46.309654+00:00 | Not calibrated | WEAK 37/100 | HIGH 68/100 | Watch | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | VVV/USD | 61.290 | 24.948 | +0.49% | 1.26x |
| 2 | XLM/USD | 59.010 | 0.131354 | -0.26% | 1.16x |
| 3 | QNT/USD | 58.186 | 155.54 | +0.28% | 0.67x |
| 4 | XRP/USD | 57.703 | 0.94387 | -0.12% | 1.12x |
| 5 | SOL/USD | 56.935 | 72.2 | +0.03% | 1.26x |
| 6 | XDG/USD | 56.847 | 0.0564956 | -0.11% | 1.95x |
| 7 | LINK/USD | 56.745 | 9.0526 | -0.27% | 13.52x |
| 8 | LTC/USD | 56.502 | 41.58 | -0.31% | 0.98x |
| 9 | HYPE/USD | 55.746 | 63.85 | +0.19% | 0.74x |
| 10 | ADA/USD | 55.180 | 0.148983 | -0.29% | 1.01x |
| 11 | PAXG/USD | 52.746 | 3646.58 | +0.26% | 1.26x |
| 12 | XAUT/USD | 38.490 | 3648.2 | +0.26% | 2.85x |

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

- Persisted scans: 1504; predictions: 12805; observations: 911037.
- Matured sampled outcomes across 1/6/24/48h: 23571; gap abstentions: 22370. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 132 (sampled only; not a success-rate estimate).
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

**Writer:** 45301569881 · **Generation:** 1504 · **Legacy run:** 45301569881
**Main quote time:** 2026-11-24T01:01:52.604427+00:00 · **Legacy report time:** 2026-11-24T01:03:01.320858+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | LINK/USD | 9.0526 | 70.40 | -0.27% | 13.52x | MODERATE 65/100 | HIGH 61/100 | Watch |
| 2 | VVV/USD ⭐ | 24.948 | 66.35 | +0.49% | 1.26x | STRONG 73/100 | HIGH 61/100 | Watch |
| 3 | XDG/USD | 0.0564956 | 65.79 | -0.11% | 1.95x | MODERATE 53/100 | HIGH 61/100 | Watch |
| 4 | SOL/USD | 72.2 | 59.64 | +0.03% | 1.26x | MODERATE 55/100 | HIGH 55/100 | Watch |
| 5 | XLM/USD | 0.131354 | 59.28 | -0.26% | 1.16x | WEAK 40/100 | HIGH 68/100 | Watch |
| 6 | XRP/USD | 0.94387 | 58.33 | -0.12% | 1.12x | WEAK 39/100 | HIGH 68/100 | Watch |
| 7 | PAXG/USD ⭐ | 3646.58 | 56.61 | +0.26% | 1.26x | STRONG 73/100 | HIGH 55/100 | Watch |
| 8 | QNT/USD | 155.54 | 56.30 | +0.28% | 0.67x | MODERATE 58/100 | VERY_HIGH 70/100 | Watch |
| 9 | XAUT/USD | 3648.2 | 54.79 | +0.26% | 2.85x | STRONG 82/100 | HIGH 60/100 | Watch |
| 10 | LTC/USD | 41.58 | 54.70 | -0.31% | 0.98x | WEAK 32/100 | HIGH 68/100 | Do nothing |
| 11 | HYPE/USD | 63.85 | 54.14 | +0.19% | 0.74x | MODERATE 47/100 | VERY_HIGH 70/100 | Watch |
| 12 | ADA/USD | 0.148983 | 53.76 | -0.29% | 1.01x | WEAK 37/100 | HIGH 68/100 | Watch |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | VVV/USD ⭐ | 24.86 | 59.73 | +0.49% | 1.26x | 13774 | STRONG 70/100 | HIGH 61/100 | Watch |
| 2 | PAXG/USD ⭐ | 3650.5 | 56.75 | +0.26% | 1.26x | 6054 | STRONG 73/100 | HIGH 55/100 | Watch |

**Same-run overlap:** VVV/USD, PAXG/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
