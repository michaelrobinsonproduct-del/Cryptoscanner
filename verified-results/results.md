# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-21T01:45:35.072898+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/44851950342
**Source SHA:** bdc7e68f7fa75fae6636b7738d52f10a65d92038
**Previous ledger commit:** 13aa667f81580a9fe5ad35c18637c6d116714501 (atomic ledger/results publication)
**Ledger generation:** 1057 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 9s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 628; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 610; valid market observations: 608; OHLC screened: 24.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | VVV/USD | 21.161 | 81.548 | 66.170 | +2.03% | +0.08% | 5.13x | 6.1 | 2026-11-21T01:45:26.122038+00:00 | Not calibrated | STRONG 86/100 | HIGH 55/100 | Watch | WATCH |
| 2 | BLESS/USD | 0.014322 | 49.021 | 46.562 | +3.99% | +1.89% | 0.30x | 34.2 | 2026-11-21T01:45:26.122038+00:00 | Not calibrated | MODERATE 45/100 | EXTREME 87/100 | Do nothing | WATCH |
| 3 | DOT/USD | 0.6631 | 44.228 | 36.014 | +0.32% | +0.50% | 1.57x | 1.5 | 2026-11-21T01:45:26.122038+00:00 | Not calibrated | MODERATE 67/100 | HIGH 60/100 | Watch | WATCH |
| 4 | MEGA/USD | 0.04814 | 40.221 | 28.385 | +0.63% | +1.50% | 1.44x | 16.6 | 2026-11-21T01:45:26.122038+00:00 | Not calibrated | MODERATE 60/100 | HIGH 66/100 | Watch | WATCH |
| 5 | SKY/USD | 0.04422 | 37.542 | 37.339 | +0.87% | +0.09% | 0.97x | 9.0 | 2026-11-21T01:45:26.122038+00:00 | Not calibrated | WEAK 39/100 | HIGH 67/100 | Watch | WATCH |
| 6 | DCR/USD | 10.159 | 31.839 | 32.992 | +0.53% | -0.25% | 1.01x | 3.0 | 2026-11-21T01:45:26.122038+00:00 | Not calibrated | WEAK 26/100 | VERY_HIGH 80/100 | Do nothing | WATCH |
| 7 | CT/USD | 0.123 | 31.393 | 34.808 | +1.57% | +0.57% | 0.37x | 16.2 | 2026-11-21T01:45:26.122038+00:00 | Not calibrated | WEAK 41/100 | VERY_HIGH 81/100 | Watch | WATCH |
| 8 | PYTH/USD | 0.04845 | 26.137 | 28.670 | +0.71% | +0.19% | 0.65x | 16.5 | 2026-11-21T01:45:26.122038+00:00 | Not calibrated | WEAK 28/100 | VERY_HIGH 81/100 | Do nothing | WATCH |
| 9 | BLUR/USD | 0.00733 | 13.925 | 21.165 | +0.41% | -0.41% | 0.48x | 27.4 | 2026-11-21T01:45:26.122038+00:00 | Not calibrated | WEAK 2/100 | EXTREME 93/100 | Do nothing | WATCH |
| 10 | PIEVERSE/USD | 3.0168 | 13.219 | 26.558 | +0.60% | -1.28% | 0.31x | 25.0 | 2026-11-21T01:45:26.122038+00:00 | Not calibrated | WEAK 2/100 | EXTREME 97/100 | Do nothing | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | VVV/USD | 66.170 | 21.161 | +0.08% | 5.13x |
| 2 | BLESS/USD | 46.562 | 0.014322 | +1.89% | 0.30x |
| 3 | SKY/USD | 37.339 | 0.04422 | +0.09% | 0.97x |
| 4 | DOT/USD | 36.014 | 0.6631 | +0.50% | 1.57x |
| 5 | CT/USD | 34.808 | 0.123 | +0.57% | 0.37x |
| 6 | DCR/USD | 32.992 | 10.159 | -0.25% | 1.01x |
| 7 | PYTH/USD | 28.670 | 0.04845 | +0.19% | 0.65x |
| 8 | MEGA/USD | 28.385 | 0.04814 | +1.50% | 1.44x |
| 9 | PIEVERSE/USD | 26.558 | 3.0168 | -1.28% | 0.31x |
| 10 | BLUR/USD | 21.165 | 0.00733 | -0.41% | 0.48x |

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

- Persisted scans: 1057; predictions: 8477; observations: 639016.
- Matured sampled outcomes across 1/6/24/48h: 10941; gap abstentions: 19255. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 10 (sampled only; not a success-rate estimate).
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

**Writer:** 44851950342 · **Generation:** 1057 · **Legacy run:** 44851950342
**Main quote time:** 2026-11-21T01:45:35.072898+00:00 · **Legacy report time:** 2026-11-21T01:46:36.615511+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | VVV/USD ⭐ | 21.161 | 81.55 | +0.08% | 5.13x | STRONG 96/100 | HIGH 55/100 | Watch |
| 2 | BLESS/USD | 0.014322 | 49.02 | +1.89% | 0.30x | MODERATE 45/100 | EXTREME 87/100 | Do nothing |
| 3 | DOT/USD ⭐ | 0.6631 | 44.23 | +0.50% | 1.57x | STRONG 77/100 | HIGH 60/100 | Consider small entry |
| 4 | MEGA/USD | 0.04814 | 40.22 | +1.50% | 1.44x | MODERATE 60/100 | HIGH 66/100 | Watch |
| 5 | SKY/USD | 0.04422 | 37.54 | +0.09% | 0.97x | WEAK 39/100 | HIGH 67/100 | Watch |
| 6 | DCR/USD | 10.159 | 31.84 | -0.25% | 1.01x | WEAK 26/100 | VERY_HIGH 80/100 | Do nothing |
| 7 | CT/USD | 0.123 | 31.39 | +0.57% | 0.37x | WEAK 41/100 | VERY_HIGH 81/100 | Watch |
| 8 | PYTH/USD | 0.04845 | 26.14 | +0.19% | 0.65x | WEAK 28/100 | VERY_HIGH 81/100 | Do nothing |
| 9 | BLUR/USD | 0.00733 | 13.93 | -0.41% | 0.48x | WEAK 2/100 | EXTREME 93/100 | Do nothing |
| 10 | PIEVERSE/USD | 3.0168 | 13.22 | -1.28% | 0.31x | WEAK 2/100 | EXTREME 97/100 | Do nothing |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | VVV/USD ⭐ | 21.208 | 73.19 | +0.08% | 5.13x | 11735 | STRONG 92/100 | HIGH 55/100 | Watch |
| 2 | XDG/USD | 0.0543852 | 55.39 | +0.08% | 1.55x | 12428 | MODERATE 63/100 | HIGH 55/100 | Watch |
| 3 | UNI/USD | 4.4772 | 51.32 | +0.23% | 3.33x | 9220 | STRONG 81/100 | HIGH 55/100 | Watch |
| 4 | ADA/USD | 0.143136 | 49.65 | +0.30% | 1.30x | 17494 | STRONG 70/100 | HIGH 55/100 | Watch |
| 5 | DOT/USD ⭐ | 0.6632 | 44.49 | +0.50% | 1.57x | 11599 | STRONG 77/100 | HIGH 60/100 | Consider small entry |

**Same-run overlap:** VVV/USD, DOT/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
