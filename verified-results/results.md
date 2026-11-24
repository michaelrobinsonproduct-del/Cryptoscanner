# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-24T05:51:30.715262+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/45336008920
**Source SHA:** 858c8bc8ec5d7641ddb39cacd8aca91719f855b1
**Previous ledger commit:** 9643a23647f82de0c1cd5a8cb3eaa9b2ca065f87 (atomic ledger/results publication)
**Ledger generation:** 1533 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 6s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 628; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 610; valid market observations: 609; OHLC screened: 24.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | PEPE/USD | 3.595e-06 | 90.963 | 81.646 | +5.06% | +0.17% | 1.85x | 8.3 | 2026-11-24T05:51:24.306046+00:00 | Not calibrated | STRONG 80/100 | HIGH 55/100 | Watch | WATCH |
| 2 | NEAR/USD | 3.0485 | 88.081 | 70.311 | +2.26% | +0.55% | 3.70x | 1.0 | 2026-11-24T05:51:24.306046+00:00 | Not calibrated | STRONG 99/100 | HIGH 55/100 | Consider small entry | WATCH |
| 3 | ICNT/USD | 0.3303 | 81.232 | 68.284 | +6.86% | +2.93% | 0.83x | 18.2 | 2026-11-24T05:51:24.306046+00:00 | Not calibrated | MODERATE 66/100 | VERY_HIGH 73/100 | Watch | WATCH |
| 4 | HYPE/USD | 64.37 | 77.876 | 62.253 | +1.15% | +0.12% | 5.09x | 1.6 | 2026-11-24T05:51:24.306046+00:00 | Not calibrated | STRONG 84/100 | HIGH 55/100 | Watch | WATCH |
| 5 | XRP/USD | 0.95562 | 72.690 | 65.996 | +1.73% | +0.02% | 1.66x | 2.2 | 2026-11-24T05:51:24.306046+00:00 | Not calibrated | STRONG 71/100 | HIGH 55/100 | Watch | WATCH |
| 6 | VVV/USD | 25.145 | 68.235 | 72.570 | +2.85% | -0.32% | 0.73x | 4.8 | 2026-11-24T05:51:24.306046+00:00 | Not calibrated | WEAK 39/100 | VERY_HIGH 76/100 | Watch | WATCH |
| 7 | XMR/USD | 494.62 | 68.059 | 63.137 | +1.77% | +0.26% | 1.36x | 8.5 | 2026-11-24T05:51:24.306046+00:00 | Not calibrated | STRONG 79/100 | HIGH 55/100 | Watch | WATCH |
| 8 | ADA/USD | 0.149501 | 63.746 | 58.532 | +0.71% | +0.19% | 1.42x | 2.9 | 2026-11-24T05:51:24.306046+00:00 | Not calibrated | MODERATE 67/100 | HIGH 55/100 | Watch | WATCH |
| 9 | LTC/USD | 41.87 | 63.211 | 61.412 | +1.09% | +0.02% | 1.17x | 2.4 | 2026-11-24T05:51:24.306046+00:00 | Not calibrated | MODERATE 57/100 | HIGH 62/100 | Watch | WATCH |
| 10 | XDC/USD | 0.02712 | 59.581 | 63.151 | +4.39% | +0.74% | 0.27x | 7.4 | 2026-11-24T05:51:24.306046+00:00 | Not calibrated | MODERATE 60/100 | VERY_HIGH 75/100 | Watch | WATCH |
| 11 | AVAX/USD | 6.836 | 59.398 | 50.640 | +0.87% | +0.13% | 1.81x | 2.9 | 2026-11-24T05:51:24.306046+00:00 | Not calibrated | MODERATE 65/100 | HIGH 55/100 | Watch | WATCH |
| 12 | XDG/USD | 0.0567582 | 59.161 | 60.193 | +0.80% | +0.18% | 0.81x | 0.9 | 2026-11-24T05:51:24.306046+00:00 | Not calibrated | MODERATE 50/100 | HIGH 62/100 | Watch | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | PEPE/USD | 81.646 | 3.595e-06 | +0.17% | 1.85x |
| 2 | VVV/USD | 72.570 | 25.145 | -0.32% | 0.73x |
| 3 | NEAR/USD | 70.311 | 3.0485 | +0.55% | 3.70x |
| 4 | ICNT/USD | 68.284 | 0.3303 | +2.93% | 0.83x |
| 5 | XRP/USD | 65.996 | 0.95562 | +0.02% | 1.66x |
| 6 | XDC/USD | 63.151 | 0.02712 | +0.74% | 0.27x |
| 7 | XMR/USD | 63.137 | 494.62 | +0.26% | 1.36x |
| 8 | HYPE/USD | 62.253 | 64.37 | +0.12% | 5.09x |
| 9 | LTC/USD | 61.412 | 41.87 | +0.02% | 1.17x |
| 10 | XDG/USD | 60.193 | 0.0567582 | +0.18% | 0.81x |
| 11 | ADA/USD | 58.532 | 0.149501 | +0.19% | 1.42x |
| 12 | AVAX/USD | 50.640 | 6.836 | +0.13% | 1.81x |

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

