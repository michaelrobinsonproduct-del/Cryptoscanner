# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-23T21:12:32.813764+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/45266770830
**Source SHA:** 858c8bc8ec5d7641ddb39cacd8aca91719f855b1
**Previous ledger commit:** 6d9dcb15643f71effc853e6b7a2d9b5680a60bff (atomic ledger/results publication)
**Ledger generation:** 1482 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 9s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 628; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 610; valid market observations: 609; OHLC screened: 24.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | QNT/USD | 157.61 | 115.428 | 97.143 | +9.88% | +0.66% | 2.62x | 5.7 | 2026-11-23T21:12:24.007513+00:00 | Not calibrated | STRONG 100/100 | HIGH 55/100 | Consider small entry | WATCH |
| 2 | UNI/USD | 4.8604 | 93.044 | 75.523 | +3.83% | +0.50% | 3.61x | 7.4 | 2026-11-23T21:12:24.007513+00:00 | Not calibrated | STRONG 100/100 | HIGH 55/100 | Consider small entry | WATCH |
| 3 | CC/USD | 0.07759 | 91.796 | 76.473 | +5.90% | +0.06% | 4.32x | 2.6 | 2026-11-23T21:12:24.007513+00:00 | Not calibrated | STRONG 91/100 | HIGH 60/100 | Watch | WATCH |
| 4 | SOL/USD | 72.68 | 91.351 | 74.629 | +2.90% | +0.34% | 7.03x | 1.4 | 2026-11-23T21:12:24.007513+00:00 | Not calibrated | STRONG 100/100 | HIGH 55/100 | Consider small entry | WATCH |
| 5 | ALGO/USD | 0.08134 | 90.262 | 90.015 | +7.84% | -0.73% | 1.39x | 9.8 | 2026-11-23T21:12:24.007513+00:00 | Not calibrated | MODERATE 65/100 | HIGH 61/100 | Watch | WATCH |
| 6 | LTC/USD | 41.3 | 89.877 | 72.448 | +2.84% | +0.49% | 2.79x | 4.8 | 2026-11-23T21:12:24.007513+00:00 | Not calibrated | STRONG 100/100 | HIGH 55/100 | Consider small entry | WATCH |
| 7 | KAS/USD | 0.02733 | 88.250 | 70.862 | +5.89% | +0.48% | 3.95x | 14.7 | 2026-11-23T21:12:24.007513+00:00 | Not calibrated | STRONG 94/100 | HIGH 61/100 | Consider small entry | WATCH |
| 8 | XDG/USD | 0.0566971 | 85.781 | 71.034 | +2.56% | +0.56% | 2.20x | 3.7 | 2026-11-23T21:12:24.007513+00:00 | Not calibrated | STRONG 98/100 | HIGH 55/100 | Consider small entry | WATCH |
| 9 | SUI/USD | 0.6748 | 84.882 | 74.648 | +2.91% | +0.52% | 1.76x | 1.5 | 2026-11-23T21:12:24.007513+00:00 | Not calibrated | STRONG 87/100 | HIGH 55/100 | Consider small entry | WATCH |
| 10 | INJ/USD | 6.45 | 72.894 | 75.541 | +3.56% | +0.47% | 0.50x | 4.7 | 2026-11-23T21:12:24.007513+00:00 | Not calibrated | MODERATE 66/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 11 | ATOM/USD | 1.2762 | 68.199 | 71.404 | +8.89% | +0.81% | 0.27x | 13.3 | 2026-11-23T21:12:24.007513+00:00 | Not calibrated | MODERATE 59/100 | VERY_HIGH 81/100 | Watch | WATCH |
| 12 | PAXG/USD | 3623.54 | 66.769 | 60.992 | +1.44% | +0.06% | 1.55x | 0.2 | 2026-11-23T21:12:24.007513+00:00 | Not calibrated | MODERATE 68/100 | HIGH 55/100 | Watch | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | QNT/USD | 97.143 | 157.61 | +0.66% | 2.62x |
| 2 | ALGO/USD | 90.015 | 0.08134 | -0.73% | 1.39x |
| 3 | CC/USD | 76.473 | 0.07759 | +0.06% | 4.32x |
| 4 | INJ/USD | 75.541 | 6.45 | +0.47% | 0.50x |
| 5 | UNI/USD | 75.523 | 4.8604 | +0.50% | 3.61x |
| 6 | SUI/USD | 74.648 | 0.6748 | +0.52% | 1.76x |
| 7 | SOL/USD | 74.629 | 72.68 | +0.34% | 7.03x |
| 8 | LTC/USD | 72.448 | 41.3 | +0.49% | 2.79x |
| 9 | ATOM/USD | 71.404 | 1.2762 | +0.81% | 0.27x |
| 10 | XDG/USD | 71.034 | 0.0566971 | +0.56% | 2.20x |
| 11 | KAS/USD | 70.862 | 0.02733 | +0.48% | 3.95x |
| 12 | PAXG/USD | 60.992 | 3623.54 | +0.06% | 1.55x |

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

