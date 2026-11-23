# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-23T05:31:38.146102+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/45118106399
**Source SHA:** 858c8bc8ec5d7641ddb39cacd8aca91719f855b1
**Previous ledger commit:** cc8e328b1e4322e1c1dd4506ec6829c0837e82dd (atomic ledger/results publication)
**Ledger generation:** 1387 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 7s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 628; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 610; valid market observations: 609; OHLC screened: 24.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | AI/USD | 0.01616 | 99.397 | 73.040 | +10.53% | +2.27% | 4.76x | 6.2 | 2026-11-23T05:31:31.213561+00:00 | Not calibrated | STRONG 100/100 | HIGH 67/100 | Consider small entry | WATCH |
| 2 | JUP/USD | 0.23749 | 82.029 | 67.114 | +5.75% | +1.50% | 1.74x | 14.3 | 2026-11-23T05:31:31.213561+00:00 | Not calibrated | STRONG 81/100 | HIGH 66/100 | Consider small entry | WATCH |
| 3 | NEAR/USD | 3.0283 | 75.931 | 64.290 | +1.56% | +0.59% | 1.87x | 3.3 | 2026-11-23T05:31:31.213561+00:00 | Not calibrated | STRONG 83/100 | HIGH 55/100 | Consider small entry | WATCH |
| 4 | SUI/USD | 0.6624 | 74.551 | 61.398 | +1.02% | +0.58% | 2.03x | 1.5 | 2026-11-23T05:31:31.213561+00:00 | Not calibrated | STRONG 92/100 | HIGH 55/100 | Consider small entry | WATCH |
| 5 | UNI/USD | 4.7951 | 72.596 | 55.378 | +2.43% | +0.81% | 2.32x | 5.6 | 2026-11-23T05:31:31.213561+00:00 | Not calibrated | STRONG 91/100 | HIGH 55/100 | Consider small entry | WATCH |
| 6 | SOL/USD | 71.67 | 71.981 | 64.610 | +1.47% | +0.43% | 1.52x | 1.4 | 2026-11-23T05:31:31.213561+00:00 | Not calibrated | STRONG 81/100 | HIGH 55/100 | Consider small entry | WATCH |
| 7 | CC/USD | 0.07555 | 70.983 | 55.586 | +3.11% | +0.08% | 2.75x | 2.6 | 2026-11-23T05:31:31.213561+00:00 | Not calibrated | STRONG 80/100 | HIGH 60/100 | Watch | WATCH |
| 8 | XRP/USD | 0.93511 | 70.336 | 60.339 | +0.82% | +0.23% | 1.89x | 0.7 | 2026-11-23T05:31:31.213561+00:00 | Not calibrated | STRONG 80/100 | HIGH 55/100 | Consider small entry | WATCH |
| 9 | XDG/USD | 0.0555799 | 67.764 | 50.498 | +0.54% | +0.45% | 3.11x | 0.0 | 2026-11-23T05:31:31.213561+00:00 | Not calibrated | STRONG 89/100 | HIGH 55/100 | Watch | WATCH |
| 10 | PAXG/USD | 3610.07 | 66.914 | 51.475 | +1.06% | +0.26% | 2.42x | 0.7 | 2026-11-23T05:31:31.213561+00:00 | Not calibrated | STRONG 88/100 | HIGH 55/100 | Watch | WATCH |
| 11 | XBT/USD | 61470.8 | 57.241 | 58.433 | +0.49% | +0.49% | 0.63x | 0.0 | 2026-11-23T05:31:31.213561+00:00 | Not calibrated | MODERATE 59/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 12 | ADA/USD | 0.145162 | 57.074 | 48.108 | +0.39% | +0.36% | 1.72x | 4.1 | 2026-11-23T05:31:31.213561+00:00 | Not calibrated | STRONG 74/100 | HIGH 55/100 | Watch | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | AI/USD | 73.040 | 0.01616 | +2.27% | 4.76x |
| 2 | JUP/USD | 67.114 | 0.23749 | +1.50% | 1.74x |
| 3 | SOL/USD | 64.610 | 71.67 | +0.43% | 1.52x |
| 4 | NEAR/USD | 64.290 | 3.0283 | +0.59% | 1.87x |
| 5 | SUI/USD | 61.398 | 0.6624 | +0.58% | 2.03x |
| 6 | XRP/USD | 60.339 | 0.93511 | +0.23% | 1.89x |
| 7 | XBT/USD | 58.433 | 61470.8 | +0.49% | 0.63x |
| 8 | CC/USD | 55.586 | 0.07555 | +0.08% | 2.75x |
| 9 | UNI/USD | 55.378 | 4.7951 | +0.81% | 2.32x |
| 10 | PAXG/USD | 51.475 | 3610.07 | +0.26% | 2.42x |
| 11 | XDG/USD | 50.498 | 0.0555799 | +0.45% | 3.11x |
| 12 | ADA/USD | 48.108 | 0.145162 | +0.36% | 1.72x |

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

