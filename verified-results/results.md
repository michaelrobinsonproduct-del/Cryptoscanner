# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-27T19:42:27.922247+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/46058242221
**Source SHA:** 858c8bc8ec5d7641ddb39cacd8aca91719f855b1
**Previous ledger commit:** 984edd39f7dda16eb35c581204e04043d347198e (atomic ledger/results publication)
**Ledger generation:** 2051 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 6s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 628; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 610; valid market observations: 605; OHLC screened: 24.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | UNI/USD | 4.846 | 96.819 | 79.375 | +4.21% | +0.49% | 3.48x | 5.6 | 2026-11-27T19:42:21.639499+00:00 | Not calibrated | STRONG 100/100 | HIGH 55/100 | Consider small entry | WATCH |
| 2 | ZEC/USD | 746.83 | 93.526 | 97.991 | +9.56% | +0.31% | 0.40x | 4.0 | 2026-11-27T19:42:21.639499+00:00 | Not calibrated | STRONG 77/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 3 | ENA/USD | 0.1047 | 83.669 | 64.346 | +4.28% | +0.86% | 3.43x | 9.6 | 2026-11-27T19:42:21.639499+00:00 | Not calibrated | STRONG 97/100 | HIGH 55/100 | Consider small entry | WATCH |
| 4 | NIGHT/USD | 0.05009 | 81.459 | 77.398 | +3.34% | +0.08% | 1.37x | 2.0 | 2026-11-27T19:42:21.639499+00:00 | Not calibrated | STRONG 76/100 | HIGH 55/100 | Watch | WATCH |
| 5 | INJ/USD | 6.41 | 81.367 | 64.015 | +3.52% | +0.47% | 3.19x | 6.2 | 2026-11-27T19:42:21.639499+00:00 | Not calibrated | STRONG 96/100 | HIGH 55/100 | Consider small entry | WATCH |
| 6 | SKY/USD | 0.04862 | 75.890 | 64.285 | +4.76% | +0.90% | 1.71x | 8.2 | 2026-11-27T19:42:21.639499+00:00 | Not calibrated | STRONG 83/100 | HIGH 60/100 | Consider small entry | WATCH |
| 7 | HYPE/USD | 64.03 | 70.505 | 74.582 | +2.91% | +0.25% | 0.47x | 1.6 | 2026-11-27T19:42:21.639499+00:00 | Not calibrated | MODERATE 65/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 8 | XDG/USD | 0.0579813 | 67.971 | 74.572 | +2.85% | +0.21% | 0.24x | 0.8 | 2026-11-27T19:42:21.639499+00:00 | Not calibrated | MODERATE 64/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 9 | SOL/USD | 72.36 | 64.055 | 68.321 | +2.00% | +0.42% | 0.37x | 1.4 | 2026-11-27T19:42:21.639499+00:00 | Not calibrated | MODERATE 62/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 10 | AVAX/USD | 6.665 | 62.578 | 46.375 | +1.06% | +0.24% | 3.09x | 1.5 | 2026-11-27T19:42:21.639499+00:00 | Not calibrated | STRONG 86/100 | HIGH 55/100 | Watch | WATCH |
| 11 | SUI/USD | 0.6757 | 61.550 | 62.647 | +1.20% | +0.33% | 0.73x | 1.5 | 2026-11-27T19:42:21.639499+00:00 | Not calibrated | MODERATE 61/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 12 | XRP/USD | 0.95144 | 61.081 | 61.295 | +0.92% | +0.19% | 0.88x | 0.3 | 2026-11-27T19:42:21.639499+00:00 | Not calibrated | MODERATE 51/100 | HIGH 62/100 | Watch | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | ZEC/USD | 97.991 | 746.83 | +0.31% | 0.40x |
| 2 | UNI/USD | 79.375 | 4.846 | +0.49% | 3.48x |
| 3 | NIGHT/USD | 77.398 | 0.05009 | +0.08% | 1.37x |
| 4 | HYPE/USD | 74.582 | 64.03 | +0.25% | 0.47x |
| 5 | XDG/USD | 74.572 | 0.0579813 | +0.21% | 0.24x |
| 6 | SOL/USD | 68.321 | 72.36 | +0.42% | 0.37x |
| 7 | ENA/USD | 64.346 | 0.1047 | +0.86% | 3.43x |
| 8 | SKY/USD | 64.285 | 0.04862 | +0.90% | 1.71x |
| 9 | INJ/USD | 64.015 | 6.41 | +0.47% | 3.19x |
| 10 | SUI/USD | 62.647 | 0.6757 | +0.33% | 0.73x |
| 11 | XRP/USD | 61.295 | 0.95144 | +0.19% | 0.88x |
| 12 | AVAX/USD | 46.375 | 6.665 | +0.24% | 3.09x |

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

