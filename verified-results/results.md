# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-27T19:02:10.775253+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/46053453809
**Source SHA:** 858c8bc8ec5d7641ddb39cacd8aca91719f855b1
**Previous ledger commit:** bc1ba557ab36927ba2949208f7eef8ae9737ae91 (atomic ledger/results publication)
**Ledger generation:** 2047 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 7s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 628; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 610; valid market observations: 605; OHLC screened: 24.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | ZEC/USD | 745.17 | 97.092 | 99.933 | +9.32% | +0.38% | 0.53x | 0.1 | 2026-11-27T19:02:03.859165+00:00 | Not calibrated | STRONG 79/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 2 | FET/USD | 0.1264 | 81.615 | 64.227 | +4.98% | +0.48% | 2.78x | 15.8 | 2026-11-27T19:02:03.859165+00:00 | Not calibrated | STRONG 91/100 | HIGH 61/100 | Consider small entry | WATCH |
| 3 | RENDER/USD | 1.398 | 81.324 | 63.447 | +4.88% | +0.58% | 5.04x | 7.1 | 2026-11-27T19:02:03.859165+00:00 | Not calibrated | STRONG 96/100 | HIGH 60/100 | Consider small entry | WATCH |
| 4 | SOL/USD | 71.94 | 79.383 | 63.477 | +1.41% | +0.18% | 3.17x | 2.8 | 2026-11-27T19:02:03.859165+00:00 | Not calibrated | STRONG 85/100 | HIGH 55/100 | Watch | WATCH |
| 5 | UNI/USD | 4.8204 | 76.846 | 77.594 | +3.66% | +0.59% | 0.63x | 1.0 | 2026-11-27T19:02:03.859165+00:00 | Not calibrated | MODERATE 68/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 6 | XDG/USD | 0.057722 | 76.514 | 71.628 | +2.39% | +0.09% | 1.44x | 0.2 | 2026-11-27T19:02:03.859165+00:00 | Not calibrated | STRONG 73/100 | HIGH 55/100 | Watch | WATCH |
| 7 | NIGHT/USD | 0.04988 | 72.600 | 74.361 | +2.91% | +0.18% | 0.73x | 2.0 | 2026-11-27T19:02:03.859165+00:00 | Not calibrated | MODERATE 56/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 8 | HYPE/USD | 63.74 | 72.036 | 71.316 | +2.44% | +0.65% | 0.75x | 1.6 | 2026-11-27T19:02:03.859165+00:00 | Not calibrated | MODERATE 66/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 9 | LINK/USD | 9.38999 | 69.855 | 64.175 | +1.31% | +0.32% | 1.41x | 0.0 | 2026-11-27T19:02:03.859165+00:00 | Not calibrated | STRONG 80/100 | HIGH 55/100 | Watch | WATCH |
| 10 | SPACE/USD | 0.004324 | 69.294 | 61.923 | +11.67% | +1.19% | 1.14x | 27.9 | 2026-11-27T19:02:03.859165+00:00 | Not calibrated | MODERATE 60/100 | EXTREME 86/100 | Do nothing | WATCH |
| 11 | PIEVERSE/USD | 4.2206 | 64.058 | 64.747 | +8.64% | +1.22% | 0.32x | 35.5 | 2026-11-27T19:02:03.859165+00:00 | Not calibrated | MODERATE 47/100 | VERY_HIGH 82/100 | Watch | WATCH |
| 12 | SUI/USD | 0.6733 | 60.890 | 59.387 | +0.84% | +0.36% | 0.97x | 3.0 | 2026-11-27T19:02:03.859165+00:00 | Not calibrated | MODERATE 60/100 | HIGH 62/100 | Watch | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | ZEC/USD | 99.933 | 745.17 | +0.38% | 0.53x |
| 2 | UNI/USD | 77.594 | 4.8204 | +0.59% | 0.63x |
| 3 | NIGHT/USD | 74.361 | 0.04988 | +0.18% | 0.73x |
| 4 | XDG/USD | 71.628 | 0.057722 | +0.09% | 1.44x |
| 5 | HYPE/USD | 71.316 | 63.74 | +0.65% | 0.75x |
| 6 | PIEVERSE/USD | 64.747 | 4.2206 | +1.22% | 0.32x |
| 7 | FET/USD | 64.227 | 0.1264 | +0.48% | 2.78x |
| 8 | LINK/USD | 64.175 | 9.38999 | +0.32% | 1.41x |
| 9 | SOL/USD | 63.477 | 71.94 | +0.18% | 3.17x |
| 10 | RENDER/USD | 63.447 | 1.398 | +0.58% | 5.04x |
| 11 | SPACE/USD | 61.923 | 0.004324 | +1.19% | 1.14x |
| 12 | SUI/USD | 59.387 | 0.6733 | +0.36% | 0.97x |

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

