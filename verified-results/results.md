# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-27T16:32:10.961946+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/46034057908
**Source SHA:** 858c8bc8ec5d7641ddb39cacd8aca91719f855b1
**Previous ledger commit:** 570d8f5ae67ee3b7f6b7761aa788925807ffd3df (atomic ledger/results publication)
**Ledger generation:** 2032 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 8s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 628; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 610; valid market observations: 605; OHLC screened: 24.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | ZEC/USD | 738.98 | 89.064 | 96.075 | +8.41% | +0.19% | 0.20x | 7.9 | 2026-11-27T16:32:03.022747+00:00 | Not calibrated | MODERATE 65/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 2 | HYPE/USD | 64.39 | 87.561 | 77.858 | +3.49% | +0.16% | 1.89x | 3.1 | 2026-11-27T16:32:03.022747+00:00 | Not calibrated | STRONG 79/100 | HIGH 55/100 | Watch | WATCH |
| 3 | SPACE/USD | 0.004126 | 70.164 | 72.070 | +6.56% | +0.10% | 0.76x | 7.3 | 2026-11-27T16:32:03.022747+00:00 | Not calibrated | MODERATE 55/100 | VERY_HIGH 74/100 | Watch | WATCH |
| 4 | UNI/USD | 4.7454 | 63.499 | 66.333 | +2.05% | +0.18% | 0.63x | 2.5 | 2026-11-27T16:32:03.022747+00:00 | Not calibrated | MODERATE 52/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 5 | XDG/USD | 0.0574055 | 59.898 | 67.149 | +1.83% | -0.14% | 0.35x | 1.3 | 2026-11-27T16:32:03.022747+00:00 | Not calibrated | WEAK 35/100 | VERY_HIGH 76/100 | Watch | WATCH |
| 6 | SOL/USD | 71.95 | 59.831 | 64.271 | +1.42% | -0.24% | 0.67x | 1.4 | 2026-11-27T16:32:03.022747+00:00 | Not calibrated | WEAK 35/100 | VERY_HIGH 76/100 | Watch | WATCH |
| 7 | NIGHT/USD | 0.04911 | 56.730 | 59.246 | +1.32% | +1.09% | 0.20x | 8.1 | 2026-11-27T16:32:03.022747+00:00 | Not calibrated | MODERATE 58/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 8 | VVV/USD | 26.736 | 54.154 | 61.572 | +2.11% | -0.40% | 0.46x | 7.5 | 2026-11-27T16:32:03.022747+00:00 | Not calibrated | WEAK 32/100 | VERY_HIGH 76/100 | Do nothing | WATCH |
| 9 | MELANIA/USD | 0.0507 | 49.120 | 56.067 | +8.33% | +0.00% | 0.31x | 39.5 | 2026-11-27T16:32:03.022747+00:00 | Not calibrated | WEAK 30/100 | EXTREME 94/100 | Do nothing | WATCH |
| 10 | STRK/USD | 0.03107 | 48.790 | 33.308 | +0.52% | +0.10% | 7.72x | 3.2 | 2026-11-27T16:32:03.022747+00:00 | Not calibrated | MODERATE 69/100 | HIGH 67/100 | Watch | WATCH |
| 11 | PENGU/USD | 0.004421 | 48.410 | 34.425 | +0.89% | -0.20% | 4.27x | 6.8 | 2026-11-27T16:32:03.022747+00:00 | Not calibrated | MODERATE 54/100 | VERY_HIGH 73/100 | Watch | WATCH |
| 12 | CAP/USD | 0.092933 | 47.856 | 31.123 | +0.34% | +0.35% | 2.82x | 6.1 | 2026-11-27T16:32:03.022747+00:00 | Not calibrated | STRONG 79/100 | HIGH 60/100 | Watch | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | ZEC/USD | 96.075 | 738.98 | +0.19% | 0.20x |
| 2 | HYPE/USD | 77.858 | 64.39 | +0.16% | 1.89x |
| 3 | SPACE/USD | 72.070 | 0.004126 | +0.10% | 0.76x |
| 4 | XDG/USD | 67.149 | 0.0574055 | -0.14% | 0.35x |
| 5 | UNI/USD | 66.333 | 4.7454 | +0.18% | 0.63x |
| 6 | SOL/USD | 64.271 | 71.95 | -0.24% | 0.67x |
| 7 | VVV/USD | 61.572 | 26.736 | -0.40% | 0.46x |
| 8 | NIGHT/USD | 59.246 | 0.04911 | +1.09% | 0.20x |
| 9 | MELANIA/USD | 56.067 | 0.0507 | +0.00% | 0.31x |
| 10 | PENGU/USD | 34.425 | 0.004421 | -0.20% | 4.27x |
| 11 | STRK/USD | 33.308 | 0.03107 | +0.10% | 7.72x |
| 12 | CAP/USD | 31.123 | 0.092933 | +0.35% | 2.82x |

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

- Persisted scans: 2032; predictions: 18086; observations: 1230469.
- Matured sampled outcomes across 1/6/24/48h: 40481; gap abstentions: 25968. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 150 (sampled only; not a success-rate estimate).
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

**Writer:** 46034057908 · **Generation:** 2032 · **Legacy run:** 46034057908
**Main quote time:** 2026-11-27T16:32:10.961946+00:00 · **Legacy report time:** 2026-11-27T16:32:52.078619+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | ZEC/USD | 738.98 | 89.06 | +0.19% | 0.20x | MODERATE 65/100 | VERY_HIGH 70/100 | Watch |
| 2 | HYPE/USD ⭐ | 64.39 | 87.56 | +0.16% | 1.89x | STRONG 89/100 | HIGH 55/100 | Watch |
| 3 | SPACE/USD | 0.004126 | 70.16 | +0.10% | 0.76x | MODERATE 55/100 | VERY_HIGH 74/100 | Watch |
| 4 | UNI/USD | 4.7454 | 63.50 | +0.18% | 0.63x | MODERATE 52/100 | VERY_HIGH 70/100 | Watch |
| 5 | XDG/USD | 0.0574055 | 59.90 | -0.14% | 0.35x | WEAK 35/100 | VERY_HIGH 76/100 | Watch |
| 6 | SOL/USD | 71.95 | 59.83 | -0.24% | 0.67x | WEAK 35/100 | VERY_HIGH 76/100 | Watch |
| 7 | NIGHT/USD | 0.04911 | 56.73 | +1.09% | 0.20x | MODERATE 58/100 | VERY_HIGH 70/100 | Watch |
| 8 | VVV/USD | 26.736 | 54.15 | -0.40% | 0.46x | WEAK 32/100 | VERY_HIGH 76/100 | Do nothing |
| 9 | MELANIA/USD | 0.0507 | 49.12 | +0.00% | 0.31x | WEAK 30/100 | EXTREME 94/100 | Do nothing |
| 10 | STRK/USD | 0.03107 | 48.79 | +0.10% | 7.72x | MODERATE 69/100 | HIGH 67/100 | Watch |
| 11 | PENGU/USD | 0.004421 | 48.41 | -0.20% | 4.27x | MODERATE 54/100 | VERY_HIGH 73/100 | Watch |
| 12 | CAP/USD | 0.092933 | 47.86 | +0.35% | 2.82x | STRONG 79/100 | HIGH 60/100 | Watch |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | HYPE/USD ⭐ | 64.33 | 90.52 | +0.16% | 1.89x | 19699 | STRONG 90/100 | HIGH 55/100 | Watch |

**Same-run overlap:** HYPE/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