- Persisted scans: 2051; predictions: 18314; observations: 1241964.
- Matured sampled outcomes across 1/6/24/48h: 41327; gap abstentions: 25968. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 153 (sampled only; not a success-rate estimate).
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

**Writer:** 46058242221 · **Generation:** 2051 · **Legacy run:** 46058242221
**Main quote time:** 2026-11-27T19:42:27.922247+00:00 · **Legacy report time:** 2026-11-27T19:43:23.251136+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | UNI/USD ⭐ | 4.846 | 96.82 | +0.49% | 3.48x | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 2 | ZEC/USD | 746.83 | 93.53 | +0.31% | 0.40x | STRONG 77/100 | VERY_HIGH 70/100 | Watch |
| 3 | ENA/USD ⭐ | 0.1047 | 83.67 | +0.86% | 3.43x | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 4 | NIGHT/USD ⭐ | 0.05009 | 81.46 | +0.08% | 1.37x | STRONG 86/100 | HIGH 55/100 | Watch |
| 5 | INJ/USD ⭐ | 6.41 | 81.37 | +0.47% | 3.19x | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 6 | SKY/USD ⭐ | 0.04862 | 75.89 | +0.90% | 1.71x | STRONG 93/100 | HIGH 60/100 | Consider small entry |
| 7 | HYPE/USD | 64.03 | 70.51 | +0.25% | 0.47x | MODERATE 65/100 | VERY_HIGH 70/100 | Watch |
| 8 | XDG/USD | 0.0579813 | 67.97 | +0.21% | 0.24x | MODERATE 64/100 | VERY_HIGH 70/100 | Watch |
| 9 | SOL/USD | 72.36 | 64.05 | +0.42% | 0.37x | MODERATE 62/100 | VERY_HIGH 70/100 | Watch |
| 10 | AVAX/USD | 6.665 | 62.58 | +0.24% | 3.09x | STRONG 86/100 | HIGH 55/100 | Watch |
| 11 | SUI/USD | 0.6757 | 61.55 | +0.33% | 0.73x | MODERATE 61/100 | VERY_HIGH 70/100 | Watch |
| 12 | XRP/USD | 0.95144 | 61.08 | +0.19% | 0.88x | MODERATE 51/100 | HIGH 62/100 | Watch |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | UNI/USD ⭐ | 4.846 | 100.00 | +0.49% | 3.48x | 10079 | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 2 | NIGHT/USD ⭐ | 0.05002 | 88.09 | +0.08% | 1.37x | 17721 | STRONG 89/100 | HIGH 55/100 | Watch |
| 3 | ENA/USD ⭐ | 0.1047 | 86.08 | +0.86% | 3.43x | 2721 | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 4 | INJ/USD ⭐ | 6.412 | 84.06 | +0.47% | 3.19x | 6285 | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 5 | SKY/USD ⭐ | 0.04888 | 78.60 | +0.90% | 1.71x | 6180 | STRONG 84/100 | VERY_HIGH 72/100 | Watch |
| 6 | PAXG/USD | 3638.42 | 69.27 | +0.06% | 1.06x | 4753 | MODERATE 60/100 | HIGH 62/100 | Watch |

**Same-run overlap:** UNI/USD, ENA/USD, NIGHT/USD, INJ/USD, SKY/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
