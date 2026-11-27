# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-27T18:22:26.601226+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/46048602238
**Source SHA:** 858c8bc8ec5d7641ddb39cacd8aca91719f855b1
**Previous ledger commit:** 1317a8b961137787f37cacda2a77df0846fa1aa7 (atomic ledger/results publication)
**Ledger generation:** 2043 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 8s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 628; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 610; valid market observations: 605; OHLC screened: 24.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | ZEC/USD | 742.48 | 97.612 | 97.844 | +8.92% | +0.31% | 0.82x | 4.3 | 2026-11-27T18:22:18.628426+00:00 | Not calibrated | STRONG 79/100 | HIGH 62/100 | Watch | WATCH |
| 2 | NIGHT/USD | 0.04983 | 90.654 | 73.637 | +2.81% | +0.40% | 2.73x | 2.0 | 2026-11-27T18:22:18.628426+00:00 | Not calibrated | STRONG 100/100 | HIGH 55/100 | Consider small entry | WATCH |
| 3 | UNI/USD | 4.7893 | 84.978 | 72.037 | +2.99% | -0.12% | 2.35x | 2.7 | 2026-11-27T18:22:18.628426+00:00 | Not calibrated | STRONG 72/100 | HIGH 61/100 | Watch | WATCH |
| 4 | SPACE/USD | 0.004256 | 81.680 | 71.095 | +9.92% | +1.33% | 1.39x | 9.4 | 2026-11-27T18:22:18.628426+00:00 | Not calibrated | STRONG 86/100 | HIGH 67/100 | Watch | WATCH |
| 5 | XDG/USD | 0.0575271 | 78.709 | 69.251 | +2.04% | -0.06% | 1.98x | 0.1 | 2026-11-27T18:22:18.628426+00:00 | Not calibrated | MODERATE 59/100 | HIGH 61/100 | Watch | WATCH |
| 6 | SENT/USD | 0.022918 | 75.153 | 70.138 | +6.20% | +0.07% | 1.46x | 7.9 | 2026-11-27T18:22:18.628426+00:00 | Not calibrated | STRONG 73/100 | HIGH 67/100 | Watch | WATCH |
| 7 | FET/USD | 0.1259 | 72.617 | 61.307 | +4.57% | -0.63% | 2.45x | 15.9 | 2026-11-27T18:22:18.628426+00:00 | Not calibrated | MODERATE 61/100 | HIGH 67/100 | Watch | WATCH |
| 8 | PAXG/USD | 3634.99 | 71.485 | 57.333 | +2.20% | -0.17% | 3.96x | 1.6 | 2026-11-27T18:22:18.628426+00:00 | Not calibrated | MODERATE 66/100 | HIGH 61/100 | Watch | WATCH |
| 9 | XAUT/USD | 3639.4 | 66.241 | 53.175 | +2.24% | -0.07% | 2.34x | 0.3 | 2026-11-27T18:22:18.628426+00:00 | Not calibrated | MODERATE 63/100 | HIGH 61/100 | Watch | WATCH |
| 10 | HYPE/USD | 63.41 | 58.683 | 67.600 | +1.91% | -0.44% | 0.33x | 1.6 | 2026-11-27T18:22:18.628426+00:00 | Not calibrated | WEAK 34/100 | VERY_HIGH 76/100 | Do nothing | WATCH |
| 11 | XRP/USD | 0.94603 | 54.912 | 57.383 | +0.35% | +0.07% | 0.72x | 0.1 | 2026-11-27T18:22:18.628426+00:00 | Not calibrated | MODERATE 47/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 12 | VVV/USD | 26.665 | 54.161 | 57.399 | +1.84% | +0.33% | 0.51x | 8.6 | 2026-11-27T18:22:18.628426+00:00 | Not calibrated | MODERATE 57/100 | VERY_HIGH 70/100 | Watch | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | ZEC/USD | 97.844 | 742.48 | +0.31% | 0.82x |
| 2 | NIGHT/USD | 73.637 | 0.04983 | +0.40% | 2.73x |
| 3 | UNI/USD | 72.037 | 4.7893 | -0.12% | 2.35x |
| 4 | SPACE/USD | 71.095 | 0.004256 | +1.33% | 1.39x |
| 5 | SENT/USD | 70.138 | 0.022918 | +0.07% | 1.46x |
| 6 | XDG/USD | 69.251 | 0.0575271 | -0.06% | 1.98x |
| 7 | HYPE/USD | 67.600 | 63.41 | -0.44% | 0.33x |
| 8 | FET/USD | 61.307 | 0.1259 | -0.63% | 2.45x |
| 9 | VVV/USD | 57.399 | 26.665 | +0.33% | 0.51x |
| 10 | XRP/USD | 57.383 | 0.94603 | +0.07% | 0.72x |
| 11 | PAXG/USD | 57.333 | 3634.99 | -0.17% | 3.96x |
| 12 | XAUT/USD | 53.175 | 3639.4 | -0.07% | 2.34x |

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

