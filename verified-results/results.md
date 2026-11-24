# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-24T05:31:33.722591+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/45333683987
**Source SHA:** 858c8bc8ec5d7641ddb39cacd8aca91719f855b1
**Previous ledger commit:** bdae845c3106d4a47a1a5b0458dc9c2764d5f41e (atomic ledger/results publication)
**Ledger generation:** 1531 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 6s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 628; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 610; valid market observations: 609; OHLC screened: 24.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | LTC/USD | 41.89 | 77.587 | 61.749 | +1.13% | +0.17% | 6.25x | 2.4 | 2026-11-24T05:31:27.527428+00:00 | Not calibrated | STRONG 84/100 | HIGH 55/100 | Watch | WATCH |
| 2 | PEPE/USD | 3.57e-06 | 74.622 | 76.400 | +4.33% | +0.71% | 0.47x | 8.4 | 2026-11-24T05:31:27.527428+00:00 | Not calibrated | MODERATE 67/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 3 | VVV/USD | 25.224 | 73.047 | 73.645 | +3.17% | +0.09% | 0.89x | 7.1 | 2026-11-24T05:31:27.527428+00:00 | Not calibrated | MODERATE 57/100 | HIGH 62/100 | Watch | WATCH |
| 4 | XDG/USD | 0.0566868 | 69.587 | 58.704 | +0.68% | +0.13% | 2.02x | 2.1 | 2026-11-24T05:31:27.527428+00:00 | Not calibrated | STRONG 80/100 | HIGH 55/100 | Watch | WATCH |
| 5 | XMR/USD | 494.95 | 66.368 | 66.346 | +1.84% | +0.40% | 0.80x | 3.0 | 2026-11-24T05:31:27.527428+00:00 | Not calibrated | MODERATE 63/100 | HIGH 62/100 | Watch | WATCH |
| 6 | DOT/USD | 0.6878 | 64.960 | 47.180 | +1.82% | +0.56% | 3.49x | 1.5 | 2026-11-24T05:31:27.527428+00:00 | Not calibrated | STRONG 87/100 | HIGH 60/100 | Watch | WATCH |
| 7 | XLM/USD | 0.1308 | 64.611 | 57.657 | +0.62% | +0.15% | 1.62x | 3.4 | 2026-11-24T05:31:27.527428+00:00 | Not calibrated | MODERATE 67/100 | HIGH 55/100 | Watch | WATCH |
| 8 | INX/USD | 0.004129 | 62.505 | 59.712 | +5.93% | +0.12% | 1.22x | 26.6 | 2026-11-24T05:31:27.527428+00:00 | Not calibrated | MODERATE 46/100 | EXTREME 86/100 | Do nothing | WATCH |
| 9 | XRP/USD | 0.95494 | 59.495 | 66.168 | +1.66% | -0.07% | 0.37x | 0.8 | 2026-11-24T05:31:27.527428+00:00 | Not calibrated | WEAK 35/100 | VERY_HIGH 76/100 | Watch | WATCH |
| 10 | NEAR/USD | 3.0264 | 58.337 | 62.307 | +1.52% | +0.19% | 0.51x | 6.6 | 2026-11-24T05:31:27.527428+00:00 | Not calibrated | MODERATE 49/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 11 | HYPE/USD | 64.11 | 57.138 | 58.609 | +0.74% | +0.44% | 0.63x | 3.1 | 2026-11-24T05:31:27.527428+00:00 | Not calibrated | MODERATE 59/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 12 | SUI/USD | 0.6765 | 55.282 | 57.797 | +0.51% | +0.22% | 0.64x | 1.5 | 2026-11-24T05:31:27.527428+00:00 | Not calibrated | MODERATE 58/100 | VERY_HIGH 70/100 | Watch | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | PEPE/USD | 76.400 | 3.57e-06 | +0.71% | 0.47x |
| 2 | VVV/USD | 73.645 | 25.224 | +0.09% | 0.89x |
| 3 | XMR/USD | 66.346 | 494.95 | +0.40% | 0.80x |
| 4 | XRP/USD | 66.168 | 0.95494 | -0.07% | 0.37x |
| 5 | NEAR/USD | 62.307 | 3.0264 | +0.19% | 0.51x |
| 6 | LTC/USD | 61.749 | 41.89 | +0.17% | 6.25x |
| 7 | INX/USD | 59.712 | 0.004129 | +0.12% | 1.22x |
| 8 | XDG/USD | 58.704 | 0.0566868 | +0.13% | 2.02x |
| 9 | HYPE/USD | 58.609 | 64.11 | +0.44% | 0.63x |
| 10 | SUI/USD | 57.797 | 0.6765 | +0.22% | 0.64x |
| 11 | XLM/USD | 57.657 | 0.1308 | +0.15% | 1.62x |
| 12 | DOT/USD | 47.180 | 0.6878 | +0.56% | 3.49x |

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