- Persisted scans: 2047; predictions: 18266; observations: 1239544.
- Matured sampled outcomes across 1/6/24/48h: 41147; gap abstentions: 25968. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 153 (sampled only; not a success-rate estimate).
- False positives / missed movers: NOT VERIFIED without eligible continuous outcome coverage.
- Baseline vs challenger: recorded as-of; unbiased held-out lift NOT MEASURED.
- Online Kraken /USD stablecoin-base pairs excluded: 18 (counted from this scan's online AssetPairs metadata, not inferred from price).
- Stablecoin base exclusions: BRL1, BUSD, DAI, EUR, EURC, EUROP, EURQ, EURR, EURT, FDUSD, FRAX, GUSD, PYUSD, QCAD, RLUSD, TGBP, TUSD, USD, USD1, USDC, USDD, USDE, USDG, USDQ, USDR, USDS, USDT, ZUSD.
- DEX: NOT USED; no DEX freshness gate.
- OHLC screening abstentions: 3; details in immutable scan JSON artifact.
- Storage: ledger and results published in one non-force Git commit and read back. Independent artifact recovery is NOT VERIFIED by this scan alone.
- Errors: none in successful committed scan; a failed workflow must not publish a SUCCESS report.

# Cryptoscanner — challenger and independent legacy-inspired WATCH

Paper only · risk is high or higher · 30%+ in 48h probability NOT CALIBRATED
Signal confidence 0–100 means setup strength only, NOT a win probability. Actions are research guidance; no trade authorization.

**Writer:** 46053453809 · **Generation:** 2047 · **Legacy run:** 46053453809
**Main quote time:** 2026-11-27T19:02:10.775253+00:00 · **Legacy report time:** 2026-11-27T19:02:46.959003+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | ZEC/USD | 745.17 | 97.09 | +0.38% | 0.53x | STRONG 79/100 | VERY_HIGH 70/100 | Watch |
| 2 | FET/USD ⭐ | 0.1264 | 81.62 | +0.48% | 2.78x | STRONG 100/100 | HIGH 61/100 | Consider small entry |
| 3 | RENDER/USD ⭐ | 1.398 | 81.32 | +0.58% | 5.04x | STRONG 100/100 | HIGH 60/100 | Consider small entry |
| 4 | SOL/USD ⭐ | 71.94 | 79.38 | +0.18% | 3.17x | STRONG 95/100 | HIGH 55/100 | Watch |
| 5 | UNI/USD | 4.8204 | 76.85 | +0.59% | 0.63x | MODERATE 68/100 | VERY_HIGH 70/100 | Watch |
| 6 | XDG/USD ⭐ | 0.057722 | 76.51 | +0.09% | 1.44x | STRONG 83/100 | HIGH 55/100 | Watch |
| 7 | NIGHT/USD | 0.04988 | 72.60 | +0.18% | 0.73x | MODERATE 56/100 | VERY_HIGH 70/100 | Watch |
| 8 | HYPE/USD | 63.74 | 72.04 | +0.65% | 0.75x | MODERATE 66/100 | VERY_HIGH 70/100 | Watch |
| 9 | LINK/USD | 9.38999 | 69.85 | +0.32% | 1.41x | STRONG 80/100 | HIGH 55/100 | Watch |
| 10 | SPACE/USD ⭐ | 0.004324 | 69.29 | +1.19% | 1.14x | STRONG 70/100 | EXTREME 86/100 | Do nothing |
| 11 | PIEVERSE/USD | 4.2206 | 64.06 | +1.22% | 0.32x | MODERATE 47/100 | VERY_HIGH 82/100 | Watch |
| 12 | SUI/USD | 0.6733 | 60.89 | +0.36% | 0.97x | MODERATE 60/100 | HIGH 62/100 | Watch |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | FET/USD ⭐ | 0.1268 | 82.91 | +0.48% | 2.78x | 3773 | STRONG 96/100 | HIGH 67/100 | Consider small entry |
| 2 | XDG/USD ⭐ | 0.057795 | 78.20 | +0.09% | 1.44x | 13125 | STRONG 84/100 | HIGH 55/100 | Watch |
| 3 | SOL/USD ⭐ | 72.03 | 76.20 | +0.18% | 3.17x | 45382 | STRONG 93/100 | HIGH 55/100 | Watch |
| 4 | RENDER/USD ⭐ | 1.4 | 74.35 | +0.58% | 5.04x | 1784 | STRONG 97/100 | HIGH 66/100 | Consider small entry |
| 5 | SPACE/USD ⭐ | 0.004324 | 74.29 | +1.19% | 1.14x | 2595 | STRONG 82/100 | VERY_HIGH 74/100 | Watch |

**Same-run overlap:** FET/USD, RENDER/USD, SOL/USD, XDG/USD, SPACE/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
