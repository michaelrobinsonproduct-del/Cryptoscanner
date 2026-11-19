# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-19T06:20:27.060169+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/44471331978
**Source SHA:** b271b90a2cae9e5307600070ce7d0e510fe68996
**Previous ledger commit:** 723ba7422c39c20ac561abdd754428272e2b5589 (atomic ledger/results publication)
**Ledger generation:** 775 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 6s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 627; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 609; valid market observations: 609; OHLC screened: 24.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | LIGHTER/USD | 2.909 | 97.919 | 74.739 | +7.18% | +1.64% | 3.38x | 13.7 | 2026-11-19T06:20:21.167299+00:00 | Not calibrated | STRONG 99/100 | HIGH 66/100 | Consider small entry | WATCH |
| 2 | VVV/USD | 22.969 | 93.574 | 93.768 | +5.99% | +0.35% | 0.81x | 5.7 | 2026-11-19T06:20:21.167299+00:00 | Not calibrated | STRONG 77/100 | HIGH 62/100 | Watch | WATCH |
| 3 | SOL/USD | 74.84 | 81.907 | 66.706 | +1.77% | +0.04% | 2.73x | 1.3 | 2026-11-19T06:20:21.167299+00:00 | Not calibrated | STRONG 86/100 | HIGH 55/100 | Watch | WATCH |
| 4 | USELESS/USD | 0.10469 | 80.415 | 73.508 | +9.55% | +2.47% | 0.45x | 20.1 | 2026-11-19T06:20:21.167299+00:00 | Not calibrated | MODERATE 60/100 | VERY_HIGH 82/100 | Watch | WATCH |
| 5 | NEAR/USD | 3.3971 | 74.265 | 73.813 | +3.02% | -0.04% | 1.06x | 4.7 | 2026-11-19T06:20:21.167299+00:00 | Not calibrated | MODERATE 47/100 | HIGH 68/100 | Watch | WATCH |
| 6 | ZEC/USD | 940.95 | 74.029 | 77.207 | +3.18% | -0.23% | 0.80x | 0.1 | 2026-11-19T06:20:21.167299+00:00 | Not calibrated | WEAK 42/100 | HIGH 68/100 | Watch | WATCH |
| 7 | ETH/USD | 1801.65 | 69.665 | 65.578 | +1.52% | -0.02% | 1.42x | 0.1 | 2026-11-19T06:20:21.167299+00:00 | Not calibrated | MODERATE 55/100 | HIGH 61/100 | Watch | WATCH |
| 8 | XRP/USD | 0.97712 | 64.566 | 62.736 | +1.11% | +0.13% | 1.12x | 0.1 | 2026-11-19T06:20:21.167299+00:00 | Not calibrated | MODERATE 57/100 | HIGH 62/100 | Watch | WATCH |
| 9 | TAO/USD | 196.2 | 62.842 | 68.520 | +2.21% | +0.15% | 0.36x | 3.9 | 2026-11-19T06:20:21.167299+00:00 | Not calibrated | MODERATE 51/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 10 | HYPE/USD | 68.13 | 61.464 | 67.349 | +1.87% | +0.03% | 0.40x | 1.5 | 2026-11-19T06:20:21.167299+00:00 | Not calibrated | MODERATE 51/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 11 | ADA/USD | 0.15356 | 59.110 | 64.403 | +1.52% | +0.20% | 0.37x | 2.5 | 2026-11-19T06:20:21.167299+00:00 | Not calibrated | MODERATE 60/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 12 | LINK/USD | 9.13519 | 57.811 | 59.743 | +0.69% | -0.02% | 0.82x | 0.2 | 2026-11-19T06:20:21.167299+00:00 | Not calibrated | WEAK 34/100 | HIGH 68/100 | Do nothing | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | VVV/USD | 93.768 | 22.969 | +0.35% | 0.81x |
| 2 | ZEC/USD | 77.207 | 940.95 | -0.23% | 0.80x |
| 3 | LIGHTER/USD | 74.739 | 2.909 | +1.64% | 3.38x |
| 4 | NEAR/USD | 73.813 | 3.3971 | -0.04% | 1.06x |
| 5 | USELESS/USD | 73.508 | 0.10469 | +2.47% | 0.45x |
| 6 | TAO/USD | 68.520 | 196.2 | +0.15% | 0.36x |
| 7 | HYPE/USD | 67.349 | 68.13 | +0.03% | 0.40x |
| 8 | SOL/USD | 66.706 | 74.84 | +0.04% | 2.73x |
| 9 | ETH/USD | 65.578 | 1801.65 | -0.02% | 1.42x |
| 10 | ADA/USD | 64.403 | 0.15356 | +0.20% | 0.37x |
| 11 | XRP/USD | 62.736 | 0.97712 | +0.13% | 1.12x |
| 12 | LINK/USD | 59.743 | 9.13519 | -0.02% | 0.82x |

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

