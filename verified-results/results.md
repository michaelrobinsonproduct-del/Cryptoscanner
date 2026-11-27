# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-27T17:02:19.744043+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/46038177515
**Source SHA:** 858c8bc8ec5d7641ddb39cacd8aca91719f855b1
**Previous ledger commit:** eb3408021d7ca180a75e860329957d1792e7588b (atomic ledger/results publication)
**Ledger generation:** 2035 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 8s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 628; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 610; valid market observations: 605; OHLC screened: 24.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | ZEC/USD | 747.64 | 106.120 | 96.122 | +9.68% | -1.00% | 7.49x | 7.8 | 2026-11-27T17:02:11.853525+00:00 | Not calibrated | STRONG 80/100 | HIGH 65/100 | Watch | WATCH |
| 2 | HYPE/USD | 64.45 | 76.514 | 78.536 | +3.58% | -0.42% | 1.01x | 3.1 | 2026-11-27T17:02:11.853525+00:00 | Not calibrated | MODERATE 48/100 | HIGH 68/100 | Watch | WATCH |
| 3 | SPACE/USD | 0.004169 | 76.466 | 70.946 | +7.67% | +0.65% | 1.23x | 9.6 | 2026-11-27T17:02:11.853525+00:00 | Not calibrated | STRONG 73/100 | VERY_HIGH 74/100 | Watch | WATCH |
| 4 | PAXG/USD | 3619.64 | 70.076 | 54.628 | +1.77% | +0.09% | 19.06x | 1.8 | 2026-11-27T17:02:11.853525+00:00 | Not calibrated | STRONG 80/100 | HIGH 55/100 | Watch | WATCH |
| 5 | XAUT/USD | 3621.7 | 64.728 | 48.926 | +1.74% | +0.16% | 6.43x | 1.1 | 2026-11-27T17:02:11.853525+00:00 | Not calibrated | STRONG 77/100 | HIGH 55/100 | Watch | WATCH |
| 6 | MELANIA/USD | 0.0504 | 64.600 | 65.889 | +7.69% | -0.59% | 1.17x | 19.9 | 2026-11-27T17:02:11.853525+00:00 | Not calibrated | WEAK 37/100 | EXTREME 86/100 | Do nothing | WATCH |
| 7 | NIGHT/USD | 0.04944 | 64.368 | 66.388 | +2.00% | -0.52% | 1.06x | 4.0 | 2026-11-27T17:02:11.853525+00:00 | Not calibrated | WEAK 42/100 | HIGH 68/100 | Watch | WATCH |
| 8 | TAO/USD | 184.7452 | 62.907 | 52.347 | +0.52% | -0.13% | 2.12x | 5.2 | 2026-11-27T17:02:11.853525+00:00 | Not calibrated | MODERATE 61/100 | HIGH 61/100 | Watch | WATCH |
| 9 | LINK/USD | 9.31497 | 62.741 | 55.825 | +0.50% | -0.22% | 1.80x | 5.4 | 2026-11-27T17:02:11.853525+00:00 | Not calibrated | MODERATE 51/100 | HIGH 61/100 | Watch | WATCH |
| 10 | XDG/USD | 0.0575627 | 62.450 | 69.241 | +2.11% | -0.26% | 0.45x | 1.0 | 2026-11-27T17:02:11.853525+00:00 | Not calibrated | WEAK 36/100 | VERY_HIGH 76/100 | Watch | WATCH |
| 11 | SOL/USD | 72.06 | 60.317 | 65.358 | +1.58% | -0.22% | 0.61x | 1.4 | 2026-11-27T17:02:11.853525+00:00 | Not calibrated | WEAK 35/100 | VERY_HIGH 76/100 | Watch | WATCH |
| 12 | UNI/USD | 4.7569 | 60.127 | 65.385 | +2.30% | -0.45% | 0.70x | 6.1 | 2026-11-27T17:02:11.853525+00:00 | Not calibrated | WEAK 35/100 | VERY_HIGH 76/100 | Watch | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | ZEC/USD | 96.122 | 747.64 | -1.00% | 7.49x |
| 2 | HYPE/USD | 78.536 | 64.45 | -0.42% | 1.01x |
| 3 | SPACE/USD | 70.946 | 0.004169 | +0.65% | 1.23x |
| 4 | XDG/USD | 69.241 | 0.0575627 | -0.26% | 0.45x |
| 5 | NIGHT/USD | 66.388 | 0.04944 | -0.52% | 1.06x |
| 6 | MELANIA/USD | 65.889 | 0.0504 | -0.59% | 1.17x |
| 7 | UNI/USD | 65.385 | 4.7569 | -0.45% | 0.70x |
| 8 | SOL/USD | 65.358 | 72.06 | -0.22% | 0.61x |
| 9 | LINK/USD | 55.825 | 9.31497 | -0.22% | 1.80x |
| 10 | PAXG/USD | 54.628 | 3619.64 | +0.09% | 19.06x |
| 11 | TAO/USD | 52.347 | 184.7452 | -0.13% | 2.12x |
| 12 | XAUT/USD | 48.926 | 3621.7 | +0.16% | 6.43x |

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

