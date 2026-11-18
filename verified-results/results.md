# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-18T05:30:09.548915+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/44244615566
**Source SHA:** 394c17eeb7071fba40e02dbbb1ea97cedb3a0a8a
**Previous ledger commit:** 28cb1e15c86b25fe6a71c3b7b47d6d7c16b7be5d (atomic ledger/results publication)
**Ledger generation:** 543 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 6s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 627; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 609; valid market observations: 609; OHLC screened: 17.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | XRP/USD | 0.98602 | 73.764 | 56.675 | +0.36% | +0.42% | 2.72x | 1.6 | 2026-11-18T05:30:03.501770+00:00 | Not calibrated | STRONG 92/100 | HIGH 55/100 | Consider small entry | WATCH |
| 2 | UP/USD | 0.05504 | 71.069 | 56.614 | +3.87% | -0.11% | 3.04x | 5.5 | 2026-11-18T05:30:03.501770+00:00 | Not calibrated | MODERATE 66/100 | HIGH 66/100 | Watch | WATCH |
| 3 | SENT/USD | 0.01956 | 60.769 | 61.320 | +4.77% | +0.27% | 0.81x | 6.1 | 2026-11-18T05:30:03.501770+00:00 | Not calibrated | MODERATE 60/100 | VERY_HIGH 74/100 | Watch | WATCH |
| 4 | SOL/USD | 75.35 | 60.191 | 56.667 | +0.33% | +0.39% | 1.16x | 1.3 | 2026-11-18T05:30:03.501770+00:00 | Not calibrated | MODERATE 65/100 | HIGH 62/100 | Watch | WATCH |
| 5 | CC/USD | 0.08407 | 48.256 | 47.913 | +2.36% | +0.49% | 0.79x | 8.3 | 2026-11-18T05:30:03.501770+00:00 | Not calibrated | MODERATE 54/100 | HIGH 67/100 | Watch | WATCH |
| 6 | XDC/USD | 0.03078 | 37.527 | 45.191 | +1.52% | +0.07% | 0.20x | 6.5 | 2026-11-18T05:30:03.501770+00:00 | Not calibrated | WEAK 39/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 7 | MNT/USD | 0.3766 | 35.850 | 35.051 | +0.88% | +0.75% | 0.71x | 8.0 | 2026-11-18T05:30:03.501770+00:00 | Not calibrated | MODERATE 48/100 | VERY_HIGH 75/100 | Watch | WATCH |
| 8 | PEARL/USD | 1.8399 | 33.490 | 36.674 | +1.62% | +0.38% | 0.49x | 19.0 | 2026-11-18T05:30:03.501770+00:00 | Not calibrated | WEAK 42/100 | VERY_HIGH 81/100 | Watch | WATCH |
| 9 | MELANIA/USD | 0.0495 | 17.526 | 22.103 | +1.64% | -0.80% | 0.94x | 40.4 | 2026-11-18T05:30:03.501770+00:00 | Not calibrated | WEAK 0/100 | EXTREME 100/100 | Do nothing | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | SENT/USD | 61.320 | 0.01956 | +0.27% | 0.81x |
| 2 | XRP/USD | 56.675 | 0.98602 | +0.42% | 2.72x |
| 3 | SOL/USD | 56.667 | 75.35 | +0.39% | 1.16x |
| 4 | UP/USD | 56.614 | 0.05504 | -0.11% | 3.04x |
| 5 | CC/USD | 47.913 | 0.08407 | +0.49% | 0.79x |
| 6 | XDC/USD | 45.191 | 0.03078 | +0.07% | 0.20x |
| 7 | PEARL/USD | 36.674 | 1.8399 | +0.38% | 0.49x |
| 8 | MNT/USD | 35.051 | 0.3766 | +0.75% | 0.71x |
| 9 | MELANIA/USD | 22.103 | 0.0495 | -0.80% | 0.94x |

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

- Persisted scans: 543; predictions: 4584; observations: 327694.
- Matured sampled outcomes across 1/6/24/48h: 3728; gap abstentions: 12463. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 0 (sampled only; not a success-rate estimate).
- False positives / missed movers: NOT VERIFIED without eligible continuous outcome coverage.
- Baseline vs challenger: recorded as-of; unbiased held-out lift NOT MEASURED.
- Online Kraken /USD stablecoin-base pairs excluded: 18 (counted from this scan's online AssetPairs metadata, not inferred from price).
- Stablecoin base exclusions: BRL1, BUSD, DAI, EUR, EURC, EUROP, EURQ, EURR, EURT, FDUSD, FRAX, GUSD, PYUSD, QCAD, RLUSD, TGBP, TUSD, USD, USD1, USDC, USDD, USDE, USDG, USDQ, USDR, USDS, USDT, ZUSD.
- DEX: NOT USED; no DEX freshness gate.
- OHLC screening abstentions: 8; details in immutable scan JSON artifact.
- Storage: ledger and results published in one non-force Git commit and read back. Independent artifact recovery is NOT VERIFIED by this scan alone.
- Errors: none in successful committed scan; a failed workflow must not publish a SUCCESS report.

# Cryptoscanner — challenger and independent legacy-inspired WATCH

Paper only · risk is high or higher · 30%+ in 48h probability NOT CALIBRATED
Signal confidence 0–100 means setup strength only, NOT a win probability. Actions are research guidance; no trade authorization.

**Writer:** 44244615566 · **Generation:** 543 · **Legacy run:** 44244615566
**Main quote time:** 2026-11-18T05:30:09.548915+00:00 · **Legacy report time:** 2026-11-18T05:30:31.451860+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | XRP/USD ⭐ | 0.98602 | 73.76 | +0.42% | 2.72x | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 2 | UP/USD | 0.05504 | 71.07 | -0.11% | 3.04x | MODERATE 66/100 | HIGH 66/100 | Watch |
| 3 | SENT/USD | 0.01956 | 60.77 | +0.27% | 0.81x | MODERATE 60/100 | VERY_HIGH 74/100 | Watch |
| 4 | SOL/USD ⭐ | 75.35 | 60.19 | +0.39% | 1.16x | STRONG 75/100 | HIGH 62/100 | Watch |
| 5 | CC/USD | 0.08407 | 48.26 | +0.49% | 0.79x | MODERATE 54/100 | HIGH 67/100 | Watch |
| 6 | XDC/USD | 0.03078 | 37.53 | +0.07% | 0.20x | WEAK 39/100 | VERY_HIGH 70/100 | Watch |
| 7 | MNT/USD | 0.3766 | 35.85 | +0.75% | 0.71x | MODERATE 48/100 | VERY_HIGH 75/100 | Watch |
| 8 | PEARL/USD | 1.8399 | 33.49 | +0.38% | 0.49x | WEAK 42/100 | VERY_HIGH 81/100 | Watch |
| 9 | MELANIA/USD | 0.0495 | 17.53 | -0.80% | 0.94x | WEAK 0/100 | EXTREME 100/100 | Do nothing |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | XRP/USD ⭐ | 0.98667 | 65.00 | +0.42% | 2.72x | 32016 | STRONG 97/100 | HIGH 55/100 | Consider small entry |
| 2 | SOL/USD ⭐ | 75.37 | 55.46 | +0.39% | 1.16x | 38229 | STRONG 73/100 | HIGH 62/100 | Watch |
| 3 | NEAR/USD | 3.3985 | 47.43 | +0.69% | 1.33x | 15751 | MODERATE 69/100 | HIGH 55/100 | Watch |

**Same-run overlap:** XRP/USD, SOL/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