- Persisted scans: 1531; predictions: 13105; observations: 927477.
- Matured sampled outcomes across 1/6/24/48h: 24525; gap abstentions: 22370. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 136 (sampled only; not a success-rate estimate).
- False positives / missed movers: NOT VERIFIED without eligible continuous outcome coverage.
- Baseline vs challenger: recorded as-of; unbiased held-out lift NOT MEASURED.
- Online Kraken /USD stablecoin-base pairs excluded: 18 (counted from this scan's online AssetPairs metadata, not inferred from price).
- Stablecoin base exclusions: BRL1, BUSD, DAI, EUR, EURC, EUROP, EURQ, EURR, EURT, FDUSD, FRAX, GUSD, PYUSD, QCAD, RLUSD, TGBP, TUSD, USD, USD1, USDC, USDD, USDE, USDG, USDQ, USDR, USDS, USDT, ZUSD.
- DEX: NOT USED; no DEX freshness gate.
- OHLC screening abstentions: 9; details in immutable scan JSON artifact.
- Storage: ledger and results published in one non-force Git commit and read back. Independent artifact recovery is NOT VERIFIED by this scan alone.
- Errors: none in successful committed scan; a failed workflow must not publish a SUCCESS report.

# Cryptoscanner — challenger and independent legacy-inspired WATCH

Paper only · risk is high or higher · 30%+ in 48h probability NOT CALIBRATED
Signal confidence 0–100 means setup strength only, NOT a win probability. Actions are research guidance; no trade authorization.

**Writer:** 45333683987 · **Generation:** 1531 · **Legacy run:** 45333683987
**Main quote time:** 2026-11-24T05:31:33.722591+00:00 · **Legacy report time:** 2026-11-24T05:32:45.278222+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | LTC/USD ⭐ | 41.89 | 77.59 | +0.17% | 6.25x | STRONG 94/100 | HIGH 55/100 | Watch |
| 2 | PEPE/USD | 3.57e-06 | 74.62 | +0.71% | 0.47x | MODERATE 67/100 | VERY_HIGH 70/100 | Watch |
| 3 | VVV/USD | 25.224 | 73.05 | +0.09% | 0.89x | MODERATE 57/100 | HIGH 62/100 | Watch |
| 4 | XDG/USD ⭐ | 0.0566868 | 69.59 | +0.13% | 2.02x | STRONG 90/100 | HIGH 55/100 | Watch |
| 5 | XMR/USD | 494.95 | 66.37 | +0.40% | 0.80x | MODERATE 63/100 | HIGH 62/100 | Watch |
| 6 | DOT/USD | 0.6878 | 64.96 | +0.56% | 3.49x | STRONG 87/100 | HIGH 60/100 | Watch |
| 7 | XLM/USD | 0.1308 | 64.61 | +0.15% | 1.62x | MODERATE 67/100 | HIGH 55/100 | Watch |
| 8 | INX/USD ⭐ | 0.004129 | 62.51 | +0.12% | 1.22x | MODERATE 56/100 | EXTREME 86/100 | Do nothing |
| 9 | XRP/USD | 0.95494 | 59.49 | -0.07% | 0.37x | WEAK 35/100 | VERY_HIGH 76/100 | Watch |
| 10 | NEAR/USD | 3.0264 | 58.34 | +0.19% | 0.51x | MODERATE 49/100 | VERY_HIGH 70/100 | Watch |
| 11 | HYPE/USD | 64.11 | 57.14 | +0.44% | 0.63x | MODERATE 59/100 | VERY_HIGH 70/100 | Watch |
| 12 | SUI/USD | 0.6765 | 55.28 | +0.22% | 0.64x | MODERATE 58/100 | VERY_HIGH 70/100 | Watch |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | XDC/USD | 0.02695 | 81.13 | +0.91% | 4.56x | 4975 | STRONG 91/100 | HIGH 66/100 | Consider small entry |
| 2 | INX/USD ⭐ | 0.004096 | 72.16 | +0.12% | 1.22x | 3312 | MODERATE 61/100 | EXTREME 86/100 | Do nothing |
| 3 | UNI/USD | 4.9133 | 70.39 | +0.19% | 4.67x | 9330 | STRONG 80/100 | HIGH 55/100 | Watch |
| 4 | LTC/USD ⭐ | 41.86 | 68.47 | +0.17% | 6.25x | 13099 | STRONG 89/100 | HIGH 55/100 | Watch |
| 5 | XDG/USD ⭐ | 0.0566868 | 63.59 | +0.13% | 2.02x | 11147 | STRONG 87/100 | HIGH 55/100 | Watch |

**Same-run overlap:** LTC/USD, XDG/USD, INX/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