- Persisted scans: 2035; predictions: 18122; observations: 1232284.
- Matured sampled outcomes across 1/6/24/48h: 40589; gap abstentions: 25968. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 153 (sampled only; not a success-rate estimate).
- False positives / missed movers: NOT VERIFIED without eligible continuous outcome coverage.
- Baseline vs challenger: recorded as-of; unbiased held-out lift NOT MEASURED.
- Online Kraken /USD stablecoin-base pairs excluded: 18 (counted from this scan's online AssetPairs metadata, not inferred from price).
- Stablecoin base exclusions: BRL1, BUSD, DAI, EUR, EURC, EUROP, EURQ, EURR, EURT, FDUSD, FRAX, GUSD, PYUSD, QCAD, RLUSD, TGBP, TUSD, USD, USD1, USDC, USDD, USDE, USDG, USDQ, USDR, USDS, USDT, ZUSD.
- DEX: NOT USED; no DEX freshness gate.
- OHLC screening abstentions: 4; details in immutable scan JSON artifact.
- Storage: ledger and results published in one non-force Git commit and read back. Independent artifact recovery is NOT VERIFIED by this scan alone.
- Errors: none in successful committed scan; a failed workflow must not publish a SUCCESS report.

# Cryptoscanner — challenger and independent legacy-inspired WATCH

Paper only · risk is high or higher · 30%+ in 48h probability NOT CALIBRATED
Signal confidence 0–100 means setup strength only, NOT a win probability. Actions are research guidance; no trade authorization.

**Writer:** 46038177515 · **Generation:** 2035 · **Legacy run:** 46038177515
**Main quote time:** 2026-11-27T17:02:19.744043+00:00 · **Legacy report time:** 2026-11-27T17:03:05.114727+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | ZEC/USD | 747.64 | 106.12 | -1.00% | 7.49x | STRONG 80/100 | HIGH 65/100 | Watch |
| 2 | HYPE/USD | 64.45 | 76.51 | -0.42% | 1.01x | MODERATE 48/100 | HIGH 68/100 | Watch |
| 3 | SPACE/USD ⭐ | 0.004169 | 76.47 | +0.65% | 1.23x | STRONG 83/100 | VERY_HIGH 74/100 | Watch |
| 4 | PAXG/USD ⭐ | 3619.64 | 70.08 | +0.09% | 19.06x | STRONG 90/100 | HIGH 55/100 | Watch |
| 5 | XAUT/USD | 3621.7 | 64.73 | +0.16% | 6.43x | STRONG 77/100 | HIGH 55/100 | Watch |
| 6 | MELANIA/USD | 0.0504 | 64.60 | -0.59% | 1.17x | WEAK 37/100 | EXTREME 86/100 | Do nothing |
| 7 | NIGHT/USD | 0.04944 | 64.37 | -0.52% | 1.06x | WEAK 42/100 | HIGH 68/100 | Watch |
| 8 | TAO/USD | 184.7452 | 62.91 | -0.13% | 2.12x | MODERATE 61/100 | HIGH 61/100 | Watch |
| 9 | LINK/USD | 9.31497 | 62.74 | -0.22% | 1.80x | MODERATE 51/100 | HIGH 61/100 | Watch |
| 10 | XDG/USD | 0.0575627 | 62.45 | -0.26% | 0.45x | WEAK 36/100 | VERY_HIGH 76/100 | Watch |
| 11 | SOL/USD | 72.06 | 60.32 | -0.22% | 0.61x | WEAK 35/100 | VERY_HIGH 76/100 | Watch |
| 12 | UNI/USD | 4.7569 | 60.13 | -0.45% | 0.70x | WEAK 35/100 | VERY_HIGH 76/100 | Watch |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | PAXG/USD ⭐ | 3617.77 | 72.30 | +0.09% | 19.06x | 4364 | STRONG 91/100 | HIGH 55/100 | Watch |
| 2 | SPACE/USD ⭐ | 0.004173 | 71.77 | +0.65% | 1.23x | 2456 | STRONG 81/100 | VERY_HIGH 74/100 | Watch |

**Same-run overlap:** SPACE/USD, PAXG/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