- Persisted scans: 1482; predictions: 12551; observations: 897640.
- Matured sampled outcomes across 1/6/24/48h: 22480; gap abstentions: 22370. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 131 (sampled only; not a success-rate estimate).
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

**Writer:** 45266770830 · **Generation:** 1482 · **Legacy run:** 45266770830
**Main quote time:** 2026-11-23T21:12:32.813764+00:00 · **Legacy report time:** 2026-11-23T21:13:21.975756+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | QNT/USD ⭐ | 157.61 | 115.43 | +0.66% | 2.62x | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 2 | UNI/USD ⭐ | 4.8604 | 93.04 | +0.50% | 3.61x | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 3 | CC/USD ⭐ | 0.07759 | 91.80 | +0.06% | 4.32x | STRONG 100/100 | HIGH 60/100 | Watch |
| 4 | SOL/USD ⭐ | 72.68 | 91.35 | +0.34% | 7.03x | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 5 | ALGO/USD | 0.08134 | 90.26 | -0.73% | 1.39x | MODERATE 65/100 | HIGH 61/100 | Watch |
| 6 | LTC/USD ⭐ | 41.3 | 89.88 | +0.49% | 2.79x | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 7 | KAS/USD ⭐ | 0.02733 | 88.25 | +0.48% | 3.95x | STRONG 100/100 | HIGH 61/100 | Consider small entry |
| 8 | XDG/USD ⭐ | 0.0566971 | 85.78 | +0.56% | 2.20x | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 9 | SUI/USD ⭐ | 0.6748 | 84.88 | +0.52% | 1.76x | STRONG 97/100 | HIGH 55/100 | Consider small entry |
| 10 | INJ/USD | 6.45 | 72.89 | +0.47% | 0.50x | MODERATE 66/100 | VERY_HIGH 70/100 | Watch |
| 11 | ATOM/USD | 1.2762 | 68.20 | +0.81% | 0.27x | MODERATE 59/100 | VERY_HIGH 81/100 | Watch |
| 12 | PAXG/USD | 3623.54 | 66.77 | +0.06% | 1.55x | MODERATE 68/100 | HIGH 55/100 | Watch |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | QNT/USD ⭐ | 157.57 | 99.59 | +0.66% | 2.62x | 11980 | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 2 | UNI/USD ⭐ | 4.8562 | 99.06 | +0.50% | 3.61x | 9673 | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 3 | SOL/USD ⭐ | 72.76 | 91.72 | +0.34% | 7.03x | 45649 | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 4 | LTC/USD ⭐ | 41.32 | 90.46 | +0.49% | 2.79x | 12771 | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 5 | PENGU/USD | 0.004425 | 90.39 | +0.50% | 4.06x | 4294 | STRONG 100/100 | HIGH 60/100 | Consider small entry |
| 6 | SUI/USD ⭐ | 0.6748 | 88.60 | +0.52% | 1.76x | 12149 | STRONG 99/100 | HIGH 55/100 | Consider small entry |
| 7 | XDG/USD ⭐ | 0.0566889 | 86.73 | +0.56% | 2.20x | 10028 | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 8 | KAS/USD ⭐ | 0.02727 | 83.61 | +0.48% | 3.95x | 4207 | STRONG 100/100 | HIGH 61/100 | Consider small entry |
| 9 | CC/USD ⭐ | 0.07759 | 82.09 | +0.06% | 4.32x | 5740 | STRONG 96/100 | HIGH 60/100 | Watch |
| 10 | CAP/USD | 0.105444 | 76.49 | +0.50% | 1.63x | 6653 | STRONG 73/100 | VERY_HIGH 72/100 | Watch |

**Same-run overlap:** QNT/USD, UNI/USD, CC/USD, SOL/USD, LTC/USD, KAS/USD, XDG/USD, SUI/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