- Persisted scans: 1533; predictions: 13129; observations: 928695.
- Matured sampled outcomes across 1/6/24/48h: 24602; gap abstentions: 22370. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 136 (sampled only; not a success-rate estimate).
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

**Writer:** 45336008920 · **Generation:** 1533 · **Legacy run:** 45336008920
**Main quote time:** 2026-11-24T05:51:30.715262+00:00 · **Legacy report time:** 2026-11-24T05:52:40.099424+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | PEPE/USD ⭐ | 3.595e-06 | 90.96 | +0.17% | 1.85x | STRONG 90/100 | HIGH 55/100 | Watch |
| 2 | NEAR/USD ⭐ | 3.0485 | 88.08 | +0.55% | 3.70x | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 3 | ICNT/USD | 0.3303 | 81.23 | +2.93% | 0.83x | MODERATE 66/100 | VERY_HIGH 73/100 | Watch |
| 4 | HYPE/USD | 64.37 | 77.88 | +0.12% | 5.09x | STRONG 84/100 | HIGH 55/100 | Watch |
| 5 | XRP/USD | 0.95562 | 72.69 | +0.02% | 1.66x | STRONG 71/100 | HIGH 55/100 | Watch |
| 6 | VVV/USD | 25.145 | 68.23 | -0.32% | 0.73x | WEAK 39/100 | VERY_HIGH 76/100 | Watch |
| 7 | XMR/USD | 494.62 | 68.06 | +0.26% | 1.36x | STRONG 79/100 | HIGH 55/100 | Watch |
| 8 | ADA/USD | 0.149501 | 63.75 | +0.19% | 1.42x | MODERATE 67/100 | HIGH 55/100 | Watch |
| 9 | LTC/USD | 41.87 | 63.21 | +0.02% | 1.17x | MODERATE 57/100 | HIGH 62/100 | Watch |
| 10 | XDC/USD | 0.02712 | 59.58 | +0.74% | 0.27x | MODERATE 60/100 | VERY_HIGH 75/100 | Watch |
| 11 | AVAX/USD | 6.836 | 59.40 | +0.13% | 1.81x | MODERATE 65/100 | HIGH 55/100 | Watch |
| 12 | XDG/USD | 0.0567582 | 59.16 | +0.18% | 0.81x | MODERATE 50/100 | HIGH 62/100 | Watch |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | PEPE/USD ⭐ | 3.598e-06 | 90.04 | +0.17% | 1.85x | 9192 | STRONG 90/100 | HIGH 55/100 | Watch |
| 2 | NEAR/USD ⭐ | 3.0488 | 82.32 | +0.55% | 3.70x | 23286 | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 3 | BAT/USD | 0.08099 | 74.66 | +0.20% | 1.73x | 3159 | MODERATE 62/100 | VERY_HIGH 72/100 | Watch |

**Same-run overlap:** PEPE/USD, NEAR/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
