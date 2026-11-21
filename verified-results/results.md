# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-21T02:05:36.168734+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/44853830749
**Source SHA:** bdc7e68f7fa75fae6636b7738d52f10a65d92038
**Previous ledger commit:** dd01311362d6dc9d8e4375b2645ece8bcb4c1b88 (atomic ledger/results publication)
**Ledger generation:** 1061 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 7s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 628; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 610; valid market observations: 608; OHLC screened: 24.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | XDG/USD | 0.054491 | 65.684 | 57.511 | +0.40% | +0.07% | 1.78x | 0.6 | 2026-11-21T02:05:29.174828+00:00 | Not calibrated | MODERATE 68/100 | HIGH 55/100 | Watch | WATCH |
| 2 | UNI/USD | 4.4789 | 62.490 | 47.992 | +0.26% | -0.10% | 5.96x | 3.6 | 2026-11-21T02:05:29.174828+00:00 | Not calibrated | MODERATE 61/100 | HIGH 61/100 | Watch | WATCH |
| 3 | VVV/USD | 21.241 | 60.605 | 67.712 | +2.42% | -0.40% | 0.49x | 8.5 | 2026-11-21T02:05:29.174828+00:00 | Not calibrated | WEAK 35/100 | VERY_HIGH 76/100 | Watch | WATCH |
| 4 | DCR/USD | 10.24 | 58.861 | 39.627 | +1.34% | +0.85% | 8.60x | 1.0 | 2026-11-21T02:05:29.174828+00:00 | Not calibrated | STRONG 84/100 | HIGH 67/100 | Watch | WATCH |
| 5 | ADA/USD | 0.14326 | 58.225 | 54.984 | +0.29% | -0.10% | 1.37x | 4.1 | 2026-11-21T02:05:29.174828+00:00 | Not calibrated | MODERATE 49/100 | HIGH 61/100 | Watch | WATCH |
| 6 | SKY/USD | 0.04444 | 55.983 | 39.853 | +1.37% | +0.23% | 6.21x | 11.3 | 2026-11-21T02:05:29.174828+00:00 | Not calibrated | STRONG 78/100 | HIGH 66/100 | Watch | WATCH |
| 7 | ETH/USD | 1623.44 | 54.178 | 56.750 | +0.25% | +0.14% | 0.67x | 0.1 | 2026-11-21T02:05:29.174828+00:00 | Not calibrated | MODERATE 47/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 8 | ALGO/USD | 0.07345 | 46.269 | 38.138 | +0.40% | +0.33% | 1.65x | 6.8 | 2026-11-21T02:05:29.174828+00:00 | Not calibrated | MODERATE 68/100 | HIGH 55/100 | Watch | WATCH |
| 9 | AKT/USD | 0.5058 | 34.029 | 28.305 | +0.38% | +0.34% | 1.40x | 13.8 | 2026-11-21T02:05:29.174828+00:00 | Not calibrated | MODERATE 57/100 | HIGH 66/100 | Watch | WATCH |
| 10 | DOT/USD | 0.6665 | 33.721 | 37.090 | +0.83% | +0.21% | 0.56x | 6.0 | 2026-11-21T02:05:29.174828+00:00 | Not calibrated | MODERATE 47/100 | VERY_HIGH 75/100 | Watch | WATCH |
| 11 | CC/USD | 0.07481 | 30.346 | 35.891 | +0.35% | +0.04% | 0.43x | 5.3 | 2026-11-21T02:05:29.174828+00:00 | Not calibrated | WEAK 35/100 | VERY_HIGH 75/100 | Watch | WATCH |
| 12 | NOS/USD | 0.3224 | 18.719 | 12.644 | +0.28% | +0.12% | 1.55x | 40.5 | 2026-11-21T02:05:29.174828+00:00 | Not calibrated | WEAK 29/100 | EXTREME 89/100 | Do nothing | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | VVV/USD | 67.712 | 21.241 | -0.40% | 0.49x |
| 2 | XDG/USD | 57.511 | 0.054491 | +0.07% | 1.78x |
| 3 | ETH/USD | 56.750 | 1623.44 | +0.14% | 0.67x |
| 4 | ADA/USD | 54.984 | 0.14326 | -0.10% | 1.37x |
| 5 | UNI/USD | 47.992 | 4.4789 | -0.10% | 5.96x |
| 6 | SKY/USD | 39.853 | 0.04444 | +0.23% | 6.21x |
| 7 | DCR/USD | 39.627 | 10.24 | +0.85% | 8.60x |
| 8 | ALGO/USD | 38.138 | 0.07345 | +0.33% | 1.65x |
| 9 | DOT/USD | 37.090 | 0.6665 | +0.21% | 0.56x |
| 10 | CC/USD | 35.891 | 0.07481 | +0.04% | 0.43x |
| 11 | AKT/USD | 28.305 | 0.5058 | +0.34% | 1.40x |
| 12 | NOS/USD | 12.644 | 0.3224 | +0.12% | 1.55x |

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

