# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-23T05:41:38.650267+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/45119159124
**Source SHA:** 858c8bc8ec5d7641ddb39cacd8aca91719f855b1
**Previous ledger commit:** f0f0a38484f096de3de434a7a711ef30045342cb (atomic ledger/results publication)
**Ledger generation:** 1388 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 9s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 628; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 610; valid market observations: 609; OHLC screened: 24.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | JUP/USD | 0.23962 | 98.630 | 76.034 | +6.70% | +1.96% | 2.28x | 6.3 | 2026-11-23T05:41:29.300043+00:00 | Not calibrated | STRONG 100/100 | HIGH 60/100 | Consider small entry | WATCH |
| 2 | AI/USD | 0.01629 | 91.421 | 69.891 | +11.42% | +1.31% | 12.12x | 12.3 | 2026-11-23T05:41:29.300043+00:00 | Not calibrated | STRONG 96/100 | VERY_HIGH 73/100 | Watch | WATCH |
| 3 | NEAR/USD | 3.0402 | 84.046 | 66.595 | +1.96% | +0.49% | 2.92x | 4.3 | 2026-11-23T05:41:29.300043+00:00 | Not calibrated | STRONG 97/100 | HIGH 55/100 | Consider small entry | WATCH |
| 4 | SOL/USD | 71.9 | 83.824 | 66.891 | +1.80% | +0.49% | 2.45x | 1.4 | 2026-11-23T05:41:29.300043+00:00 | Not calibrated | STRONG 97/100 | HIGH 55/100 | Consider small entry | WATCH |
| 5 | XRP/USD | 0.93894 | 80.954 | 63.550 | +1.23% | +0.48% | 3.83x | 0.1 | 2026-11-23T05:41:29.300043+00:00 | Not calibrated | STRONG 95/100 | HIGH 55/100 | Consider small entry | WATCH |
| 6 | SUI/USD | 0.6659 | 72.498 | 65.138 | +1.56% | +0.67% | 1.40x | 1.5 | 2026-11-23T05:41:29.300043+00:00 | Not calibrated | STRONG 81/100 | HIGH 55/100 | Watch | WATCH |
| 7 | UNI/USD | 4.8152 | 71.973 | 58.950 | +2.86% | +0.46% | 2.07x | 4.6 | 2026-11-23T05:41:29.300043+00:00 | Not calibrated | STRONG 91/100 | HIGH 55/100 | Consider small entry | WATCH |
| 8 | XDG/USD | 0.0557387 | 68.711 | 52.251 | +0.82% | +0.29% | 3.82x | 0.7 | 2026-11-23T05:41:29.300043+00:00 | Not calibrated | STRONG 89/100 | HIGH 55/100 | Watch | WATCH |
| 9 | NIGHT/USD | 0.05014 | 67.733 | 60.623 | +1.97% | +0.18% | 1.62x | 8.0 | 2026-11-23T05:41:29.300043+00:00 | Not calibrated | MODERATE 69/100 | HIGH 55/100 | Watch | WATCH |
| 10 | PAXG/USD | 3612.15 | 67.680 | 51.752 | +1.12% | +0.22% | 2.48x | 0.9 | 2026-11-23T05:41:29.300043+00:00 | Not calibrated | STRONG 89/100 | HIGH 55/100 | Watch | WATCH |
| 11 | XBT/USD | 61555.9 | 66.077 | 59.155 | +0.63% | +0.29% | 1.55x | 0.5 | 2026-11-23T05:41:29.300043+00:00 | Not calibrated | STRONG 78/100 | HIGH 55/100 | Watch | WATCH |
| 12 | BLESS/USD | 0.017862 | 61.323 | 70.687 | +10.99% | -0.88% | 0.50x | 26.3 | 2026-11-23T05:41:29.300043+00:00 | Not calibrated | WEAK 26/100 | EXTREME 88/100 | Do nothing | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | JUP/USD | 76.034 | 0.23962 | +1.96% | 2.28x |
| 2 | BLESS/USD | 70.687 | 0.017862 | -0.88% | 0.50x |
| 3 | AI/USD | 69.891 | 0.01629 | +1.31% | 12.12x |
| 4 | SOL/USD | 66.891 | 71.9 | +0.49% | 2.45x |
| 5 | NEAR/USD | 66.595 | 3.0402 | +0.49% | 2.92x |
| 6 | SUI/USD | 65.138 | 0.6659 | +0.67% | 1.40x |
| 7 | XRP/USD | 63.550 | 0.93894 | +0.48% | 3.83x |
| 8 | NIGHT/USD | 60.623 | 0.05014 | +0.18% | 1.62x |
| 9 | XBT/USD | 59.155 | 61555.9 | +0.29% | 1.55x |
| 10 | UNI/USD | 58.950 | 4.8152 | +0.46% | 2.07x |
| 11 | XDG/USD | 52.251 | 0.0557387 | +0.29% | 3.82x |
| 12 | PAXG/USD | 51.752 | 3612.15 | +0.22% | 2.48x |

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

