# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-23T05:51:38.870492+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/45120179921
**Source SHA:** 858c8bc8ec5d7641ddb39cacd8aca91719f855b1
**Previous ledger commit:** 9778c94ade19b0c2c5e0f2dc322e61b86f8faba6 (atomic ledger/results publication)
**Ledger generation:** 1389 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 8s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 628; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 610; valid market observations: 609; OHLC screened: 24.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | JUP/USD | 0.23953 | 94.085 | 75.637 | +6.66% | +1.30% | 2.19x | 7.1 | 2026-11-23T05:51:30.478506+00:00 | Not calibrated | STRONG 100/100 | HIGH 60/100 | Consider small entry | WATCH |
| 2 | AI/USD | 0.01619 | 91.332 | 69.802 | +10.74% | +1.31% | 14.78x | 12.5 | 2026-11-23T05:51:30.478506+00:00 | Not calibrated | STRONG 96/100 | VERY_HIGH 73/100 | Watch | WATCH |
| 3 | SOL/USD | 71.84 | 83.810 | 66.296 | +1.71% | +0.50% | 3.92x | 1.4 | 2026-11-23T05:51:30.478506+00:00 | Not calibrated | STRONG 97/100 | HIGH 55/100 | Consider small entry | WATCH |
| 4 | XMR/USD | 503.09 | 80.481 | 64.819 | +1.90% | +0.25% | 2.44x | 7.0 | 2026-11-23T05:51:30.478506+00:00 | Not calibrated | STRONG 95/100 | HIGH 55/100 | Consider small entry | WATCH |
| 5 | XRP/USD | 0.93801 | 80.058 | 62.848 | +1.13% | +0.44% | 4.41x | 0.1 | 2026-11-23T05:51:30.478506+00:00 | Not calibrated | STRONG 95/100 | HIGH 55/100 | Consider small entry | WATCH |
| 6 | SUI/USD | 0.6645 | 79.300 | 62.890 | +1.34% | +0.50% | 2.39x | 3.0 | 2026-11-23T05:51:30.478506+00:00 | Not calibrated | STRONG 95/100 | HIGH 55/100 | Consider small entry | WATCH |
| 7 | XBT/USD | 61604.3 | 76.517 | 59.961 | +0.71% | +0.31% | 4.03x | 0.0 | 2026-11-23T05:51:30.478506+00:00 | Not calibrated | STRONG 93/100 | HIGH 55/100 | Consider small entry | WATCH |
| 8 | NEAR/USD | 3.018 | 74.503 | 61.534 | +1.22% | -0.41% | 5.85x | 4.0 | 2026-11-23T05:51:30.478506+00:00 | Not calibrated | MODERATE 67/100 | HIGH 61/100 | Watch | WATCH |
| 9 | NIGHT/USD | 0.05014 | 66.672 | 59.643 | +1.97% | +0.32% | 1.54x | 10.0 | 2026-11-23T05:51:30.478506+00:00 | Not calibrated | STRONG 78/100 | HIGH 55/100 | Watch | WATCH |
| 10 | PAXG/USD | 3609.21 | 66.043 | 51.458 | +1.04% | +0.23% | 2.34x | 0.4 | 2026-11-23T05:51:30.478506+00:00 | Not calibrated | STRONG 88/100 | HIGH 55/100 | Watch | WATCH |
| 11 | ETH/USD | 1729.97 | 64.598 | 57.706 | +0.49% | +0.15% | 1.61x | 1.4 | 2026-11-23T05:51:30.478506+00:00 | Not calibrated | MODERATE 67/100 | HIGH 55/100 | Watch | WATCH |
| 12 | XLM/USD | 0.128114 | 62.067 | 55.415 | +0.46% | +0.48% | 1.43x | 3.3 | 2026-11-23T05:51:30.478506+00:00 | Not calibrated | STRONG 76/100 | HIGH 55/100 | Watch | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | JUP/USD | 75.637 | 0.23953 | +1.30% | 2.19x |
| 2 | AI/USD | 69.802 | 0.01619 | +1.31% | 14.78x |
| 3 | SOL/USD | 66.296 | 71.84 | +0.50% | 3.92x |
| 4 | XMR/USD | 64.819 | 503.09 | +0.25% | 2.44x |
| 5 | SUI/USD | 62.890 | 0.6645 | +0.50% | 2.39x |
| 6 | XRP/USD | 62.848 | 0.93801 | +0.44% | 4.41x |
| 7 | NEAR/USD | 61.534 | 3.018 | -0.41% | 5.85x |
| 8 | XBT/USD | 59.961 | 61604.3 | +0.31% | 4.03x |
| 9 | NIGHT/USD | 59.643 | 0.05014 | +0.32% | 1.54x |
| 10 | ETH/USD | 57.706 | 1729.97 | +0.15% | 1.61x |
| 11 | XLM/USD | 55.415 | 0.128114 | +0.48% | 1.43x |
| 12 | PAXG/USD | 51.458 | 3609.21 | +0.23% | 2.34x |

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