- Persisted scans: 2043; predictions: 18218; observations: 1237124.
- Matured sampled outcomes across 1/6/24/48h: 40931; gap abstentions: 25968. Per-horizon counts require independent audit; do not infer held-out lift.
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

**Writer:** 46048602238 · **Generation:** 2043 · **Legacy run:** 46048602238
**Main quote time:** 2026-11-27T18:22:26.601226+00:00 · **Legacy report time:** 2026-11-27T18:23:23.869982+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | ZEC/USD | 742.48 | 97.61 | +0.31% | 0.82x | STRONG 79/100 | HIGH 62/100 | Watch |
| 2 | NIGHT/USD ⭐ | 0.04983 | 90.65 | +0.40% | 2.73x | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 3 | UNI/USD | 4.7893 | 84.98 | -0.12% | 2.35x | STRONG 72/100 | HIGH 61/100 | Watch |
| 4 | SPACE/USD ⭐ | 0.004256 | 81.68 | +1.33% | 1.39x | STRONG 96/100 | HIGH 67/100 | Watch |
| 5 | XDG/USD | 0.0575271 | 78.71 | -0.06% | 1.98x | MODERATE 59/100 | HIGH 61/100 | Watch |
| 6 | SENT/USD ⭐ | 0.022918 | 75.15 | +0.07% | 1.46x | STRONG 83/100 | HIGH 67/100 | Watch |
| 7 | FET/USD | 0.1259 | 72.62 | -0.63% | 2.45x | MODERATE 61/100 | HIGH 67/100 | Watch |
| 8 | PAXG/USD | 3634.99 | 71.49 | -0.17% | 3.96x | MODERATE 66/100 | HIGH 61/100 | Watch |
| 9 | XAUT/USD | 3639.4 | 66.24 | -0.07% | 2.34x | MODERATE 63/100 | HIGH 61/100 | Watch |
| 10 | HYPE/USD | 63.41 | 58.68 | -0.44% | 0.33x | WEAK 34/100 | VERY_HIGH 76/100 | Do nothing |
| 11 | XRP/USD | 0.94603 | 54.91 | +0.07% | 0.72x | MODERATE 47/100 | VERY_HIGH 70/100 | Watch |
| 12 | VVV/USD | 26.665 | 54.16 | +0.33% | 0.51x | MODERATE 57/100 | VERY_HIGH 70/100 | Watch |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | NIGHT/USD ⭐ | 0.0499 | 91.54 | +0.40% | 2.73x | 16779 | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 2 | SENT/USD ⭐ | 0.022918 | 78.76 | +0.07% | 1.46x | 3348 | STRONG 84/100 | HIGH 67/100 | Watch |
| 3 | SPACE/USD ⭐ | 0.004259 | 74.96 | +1.33% | 1.39x | 2510 | STRONG 92/100 | HIGH 67/100 | Watch |

**Same-run overlap:** NIGHT/USD, SPACE/USD, SENT/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