- Persisted scans: 1388; predictions: 11423; observations: 840396.
- Matured sampled outcomes across 1/6/24/48h: 18520; gap abstentions: 22370. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 112 (sampled only; not a success-rate estimate).
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

**Writer:** 45119159124 · **Generation:** 1388 · **Legacy run:** 45119159124
**Main quote time:** 2026-11-23T05:41:38.650267+00:00 · **Legacy report time:** 2026-11-23T05:42:42.203982+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | JUP/USD ⭐ | 0.23962 | 98.63 | +1.96% | 2.28x | STRONG 100/100 | HIGH 60/100 | Consider small entry |
| 2 | AI/USD ⭐ | 0.01629 | 91.42 | +1.31% | 12.12x | STRONG 100/100 | VERY_HIGH 73/100 | Watch |
| 3 | NEAR/USD ⭐ | 3.0402 | 84.05 | +0.49% | 2.92x | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 4 | SOL/USD ⭐ | 71.9 | 83.82 | +0.49% | 2.45x | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 5 | XRP/USD ⭐ | 0.93894 | 80.95 | +0.48% | 3.83x | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 6 | SUI/USD ⭐ | 0.6659 | 72.50 | +0.67% | 1.40x | STRONG 91/100 | HIGH 55/100 | Watch |
| 7 | UNI/USD ⭐ | 4.8152 | 71.97 | +0.46% | 2.07x | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 8 | XDG/USD | 0.0557387 | 68.71 | +0.29% | 3.82x | STRONG 89/100 | HIGH 55/100 | Watch |
| 9 | NIGHT/USD ⭐ | 0.05014 | 67.73 | +0.18% | 1.62x | STRONG 79/100 | HIGH 55/100 | Watch |
| 10 | PAXG/USD ⭐ | 3612.15 | 67.68 | +0.22% | 2.48x | STRONG 99/100 | HIGH 55/100 | Consider small entry |
| 11 | XBT/USD ⭐ | 61555.9 | 66.08 | +0.29% | 1.55x | STRONG 88/100 | HIGH 55/100 | Consider small entry |
| 12 | BLESS/USD | 0.017862 | 61.32 | -0.88% | 0.50x | WEAK 26/100 | EXTREME 88/100 | Do nothing |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | JUP/USD ⭐ | 0.23962 | 83.50 | +1.96% | 2.28x | 3035 | STRONG 100/100 | HIGH 66/100 | Consider small entry |
| 2 | AI/USD ⭐ | 0.01629 | 82.55 | +1.31% | 12.12x | 3540 | STRONG 100/100 | VERY_HIGH 73/100 | Watch |
| 3 | SOL/USD ⭐ | 71.78 | 76.01 | +0.49% | 2.45x | 29816 | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 4 | NEAR/USD ⭐ | 3.0323 | 73.60 | +0.49% | 2.92x | 13422 | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 5 | XRP/USD ⭐ | 0.93754 | 72.89 | +0.48% | 3.83x | 20214 | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 6 | UNI/USD ⭐ | 4.798 | 69.30 | +0.46% | 2.07x | 4497 | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 7 | SUI/USD ⭐ | 0.6647 | 69.07 | +0.67% | 1.40x | 6419 | STRONG 90/100 | HIGH 55/100 | Watch |
| 8 | PAXG/USD ⭐ | 3609.94 | 64.77 | +0.22% | 2.48x | 6958 | STRONG 97/100 | HIGH 55/100 | Consider small entry |
| 9 | XBT/USD ⭐ | 61532.1 | 62.12 | +0.29% | 1.55x | 135000 | STRONG 86/100 | HIGH 55/100 | Consider small entry |
| 10 | NIGHT/USD ⭐ | 0.05012 | 60.69 | +0.18% | 1.62x | 10940 | STRONG 75/100 | HIGH 55/100 | Watch |
| 11 | ETH/USD | 1731.43 | 57.85 | +0.11% | 1.16x | 43443 | MODERATE 54/100 | HIGH 62/100 | Watch |

**Same-run overlap:** JUP/USD, AI/USD, NEAR/USD, SOL/USD, XRP/USD, SUI/USD, UNI/USD, NIGHT/USD, PAXG/USD, XBT/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