- Persisted scans: 1389; predictions: 11435; observations: 841005.
- Matured sampled outcomes across 1/6/24/48h: 18552; gap abstentions: 22370. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 114 (sampled only; not a success-rate estimate).
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

**Writer:** 45120179921 · **Generation:** 1389 · **Legacy run:** 45120179921
**Main quote time:** 2026-11-23T05:51:38.870492+00:00 · **Legacy report time:** 2026-11-23T05:52:39.300048+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | JUP/USD ⭐ | 0.23953 | 94.09 | +1.30% | 2.19x | STRONG 100/100 | HIGH 60/100 | Consider small entry |
| 2 | AI/USD ⭐ | 0.01619 | 91.33 | +1.31% | 14.78x | STRONG 100/100 | VERY_HIGH 73/100 | Watch |
| 3 | SOL/USD ⭐ | 71.84 | 83.81 | +0.50% | 3.92x | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 4 | XMR/USD ⭐ | 503.09 | 80.48 | +0.25% | 2.44x | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 5 | XRP/USD ⭐ | 0.93801 | 80.06 | +0.44% | 4.41x | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 6 | SUI/USD ⭐ | 0.6645 | 79.30 | +0.50% | 2.39x | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 7 | XBT/USD ⭐ | 61604.3 | 76.52 | +0.31% | 4.03x | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 8 | NEAR/USD | 3.018 | 74.50 | -0.41% | 5.85x | MODERATE 67/100 | HIGH 61/100 | Watch |
| 9 | NIGHT/USD ⭐ | 0.05014 | 66.67 | +0.32% | 1.54x | STRONG 88/100 | HIGH 55/100 | Consider small entry |
| 10 | PAXG/USD ⭐ | 3609.21 | 66.04 | +0.23% | 2.34x | STRONG 98/100 | HIGH 55/100 | Consider small entry |
| 11 | ETH/USD | 1729.97 | 64.60 | +0.15% | 1.61x | MODERATE 67/100 | HIGH 55/100 | Watch |
| 12 | XLM/USD | 0.128114 | 62.07 | +0.48% | 1.43x | STRONG 76/100 | HIGH 55/100 | Watch |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | AI/USD ⭐ | 0.01619 | 82.54 | +1.31% | 14.78x | 3445 | STRONG 100/100 | VERY_HIGH 73/100 | Watch |
| 2 | JUP/USD ⭐ | 0.23996 | 81.24 | +1.30% | 2.19x | 3064 | STRONG 100/100 | HIGH 60/100 | Consider small entry |
| 3 | SOL/USD ⭐ | 71.87 | 79.79 | +0.50% | 3.92x | 29932 | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 4 | XRP/USD ⭐ | 0.93861 | 73.94 | +0.44% | 4.41x | 20189 | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 5 | XBT/USD ⭐ | 61666.4 | 70.64 | +0.31% | 4.03x | 134807 | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 6 | SUI/USD ⭐ | 0.6649 | 69.88 | +0.50% | 2.39x | 6374 | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 7 | XMR/USD ⭐ | 503.17 | 67.19 | +0.25% | 2.44x | 8481 | STRONG 99/100 | HIGH 55/100 | Consider small entry |
| 8 | NIGHT/USD ⭐ | 0.05024 | 63.76 | +0.32% | 1.54x | 10939 | STRONG 82/100 | HIGH 61/100 | Consider small entry |
| 9 | PAXG/USD ⭐ | 3611.03 | 63.70 | +0.23% | 2.34x | 6980 | STRONG 97/100 | HIGH 55/100 | Consider small entry |

**Same-run overlap:** JUP/USD, AI/USD, SOL/USD, XMR/USD, XRP/USD, SUI/USD, XBT/USD, NIGHT/USD, PAXG/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
