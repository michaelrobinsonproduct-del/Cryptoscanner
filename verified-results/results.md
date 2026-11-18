# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-18T16:10:19.617004+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/44343928778
**Source SHA:** b271b90a2cae9e5307600070ce7d0e510fe68996
**Previous ledger commit:** e9f6ecdc4443578e96845c01440ed2a5d2960e06 (atomic ledger/results publication)
**Ledger generation:** 609 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 5s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 627; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 609; valid market observations: 609; OHLC screened: 15.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | SENT/USD | 0.019545 | 64.258 | 60.828 | +4.69% | -0.08% | 1.38x | 6.1 | 2026-11-18T16:10:14.117887+00:00 | Not calibrated | MODERATE 52/100 | VERY_HIGH 73/100 | Watch | WATCH |
| 2 | PROS/USD | 0.5686 | 52.692 | 63.659 | +10.00% | -0.91% | 0.36x | 24.5 | 2026-11-18T16:10:14.117887+00:00 | Not calibrated | WEAK 21/100 | EXTREME 100/100 | Do nothing | WATCH |
| 3 | TRUST/USD | 0.04921 | 49.309 | 59.950 | +4.37% | -0.49% | 0.18x | 6.1 | 2026-11-18T16:10:14.117887+00:00 | Not calibrated | WEAK 30/100 | VERY_HIGH 81/100 | Do nothing | WATCH |
| 4 | CT/USD | 0.1188 | 45.556 | 54.416 | +5.13% | -0.17% | 0.20x | 25.3 | 2026-11-18T16:10:14.117887+00:00 | Not calibrated | WEAK 18/100 | EXTREME 100/100 | Do nothing | WATCH |
| 5 | ZAMA/USD | 0.06079 | 38.353 | 37.519 | +1.44% | +0.40% | 0.89x | 8.3 | 2026-11-18T16:10:14.117887+00:00 | Not calibrated | MODERATE 49/100 | VERY_HIGH 74/100 | Watch | WATCH |
| 6 | TRX/USD | 0.309285 | 34.606 | 42.538 | +0.45% | +0.04% | 0.19x | 2.5 | 2026-11-18T16:10:14.117887+00:00 | Not calibrated | WEAK 37/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 7 | CC/USD | 0.08236 | 33.206 | 34.404 | +0.28% | +0.10% | 0.83x | 6.1 | 2026-11-18T16:10:14.117887+00:00 | Not calibrated | WEAK 37/100 | HIGH 67/100 | Watch | WATCH |
| 8 | MEGA/USD | 0.05275 | 27.840 | 34.816 | +2.15% | +0.51% | 0.05x | 22.7 | 2026-11-18T16:10:14.117887+00:00 | Not calibrated | WEAK 34/100 | EXTREME 94/100 | Do nothing | WATCH |
| 9 | AKE/USD | 0.01026701 | 27.704 | 40.540 | +2.83% | -1.38% | 0.41x | 25.5 | 2026-11-18T16:10:14.117887+00:00 | Not calibrated | WEAK 9/100 | EXTREME 97/100 | Do nothing | WATCH |
| 10 | FLR/USD | 0.00516 | 21.481 | 18.670 | +0.98% | +0.19% | 1.18x | 38.8 | 2026-11-18T16:10:14.117887+00:00 | Not calibrated | WEAK 21/100 | EXTREME 86/100 | Do nothing | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | PROS/USD | 63.659 | 0.5686 | -0.91% | 0.36x |
| 2 | SENT/USD | 60.828 | 0.019545 | -0.08% | 1.38x |
| 3 | TRUST/USD | 59.950 | 0.04921 | -0.49% | 0.18x |
| 4 | CT/USD | 54.416 | 0.1188 | -0.17% | 0.20x |
| 5 | TRX/USD | 42.538 | 0.309285 | +0.04% | 0.19x |
| 6 | AKE/USD | 40.540 | 0.01026701 | -1.38% | 0.41x |
| 7 | ZAMA/USD | 37.519 | 0.06079 | +0.40% | 0.89x |
| 8 | MEGA/USD | 34.816 | 0.05275 | +0.51% | 0.05x |
| 9 | CC/USD | 34.404 | 0.08236 | +0.10% | 0.83x |
| 10 | FLR/USD | 18.670 | 0.00516 | +0.19% | 1.18x |

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

- Persisted scans: 609; predictions: 5229; observations: 367888.
- Matured sampled outcomes across 1/6/24/48h: 4448; gap abstentions: 13125. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 0 (sampled only; not a success-rate estimate).
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

**Writer:** 44343928778 · **Generation:** 609 · **Legacy run:** 44343928778
**Main quote time:** 2026-11-18T16:10:19.617004+00:00 · **Legacy report time:** 2026-11-18T16:10:49.703054+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | SENT/USD | 0.019545 | 64.26 | -0.08% | 1.38x | MODERATE 52/100 | VERY_HIGH 73/100 | Watch |
| 2 | PROS/USD | 0.5686 | 52.69 | -0.91% | 0.36x | WEAK 21/100 | EXTREME 100/100 | Do nothing |
| 3 | TRUST/USD | 0.04921 | 49.31 | -0.49% | 0.18x | WEAK 30/100 | VERY_HIGH 81/100 | Do nothing |
| 4 | CT/USD | 0.1188 | 45.56 | -0.17% | 0.20x | WEAK 18/100 | EXTREME 100/100 | Do nothing |
| 5 | ZAMA/USD | 0.06079 | 38.35 | +0.40% | 0.89x | MODERATE 49/100 | VERY_HIGH 74/100 | Watch |
| 6 | TRX/USD | 0.309285 | 34.61 | +0.04% | 0.19x | WEAK 37/100 | VERY_HIGH 70/100 | Watch |
| 7 | CC/USD | 0.08236 | 33.21 | +0.10% | 0.83x | WEAK 37/100 | HIGH 67/100 | Watch |
| 8 | MEGA/USD | 0.05275 | 27.84 | +0.51% | 0.05x | WEAK 34/100 | EXTREME 94/100 | Do nothing |
| 9 | AKE/USD | 0.01026701 | 27.70 | -1.38% | 0.41x | WEAK 9/100 | EXTREME 97/100 | Do nothing |
| 10 | FLR/USD ⭐ | 0.00516 | 21.48 | +0.19% | 1.18x | WEAK 31/100 | EXTREME 86/100 | Do nothing |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | FLR/USD ⭐ | 0.00516 | 23.14 | +0.19% | 1.18x | 1120 | WEAK 32/100 | EXTREME 86/100 | Do nothing |

**Same-run overlap:** FLR/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
