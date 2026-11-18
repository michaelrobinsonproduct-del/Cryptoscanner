# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-18T06:10:09.878807+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/44249271125
**Source SHA:** 394c17eeb7071fba40e02dbbb1ea97cedb3a0a8a
**Previous ledger commit:** 1803da19ded110affaede5d9ebcf0f9887f123f5 (atomic ledger/results publication)
**Ledger generation:** 551 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 7s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 627; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 609; valid market observations: 609; OHLC screened: 22.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | SENT/USD | 0.019822 | 95.653 | 72.475 | +6.18% | +1.64% | 3.71x | 3.5 | 2026-11-18T06:10:02.666601+00:00 | Not calibrated | STRONG 100/100 | HIGH 67/100 | Consider small entry | WATCH |
| 2 | CC/USD | 0.08467 | 67.774 | 53.790 | +3.09% | +0.09% | 2.35x | 7.1 | 2026-11-18T06:10:02.666601+00:00 | Not calibrated | STRONG 79/100 | HIGH 60/100 | Watch | WATCH |
| 3 | VVV/USD | 21.303 | 65.843 | 54.239 | +1.32% | +0.37% | 1.97x | 7.0 | 2026-11-18T06:10:02.666601+00:00 | Not calibrated | STRONG 78/100 | HIGH 55/100 | Watch | WATCH |
| 4 | ICNT/USD | 0.2869 | 61.126 | 53.502 | +3.91% | +0.46% | 1.53x | 14.0 | 2026-11-18T06:10:02.666601+00:00 | Not calibrated | STRONG 71/100 | HIGH 66/100 | Watch | WATCH |
| 5 | NEAR/USD | 3.41 | 54.158 | 57.543 | +0.51% | +0.59% | 0.36x | 2.1 | 2026-11-18T06:10:02.666601+00:00 | Not calibrated | MODERATE 57/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 6 | PEARL/USD | 1.847 | 42.658 | 46.146 | +2.02% | -0.10% | 0.70x | 5.4 | 2026-11-18T06:10:02.666601+00:00 | Not calibrated | WEAK 26/100 | VERY_HIGH 81/100 | Do nothing | WATCH |
| 7 | MNT/USD | 0.3787 | 39.966 | 39.039 | +1.45% | +0.32% | 0.93x | 7.9 | 2026-11-18T06:10:02.666601+00:00 | Not calibrated | MODERATE 50/100 | HIGH 67/100 | Watch | WATCH |
| 8 | BLESS/USD | 0.01016 | 36.642 | 22.994 | +1.86% | +0.04% | 2.35x | 43.8 | 2026-11-18T06:10:02.666601+00:00 | Not calibrated | MODERATE 48/100 | VERY_HIGH 82/100 | Watch | WATCH |
| 9 | AKT/USD | 0.514 | 31.996 | 36.931 | +0.92% | -0.98% | 1.00x | 3.9 | 2026-11-18T06:10:02.666601+00:00 | Not calibrated | WEAK 21/100 | VERY_HIGH 73/100 | Do nothing | WATCH |
| 10 | CT/USD | 0.1151 | 25.369 | 35.274 | +1.86% | -0.26% | 0.14x | 17.4 | 2026-11-18T06:10:02.666601+00:00 | Not calibrated | WEAK 13/100 | EXTREME 94/100 | Do nothing | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | SENT/USD | 72.475 | 0.019822 | +1.64% | 3.71x |
| 2 | NEAR/USD | 57.543 | 3.41 | +0.59% | 0.36x |
| 3 | VVV/USD | 54.239 | 21.303 | +0.37% | 1.97x |
| 4 | CC/USD | 53.790 | 0.08467 | +0.09% | 2.35x |
| 5 | ICNT/USD | 53.502 | 0.2869 | +0.46% | 1.53x |
| 6 | PEARL/USD | 46.146 | 1.847 | -0.10% | 0.70x |
| 7 | MNT/USD | 39.039 | 0.3787 | +0.32% | 0.93x |
| 8 | AKT/USD | 36.931 | 0.514 | -0.98% | 1.00x |
| 9 | CT/USD | 35.274 | 0.1151 | -0.26% | 0.14x |
| 10 | BLESS/USD | 22.994 | 0.01016 | +0.04% | 2.35x |

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

- Persisted scans: 551; predictions: 4652; observations: 332566.
- Matured sampled outcomes across 1/6/24/48h: 3890; gap abstentions: 12463. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 0 (sampled only; not a success-rate estimate).
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

**Writer:** 44249271125 · **Generation:** 551 · **Legacy run:** 44249271125
**Main quote time:** 2026-11-18T06:10:09.878807+00:00 · **Legacy report time:** 2026-11-18T06:10:28.283683+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | SENT/USD ⭐ | 0.019822 | 95.65 | +1.64% | 3.71x | STRONG 100/100 | HIGH 67/100 | Consider small entry |
| 2 | CC/USD ⭐ | 0.08467 | 67.77 | +0.09% | 2.35x | STRONG 89/100 | HIGH 60/100 | Watch |
| 3 | VVV/USD ⭐ | 21.303 | 65.84 | +0.37% | 1.97x | STRONG 88/100 | HIGH 55/100 | Consider small entry |
| 4 | ICNT/USD ⭐ | 0.2869 | 61.13 | +0.46% | 1.53x | STRONG 81/100 | HIGH 66/100 | Consider small entry |
| 5 | NEAR/USD | 3.41 | 54.16 | +0.59% | 0.36x | MODERATE 57/100 | VERY_HIGH 70/100 | Watch |
| 6 | PEARL/USD | 1.847 | 42.66 | -0.10% | 0.70x | WEAK 26/100 | VERY_HIGH 81/100 | Do nothing |
| 7 | MNT/USD | 0.3787 | 39.97 | +0.32% | 0.93x | MODERATE 50/100 | HIGH 67/100 | Watch |
| 8 | BLESS/USD | 0.01016 | 36.64 | +0.04% | 2.35x | MODERATE 48/100 | VERY_HIGH 82/100 | Watch |
| 9 | AKT/USD | 0.514 | 32.00 | -0.98% | 1.00x | WEAK 21/100 | VERY_HIGH 73/100 | Do nothing |
| 10 | CT/USD | 0.1151 | 25.37 | -0.26% | 0.14x | WEAK 13/100 | EXTREME 94/100 | Do nothing |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | SENT/USD ⭐ | 0.019857 | 83.51 | +1.64% | 3.71x | 4553 | STRONG 100/100 | HIGH 67/100 | Consider small entry |
| 2 | CC/USD ⭐ | 0.08467 | 76.13 | +0.09% | 2.35x | 4363 | STRONG 93/100 | HIGH 60/100 | Watch |
| 3 | ICNT/USD ⭐ | 0.2871 | 75.18 | +0.46% | 1.53x | 4654 | STRONG 83/100 | VERY_HIGH 72/100 | Watch |
| 4 | VVV/USD ⭐ | 21.303 | 53.94 | +0.37% | 1.97x | 7374 | STRONG 82/100 | HIGH 55/100 | Consider small entry |

**Same-run overlap:** SENT/USD, CC/USD, VVV/USD, ICNT/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