- Persisted scans: 775; predictions: 6444; observations: 468981.
- Matured sampled outcomes across 1/6/24/48h: 6511; gap abstentions: 13838. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 10 (sampled only; not a success-rate estimate).
- False positives / missed movers: NOT VERIFIED without eligible continuous outcome coverage.
- Baseline vs challenger: recorded as-of; unbiased held-out lift NOT MEASURED.
- Online Kraken /USD stablecoin-base pairs excluded: 18 (counted from this scan's online AssetPairs metadata, not inferred from price).
- Stablecoin base exclusions: BRL1, BUSD, DAI, EUR, EURC, EUROP, EURQ, EURR, EURT, FDUSD, FRAX, GUSD, PYUSD, QCAD, RLUSD, TGBP, TUSD, USD, USD1, USDC, USDD, USDE, USDG, USDQ, USDR, USDS, USDT, ZUSD.
- DEX: NOT USED; no DEX freshness gate.
- OHLC screening abstentions: 7; details in immutable scan JSON artifact.
- Storage: ledger and results published in one non-force Git commit and read back. Independent artifact recovery is NOT VERIFIED by this scan alone.
- Errors: none in successful committed scan; a failed workflow must not publish a SUCCESS report.

# Cryptoscanner — challenger and independent legacy-inspired WATCH

Paper only · risk is high or higher · 30%+ in 48h probability NOT CALIBRATED
Signal confidence 0–100 means setup strength only, NOT a win probability. Actions are research guidance; no trade authorization.

**Writer:** 44471331978 · **Generation:** 775 · **Legacy run:** 44471331978
**Main quote time:** 2026-11-19T06:20:27.060169+00:00 · **Legacy report time:** 2026-11-19T06:21:03.925616+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | LIGHTER/USD ⭐ | 2.909 | 97.92 | +1.64% | 3.38x | STRONG 100/100 | HIGH 66/100 | Consider small entry |
| 2 | VVV/USD | 22.969 | 93.57 | +0.35% | 0.81x | STRONG 77/100 | HIGH 62/100 | Watch |
| 3 | SOL/USD | 74.84 | 81.91 | +0.04% | 2.73x | STRONG 86/100 | HIGH 55/100 | Watch |
| 4 | USELESS/USD | 0.10469 | 80.42 | +2.47% | 0.45x | MODERATE 60/100 | VERY_HIGH 82/100 | Watch |
| 5 | NEAR/USD | 3.3971 | 74.27 | -0.04% | 1.06x | MODERATE 47/100 | HIGH 68/100 | Watch |
| 6 | ZEC/USD | 940.95 | 74.03 | -0.23% | 0.80x | WEAK 42/100 | HIGH 68/100 | Watch |
| 7 | ETH/USD | 1801.65 | 69.67 | -0.02% | 1.42x | MODERATE 55/100 | HIGH 61/100 | Watch |
| 8 | XRP/USD ⭐ | 0.97712 | 64.57 | +0.13% | 1.12x | MODERATE 67/100 | HIGH 62/100 | Watch |
| 9 | TAO/USD | 196.2 | 62.84 | +0.15% | 0.36x | MODERATE 51/100 | VERY_HIGH 70/100 | Watch |
| 10 | HYPE/USD | 68.13 | 61.46 | +0.03% | 0.40x | MODERATE 51/100 | VERY_HIGH 70/100 | Watch |
| 11 | ADA/USD | 0.15356 | 59.11 | +0.20% | 0.37x | MODERATE 60/100 | VERY_HIGH 70/100 | Watch |
| 12 | LINK/USD | 9.13519 | 57.81 | -0.02% | 0.82x | WEAK 34/100 | HIGH 68/100 | Do nothing |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | LIGHTER/USD ⭐ | 2.915 | 86.90 | +1.64% | 3.38x | 4207 | STRONG 100/100 | HIGH 66/100 | Consider small entry |
| 2 | XRP/USD ⭐ | 0.97817 | 67.31 | +0.13% | 1.12x | 36707 | MODERATE 69/100 | HIGH 62/100 | Watch |

**Same-run overlap:** LIGHTER/USD, XRP/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
