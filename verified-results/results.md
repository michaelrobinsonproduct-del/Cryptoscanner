# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-21T01:48:26.155614+00:00
**GitHub trigger:** scheduled (verified event=schedule; originating cron=2,7,12,17,22,27,32,37,42,47,52,57 * * * *, intended UTC minute=2,7,12,17,22,27,32,37,42,47,52,57; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/44852214799
**Source SHA:** bdc7e68f7fa75fae6636b7738d52f10a65d92038
**Previous ledger commit:** 83dba3856db9fa7d07cf717e78a92cff280a4beb (atomic ledger/results publication)
**Ledger generation:** 1058 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 7s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 628; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 610; valid market observations: 608; OHLC screened: 24.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | VVV/USD | 21.242 | 82.888 | 67.510 | +2.43% | +0.08% | 5.13x | 8.9 | 2026-11-21T01:48:19.267771+00:00 | Not calibrated | STRONG 86/100 | HIGH 55/100 | Watch | WATCH |
| 2 | XDG/USD | 0.0544263 | 62.124 | 56.189 | +0.28% | +0.08% | 1.55x | 1.5 | 2026-11-21T01:48:19.267771+00:00 | Not calibrated | MODERATE 66/100 | HIGH 55/100 | Watch | WATCH |
| 3 | ADA/USD | 0.143261 | 59.391 | 54.885 | +0.29% | +0.30% | 1.30x | 4.3 | 2026-11-21T01:48:19.267771+00:00 | Not calibrated | STRONG 75/100 | HIGH 55/100 | Watch | WATCH |
| 4 | DOT/USD | 0.6642 | 42.388 | 34.174 | +0.48% | +0.50% | 1.57x | 7.5 | 2026-11-21T01:48:19.267771+00:00 | Not calibrated | MODERATE 66/100 | HIGH 60/100 | Watch | WATCH |
| 5 | MEGA/USD | 0.04819 | 40.962 | 29.126 | +0.73% | +1.50% | 1.44x | 16.6 | 2026-11-21T01:48:19.267771+00:00 | Not calibrated | MODERATE 60/100 | HIGH 66/100 | Watch | WATCH |
| 6 | SKY/USD | 0.04422 | 37.533 | 37.330 | +0.87% | +0.09% | 0.97x | 9.1 | 2026-11-21T01:48:19.267771+00:00 | Not calibrated | WEAK 39/100 | HIGH 67/100 | Watch | WATCH |
| 7 | DCR/USD | 10.148 | 30.091 | 31.244 | +0.43% | -0.25% | 1.01x | 4.9 | 2026-11-21T01:48:19.267771+00:00 | Not calibrated | WEAK 25/100 | VERY_HIGH 80/100 | Do nothing | WATCH |
| 8 | CC/USD | 0.07478 | 29.955 | 34.634 | +0.31% | +0.13% | 0.47x | 8.0 | 2026-11-21T01:48:19.267771+00:00 | Not calibrated | WEAK 35/100 | VERY_HIGH 75/100 | Watch | WATCH |
| 9 | PYTH/USD | 0.04859 | 29.218 | 31.752 | +1.00% | +0.19% | 0.65x | 14.4 | 2026-11-21T01:48:19.267771+00:00 | Not calibrated | WEAK 30/100 | VERY_HIGH 81/100 | Do nothing | WATCH |
| 10 | BLUR/USD | 0.00736 | 16.847 | 24.087 | +0.82% | -0.41% | 0.48x | 27.3 | 2026-11-21T01:48:19.267771+00:00 | Not calibrated | WEAK 3/100 | EXTREME 93/100 | Do nothing | WATCH |
| 11 | PIEVERSE/USD | 3.0168 | 10.397 | 23.735 | +0.60% | -1.28% | 0.31x | 30.6 | 2026-11-21T01:48:19.267771+00:00 | Not calibrated | WEAK 0/100 | EXTREME 97/100 | Do nothing | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | VVV/USD | 67.510 | 21.242 | +0.08% | 5.13x |
| 2 | XDG/USD | 56.189 | 0.0544263 | +0.08% | 1.55x |
| 3 | ADA/USD | 54.885 | 0.143261 | +0.30% | 1.30x |
| 4 | SKY/USD | 37.330 | 0.04422 | +0.09% | 0.97x |
| 5 | CC/USD | 34.634 | 0.07478 | +0.13% | 0.47x |
| 6 | DOT/USD | 34.174 | 0.6642 | +0.50% | 1.57x |
| 7 | PYTH/USD | 31.752 | 0.04859 | +0.19% | 0.65x |
| 8 | DCR/USD | 31.244 | 10.148 | -0.25% | 1.01x |
| 9 | MEGA/USD | 29.126 | 0.04819 | +1.50% | 1.44x |
| 10 | BLUR/USD | 24.087 | 0.00736 | -0.41% | 0.48x |
| 11 | PIEVERSE/USD | 23.735 | 3.0168 | -1.28% | 0.31x |

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

- Persisted scans: 1058; predictions: 8488; observations: 639624.
- Matured sampled outcomes across 1/6/24/48h: 10942; gap abstentions: 19255. Per-horizon counts require independent audit; do not infer held-out lift.
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

**Writer:** 44852214799 · **Generation:** 1058 · **Legacy run:** 44852214799
**Main quote time:** 2026-11-21T01:48:26.155614+00:00 · **Legacy report time:** 2026-11-21T01:49:28.952874+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | VVV/USD ⭐ | 21.242 | 82.89 | +0.08% | 5.13x | STRONG 96/100 | HIGH 55/100 | Watch |
| 2 | XDG/USD ⭐ | 0.0544263 | 62.12 | +0.08% | 1.55x | STRONG 76/100 | HIGH 55/100 | Watch |
| 3 | ADA/USD ⭐ | 0.143261 | 59.39 | +0.30% | 1.30x | STRONG 85/100 | HIGH 55/100 | Watch |
| 4 | DOT/USD ⭐ | 0.6642 | 42.39 | +0.50% | 1.57x | STRONG 76/100 | HIGH 60/100 | Consider small entry |
| 5 | MEGA/USD | 0.04819 | 40.96 | +1.50% | 1.44x | MODERATE 60/100 | HIGH 66/100 | Watch |
| 6 | SKY/USD | 0.04422 | 37.53 | +0.09% | 0.97x | WEAK 39/100 | HIGH 67/100 | Watch |
| 7 | DCR/USD | 10.148 | 30.09 | -0.25% | 1.01x | WEAK 25/100 | VERY_HIGH 80/100 | Do nothing |
| 8 | CC/USD | 0.07478 | 29.95 | +0.13% | 0.47x | WEAK 35/100 | VERY_HIGH 75/100 | Watch |
| 9 | PYTH/USD | 0.04859 | 29.22 | +0.19% | 0.65x | WEAK 30/100 | VERY_HIGH 81/100 | Do nothing |
| 10 | BLUR/USD | 0.00736 | 16.85 | -0.41% | 0.48x | WEAK 3/100 | EXTREME 93/100 | Do nothing |
| 11 | PIEVERSE/USD | 3.0168 | 10.40 | -1.28% | 0.31x | WEAK 0/100 | EXTREME 97/100 | Do nothing |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | VVV/USD ⭐ | 21.277 | 78.19 | +0.08% | 5.13x | 11730 | STRONG 94/100 | HIGH 55/100 | Watch |
| 2 | XDG/USD ⭐ | 0.0544404 | 56.06 | +0.08% | 1.55x | 12427 | STRONG 73/100 | HIGH 55/100 | Watch |
| 3 | SOL/USD | 68.79 | 55.47 | +0.16% | 2.12x | 44159 | STRONG 73/100 | HIGH 55/100 | Watch |
| 4 | ADA/USD ⭐ | 0.143351 | 48.96 | +0.30% | 1.30x | 17490 | STRONG 79/100 | HIGH 55/100 | Watch |
| 5 | UNI/USD | 4.4783 | 48.50 | +0.23% | 3.33x | 9218 | STRONG 79/100 | HIGH 55/100 | Watch |
| 6 | DOT/USD ⭐ | 0.665 | 47.77 | +0.50% | 1.57x | 11585 | STRONG 79/100 | HIGH 60/100 | Consider small entry |

**Same-run overlap:** VVV/USD, XDG/USD, ADA/USD, DOT/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