- Persisted scans: 1387; predictions: 11411; observations: 839787.
- Matured sampled outcomes across 1/6/24/48h: 18484; gap abstentions: 22370. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 108 (sampled only; not a success-rate estimate).
- False positives / missed movers: NOT VERIFIED without eligible continuous outcome coverage.
- Baseline vs challenger: recorded as-of; unbiased held-out lift NOT MEASURED.
- Online Kraken /USD stablecoin-base pairs excluded: 18 (counted from this scan's online AssetPairs metadata, not inferred from price).
- Stablecoin base exclusions: BRL1, BUSD, DAI, EUR, EURC, EUROP, EURQ, EURR, EURT, FDUSD, FRAX, GUSD, PYUSD, QCAD, RLUSD, TGBP, TUSD, USD, USD1, USDC, USDD, USDE, USDG, USDQ, USDR, USDS, USDT, ZUSD.
- DEX: NOT USED; no DEX freshness gate.
- OHLC screening abstentions: 5; details in immutable scan JSON artifact.
- Storage: ledger and results published in one non-force Git commit and read back. Independent artifact recovery is NOT VERIFIED by this scan alone.
- Errors: none in successful committed scan; a failed workflow must not publish a SUCCESS report.

# Cryptoscanner — challenger and independent legacy-inspired WATCH

Paper only · risk is high or higher · 30%+ in 48h probability NOT CALIBRATED
Signal confidence 0–100 means setup strength only, NOT a win probability. Actions are research guidance; no trade authorization.

**Writer:** 45118106399 · **Generation:** 1387 · **Legacy run:** 45118106399
**Main quote time:** 2026-11-23T05:31:38.146102+00:00 · **Legacy report time:** 2026-11-23T05:32:40.387634+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | AI/USD ⭐ | 0.01616 | 99.40 | +2.27% | 4.76x | STRONG 100/100 | HIGH 67/100 | Consider small entry |
| 2 | JUP/USD ⭐ | 0.23749 | 82.03 | +1.50% | 1.74x | STRONG 91/100 | HIGH 66/100 | Consider small entry |
| 3 | NEAR/USD ⭐ | 3.0283 | 75.93 | +0.59% | 1.87x | STRONG 93/100 | HIGH 55/100 | Consider small entry |
| 4 | SUI/USD ⭐ | 0.6624 | 74.55 | +0.58% | 2.03x | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 5 | UNI/USD ⭐ | 4.7951 | 72.60 | +0.81% | 2.32x | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 6 | SOL/USD ⭐ | 71.67 | 71.98 | +0.43% | 1.52x | STRONG 91/100 | HIGH 55/100 | Consider small entry |
| 7 | CC/USD ⭐ | 0.07555 | 70.98 | +0.08% | 2.75x | STRONG 90/100 | HIGH 60/100 | Watch |
| 8 | XRP/USD ⭐ | 0.93511 | 70.34 | +0.23% | 1.89x | STRONG 90/100 | HIGH 55/100 | Consider small entry |
| 9 | XDG/USD | 0.0555799 | 67.76 | +0.45% | 3.11x | STRONG 89/100 | HIGH 55/100 | Watch |
| 10 | PAXG/USD ⭐ | 3610.07 | 66.91 | +0.26% | 2.42x | STRONG 98/100 | HIGH 55/100 | Consider small entry |
| 11 | XBT/USD | 61470.8 | 57.24 | +0.49% | 0.63x | MODERATE 59/100 | VERY_HIGH 70/100 | Watch |
| 12 | ADA/USD | 0.145162 | 57.07 | +0.36% | 1.72x | STRONG 74/100 | HIGH 55/100 | Watch |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | AI/USD ⭐ | 0.01608 | 85.49 | +2.27% | 4.76x | 3685 | STRONG 100/100 | VERY_HIGH 73/100 | Watch |
| 2 | JUP/USD ⭐ | 0.23774 | 79.87 | +1.50% | 1.74x | 2981 | STRONG 90/100 | HIGH 66/100 | Consider small entry |
| 3 | CC/USD ⭐ | 0.07551 | 73.42 | +0.08% | 2.75x | 4139 | STRONG 92/100 | HIGH 60/100 | Watch |
| 4 | UNI/USD ⭐ | 4.8058 | 73.33 | +0.81% | 2.32x | 4490 | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 5 | SOL/USD ⭐ | 71.59 | 68.90 | +0.43% | 1.52x | 29709 | STRONG 89/100 | HIGH 55/100 | Consider small entry |
| 6 | NEAR/USD ⭐ | 3.0305 | 67.63 | +0.59% | 1.87x | 13459 | STRONG 89/100 | HIGH 55/100 | Consider small entry |
| 7 | SUI/USD ⭐ | 0.6622 | 66.71 | +0.58% | 2.03x | 6302 | STRONG 98/100 | HIGH 55/100 | Consider small entry |
| 8 | XRP/USD ⭐ | 0.93469 | 64.83 | +0.23% | 1.89x | 20151 | STRONG 87/100 | HIGH 55/100 | Consider small entry |
| 9 | PAXG/USD ⭐ | 3608.42 | 64.17 | +0.26% | 2.42x | 6984 | STRONG 97/100 | HIGH 55/100 | Consider small entry |
| 10 | LINK/USD | 8.923 | 62.86 | +0.39% | 1.23x | 4742 | MODERATE 66/100 | HIGH 62/100 | Watch |

**Same-run overlap:** AI/USD, JUP/USD, NEAR/USD, SUI/USD, UNI/USD, SOL/USD, CC/USD, XRP/USD, PAXG/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