- Persisted scans: 1061; predictions: 8518; observations: 641448.
- Matured sampled outcomes across 1/6/24/48h: 10950; gap abstentions: 19342. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 10 (sampled only; not a success-rate estimate).
- False positives / missed movers: NOT VERIFIED without eligible continuous outcome coverage.
- Baseline vs challenger: recorded as-of; unbiased held-out lift NOT MEASURED.
- Online Kraken /USD stablecoin-base pairs excluded: 18 (counted from this scan's online AssetPairs metadata, not inferred from price).
- Stablecoin base exclusions: BRL1, BUSD, DAI, EUR, EURC, EUROP, EURQ, EURR, EURT, FDUSD, FRAX, GUSD, PYUSD, QCAD, RLUSD, TGBP, TUSD, USD, USD1, USDC, USDD, USDE, USDG, USDQ, USDR, USDS, USDT, ZUSD.
- DEX: NOT USED; no DEX freshness gate.
- OHLC screening abstentions: 12; details in immutable scan JSON artifact.
- Storage: ledger and results published in one non-force Git commit and read back. Independent artifact recovery is NOT VERIFIED by this scan alone.
- Errors: none in successful committed scan; a failed workflow must not publish a SUCCESS report.

# Cryptoscanner — challenger and independent legacy-inspired WATCH

Paper only · risk is high or higher · 30%+ in 48h probability NOT CALIBRATED
Signal confidence 0–100 means setup strength only, NOT a win probability. Actions are research guidance; no trade authorization.

**Writer:** 44853830749 · **Generation:** 1061 · **Legacy run:** 44853830749
**Main quote time:** 2026-11-21T02:05:36.168734+00:00 · **Legacy report time:** 2026-11-21T02:06:31.502849+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | XDG/USD ⭐ | 0.054491 | 65.68 | +0.07% | 1.78x | STRONG 78/100 | HIGH 55/100 | Watch |
| 2 | UNI/USD | 4.4789 | 62.49 | -0.10% | 5.96x | MODERATE 61/100 | HIGH 61/100 | Watch |
| 3 | VVV/USD | 21.241 | 60.60 | -0.40% | 0.49x | WEAK 35/100 | VERY_HIGH 76/100 | Watch |
| 4 | DCR/USD ⭐ | 10.24 | 58.86 | +0.85% | 8.60x | STRONG 94/100 | HIGH 67/100 | Consider small entry |
| 5 | ADA/USD | 0.14326 | 58.22 | -0.10% | 1.37x | MODERATE 49/100 | HIGH 61/100 | Watch |
| 6 | SKY/USD ⭐ | 0.04444 | 55.98 | +0.23% | 6.21x | STRONG 88/100 | HIGH 66/100 | Consider small entry |
| 7 | ETH/USD | 1623.44 | 54.18 | +0.14% | 0.67x | MODERATE 47/100 | VERY_HIGH 70/100 | Watch |
| 8 | ALGO/USD | 0.07345 | 46.27 | +0.33% | 1.65x | MODERATE 68/100 | HIGH 55/100 | Watch |
| 9 | AKT/USD | 0.5058 | 34.03 | +0.34% | 1.40x | MODERATE 57/100 | HIGH 66/100 | Watch |
| 10 | DOT/USD | 0.6665 | 33.72 | +0.21% | 0.56x | MODERATE 47/100 | VERY_HIGH 75/100 | Watch |
| 11 | CC/USD | 0.07481 | 30.35 | +0.04% | 0.43x | WEAK 35/100 | VERY_HIGH 75/100 | Watch |
| 12 | NOS/USD | 0.3224 | 18.72 | +0.12% | 1.55x | WEAK 29/100 | EXTREME 89/100 | Do nothing |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | XDG/USD ⭐ | 0.0545282 | 59.95 | +0.07% | 1.78x | 12087 | STRONG 75/100 | HIGH 55/100 | Watch |
| 2 | DCR/USD ⭐ | 10.24 | 58.42 | +0.85% | 8.60x | 2201 | STRONG 94/100 | HIGH 67/100 | Consider small entry |
| 3 | SKY/USD ⭐ | 0.04444 | 50.64 | +0.23% | 6.21x | 5876 | STRONG 90/100 | HIGH 60/100 | Consider small entry |

**Same-run overlap:** XDG/USD, DCR/USD, SKY/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
