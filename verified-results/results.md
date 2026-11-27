# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-27T20:22:11.005083+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/46062851743
**Source SHA:** 858c8bc8ec5d7641ddb39cacd8aca91719f855b1
**Previous ledger commit:** 6d9957319db6d911147aa73d797dcb53a2abc2d6 (atomic ledger/results publication)
**Ledger generation:** 2055 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 8s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 628; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 610; valid market observations: 605; OHLC screened: 24.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | ZEC/USD | 740.35 | 112.963 | 99.933 | +8.61% | -0.39% | 2.54x | 0.1 | 2026-11-27T20:22:03.158163+00:00 | Not calibrated | STRONG 80/100 | HIGH 61/100 | Watch | WATCH |
| 2 | SKY/USD | 0.04963 | 84.975 | 78.349 | +6.94% | +1.42% | 0.95x | 4.0 | 2026-11-27T20:22:03.158163+00:00 | Not calibrated | STRONG 72/100 | HIGH 67/100 | Watch | WATCH |
| 3 | NIGHT/USD | 0.05038 | 84.844 | 80.599 | +3.94% | +0.36% | 1.25x | 4.0 | 2026-11-27T20:22:03.158163+00:00 | Not calibrated | STRONG 77/100 | HIGH 62/100 | Watch | WATCH |
| 4 | XDG/USD | 0.0575699 | 83.899 | 69.782 | +2.12% | -0.18% | 3.38x | 0.1 | 2026-11-27T20:22:03.158163+00:00 | Not calibrated | STRONG 72/100 | HIGH 61/100 | Watch | WATCH |
| 5 | HYPE/USD | 63.98 | 73.701 | 73.237 | +2.83% | +0.05% | 1.02x | 3.1 | 2026-11-27T20:22:03.158163+00:00 | Not calibrated | MODERATE 62/100 | HIGH 62/100 | Watch | WATCH |
| 6 | UNI/USD | 4.8349 | 73.498 | 80.398 | +3.97% | +0.02% | 0.30x | 0.2 | 2026-11-27T20:22:03.158163+00:00 | Not calibrated | MODERATE 57/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 7 | SOL/USD | 71.99 | 73.488 | 64.666 | +1.48% | +0.01% | 1.88x | 1.4 | 2026-11-27T20:22:03.158163+00:00 | Not calibrated | STRONG 72/100 | HIGH 55/100 | Watch | WATCH |
| 8 | SUI/USD | 0.6719 | 72.619 | 58.659 | +0.63% | -0.21% | 4.12x | 1.5 | 2026-11-27T20:22:03.158163+00:00 | Not calibrated | MODERATE 66/100 | HIGH 61/100 | Watch | WATCH |
| 9 | RENDER/USD | 1.403 | 59.802 | 62.562 | +5.25% | +0.07% | 0.69x | 14.3 | 2026-11-27T20:22:03.158163+00:00 | Not calibrated | MODERATE 45/100 | VERY_HIGH 81/100 | Watch | WATCH |
| 10 | PAXG/USD | 3644.02 | 57.788 | 59.505 | +2.45% | +0.02% | 0.82x | 1.5 | 2026-11-27T20:22:03.158163+00:00 | Not calibrated | MODERATE 49/100 | HIGH 62/100 | Watch | WATCH |
| 11 | ADA/USD | 0.148954 | 57.745 | 54.326 | +0.33% | -0.11% | 1.40x | 3.8 | 2026-11-27T20:22:03.158163+00:00 | Not calibrated | MODERATE 49/100 | HIGH 61/100 | Watch | WATCH |
| 12 | JUP/USD | 0.24841 | 56.642 | 62.639 | +5.00% | +0.01% | 0.40x | 10.9 | 2026-11-27T20:22:03.158163+00:00 | Not calibrated | WEAK 43/100 | VERY_HIGH 81/100 | Watch | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | ZEC/USD | 99.933 | 740.35 | -0.39% | 2.54x |
| 2 | NIGHT/USD | 80.599 | 0.05038 | +0.36% | 1.25x |
| 3 | UNI/USD | 80.398 | 4.8349 | +0.02% | 0.30x |
| 4 | SKY/USD | 78.349 | 0.04963 | +1.42% | 0.95x |
| 5 | HYPE/USD | 73.237 | 63.98 | +0.05% | 1.02x |
| 6 | XDG/USD | 69.782 | 0.0575699 | -0.18% | 3.38x |
| 7 | SOL/USD | 64.666 | 71.99 | +0.01% | 1.88x |
| 8 | JUP/USD | 62.639 | 0.24841 | +0.01% | 0.40x |
| 9 | RENDER/USD | 62.562 | 1.403 | +0.07% | 0.69x |
| 10 | PAXG/USD | 59.505 | 3644.02 | +0.02% | 0.82x |
| 11 | SUI/USD | 58.659 | 0.6719 | -0.21% | 4.12x |
| 12 | ADA/USD | 54.326 | 0.148954 | -0.11% | 1.40x |

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

- Persisted scans: 2055; predictions: 18362; observations: 1244384.
- Matured sampled outcomes across 1/6/24/48h: 41531; gap abstentions: 25968. Per-horizon counts require independent audit; do not infer held-out lift.
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

**Writer:** 46062851743 · **Generation:** 2055 · **Legacy run:** 46062851743
**Main quote time:** 2026-11-27T20:22:11.005083+00:00 · **Legacy report time:** 2026-11-27T20:22:47.039735+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | ZEC/USD | 740.35 | 112.96 | -0.39% | 2.54x | STRONG 80/100 | HIGH 61/100 | Watch |
| 2 | SKY/USD | 0.04963 | 84.98 | +1.42% | 0.95x | STRONG 72/100 | HIGH 67/100 | Watch |
| 3 | NIGHT/USD ⭐ | 0.05038 | 84.84 | +0.36% | 1.25x | STRONG 87/100 | HIGH 62/100 | Watch |
| 4 | XDG/USD | 0.0575699 | 83.90 | -0.18% | 3.38x | STRONG 72/100 | HIGH 61/100 | Watch |
| 5 | HYPE/USD | 63.98 | 73.70 | +0.05% | 1.02x | MODERATE 62/100 | HIGH 62/100 | Watch |
| 6 | UNI/USD | 4.8349 | 73.50 | +0.02% | 0.30x | MODERATE 57/100 | VERY_HIGH 70/100 | Watch |
| 7 | SOL/USD | 71.99 | 73.49 | +0.01% | 1.88x | STRONG 72/100 | HIGH 55/100 | Watch |
| 8 | SUI/USD | 0.6719 | 72.62 | -0.21% | 4.12x | MODERATE 66/100 | HIGH 61/100 | Watch |
| 9 | RENDER/USD | 1.403 | 59.80 | +0.07% | 0.69x | MODERATE 45/100 | VERY_HIGH 81/100 | Watch |
| 10 | PAXG/USD | 3644.02 | 57.79 | +0.02% | 0.82x | MODERATE 49/100 | HIGH 62/100 | Watch |
| 11 | ADA/USD | 0.148954 | 57.74 | -0.11% | 1.40x | MODERATE 49/100 | HIGH 61/100 | Watch |
| 12 | JUP/USD | 0.24841 | 56.64 | +0.01% | 0.40x | WEAK 43/100 | VERY_HIGH 81/100 | Watch |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | NIGHT/USD ⭐ | 0.05038 | 89.43 | +0.36% | 1.25x | 18093 | STRONG 90/100 | HIGH 62/100 | Watch |

**Same-run overlap:** NIGHT/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
